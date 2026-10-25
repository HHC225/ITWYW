#!/usr/bin/env python3
"""Validate ITWYW's distributable structure and local documentation offline."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


def validate(root: Path) -> tuple[list[str], dict[str, object]]:
    errors: list[str] = []
    skill = root / "skills" / "itwyw"
    main = skill / "SKILL.md"
    if not main.is_file():
        return ["Missing skills/itwyw/SKILL.md"], {}
    text = main.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not frontmatter:
        errors.append("SKILL.md must begin with YAML frontmatter.")
    else:
        fields = {}
        for line in frontmatter.group(1).splitlines():
            key, sep, value = line.partition(":")
            if sep:
                fields[key.strip()] = value.strip()
        if set(fields) != {"name", "description"}:
            errors.append("SKILL.md frontmatter must contain name and description only.")
        if fields.get("name") != "itwyw":
            errors.append("Skill name must match its itwyw directory.")
        if not fields.get("description") or len(fields["description"]) > 1024:
            errors.append("Skill description must contain 1–1024 characters.")

    metadata = skill / "agents" / "openai.yaml"
    if not metadata.is_file() or "$itwyw" not in metadata.read_text(encoding="utf-8"):
        errors.append("Agent metadata must include an invocation of $itwyw.")

    markdown_files = sorted(root.rglob("*.md"))
    link_pattern = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)")
    for path in markdown_files:
        if ".git" in path.parts:
            continue
        body = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(body):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            destination = (path.parent / unquote(parts.path)).resolve()
            if not destination.exists():
                errors.append(f"{path.relative_to(root)}: missing link target {target}")
            if path.is_relative_to(skill) and not destination.is_relative_to(skill.resolve()):
                errors.append(f"{path.relative_to(root)}: runtime link escapes the installable skill folder: {target}")

    counts: Counter[str] = Counter()
    ids: list[str] = []
    source_urls: list[str] = []
    phrase_count = 0
    catalogues = []
    for path in sorted((skill / "references").glob("*.md")):
        body = path.read_text(encoding="utf-8")
        if re.search(r"[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]", body):
            errors.append(f"{path.name}: runtime references should be written in English.")
        if not path.name.startswith(("frontend-", "backend-", "infra-")):
            continue
        catalogues.append(path.name)
        definitions = set()
        for match in re.finditer(
            r"^(?:\|\s*([A-Z][A-Z0-9-]+)\s*\||-\s+\*\*([A-Z][A-Z0-9-]+)\*\*|\[([A-Z][A-Z0-9-]+)\]:)",
            body,
            re.M,
        ):
            definitions.add(next(group for group in match.groups() if group))
        for line in body.splitlines():
            if not re.match(r"^\|\s*(?:FE|BE|INF)-[^ |]+\s*\|", line):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 6:
                errors.append(f"{path.name}: expected six columns: {line[:80]}")
                continue
            identifier, _, phrases, explanation, cue, sources = cells
            ids.append(identifier)
            counts[path.name.split("-", 1)[0]] += 1
            if len(phrases.split(" / ")) != 2:
                errors.append(f"{identifier}: expected two everyday-language phrases.")
            phrase_count += len(phrases.split(" / "))
            if not explanation or not cue:
                errors.append(f"{identifier}: explanation and distinguishing cue are required.")
            keys = re.findall(r"[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*", sources)
            if not keys or any(key not in definitions for key in keys):
                errors.append(f"{identifier}: unresolved source keys {sources}")
        source_urls.extend(re.findall(r"https://[^\s)>|]+", body))

    duplicate_ids = [identifier for identifier, count in Counter(ids).items() if count > 1]
    if duplicate_ids:
        errors.append(f"Duplicate concept IDs: {', '.join(duplicate_ids)}")
    if len(catalogues) != 10:
        errors.append(f"Expected ten domain catalogues; found {len(catalogues)}.")
    for path in (skill / "references").glob("*.md"):
        if f"references/{path.name}" not in text:
            errors.append(f"{path.name} is not directly discoverable from SKILL.md.")

    total = sum(counts.values())
    numbers = [*counts.values(), total, phrase_count, len(source_urls), len(set(source_urls))]
    for name in ("README.md", "README.ko.md", "README.ja.md", "README.zh-TW.md"):
        path = root / name
        if not path.is_file():
            errors.append(f"Missing {name}")
            continue
        body = path.read_text(encoding="utf-8")
        for number in numbers:
            if not re.search(rf"(?<!\d){number}(?!\d)", body):
                errors.append(f"{name}: coverage number {number} is missing or stale.")

    rules_file = root / ".github" / "rulesets" / "main.json"
    if rules_file.is_file():
        try:
            rules = json.loads(rules_file.read_text(encoding="utf-8"))
            expected_bypass = [{"actor_id": 237215883, "actor_type": "User", "bypass_mode": "pull_request"}]
            if rules.get("bypass_actors") != expected_bypass:
                errors.append("Ruleset bypass must be limited to HHC225's individual account and pull requests only.")
            if rules.get("target") != "branch":
                errors.append("Proposed ruleset must target branches.")
            pr_rules = [rule for rule in rules.get("rules", []) if rule.get("type") == "pull_request"]
            if len(pr_rules) != 1 or pr_rules[0].get("parameters", {}).get("require_code_owner_review") is not True:
                errors.append("Proposed ruleset must require the sole code owner's review.")
            elif pr_rules[0].get("parameters", {}).get("required_approving_review_count") != 1:
                errors.append("Proposed ruleset must require one approving review from the sole code owner.")
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid ruleset JSON: {exc}")
    else:
        errors.append("Missing proposed ruleset .github/rulesets/main.json.")

    owners_file = root / ".github" / "CODEOWNERS"
    if not owners_file.is_file():
        errors.append("Missing .github/CODEOWNERS.")
    else:
        owner_rules = [
            line.split()
            for line in owners_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        if owner_rules != [["*", "@HHC225"]]:
            errors.append("CODEOWNERS must designate only @HHC225 for every path.")

    summary = {
        "catalogues": len(catalogues),
        "mapping_entries": total,
        "by_area": dict(sorted(counts.items())),
        "example_phrases": phrase_count,
        "source_entries": len(source_urls),
        "distinct_source_urls": len(set(source_urls)),
        "reference_files": len(list((skill / "references").glob("*.md"))),
    }
    return errors, summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, summary = validate(args.root.resolve())
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    for error in errors:
        print(f"ERROR: {error}")
    print(f"{'FAIL' if errors else 'PASS'}: offline structural validation")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
