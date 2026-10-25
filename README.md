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

## Use the skill

The distributable skill folder is **[skills/itwyw](skills/itwyw)**. Its entry point is **[SKILL.md](skills/itwyw/SKILL.md)**.

1. Clone or download this repository.
2. Copy the complete `skills/itwyw` folder, including `references/` and `agents/`, into a skill directory supported by your agent. Follow that host's installation instructions; discovery paths and invocation syntax differ.
3. Where named skill invocation is supported, ask:

   ```text
   Use $itwyw. I want a little panel to slide out from the right when I tap the menu.
   ```

   Or ask in your own language and name ITWYW explicitly.

No application server, runtime package, API key, or image-generation service is bundled or required by this skill. An agent capable of reading and following skills is required. Browsing is useful when a requested term falls outside the references or needs current product-specific verification.

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

## Limits

ITWYW helps establish a shared meaning before development. It is not an architecture approval, a security audit, a performance diagnosis, or a working implementation. It does not infer backend internals from a screenshot. It should keep confirmed intent, accept corrections, and stop asking the same question after the user has answered.
