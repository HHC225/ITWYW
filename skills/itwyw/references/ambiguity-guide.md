# Distinguish similar requests

Use one relevant row, then return no more than three candidate options. The larger catalogue here is internal reference material. Ask one plain question about what should happen. Some concepts cooperate or describe different dimensions; do not force a choice between those.

## Contents

- [Screen structure and controls](#screen-structure-and-controls)
- [Feedback and movement](#feedback-and-movement)
- [Data and backend behavior](#data-and-backend-behavior)
- [Identity and access](#identity-and-access)
- [Infrastructure and operations](#infrastructure-and-operations)
- [Evidence and terminology boundaries](#evidence-and-terminology-boundaries)

## Screen structure and controls

| Vague description | Distinction to preserve | One easy question |
| --- | --- | --- |
| "A box pops up" | Modal dialog: must deal with it before continuing. Popover: a small anchored surface. Toast: brief status feedback. Choose only plausible candidates. | "Do you need to answer it, use options beside a button, or just read a quick message?" |
| "It comes from the side" | Drawer names placement/opening style. Modal names whether the rest of the page is blocked. A drawer may also be modal; they are not inherently rival types. | "Should the side panel cover the page or make the page narrower?" |
| "Help beside an icon" | Tooltip gives brief non-interactive help on hover/focus. A help popover can contain controls and open on activation. Inline help stays in the page. | "Should the help appear when you point at the icon, when you tap it, or stay visible?" |
| "A dropdown" | A select chooses a value. A menu offers actions or links. An editable combobox combines typing with choices; a combobox can also be select-only. Opening downward alone does not decide semantics. | "Are people picking a value, choosing an action, or typing to find a choice?" |
| "Click and more is shown" | Accordion/disclosure expands content in place. Tabs replace a shared content area. Navigation opens a different destination. | "Should the answer unfold underneath, replace the middle area, or open another page?" |
| "Many things in boxes" | Uniform card grids repeat similarly sized items. Bento grids emphasize varied tile sizes. Masonry packs uneven-height items with staggered bottoms. | "Should the boxes have matching sizes, deliberately different sizes, or fit tightly around their content?" |
| "Two halves" | Split layout divides the view. Split-pane resizing lets the user drag the divider. A before/after slider reveals parts of two overlapping images. | "Are these two separate areas, a divider you can drag, or two versions of one image?" |
| "Menu follows the screen" | Fixed stays at a viewport position. Sticky scrolls normally until a threshold within its container. Both may look like a persistent header in one screenshot. | "Should it stay at the top from the start, or stick there only after you scroll to it?" |
| "Change content with left/right arrows" | Carousel changes the current item. Horizontal scrolling moves a strip. Scroll snap controls stopping points and can support either. | "Should one item become the main item, or should the whole strip slide along?" |
| "A mark beside a title" | Badge communicates status/count. Checkbox is a selectable control. Status icon is a visual state cue. | "Does the mark show information, or should people click it to choose the item?" |
| "Several steps" | Stepper shows progress through a known flow. Wizard guides completion. Timeline displays events; it need not collect input. | "Are people filling things out, or looking at things that already happened?" |
| "Move things around" | Drag-and-drop is an interaction. Sorting automatically applies a rule. Resizing changes dimensions. | "Should people drag items into their own order, choose a sorting rule, or change their size?" |

## Feedback and movement

| Vague description | Distinction to preserve | One easy question |
| --- | --- | --- |
| "Tell me it worked" | Toast/snackbar is brief. Inline success stays beside the action. Confirmation dialog asks before proceeding rather than merely reporting success. | "Should the message disappear, stay beside the form, or ask before doing the action?" |
| "Show loading" | Skeleton resembles the coming layout. Spinner indicates waiting without quantity. Progress bar shows completed amount only when known, or an explicitly indeterminate state. | "Do you want empty shapes of the coming content, a waiting symbol, or how much is finished?" |
| "Appear while scrolling" | Scroll reveal is a visibility effect. Lazy loading defers fetching. Infinite scroll appends more items. These can coexist. | "Should existing items fade into view, images download only when needed, or more items be added at the bottom?" |
| "It moves with scrolling" | Parallax gives layers different speeds. Scroll-linked animation ties progress to scrolling. Sticky positioning holds an element in place. | "Should the background move slower, an animation follow your scrolling, or an item stay in one spot?" |
| "Cards take turns appearing" | Stagger changes each item's start time. Carousel changes the displayed item. A queue changes when work is processed. | "Should several cards stay on screen after appearing one by one?" |
| "It snaps smoothly" | Smooth scrolling changes travel over time. Scroll snap changes the resting position. Easing changes speed during a transition. | "Should it simply travel gently, or also stop exactly at each section?" |
| "React when I touch it" | Hover is pointer presence, press is activation, focus is keyboard/current-control position. Touch devices do not reliably provide persistent hover. | "Should it react before the click, during the press, or when selected with the keyboard?" |
| "Feels immediate" | Optimistic UI displays an assumed result before confirmation. Actual completion is confirmed work. A loading state communicates unfinished work. | "Should the screen update immediately and correct itself if saving fails?" |
| "The screen shines through" | Transparency lets the background show. Backdrop blur softens what is behind. Glassmorphism is a combined visual style. | "Should the background simply show through, or also look blurred like frosted glass?" |

## Data and backend behavior

| Vague description | Distinction to preserve | One easy question |
| --- | --- | --- |
| "Remember what I typed" | Local persistence stays on that browser/device. Server persistence can support account access elsewhere. Autosave describes when saving occurs. | "Should it also appear when you sign in on another device?" |
| "Save without pressing a button" | Autosave periodically/on-change saves. A draft is unfinished content. Browser history or cached pages are not reliable draft storage. | "Should unfinished writing be restored when you come back later?" |
| "Undo delete" | Undo reverses an action. Soft deletion keeps an item in trash. Backup restore recovers from a past saved copy. | "Do you want an immediate undo button, a trash folder, or recovery after data is lost?" |
| "Stop duplicates" | Idempotency handles repeats of one logical operation. A unique constraint enforces uniqueness of a chosen value. Debounce delays/coalesces rapid input and is not durable duplicate protection. | "Is the problem repeating the same order, reusing a name that must be unique, or reacting to every keystroke?" |
| "Everything succeeds together" | A database transaction can make a bounded set of database changes atomic. Distributed compensation reverses earlier actions where possible; it is not the same guarantee. | "Is this one set of saved records, or steps involving other services such as payment and shipping?" |
| "Only one person gets the last item" | Atomic updates, locking, or concurrency checks prevent conflicts. A disabled button on one person's screen does not coordinate other users. | "Should the second person be told that someone else already took the item?" |
| "Find matching things" | Exact search looks for the specified match. Full-text search works with words in text. Fuzzy search tolerates near matches such as spelling mistakes. | "Should it match exactly, look through long text, or forgive spelling mistakes?" |
| "Show good choices while typing" | Autocomplete is suggestion behavior. Fuzzy search controls matching. Recommendations may use interests/history. These are not identical. | "Should the choices finish the typed word or suggest things based on the person's interests?" |
| "Next page" | Offset pagination uses positions/page numbers. Cursor pagination follows a marker. Both support partial retrieval; stability depends on ordering and changing data. | "Do people need to jump to page 12, or just keep moving forward through the newest items?" |
| "Keep trying" | Retry repeats failed work. Backoff spaces retries. Idempotency makes defined repeats safe. They can cooperate; retries alone do not ensure success. | "If the first attempt already worked but its reply was lost, should trying again reuse that result?" |
| "Do it later" | Background job runs outside the immediate response. Scheduled job waits for a time. Queue holds work until a worker takes it. | "Should it start as soon as possible, or at a chosen time?" |
| "Tell my app when payment is done" | Webhook pushes an event to another server. Polling repeatedly asks for status. Browser notifications are a delivery surface for a person. | "Should the other service tell your app, or should your app keep checking?" |
| "Updates appear live" | Live updates is the product capability. Polling, server-sent events, and WebSockets are possible transports. Do not choose a transport from appearance alone. | "Do people only receive updates, or also send changes back immediately?" |
| "We edit together" | Collaborative editing includes rules for concurrent changes. Presence shows who is there. Live updates alone do not resolve editing conflicts. | "Should people type in the same text at once, or only see who is viewing it?" |
| "Approve before showing" | Moderation filters/reviews content. Approval workflow records a decision. Publishing changes availability. They can be successive steps. | "Who should decide whether the item is allowed to appear?" |

## Identity and access

| Vague description | Distinction to preserve | One easy question |
| --- | --- | --- |
| "Log in and keep others out" | Authentication verifies who someone is. Authorization decides what they can do. Both may be needed. | "Do you mean signing people in, limiting what signed-in people can see, or both?" |
| "Google login" | Federated sign-in can use OpenID Connect. OAuth delegates access; OAuth alone is not a general identity proof. Single sign-on concerns reuse across services. | "Do you just want to sign in, or also let the app read something from the outside account?" |
| "Stay logged in" | A session preserves sign-in state; session lifetime and remembered devices affect it. Saving form data is a separate behavior. | "Should signing in remain active after the browser is closed?" |
| "One extra code" | MFA adds a different factor. A one-time email/SMS code may be the only factor. A passkey is a credential type; its security properties depend on the flow. | "Is the code the whole sign-in, or an extra check after another sign-in step?" |
| "Only managers" | Role-based permission uses a role. Ownership checks depend on who owns an item. Tenant isolation separates organizations. | "Is access based on the person's job, who owns the item, or which company they belong to?" |
| "Hide the admin page" | Hiding navigation changes appearance. Enforced authorization rejects unauthorized requests even with a direct link. | "Should people also be blocked if they paste the page's address directly?" |
| "Pay to unlock" | Subscription is a billing relationship. Entitlement is access to a capability. A quota limits how much it can be used. | "Are you charging regularly, deciding which features open, or limiting how often they can be used?" |

## Infrastructure and operations

| Vague description | Distinction to preserve | One easy question |
| --- | --- | --- |
| "Make the site fast" | This is a goal, not evidence for caching, CDN, indexing, or scaling. Locate the slow moment first. | "Is it slow when the page first opens, when you search, or when you save?" |
| "Handle more visitors" | Load balancing shares traffic among available servers. Autoscaling changes capacity. Caching reuses results. They can cooperate. | "Does it slow down only when many people arrive at once?" |
| "Copy the data so it is safe" | Replication maintains another current copy and may copy mistakes too. Backup preserves recoverable past state. Snapshot captures a point-in-time state subject to its storage guarantees. | "Do you need another running copy, or an older copy to recover after a mistake?" |
| "Keep working if it breaks" | Redundancy supplies additional resources. Failover switches to a replacement. Disaster recovery restores broader service after disruption. | "Should a spare take over immediately, or is restoring the service later acceptable?" |
| "Update without stopping" | Rolling changes instances gradually. Blue-green switches between environments. Canary exposes a small share first. None alone promises interruption-free behavior. | "Do you want to replace copies gradually, switch everything together, or try the change with a few people first?" |
| "Roll it back" | Application rollback changes running code/configuration. Database restore changes saved data and may discard newer writes. Feature rollback can disable a flag. | "Do you want the old app version back, old data back, or just the new feature switched off?" |
| "Some users see something different" | A/B testing compares outcomes. Feature flags target availability. Canary release limits deployment exposure. | "Are you comparing which design works better, controlling who gets a feature, or checking a new release?" |
| "Automatically publish code" | CI builds/checks changes. Continuous delivery prepares release. Continuous deployment releases automatically after the required checks. | "Should passing changes go live by themselves, or wait for your release decision?" |
| "Tell me what happened" | Logs record events. Metrics summarize measurements. Traces connect steps of a request. | "Do you need the event messages, a trend like error counts, or the path of one slow request?" |
| "Tell me when it breaks" | Monitoring observes; alerting notifies on conditions. A health check reports a component's configured health signal, not every real user journey. | "Should someone receive a message when a specific check fails?" |
| "Block bad traffic" | Firewall controls network traffic. WAF examines web requests. Rate limiting caps request volume. A private network limits reachability. | "Are you trying to block unwanted addresses, suspicious web requests, or too many requests?" |
| "Only my team can reach it" | Private networking controls reachability; authentication/authorization control people and actions. VPN is one access mechanism. | "Should it be unreachable outside your private connection, or reachable but require team sign-in?" |
| "Use my own address" | A domain is the name. DNS points names to destinations. Hosting runs/serves the site. HTTPS protects the connection. | "Do you already have a working site and just want a name for it?" |
| "Keep the bill small" | A budget alert warns. A quota caps a resource. Autoscaling limits bound some capacity. None alone implies a universal spending cap. | "Should you receive a warning, or should a specific kind of usage actually stop?" |

## Evidence and terminology boundaries

The terms are grounded in the primary documentation listed in the corresponding frontend, backend, and infrastructure catalogue files. Everyday descriptions and questions are original teaching examples. Sources establish meanings; they do not establish what a user's screenshot or system actually implements. Verify a disputed convention or product-specific term from its primary documentation before asserting it.
