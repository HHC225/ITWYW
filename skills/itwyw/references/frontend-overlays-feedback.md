# Frontend: overlays, feedback, and content presentation

ITWYW reference catalog. **28 concepts: FE-057–FE-084.** Research checked 2026-10-25.

## Contents

- [How to use this file](#how-to-use-this-file)
- [Panels over the page](#panels-over-the-page)
- [Messages and decisions](#messages-and-decisions)
- [Loading and results](#loading-and-results)
- [Content and identity](#content-and-identity)
- [Important distinctions](#important-distinctions)
- [Sources](#sources)

## How to use this file

Start with what appears, what causes it to appear, whether it blocks the page, and how it closes. The two everyday phrases in each row are original examples. A visual shape and its behavior can have different names: a drawer can be modal, and a success message can appear in a toast.

**Evidence limit:** A screenshot alone cannot prove modality, focus handling, keyboard support, accessibility, automatic dismissal, animation, live updates, real data, or a backend. A dim background is a visual clue, not proof that the background is truly inactive.

**Naming limit:** “Popup” is an umbrella word. “Toast,” “snackbar,” “drawer,” “sheet,” and “lightbox” are conventional labels whose details vary across systems. A visual label does not automatically specify an HTML element or ARIA role. Source keys resolve locally.

## Panels over the page

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-057 | **Modal dialog**; modal, blocking dialog | “Open a box and make me finish or close it before continuing.” / “Put the form over the page and pause everything behind it.” | A dialog needs your attention before you can use the page behind it. | Can the user interact with anything outside it while it is open? | O01 |
| FE-058 | **Non-modal dialog**; modeless dialog, floating tool window | “Keep this little tool window open while I work.” / “Let me use the page without closing the box.” | A separate dialog stays open while the page remains usable. | Can the user move between the dialog and the rest of the page? | O02 |
| FE-059 | **Drawer**; side sheet, slide-out panel, off-canvas panel | “Open the filters from the right edge.” / “Slide a panel in from the side when I click.” | An extra panel opens from a side of the screen. | Which edge? Does it cover content, push content, or block background interaction? | O03 |
| FE-060 | **Bottom sheet**; bottom drawer, slide-up sheet | “Bring the choices up from the bottom.” / “Open a short panel above the bottom edge.” | A panel opens from the bottom of the screen. | Is it attached to the bottom, and can the page behind it still be used? | O04 |
| FE-061 | **Dropdown menu**; menu button, action menu, overflow menu | “Click the three dots to see more actions.” / “Open a small menu with Rename and Delete.” | A control opens a list of commands. | Do choices perform actions, select a form value, or navigate? | O05 |
| FE-062 | **Context menu**; right-click menu | “Right-click an item to see what I can do with it.” / “Show actions for the thing I pressed on.” | A menu offers actions for the item you are using. | Is it requested on a specific item, often with right-click or a menu key? | O06 |
| FE-063 | **Popover**; anchored overlay, floating information panel | “Open a small card next to this button.” / “Show extra details here without taking over the screen.” | A small floating panel shows extra information or controls. | Does it need clickable content? Should the rest of the page remain usable? | O07 |
| FE-064 | **Tooltip**; hover hint, help tooltip | “Explain the icon when I point at it.” / “Show a little label when this control gets focus.” | A short hint explains the control beside it. | Is it brief non-interactive help shown on hover or focus? Links suggest another panel type. | O08 |

## Messages and decisions

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-065 | **Toast notification / snackbar**; transient notification | “Briefly show Saved in a small corner message.” / “Tell me it worked without stopping what I am doing.” | A small message reports an update without taking over the page. | Should it disappear, stay until dismissed, or offer an action such as Undo? | O09, O10 |
| FE-066 | **Inline notification**; inline alert, contextual message | “Show the warning next to the affected section.” / “Keep this message inside the page until the problem is resolved.” | A message sits beside the content it concerns. | Is it tied to this section rather than floating over the page? | O10 |
| FE-067 | **Announcement banner**; notification banner, site alert | “Put a maintenance notice across the top.” / “Show an announcement that applies to the whole site.” | A wide message announces something affecting a large part of the site. | Does it concern the whole site or only a single field or action? | O11 |
| FE-068 | **Notification center**; notification panel, notification inbox | “Let me open the bell and read earlier notices.” / “Keep all my updates in one panel.” | One place collects notices you can return to later. | Must messages remain available after a brief popup is gone? | O10 |
| FE-069 | **Confirmation dialog**; confirm action prompt, confirm/cancel dialog | “Ask if I am sure before deleting it.” / “Let me confirm or cancel before the change happens.” | A dialog asks you to approve an action before it happens. | Is the person approving a future action or being told it already happened? | O12 |

## Loading and results

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-070 | **Skeleton loading**; skeleton screen, skeleton placeholder | “Show pale shapes where the content will arrive.” / “Keep the page's shape visible while it loads.” | Empty shapes stand in for content that is still arriving. | Do the shapes match the coming content, rather than show a generic spinner? | O13 |
| FE-071 | **Indeterminate loading indicator**; spinner, busy indicator | “Show a spinning circle while I wait.” / “Let me know the page is still working.” | A repeating indicator says work is happening. | Is the amount completed unknown? A spinner does not report a percentage. | O13 |
| FE-072 | **Determinate progress indicator**; progress bar, progress ring | “Show how much of the upload is finished.” / “Fill the bar as the task gets closer to done.” | A growing bar or ring shows how much work is complete. | Is there a real completed amount to show? A bar can also be indeterminate. | O14 |
| FE-073 | **Empty state**; no-data state, no-results state | “Explain what to do when the list is empty.” / “Show a helpful message when nothing matches the search.” | A message explains why there is nothing to show. | Is there no content yet, no match, or a failure to fetch existing content? | O15 |
| FE-074 | **Error state**; failure state, retry state | “Tell me the list could not load and let me try again.” / “Show what went wrong instead of leaving a blank space.” | The page explains a failure and offers a useful next step. | Did something fail, or is the result simply empty? Is retry actually possible? | O15 |
| FE-075 | **Success confirmation**; completion state, confirmation page | “Clearly tell me the request has been submitted.” / “Show a finished screen with what happens next.” | A message confirms that the task is complete. | Has it completed, or is it only received and still being processed? | O16 |

## Content and identity

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-076 | **Notification badge**; count badge, unread dot | “Put the unread number on the bell.” / “Add a small dot when there is something new.” | A small mark adds a count or status to another item. | Is it attached to an icon or destination, or is it a category label? | O17 |
| FE-077 | **Avatar**; profile image, user picture | “Show each person's picture beside their message.” / “Use a little image to represent the account.” | A small picture represents a person or group. | Does it represent an identity rather than the content itself? | O18 |
| FE-078 | **Tag**; category label, chip, token | “Show small labels for the topics.” / “Put each selected filter in its own little pill.” | A compact label names a category or chosen item. | Is it only a label, or can the user select, remove, or act on it? | O19 |
| FE-079 | **Carousel**; slideshow, image rotator, content slider | “Let me move through the pictures with arrows.” / “Show a few cards at a time and slide to the next ones.” | A viewer changes which items from a sequence are visible. | Does it advance manually or automatically? How many items appear at once? | O20 |
| FE-080 | **Lightbox**; image-viewer overlay, click-to-enlarge viewer | “Click the photo to see it larger over the page.” / “Let me inspect the image without leaving this screen.” | A larger image opens above the current page. | Does it enlarge the image in an overlay, or open a new page or file? | O21 |
| FE-081 | **Media player**; video player, audio player | “Let people play and pause the video here.” / “Add volume and a way to skip to another point.” | Controls let you play, stop, and move through media. | Is this controllable media or an automatically moving decorative image? | O22 |
| FE-082 | **Copy-to-clipboard control**; copy button | “Add a button that copies this code.” / “Let me copy the link without selecting the text.” | One press copies content so you can paste it elsewhere. | Should it copy the displayed text, a link, or another value? | O23 |
| FE-083 | **Data visualization**; chart, graph | “Turn these numbers into a picture I can compare.” / “Show how the total changes over time.” | A chart makes patterns in numbers easier to see. | Is the question about comparison, change over time, or parts of a whole? | O24 |
| FE-084 | **Activity timeline**; event timeline, activity history | “Show what happened and when in order.” / “List the updates along a line with dates.” | Events are arranged along a line in time order. | Is this a history of events or a schedule of planned tasks and durations? | O25 |

## Important distinctions

- **Dialog is not a synonym for modal.** Modal describes blocked interaction outside the dialog; a dialog can also be non-modal. A drawer or sheet may use either behavior. [O01–O04]
- **Tooltip versus popover:** tooltips are brief explanatory content and do not receive focus; content with focusable actions needs another interaction pattern. The APG tooltip page explicitly remains work in progress. [O07, O08]
- **Toast and snackbar are related labels, not universal specifications.** Placement, lifetime, and actions vary. Do not infer that a visible toast must dismiss automatically. [O09, O10]
- **Message meaning and container are separate.** “Success” describes a result; “toast,” “inline,” “banner,” or “dialog” describes how the message is presented.
- **“Alert” is also a semantic term.** A warning-colored box does not establish an ARIA alert or justify an urgent screen-reader interruption.
- **Empty, loading, and failed are different states.** Ask whether nothing exists, content is still coming, or something prevented it from appearing.
- **A pill shape is not an interaction contract.** A tag may be static, removable, selectable, or actionable. A badge may only add a count. [O17, O19]

## Sources

Only primary official documentation is used. Sources establish names and behavior; they do not recommend a vendor, framework, or implementation stack.

| Key | Source and exact URL | What it verifies |
|---|---|---|
| O01 | [W3C APG — Modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | Modal dialogs, inactive background content, and focus containment. |
| O02 | [MDN — dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog) | Modal and non-modal dialogs, and whether the surrounding page remains interactive. |
| O03 | [Material Design — Side sheets](https://m3.material.io/components/side-sheets/overview) | Side-anchored secondary panels and modal/standard variants. “Drawer” remains a broader design label. |
| O04 | [Material Design — Bottom sheets](https://m3.material.io/components/bottom-sheets/overview) | Bottom-anchored secondary content, including modal and standard variants. |
| O05 | [W3C APG — Menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) | A control that opens a menu of actions or destinations; differs from choosing a form value. |
| O06 | [MDN — contextmenu event](https://developer.mozilla.org/en-US/docs/Web/API/Element/contextmenu_event) | Context menus requested on an element by mouse or keyboard. |
| O07 | [MDN — Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API) | Overlaid content; the native Popover API is non-modal and does not itself choose a semantic role. |
| O08 | [W3C APG — Tooltip](https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/) | Hover/focus explanatory popup, no focusable contents. The page explicitly labels the pattern work in progress. |
| O09 | [Material Design — Snackbar](https://m3.material.io/components/snackbar/overview) | Short updates about app processes, conventionally shown near the bottom. |
| O10 | [Carbon — Notifications](https://www.carbondesignsystem.com/building-blocks/core/patterns/notifications) | Toast, inline, and notification-center distinctions; timing varies by action requirements. Notification-panel guidance is still developing. |
| O11 | [USWDS — Site alert](https://designsystem.digital.gov/components/site-alert/) | Prominent messages for site-level information. Distinct from the USWDS government-identity Banner component. |
| O12 | [W3C APG — Alert and message dialogs](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/) | Important prompts that acquire a response, including confirmation. Not every confirmation should use the alertdialog role. |
| O13 | [Carbon — Loading](https://www.carbondesignsystem.com/building-blocks/core/patterns/loading) | Skeleton placeholders and generic indicators that show activity without a completed amount. |
| O14 | [MDN — progress](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress) | Completion progress, including determinate and indeterminate cases. |
| O15 | [Carbon — Empty states](https://www.carbondesignsystem.com/building-blocks/core/patterns/empty-states) | First-use, no-results, and error-management empty states, with explanatory next steps. |
| O16 | [GOV.UK — Confirmation pages](https://design-system.service.gov.uk/patterns/confirmation-pages/) | Confirming a completed transaction and explaining subsequent steps. |
| O17 | [Material Design — Badges](https://m3.material.io/components/badges/overview) | Counts, notifications, or status attached to navigation items and icons. |
| O18 | [Primer — Avatar](https://primer.style/product/components/avatar/) | An image representing a user or organization. |
| O19 | [Carbon — Tag guidelines](https://www.carbondesignsystem.com/building-blocks/core/components/tag/guidelines) | Labeling/categorization and static, dismissible, selectable, or operational variants. |
| O20 | [W3C APG — Carousel](https://www.w3.org/WAI/ARIA/apg/patterns/carousel/) | Sequential subsets of slides, manual/automatic rotation, and controls. |
| O21 | [WordPress documentation — Image block](https://wordpress.org/documentation/article/image-block/) | The official “Enlarge on click” feature explicitly identifies an in-page larger-image view as a lightbox. Terminology evidence only. |
| O22 | [MDN — video](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video) | Playback controls, seeking, volume, and related audio/video behavior. |
| O23 | [Carbon — Code snippet guidelines](https://www.carbondesignsystem.com/building-blocks/core/components/code-snippet/guidelines) | A copy control that puts content on the clipboard. |
| O24 | [USWDS — Data visualizations](https://designsystem.digital.gov/components/data-visualizations/) | Communicating numerical patterns and relationships; charts need meaningful alternatives. |
| O25 | [Primer — Timeline](https://primer.style/product/components/timeline/) | Connected timeline items used to present a sequence of activity. No server-side audit-log guarantee is implied. |
