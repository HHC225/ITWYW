# Sources and coverage

Research date: **2026-10-25**. The catalogue uses primary documentation from standards bodies, browser documentation, official design systems, service maintainers, and platform documentation. It names capabilities; it does not select a vendor or promise an implementation's performance or security.

## Coverage

| Reference | Mapping entries | Scope |
| --- | ---: | --- |
| [Frontend layout and navigation](frontend-layout-navigation.md) | 28 | Structure, navigation, panels, hierarchy, content browsing. |
| [Frontend inputs and data](frontend-inputs-data.md) | 29 | Forms, selection, editing, tables, search controls. |
| [Frontend overlays and feedback](frontend-overlays-feedback.md) | 28 | Dialogs, help, status, loading, media controls. |
| [Frontend visual style and motion](frontend-visual-motion.md) | 28 | Responsive behavior, focus/hover, animation, scroll, appearance. |
| [Backend data and search](backend-data-search.md) | 39 | Persistence, correctness, search, content workflows, collaboration. |
| [Backend identity and access](backend-identity-access.md) | 27 | Identity, sessions, permission, sharing, entitlements. |
| [Backend jobs and integrations](backend-jobs-integrations.md) | 33 | APIs, jobs, idempotency, notifications, integration, billing state. |
| [Infrastructure hosting and network](infra-hosting-network.md) | 28 | Compute, domains, routing, private access, traffic handling. |
| [Infrastructure delivery and operations](infra-delivery-operations.md) | 28 | Build, release, environments, configuration, operational costs. |
| [Infrastructure reliability and data](infra-reliability-data.md) | 28 | Signals, capacity, continuity, recovery, storage. |
| **Total** | **296** | **592 original everyday-language example phrases.** |

These are 296 mapping entries, not a claim that every label is globally unique across layers. For example, a screen can expose filtering while the backend applies the filter, and an application or edge service can enforce rate limits. Aliases remain within their entry. The catalogue is broad but open-ended; infer unfamiliar intentions using the workflow and verify missing terms when necessary.

The ten catalogues contain **255 source entries covering 254 distinct source URLs** at publication. Sources are colocated with the relevant entries so a small lookup retains its evidence. A citation establishes the stated concept or mechanism, not the user's actual system behavior. The plain explanations, example phrases, questions, and motion storyboards are original synthesis.

## Source families

| Primary source family | Use |
| --- | --- |
| [W3C ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/patterns/) | Widget behavior, distinctions, accessibility semantics. APG is guidance; source-specific draft status is preserved. |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | HTML, CSS, browser APIs, input behavior, HTTP. |
| [USWDS](https://designsystem.digital.gov/components/), [GOV.UK Design System](https://design-system.service.gov.uk/components/), [Carbon](https://www.carbondesignsystem.com/), [Material Design](https://m3.material.io/) | Conventional component names and behavior within established design systems. |
| [PostgreSQL documentation](https://www.postgresql.org/docs/current/) | Stored records, queries, transactions, constraints, search, concurrency. |
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Authentication, authorization, file handling, session and tenant boundaries. |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) and [OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749) | Distinguish identity verification from delegated authorization. |
| [Stripe documentation](https://docs.stripe.com/), [RabbitMQ documentation](https://www.rabbitmq.com/docs), [Redis documentation](https://redis.io/docs/latest/) | Request duplication, events, queues, billing states, expiring data. Product-specific guarantees are not generalized. |
| [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/patterns/), [AWS documentation](https://docs.aws.amazon.com/), [Google Cloud documentation](https://docs.cloud.google.com/) | Resilience patterns, compute, delivery, networks, storage, cost controls. |
| [Kubernetes documentation](https://kubernetes.io/docs/), [Docker documentation](https://docs.docker.com/), [OpenTelemetry](https://opentelemetry.io/docs/) | Packaging, orchestration, probes, logs, metrics, traces. |
| Official GitHub, WordPress, Firebase, Twilio, Stately, Fluid Framework, and tus documentation | Concrete product/workflow examples where a general label needs a real behavior anchor. Exact URLs and scopes appear in the catalogues. |

Material Design pages exposed script-rendered shells during research; those entries used indexed excerpts of the official pages. No third-party mirror was substituted. Common labels such as bento grid and glassmorphism are identified as conventions; their sources verify the underlying layout or visual mechanism rather than an invented standard.

## Screenshot coverage

The source screenshot was an example of the user's intended vocabulary problem. All 24 of its labels are represented; its artwork is not included in this skill. The expanded catalogue also covers nonvisual behavior.

| Screenshot label | Catalogue entry |
| --- | --- |
| Hero Section | FE-001 |
| Responsive Layout | FE-085 |
| Card Layout | FE-002 |
| Bento Grid | FE-003 |
| Sidebar Layout | FE-005 |
| Sticky Header | FE-013 |
| Split Layout | FE-006 |
| Tabs | FE-015 |
| Accordion | FE-016 |
| Modal / Dialog | FE-057; FE-058 distinguishes non-modal dialogs |
| Drawer | FE-059 |
| Dropdown | FE-061; FE-034 distinguishes value selection |
| Tooltip | FE-064 |
| Toast / Snackbar | FE-065 |
| Carousel | FE-079 |
| Skeleton Loading | FE-070 |
| Hover Effect | FE-091 |
| Scroll Reveal | FE-096 |
| Stagger Animation | FE-095 |
| Smooth Transition | FE-094 |
| Glassmorphism | FE-102 |
| Parallax Scrolling | FE-098 |
| Scroll Snap | FE-099 |
| Micro-interaction | FE-101 |

## Maintain evidence quality

When changing a mapping, read its primary source and retain the distinction that makes it useful. Do not paste long passages into the catalogue. Replace dead links with an official successor only after checking that it supports the same claim. Treat example utterances as illustrative, not an exhaustive training set or a measured recognition benchmark. Update counts when entries or phrases change, and evaluate ambiguous examples in their response language.
