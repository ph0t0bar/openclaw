# Checkpoint Format

Any agent can produce a checkpoint. Same structure, same sections, always parseable.

## Template

```markdown
# Session Checkpoint: YYYY-MM-DD

## Summary

One paragraph. What happened, what changed, why it matters.

## Topics

- Bullet list of themes covered

## Entities

- Named things: repos, files, services, people, tools, APIs

## Decisions

- What was decided and why (brief)

## Actions

- [x] Completed items
- [ ] Open items for next session

## Context

- Runtime details, gotchas, things the next agent needs to know
```

## Rules

1. **Summary** is mandatory. Everything else is optional but encouraged.
2. **Actions** distinguish done (`[x]`) from open (`[ ]`). Open items are the handoff.
3. **Context** captures things that aren't obvious — error patterns, env quirks, timing issues.
4. Filename: `YYYY-MM-DD-HHMMSS-checkpoint.md`
5. One checkpoint per session. Update rather than duplicate.

## Who Produces These

- **Claude Code**: End of session, dropped to `from-claude-code/`
- **OpenClaw**: End of conversation or on demand, dropped to `from-openclaw/`
- **MemoryVault** (Poe): `!checkpoint` command, stored as CDN
- **Any future agent**: Same format, different drop directory
