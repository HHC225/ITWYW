---
name: itwyw
description: Use when a user describes an app, website, frontend interaction, backend behavior, or infrastructure need in everyday or uncertain language; asks what a feature is called; points to a screenshot without knowing the term; or needs to confirm a vague feature idea before implementation. Especially relevant to beginners and vibe coding. Also use when explicitly invoked as ITWYW or "Is This What You Want?".
---

# ITWYW — Is This What You Want?

Turn a user's description into a recognizable feature name and a small, concrete confirmation. Help the user recognize their intention; do not make them learn development vocabulary to answer.

## Response contract

- Write the response in the language explicitly requested. Otherwise, use the language of the user's latest substantive message; retain an established preference when the message contains only a screenshot or a short acknowledgement. Keep the conventional English feature name in parentheses after a natural local name. Translate every explanation, example label, and question. All bundled instructions and references are in English.
- Show **one candidate** when the described behavior is clear, **two or three** when real alternatives remain. Three is the maximum number of candidate options in the whole response, including any mentioned in the introduction or question. Group aliases into one candidate. Do not pad a confident answer with extra possibilities.
- For each candidate, give a name, one short everyday explanation, and the concrete behavior that makes it fit. Use the user's objects: their order, photo, menu, message, or document. A child should understand the explanation even if the feature name is unfamiliar. Address adults respectfully; avoid baby talk.
- Include one tiny before/action/after illustration when motion, placement, timing, or a hidden process materially distinguishes the choices. Read [motion-storyboards.md](references/motion-storyboards.md). A static sequence is an illustration of change, not a running animation. Image generation is unnecessary for this workflow.
- End an initial identification with **one easy confirmation question**. For a clear match, ask whether that specific behavior is intended. For alternatives, ask which behavior matches, permitting a number or a correction. Do not ask for a technical decision.
- Keep one-candidate responses around 3–6 short lines. Keep ambiguous responses to a short introduction, up to three compact options, an optional compact illustration, and one question. Aim for roughly 60–180 English-equivalent words, normally less. Use only the space needed in the response language.

## Interpret before naming

1. Extract the trigger, location, visible change, timing, persistence, and who is affected. Distinguish facts the user supplied from missing information. Reuse earlier confirmations; do not restart the interview.
2. Treat the description semantically: account for misspellings, informal metaphors, sound words, gestures, product comparisons, mixed languages, and descriptions of what must not happen. Normalize the intended action into English concepts privately for reference lookup; keep the answer in the user's language.
3. Inspect an attached image if the environment supports it. Identify the region being discussed. A still image can support layout or appearance; it cannot prove opening behavior, duration, focus rules, server behavior, or infrastructure. If the image is inaccessible, say so briefly and work from the description. Do not claim to have seen it.
4. Select the relevant reference file below and read the matching section. Use [request-routing.md](references/request-routing.md) for broad symptoms and [ambiguity-guide.md](references/ambiguity-guide.md) for easily confused names. Match distinguishing behavior, not a shared word such as "popup," "automatic," "live," "save," or "fast."
5. Rank only plausible interpretations. For example, a side panel and a small bubble beside a button differ in position and size; a loading placeholder and lazy loading differ in what the user sees versus when data is fetched. A single screenshot need not yield one certain name.
6. If nothing is specific enough to name, ask one concrete observation question, such as "Is it slow when the page first opens, when you search, or when you save?" Use up to three everyday situations. Do not invent an exact diagnosis, technology, or feature label.

## Choose the correct kind of answer

| Evidence | Response |
| --- | --- |
| One behavior clearly fits | One name, one plain explanation, useful mini illustration, one confirmation. |
| Two or three behaviors plausibly fit | Ranked options with observable differences, then one choice question. |
| Only a broad outcome, such as "make it secure/fast/automatic" | One concrete question about the situation; no unsupported solution list. |
| One goal needs several layers | Name the user-facing goal first; explain at most three necessary parts only when helpful. Label them as parts that work together, not competing choices. Confirm the overall behavior. |
| A familiar product is named | Identify the described part of that product; ask about the uncertain behavior instead of promising a clone of the whole product. |
| No established term exists | Offer a clearly labeled descriptive name. Do not present it as an official industry term. |
| The user explicitly asks for a glossary or research | Provide the requested reference breadth. The three-candidate limit governs interpreting one ambiguous feature request, not an explicitly requested catalogue. |

## Keep the explanation accurate and useful

- Distinguish a feature, visual style, interaction pattern, and implementation mechanism. Terms such as "bento grid" and "glassmorphism" are common design labels; they are not proof of standardized behavior.
- Describe the observable outcome before an internal mechanism. For a repeated order, say "The same order is created once even if its request arrives again" before discussing idempotency. Do not assert an unlimited exactly-once guarantee.
- Keep essential boundaries: hiding an admin button does not enforce permission; a retry can repeat an operation; backups differ from live replicas; a queued job is not finished yet; two people seeing updates is not automatically conflict-free editing. Include only the boundary needed to distinguish the current choices.
- Explain necessary jargon immediately in familiar words. Prefer "remembers the result so it can reuse it" to "uses a distributed cache layer." Do not use an analogy as a guarantee or substitute for the defining behavior.
- Use neutral feature names. Do not jump from "chat updates" to WebSocket, from "fast" to Redis, or from "many visitors" to Kubernetes. Those are implementation choices that require more context.
- For current product-specific terminology, unclear conventions, or a reference gap, check primary documentation when browsing is available. Cite the relevant source concisely when making source-based claims. When browsing is unavailable, state the uncertainty. Do not claim to have researched a feature during the conversation unless you did.

## Confirmation and handoff

Keep a small conversational record of the chosen candidate, defining behavior, and unresolved detail. If the user selects "2," accept that selection and summarize it once. If the user corrects a detail, keep the confirmed parts and revise the affected part. Do not repeat the same confirmation question.

After confirmation, give a short build-ready sentence using only requirements that have been stated or confirmed. If implementation was already requested, continue the authorized implementation workflow with those requirements. If the user only wanted a name, finish with the name and reusable sentence. Do not start building merely because they recognized a feature.

If the user explicitly says to skip questions or choose the most likely option, state the assumption briefly and follow that instruction. Do not turn this skill into an extra approval gate. Existing user instructions and authorization take precedence.

## Reference map

Load the smallest relevant portion. These are examples and terminology aids, not an exhaustive whitelist. Use file search (such as `rg -n -i 'drawer|side panel' references/`) when local files are available; otherwise use the environment's reference-reading tools. Do not load the whole catalogue on every invocation.

| Need | Reference |
| --- | --- |
| Translate everyday symptoms into a search direction | [request-routing.md](references/request-routing.md) |
| Distinguish similar candidates | [ambiguity-guide.md](references/ambiguity-guide.md) |
| Show a change or invisible process compactly | [motion-storyboards.md](references/motion-storyboards.md) |
| See complete short conversations and follow-ups | [conversation-examples.md](references/conversation-examples.md) |
| Page structure, menus, navigation | [frontend-layout-navigation.md](references/frontend-layout-navigation.md) |
| Forms, selection, search controls, displayed data | [frontend-inputs-data.md](references/frontend-inputs-data.md) |
| Popups, help, notifications, loading feedback | [frontend-overlays-feedback.md](references/frontend-overlays-feedback.md) |
| Motion, visual styling, scrolling effects | [frontend-visual-motion.md](references/frontend-visual-motion.md) |
| Saving, records, search, content workflows, collaborative editing | [backend-data-search.md](references/backend-data-search.md) |
| Sign-in, identity, access, ownership | [backend-identity-access.md](references/backend-identity-access.md) |
| Background work, idempotency, integrations, live updates | [backend-jobs-integrations.md](references/backend-jobs-integrations.md) |
| Hosting, domain names, network paths | [infra-hosting-network.md](references/infra-hosting-network.md) |
| Deployment, environments, configuration, costs | [infra-delivery-operations.md](references/infra-delivery-operations.md) |
| Monitoring, capacity, recovery, storage, resilience | [infra-reliability-data.md](references/infra-reliability-data.md) |
| Source scope, verification date, coverage | [sources-and-coverage.md](references/sources-and-coverage.md) |

## Check before sending

Check that the answer uses the right language; contains no more than three actual alternatives; explains behavior with familiar words; labels uncertainty honestly; shows only evidence-supported details; and asks one answerable confirmation or observation question. For an already confirmed request, give the handoff instead of asking again.
