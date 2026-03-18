# Security Escalations

## 2026-03-18 08:33 UTC - SECRET EXPOSURE

**Severity:** HIGH 🔴
**Type:** API Key Leak
**Found:** Anthropic API key (`sk-ant-oat01-GgOnC1EC...`) exposed in git diff within last 3 commits
**Location:** git diff HEAD~3 shows key in error message
**Action Required:** 
1. Rotate Anthropic API key immediately
2. Review commit history for other exposed secrets
3. Audit error logging to prevent future key exposure in logs

**Detection:** Sentry automated secret scan
**Reporter:** Claw (Sentry AI)