# Repository protection

## What is policy and what is enforcement?

`AGENTS.md` requires the owner's explicit authorization before an agent merges a PR, enables auto-merge, pushes directly to `main`, or bypasses a review rule. `.github/CODEOWNERS` routes review to `@HHC225`. These files do not themselves activate GitHub branch protection.

The `Validate ITWYW` workflow runs the offline structure checks. A passing workflow is not permission for an agent to merge.

## Proposed GitHub ruleset

The importable configuration is [main.json](../.github/rulesets/main.json). Its intended behavior is:

| Rule | Result |
| --- | --- |
| Target the default branch | Apply to `main`, or its successor if the default changes. |
| Pull request required | Changes go through a PR instead of an ordinary direct push. |
| One approving review | Another eligible reviewer must approve. |
| Dismiss stale approvals | A changed diff needs fresh review. |
| Approval of the latest reviewable push | The last pusher cannot be the only person approving the latest change. |
| Resolve review discussions | Unresolved review threads block merging. |
| Required `validate` check | The structural validation job must pass. |
| Branch up to date | Required checks must apply to an up-to-date branch. |
| No force pushes or deletion | Protect published branch history and the branch itself. |
| Empty bypass list | No actor is deliberately exempted in this ruleset. |

Code-owner review is **not** additionally required by this proposed ruleset: making the single owner a mandatory approver can deadlock that owner's own PRs. CODEOWNERS still provides review routing when applicable. The independent-review requirement remains.

### Identity limitation

GitHub evaluates authenticated identities. It cannot distinguish a person from an agent acting through the same account or token. A repository administrator can also edit repository rules. Therefore, a ruleset is not proof that an AI using the owner's administration authority can never change policy.

GitHub does not allow authors to approve their own pull requests. With one required approval and no bypass, a repository with only one eligible reviewer needs another trusted reviewer for that person's PRs. Keep this consequence visible before enabling the configuration. Do not add a bypass or a second account automatically to get around it.

If stronger separation is required, keep an agent on a separate, least-privilege identity without repository-administration authority and preserve the human's approval role. Changing credentials or account permissions requires its own explicit authorization.

## Apply the configuration

Apply only after the initial default branch exists and the `validate` job has run successfully.

An administrator can import the JSON through GitHub's repository rules interface, or use the official GitHub CLI after authenticating in their own environment:

```bash
gh api --method POST repos/HHC225/ITWYW/rulesets \
  --input .github/rulesets/main.json
```

Before running the command, inspect existing rules and update the matching rule instead of creating duplicates. Keep auto-merge disabled in repository settings. Review the resulting active ruleset and confirm the actual target, review count, bypass list, and check name. A checked-in JSON file or a successful upload is not evidence that the rule is active.

## Initial setup status

At the initial inspection on 2026-10-25, the repository was empty, `allow_auto_merge` was `false`, and the repository ruleset list was empty. The connected GitHub tool allowed content/commit operations but exposed no repository-administration write operation. The settings page required a separate browser sign-in.

The importable configuration is prepared for activation. **Do not infer live enforcement from this document.** Confirm live GitHub settings before asserting that a merge is blocked by server-side rules.

## Official references

- [GitHub: Available rules for rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [GitHub: About protected branches](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
- [GitHub: REST API endpoints for repository rules](https://docs.github.com/en/rest/repos/rules)
- [GitHub: Approving a pull request with required reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews)
