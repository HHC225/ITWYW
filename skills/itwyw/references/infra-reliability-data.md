# Infrastructure: reliability and data protection

Use these mappings when someone wants to understand failures, handle demand, keep services available, store files, or recover lost data. A goal such as “never lose anything” needs clarification about acceptable interruption and data loss; it does not prove that one named feature is sufficient.

Verified against the official sources below on 2026-10-25. **28 concepts.** Related references: [Hosting and network access](infra-hosting-network.md), [Delivery and operations](infra-delivery-operations.md).

## Contents

- [Seeing what is happening](#seeing-what-is-happening)
- [Capacity and continuity](#capacity-and-continuity)
- [Backup and recovery](#backup-and-recovery)
- [Storage types and lifecycle](#storage-types-and-lifecycle)
- [Ambiguity traps](#ambiguity-traps)
- [Sources](#sources)

## Seeing what is happening

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-RD-01 | Logging; application logs; operational logs | “Keep a record of what the server did.” / “Show the error messages from last night.” | Logs are dated notes about events in the app or its computers. | Do you need individual event details rather than a chart of totals? | [INF-RD-S01] |
| INF-RD-02 | Metrics; service metrics; infrastructure metrics | “Show how busy the servers are.” / “Graph errors and response times over the day.” | Metrics are measurements that help show how a system changes over time. | Do you need numbers and trends rather than one request's story? | [INF-RD-S02] |
| INF-RD-03 | Distributed tracing; request tracing; traces | “Follow one request through all our services.” / “Show which step made this action slow.” | A trace follows one job through the different parts that handle it. | Do you need the path and timing of one request across components? | [INF-RD-S03] |
| INF-RD-04 | Monitoring; service monitoring | “Keep watching whether our service is healthy.” / “Give us a dashboard of how the app is doing.” | Monitoring regularly watches signals that tell you how the service is behaving. | Which conditions must be watched, and how will healthy behavior be recognized? | [INF-RD-S04] |
| INF-RD-05 | Alerting; operational alert; incident notification | “Tell us when errors suddenly rise.” / “Notify someone when the app stops responding.” | An alert calls attention to a condition that needs action. | Which condition should notify whom, and after how long? | [INF-RD-S05] |
| INF-RD-06 | Liveness health check; liveness probe | “Check whether the app is stuck.” / “Restart an app copy that cannot make progress.” | A small check asks whether the running app is still functioning. | Should failure trigger a restart, rather than only remove incoming traffic? | [INF-RD-S06] |
| INF-RD-07 | Readiness check; readiness probe | “Do not send visitors to a copy until it is ready.” / “Take an unready server out of the traffic pool.” | A readiness check asks whether this app copy can accept requests now. | Can it be alive but temporarily unable to serve traffic? | [INF-RD-S06] |
| INF-RD-08 | Uptime check; synthetic monitoring; synthetic transaction | “Try the site regularly from outside.” / “Check that a pretend visitor can complete the important steps.” | A scheduled test visits the service to see whether a chosen action works. | Is this an outside test rather than a report from inside the server? | [INF-RD-S07] |
| INF-RD-09 | Observability | “Give us enough clues to explain weird failures.” / “Connect the error, timing, and request information.” | Observability gives people clues for understanding why a system behaves as it does. | Do you need to investigate new problems beyond checking known conditions? | [INF-RD-S08] |

## Capacity and continuity

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-RD-10 | Horizontal scaling; scale out; scale in | “Add more app copies when we need capacity.” / “Share work across more servers.” | More workers do the work together; fewer can be used when less work arrives. | Can the work be shared across multiple copies? | [INF-RD-S09] |
| INF-RD-11 | Vertical scaling; scale up; scale down | “Give this server more memory.” / “Move this job to a more powerful machine.” | One worker gets a bigger workbench or more power. | Does one instance need more capacity rather than more instances? | [INF-RD-S09] |
| INF-RD-12 | Autoscaling; automatic scaling; elastic capacity | “Grow capacity when demand rises.” / “Reduce spare servers when traffic falls.” | Rules automatically adjust resources as demand changes. | What demand signal and upper and lower limits should control the change? | [INF-RD-S09] |
| INF-RD-13 | Redundancy; redundant instances (part of high availability, HA) | “Keep another copy ready if one fails.” / “Do not rely on just one machine.” | Extra components help the service continue when one part fails. | Which failure must the extra copy survive, and does it share that failure's cause? | [INF-RD-S10] |
| INF-RD-14 | Failover; automatic failover; standby takeover | “Switch to the spare if the main system fails.” / “Have another location take over during an outage.” | Work moves to a functioning replacement when the usual one fails. | Is a replacement merely present, or is there a tested way to switch to it? | [INF-RD-S10] |

## Backup and recovery

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-RD-15 | Backup; recovery copy | “Keep a copy we can recover after a mistake.” / “Save our data so we can bring it back.” | A backup saves data for later recovery. | Do you need an older recoverable copy rather than another live copy? | [INF-RD-S11] |
| INF-RD-16 | Scheduled backups; backup policy; backup retention policy | “Back things up every night.” / “Keep the last month's recovery copies automatically.” | A policy says what to copy, when to copy it, and how long to keep it. | What data, schedule, retention period, and failure reporting are required? | [INF-RD-S12] |
| INF-RD-17 | Point-in-time recovery; PITR; continuous backup | “Restore the database to just before the mistake.” / “Go back to a chosen time this morning.” | Saved history can rebuild supported data as it was at a chosen time. | Is the required time inside the retained recovery window? | [INF-RD-S13] |
| INF-RD-18 | Snapshot; storage snapshot; volume snapshot | “Take a picture of this disk before the change.” / “Save this storage state at one moment.” | A snapshot records storage as it was at a particular time. | Is the snapshot consistent and recoverable independently of the thing that might fail? | [INF-RD-S14] |
| INF-RD-19 | Replication; data replication; replica | “Keep another copy updated as data changes.” / “Copy new files to our other location automatically.” | Replication keeps another copy updated with changes. | Do you need a current duplicate, or a protected earlier version? | [INF-RD-S15] |
| INF-RD-20 | Disaster recovery; DR; recovery plan | “Get the service running after a major outage.” / “Have a plan if our main location is lost.” | A recovery plan brings the service and its data back after a serious failure. | Does the plan cover people, infrastructure, dependencies, data, and recovery steps? | [INF-RD-S16] |
| INF-RD-21 | Restore test; recovery drill; backup validation | “Prove that our backups actually work.” / “Practice recovering before we need it.” | A practice restore checks whether saved data can be brought back and used. | Has recovery been tested for usability as well as successful backup creation? | [INF-RD-S17] |
| INF-RD-22 | Recovery time objective; RTO | “We must be running again within an hour.” / “How long can this service be unavailable?” | RTO is the target for how quickly service should return. | What is the maximum acceptable recovery time? | [INF-RD-S18] |
| INF-RD-23 | Recovery point objective; RPO | “We can afford to lose at most fifteen minutes of work.” / “How recent must the recovered data be?” | RPO says how much recent work the business can accept losing. | What is the maximum acceptable gap between saved data and the failure? | [INF-RD-S18] |

## Storage types and lifecycle

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-RD-24 | Object storage; bucket storage; blob storage | “Store uploaded pictures and downloads.” / “Keep each file as an item we can fetch by name.” | Each item is stored as a named object with information about it. | Will the app fetch whole objects, rather than use an ordinary shared disk? | [INF-RD-S19] |
| INF-RD-25 | File storage; shared filesystem; network file share | “Give several servers the same folders.” / “Let the app read and write shared files normally.” | Computers share files arranged in folders. | Does the app need shared folder and file behavior? | [INF-RD-S19] |
| INF-RD-26 | Block storage; disk volume; attached disk | “Attach a disk to this server.” / “Keep the machine's data on a separate volume.” | A storage volume acts like a disk the computer can use. | Does the workload need disk-style storage rather than named objects or shared folders? | [INF-RD-S19] |
| INF-RD-27 | Storage lifecycle policy; archival rule; expiration rule | “Move old uploads to cheaper storage.” / “Delete files automatically after their retention period.” | Rules move or remove stored items when they reach a chosen age. | Should old data be archived, deleted, or retained under a separate rule? | [INF-RD-S20] |
| INF-RD-28 | Object versioning; file version retention | “Keep the old file when someone replaces it.” / “Recover an earlier version of an uploaded item.” | Previous versions stay available when the stored item changes. | Do you need an item's past versions rather than a complete system restore? | [INF-RD-S21] |

## Ambiguity traps

- **“Show what went wrong”** can call for logs, metrics, traces, or a combination. Logs describe events; metrics measure behavior; traces connect steps in a request. Monitoring watches chosen conditions; observability helps investigate why something happened. [INF-RD-S01] [INF-RD-S02] [INF-RD-S03] [INF-RD-S04] [INF-RD-S08]
- **“Check that it is up”** might mean liveness, readiness, a reachable URL, or a complete user journey. A process can be alive while a critical action is broken. Ask what successful check represents the user's actual need. [INF-RD-S06] [INF-RD-S07]
- **“Handle more users”** might call for more instances, a bigger instance, caching, reduced work, or fixing a slower dependency. Autoscaling changes capacity; a load balancer routes traffic; a cache reuses work. Measure the actual bottleneck before naming a solution. [INF-RD-S09] See [traffic delivery](infra-hosting-network.md#traffic-delivery-and-routing).
- **“Keep a second copy”** does not distinguish backup, snapshot, versioning, or replication. Replication can copy unwanted changes; snapshot consistency and independence depend on the service; a retained backup still needs a working restore procedure. None alone constitutes a complete disaster recovery plan. [INF-RD-S12] [INF-RD-S14] [INF-RD-S15] [INF-RD-S16] [INF-RD-S17] [INF-RD-S21]
- **“Never go down”** is not a promise to make. Redundancy adds components; failover moves work; recovery restores service after failure. Ask which failures matter and agree recovery targets. [INF-RD-S10] [INF-RD-S16] [INF-RD-S18]
- **“Recover quickly”** leaves two separate questions: how long may recovery take, and how much recent data may be lost? Those are RTO and RPO, respectively. They are objectives, not evidence that the system already meets them. [INF-RD-S18]
- **“Store files”** does not by itself choose object, file, or block storage. Ask how the app needs to access and update the data. Storage replication or durability does not automatically provide the historical recovery the user expects. [INF-RD-S19] [INF-RD-S21]
- **“We have backups”** should prompt questions about what is included, the schedule, retained recovery points, and the latest restore test. A successful copy operation and a successful usable recovery are separate evidence. [INF-RD-S12] [INF-RD-S17]

## Sources

Provider-specific examples verify the vocabulary without selecting a vendor or designing an implementation. The everyday phrases and explanations are original paraphrases.

| Source key | Official title and publisher | Verified topics |
| --- | --- | --- |
| [INF-RD-S01] | OpenTelemetry — Logs | Timestamped event records and structured metadata. |
| [INF-RD-S02] | OpenTelemetry — Metrics | Runtime measurements and associated time and metadata. |
| [INF-RD-S03] | OpenTelemetry — Traces | A request's path through application components. |
| [INF-RD-S04] | Google Cloud — Cloud Monitoring overview | Observing service health and performance; dashboards and monitoring data. |
| [INF-RD-S05] | Google Cloud — Alerting overview | Conditions, alerting policies, and notifications. |
| [INF-RD-S06] | Kubernetes — Liveness, Readiness, and Startup Probes | Restart decisions versus readiness for incoming traffic. |
| [INF-RD-S07] | Google Cloud — Synthetic monitoring overview | Uptime checks and tests of service behavior. |
| [INF-RD-S08] | OpenTelemetry — Observability primer | Investigating a system using its outputs and answering why problems occur. |
| [INF-RD-S09] | Microsoft Learn — Autoscaling | Horizontal and vertical scaling; automatic resource adjustment; dependent bottlenecks. |
| [INF-RD-S10] | Microsoft Learn — Architecture strategies for designing for redundancy | Redundant components, standby resources, failure separation, and failover. |
| [INF-RD-S11] | AWS — What is AWS Backup? | Data protection, recoverable backups, and backup management. |
| [INF-RD-S12] | AWS — Backup plans | Resource selection, timing, retained backups, and policy. |
| [INF-RD-S13] | AWS — Continuous backups and point-in-time recovery (PITR) | Recovery to a chosen time using supported retained history. |
| [INF-RD-S14] | AWS — Amazon EBS snapshots | Point-in-time volume copies, incremental snapshots, and restore purposes. |
| [INF-RD-S15] | AWS — Replicating objects within and across Regions | Automatic copying of changed objects and replication scope. |
| [INF-RD-S16] | AWS — Disaster recovery options in the cloud | Backup/restore, standby approaches, failover, testing, and recovery scope. |
| [INF-RD-S17] | AWS — Restore testing | Periodic restoration tests, viability, duration, and validation. |
| [INF-RD-S18] | AWS Well-Architected — Disaster Recovery (DR) objectives | Recovery time objective and recovery point objective definitions. |
| [INF-RD-S19] | AWS — Block vs File vs Object Storage | Object access, shared filesystems, and disk/block access. |
| [INF-RD-S20] | AWS — Managing the lifecycle of objects | Storage-class transitions and object expiration. |
| [INF-RD-S21] | AWS — Retaining multiple versions of objects with S3 Versioning | Retaining, retrieving, and restoring earlier object versions. |

[INF-RD-S01]: https://opentelemetry.io/docs/concepts/signals/logs/
[INF-RD-S02]: https://opentelemetry.io/docs/concepts/signals/metrics/
[INF-RD-S03]: https://opentelemetry.io/docs/concepts/signals/traces/
[INF-RD-S04]: https://docs.cloud.google.com/monitoring/docs/monitoring-overview
[INF-RD-S05]: https://docs.cloud.google.com/monitoring/alerts
[INF-RD-S06]: https://kubernetes.io/docs/concepts/workloads/pods/probes/
[INF-RD-S07]: https://docs.cloud.google.com/monitoring/uptime-checks/introduction
[INF-RD-S08]: https://opentelemetry.io/docs/concepts/observability-primer/
[INF-RD-S09]: https://learn.microsoft.com/en-us/azure/architecture/best-practices/auto-scaling
[INF-RD-S10]: https://learn.microsoft.com/en-us/azure/well-architected/reliability/redundancy
[INF-RD-S11]: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
[INF-RD-S12]: https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html
[INF-RD-S13]: https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html
[INF-RD-S14]: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html
[INF-RD-S15]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html
[INF-RD-S16]: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html
[INF-RD-S17]: https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html
[INF-RD-S18]: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html
[INF-RD-S19]: https://aws.amazon.com/compare/the-difference-between-block-file-object-storage/
[INF-RD-S20]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
[INF-RD-S21]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html
