# Agent Communications Guide

## Internal: Reaching Claw (Co-CEO / Chief of Staff)

**Your door is always open.** Three channels:

1. **Agent Board** (`ops/agent-board.md`) — For work posts, votes, proposals. Async. All agents see it.
2. **Escalations** (`ops/escalations.md`) — For things that need Claw's decision or action. Checked every heartbeat.
3. **Direct session message** — For URGENT matters. Use this instruction in your output:
   ```
   ESCALATE TO CLAW: [your message]
   ```
   When delivery mode is "announce", this reaches the main session where Claw lives.

**When to use each:**
| Need | Channel |
|------|---------|
| Normal work output | Agent Board |
| Teammate feedback | Agent Board (vote) |
| Need Claw's decision | Escalations file |
| Agent proposal | Agent Board + Escalations |
| URGENT (system down, revenue impact) | Direct escalate in output |
| Bug for Dropper-Code | Agent Board (DC Mgr picks up) |
| Strategic direction question | Escalations |

## External: Reaching Joey (Co-CEO / Human Founder)

**Joey gets notified via WhatsApp (+18477361508) or webchat.**

**Rules:**
- Only Claw sends messages to Joey directly (agents escalate TO Claw, Claw decides what Joey needs to see)
- Exception: CRITICAL alerts (system down, revenue loss) can include "ALERT JOEY:" prefix
- Morning brief is sent by Claw ~8am CST
- Don't spam Joey. Batch updates. Quality > quantity.

## External: Hub API (for operational actions)

All agents have access to:
- `HUB_API_KEY` — env var, use in X-API-Key header
- Hub base URL: `https://hub-production-f423.up.railway.app`
- See HEARTBEAT.md for endpoint list

## External: GitHub

- Token: `export $(grep GITHUB_TOKEN /root/.openclaw/.env.local | head -1)`
- Repos: opoerator-hub, dropanywhere-app, brutallyhonest-next, openclaw, joey-backup
- API: `curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/ph0t0bar/{repo}/...`

## External: Dropper-Code (Code Agent)

- Health: `GET https://dropper-code-production.up.railway.app/health`
- Trigger: `POST https://dropper-code-production.up.railway.app/trigger/{job_name}`
- Task queue: Via Hub API `/api/ops/tasks`

## Communication Flow

```
Agent finds something
    │
    ├─ Routine finding → Agent Board (teammates vote)
    ├─ Needs decision → Escalations file (Claw reviews)
    ├─ Urgent → "ESCALATE TO CLAW: ..." in output
    └─ Critical → "ALERT JOEY: ..." in output (rare!)
         │
    Claw reviews all channels
    │
    ├─ Resolves internally → Updates escalations + board
    ├─ Needs Joey → Messages Joey via WhatsApp/webchat
    └─ Spawns new work → Creates tasks, sets direction on board
```

## The Rule: No Lost Signals

Every finding, every bug, every idea, every question gets captured somewhere:
- Agent Board for work
- Escalations for decisions
- Daily log for history
- Goldmine index for discoveries

**Nothing falls through the cracks.**

