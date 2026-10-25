# Frontend: inputs and working with data

ITWYW reference catalog. **29 concepts: FE-029–FE-056 and FE-113.** Research checked 2026-10-25.

## Contents

- [How to use this file](#how-to-use-this-file)
- [Entering and choosing](#entering-and-choosing)
- [Numbers and specialized values](#numbers-and-specialized-values)
- [Helping with text](#helping-with-text)
- [Working with collections](#working-with-collections)
- [Important distinctions](#important-distinctions)
- [Sources](#sources)

## How to use this file

Choose the name by what the user wants to enter, select, or change. These everyday phrases are original examples, not source quotations. The easy question should settle a real ambiguity; do not ask every question in the catalog.

**Evidence limit:** A screenshot can show a field or table, but it does not prove typing behavior, validation timing, keyboard access, accessibility, saving, search quality, permissions, or backend processing. A selected file is not proof of a completed upload. An editable value is not proof it has been saved.

**Naming limit:** Different appearances can have the same semantics. Segmented choices may behave as radios, tabs, or buttons. “Dropdown” may mean choosing a value, getting suggestions, or running an action. APG names describe specific interaction patterns; do not assign roles from shape alone.

## Entering and choosing

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-029 | **Button**; action button, push button | “Give me something to press to save this.” / “Add a clear control that starts the task.” | Pressing it starts an action. | Does it do something here, or simply take the user to a new address? | I01 |
| FE-030 | **Text input**; text field, single-line field | “Let people type their name.” / “Add a small box for a short answer.” | A field holds one line of typed text. | Is the answer a short line rather than a paragraph? | I02 |
| FE-031 | **Textarea**; multiline input, long-answer field | “Give people room to write a message.” / “Let the answer run over several lines.” | A larger text box holds paragraphs. | Does it need multiple lines without rich formatting tools? | I03 |
| FE-032 | **Search field**; search box, search bar | “Let me find an item by typing its name.” / “Add a box to search the site.” | Typed words help find matching content. | Is the user looking for content, or choosing the value of a form field? | I04 |
| FE-033 | **Autocomplete**; typeahead, editable combobox, autosuggest | “Suggest matching cities while I type.” / “Let me type a few letters and choose from the matches.” | Suggestions appear while you enter a value. | May the user keep a new value, or must they choose an existing suggestion? | I05 |
| FE-034 | **Select**; dropdown selector, single-select dropdown | “Let me pick one country from a list.” / “Open the choices when I click the arrow.” | A compact control lets you choose one value. | Does choosing set a value, rather than run an action or open a page? | I06, I05 |
| FE-035 | **Multi-select listbox**; multi-select picker | “Let me choose several people from this list.” / “Keep more than one option selected.” | A list lets you keep several options selected. | Is this a selectable list, or separate checkboxes that can each be checked? | I07 |
| FE-036 | **Radio group**; radio buttons, single-choice group | “Choose exactly one delivery option.” / “Show all the choices, but allow only one.” | Picking one option turns the other choices off. | Are the choices mutually exclusive and visible together? | I08 |
| FE-037 | **Checkbox group**; checkboxes, multiple-choice group | “Tick every option that applies.” / “Let people choose email, text messages, or both.” | Each box can be checked on its own. | Can several choices be checked independently? | I09 |
| FE-038 | **Switch**; on/off toggle, toggle switch | “Add an on-and-off control for notifications.” / “Let me turn this setting off.” | A switch changes one setting between on and off. | Is the meaning on/off, rather than membership in a list of choices? | I10 |

## Numbers and specialized values

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-039 | **Slider input**; single-thumb slider, range input | “Drag a handle to set the volume.” / “Let me choose a value between low and high.” | Moving one handle changes a value along a scale. | Is there one value to set, or two ends of an interval? | I11 |
| FE-040 | **Range slider**; dual-thumb slider, interval slider | “Choose the lowest and highest price.” / “Let me drag both ends of the allowed range.” | Two handles set the beginning and end of an interval. | Are two values selected together? Some libraries call any slider a range slider. | I12 |
| FE-041 | **Number stepper**; spinbutton, quantity selector | “Add plus and minus buttons beside the quantity.” / “Let me increase the number one at a time.” | Controls increase or decrease a number in steps. | Does it edit a quantity rather than show steps in a process? | I13 |
| FE-042 | **Date picker**; calendar picker, date selector | “Open a calendar so I can choose a day.” / “Let me pick the appointment date from a month view.” | A calendar helps you choose a date. | One day or a start-and-end pair? A typed date field alone is not a calendar. | I14 |
| FE-043 | **Time input**; time picker, time selector | “Let me choose the hour and minutes.” / “Add a control for the appointment time.” | A control collects a time of day. | Is this a clock time, a duration, or a combined date and time? | I15 |
| FE-044 | **File upload control**; file picker, upload dropzone | “Let me attach a photo from my computer.” / “Give me a place to drop a document.” | You choose a file for the page to use. | Should users browse, drop files, or both? Is selection separate from uploading? | I16 |
| FE-045 | **Password visibility toggle**; show/hide password, reveal password | “Add an eye so I can check what I typed.” / “Let me show the password for a moment.” | A control switches between hidden and readable password text. | Does the request concern visibility, rather than changing or recovering the password? | I17 |
| FE-046 | **Character counter**; word counter, remaining-length indicator | “Show how many letters I have left.” / “Tell me when my answer is too long.” | A count shows how much text fits or remains. | Count characters or words? Does it warn at a limit or block more input? | I18 |

## Helping with text

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-047 | **Rich text editor**; formatted-text editor, WYSIWYG editor | “Let people make words bold and add lists.” / “Give the message box simple document tools.” | You write text and change its formatting. | Does the user need formatting controls, or only plain paragraphs? | I19, I20 |
| FE-048 | **Rating input**; star rating, score picker | “Let people give this one to five stars.” / “Ask how happy they are on a short scale.” | A person chooses a score from a small scale. | Can the user change the score, or is this only a displayed rating? | I08, I11 |
| FE-049 | **Color picker**; color selector, swatch picker | “Let me choose a color from a palette.” / “Add a color box I can change.” | A control lets you pick a color. | Must users choose preset colors, or may they choose any color? | I21 |
| FE-050 | **Input mask**; input formatting mask, guided formatting | “Add the phone-number dashes as I type.” / “Guide my answer into the right shape.” | The field helps arrange typed characters into a set format. | Should the format change while typing, or should the page only report mistakes? | I22 |
| FE-051 | **Inline form validation**; field error message, validation feedback | “Tell me which answer I need to fix.” / “Show the problem right beside the box.” | A nearby message explains a problem with an answer. | Is the problem the user's answer or a failed service? When should feedback appear? | I23 |

## Working with collections

| ID | Conventional name and aliases | Everyday user phrases (two examples) | Simple explanation | Decisive cue or easy question | Sources |
|---|---|---|---|---|---|
| FE-052 | **Data table**; tabular list, comparison table | “Line up names, dates, and amounts in columns.” / “Make it easy to compare the same facts for every item.” | Rows and columns keep related facts lined up. | Are values compared under shared headings, or are these independent cards? | I24 |
| FE-053 | **Table sorting**; sortable columns, sort control | “Click Price to put the cheapest items first.” / “Let me reverse the order by date.” | A control changes the order of the existing items. | Should items change order, or should some items disappear from the result set? | I25 |
| FE-054 | **Filtering**; faceted filters, filter controls | “Only show the red items in my size.” / “Let me narrow the results by date and category.” | Choices reduce the list to items that match. | Should each choice apply immediately, or after an Apply button? | I26 |
| FE-055 | **Bulk actions**; batch actions, multi-row actions | “Select several rows and archive them together.” / “Let me apply the same action to all checked items.” | One action affects the selected group of items. | Does the action apply to one row, selected rows, or all matching results? | I25 |
| FE-056 | **Inline editing**; in-place editing, editable cells | “Click the value and change it right there.” / “Let me edit a row without opening another page.” | You change a value where it is already displayed. | Does editing happen in the current spot? How are Save and Cancel handled? | I20, I27 |
| FE-113 | **List virtualization**; windowing, virtualized list, virtual scrolling | “Keep a huge list smooth without drawing every row at once.” / “Only draw the part of the list I can see.” | The page draws nearby visible items instead of the whole list. | Is drawing many rows the measured problem, or is fetching the data slow? This differs from loading more items. | I28 |

## Important distinctions

- **Select, autocomplete, and menu:** a select chooses a value; autocomplete adds typing and suggestions; an action menu offers commands. A combobox can also be select-only, so “combobox always means a text field” is incorrect. [I05]
- **Switch, checkbox, and toggle button:** all can represent two states, but their meaning differs. Ask about on/off, checked membership, or a pressed tool. Timing alone does not determine the role. [I01, I09, I10]
- **Tabs versus segmented choices:** swapping a content panel suggests tabs (FE-015); picking a form value suggests radios (FE-036). The same connected-button shape can support either.
- **Slider is ambiguous:** an input sets a value; a carousel changes the visible slide (FE-079). A price interval usually needs two values (FE-040).
- **Mask versus validation:** adding separators helps format an answer; reporting that it is unacceptable is validation. A neat-looking value can still be wrong.
- **Frontend scope:** these names identify controls and visible behavior. They do not establish persistence, search infrastructure, file storage, or permission enforcement.
- **Virtualization versus infinite scrolling:** virtualization limits drawn items; infinite scrolling adds items to browse. They can be combined, and neither follows automatically from a vague request for speed. [I28]

## Sources

Only primary official documentation is used. Sources establish behavior and terminology, not a recommendation to adopt their libraries. The question wording and everyday examples are original editorial material.

| Key | Source and exact URL | What it verifies |
|---|---|---|
| I01 | [W3C APG — Button](https://www.w3.org/WAI/ARIA/apg/patterns/button/) | Actions, toggle buttons, and the distinction between buttons and links. |
| I02 | [GOV.UK — Text input](https://design-system.service.gov.uk/components/text-input/) | Short, single-line text entry. |
| I03 | [GOV.UK — Textarea](https://design-system.service.gov.uk/components/textarea/) | Longer answers spanning multiple lines. |
| I04 | [USWDS — Search](https://designsystem.digital.gov/components/search/) | Finding content by entering search terms. |
| I05 | [W3C APG — Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) | Editable and select-only choices, suggestions, and allowed versus arbitrary values. |
| I06 | [GOV.UK — Select](https://design-system.service.gov.uk/components/select/) | Choosing one value from a compact list. |
| I07 | [W3C APG — Listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/) | Single- and multiple-selection lists; options are not containers for arbitrary interactive controls. |
| I08 | [W3C APG — Radio group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/) | Mutually exclusive choices and the five-star rating example. |
| I09 | [W3C APG — Checkbox](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/) | Independent checked states and mixed group state. |
| I10 | [W3C APG — Switch](https://www.w3.org/WAI/ARIA/apg/patterns/switch/) | Binary on/off meaning and relationship to checkboxes and toggle buttons. |
| I11 | [W3C APG — Slider](https://www.w3.org/WAI/ARIA/apg/patterns/slider/) | Selecting a value along a range; includes rating and media-seek examples. |
| I12 | [W3C APG — Multi-thumb slider](https://www.w3.org/WAI/ARIA/apg/patterns/slider-multithumb/) | Several related values, including minimum and maximum price. |
| I13 | [W3C APG — Spinbutton](https://www.w3.org/WAI/ARIA/apg/patterns/spinbutton/) | Increasing and decreasing discrete values, often with direct text entry. |
| I14 | [USWDS — Date picker](https://designsystem.digital.gov/components/date-picker/) | Choosing a date in calendar context and distinguishing familiar typed dates. |
| I15 | [MDN — input type=time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time) | A time-of-day control; appearance varies by browser and platform. |
| I16 | [USWDS — File input](https://designsystem.digital.gov/components/file-input/) | Choosing files and drag-and-drop selection. Does not prove storage or upload completion. |
| I17 | [GOV.UK — Password input](https://design-system.service.gov.uk/components/password-input/) | Revealing and hiding entered password text. |
| I18 | [GOV.UK — Character count](https://design-system.service.gov.uk/components/character-count/) | Character or word limits and remaining/exceeded counts. |
| I19 | [W3C APG — Toolbar example](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/examples/toolbar/) | Text formatting controls such as bold, alignment, and font size. A rich editor is a composite feature. |
| I20 | [MDN — contenteditable](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable) | Editing displayed content and the distinction between rich and plain text. Does not define a complete editor or saving workflow. |
| I21 | [MDN — input type=color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color) | Choosing a color through a picker or entered color value. |
| I22 | [USWDS — Input mask](https://designsystem.digital.gov/components/input-mask/) | Formatting constraints that guide input; a named feature, not a blanket recommendation to mask every field. |
| I23 | [GOV.UK — Error message](https://design-system.service.gov.uk/components/error-message/) | Feedback on a user's answer, distinct from service failures. |
| I24 | [W3C APG — Table](https://www.w3.org/WAI/ARIA/apg/patterns/table/) | Static tabular structure and distinction from an interactive grid. |
| I25 | [Carbon — Data table guidelines](https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines) | Sorting columns, selecting rows, and performing batch actions. |
| I26 | [Carbon — Filtering](https://www.carbondesignsystem.com/building-blocks/core/patterns/filtering) | Narrowing results with selected attributes; immediate and batched application. |
| I27 | [W3C APG — Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) | Interactive tabular widgets and examples with cell editing. Not every table with a button needs the grid pattern. |
| I28 | [web.dev — Virtualize large lists with react-window](https://web.dev/articles/virtualize-long-lists-react-window) | Rendering a small visible window of a large collection; distinguishes windowing from adding data. The library is an illustrative implementation, not a recommendation. |
