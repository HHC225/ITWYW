# ITWYW

### Is This What You Want?

[English](README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [繁體中文](README.zh-TW.md)

**Describe the feature in your own words. Get its name, a simple explanation, and a quick check that it is what you meant.**

ITWYW is an AI agent skill for people who know what they want an app to do but do not know the development term. It supports frontend interactions, backend behavior, and infrastructure needs. It is especially useful for beginners and people building with AI through natural-language instructions.

> “When I press the button, something should slide in from the right.”
>
> **Drawer (side panel):** a panel opens from the edge to show more options.
>
> “Is a panel that opens from the right what you want?”

## What it does

- Identifies **one likely feature** when the behavior is clear.
- Offers **up to three candidates** when the description could mean different things.
- Explains each candidate in brief, everyday language that does not require development experience.
- Uses small before/after tables or text sequences when they make movement or hidden processing easier to understand. It does not require image generation.
- Asks **one easy confirmation question**, then carries the confirmed behavior forward.
- Responds in the user's language, or in a language they explicitly request. The skill and its reference material are written in English.
- Keeps implementation choices separate from feature identification. “Make it fast” does not automatically become a recommendation for a particular database, framework, or cloud service.

## Examples

| What a person might say | What ITWYW can help identify |
| --- | --- |
| “Tap a question and its answer opens underneath.” | Accordion or disclosure. |
| “A little box should pop up.” | Modal dialog, popover, or toast, depending on its behavior. |
| “The menu stays at the top while I scroll.” | Persistent header; distinguish fixed and sticky behavior when needed. |
| “Even if I press Buy twice, create one order.” | Duplicate-order prevention using idempotency. |
| “Only the person who owns the file can open it.” | Authorization and ownership checks. |
| “Work on the report while I keep using the page.” | Background job with status feedback. |
| “We should both be able to type in one document.” | Real-time collaborative editing. |
| “Bring the site back if the main server stops.” | Failover or recovery, depending on the acceptable interruption. |

These are example interpretations, not hardcoded phrase matches. The skill uses context and observable differences. A screenshot can show appearance; it cannot prove hidden server behavior or how an animation works.

### Showing a change

For a background task, an explanation can stay this small:

| You ask | While it works | When it finishes |
| --- | --- | --- |
| Export the report | Keep using the page | Download the report |

For ambiguous requests, the skill explains the difference between candidates instead of burying the user in a technical glossary. A static sequence illustrates motion; it is not presented as a running animation. Plain-text ASCII frames are a fallback when the host cannot render a clearer representation.

## Install

**Install only [skills/itwyw](skills/itwyw).** Keep its `SKILL.md`, `references/`, and `agents/` together. The repository's README files, evaluations, CI, and development scripts are not needed in your agent's skill directory.

### One command

Run this in the project where you want to use ITWYW, then choose your coding agent if prompted:

```bash
npx skills add HHC225/ITWYW --skill itwyw
```

The [Vercel Labs skills CLI](https://github.com/vercel-labs/skills) discovers the nested skill folder automatically. Its current release requires **Node.js 22.20+**; Git must also be available for this GitHub source.

To choose the agent directly:

```bash
# Codex
npx skills add HHC225/ITWYW --skill itwyw -a codex

# Claude Code
npx skills add HHC225/ITWYW --skill itwyw -a claude-code

# Both
npx skills add HHC225/ITWYW --skill itwyw -a codex claude-code
```

Add `-g` to install for all your projects. Add `--copy` if you prefer independent folders instead of links, and `-y` to skip the installer's questions.

### Clone and copy

For macOS, Linux, or Git Bash, run these from your own project directory:

```bash
git clone --depth 1 https://github.com/HHC225/ITWYW.git
mkdir -p .agents/skills
cp -R ITWYW/skills/itwyw .agents/skills/
```

Choose the destination for your agent:

| Agent or setup | This project | All your projects |
| --- | --- | --- |
| Codex / agents using the shared skills location | `.agents/skills/itwyw/` | `~/.agents/skills/itwyw/` |
| Claude Code | `.claude/skills/itwyw/` | `~/.claude/skills/itwyw/` |
| An existing Codex setup using its older user location | Use the current `.agents/skills/` location | `~/.codex/skills/itwyw/`, if your installation uses it |

For Claude Code, replace `.agents/skills` in the copy commands with `.claude/skills`. For a new Codex installation, use the documented `.agents/skills` location. Copy the **`itwyw` folder**, so the result is `<destination>/itwyw/SKILL.md`.

See [Installation details](docs/installation.md) for PowerShell, the older Codex user location, updates, and troubleshooting. Paths and invocation details follow the official [Codex](https://learn.chatgpt.com/docs/build-skills) and [Claude Code](https://code.claude.com/docs/en/skills) documentation.

### Use it

In Codex:

```text
$itwyw I want a little panel to slide out from the right when I tap the menu.
```

In Claude Code:

```text
/itwyw I want a little panel to slide out from the right when I tap the menu.
```

Or ask in your own language and name ITWYW explicitly. If the skill does not appear, restart the agent after installation.

The skill itself needs no application server, npm runtime dependency, API key, or image-generation service. Node.js and the CLI are needed only for the `npx` installation route; manual copying does not need Node.js. Browsing is useful when a requested term falls outside the references or needs current product-specific verification.

## Reference coverage

| Area | Mapping entries | Examples of coverage |
| --- | ---: | --- |
| Frontend | 113 | Layout, navigation, forms, tables, overlays, feedback, loading, visual effects, motion. |
| Backend | 99 | Data, search, identity, access, jobs, integrations, notifications, billing states, collaborative editing. |
| Infrastructure | 84 | Hosting, domains, networking, deployment, environments, monitoring, capacity, backup, recovery. |
| **Total** | **296** | **592 everyday-language example phrases.** |

The ten domain catalogues include **255 source entries covering 254 distinct primary-source URLs**, researched on **2026-10-25**. Sources include W3C, MDN, official design systems, PostgreSQL, OWASP, OpenID, Stripe, RabbitMQ, AWS, Microsoft, Google Cloud, Kubernetes, Docker, and OpenTelemetry.

The count is a count of mapping entries, not a claim that all labels are globally distinct across layers. The reference set remains open-ended. Ordinary phrases, short explanations, questions, and state sequences are original synthesis. Source limitations and conventional labels are stated explicitly.

See **[Sources and coverage](skills/itwyw/references/sources-and-coverage.md)** for the complete map, evidence scope, and coverage of all 24 patterns in the motivating frontend screenshot.

## How the files are organized

| File or directory | Purpose |
| --- | --- |
| `skills/itwyw/SKILL.md` | Matching workflow, response contract, language rules, confirmation and handoff. |
| `skills/itwyw/agents/openai.yaml` | Display metadata and the default invocation prompt. |
| `skills/itwyw/references/frontend-*.md` | Four frontend catalogues. |
| `skills/itwyw/references/backend-*.md` | Three backend catalogues. |
| `skills/itwyw/references/infra-*.md` | Three infrastructure catalogues. |
| `request-routing.md`, `ambiguity-guide.md` | Find the relevant concepts and distinguish similar behaviors. These files live in `references/`. |
| `motion-storyboards.md`, `conversation-examples.md` | Lightweight illustrations and complete conversation patterns, also in `references/`. |
| `evals/` | Behavioral scenarios and evaluation criteria for maintainers. |
| `scripts/validate.py` | Offline structural checks for the skill and repository documentation. |
| `AGENTS.md` | Repository instructions, including the explicit-approval merge policy. |

References load selectively. The skill does not require an agent to read every catalogue for every question.

## Contributing and validation

Preserve the beginner-facing explanation style, the three-candidate limit, language selection, and the distinction between confirmed facts and assumptions. Add a primary source and a distinguishing cue when adding a feature. Check all four README translations when public behavior changes.

Run the offline checks:

```bash
python3 scripts/validate.py
```

Then exercise the relevant scenarios in [evals/scenarios.md](evals/scenarios.md) with a fresh agent using the skill. Structural checks do not establish that a model will always understand every description.

## Merge policy

**Agents may prepare changes, push an authorized working branch, and open a draft pull request. They must not merge, enable auto-merge, bypass branch rules, or weaken review requirements without the owner's explicit approval for that specific action.**

Repository policy files guide cooperating agents. Actual enforcement requires active GitHub branch protection or rulesets. The proposed configuration and its limitations are documented in **[Repository protection](docs/repository-protection.md)**. This README does not claim that a checked-in policy file activates server-side protection.

**`@HHC225` is the sole code owner and required reviewer for other contributors' PRs.** Another person's review cannot replace the owner's approval. Only `@HHC225` has the personal bypass permission to merge a PR without review, including their own PRs. The bypass covers the whole ruleset, including required checks at PR merge, but does not apply to direct pushes. An agent using the owner's account shares that technical permission and must still obtain the owner's explicit instruction for the specific bypass or merge action.

## Limits

ITWYW helps establish a shared meaning before development. It is not an architecture approval, a security audit, a performance diagnosis, or a working implementation. It does not infer backend internals from a screenshot. It should keep confirmed intent, accept corrections, and stop asking the same question after the user has answered.
