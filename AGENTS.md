# Repository instructions

## Purpose

Maintain ITWYW, an English-language agent skill that helps beginners identify frontend, backend, and infrastructure features from everyday descriptions. Responses produced by the skill follow the user's language preference. Keep the English, Korean, Japanese, and Traditional Chinese README files aligned.

## Branches, reviews, and merges

- Treat `main` as the owner's release branch. After initial repository setup, work on a separate branch and open a pull request.
- Creating or updating files, committing, pushing a working branch, or opening a draft pull request is not permission to merge.
- **Do not merge a pull request, enable auto-merge, add it to a merge queue, or push directly to `main` without the owner's explicit authorization for that specific action.**
- Do not approve your own changes or submit an approval using the owner's identity to satisfy a human-review requirement.
- The sole required reviewer and code owner is `@HHC225`. Preserve `* @HHC225` as the only CODEOWNERS rule and require code-owner approval. Do not add another reviewer or disable that requirement to resolve an author/reviewer identity conflict.
- Do not bypass, disable, weaken, or delete branch protections, rulesets, required reviews, or required status checks to finish a task. A failed protection check is a blocker to report.
- Never force-push a protected branch, delete it, or rewrite published history without separate explicit authorization.
- Preserve the owner's existing work and settings. Do not expand app permissions or create credentials as a workaround.
- A statement such as "build it," "fix it," or "push your changes" does not authorize a later merge unless the owner explicitly says to merge that PR or branch.

These instructions guide cooperating agents. GitHub rules enforce repository access separately; do not claim these instructions alone make unauthorized merging impossible.

## Content requirements

- Keep the runtime skill and all reference Markdown in English.
- Keep the three-candidate maximum for identifying one ambiguous request, while allowing one confident match and a single observation question for under-specified goals.
- Explain behavior using familiar words and retain the conventional English feature name.
- Use confirmed context. A screenshot does not prove dynamic behavior, persistence, access enforcement, or infrastructure.
- Cite primary sources in catalogue entries and preserve provider-specific limitations.
- Keep common design labels distinct from standardized semantics and features distinct from implementation choices.
- Keep references selective and discoverable from `skills/itwyw/SKILL.md`.
- Do not add generated images, runtime dependencies, vendor recommendations, or implementation code to the skill unless requested.

## Verification

Run `python3 scripts/validate.py` after editing the skill or documentation. For behavioral changes, use relevant fresh-context scenarios from `evals/scenarios.md`; keep expected answers out of the agent's input. Report actual outputs and remaining limitations. Update coverage totals and all four README files when catalogue counts change.
