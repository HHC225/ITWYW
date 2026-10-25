# Infrastructure: delivery and operations

Use these mappings for requests about releasing changes, separating work from live service, managing operational settings, and controlling infrastructure use. They identify vocabulary and intent; they do not prescribe a release architecture or authorize a deployment.

Verified against the official sources below on 2026-10-25. **28 concepts.** Related references: [Hosting and network access](infra-hosting-network.md), [Reliability and data](infra-reliability-data.md).

## Contents

- [Environments](#environments)
- [Build and delivery](#build-and-delivery)
- [Release controls](#release-controls)
- [Configuration and maintenance](#configuration-and-maintenance)
- [Cost and resource controls](#cost-and-resource-controls)
- [Ambiguity traps](#ambiguity-traps)
- [Sources](#sources)

## Environments

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-DO-01 | Development environment; dev; sandbox | “Give developers somewhere to try changes.” / “Let me work without affecting customers.” | This is a workspace for making and trying changes. | Is this mainly for building changes? | [INF-DO-S01] |
| INF-DO-02 | Test environment; QA environment | “Give testers their own copy.” / “Check new changes away from live users.” | This is a place to check whether the app works. | Is the main purpose testing a candidate change? | [INF-DO-S01] |
| INF-DO-03 | Staging environment; preproduction; preprod | “Let us rehearse before going live.” / “Check it in a place like the real site.” | This is a practice setting that resembles the live service. | Is this the final check before production? | [INF-DO-S01] |
| INF-DO-04 | Production environment; prod; live environment | “Put it where customers actually use it.” / “This is our real running service.” | This is the app that real users depend on. | Will the change affect live users or data? | [INF-DO-S01] |
| INF-DO-05 | Preview environment; preview deployment; review app | “Give me a link for this proposed change.” / “Let others try this branch before we publish it.” | A temporary version lets people inspect one proposed change. | Is the link tied to one change, rather than a shared staging environment? | [INF-DO-S02] |

## Build and delivery

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-DO-06 | Build; build process; packaging | “Turn the project into something we can run.” / “Prepare the website files for publishing.” | A build turns the project's ingredients into a runnable package. | Do you need to prepare a package, or put an existing package on a server? | [INF-DO-S03] |
| INF-DO-07 | Build artifact; release artifact; deployable package | “Keep the exact package that passed testing.” / “Save the files we are going to release.” | An artifact is the saved output of a build or other workflow step. | Do you mean the finished package, the source code, or the running app? | [INF-DO-S03] |
| INF-DO-08 | Container registry; image registry | “Store our app images somewhere the servers can fetch them.” / “Keep versions of our container packages.” | A registry is a storehouse for container images. | Are these container images rather than ordinary files or source code? | [INF-DO-S04] |
| INF-DO-09 | Continuous integration; CI | “Check every code change automatically.” / “Build and test when developers submit updates.” | Frequent changes are combined and checked by automated builds and tests. | Should automation check the change, publish it, or both? | [INF-DO-S05] |
| INF-DO-10 | Continuous delivery; CD | “Always have a tested version ready to release.” / “Prepare updates automatically, with a final go-live choice.” | Automation keeps a checked package ready for release. | Must a person still decide when production changes? | [INF-DO-S05] |
| INF-DO-11 | Continuous deployment; CD | “Publish each update automatically after it passes.” / “Make successful changes go live without a manual release step.” | Passing changes automatically move into the live service. | Is automatic production release explicitly wanted? | [INF-DO-S05] |
| INF-DO-12 | Deployment; deploy; rollout | “Put this version onto the server.” / “Update the app that is running.” | Deployment puts a chosen version into an environment where it can run. | Which environment should receive this version? | [INF-DO-S03] |
| INF-DO-13 | Deployment pipeline; delivery pipeline; CI/CD workflow | “Run our release steps in the right order.” / “Connect building, checking, and publishing.” | A pipeline links the steps that prepare and deliver changes. | Which steps, triggers, and approval points belong in the workflow? | [INF-DO-S06] |
| INF-DO-14 | Deployment approval; release gate; environment protection | “Have someone approve before it goes live.” / “Do not publish until the required checks pass.” | A gate holds the release until its conditions are met. | Is the condition a person's approval, an automated check, or both? | [INF-DO-S07] |

## Release controls

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-DO-15 | Rolling deployment; rolling update | “Update the servers a few at a time.” / “Replace old app copies gradually.” | Small groups of running copies are replaced in turn. | Should old and new copies run together during replacement? | [INF-DO-S08] |
| INF-DO-16 | Blue-green deployment; environment switch | “Prepare a second full version, then switch traffic.” / “Keep the old setup ready while the new one starts.” | Two environments let traffic move from the old version to the prepared new one. | Are there two separate production-capable environments? | [INF-DO-S09] |
| INF-DO-17 | Canary deployment; canary release; progressive rollout | “Try the new version with a few visitors first.” / “Expand the rollout only after it looks healthy.” | A small group gets the change before more users do. | Are you limiting who receives the new version while observing results? | [INF-DO-S10] |
| INF-DO-18 | Deployment rollback; rollback | “Go back to the previous working version.” / “Undo this release because it broke something.” | Rollback restores an earlier deployed version. | Are you reversing code, settings, data changes, or all three? | [INF-DO-S08] |
| INF-DO-19 | Feature flag; feature toggle; release toggle | “Turn this feature off without publishing again.” / “Enable it only for selected users.” | A switch controls whether people can use a feature already in the app. | Is the code already deployed, with only its availability changing? | [INF-DO-S11] |

## Configuration and maintenance

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-DO-20 | Infrastructure as code; IaC | “Save our server setup in files we can review.” / “Recreate the same infrastructure from a description.” | Written instructions describe the infrastructure so tools can manage it consistently. | Are these infrastructure resources rather than the app's business code? | [INF-DO-S12] |
| INF-DO-21 | Runtime configuration; environment configuration; environment variable | “Use different settings on test and live.” / “Change the service address without editing the app.” | Settings tell the app how to behave in each environment. | Is this an ordinary setting or a sensitive credential? | [INF-DO-S13] |
| INF-DO-22 | Secret management; secrets store; credential vault | “Keep API keys out of our code.” / “Let only the right services read the passwords.” | A protected store keeps sensitive keys and passwords for approved users or apps. | Does this value grant access or reveal sensitive information? | [INF-DO-S14] |
| INF-DO-23 | Secret rotation; credential rotation | “Replace service passwords regularly.” / “Change the key without leaving apps using the old one.” | Rotation replaces a secret and updates the service that checks it. | Must both the stored secret and its users or target service change? | [INF-DO-S15] |
| INF-DO-27 | Patch management; system updates | “Keep the server software's fixes up to date.” / “Check which machines still need security updates.” | Patching installs fixes for software that is already running. | Are you updating operating systems or dependencies rather than releasing a new app feature? | [INF-DO-S19] |

## Cost and resource controls

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-DO-24 | Budget alert; cost alert; spending notification | “Tell me when the bill is getting too high.” / “Warn me before we exceed our monthly target.” | An alert tells you when spending approaches or passes a chosen amount. | Do you want a warning, or an enforced stop? | [INF-DO-S16] |
| INF-DO-25 | Spending limit; spend cap; enforced cost control | “Stop supported spending when it reaches the limit.” / “I need a cap, not just a bill warning.” | A supported spending control stops or restricts covered use at its limit. | Does this provider and plan support a cap, what does it cover, and what stops? | [INF-DO-S17] |
| INF-DO-26 | Resource quota; usage limit; capacity limit | “Do not let us create unlimited servers.” / “Set a maximum for this resource.” | A quota limits how much of a resource may be used. | Is the ceiling on resource quantity, request rate, or money? | [INF-DO-S18] |
| INF-DO-28 | Resource tags; resource labels; cost allocation tags | “Show which project owns each cloud resource.” / “Split our bill by team.” | Labels help group resources by owner, purpose, or project. | Do you need labels, or a report that actually allocates costs using them? | [INF-DO-S20] [INF-DO-S21] |

## Ambiguity traps

- **“Publish automatically”** needs one question: automatically prepare a release, or automatically change production? “CD” can mean continuous delivery or continuous deployment. [INF-DO-S05]
- **“Build,” “deploy,” and “release”** are not interchangeable. Building prepares output; deployment places a version into an environment; feature release can happen separately through a flag. [INF-DO-S03] [INF-DO-S11]
- **“A safe place to try it”** may mean development, QA, staging, or one preview link. Environment labels vary by team. A preview URL does not prove that its database or external integrations are isolated from production. Ask about connected data and services. [INF-DO-S01] [INF-DO-S02]
- **“Let a few people see it first”** may mean a preview link, a canary release, or a feature flag. Ask whether they are reviewing a temporary version, receiving a new deployed version, or unlocking existing code. [INF-DO-S02] [INF-DO-S10] [INF-DO-S11]
- **“Update without downtime”** is a reliability goal. Rolling, blue-green, and canary describe different release methods; none alone guarantees uninterrupted service. Rollback also needs attention to changed data and compatibility. [INF-DO-S08] [INF-DO-S09] [INF-DO-S10]
- **“Keep the bill under X”** is not satisfied by an alert-only budget. A spending cap is provider- and plan-dependent, may have exclusions, and can interrupt service. A resource quota limits a measured resource, not necessarily the total bill. [INF-DO-S16] [INF-DO-S17] [INF-DO-S18]
- **“Set an environment variable”** does not tell you whether the value is secret or safely stored. Distinguish ordinary configuration from credentials and their access controls. [INF-DO-S13] [INF-DO-S14]

## Sources

The named providers document the concepts; these links do not select a provider for the user. The example phrases and explanations are original paraphrases.

| Source key | Official title and publisher | Verified topics |
| --- | --- | --- |
| [INF-DO-S01] | Microsoft Learn — Environments | Development, test, staging, and production purposes. |
| [INF-DO-S02] | Firebase — Deploy to live & preview channels via GitHub pull requests | Per-change preview URLs; preview access to real backend resources. |
| [INF-DO-S03] | AWS CodePipeline — Input and output artifacts | Separate source, build, artifact, and deploy steps. |
| [INF-DO-S04] | Docker Docs — What is a registry? | Storage and distribution of container images. |
| [INF-DO-S05] | AWS — What is continuous integration and continuous delivery/deployment? | CI; delivery readiness; automatic production deployment. |
| [INF-DO-S06] | GitHub Docs — Understanding GitHub Actions | Event-triggered workflows; ordered and parallel jobs; build/test/deploy pipelines. |
| [INF-DO-S07] | GitHub Docs — Deployments and environments | Required reviewers and deployment protection rules. |
| [INF-DO-S08] | Kubernetes — Deployments | Rolling replacement, deployment revisions, rollback behavior and scope. |
| [INF-DO-S09] | AWS — Introduction: Blue/Green Deployments on AWS | Two environments; traffic switching; rollback to an earlier environment. |
| [INF-DO-S10] | Microsoft Learn — Architecture strategies for safe deployment practices | Progressive exposure, canary releases, health checks, and release risk. |
| [INF-DO-S11] | Microsoft Learn — Understand feature management using Azure App Configuration | Feature availability separated from deployment; toggles and targeting. |
| [INF-DO-S12] | HashiCorp Developer — What is Terraform? | Infrastructure descriptions that can be versioned, reused, and reviewed. |
| [INF-DO-S13] | Kubernetes — ConfigMaps | Non-confidential settings; environment variables and configuration files. |
| [INF-DO-S14] | AWS — What is AWS Secrets Manager? | Controlled storage and retrieval of passwords, keys, and other secrets. |
| [INF-DO-S15] | AWS — Rotate AWS Secrets Manager secrets | Updating credentials in the secret and the target service. |
| [INF-DO-S16] | Google Cloud — Create, edit, or delete budgets and budget alerts | Alert-only budgets; thresholds; distinction from spending caps. |
| [INF-DO-S17] | Microsoft Learn — Azure spending limit | Supported subscription limits, service interruption, and exclusions. |
| [INF-DO-S18] | AWS — What is Service Quotas? | Resource and operation quotas; limits and usage. |
| [INF-DO-S19] | AWS — AWS Systems Manager Patch Manager | Scanning for and applying operating system and application updates. |
| [INF-DO-S20] | AWS — What are tags? | Metadata labels for organizing and identifying resources. |
| [INF-DO-S21] | AWS Billing — Organizing and tracking costs using AWS cost allocation tags | Activated cost allocation tags and grouping resource costs. |

[INF-DO-S01]: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/considerations/environments
[INF-DO-S02]: https://firebase.google.com/docs/hosting/github-integration
[INF-DO-S03]: https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome-introducing-artifacts.html
[INF-DO-S04]: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/
[INF-DO-S05]: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/what-is-continuous-integration-and-continuous-deliverydeployment.html
[INF-DO-S06]: https://docs.github.com/en/actions/get-started/understand-github-actions
[INF-DO-S07]: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments
[INF-DO-S08]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
[INF-DO-S09]: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/introduction.html
[INF-DO-S10]: https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments
[INF-DO-S11]: https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-feature-management
[INF-DO-S12]: https://developer.hashicorp.com/terraform/intro
[INF-DO-S13]: https://kubernetes.io/docs/concepts/configuration/configmap/
[INF-DO-S14]: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
[INF-DO-S15]: https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html
[INF-DO-S16]: https://docs.cloud.google.com/billing/docs/how-to/budgets
[INF-DO-S17]: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit
[INF-DO-S18]: https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html
[INF-DO-S19]: https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html
[INF-DO-S20]: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html
[INF-DO-S21]: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html
