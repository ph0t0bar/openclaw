# Escalations — Chief of Staff Gap Check
## 2026-03-17 19:42 UTC

### 🔴 CRITICAL: Digest Pipeline Stalled
- **Symptom:** Only 2 digests sent in 24h (down from 70+)
- **Impact:** 105 users not receiving core value
- **Last known working:** Pre-18:06 UTC (per PRD Section 8)
- **Hypothesis:** digest_sender.py regression or DIGEST-POLICY.md enforcement

### 🟡 HIGH: Hub Error Spike
- **Symptom:** 24 errors in 19:00 hour
- **Needs:** Error log inspection

### 🟢 Backup: Healthy
- Last commit: 4 min ago (2026-03-17T19:38:24Z)

### 🟢 Agents: Active
- All agents posted within last hour
- No >2h silence gaps

---
*Next check: 20min or on heartbeat*
