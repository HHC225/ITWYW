# Repository protection

## What is policy and what is enforcement?

`AGENTS.md` requires the owner's explicit authorization before an agent merges a PR, enables auto-merge, pushes directly to `main`, or bypasses a review rule. `.github/CODEOWNERS` routes review to `@HHC225`. These files do not themselves activate GitHub branch protection.

The `Validate ITWYW` workflow runs the offline structure checks. A passing workflow is not permission for an agent to merge.

## GitHub ruleset configuration

The importable configuration is [main.json](../.github/rulesets/main.json). Its behavior is:

| Rule | Result |
| --- | --- |
| Target the default branch | Apply to `main`, or its successor if the default changes. |
| Pull request required | Changes go through a PR instead of an ordinary direct push. |
| One approving review, with code-owner review required | The sole code owner, `@HHC225`, must approve. Another person's approval cannot replace this. |
| Dismiss stale approvals | A changed diff needs fresh review. |
| Approval of the latest reviewable push | The last pusher cannot be the only person approving the latest change. |
| Resolve review discussions | Unresolved review threads block merging. |
| Required `validate` check from GitHub Actions | The structural validation job must pass; a same-named status from another source does not replace it. |
| No extra approval for unattributed Copilot PRs | Preserve the one-owner approval process instead of adding a second required approval. This does not enable automatic Copilot reviews. |
| Branch up to date | Required checks must apply to an up-to-date branch. |
| No force pushes or deletion | Protect published branch history and the branch itself. |
| HHC225's individual account, PR-only bypass | The owner can merge a PR without review. The exception also covers other rules in this ruleset at PR merge; it does not allow direct-push bypass. |

**The only required reviewer and code owner is `@HHC225`.** Contributors without the owner's bypass still require code-owner review, and `.github/CODEOWNERS` contains only `* @HHC225`. Do not add other owners, substitute reviewers, or path-specific overrides. GitHub may still let other people leave comments or reviews according to their access; those approvals cannot satisfy the required owner's approval.

At the owner's explicit request, the only bypass entry is the individual user `HHC225` (GitHub user ID `237215883`) with mode `pull_request`. No repository role, team, app, or other user is included. This exception applies to the entire ruleset during PR merging, including required reviews and status checks. Direct pushes, force pushes, and deletions do not gain bypass permission from this PR-only entry. The rule table above describes the ordinary requirements; the owner can explicitly bypass them when merging a PR.

### Identity limitation

GitHub evaluates authenticated identities. It cannot distinguish a person from an agent acting through the same account or token. A repository administrator can also edit repository rules. Therefore, a ruleset is not proof that an AI using the owner's administration authority can never change policy.

GitHub does not allow authors to approve their own pull requests. The owner can now merge their own PR using the expressly authorized PR-only bypass instead of submitting a self-approval. The latest-push and review requirements continue to apply to actors without that exception.

An agent authenticated as `HHC225` shares the account's technical bypass permission. `AGENTS.md` still requires the owner's explicit instruction before an agent merges or uses bypass for a specific PR. Permission to configure this exception is not permission to merge a PR. A separately authorized contributor identity without administration or bypass authority can provide stronger separation; creating or changing accounts, credentials, or permissions requires its own explicit authorization.

## Apply the configuration

Apply only after the initial default branch exists and the `validate` job has run successfully.

An administrator can import the JSON through GitHub's repository rules interface, or use the official GitHub CLI after authenticating in their own environment:

```bash
gh api --method POST repos/HHC225/ITWYW/rulesets \
  --input .github/rulesets/main.json
```

Before running the command, inspect existing rules and update the matching rule instead of creating duplicates. Keep auto-merge disabled in repository settings. Review the resulting active ruleset and confirm the actual target, review count, bypass list, and check name. A checked-in JSON file or a successful upload is not evidence that the rule is active.

## Setup verification

At the initial inspection on 2026-10-25, the repository was empty, `allow_auto_merge` was `false`, and the repository ruleset list was empty. The connected GitHub tool allowed content/commit operations but exposed no repository-administration write operation. The settings page required a separate browser sign-in.

After browser sign-in on 2026-10-25, ruleset [25819387](https://github.com/HHC225/ITWYW/rules/25819387) was created and verified through the GitHub API. It initially had no bypass actors. `main` reported `protected: true`; repository auto-merge remained disabled. Required code-owner review, one approval, latest-push approval, stale-approval dismissal, resolved conversations, and the GitHub Actions `validate` check were present. The additional-approval option for unattributed Copilot PRs was explicitly off so it could not introduce another required reviewer.

The owner then explicitly requested permission to merge without review. The updated active ruleset was verified with exactly one bypass actor: `User` ID `237215883`, mode `pull_request`. GitHub reported `current_user_can_bypass: pull_requests_only`. All ordinary rule requirements remained configured; the owner's PR-only exception is the distinction.

This is a dated observation. **Do not infer current enforcement from a checked-in file.** Confirm live GitHub settings before asserting that a merge is blocked by server-side rules. Documentation updates are prepared on a separate branch for the owner to inspect; the configuration change itself does not authorize an agent to merge them.

At the owner's request, unused repository features were also disabled: Wikis and Projects were switched off, and Discussions was confirmed off. Issues remain available for bug reports and requests; pull requests and Actions support the review and validation workflow.

## Official references

- [GitHub: Available rules for rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [GitHub: About protected branches](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
- [GitHub: REST API endpoints for repository rules](https://docs.github.com/en/rest/repos/rules)
- [GitHub: Granting bypass permissions for branch or tag rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
- [GitHub: Approving a pull request with required reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews)
