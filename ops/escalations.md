# ESCALATIONS - Chief of Staff Gap Findings

## Current Escalations (00:44 UTC)

### 🚨 P0 MANUAL TASK - Shadow Bot Cross-Promo (OVERDUE)
- **Issue:** Section 5.1 of PRD - Shadow bot cross-promo descriptions need manual update
- **Blocked by:** Poe API 500s on PATCH requests - must be done manually in Poe UI
- **Impact:** Every original conversation → funnel to v2 shadow bots with CTA + logging
- **Status:** Manual action required from Joey (10 minutes)
- **Why urgent:** 70K+ bot users not being funneled to Hub-backed versions

### ⚠️ DIGEST STALL - Only 2 Digests Sent (24h)
- **Normal:** 30-50 digests/day expected with 108 users
- **Actual:** 2 digests in 24 hours
- **Cause:** DISABLE_CRONS=1 on Hub (by design) but digest pipeline showing 0 attempts
- **Status:** Under investigation - may be working as intended (manual control)

### 📊 Family Members at Risk (User Health)
- **lhamer228@gmail.com:** 13 days inactive, 12 digests sent since engagement
- **rhamersunsetpartners@gmail.com:** 10 days inactive, 8 digests sent since engagement  
- **hamer.daniel@gmail.com:** 0 drops ever, digest enabled but frequency: none

### 🔧 OpenClaw CI Failure (Known Issue)
- **Status:** CI showing "failure" on dashboard
- **Impact:** Non-blocking - system operational
- **Note:** Known issue, system continues to function

---
*Updated: 2026-03-18 00:44 UTC*