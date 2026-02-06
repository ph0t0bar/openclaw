# Agent Drops

Async notes between Claude Code and OpenClaw. Same philosophy as DropAnywhere:
capture the thought now, process it later, nothing gets lost.

## Directories

- `from-claude-code/` — Claude Code drops context for OpenClaw
- `from-openclaw/` — OpenClaw drops context for Claude Code

## Drop Format

Filename: `YYYY-MM-DD-HHMMSS-slug.md`

```markdown
# Short title

Body text — what happened, what matters, what to do with it.
```

## How It Works

**Claude Code → OpenClaw**: Files committed here deploy with the repo.
The entrypoint copies them to OpenClaw's workspace at `/root/.openclaw/workspace/drops/`.
OpenClaw reads them as context.

**OpenClaw → Claude Code**: OpenClaw writes to `/root/.openclaw/workspace/drops/from-openclaw/`.
Claude Code reads them via `railway run` on next session.
