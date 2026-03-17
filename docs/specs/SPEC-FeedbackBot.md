# SPEC-FeedbackBot — Drop Routing & Decision Processing Agent

**Status:** Skeleton  
**Created:** 2026-03-17 12:11 UTC by SpecBot  
**Source:** ops/agent-board.md — FeedbackBot actively processing drops without spec coverage  

---

## 1. Purpose

FeedbackBot is the intake router for Joey's DropAnywhere drops. It reads incoming drops, classifies them by intent, routes actionable items to appropriate agents, and maintains the decision ledger for the agent swarm.

**Core Jobs:**
1. Read and classify new drops from Joey
2. Route high-priority items to agent-board actions
3. Log decisions to `decisions.log`
4. Maintain `ops/agent-board.md` current status

---

## 2. Trigger & Cadence

| Parameter | Value |
|-----------|-------|
| **Trigger** | Cron (every 30min) + Webhook on new drop |
| **Runtime** | 5-10 minutes |
| **Priority** | HIGH — blocks all downstream agent work |

---

## 3. Inputs

| Source | Endpoint/Path | Data |
|--------|---------------|------|
| DropAnywhere Hub | `/api/search?user_id=b419d8ad5d23513f` | Recent drops from Joey |
| Current Board | `ops/agent-board.md` | Existing actions, votes, status |

---

## 4. Processing Logic

### 4.1 Drop Classification

```
IF drop.content contains "approve" | "reject" | "hold" → Decision Response
IF drop.content contains "kill" | "stop" | "disable" → Product Decision
IF drop.content contains "urgent" | "asap" | "emergency" → Escalation
IF drop.content contains "resend" | "retry" | "again" → Retry Request
ELSE → General Feedback / Content
```

### 4.2 Routing Table

| Drop Type | Route To | Action |
|-----------|----------|--------|
| Product decision (kill ACKs, etc.) | `decisions.log` + SPEC task | Create/Update spec |
| Compliance issue | Immediate agent-board alert | Flag for Sonnet Worker |
| Content approval | `approved-content.md` | Archive for reuse |
| Strategic insight | ops/agent-board.md | Post as vote item |
| Bug report | `docs/bugs/` + GitHub issue | Escalate to DC Manager |

### 4.3 Decision Ledger Format

Each processed drop appends to `decisions.log`:

```
[ISO8601] DROP-[id] — [classification]
  Source: [drop preview]
  Routed to: [agent/artifact]
  Action: [what was done]
```

---

## 5. Outputs

| Artifact | Path | Purpose |
|----------|------|---------|
| Agent Board | `ops/agent-board.md` | Current status, action queue |
| Decision Log | `ops/decisions.log` | Immutable decision record |
| Approved Content | `ops/approved-content.md` | Joey-approved copy for reuse |
| Spec Tasks | `docs/specs/SPEC-*.md` | Auto-create for product decisions |

---

## 6. Integration Points

| System | Direction | Notes |
|--------|-----------|-------|
| Hub API | Read | Search drops by user_id |
| WhatsApp | Write | Notify Joey of urgent items |
| GitHub | Write | Create issues for bugs |
| Agent Board | Read/Write | Collaborative workspace |

---

## 7. Open Questions

1. **Auto-approval threshold:** What decisions can FeedbackBot execute vs. escalate?
2. **Urgency detection:** How to distinguish "urgent" from casual use?
3. **Spec auto-creation:** Should product decisions auto-generate SPEC skeletons?
4. **Board voting:** Should FeedbackBot vote on existing items or just post new ones?

---

## 8. Next Steps

- [ ] Define classification prompt (low/med/high confidence)
- [ ] Create urgency detection rubric
- [ ] Build decisions.log parser for trend analysis
- [ ] Integrate with WhatsApp for real-time alerts

---

*The parrot way — Decisions flow like water* 🦜
