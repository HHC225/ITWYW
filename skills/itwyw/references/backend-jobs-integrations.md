# Backend: jobs, integrations, notifications, and billing

Use this file when a person describes connecting systems, doing work later, keeping updates flowing, coping with failures, sending alerts, or charging customers. Name the requested behavior before discussing a transport or pattern. These entries are vocabulary, not an architecture or vendor recommendation. Everyday phrases are original examples; sources verify the underlying concepts. Last verified: 2026-10-25.

## Contents

- [Connecting systems and showing updates](#connecting-systems-and-showing-updates)
- [Background work and recovery](#background-work-and-recovery)
- [Limits, speed, and consistency](#limits-speed-and-consistency)
- [Notifications](#notifications)
- [Payments and billing](#payments-and-billing)
- [Important distinctions](#important-distinctions)
- [Sources](#sources)

## Connecting systems and showing updates

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-J01 | HTTP API; request-response integration | “Let our other system fetch these orders.” / “Send this form to the booking service.” | Lets one program ask another for information or an action. | An on-demand request, event notification, scheduled transfer, or ongoing conversation? | MDN-HTTP |
| BE-J02 | Webhook; event callback; server-to-server event delivery | “Tell our system when a payment succeeds.” / “Update us whenever the supplier changes an order.” | One service calls another when an event happens. | Can the receiver accept incoming requests? How should repeats, delays, and missing events be handled? | STRIPE-WEBHOOKS |
| BE-J03 | Webhook signature verification; authenticated event reception | “Only trust updates really sent by the payment service.” / “Make sure nobody can fake that delivery notice.” | Checks a received event's proof before trusting its sender. | What signature and replay checks does the sender support? A secret-looking address is not proof. | STRIPE-WEBHOOKS |
| BE-J04 | Polling; periodic status checks | “Check every few seconds for a reply.” / “Refresh the order status automatically.” | Repeatedly asks whether something has changed. | How often is useful, and is a delayed answer acceptable? | AZ-ASYNC |
| BE-J05 | Server-sent events; SSE; one-way event stream | “Keep sending new progress messages to this open page.” / “Update the live feed without repeated refreshes.” | Keeps a connection open for the server to send events to the page. | Are updates mainly server-to-browser? Browser actions can still use separate requests. | MDN-SSE |
| BE-J06 | WebSocket; two-way live messaging connection | “Let both sides send chat messages immediately.” / “Keep sending game actions and updates both ways.” | Keeps a two-way connection open between a client and server. | Is two-way messaging needed, and how should reconnecting or missed messages work? | MDN-WEBSOCKET |

## Background work and recovery

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-J07 | Background job; asynchronous task; worker task | “Let the report finish while I do something else.” / “Process the upload after the page responds.” | Accepts work now and finishes it separately. | Must it survive a closed page or service restart, and how will the result be found? | AZ-ASYNC |
| BE-J08 | Job queue; work queue; task backlog | “Keep incoming work waiting until a worker is free.” / “Don't lose requests when everyone submits at once.” | Holds work for workers to collect and process. | What happens on overload, worker failure, or repeated delivery? A queue alone does not guarantee completion. | RABBIT-QUEUES; RABBIT-RELIABILITY |
| BE-J09 | Scheduled job; recurring task; delayed task; scheduler | “Send the summary every Monday.” / “Run this tomorrow at nine.” | Starts work at a chosen time or repeating schedule. | Which time zone, daylight-saving rule, missed-run behavior, and allowed delay? | AWS-SCHEDULE |
| BE-J10 | Automatic retry; transient-failure recovery | “Try again if the connection briefly fails.” / “Give a temporary error another chance.” | Repeats a failed attempt when trying again may help. | Is the failure temporary, how many attempts, and could repeating the action cause a duplicate? | AWS-RETRY |
| BE-J11 | Exponential backoff and jitter; spaced retries | “Wait longer between repeated failures.” / “Don't have everyone retry at the same moment.” | Spaces retries apart and varies their timing to reduce crowding. | Is this retry spacing, a request-rate limit, or waiting after typing in the interface? | AWS-RETRY |
| BE-J12 | Dead-letter queue; failed-job holding area; manual replay | “Keep jobs that keep failing for someone to inspect.” / “Let us fix bad items and try them again later.” | Separates failed work so it can be examined and handled. | Which failures go there, who is alerted, and what makes replay safe? | RABBIT-DLX |
| BE-J13 | Idempotency; duplicate-request protection; idempotency key | “Don't charge twice if I press again.” / “A retried order should still be one order.” | Makes repeats of the same intended request avoid an extra effect. | How is the same request recognized, for how long, and across which side effects? | STRIPE-IDEMPOTENCY |
| BE-J14 | Job status and progress tracking; operation status | “Tell me whether the import finished.” / “Show how much of the report is done.” | Keeps a checkable record of unfinished, successful, or failed work. | Is a state enough, or is measurable progress available? Avoid invented percentage precision. | AZ-ASYNC |
| BE-J15 | Job cancellation; cooperative cancellation | “Stop the export I started.” / “Cancel the remaining import work.” | Requests that unfinished work stop and records the result. | Stop active work or only later steps? Completed effects may need separate reversal. | AZ-ASYNC; AZ-COMPENSATE |
| BE-J16 | Request timeout; operation deadline | “Don't leave this waiting forever.” / “Give up waiting after thirty seconds.” | Limits how long a caller waits for an answer. | Stop waiting, stop the remote work, or both? A timeout does not prove the action failed. | AWS-RETRY |
| BE-J23 | Compensating action; compensation workflow; saga compensation | “Refund the charge if the booking cannot be completed.” / “Release what we reserved if a later step fails.” | Uses follow-up actions to counter completed steps across separate systems. | What can be reversed, and what needs manual help? This is not one database rollback. | AZ-COMPENSATE |

## Limits, speed, and consistency

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-J17 | Rate limiting; request throttling; burst control | “Stop one person sending hundreds of requests each second.” / “Slow down clients that hit us too often.” | Limits how quickly requests may arrive from a chosen source. | Limit by account, credential, device, or address? Which rate window and burst allowance? | MDN-429 |
| BE-J18 | Usage quota; allowance; consumption cap | “Each team gets a thousand exports a month.” / “Warn me when my storage allowance is nearly used.” | Tracks how much of a chosen allowance has been used. | A warning or a strict stop? What is counted, and when does the allowance reset? | AWS-QUOTAS |
| BE-J19 | Caching; reusable result cache | “Don't calculate the same result every time.” / “Keep popular data ready to load faster.” | Reuses a saved copy of an earlier result. | How old may the copy be, and is it private to a person or organization? | AZ-CACHE |
| BE-J20 | Cache invalidation; cache refresh; stale-data handling | “Stop showing the old price after I change it.” / “Refresh saved results when their source changes.” | Removes or refreshes a reused copy when it should no longer be trusted. | Refresh on a change, after a time limit, or on the next request? | AZ-CACHE |
| BE-J21 | Eventual consistency; delayed synchronization | “It is okay if reports catch up a little later.” / “The change appears here before it reaches the other view.” | Allows a change to appear in different copies at different times. | How stale is acceptable, and which decisions require the newest confirmed data? | AWS-CONSISTENCY |
| BE-J22 | Event ordering; stale-event protection; version-aware processing | “Don't let an old update replace a newer one.” / “A delayed message must not undo the latest status.” | Uses agreed ordering or version rules when updates arrive at different times. | Order per item or across everything? Arrival time and timestamps may not be enough. | STRIPE-WEBHOOKS; RABBIT-QUEUES |

## Notifications

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-J24 | Delivery status tracking; delivery receipts; notification outcomes | “Tell me if the reminder reached their phone.” / “Show failed messages so we can follow up.” | Tracks the delivery states a message provider reports. | Accepted, sent, delivered, or read? Which states does this channel actually report? | TWILIO-STATUS |
| BE-J25 | Transactional email notification; email alert | “Email me when my order ships.” / “Send a receipt after payment.” | Sends an email because a relevant event happened. | Which event and recipient? Is it an essential message or an optional subscription? | AWS-EMAIL |
| BE-J26 | SMS notification; text-message alert | “Text me before the appointment.” / “Send urgent updates to my phone number.” | Sends a message to a phone number through a messaging service. | Which recipients and events? Is the request for SMS or an app notification? | TWILIO-STATUS |
| BE-J27 | Push notification; web push; device push | “Alert my phone even when I am not looking at the app.” / “Send a browser alert when there is a new reply.” | Sends an update through a device or browser push subscription. | Which devices, permission state, and fallback? Receiving push and showing an alert are separate steps. | MDN-PUSH |
| BE-J28 | In-app notification inbox; unread activity feed | “Keep my alerts under the bell.” / “Show unread updates when I return.” | Saves notifications inside the app with states such as read or unread. | Persistent inbox entries, live temporary pop-ups, or both? | GH-NOTIFICATIONS |
| BE-J29 | Notification preferences; notification subscriptions; opt-out | “Let me choose which alerts I get.” / “Mute these updates without leaving the project.” | Stores a person's choices about which updates to receive and where. | Which topics and channels can change, and which messages must still be sent? | GH-PREFERENCES |

## Payments and billing

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-J30 | Payment processing; one-time payment; payment status | “Let customers pay for an order.” / “Mark the order paid when the payment really succeeds.” | Requests payment and follows its confirmed result. | One payment or recurring billing? What confirmed state allows the order to be fulfilled? | STRIPE-PAYMENTS |
| BE-J31 | Subscription billing; recurring billing; subscription lifecycle | “Charge members each month.” / “Let customers upgrade, cancel, or restart their plan.” | Manages repeated billing and the changing state of a subscription. | Renewal, trial, failed payment, cancellation, and feature access may follow different rules. | STRIPE-SUBSCRIPTIONS |
| BE-J32 | Usage metering; usage-based billing; consumption billing | “Charge for how many messages we send.” / “Bill customers for the storage they use.” | Records billable activity so charges can follow actual use. | What counts as one unit, how are repeats corrected, and which billing period receives late usage? | STRIPE-USAGE |
| BE-J33 | Refund processing; partial refund; payment reversal | “Give the customer their money back.” / “Refund only the missing item.” | Requests the return of some or all of a completed payment. | Cancel an unfinished payment or refund a completed one? A request may still be pending. | STRIPE-REFUNDS |

## Important distinctions

- **Choose by direction and timing.** An API call asks for a response. A webhook notifies another server. Polling asks repeatedly. SSE sends events toward an open client; WebSocket supports two-way messages. None of these names alone promises zero delay or recovery of missed events. (`MDN-HTTP`, `STRIPE-WEBHOOKS`, `AZ-ASYNC`, `MDN-SSE`, `MDN-WEBSOCKET`)
- **Repeated delivery is possible.** A queue or webhook may redeliver. Name the intended business effect and its duplicate-handling rules; never turn “use a queue” into a universal exactly-once promise. (`RABBIT-RELIABILITY`, `STRIPE-WEBHOOKS`)
- **Three duplicate problems need different names.** Idempotency concerns repeating one intended action. A unique constraint concerns distinct saved records sharing a forbidden value. UI debounce concerns when the interface sends a request. These can be combined but are not substitutes. (`STRIPE-IDEMPOTENCY`; see `BE-D12`)
- **Time limits do not erase effects.** A timeout can mean the caller stopped waiting while the other system continued. Cancellation asks unfinished work to stop; compensation handles already completed effects. (`AWS-RETRY`, `AZ-ASYNC`, `AZ-COMPENSATE`)
- **Freshness needs a stated requirement.** Caching reuses results; eventual consistency permits copies to lag. Ask which operation needs fresh information and how much delay is acceptable. Avoid inventing a guaranteed catch-up time. (`AZ-CACHE`, `AWS-CONSISTENCY`)
- **Sending is not the same as reading.** Provider acceptance, delivery, and read status are separate, channel-dependent observations. Push receipt and a visible device alert are also different. (`TWILIO-STATUS`, `MDN-PUSH`)
- **Billing and access are separate.** A payment result, subscription state, metered usage, and feature entitlement answer different questions. Ask which states should enable or disable the feature; see `BE-A27`. (`STRIPE-PAYMENTS`, `STRIPE-SUBSCRIPTIONS`, `STRIPE-USAGE`)

## Sources

These primary sources verify the names and boundaries. Provider-specific limits, policies, and guarantees are not generalized.

- **MDN-HTTP** — [MDN: Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview). Verified: client requests, server responses, and HTTP communication.
- **STRIPE-WEBHOOKS** — [Stripe: Receive Stripe events in your webhook endpoint](https://docs.stripe.com/webhooks). Verified: event callbacks, signature checks, duplicate delivery, and lack of event-order guarantees.
- **AZ-ASYNC** — [Microsoft: Asynchronous Request-Reply pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply). Verified: background processing, polling, operation status, and cancellation requests.
- **MDN-SSE** — [MDN: Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events). Verified: a one-way server-to-client event connection and reconnection behavior.
- **MDN-WEBSOCKET** — [MDN: WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Verified: two-way client-server communication and connection limitations.
- **RABBIT-QUEUES** — [RabbitMQ: Queues](https://www.rabbitmq.com/docs/queues). Verified: queue buffering and ordering limits when delivery and consumption conditions change.
- **RABBIT-RELIABILITY** — [RabbitMQ: Reliability Guide](https://www.rabbitmq.com/docs/reliability). Verified: failures, acknowledgments, retransmission, and possible duplicate delivery.
- **AWS-SCHEDULE** — [Amazon EventBridge Scheduler: Schedule types](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html). Verified: repeating and one-time schedules, time zones, and daylight-saving behavior.
- **AWS-RETRY** — [AWS Builders' Library: Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/). Verified: bounded waiting, temporary failures, retry spacing, jitter, and side effects after timeouts.
- **RABBIT-DLX** — [RabbitMQ: Dead Letter Exchanges](https://www.rabbitmq.com/docs/dlx). Verified: routing messages after rejection, expiry, length limits, or delivery limits; dead lettering is not guaranteed repair.
- **STRIPE-IDEMPOTENCY** — [Stripe API: Idempotent requests](https://docs.stripe.com/api/idempotent_requests). Verified: identifying repeated requests and avoiding repeated operations within the service's documented rules.
- **AZ-COMPENSATE** — [Microsoft: Compensating Transaction pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction). Verified: undoing effects of completed steps, business-specific rules, and possible manual intervention.
- **MDN-429** — [MDN: 429 Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/429). Verified: rate limiting and possible retry timing information.
- **AWS-QUOTAS** — [Amazon API Gateway: Usage plans and API keys for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html). Verified: quota periods versus rate throttling. This provider's limits are best effort; the catalogue does not claim universal hard enforcement.
- **AZ-CACHE** — [Microsoft: Cache-Aside pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside). Verified: reusable cached copies, staleness, expiry, and invalidation.
- **AWS-CONSISTENCY** — [Amazon DynamoDB: Read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html). Verified: reads that can lag a recent write and alternatives requiring fresher data.
- **TWILIO-STATUS** — [Twilio: Track the Message Status of Outbound Messages](https://www.twilio.com/docs/messaging/guides/track-outbound-message-status). Verified: messaging delivery states and channel-dependent read status.
- **AWS-EMAIL** — [Amazon SES: What is Amazon SES?](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html). Verified: transactional and other application email delivery.
- **MDN-PUSH** — [MDN: Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API). Verified: push subscriptions and receiving messages through a service worker when a page is not active.
- **GH-NOTIFICATIONS** — [GitHub: REST API endpoints for notifications](https://docs.github.com/en/rest/activity/notifications). Verified: a persisted notification inbox and read/unread handling as a concrete example.
- **GH-PREFERENCES** — [GitHub: Configuring notifications](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications). Verified: choosing notification delivery destinations and subscriptions.
- **STRIPE-PAYMENTS** — [Stripe: The Payment Intents API](https://docs.stripe.com/payments/payment-intents). Verified: a payment's changing status and confirmed outcome; used as a terminology source, not an API recommendation.
- **STRIPE-SUBSCRIPTIONS** — [Stripe: How subscriptions work](https://docs.stripe.com/billing/subscriptions/overview). Verified: recurring invoices, collection, subscription states, and cancellation.
- **STRIPE-USAGE** — [Stripe: Record usage for billing](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage). Verified: recording customer consumption for usage-based charges.
- **STRIPE-REFUNDS** — [Stripe: Refund and cancel payments](https://docs.stripe.com/refunds). Verified: canceling incomplete payments, full or partial refunds, and refund states.
