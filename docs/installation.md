# Installing ITWYW

ITWYW is one self-contained skill: [`skills/itwyw`](../skills/itwyw). Install that directory with its `SKILL.md`, 15 reference Markdown files, and `agents/openai.yaml`. Repository-level documentation, evaluations, GitHub configuration, and validation scripts are for maintainers; they are not skill runtime dependencies.

## Install with npx

From the project where you want to use the skill:

```bash
npx skills add HHC225/ITWYW --skill itwyw
```

Choose your agent if prompted. The CLI can also detect the agent it is running inside. To select it in the command:

```bash
npx skills add HHC225/ITWYW --skill itwyw -a codex
npx skills add HHC225/ITWYW --skill itwyw -a claude-code
npx skills add HHC225/ITWYW --skill itwyw -a codex claude-code
```

These are alternatives; run the one for your setup. The [skills CLI installation reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) documents source formats and options. Its [discovery rules](https://github.com/vercel-labs/skills/blob/main/docs/creating-skills.md) support `skills/<name>/SKILL.md`, so ITWYW needs no npm publication or package manifest.

| Option | Use it when |
| --- | --- |
| `-g` / `--global` | You want the skill available across projects. |
| `-a codex` / `-a claude-code` | You want to choose the target agent explicitly. |
| `-a codex claude-code` | You use both agents. |
| `--copy` | You want independent copies instead of the CLI's shared folder and links. |
| `-y` / `--yes` | You want to accept the CLI's installation choices without its interactive questions. |

For example, install for both agents across your projects:

```bash
npx skills add HHC225/ITWYW --skill itwyw -a codex claude-code -g
```

The current CLI release requires Node.js 22.20 or later. Install Git as well for the GitHub source. See the CLI's [README](https://github.com/vercel-labs/skills) and [npm metadata](https://registry.npmjs.org/skills/latest) for current requirements. Node.js runs the installer; the installed ITWYW skill itself is instructions and reference files.

The CLI may maintain lock files and its own installation state outside the skill folder. “Install only the skill” means repository development files are not copied into the runtime skill; it does not mean the installer writes no bookkeeping files.

## Clone and copy manually

### macOS, Linux, or Git Bash

Run this from your own project directory. The clone creates an `ITWYW` download folder there:

```bash
git clone --depth 1 https://github.com/HHC225/ITWYW.git
mkdir -p .agents/skills
cp -R ITWYW/skills/itwyw .agents/skills/
```

For Claude Code, use `.claude/skills` in both copy-related commands:

```bash
mkdir -p .claude/skills
cp -R ITWYW/skills/itwyw .claude/skills/
```

For all projects, use `~/.agents/skills` for current Codex or `~/.claude/skills` for Claude Code. The complete skill folder must remain together.

### Windows PowerShell

```powershell
git clone --depth 1 https://github.com/HHC225/ITWYW.git
New-Item -ItemType Directory -Force .agents/skills | Out-Null
Copy-Item -Recurse ITWYW/skills/itwyw .agents/skills/
```

Replace `.agents/skills` with `.claude/skills` for Claude Code. For a user-wide destination in PowerShell, use a path such as `"$HOME/.agents/skills"` or `"$HOME/.claude/skills"`.

### Correct final paths

| Host | Project skill entry point | User-wide skill entry point |
| --- | --- | --- |
| Codex | `.agents/skills/itwyw/SKILL.md` | `~/.agents/skills/itwyw/SKILL.md` |
| Claude Code | `.claude/skills/itwyw/SKILL.md` | `~/.claude/skills/itwyw/SKILL.md` |

These paths follow the official [Codex local skill locations](https://learn.chatgpt.com/docs/build-skills), [Claude Code skill locations](https://code.claude.com/docs/en/skills), and the CLI's [agent directory table](https://github.com/vercel-labs/skills/blob/main/docs/agents.md). A local installation does not automatically install the skill into a separately hosted cloud session.

### Existing Codex installations using .codex

Some Codex setups use `~/.codex/skills`; an official [Codex skills use case](https://learn.chatgpt.com/use-cases/reusable-codex-skills) documents that user location. If your existing host uses it, copy the same skill folder there:

```bash
mkdir -p ~/.codex/skills
cp -R ITWYW/skills/itwyw ~/.codex/skills/
```

For a new installation, follow the current `.agents/skills` locations above. Do not assume that every Codex version or host scans a project-local `.codex/skills` directory. Do not install duplicate copies into both locations for the same agent unless you deliberately manage that setup.

## Use, update, and remove

In Codex, mention `$itwyw`; in Claude Code, use `/itwyw`. You can also ask the agent to use ITWYW by name. Describe the feature in your own language; the skill follows that language or your explicit language preference.

For a project installation managed by the skills CLI:

```bash
npx skills list
npx skills update itwyw -p
npx skills remove itwyw
```

For a global installation, use the global flag explicitly:

```bash
npx skills list -g
npx skills update itwyw -g
npx skills remove itwyw -g
```

Removal defaults to the current project when `-g` is omitted; it does not ask you to choose a scope. For a manual installation, update your downloaded repository and replace only the existing `itwyw` skill folder with the fresh complete folder. To uninstall manually, remove only that installed `itwyw` folder.

## If it does not appear

- Check that `SKILL.md` is inside `<agent skill directory>/itwyw/`, with `references/` next to it. Do not copy only `SKILL.md` or add an extra `skills/itwyw` nesting level.
- Confirm you installed in the project where you run the agent, or choose a user-wide installation.
- Restart the agent after adding a new skills directory. Host-specific trust or managed policy can also affect discovery; follow that host's instructions.
- If `npx` is unavailable or your Node.js version is too old, update Node.js or use manual copying.
- If you use the CLI's default links, retain its canonical `.agents/skills/itwyw` folder. Use `--copy` when you need standalone folders.

## Evidence scope

See [Installation verification](../evals/installation-verification.md) for the tested CLI version, published source revision, file-integrity checks, and limits. Installing the files verifies packaging and discovery by the installer; it is not a guarantee that every host will load a skill regardless of its version or administrator policy.
