# Backend: data, search, and content workflows

Use this file when a person describes saving information, finding it, changing it, or moving content through a process. These are feature names to confirm with the person, not a database or vendor recommendation. Everyday phrases are original examples; sources verify the underlying concepts. Last verified: 2026-10-25.

## Contents

- [Saving and changing information](#saving-and-changing-information)
- [Keeping data correct](#keeping-data-correct)
- [Moving files and records](#moving-files-and-records)
- [Finding and listing information](#finding-and-listing-information)
- [Content and teamwork](#content-and-teamwork)
- [Important distinctions](#important-distinctions)
- [Sources](#sources)

## Saving and changing information

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-D01 | Server-side persistence; shared saved data | “Keep my list when I come back.” / “Show the same list on my phone.” | Keeps information with the service so permitted devices can fetch it later. | Must it follow the account across devices, or only survive in this browser? | PG-TX; MDN-LOCAL |
| BE-D02 | Create a record; add item; CRUD create | “Let me add a customer.” / “Save a new appointment.” | Adds one new item to the saved collection. | Is this a new item, a copy, or a change to an existing item? | PG-INSERT |
| BE-D03 | Read or retrieve records; detail lookup; CRUD read | “Open the order details.” / “Show what we saved last time.” | Fetches saved information for someone allowed to see it. | One known item, a list, or a search? | PG-SELECT |
| BE-D04 | Update a record; edit; CRUD update | “Let me change their address.” / “Correct that order.” | Changes information inside an existing saved item. | Should the item's identity stay the same, and can someone else edit it too? | PG-UPDATE |
| BE-D05 | Hard delete; permanent record deletion; CRUD delete | “Remove this customer record completely.” / “Delete the saved test orders.” | Removes an item from the main saved collection. | Is recovery required? Does the request also cover old copies and backups? | PG-DELETE |
| BE-D06 | Autosave; automatic saving | “Save as I type.” / “Don't make me keep pressing Save.” | Saves edits automatically while someone works. | Save to this browser or the server? Should saved edits become public? | WP-REVISIONS; MDN-LOCAL |
| BE-D07 | Draft and publish workflow; unpublished content | “Let me finish this later.” / “Keep changes hidden until I press Publish.” | Keeps unfinished work separate from the version other people can see. | Is the need automatic saving, private unfinished work, or an approval step? | WP-STATUS |
| BE-D08 | Soft delete; trash; recoverable deletion | “Put it in a bin first.” / “Let me bring back deleted projects.” | Hides an item while keeping enough information to restore it. | How long can it be restored, and who may still see it? | MS-SOFTDELETE |
| BE-D09 | Undo; reverse a completed action | “Take back my last change.” / “Undo the move I just made.” | Applies a new action that reverses an earlier action where possible. | One action or an older saved version? Can its outside effects be reversed? | AZ-COMPENSATE |
| BE-D10 | Revision history; version history; restore version | “Show yesterday's version.” / “Let me recover an older draft.” | Keeps earlier versions so people can compare or restore them. | Must old content be restored, or is a record of who changed it enough? | WP-REVISIONS |

## Keeping data correct

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-D11 | Server-side validation; required fields; business rules | “Don't accept a blank name.” / “The end date must come after the start date.” | Checks incoming information before accepting it. | Must this rule hold even when someone skips the form and calls the service directly? | OW-VALIDATE; PG-CONSTRAINTS |
| BE-D12 | Unique constraint; uniqueness rule | “No two accounts can use this username.” / “Each booking reference must be different.” | Stops saved items from sharing a value that must be unique. | Unique across everyone, one company, or several fields together? | PG-CONSTRAINTS |
| BE-D13 | Referential integrity; foreign key; related-record protection | “Every order must belong to a real customer.” / “Don't leave payments attached to a missing invoice.” | Keeps links between saved items pointing to valid items. | If the parent is deleted, should related items stay, disappear, or block deletion? | PG-CONSTRAINTS |
| BE-D14 | Database transaction; atomic update; all-or-nothing save | “Save the order and its lines together.” / “If one part fails, save none of it.” | Makes several changes in one database succeed together or save nothing. | Is all work inside one transaction, or does it include outside services and payments? | PG-TX |
| BE-D15 | Optimistic concurrency control; version check; conflict detection | “Warn me if someone changed this first.” / “Don't silently overwrite my teammate's work.” | Checks that the saved item still matches the version you edited. | Should a conflict ask the user, retry, or merge? This does not itself merge edits. | MS-CONCURRENCY |
| BE-D16 | Pessimistic locking; exclusive update lock | “Only one person should change this stock count at a time.” / “Don't let two checkouts take the last item together.” | Temporarily makes competing changes wait while one change finishes. | Is this a short data update or a customer reservation with an expiry time? | PG-LOCKS |
| BE-D17 | Upsert; insert-or-update | “Update existing products and add new ones.” / “If that customer is already there, refresh their details.” | Adds an item when absent and updates the matching item when present. | Which stable key means “the same item,” and which fields may be replaced? | PG-UPSERT |
| BE-D18 | Bulk operation; batch update | “Mark all these orders as shipped.” / “Change the price for every selected product.” | Applies an action to several items in one request or job. | Must all items succeed together, or may each item have its own result? | PG-UPDATE; PG-TX |
| BE-D33 | Duplicate detection and record merging; data deduplication | “Find customers we entered twice.” / “Combine these duplicate contacts.” | Finds likely repeated items and helps combine the right ones. | Are duplicates already stored, or should new duplicates be blocked? Who chooses the surviving values? | MS-DEDUPE |
| BE-D34 | Data expiry; time-to-live; retention cleanup | “Remove temporary codes after ten minutes.” / “Clear old temporary results after a week.” | Makes temporary information stop being usable after a chosen time. | Should it become unusable immediately, or be physically cleaned up later? Are old copies in scope? | REDIS-EXPIRE |

## Moving files and records

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-D19 | Data import; CSV import; field mapping | “Bring in my spreadsheet of customers.” / “Load the old product list.” | Turns rows from a file into the service's saved items. | Which columns match which fields? Should existing items be updated, skipped, or duplicated? | PG-COPY; PG-UPSERT |
| BE-D20 | Data export; downloadable report | “Download all my orders as a spreadsheet.” / “Give me a file of these search results.” | Packages permitted information into a file someone can keep. | Which format, columns, and rows? Current page, current filter, or every permitted item? | PG-COPY |
| BE-D21 | File upload; attachment storage; upload validation | “Let customers attach a receipt.” / “Store a photo with each report.” | Accepts a file and attaches it to the right saved item. | Which sizes and file types are allowed, and who can fetch it afterward? | OW-UPLOAD |
| BE-D22 | Resumable upload; interrupted-upload recovery | “Continue the upload after my connection drops.” / “Don't restart a huge file from zero.” | Continues sending a file from a saved stopping point. | Must it resume after a tab closes too, and how long should unfinished uploads remain? | TUS |

## Finding and listing information

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-D23 | Exact-match lookup; equality search | “Find this exact order number.” / “Only show the customer with this email.” | Finds items whose chosen field matches the requested value. | Should capitals, spaces, accents, or punctuation count as different? | PG-SELECT |
| BE-D24 | Partial-text search; prefix search; substring matching | “Find names starting with Sam.” / “Find anything containing this bit of text.” | Finds text that starts with or contains the supplied letters. | Must the letters appear exactly, or should spelling mistakes also match? | PG-PATTERN |
| BE-D25 | Fuzzy search; typo-tolerant matching; similarity search | “Find it even if I misspell it.” / “Show names close to the one I typed.” | Finds text that looks similar even when some letters differ. | Are near spellings wanted, or related meanings and ideas? | PG-FUZZY |
| BE-D26 | Full-text search; document search; relevance ranking | “Search inside all the articles.” / “Put the most relevant documents first.” | Searches words in longer writing and can rank useful matches. | Which language and fields? Need word forms, exact phrases, typo tolerance, or meaning-based search? | PG-FTS |
| BE-D27 | Filtering; faceted filtering; query conditions | “Only show unpaid orders from this month.” / “Show blue items under twenty dollars.” | Keeps only items that pass the chosen conditions. | Should several choices mean “all of these” or “any of these”? | PG-FILTER |
| BE-D28 | Sorting; ordering; multi-field sort | “Put the newest first.” / “Sort by price, then by name.” | Arranges the same items in a chosen order. | What breaks ties, and where should missing values go? | PG-SORT |
| BE-D29 | Database index; search index | “Finding an order number gets slow with more customers.” / “Make these repeated lookups quicker.” | Keeps an extra lookup guide that can make some searches faster. | Which measured lookup is slow? An index does not decide what “matching” means. | PG-INDEX |
| BE-D30 | Offset pagination; numbered pages | “Show twenty items per page.” / “Let me jump to page five.” | Returns a slice after skipping a chosen number of items. | Do people need page numbers, and can the list change while they browse? | PG-PAGES |
| BE-D31 | Cursor pagination; continuation token | “Give me the next batch after these.” / “Keep loading older messages.” | Continues a list from a saved place or marker. | Need arbitrary page jumps or a next/previous flow? What defines stable order? | STRIPE-PAGES |
| BE-D32 | Aggregation; grouped totals; summary reporting | “Show sales totals by month.” / “Count open tickets for each team.” | Combines many items into counts, totals, or other summaries. | Which grouping, date range, time zone, and included statuses define the number? | PG-AGG |

## Content and teamwork

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-D35 | Comments and replies; discussion threads | “Let people discuss each report.” / “Let me reply under a customer's comment.” | Stores messages linked to an item, with replies when needed. | Flat comments or nested replies? Who may read, edit, and delete them? | WP-COMMENTS |
| BE-D36 | Content moderation; approval queue; report-and-review | “Check comments before everyone sees them.” / “Let us remove reported posts.” | Holds or reviews content so a permitted reviewer can decide what stays visible. | Review before publishing or after reports? Human decisions, automatic screening, or both? | WP-COMMENTS |
| BE-D37 | Human approval workflow; review and sign-off | “A manager must approve expenses first.” / “Let someone request changes before this goes live.” | Waits for a person's decision before allowing the next step. | Which approver, how many approvals, and what happens after edits or rejection? | GH-REVIEWS |
| BE-D38 | Workflow states; state machine; allowed transitions | “Orders go from paid to packed to shipped.” / “A closed ticket must be reopened before editing.” | Gives an item named stages and rules for moving between them. | Which moves are allowed, who can make them, and which actions happen on each move? | STATELY-STATES; STATELY-TRANSITIONS |
| BE-D39 | Collaborative editing; shared document synchronization | “Let us edit the same document together.” / “Combine our changes while we both type.” | Shares edits and resolves overlapping changes using agreed rules. | Whole-record conflict warnings or simultaneous merged edits? Presence indicators alone do not provide merging. | FLUID-DDS; MS-CONCURRENCY |

## Important distinctions

- **Saving:** persistence answers where information survives; autosave answers when it is saved; a draft answers who can see unfinished work. Local browser storage alone does not establish account-wide synchronization. (`PG-TX`, `MDN-LOCAL`, `WP-REVISIONS`, `WP-STATUS`)
- **Reversing:** trash restores a hidden item; undo reverses an action; version history restores content. A completed action involving another service may need a compensating action, and some effects cannot be fully reversed. (`MS-SOFTDELETE`, `WP-REVISIONS`, `AZ-COMPENSATE`)
- **Duplicates:** a unique constraint protects a chosen data rule; upsert chooses insert versus update; deduplication cleans existing records. For a repeated network request, also consult idempotency in the jobs file. Waiting between clicks in the interface does not establish any of those server guarantees. (`PG-CONSTRAINTS`, `PG-UPSERT`, `MS-DEDUPE`; see `BE-J13`)
- **Atomicity:** “all or nothing” must name the boundary. A database transaction does not automatically include an email, another database, or an external payment. (`PG-TX`, `AZ-COMPENSATE`)
- **Search:** matching decides which items qualify; filtering narrows by conditions; sorting orders results; an index may speed the work. Fuzzy spelling and full-text search do not by themselves mean semantic or AI search. (`PG-PATTERN`, `PG-FUZZY`, `PG-FTS`, `PG-FILTER`, `PG-SORT`, `PG-INDEX`)
- **Collaboration:** detecting a stale edit, locking a record, merging concurrent edits, and showing who is online are different capabilities. Ask what should happen when two people change the same thing. (`MS-CONCURRENCY`, `PG-LOCKS`, `FLUID-DDS`)

## Sources

Official product documentation below verifies terminology or provides a concrete example; it does not prescribe that product. Source keys apply only to the concepts named in their rows. No provider-specific timing, limits, or delivery promises are generalized.

- **PG-TX** — [PostgreSQL: Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html). Verified: committed persistence, atomic transactions, and transaction rollback.
- **MDN-LOCAL** — [MDN: Window.localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage). Verified: origin-scoped browser storage and persistence across browser sessions.
- **PG-INSERT** — [PostgreSQL: Populating a Table With Rows](https://www.postgresql.org/docs/current/tutorial-populate.html). Verified: inserting saved rows.
- **PG-SELECT** — [PostgreSQL: Querying a Table](https://www.postgresql.org/docs/current/tutorial-select.html). Verified: retrieval and equality conditions.
- **PG-UPDATE** — [PostgreSQL: Updates](https://www.postgresql.org/docs/current/tutorial-update.html). Verified: updating selected rows, including multiple rows.
- **PG-DELETE** — [PostgreSQL: Deletions](https://www.postgresql.org/docs/current/tutorial-delete.html). Verified: removing rows from a table; no claim about erasing backups.
- **WP-REVISIONS** — [WordPress: Revisions](https://wordpress.org/documentation/article/revisions/). Verified: autosaves, stored revisions, comparison, and restoration.
- **WP-STATUS** — [WordPress: Post Status](https://wordpress.org/documentation/article/post-status/). Verified: draft, published, pending, and trash states.
- **MS-SOFTDELETE** — [Microsoft: Global Query Filters](https://learn.microsoft.com/en-us/ef/core/querying/filters). Verified: marking data deleted while retaining it and filtering it from ordinary queries.
- **AZ-COMPENSATE** — [Microsoft: Compensating Transaction pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction). Verified: business-specific reversal of completed steps and limits on restoring prior state.
- **OW-VALIDATE** — [OWASP: Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html). Verified: syntactic and semantic checks and validation at the trusted server boundary.
- **PG-CONSTRAINTS** — [PostgreSQL: Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html). Verified: checks, required values, unique keys, and referential integrity.
- **MS-CONCURRENCY** — [Microsoft: Handling Concurrency Conflicts](https://learn.microsoft.com/en-us/ef/core/saving/concurrency). Verified: version-based optimistic checks and handling conflicts.
- **PG-LOCKS** — [PostgreSQL: Explicit Locking](https://www.postgresql.org/docs/current/explicit-locking.html). Verified: competing operations and row-level locks; long-lived reservations require separate rules.
- **PG-UPSERT** — [PostgreSQL: INSERT](https://www.postgresql.org/docs/current/sql-insert.html). Verified: insert-on-conflict behavior and atomic insert-or-update.
- **MS-DEDUPE** — [Microsoft: Merge duplicate records](https://learn.microsoft.com/en-us/power-apps/user/merge-duplicate-records). Verified: detecting possible duplicates and choosing records and values to merge.
- **REDIS-EXPIRE** — [Redis: EXPIRE](https://redis.io/docs/latest/commands/expire/). Verified: key expiration and time-to-live; not a complete data-erasure policy.
- **PG-COPY** — [PostgreSQL: COPY](https://www.postgresql.org/docs/current/sql-copy.html). Verified: moving tabular data between files and stored tables, including CSV.
- **OW-UPLOAD** — [OWASP: File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html). Verified: file validation, size restrictions, storage, and access considerations.
- **TUS** — [tus: Resumable upload protocol 1.0.x](https://tus.io/protocols/resumable-upload). Verified: resumable HTTP uploads and upload offsets.
- **PG-PATTERN** — [PostgreSQL: Pattern Matching](https://www.postgresql.org/docs/current/functions-matching.html). Verified: prefix and substring patterns and case behavior.
- **PG-FUZZY** — [PostgreSQL: pg_trgm](https://www.postgresql.org/docs/current/pgtrgm.html). Verified: similarity-based text matching.
- **PG-FTS** — [PostgreSQL: Introduction to Full Text Search](https://www.postgresql.org/docs/current/textsearch-intro.html). Verified: word normalization, document matching, and relevance ranking.
- **PG-FILTER** — [PostgreSQL: Table Expressions](https://www.postgresql.org/docs/current/queries-table-expressions.html). Verified: WHERE filtering and grouping conditions.
- **PG-SORT** — [PostgreSQL: Sorting Rows (ORDER BY)](https://www.postgresql.org/docs/current/queries-order.html). Verified: explicit ordering, multiple sort keys, and null placement.
- **PG-INDEX** — [PostgreSQL: Introduction to Indexes](https://www.postgresql.org/docs/current/indexes-intro.html). Verified: faster selected lookups and index maintenance costs.
- **PG-PAGES** — [PostgreSQL: LIMIT and OFFSET](https://www.postgresql.org/docs/current/queries-limit.html). Verified: slices, skipped rows, and the need for predictable ordering.
- **STRIPE-PAGES** — [Stripe API: Pagination](https://docs.stripe.com/api/pagination). Verified: cursor-based continuation using a known object marker.
- **PG-AGG** — [PostgreSQL: Aggregate Functions](https://www.postgresql.org/docs/current/tutorial-agg.html). Verified: counts, sums, averages, and grouped summaries.
- **WP-COMMENTS** — [WordPress: Comments in WordPress](https://wordpress.org/documentation/article/comments-in-wordpress/). Verified: comments, replies, approval, spam, and moderation.
- **GH-REVIEWS** — [GitHub: Pull request reviews](https://docs.github.com/en/pull-requests/reference/pull-request-reviews). Verified: approve, request changes, and review requirements as an example of human approval.
- **STATELY-STATES** — [Stately: Finite states](https://stately.ai/docs/finite-states). Verified: named states and state-dependent behavior.
- **STATELY-TRANSITIONS** — [Stately: Events and transitions](https://stately.ai/docs/transitions). Verified: events causing allowed state changes.
- **FLUID-DDS** — [Fluid Framework: Types of distributed data structures](https://fluidframework.com/docs/data-structures/overview). Verified: shared state, consistency, and conflict merge policies for collaborative data.
