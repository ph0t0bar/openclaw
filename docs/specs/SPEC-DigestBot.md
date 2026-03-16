# SPEC — DigestBot (Operations Agent)

## Purpose
End-to-end ownership of the digest pipeline — from scheduler monitoring to user recovery to root cause analysis. DigestBot ensures DropAnywhere's core promise ("insights delivered daily") never fails silently.

## Status
🟡 **SKELETON** — Core structure defined, implementation details pending

## Problem Statement
The digest stall crisis (Mar 2026) revealed critical gaps:
- **No early warning:** 3 digests sent instead of 90-100 — detected by accident during routine check
- **No auto-recovery:** 14+ users stalled for 24+ hours without intervention
- **No root cause visibility:** Multiple hypotheses (DISABLE_CRONS, eligibility logic, DB flags) — no data to confirm
- **Reactive, not preventive:** We find out about stalls when users complain or agents happen to check

## Solution: DigestBot Operations Agent

### Core Responsibilities
| Function | What DigestBot Does | Frequency |
|----------|---------------------|-----------|
| **Monitor** | Track digest_sent metrics, alert on anomalies | Every 30min |
| **Diagnose** | When stall detected, run root cause playbook | On alert |
| **Recover** | Execute user recovery (batch trigger, flag reset) | Auto on P0 |
| **Report** | Document incidents, update agent board | After resolution |
| **Prevent** | Proactive checks before stalls occur | Daily |

### Success Criteria
- **Detection latency:** < 30min from first missed digest to alert
- **Recovery time:** < 1h from alert to bulk user recovery
- **False positive rate:** < 5% (avoid alert fatigue)
- **Coverage:** 100% of active users monitored

## Architecture

### Data Sources
```yaml
hub_dashboard:
  endpoint: /api/ops/dashboard
  metrics:
    - digests_sent_24h
    - active_users_24h
    - emails_delivered_24h
    - drops_created_24h

hub_database:
  query_permissions: read-only
  tables:
    - users (digest_enabled, last_digest_at)
    - digests (status, created_at, sent_at)
    - drops (user_id, created_at)

scheduler_state:
  env_vars:
    - DISABLE_CRONS (boolean)
    - DIGEST_SCHEDULE (cron expression)
    - POLL_INTERVAL (seconds)
```

### Alert Thresholds
| Metric | Normal | Warning | Critical |
|--------|--------|---------|----------|
| Digests sent (24h) | 80-120 | 40-79 | < 40 |
| Active users with 0 digests (48h) | 0-5 | 6-15 | > 15 |
| Scheduler last run | < 5min ago | 5-30min ago | > 30min ago |
| Failed digest jobs | 0-2 | 3-10 | > 10 |

## Detection Playbook

### Step 1: Metrics Collection (Every 30min)
```python
# Pseudocode for detection logic
def check_digest_health():
    dashboard = fetch_hub_dashboard()
    expected_digests = dashboard.active_users * 0.9  # 90% delivery rate
    actual_digests = dashboard.digests_sent_24h
    
    if actual_digests < expected_digests * 0.5:  # < 50% of expected
        return AlertLevel.CRITICAL
    elif actual_digests < expected_digests * 0.8:  # < 80% of expected
        return AlertLevel.WARNING
    else:
        return AlertLevel.HEALTHY
```

### Step 2: Root Cause Analysis (On Alert)
When alert triggered, check in order:

1. **Environment Check** (30s)
   - Is DISABLE_CRONS=1? → Immediate cause identified
   - Is Hub responding? → If not, infrastructure issue

2. **Scheduler Check** (1min)
   - Last scheduler run timestamp
   - Cron job execution logs
   - Queue depth (pending digests)

3. **User-Level Check** (2min)
   - Query users with digest_enabled=true AND last_digest_at < now - 24h
   - Count stalled users
   - Check for patterns (specific user segment?)

4. **Database Check** (2min)
   - Pending digest jobs with status='failed'
   - Recent errors in digest generation
   - Locks or contention on digest tables

### Step 3: Auto-Recovery (If safe)
| Condition | Auto-Action |
|-----------|-------------|
| DISABLE_CRONS=1 AND < 10 stalled users | Alert only (needs human decision) |
| DISABLE_CRONS=0 AND scheduler stuck | Trigger scheduler manually |
| User flags stale (> 48h) | Reset digest flags for affected users |
| Eligibility window bug confirmed | Batch trigger with fixed window |

## Message Bottle Integration

DigestBot writes bottles to `ops/bottles/DIGESTBOT/`:

### Healthy Check Bottle (every 30min)
```yaml
---
from: DIGESTBOT
type: metric
priority: p3
---
## Summary
Digest pipeline healthy — 94 digests sent (24h), 0 stalled users

## Metrics
- digests_sent_24h: 94
- active_users: 105
- stalled_users: 0
- scheduler_status: running
```

### Alert Bottle (on anomaly)
```yaml
---
from: DIGESTBOT
type: alert
priority: p0
---
## Summary
🚨 DIGEST STALL DETECTED: Only 3 digests sent (expected 90+)

## Root Cause (Preliminary)
DISABLE_CRONS=1 — scheduler not running

## Affected Users
14 users stalled > 24h

## Auto-Recovery
Disabled — DISABLE_CRONS requires human decision

## Recommended Action
Remove DISABLE_CRONS or create external trigger endpoint
```

## Runbook: Manual Recovery

When auto-recovery can't proceed, DigestBot creates a task bottle for Dropper-Code Manager:

```yaml
---
from: DIGESTBOT
type: task
priority: p0
assignee: DROPPER-CODE-MANAGER
---
## Task: Emergency Digest Recovery

### Context
Digest stall detected. Auto-recovery blocked by DISABLE_CRONS=1.

### Steps Required
1. Remove DISABLE_CRONS from Hub env vars OR
2. Create external trigger endpoint at /api/alerts/trigger-digests
3. Deploy and verify scheduler running
4. Run bulk recovery for 14 stalled users (script provided below)

### Recovery Script
```bash
curl -X POST https://hub-production-f423.up.railway.app/api/alerts/bulk-recover \
  -H "Authorization: Bearer $HUB_API_KEY" \
  -d '{"user_ids": ["id1", "id2", ...], "reason": "digest_stall_recovery"}'
```

### Verification
DigestBot will confirm recovery within 30min of deployment.
```

## Implementation Checklist

### Phase 1: Monitoring (Week 1)
- [ ] Create DigestBot agent skeleton
- [ ] Implement Hub dashboard polling
- [ ] Set up alert thresholds
- [ ] Write message bottle format
- [ ] Test detection on historical stall data

### Phase 2: Diagnosis (Week 2)
- [ ] Build root cause playbook
- [ ] Add database query capabilities
- [ ] Create diagnostic report format
- [ ] Integrate with agent board

### Phase 3: Recovery (Week 3)
- [ ] Implement safe auto-recovery rules
- [ ] Build bulk recovery script
- [ ] Create task delegation to Dropper-Code
- [ ] Add recovery verification

### Phase 4: Prevention (Week 4)
- [ ] Proactive health checks
- [ ] Trend analysis (predict stalls before they happen)
- [ ] User communication templates
- [ ] Incident post-mortem automation

## Metrics Dashboard

DigestBot tracks:

| Metric | Target | Current |
|--------|--------|---------|
| Mean time to detect (MTTD) | < 30min | TBD |
| Mean time to recover (MTTR) | < 1h | TBD |
| Digest success rate | > 95% | TBD |
| False positive rate | < 5% | TBD |
| Users recovered automatically | > 80% | TBD |

## Related
- SPEC-Message-Bottle-Protocol.md — Async communication standard
- AGENT-COMPANY-v3.md — Agent roles and responsibilities
- ops/digest-stall-strategy.md — Root cause analysis of Mar 2026 crisis
- Hub PR #186 — DISABLE_CRONS discussion

## Open Questions
1. Should DigestBot have write access to Hub env vars for DISABLE_CRONS removal?
2. How to handle partial digests (some users succeed, others fail)?
3. Should we maintain a "digest quality score" beyond just delivery?
4. Integration with Weekly Catch — should stalled users get special handling?

---
*Created: 2026-03-16 by SpecBot*
*Status: Skeleton — needs implementation review*
*Priority: P0 — blocks launch*
