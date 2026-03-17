# SPEC-DigestBot — Operations Agent for Digest Pipeline

**Status:** Draft  
**Created:** 2026-03-17  
**Department:** Operations  
**Cadence:** 30 minutes  
**Priority:** CRITICAL (blocks launch)

---

## 1. Purpose

DigestBot owns the DropAnywhere digest pipeline end-to-end. Without working digests, DropAnywhere is just an inbox. With digests, it's magic. This agent ensures digests flow reliably from drop aggregation → insight extraction → email delivery.

**Core mandate:** Detect, diagnose, and recover digest stalls automatically. Escalate to humans only when automated recovery fails.

---

## 2. Current State (Crisis)

- **Failure rate:** 97% (3 digests sent vs 90-100 expected in 24h)
- **Root cause:** `DISABLE_CRONS=1` on Hub prevents scheduler execution
- **Impact:** 14+ users affected, launch blocker
- **Email infra:** Healthy (96 emails delivered via Resend)

**Related PRs:** #180-186 (opoerator-hub), all attempting digest scheduler fixes

---

## 3. Responsibilities

### 3.1 Monitoring (Every 30min)
- [ ] Query `/api/admin/stats` for `digests_sent_24h`
- [ ] Alert if < 50% of expected volume (threshold: < 45 digests/24h)
- [ ] Check Resend delivery rates (via `/api/ops/dashboard`)
- [ ] Track user digest eligibility flags in DB

### 3.2 Auto-Recovery (When stall detected)
- [ ] Attempt manual trigger via Hub API (if endpoint exists)
- [ ] Reset stuck `digest_pending` flags for eligible users
- [ ] Check `DISABLE_CRONS` env var state
- [ ] Log all recovery attempts to daily log

### 3.3 Escalation (When auto-recovery fails)
- [ ] Create Dropper-Code task with full context
- [ ] Notify Joey via WhatsApp with summary + action taken
- [ ] Update agent-board.md with incident status

### 3.4 Reporting
- [ ] Daily digest health summary (sent to Joey)
- [ ] Weekly pipeline metrics (sent to PRD maintenance cron)
- [ ] Incident timeline for each stall event

---

## 4. API Endpoints to Poll

| Endpoint | Purpose | Frequency |
|----------|---------|-----------|
| `GET /api/admin/stats` | Digest counts, user activity | Every 30min |
| `GET /api/ops/dashboard` | System health, Resend metrics | Every 30min |
| `GET /api/alerts/daily-summary` | Trigger manual summary | On-demand |
| `POST /api/digests/trigger` | Manual digest trigger (if exists) | Recovery only |

---

## 5. Alert Conditions

| Severity | Condition | Action |
|----------|-----------|--------|
| 🔴 CRITICAL | `digests_sent_24h` < 10 | Immediate WhatsApp + auto-recovery |
| 🟠 WARNING | `digests_sent_24h` < 45 | Log + monitor for 2 cycles |
| 🟡 INFO | Single user digest stall > 48h | Queue for batch recovery |

---

## 6. Cron Configuration

```json
{
  "name": "DigestBot — Digest Pipeline Monitor",
  "schedule": { "kind": "every", "everyMs": 1800000 },
  "payload": {
    "kind": "agentTurn",
    "message": "[DigestBot] Run digest pipeline health check. Query Hub /api/admin/stats and /api/ops/dashboard. If digests_sent_24h < 45, attempt recovery. Log to daily log. Escalate if auto-recovery fails.",
    "model": "openrouter/moonshotai/kimi-k2.5"
  },
  "sessionTarget": "isolated",
  "delivery": { "mode": "none" }
}
```

---

## 7. Success Metrics

- [ ] Digest success rate > 95% (target: 90-100 digests/24h)
- [ ] Mean time to detect (MTTD) stall: < 30 minutes
- [ ] Mean time to recover (MTTR) stall: < 2 hours
- [ ] Zero manual interventions per week (goal)

---

## 8. Open Questions

1. Does Hub have a manual digest trigger endpoint? (Check PR #186)
2. Should DigestBot also monitor `dropanywhere-cron` service health?
3. What's the approved recovery procedure for bulk user flag resets?
4. Should DigestBot own the daily summary generation currently in Hub?

---

## 9. Dependencies

- Hub API access (`HUB_API_KEY`)
- WhatsApp notification channel
- Dropper-Code task creation access
- Read access to agent-board.md for incident logging

---

## 10. Next Steps

1. ✅ Create this skeleton spec (SpecBot — today)
2. [ ] Get Joey approval on scope/mandate
3. [ ] Create cron job (via `cron add`)
4. [ ] Test first run manually
5. [ ] Document runbook in `ops/digestbot-runbook.md`

---

*Built on agent-board.md proposal by Opus Strategist (2026-03-16)*
*Related: SPEC-DigestBot-v2.md (detailed implementation — future)*
