# Route everyday descriptions

Use this as a retrieval map, not a script or a keyword classifier. The phrases are illustrative English translations of intentions that may be expressed in any language. Interpret the whole request and earlier context before choosing a term.

## Contents

- [Extract the observable request](#extract-the-observable-request)
- [Find the likely domain](#find-the-likely-domain)
- [Handle vague language](#handle-vague-language)
- [Handle combined features](#handle-combined-features)
- [Use the catalogue efficiently](#use-the-catalogue-efficiently)

## Extract the observable request

Privately fill only the fields the user actually supplied:

| Field | Everyday evidence | Useful distinction |
| --- | --- | --- |
| Trigger | "when I tap," "as I type," "at midnight," "when payment succeeds" | A click, live input, a schedule, or another system's event. |
| Place | "beside the icon," "from the right," "on another phone" | Nearby help, an edge panel, or shared account data. |
| Change | "opens," "follows," "remembers," "sends," "blocks" | Display, motion, storage, work, or access. |
| Time | "right away," "after a pause," "later," "even after closing" | Immediate feedback, debounce, background work, or persistence. |
| Scope | "just me," "everyone," "my company," "admins only" | Local state, shared updates, tenant separation, or permissions. |
| Failure expectation | "if I press twice," "if the internet drops," "if a server dies" | Duplicate handling, offline recovery, or service resilience. |
| Boundary | "without leaving this page," "only while typing," "until I close it" | Preserve these conditions; they often determine the correct name. |

Missing fields are not invitations to ask seven questions. Ask only the next observable distinction needed to identify the feature.

## Find the likely domain

| Everyday description | Search direction, not an automatic answer | Start with |
| --- | --- | --- |
| "The big first part with a picture and a button" | Hero section; split layout if it is about two columns | [Frontend layout](frontend-layout-navigation.md) |
| "Small boxes like an organized lunch box" | Card layout, bento grid, masonry; inspect sizes and alignment | [Frontend layout](frontend-layout-navigation.md) |
| "It should fit my phone too" | Responsive layout; clarify only if they mean a separate mobile app | [Frontend display adaptation](frontend-visual-motion.md#adapting-the-display) |
| "The menu follows me down" | Persistent header; sticky versus fixed behavior | [Frontend layout](frontend-layout-navigation.md) |
| "I change the label and the same space shows different stuff" | Tabs; not necessarily a new page | [Frontend layout](frontend-layout-navigation.md) |
| "Tap the question and its answer opens underneath" | Accordion or disclosure | [Frontend layout](frontend-layout-navigation.md) |
| "A little box pops out" | Position, interruption, trigger, and lifetime are missing | [Ambiguities](ambiguity-guide.md) |
| "It slides in from the side" | Drawer or side panel; check whether it covers or pushes the page | [Frontend overlays](frontend-overlays-feedback.md) |
| "Tell me what this tiny icon means" | Tooltip, inline help, or help popover | [Frontend overlays](frontend-overlays-feedback.md) |
| "Show a little 'done' message and let me keep going" | Toast or snackbar | [Frontend overlays](frontend-overlays-feedback.md) |
| "Show something while the real content arrives" | Skeleton, spinner, or progress indicator | [Frontend overlays](frontend-overlays-feedback.md) |
| "Pictures move when I scroll" | Parallax, scroll reveal, or scroll-linked animation | [Frontend motion](frontend-visual-motion.md) |
| "The cards appear one after another" | Stagger animation; no automatic implication of new data | [Frontend motion](frontend-visual-motion.md) |
| "Stop neatly on each section" | Scroll snap | [Frontend motion](frontend-visual-motion.md) |
| "Like foggy glass, but I can see colors behind it" | Glassmorphism or frosted-glass styling | [Frontend motion](frontend-visual-motion.md) |
| "Start typing and show possible names" | Autocomplete, combobox, or search suggestions | [Frontend inputs](frontend-inputs-data.md) |
| "Find it even if I spelled it wrong" | Fuzzy search; not just autocomplete | [Backend data](backend-data-search.md) |
| "Only show red ones under $20" | Filtering or faceted filtering | [Frontend inputs](frontend-inputs-data.md) |
| "Put the newest ones first" | Sorting; clarify which date only if necessary | [Backend data](backend-data-search.md) |
| "More items keep coming when I reach the bottom" | Infinite scrolling; storage retrieval is a separate layer | [Frontend layout](frontend-layout-navigation.md) |
| "A huge list should scroll smoothly" | List virtualization is a candidate only when rendering is the issue | [Frontend inputs](frontend-inputs-data.md) |
| "Keep what I typed if I accidentally leave" | Draft saving or persistence; local versus account-wide | [Backend data](backend-data-search.md) |
| "Save by itself while I write" | Autosave; specify where it is saved only when needed | [Backend data](backend-data-search.md) |
| "Bring it back after I deleted it" | Undo, soft deletion/trash, or backup restore | [Ambiguities](ambiguity-guide.md) |
| "One order even if the button is tapped twice" | Idempotency, with optional button feedback; define the same logical order | [Backend jobs](backend-jobs-integrations.md) |
| "Nobody should grab the last ticket at the same time" | Atomic reservation or concurrency control | [Backend data](backend-data-search.md) |
| "Let me sign in with an account I already have" | Federated login or single sign-on; not permission to read all external data | [Backend identity](backend-identity-access.md) |
| "Only the owner can open this link" | Authorization and ownership checks; not hiding the link | [Backend identity](backend-identity-access.md) |
| "Each company sees its own stuff" | Tenant isolation; company membership matters | [Backend identity](backend-identity-access.md) |
| "The paid plan unlocks this button" | Entitlements; the server also needs to enforce access | [Backend identity](backend-identity-access.md) |
| "Email me when another service finishes" | Event notification or webhook-driven workflow | [Backend jobs](backend-jobs-integrations.md) |
| "Work on a large export while I keep using the page" | Background job and status feedback | [Backend jobs](backend-jobs-integrations.md) |
| "Run it every morning" | Scheduled job; user timezone may matter later | [Backend jobs](backend-jobs-integrations.md) |
| "Try again if it fails" | Retry policy; safety depends on whether the work can be repeated | [Backend jobs](backend-jobs-integrations.md) |
| "New messages appear without refreshing" | Live updates; transport is not yet determined | [Backend jobs](backend-jobs-integrations.md) |
| "We can both edit one document" | Collaborative editing and conflict handling | [Backend data](backend-data-search.md) |
| "Let my manager say yes before it goes live" | Approval workflow and state transitions | [Backend data](backend-data-search.md) |
| "People need to open it on the internet" | Hosting and deployment; not enough evidence for a hosting model | [Infrastructure hosting](infra-hosting-network.md) |
| "I want my own web address" | Custom domain and DNS | [Infrastructure hosting](infra-hosting-network.md) |
| "The address should have the lock symbol" | HTTPS/TLS; this protects the connection, not every app behavior | [Infrastructure hosting](infra-hosting-network.md) |
| "Only the office should reach it" | Private access; distinguish network access from user permission | [Infrastructure hosting](infra-hosting-network.md) |
| "Make it fast everywhere" | Ask when and where it is slow before suggesting CDN or caching | [Ambiguities](ambiguity-guide.md) |
| "Lots of visitors arrive at once" | Capacity planning, load balancing, autoscaling, or waiting room depending on observed need | [Infrastructure resilience](infra-reliability-data.md) |
| "New code should get checked and released for me" | CI and CD; build, check, and release are separate steps | [Infrastructure delivery](infra-delivery-operations.md) |
| "Try changes somewhere customers cannot see" | Staging or preview environment | [Infrastructure delivery](infra-delivery-operations.md) |
| "Let a few people try the new version first" | Canary release, feature flag rollout, or A/B test depending on purpose | [Ambiguities](ambiguity-guide.md) |
| "Tell me when something breaks" | Monitoring and alerting; ask what counts as broken if unspecified | [Infrastructure resilience](infra-reliability-data.md) |
| "Find out why that one request was slow" | Tracing, logs, and metrics have different roles | [Infrastructure resilience](infra-reliability-data.md) |
| "Get everything back after a disaster" | Backup, restore, and disaster recovery | [Infrastructure resilience](infra-reliability-data.md) |
| "Keep serving people if one machine stops" | Redundancy and failover; a backup file does not take over traffic | [Infrastructure resilience](infra-reliability-data.md) |
| "The bill should not suddenly explode" | Budgets/alerts, quotas, or hard limits; distinguish warning from enforcement | [Infrastructure delivery](infra-delivery-operations.md) |

## Handle vague language

Sound words such as "whoosh," "pop," "snap," or "bounce" suggest a transition but do not identify its purpose. A "pop" might be a dialog, tooltip, notification, or a button animation. Ask what appears and whether the rest of the page remains usable.

Treat "like Instagram," "like a spreadsheet," or "like an online shop" as context, not as a feature specification. Anchor the response to the named behavior: a swipeable photo set, editable cells, a cart, or a checkout. Do not copy branding or invent unmentioned functions.

For "make it professional," "make it smarter," "secure," "automatic," and "never lose anything," find the desired observable outcome. A short question about the moment or consequence is more helpful than three impressive-sounding technologies.

When a term the user supplies conflicts with the behavior, use the behavior to propose a correction gently: "That sounds like a drawer: it opens from the edge. Is that what you mean by the popup?"

## Handle combined features

Do not misrepresent cooperating layers as alternatives:

| User's goal | Parts that may cooperate | The question to settle first |
| --- | --- | --- |
| A chat message shows up right away | Immediate screen feedback, delivery confirmation, live updates | "Should the sender see it immediately while it is still being sent?" |
| A purchase happens once | Button feedback, server duplicate handling, order identity | "Should repeating the same purchase request return the existing order?" |
| An upload keeps going while the page is used | Upload transfer, background processing, progress display | "Do you need to keep using the page while the upload finishes?" |
| A team edits a shared document | Shared content, collaboration logic, presence indicators | "Should everyone be able to type in the same document at once?" |
| A busy site stays usable | Capacity, traffic distribution, buffering, graceful degradation | "What becomes unavailable when many people arrive?" |

Name the product goal first. Expand into parts only when it helps the user confirm the goal. Architecture choices come after that.

## Use the catalogue efficiently

Search for both the user's action and a likely alias. Read the surrounding comparison cue, not only the matching row. The primary source lists in each domain file establish the underlying terms; the everyday phrases are original examples written for this skill. A phrase is not evidence that a particular implementation is already present.
