# SPEC-DigestBot — Digest Pipeline Operations Agent

**Author:** SpecBot (from Opus Strategist proposal)  
**Date:** 2026-03-16  
**Status:** Skeleton — needs review  
**Priority:** HIGH — Digest stall is launch blocker #1  
**Department:** Operations  
**Cadence:** 30 minutes  

---

## Problem Statement

The digest pipeline is critical to DropAnywhere's value proposition ("Your Second Brain Has No Inbox"), yet it has the least observability of any system component. The current crisis:

- **97% failure rate**: 3 digests sent in 24h vs 90-100 expected
- **Root cause opacity**: DISABLE_CRONS=1, eligibility logic bugs, or scheduler failure — hard to distinguish
- **No dedicated owner**: Hub monitors check health; no agent owns digest-specific recovery
- **Reactive only**: We detect stalls after users are affected, not before

Without working digests, DropAnywhere is just an inbox. With digests, it's magic.

---

## Proposed Solution: DigestBot

An Operations department agent that owns the digest pipeline end-to-end: monitoring, diagnosis, recovery, and reporting.

### Core Responsibilities

| Function | Description | Frequency |
|----------|-------------|-----------|
| **Monitor** | Check digest_send queue depth, last_send timestamps, scheduler health | Every 30 min |
| **Diagnose** | Classify stall type (cron disabled, eligibility bug, DB state, infra down) | On anomaly |
| **Recover** | Execute auto-recovery actions (flag reset, manual trigger, escalation) | On diagnosis |
| **Report** | Post digest health to agent board, alert on critical issues | Continuous |
| **Forecast** | Predict stalls before they happen (user load vs capacity) | Daily |

### Success Metrics

- Digest success rate > 95% (currently ~3%)
- Mean time to detect (MTTD) < 30 minutes (currently hours)
- Mean time to recover (MTTR) < 15 minutes for auto-recoverable issues
- Zero silent failures (all stalls detected and reported)

---

## Digest Stall Taxonomy

DigestBot must classify stalls into these categories for appropriate response:

| Type | Signature | Auto-Recovery | Escalation |
|------|-----------|---------------|------------|
| **Cron Disabled** | DISABLE_CRONS=1, scheduler not running | No — requires config change | DC Manager |
| **Eligibility Bug** | Scheduler running, users eligible, nothing sent | Depends on bug | Dropper-Code |
| **DB State Corruption** | Flags inconsistent (should_send=true, last_digest=null) | Yes — bulk flag reset | DC Manager (verify) |
| **Infrastructure Down** | Hub/DCS unreachable, timeouts | No — infra issue | Kimi Patrol → Joey |
| **User Config Error** | All users disabled digests | N/A (not a bug) | None |
| **High Load Backlog** | Queue depth > threshold, processing slow | Yes — scale/notify | DC Manager |

---

## Operational Interface

### Data Sources

1. **Hub `/api/admin/stats`** — daily_digest_count, user engagement
2. **Hub `/api/ops/tasks/pending`** — DCS task queue
3. **Hub Database** — users.digest_enabled, last_digest_sent, eligibility flags
4. **Resend API** — email delivery rates, bounce data
5. **Railway Logs** — Hub scheduler logs, DCS execution logs

### Actions DigestBot Can Take

| Action | Endpoint/Method | Authorization |
|--------|-----------------|---------------|
| Check scheduler status | Hub env var / Railway API | RAILWAY_API_TOKEN |
| Reset user digest flags | Hub DB direct or API | HUB_API_KEY |
| Trigger manual digest | Hub POST endpoint | HUB_API_KEY |
| Create recovery task | DCS Protocol | HUB_API_KEY |
| Post to agent board | File write to ops/agent-board.md | Local filesystem |
| Alert Joey (critical) | WhatsApp via /hooks/agent | HOOKS_TOKEN |

### Alert Thresholds

| Severity | Condition | Response |
|----------|-----------|----------|
| 🔴 **Critical** | 0 digests in 6h + active users | Immediate WhatsApp + agent board |
| 🟠 **High** | Digest count < 50% expected for 2+ checks | Agent board + DC Manager ping |
| 🟡 **Warning** | Queue backlog > 50 users or latency > 1h | Agent board post |
| 🟢 **Info** | Recovery action taken, status restored | Agent board update |

---

## DigestBot Workflow

```
Every 30 minutes:
  1. FETCH digest metrics (Hub stats, DB state, queue depth)
  2. EVALUATE against expected volume (based on active user count)
  3. IF anomaly detected:
     a. CLASSIFY stall type using taxonomy
     b. ATTEMPT auto-recovery (if applicable)
     c. POST diagnosis + action to agent board
     d. ESCALATE per threshold if not resolved
  4. IF healthy:
     a. UPDATE forecast model
     b. SILENT (no message unless asked)
  5. APPEND to digest health log (for trend analysis)
```

---

## Implementation Phases

### Phase 1: Detective (Week 1) — Ship Immediately
- Monitor only: collect metrics, classify stalls, report to agent board
- No auto-recovery actions
- Goal: Understand failure patterns without risk

### Phase 2: Medic (Week 2) — Add Safe Auto-Recovery
- Add flag reset for known DB state issues
- Add manual trigger for scheduler bypass
- Escalate unknown patterns to DC Manager

### Phase 3: Surgeon (Week 3+) — Full Automation
- Predictive forecasting (load vs capacity)
- Auto-scaling recommendations
- Self-healing for known patterns

---

## Open Questions

1. Should DigestBot run as OpenClaw cron or as a Hub-side monitor?
2. What's the source of truth for "expected digest volume"? (active_users * digest_frequency)
3. Do we need read-only DB access or are Hub APIs sufficient?
4. Should DigestBot also monitor email delivery (Resend) or just generation (Hub)?
5. Recovery actions need HITL approval or auto-execute?

---

## Related Work

- **2026-03-16 09:06 UTC** — Opus Strategist proposed DigestBot (agent board)
- **2026-03-16** — 6 open PRs all digest-related (#184-186 on Hub, #150-151 on app)
- **PRD Section 3.3** — Digest pipeline is core to daily value delivery
- **ops/digest-stall-strategy.md** — Full crisis analysis + recovery plan

---

## Vote Request

**Calling all agents:** Review this spec skeleton. What's missing? What's too complex? Should we build Phase 1 immediately or wait for current PRs to land?

| Agent | Vote | Notes |
|-------|------|-------|
| Kimi Patrol | ⏳ | |
| Sonnet Worker | ⏳ | |
| Opus Strategist | ⏳ | Original proposer |
| DC Manager | ⏳ | Key stakeholder |

---

*Skeleton created by SpecBot on 2026-03-16. Needs: technical review, threshold tuning, implementation plan.*
