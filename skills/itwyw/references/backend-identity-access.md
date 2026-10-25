# Backend: identity, access, and entitlements

Use this file when a person says who should get in, what they may do, whose information they may see, or what their plan includes. Names describe capabilities; they do not choose an identity provider or prescribe an architecture. Everyday phrases are original examples; sources verify the underlying concepts. Last verified: 2026-10-25.

## Contents

- [Accounts and sign-in](#accounts-and-sign-in)
- [Sessions and alternative sign-in](#sessions-and-alternative-sign-in)
- [Permissions and organization boundaries](#permissions-and-organization-boundaries)
- [Machine access, sharing, and records](#machine-access-sharing-and-records)
- [Important distinctions](#important-distinctions)
- [Sources](#sources)

## Accounts and sign-in

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-A01 | Authentication; sign-in | “Make people log in first.” / “Check that it is really me.” | Checks which account is trying to use the service. | Sign in to an account, verify an email, or prove a real-world identity? | OW-AUTH |
| BE-A02 | Authorization; access control; permission enforcement | “Only staff should change prices.” / “Customers must not open the admin pages.” | Checks whether this person may perform this action on this item. | Which action and item? Hiding a button does not enforce the rule. | OW-AUTHZ |
| BE-A03 | Account registration; sign-up; user provisioning | “Let people create an account.” / “Let our admin add new staff.” | Creates the saved account a person will use. | Open sign-up, invitation-only joining, or accounts created by an administrator? | FIREBASE-USERS |
| BE-A04 | Email verification; email ownership confirmation | “Make sure they own that email address.” / “Ask them to confirm their address before using the account.” | Checks that someone can receive mail at the address they supplied. | Verify the address once, or use email as the sign-in method? | OW-AUTH |
| BE-A05 | Password reset; account recovery | “I forgot my password.” / “Help customers get back into their account.” | Gives a checked way to regain access when the usual sign-in fails. | Forgotten password, lost second factor, or lost access to the recovery email? | OW-RECOVERY |
| BE-A21 | Account suspension; disable account; access deactivation | “Stop this person using the account.” / “Suspend a member without deleting their work.” | Keeps the account record while blocking its permitted use. | Block new sign-ins only, or also end current sessions and revoke credentials? | FIREBASE-USERS; FIREBASE-SESSIONS |

## Sessions and alternative sign-in

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-A06 | Session management; signed-in session; remember sign-in | “Don't ask me to log in on every page.” / “Keep me signed in on this device.” | Lets later requests continue an earlier successful sign-in. | For how long, on which devices, and across browser restarts? | OW-SESSIONS |
| BE-A07 | Session expiry; idle timeout; reauthentication | “Log me out after a while.” / “Ask for proof again before changing bank details.” | Stops an old sign-in or asks for fresh proof when needed. | Inactivity, total elapsed time, or a sensitive action? | OW-SESSIONS; OW-AUTH |
| BE-A08 | Session revocation; remote logout; sign out everywhere | “Sign me out on my lost phone.” / “Log out every other device.” | Makes selected earlier sign-ins stop being accepted. | This device, one other session, or all sessions? When must revocation take effect? | FIREBASE-SESSIONS |
| BE-A09 | Single sign-on; SSO | “One work login should open all our tools.” / “Don't make staff sign in separately to each company app.” | Lets one identity sign-in help someone enter several connected apps. | Several apps sharing work identity, or one app offering an outside login button? | MS-SSO |
| BE-A10 | Federated sign-in; social login; OpenID Connect sign-in | “Let me sign in with my existing provider account.” / “Use my company identity instead of another password.” | Lets the service trust sign-in proof from another identity service. | Is the outside service proving identity, granting data access, or doing both? | OIDC |
| BE-A11 | OAuth delegated authorization; connected-account consent | “Let this app read my calendar.” / “Connect my storage account without giving you its password.” | Lets another app use selected access that the account owner grants. | Which outside data and actions? OAuth alone does not define user login. | OAUTH |
| BE-A12 | Passkey sign-in; passwordless public-key credentials | “Let me use my device unlock to sign in.” / “I don't want to remember a password.” | Uses a sign-in key, often unlocked by a PIN or fingerprint. | Is a passkey wanted, or an email link? What happens if the device is lost? | MDN-WEBAUTHN |
| BE-A13 | Multi-factor authentication; MFA; two-factor authentication | “Ask for a second kind of proof.” / “A stolen password should not be enough.” | Checks evidence from more than one kind of sign-in factor. | Which independent factors? Two passwords are still the same kind of factor. | OW-MFA |
| BE-A14 | Recovery codes; backup codes | “Give me backup codes if I lose my phone.” / “Let me keep emergency sign-in codes somewhere safe.” | Gives special one-use codes for recovering access. | Are these recovery codes, ordinary sign-in codes, or a password reset? | OW-MFA |
| BE-A15 | Magic-link sign-in; passwordless email-link authentication | “Email me a button to sign in.” / “Let me log in without setting a password.” | Signs someone in after they use a checked link sent to their email. | Is the email proving a sign-in now, or just confirming an address? | FIREBASE-EMAIL |

## Permissions and organization boundaries

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-A16 | Role-based access control; RBAC | “Managers can approve, staff can submit.” / “Give editors different powers from viewers.” | Gives people permissions through named roles. | Are fixed job-like roles enough, or do rules depend on the item and situation? | MS-RBAC |
| BE-A17 | Attribute-based access control; ABAC; conditional permissions | “Only staff in this region may see these cases.” / “Allow this action only for approved devices.” | Uses facts about the person, item, or situation to decide access. | Which facts decide access, and who controls those facts? | MS-ABAC |
| BE-A18 | Record ownership checks; object-level authorization | “People should only edit their own profile.” / “Each customer should see only their orders.” | Checks permission for the particular saved item being requested. | Owner only, selected collaborators, or everyone in the same organization? | OW-IDOR |
| BE-A19 | Tenant isolation; organization-level data separation | “Each company must only see its own data.” / “Our customer teams must never mix.” | Keeps one organization's information outside another organization's reach. | What defines an organization, and can a person belong to several? Check files and jobs too. | OW-TENANTS |
| BE-A20 | Team membership; invitations; organization joining | “Invite my coworker into our workspace.” / “Let an owner remove someone from the team.” | Adds or removes a person's membership in a group. | Does an invitation create membership immediately or require acceptance? Which role follows joining? | GH-INVITES |
| BE-A24 | Resource sharing permissions; access-control list; ACL | “Share this file with just these people.” / “Give Alex viewing access but let Sam edit.” | Gives selected people or groups specific access to one item. | Named people, groups, the organization, or anyone with a link? | DRIVE-SHARING |
| BE-A27 | Feature entitlements; plan access; subscription feature gating | “Only paying teams get exports.” / “Turn on advanced reports for the Pro plan.” | Records which product features an account is entitled to use. | Is the rule about a person's role, a purchased feature, a usage limit, or several together? | STRIPE-ENTITLEMENTS |

## Machine access, sharing, and records

| ID | Conventional feature name and aliases | Two everyday phrases | Simple explanation | Decisive cue or question | Sources |
|---|---|---|---|---|---|
| BE-A22 | API credentials; API keys; service credentials | “Let our other system connect automatically.” / “Give the integration its own access key.” | Gives software a key it presents when calling a service. | Must it identify a project, a machine, or a person? API keys have different powers in different services. | GOOGLE-KEYS |
| BE-A23 | Scoped access tokens; delegated permission scopes | “Let the integration read but never delete.” / “Only let this connection use calendar events.” | Limits the set of actions a credential may request. | Which scopes and resources? The service still has to enforce permission on each request. | OAUTH; OW-AUTHZ |
| BE-A25 | Signed download link; presigned URL; expiring access link | “Let this download link work for one hour.” / “Send a temporary link to this private file.” | Gives the link holder temporary access to a particular resource. | Can anyone holding the link use it, or must the recipient also sign in? | AWS-SIGNEDURL |
| BE-A26 | Audit trail; activity audit log | “Show who changed this setting and when.” / “Keep a record of who approved each request.” | Records important actions with who did them and when. | Need accountability, restorable old content, or operational error logs? Which events and retention? | OW-LOGGING |

## Important distinctions

- **Identity is separate from permission.** Authentication answers “who”; authorization answers “may this identity do this to this item?” Every relevant server request needs its permission decision, including requests made outside the interface. (`OW-AUTH`, `OW-AUTHZ`, `OW-IDOR`)
- **SSO, federation, and OAuth are not interchangeable names.** SSO describes a sign-in experience across apps. OpenID Connect defines identity information for federated sign-in. OAuth grants delegated access; a system can combine them. (`MS-SSO`, `OIDC`, `OAUTH`)
- **A session is continued sign-in state.** A cookie can carry a session identifier; a token is a credential or message format. A signed JWT is not automatically encrypted and does not remove the need to validate claims and permissions. Do not propose JWT just because someone asks for login. (`OW-SESSIONS`, `JWT`, `OW-AUTHZ`)
- **Passwordless does not automatically mean the same security properties.** Email links and passkeys prove access in different ways. MFA concerns distinct factors; a passkey can support MFA when its use includes the required user verification. (`FIREBASE-EMAIL`, `MDN-WEBAUTHN`, `OW-MFA`)
- **Passkeys and WebAuthn name different things.** A passkey is a sign-in credential. WebAuthn is the web API used to create and use public-key credentials; the API name is an implementation detail, not an alias for every passkey. (`MDN-WEBAUTHN`)
- **Ownership and tenancy are separate boundaries.** “My records” may mean one person, a team, or a whole customer organization. Membership does not by itself define every permission inside that organization. (`OW-IDOR`, `OW-TENANTS`, `GH-INVITES`)
- **Entitlement is separate from payment and role.** A paid plan can grant a feature while a person's role still forbids the action. A feature's monthly allowance is a quota; request bursts are rate limits. Consult `BE-J17`, `BE-J18`, and `BE-J31`. (`STRIPE-ENTITLEMENTS`, `MS-RBAC`)
- **Share links need an audience decision.** An unlisted or hard-to-guess URL is not the same requirement as named-person access. Signed URLs commonly grant access to whoever holds them until their applicable expiry. (`AWS-SIGNEDURL`, `DRIVE-SHARING`)

## Sources

Official documentation verifies the concepts below. Provider examples do not imply vendor selection or identical behavior in every service.

- **OW-AUTH** — [OWASP: Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html). Verified: identity verification, verified email addresses, and reauthentication.
- **OW-AUTHZ** — [OWASP: Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). Verified: authorization versus authentication and permission checks on every request.
- **FIREBASE-USERS** — [Firebase: Manage Users](https://firebase.google.com/docs/auth/admin/manage-users). Verified: creating user records, verified email state, and disabling accounts.
- **OW-RECOVERY** — [OWASP: Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html). Verified: recovery tokens, reset flows, and recovery safeguards.
- **OW-SESSIONS** — [OWASP: Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html). Verified: session identifiers, continued authenticated state, and server-enforced expiration.
- **FIREBASE-SESSIONS** — [Firebase: Manage User Sessions](https://firebase.google.com/docs/auth/admin/manage-sessions). Verified: refresh-token revocation and checking revoked sessions; immediate effects depend on the credential and checks used.
- **MS-SSO** — [Microsoft: What is single sign-on in Microsoft Entra ID?](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on). Verified: one sign-in across multiple applications.
- **OIDC** — [OpenID Foundation: OpenID Connect Core 1.0 incorporating errata set 2](https://openid.net/specs/openid-connect-core-1_0.html). Verified: an identity layer over OAuth 2.0 and ID-token-based identity information.
- **OAUTH** — [IETF RFC 6749: The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749). Verified: delegated access, access tokens, and scopes. Used for vocabulary, not an implementation recipe or a claim that all historic flows are current best practice.
- **MDN-WEBAUTHN** — [MDN: Web Authentication API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API). Verified: public-key authentication, WebAuthn, and passkeys.
- **OW-MFA** — [OWASP: Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html). Verified: distinct factors, passkey user verification, and single-use recovery codes.
- **FIREBASE-EMAIL** — [Firebase: Authenticate with Firebase Using Email Link in JavaScript](https://firebase.google.com/docs/auth/web/email-link-auth). Verified: passwordless email-link sign-in as a concrete example.
- **MS-RBAC** — [Microsoft: What is Azure role-based access control?](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview). Verified: assigning permissions through roles and a scope.
- **MS-ABAC** — [Microsoft: What is Azure attribute-based access control?](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-overview). Verified: decisions using subject, resource, and environment attributes.
- **OW-IDOR** — [OWASP: Insecure Direct Object Reference Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html). Verified: per-object permission checks and restricting retrieval to permitted records.
- **OW-TENANTS** — [OWASP: Multi Tenant Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html). Verified: cross-tenant isolation across data, cache, files, and processing boundaries.
- **GH-INVITES** — [GitHub: Inviting users to join your organization](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization). Verified: invitations, acceptance, and organization membership.
- **DRIVE-SHARING** — [Google Drive: Share files, folders, and drives](https://developers.google.com/workspace/drive/api/guides/manage-sharing). Verified: per-resource permissions for people and groups with reader, commenter, and writer roles.
- **STRIPE-ENTITLEMENTS** — [Stripe: Entitlements](https://docs.stripe.com/billing/entitlements). Verified: mapping product features to subscription-driven access grants.
- **GOOGLE-KEYS** — [Google Cloud: Manage API keys](https://docs.cloud.google.com/docs/authentication/api-keys). Verified: key-based API access, restrictions, and differing key identity properties.
- **AWS-SIGNEDURL** — [Amazon S3: Download and upload objects with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html). Verified: resource-specific temporary access and link-holder access.
- **OW-LOGGING** — [OWASP: Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html). Verified: recording the actor, action, time, and context of important events.
- **JWT** — [IETF RFC 7519: JSON Web Token](https://www.rfc-editor.org/rfc/rfc7519). Verified: claims represented using signed or encrypted structures; signing does not itself encrypt their contents.
