# COMMS-GUIDE — DropAnywhere Agent Company

## Communication Channels

### Internal (Agent-to-Agent)
- **Agent Board**: `ops/agent-board.md` — Routine updates, votes, status
- **Escalations**: `ops/escalations.md` — Decisions requiring judgment
- **Memory**: `memory/YYYY-MM-DD.md` — Daily logs, findings

### External (To Human)
- **URGENT prefix**: "ESCALATE TO CLAW: [message]" — Immediate attention
- **Approval prefix**: "ALERT JOEY: [message]" — Customer-facing needs OK

## Message Format

### Vote Format
```
VOTE: [TASK-ID]
CHOICE: ✅ | 🔄 | ❌ | 💡
REASON: [brief explanation]
```

### Status Update Format
```
STATUS: [AGENT-NAME] Cycle #[N]
- Checked: [what was checked]
- Found: [what was found]
- Action: [what was done]
```

### Task Creation Format
```
TASK: [TASK-ID]
TYPE: [bug|feature|infra|security]
ASSIGNEE: [dropper-code|railway-bot|frontend-bot|bha-bot]
PRIORITY: [P0|P1|P2|P3]
DESC: [description]
```

## Response Codes

| Emoji | Meaning |
|-------|---------|
| ✅ | Approve / Go |
| 🔄 | Revise / Retry |
| ❌ | Reject / Block |
| 💡 | Idea / Suggestion |
| 🟢 | Healthy / Good |
| 🟡 | Unknown / Pending |
| 🔴 | Problem / Down |
