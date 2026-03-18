# Escalations

## 2026-03-18 09:39 UTC - EXPOSED API KEY DETECTED

**Severity:** 🔴 CRITICAL

**Finding:** Anthropic API key `sk-ant-oat01-GgOnC1EC...` found exposed in git diff (recent commits)

**Impact:** 
- Potential unauthorized access to Anthropic API
- Possible billing abuse
- Security breach of AI services

**Immediate Actions Required:**
1. Rotate the exposed Anthropic API key immediately
2. Review git history for the exposed key
3. Check Anthropic billing for unauthorized usage
4. Update all services using this key

**Detection:** Sentry automated scan (cron job 8dad9141)
**Reporter:** SENTRY AI
**Status:** ESCALATED - Requires immediate attention

---

## 2026-03-18 09:47 UTC - DOCBOT TIMEOUT CLUSTER

**Severity:** 🟡 MEDIUM

**Finding:** DocBot agent has 8+ consecutive timeout failures across multiple sessions

**Pattern:** 
- Consistent timeouts during document update operations
- May be related to PRD.md size (60KB+) or Hub API latency
- Infrastructure strain with system success rate at 73% (below 95% target)

**Recommendation:** 
- **Option 1:** Prompt optimization to reduce scope/complexity
- **Option 2:** Disable DocBot temporarily until infrastructure improved
- **Option 3:** Implement timeout handling/retry logic

**Similar Agents Affected:**
- Creative Review Emailer (4 consecutive timeouts)
- SkillMiner (3 consecutive timeouts) - now resolved

**Detection:** Meta organizational effectiveness monitoring
**Reporter:** META AI
**Status:** REQUIRES INVESTIGATION

---