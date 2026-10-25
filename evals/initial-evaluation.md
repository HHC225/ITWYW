# Initial evaluation

Date: **2026-10-25**. Scope: the initial ITWYW skill and reference set in this repository.

## Method

Six independent user prompts were first answered without ITWYW. The answers generally found sensible terms but did not consistently finish with a confirmation. The generic popup case also moved toward a modal example without evidence that a modal was intended.

Fresh agents then received the skill path and raw requests, with no expected answers or reviewer diagnoses. Three independent batches covered eleven scenarios. Each scenario within a batch was presented as a separate conversation. Review was manual against the requested behavior; this was not an automated comprehension or accuracy benchmark.

## Observed outcomes

| Scenario | Observation |
| --- | --- |
| Korean description of a panel sliding in from the side | Named drawer/side panel, gave a short sequence, asked whether that edge-opening behavior matched. |
| Korean request to create one order after two quick presses | Explained duplicate-order prevention and idempotency in plain language, illustrated one result for the same request, and confirmed intent. |
| Broad Korean request for a faster site | Asked which moment was slow; did not prescribe a technology. |
| Japanese question with an explicit English request | Answered in English, distinguished fixed and sticky behavior, and asked one choice question. |
| Traditional Chinese collaborative editing request | Answered in Traditional Chinese, named collaborative editing, and noted concurrent-change rules without prescribing a transport. |
| English generic popup request | Offered three behavior-distinct candidates and one choice question; did not force a single interpretation. |
| Korean selection of a previously offered popover, with name-only instruction | Returned the selected name in Korean/English without repeating confirmation. |
| Recovery of yesterday's saved data after deletion | Named backup/restore, illustrated recovery, and briefly explained the effect of restoring an older copy. |
| Loading more cards and fading them in one by one | Treated infinite scroll and staggered fade-in as cooperating parts, not mutually exclusive options. |
| Explicit request for no questions about a brief Saved message | Named toast notification, stated the assumption, and respected the no-question instruction. |
| Korean belief that hiding a menu blocks direct URLs | Corrected the misconception, named enforced authorization, and asked whether access was for all members or only administrators. |

All eleven sampled responses met the relevant observed criteria. This limited sample does not establish behavior on every language, screenshot, custom product, or ambiguous request. A still-image interaction scenario and repeated adversarial phrasing were not behaviorally exercised in this initial run.

## Structural verification

- The skill-creator frontmatter validator accepted `skills/itwyw`.
- The offline repository validator found ten catalogues, 296 mapping entries, 592 example phrases, 255 source entries, 254 distinct source URLs, and fifteen reference Markdown files.
- All catalogue source keys resolved, IDs were unique, local Markdown file links existed, and reference files were discoverable directly from `SKILL.md`.
- English, Korean, Japanese, and Traditional Chinese READMEs contained matching coverage numbers and link destinations.
- Deliberately broken temporary fixtures confirmed that the validator rejects a missing reference link and a duplicate concept ID.

The structural validator checks file paths and source-key integrity; it does not fetch every external URL or prove that a linked page supports every word of a mapping. Research and semantic review remain separate tasks.

## Independent content review

A separate reviewer read the complete runtime skill, fifteen references, four README translations, validator, workflow, and proposed protection configuration. Two minor issues were found and corrected: the responsive-layout routing link now points to its actual catalogue, and the dropdown comparison explicitly distinguishes editable and select-only comboboxes. The review found no publication blocker and no claim that the proposed ruleset was already active. Live settings and all external URLs were outside that static review's verification scope.

A final reference-navigation check also added FE-113 (list virtualization), so the existing large-list routing entry now resolves to a concrete sourced mapping. Coverage totals above describe the final validated package.
