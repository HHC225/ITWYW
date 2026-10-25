# Installation verification

Date: **2026-10-25**.

## Tested package and source

- Installer: the published npm package `skills@1.7.4`.
- Runtime: Node.js `v24.22.1`; the installer declares Node.js `>=22.20.0`.
- Source: the public `HHC225/ITWYW` repository, with `main` at `cf183646ccfac8eede73f0e645f134c84f0145fa`.
- Skill: `skills/itwyw`, containing 17 files, including 15 reference Markdown files.

Both tests ran in separate empty project directories. Telemetry was disabled and installer state/cache were directed to temporary test locations. No global skill installation was requested.

## Executed installation cases

### Independent copies

```bash
npx --yes skills@1.7.4 add HHC225/ITWYW --skill itwyw --agent codex claude-code --copy --yes
```

The installer found exactly one skill, selected `itwyw`, and exited successfully. It installed complete folders at `.agents/skills/itwyw` and `.claude/skills/itwyw`.

### Default shared-folder and link mode

```bash
npx --yes skills@1.7.4 add HHC225/ITWYW --skill itwyw --agent codex claude-code --yes
```

The installer again found one skill and exited successfully. Codex used `.agents/skills/itwyw`; `.claude/skills/itwyw` was a valid symlink to that canonical folder.

## File checks

For both modes and both target paths, SHA-256 manifests matched the original skill directory exactly: all 17 files were present and byte-identical, including all 15 references and `agents/openai.yaml`. No repository-level README, evaluation, workflow, governance file, or development script appeared inside the installed skill.

The repository validator also checks that runtime Markdown links stay within the installable skill folder. A temporary broken fixture with a link from `SKILL.md` to the repository README was rejected, even though that README existed in the checkout. This catches dependencies that would break when only `skills/itwyw` is installed.

## Limits

These tests establish current installer discovery, copying/linking, and package completeness on this Linux test environment. They do not establish skill loading in every Codex or Claude Code version, managed enterprise policy, Windows host, or separate cloud session. The PowerShell instructions and older `~/.codex/skills` route are documented from host guidance and were not executed here. Model behavior is evaluated separately in [Initial evaluation](initial-evaluation.md).
