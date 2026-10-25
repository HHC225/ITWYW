# Frontend: layout and navigation

ITWYW reference catalog. **28 concepts: FE-001–FE-028.** Research checked 2026-10-25.

## Contents

- [How to use this file](#how-to-use-this-file)
- [Page arrangements](#page-arrangements)
- [Finding a place](#finding-a-place)
- [Moving through content](#moving-through-content)
- [Application navigation](#application-navigation)
- [Important distinctions](#important-distinctions)
- [Sources](#sources)

## How to use this file

Match the user's desired behavior first. The phrases below are examples written for this catalog, not quotations from sources. Offer one likely name and a short explanation; ask the distinguishing question only when it changes the interpretation. Several concepts can apply together.

**Evidence limit:** A screenshot can suggest arrangement and appearance. It cannot establish click or scroll behavior, keyboard support, accessibility, responsive behavior, working data, or a backend. Treat these as hypotheses until described or observed.

**Naming limit:** These are conventional product and frontend names. An APG pattern describes accessibility semantics and interaction guidance; a visual label does not automatically imply that pattern. “Bento grid,” “split layout,” “hero,” and “dashboard” are design descriptions, not special HTML or ARIA roles. Source keys resolve in this file.

## Page arrangements

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-001 | **Hero section**; hero banner, hero area | “Put a big introduction at the very top.” / “Start with one bold message and a big picture.” | A large opening area introduces the page's main message. | Is this the main opening message, or a small notice above it? | L01 |
| FE-002 | **Card layout**; card grid, tile layout | “Put each product in its own little box.” / “Show separate blocks with a picture and a title.” | Each item gets its own small container. | Does each box describe one item that can stand on its own? | L02 |
| FE-003 | **Bento grid**; bento layout, bento box layout | “Use a few big boxes and several small ones.” / “Make the feature blocks fit together like a lunch box.” | Different-sized blocks fit into a planned grid. | Are the blocks deliberately different sizes while their edges line up? | L03 |
| FE-004 | **Masonry layout**; masonry grid, waterfall layout | “Pack photos together even when their heights differ.” / “Fill the gaps under the shorter pictures.” | Uneven-height items pack closely into columns. | Do items stack into gaps rather than share straight rows? | L04 |
| FE-005 | **Sidebar layout**; side-column layout | “Keep the menu in a column on the left.” / “Put filters beside the main results.” | A narrow side area sits beside the main content. | Is the side area part of the page, or does it open over the page? | L05, L06 |
| FE-006 | **Split layout**; split screen, two-panel layout | “Put the picture on one half and the text on the other.” / “Give both sides their own big area.” | The page is divided into two main areas. | Are both areas prominent, or is one only a narrow sidebar? | L05 |
| FE-007 | **List-detail layout**; master-detail layout | “Keep the message list visible when I open a message.” / “Click a row and show its details beside it.” | One area lists items and another shows the chosen item. | Does choosing an item update the neighboring detail area? | L07 |
| FE-008 | **Dashboard**; overview page, monitoring dashboard | “Show the main numbers and charts in one place.” / “Give me one screen where I can see how things are going.” | One page gathers important summaries and status. | Is the purpose to understand the overall situation at a glance? | L08 |

## Finding a place

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-009 | **Navigation bar**; navbar, primary navigation | “Put the main sections across the top.” / “Give people a menu to move around the site.” | A group of links takes people to the site's main places. | Do the items change location, or perform actions on the current content? | L09 |
| FE-010 | **Mega menu**; expanded navigation panel | “Open a big menu with several groups of links.” / “Show all the shopping categories in columns.” | A large menu groups many destinations in one panel. | Does it contain grouped columns of destinations rather than one short list? | L09 |
| FE-011 | **Breadcrumbs**; breadcrumb trail | “Show Home, then the category, then this page.” / “Let me go back up to the parent section.” | A trail shows where this page sits inside the site. | Are these parent sections, or steps someone has completed? | L10 |
| FE-012 | **In-page navigation**; table of contents, anchor navigation | “Add a list that jumps to sections on this page.” / “Let me skip straight to pricing without leaving the page.” | Links take you to headings farther down the same page. | Does the link move within this page or open another page? | L11 |
| FE-013 | **Sticky header**; sticky navigation | “Keep the header at the top after I scroll past it.” / “Let the menu stick while the page moves underneath.” | The header scrolls up, then stays at the top. | Should it stick after reaching an edge, or stay attached from the start? | L12 |
| FE-014 | **Fixed bottom navigation**; bottom navigation bar, bottom tabs | “Keep the main destinations along the bottom of the screen.” / “Leave Home and Search within reach while I scroll.” | A bottom bar keeps important destinations in the same screen position. | Does it stay visible during scrolling, and do its items go to destinations? | L12, L13 |

## Moving through content

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-015 | **Tabs**; tabbed panels, tab interface | “Click Overview or Reviews to swap the section below.” / “Show one of these sections at a time without changing pages.” | A row of labels chooses which content panel is visible. | Does the selection replace a panel here, or take the user to another page? | L14 |
| FE-016 | **Accordion**; expandable section group | “Click each question to open its answer.” / “Stack the sections so I can fold them away.” | Stacked headings open and close their own content. | Is this a group of expandable sections? Can several stay open? | L15 |
| FE-017 | **Disclosure**; show/hide, show more, expandable details | “Hide the extra explanation until I ask for it.” / “Add a More details button under this paragraph.” | One control reveals or hides extra content nearby. | Is it one optional section, rather than a set of grouped headings? | L16 |
| FE-018 | **Pagination**; page navigation, paged results | “Split the results into numbered pages.” / “Add Previous and Next below the list.” | A long collection is divided into pages you can choose. | Does moving forward replace the current results instead of adding below them? | L17 |
| FE-019 | **Load more**; show more results, incremental loading button | “Add ten more results when I press the button.” / “Keep the current items and let me ask for more.” | A button adds more items to the existing list. | Must the person press a control to get the next batch? | L18 |
| FE-020 | **Infinite scroll**; endless scrolling, automatic incremental loading | “Keep showing more posts as I reach the bottom.” / “Load the next batch without making me press Next.” | More items appear automatically as you scroll onward. | Does scrolling itself trigger more items? “Infinite” need not mean unlimited. | L18 |
| FE-021 | **Wizard**; multi-step flow, stepped form | “Ask a few questions, then take me to the next step.” / “Guide me through setup one screen at a time.” | A task is broken into a sequence of smaller screens. | Does the user complete a task in order, rather than browse related content? | L19 |
| FE-022 | **Step indicator**; progress steps, stepper | “Show that I am on step two of four.” / “Mark which setup stages are already finished.” | A row or list shows your place in a process. | Is this a progress display, navigation, or both? It need not be clickable. | L19 |

## Application navigation

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-023 | **Tree view**; folder tree, hierarchical tree | “Let me open folders inside other folders.” / “Show nested categories with little expand arrows.” | Branches open to reveal items inside them. | Are there nested parents and children, rather than a flat menu? | L20 |
| FE-024 | **Toolbar**; action bar, tool strip | “Keep editing tools together above the document.” / “Put the actions for this list in one row.” | Related action controls sit together in one place. | Do these controls act on the current item instead of navigating the site? | L21 |
| FE-025 | **Command palette**; command menu, quick actions palette | “Let me type the name of an action to run it.” / “Open one search box for commands and places.” | A searchable panel helps you find actions or destinations. | Are results commands to run, content to read, or both? | L22 |
| FE-026 | **Skip link**; skip to content | “Let keyboard users jump past the repeated menu.” / “Give people a shortcut straight to the main content.” | An early link skips repeated navigation. | Does it bypass the page's repeated beginning for keyboard users? | L23 |
| FE-027 | **Back-to-top link**; scroll to top control | “Add a button that takes me back to the top.” / “Let me return to the beginning without scrolling all the way.” | One control moves you to the start of the page. | Is the destination the top of this page, rather than the previous page? | L24 |
| FE-028 | **Footer**; page footer, site footer | “Put contact and legal links at the bottom.” / “Repeat the useful links after the main content.” | The closing area holds information and links after the page content. | Is it after the content, or always fixed to the bottom of the screen? | L25 |

## Important distinctions

- **Geometry can combine with behavior.** A dashboard may use cards in a bento grid; these are related descriptions, not interchangeable names.
- **“Menu” is broad everyday language.** Ordinary site navigation does not automatically need the desktop-style ARIA menu pattern. Ask whether items navigate, choose a value, or run a command. See FE-034 and FE-061.
- **Sticky and fixed differ.** Sticky positioning is constrained by its scroll context and container. A still image cannot determine which behavior is used. [L12]
- **“Stepper” is ambiguous.** It can mean process steps (FE-022) or a numeric plus/minus input (FE-041).
- **“Grid” is ambiguous.** A visual arrangement of boxes does not establish the interactive ARIA grid pattern used for keyboard navigation within cells. See FE-052 and FE-056.
- **Names do not prescribe implementation.** In particular, a bento composition can be built in several ways. L03 verifies the geometry of grid tracks and spanning; it does not establish “bento” as a standardized term.

## Sources

Only primary official documentation is used. Design-system sources establish terminology or behavior in their own systems; they are not framework recommendations. Where a source verifies mechanics rather than a popular label, that limitation is explicit.

| Key | Source and exact URL | What it verifies |
|---|---|---|
| L01 | [USWDS — Landing page](https://designsystem.digital.gov/templates/landing-page/) | Hero area at the start of a landing page and its introductory purpose. |
| L02 | [USWDS — Card](https://designsystem.digital.gov/components/card/) | Content and actions grouped around one subject; grouped card arrangements. |
| L03 | [MDN — Basic concepts of grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts) | Rows, columns, and items spanning cells. Supports the bento geometry, not the marketing label. |
| L04 | [MDN — Grid lanes layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes) | Masonry-style packing along one axis without aligned tracks on the other. No implementation support claim is made here. |
| L05 | [MDN — Realizing common layouts using grids](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Common_grid_layouts) | Major page areas, columns, sidebars, and content placement. Supports descriptive sidebar/split geometry. |
| L06 | [USWDS — Side navigation](https://designsystem.digital.gov/components/side-navigation/) | Navigation arranged beside content and hierarchy within a section. |
| L07 | [Material Design — List-detail canonical layout](https://m3.material.io/foundations/layout/canonical-examples/list-detail) | Selecting from a list with an associated detail pane; the layout may adapt across sizes. |
| L08 | [Carbon — 2x Grid guidelines](https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/guidelines) | Dashboards and overview pages combine separate pieces of information into a larger picture. |
| L09 | [USWDS — Header](https://designsystem.digital.gov/components/header/) | Primary navigation and expanded megamenus that group many destinations. |
| L10 | [USWDS — Breadcrumb](https://designsystem.digital.gov/components/breadcrumb/) | Location within site hierarchy; distinguishes hierarchy from linear task steps. |
| L11 | [USWDS — In-page navigation](https://designsystem.digital.gov/components/in-page-navigation/) | Links to sections of the same long page. |
| L12 | [MDN — position](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position) | Sticky versus fixed positioning and their containing contexts. |
| L13 | [Material Design — Navigation bar](https://m3.material.io/components/navigation-bar/overview) | Persistent top-level destination navigation; bottom-navigation convention. |
| L14 | [W3C APG — Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) | One associated panel shown at a time and tab interaction semantics. |
| L15 | [W3C APG — Accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/) | Stacked headings that reveal or hide associated sections; one-open and multiple-open variants. |
| L16 | [W3C APG — Disclosure](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) | A control that expands or collapses associated content. |
| L17 | [USWDS — Pagination](https://designsystem.digital.gov/components/pagination/) | Collections divided into navigable pages; distinction from process steps. |
| L18 | [W3C APG — Feed](https://www.w3.org/WAI/ARIA/apg/patterns/feed/) | Content added while scrolling, contrasted with an explicit next-batch button. Not every infinite list is an ARIA feed. |
| L19 | [USWDS — Step indicator](https://designsystem.digital.gov/components/step-indicator/) | Multi-screen processes and a progress indicator that complements Back/Next controls. |
| L20 | [W3C APG — Tree view](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/) | Hierarchical parent/child items that expand and collapse. |
| L21 | [W3C APG — Toolbar](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/) | A grouped set of controls and its distinct keyboard interaction pattern. |
| L22 | [GitHub Docs — GitHub Command Palette](https://docs.github.com/en/get-started/accessibility/github-command-palette) | A concrete official example of finding navigation and commands in one on-demand palette. |
| L23 | [GOV.UK — Skip link](https://design-system.service.gov.uk/components/skip-link/) | Bypassing repeated navigation to reach main content. |
| L24 | [MDN — a: HTML anchor element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a) | Links to locations on the same page, including top-of-page navigation. |
| L25 | [USWDS — Footer](https://designsystem.digital.gov/components/footer/) | Closing site navigation, contact information, and supporting links. |
