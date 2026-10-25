# Frontend: responsive behavior, visual styles, and motion

ITWYW reference catalog. **28 concepts: FE-085–FE-112.** Research checked 2026-10-25.

## Contents

- [How to use this file](#how-to-use-this-file)
- [Adapting the display](#adapting-the-display)
- [Control states](#control-states)
- [Motion and scrolling](#motion-and-scrolling)
- [Visual treatment and sizing](#visual-treatment-and-sizing)
- [Direct manipulation and viewing](#direct-manipulation-and-viewing)
- [Important distinctions](#important-distinctions)
- [Sources](#sources)

## How to use this file

First ask what should change and what should cause the change: pointer movement, pressing, scrolling, resizing, a setting, or a task result. The two everyday phrases per row are original examples. Terms can describe different aspects of the same effect: a group can reveal on scroll, enter with a stagger, and use a smooth transition.

**Evidence limit:** A screenshot alone cannot establish animation, hover, scrolling, responsiveness, user preferences, keyboard support, accessibility, actual performance, or a backend. A static blur can resemble glass; an arrow can resemble a drag handle without being interactive. Use video, a live example, or the user's description to confirm behavior.

**Naming limit:** “Glassmorphism” and “micro-interaction” are conventional design terms, not standardized roles. CSS documentation verifies mechanisms and underlying behavior; a design label does not require one specific CSS feature or library. This catalog makes no browser-support claims or framework recommendations.

## Adapting the display

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-085 | **Responsive layout**; responsive design, mobile-friendly layout | “Make it fit phones as well as computers.” / “Stack the columns when the screen gets narrow.” | The arrangement adjusts to the available screen space. | What should change on a narrow screen: columns, navigation, spacing, or all three? | V01 |
| FE-086 | **Fluid typography**; fluid text sizing, scalable typography | “Let the title grow gently on bigger screens.” / “Make the heading smaller as the window narrows.” | Text size grows or shrinks with the available space. | Should size change smoothly with width or jump at a few set sizes? | V02 |
| FE-087 | **Responsive images**; image art direction, resolution switching | “Use a closer crop of the picture on phones.” / “Choose a picture version that suits each screen.” | The page chooses a picture version suited to its space or screen. | Is the same picture resized, a different crop shown, or a different-resolution file used? | V03 |
| FE-088 | **Dark mode**; light/dark theme, color-scheme switch | “Let me switch to a dark background at night.” / “Follow my device's dark setting.” | The interface can use a light or dark color theme. | Should the theme follow the device, a site switch, or both? | V04 |
| FE-089 | **High-contrast mode**; contrast theme | “Give me a version where the text stands out more.” / “Let people choose stronger separation between text and background.” | An alternate appearance makes foreground and background more distinct. | Is this a selectable theme, a device preference, or a general contrast correction? | V05 |

## Control states

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-090 | **Focus indicator**; focus ring, keyboard focus state | “Show where I am when I move with the keyboard.” / “Outline the control that will react if I press Enter.” | A visible mark shows which control has keyboard focus. | Does the mark follow keyboard focus rather than the mouse pointer or selection? | V06 |
| FE-091 | **Hover effect**; hover state, rollover effect | “Change the button when the mouse is over it.” / “Lift the card a little when I point at it.” | An item changes appearance when the pointer rests over it. | Must the pointer be over it without clicking? What should happen on touch? | V07 |
| FE-092 | **Pressed state**; active state, press feedback | “Make the button look pushed down while I press it.” / “Give a small visual response as I click.” | A control changes appearance during a press. | Does it last only during the press, or remain selected afterward? | V08 |
| FE-093 | **Disabled state**; unavailable control, inactive control | “Stop people pressing Continue until this is ready.” / “Show that this option cannot be used right now.” | A control is present but cannot currently be used. | Is it truly unavailable, or merely styled gray? What makes it available again? | V09 |

## Motion and scrolling

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-094 | **Smooth transition**; animated transition, eased state change | “Let the color fade instead of changing all at once.” / “Make opening and closing feel gentle.” | An item moves gradually from one appearance to another. | Which change should be gradual: color, size, position, opacity, or page content? | V10 |
| FE-095 | **Stagger animation**; staggered entrance, sequential animation | “Let the cards appear one after another.” / “Make each item start a little later than the previous one.” | Several items begin moving at slightly different times. | Are start times offset across items, rather than every item moving together? | V11 |
| FE-096 | **Scroll reveal**; reveal on scroll, scroll-triggered entrance | “Make sections appear as I reach them.” / “Fade the cards in when they enter the screen.” | Content appears when scrolling brings it into view. | Does entering the view start an animation, or does every scroll movement control its progress? | V12, V13 |
| FE-097 | **Scroll-driven animation**; scroll-linked animation, scroll scrubbing | “Make the illustration change as I move down the page.” / “Let scrolling control how far the animation has played.” | Scrolling directly controls an animation's progress. | Does the effect stop at the current point when scrolling stops and reverse when scrolling back? | V13 |
| FE-098 | **Parallax scrolling**; parallax effect, layered scroll motion | “Move the background more slowly than the words.” / “Make the layers feel farther apart as I scroll.” | Layers move at different rates to create a sense of depth. | Is the key effect relative movement between layers, rather than simply revealing content? | V14 |
| FE-099 | **Scroll snap**; snapping scroll, snap-to-section | “Let each panel settle neatly into place after I swipe.” / “Stop the scrolling with a whole card lined up.” | Scrolling settles at chosen positions. | Does scrolling land on set positions, rather than stop freely anywhere? | V15 |
| FE-100 | **Smooth scrolling**; animated scrolling | “Glide down to the section when I click its link.” / “Move back to the top gently instead of jumping.” | The view travels gradually to a scroll destination. | Is the page moving to a destination, rather than an item changing its own appearance? | V16 |
| FE-101 | **Micro-interaction**; small interaction feedback | “Give the heart a tiny response when I like something.” / “Show a small change so I know my click registered.” | A small response helps you understand one action or state change. | What action or change should it acknowledge? This is an umbrella term, not one effect. | V17 |

## Visual treatment and sizing

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-102 | **Glassmorphism**; frosted-glass UI, translucent glass effect | “Make the panel look like frosted glass.” / “Let the blurred background show through the card.” | A partly transparent surface looks like blurred glass. | Is the blur behind the panel, rather than on the panel's text or image? | V18 |
| FE-103 | **Gradient**; gradient background, color blend | “Blend the blue into purple across the background.” / “Make the color change gently from one side to the other.” | Colors blend across an area. | Is the blend across space, or should the colors change over time? | V19 |
| FE-104 | **Drop shadow**; shadow effect, visual elevation | “Make the card look slightly raised from the page.” / “Add a soft shadow behind this panel.” | A shadow makes an item look separated from its background. | Is this a permanent shadow or a change that happens on hover or press? | V20 |
| FE-105 | **Image fitting and cropping**; cover/contain fit, object fit | “Fill the picture box without stretching the photo.” / “Keep the whole image visible even if there is empty space.” | The picture is fitted inside a frame, with cropping or empty space as needed. | Should the frame be filled, or must the entire image remain visible? | V21 |
| FE-106 | **Aspect ratio**; fixed proportions, proportional sizing | “Keep all the thumbnails square.” / “Keep the video the same wide shape when it resizes.” | A box keeps the same shape as it grows or shrinks. | Are you controlling the frame's shape or which part of the image is visible? | V22 |
| FE-107 | **Text truncation**; ellipsis, line clamping | “Cut long titles after two lines and add dots.” / “Keep each preview short without changing the original text.” | Long text is visually shortened to fit a space. | Should the rest be accessible elsewhere, through expansion, or by opening the item? | V23 |
| FE-108 | **Reduced-motion mode**; motion preference support | “Respect the setting that turns down animations.” / “Give people a calmer version with less movement.” | Extra movement is reduced when a person asks for less motion. | Should it follow the device preference, a site setting, or both? | V24 |

## Direct manipulation and viewing

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-109 | **Drag and drop**; drag-to-reorder, drag-to-move | “Let me drag cards into a different order.” / “Move an item into another column by dropping it there.” | You move an item by dragging it to a new place. | Are items reordered, moved between groups, or files brought into the page? | V25 |
| FE-110 | **Resizable panes**; split pane, window splitter, resizable divider | “Let me drag the divider to give this side more room.” / “Make the left panel wider without resizing the whole window.” | Moving a divider changes the sizes of neighboring areas. | Can the divider move, or is this only a fixed two-column layout? | V26 |
| FE-111 | **Zoom and pan**; magnify and move, zoomable viewer | “Let me zoom into the picture and move around it.” / “Make the map bigger so I can inspect a small area.” | You enlarge content and move the visible area around it. | Is the change inside a viewer, or should it enlarge the whole browser page? | V27 |
| FE-112 | **Fullscreen view**; enter fullscreen, fullscreen mode | “Let the video take over the whole screen.” / “Hide the browser bars while I view this.” | Content uses the entire screen until you leave fullscreen. | Should browser controls disappear, or should content only fill the page area? | V28 |

## Important distinctions

- **A motion request has several parts:** trigger, moving element, change, timing, repetition, and stopping behavior. Ask for the missing part that distinguishes the likely candidates.
- **Reveal, stagger, and transition can combine.** Reveal describes when content becomes visible; stagger describes the order of several starts; transition describes the change between states.
- **Scroll-triggered and scroll-driven differ.** A trigger starts a time-based animation at a scroll threshold. A driven animation ties progress to scroll position. “Reveal on scroll” alone does not choose the mechanism. [V12, V13]
- **Parallax, snap, and smooth scrolling differ.** Parallax concerns relative layer motion; snap concerns where scrolling settles; smooth scrolling concerns how the view travels to a destination.
- **Hover, focus, pressed, and selected are separate states.** Pointer location is not keyboard focus. A temporary press is not a persistent selection. Never infer functionality from a colored outline alone.
- **Appearance is not an accessibility verdict.** A dark or high-contrast theme can still have unreadable combinations; a visible focus ring does not prove that all controls work by keyboard.
- **Glassmorphism is a style label.** V18 establishes translucent background blur as a mechanism. It does not define an official “glassmorphism” standard, and a still picture cannot prove live backdrop filtering.
- **Dragging is an interaction choice.** A drag handle does not establish mouse, touch, keyboard, or non-drag alternatives. A movement preview also does not prove that the new order is saved.

## Sources

Only primary official documentation is used. These sources verify behavior or visual mechanics, not a single required implementation. CSS support and implementation choices should be checked separately when building.

| Key | Source and exact URL | What it verifies |
|---|---|---|
| V01 | [MDN — Responsive web design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design) | Flexible layouts and changes across available screen sizes. |
| V02 | [MDN — clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp) | Fluid type sizing with upper/lower bounds; terminology and mechanics. |
| V03 | [MDN — Using responsive images in HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images) | Resolution switching and art-directed image changes for different spaces. |
| V04 | [MDN — prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme) | User preferences for light or dark themes. |
| V05 | [MDN — prefers-contrast](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-contrast) | Requests for greater or lower contrast; a preference is not proof of compliance. |
| V06 | [MDN — :focus-visible](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible) | Visible focus indications and their relation to input method. |
| V07 | [MDN — :hover](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover) | Pointer-over state; separate from pressing or focusing. |
| V08 | [MDN — :active](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active) | Temporary activation/press state. A persistent pressed toggle is a separate meaning. |
| V09 | [MDN — disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled) | Controls that cannot be operated, distinct from a mere gray appearance. |
| V10 | [MDN — transition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition) | A timed change between two element states. |
| V11 | [Carbon — Motion choreography](https://www.carbondesignsystem.com/building-blocks/foundations/motion/choreography) | Sequenced and staggered entrances distributed over time. |
| V12 | [MDN — Using CSS scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations) | Starting/stopping time-based animations at scroll positions. Source documents a mechanism, not a mandatory implementation. |
| V13 | [MDN — CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) | Animation progress driven by a scroll timeline rather than passing time. |
| V14 | [Chrome for Developers — Performant Parallaxing](https://developer.chrome.com/blog/performant-parallaxing) | Scroll-coupled layered movement and the depth effect. Only the effect definition is used, not dated implementation advice. |
| V15 | [MDN — CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap) | Chosen scroll positions and snapping after scroll movement. |
| V16 | [MDN — scroll-behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-behavior) | Gradual navigation/programmatic scrolling. Does not imply replacing natural wheel or touch scrolling. |
| V17 | [Carbon — Motion overview](https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview) | Small interaction responses such as button-state and disclosure feedback; “micro-interaction” is a broad design term. |
| V18 | [MDN — backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter) | Blur/effects behind a transparent or partly transparent surface. Supports the visual mechanism, not a standardized glassmorphism label. |
| V19 | [MDN — linear-gradient()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient) | A spatial blend between colors; separate from a time-based animation. |
| V20 | [MDN — box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow) | Shadow appearance around an element. Does not make the element interactive or actually change its depth. |
| V21 | [MDN — object-fit](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit) | Fitting image/video content within a frame, including cover and contain choices. |
| V22 | [MDN — aspect-ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio) | The relationship between an element's width and height. |
| V23 | [MDN — line-clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp) | Limiting visible text lines and indicating truncation. Does not supply an expansion control by itself. |
| V24 | [MDN — prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion) | User preference to reduce nonessential motion. |
| V25 | [MDN — HTML Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API) | Moving items within a page and transferring content into/out of a page. Does not imply saving or accessible alternatives. |
| V26 | [W3C APG — Window splitter](https://www.w3.org/WAI/ARIA/apg/patterns/windowsplitter/) | A movable separator that resizes neighboring panes. APG explicitly says its review/example work is incomplete. |
| V27 | [MDN — touch-action](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/touch-action) | Panning and pinch-zoom gestures. Supports behavior terminology, not a complete viewer specification. |
| V28 | [MDN — Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API) | Presenting content across the whole screen and exiting fullscreen. |
