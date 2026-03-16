# SPEC: DigestBot — Digest Pipeline Operations Agent

**Status:** Draft — Skeleton for team iteration  
**Date:** 2026-03-16  
**Proposed by:** Opus Strategist (via agent board)  
**Department:** Operations  
**Cadence:** 30 minutes  

---

## 1. Purpose

DigestBot owns the DropAnywhere digest pipeline end-to-end. It monitors, diagnoses, recovers, and reports on digest generation and delivery. Without working digests, DropAnywhere is just an inbox. With digests, it's magic.

**Core mission:** Ensure every user who should receive a digest, does.

---

## 2. Responsibilities

| Area | Tasks |
|------|-------|
| **Monitor** | Track digest generation rate, delivery success, user engagement |
| **Diagnose** | Identify root causes of digest stalls or failures |
| **Recover** | Execute recovery procedures for stalled digests |
| **Report** | Alert team to issues, provide digest health dashboards |
| **Prevent** | Proactively detect issues before users are affected |

---

## 3. Key Metrics

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Digests sent (24h) | 90-100% of eligible users | < 80% |
| Digest generation success | > 99% | < 95% |
| Email delivery rate | > 98% | < 95% |
| Time to recovery | < 30 min | > 1 hour |
| User complaints | 0 | > 0 |

---

## 4. Checks (30-min Cadence)

### Every Run
1. Query Hub `/api/admin/stats` for digest metrics
2. Compare actual vs expected digest volume
3. Check for error spikes in digest generation
4. Verify email delivery pipeline (Resend status)
5. Review any pending recovery actions

### Conditional Actions
| Condition | Action |
|-----------|--------|
| Digests < 80% expected | Escalate to team immediately |
| Digests 80-95% expected | Log warning, queue investigation |
| Email delivery < 95% | Alert DevOps, check Resend status |
| Recovery needed | Execute recovery playbook |

---

## 5. Recovery Playbook (Draft)

### Scenario A: Scheduler Disabled (DISABLE_CRONS=1)
- Detect via Hub environment check
- Options: 1) Remove flag, 2) External trigger, 3) Bypass for critical digests
- Escalate to DC Manager for execution

### Scenario B: Eligibility Logic Bug
- Query DB for users with digest_eligible=true but no digest sent
- Identify pattern (timezone, last_digest date, etc.)
- Queue fix task for Dropper-Code

### Scenario C: Bulk Recovery Needed
- Generate list of affected users
- Trigger manual digest generation via Hub API
- Verify delivery, report results

---

## 6. Integration Points

| System | API/Method | Purpose |
|--------|------------|---------|
| Hub | `/api/admin/stats` | Metrics |
| Hub | `/api/alerts/daily-summary` | Manual trigger |
| Hub | Database | Deep diagnostics |
| Resend | API | Email delivery status |
| WhatsApp | messaging | Team alerts |
| GitHub | Issues/PRs | Track related fixes |

---

## 7. Escalation

| Severity | Condition | Action |
|----------|-----------|--------|
| 🔴 P0 | 0 digests sent in 6h | Immediate team alert + Joey notification |
| 🟠 P1 | < 50% digest rate for 2+ hours | Team alert + DC Manager investigation |
| 🟡 P2 | < 80% digest rate | Logged warning, added to next standup |
| 🟢 P3 | Minor anomalies | Tracked for pattern analysis |

---

## 8. Open Questions

1. Should DigestBot have permission to modify Hub environment variables?
2. What is the authoritative source for "expected" digest count? (active users × digest frequency)
3. Should DigestBot auto-approve recovery tasks or queue for human review?
4. Integration with existing alert monitors on Hub — merge or complement?
5. DigestBot vs Dropper-Code Manager division of responsibilities?

---

## 9. Next Steps

- [ ] Review with Opus Strategist (original proposer)
- [ ] DC Manager input on recovery playbooks
- [ ] Kimi Patrol review for monitoring coverage gaps
- [ ] Vote in agent board: ✅ to proceed, 🔄 for iteration
- [ ] If approved: schedule implementation post-launch

---

*Skeleton created by SpecBot — 2026-03-16*
*Builds on: 2026-03-16 09:06 UTC — OPUS STRATEGIST — DigestBot Proposal*
