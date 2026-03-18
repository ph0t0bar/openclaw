# Security Escalations

## 2026-03-18 08:51 UTC - CRITICAL: API Key Exposure

**Finding:** Anthropic API key `sk-ant-oat01-GgOnC1EC...` exposed in git history (last 3 commits)

**Risk:** HIGH - Live API key in version control
**Location:** Git diff shows key in error message/log output
**Immediate Action Required:**
1. Rotate the Anthropic API key immediately
2. Review git history for other exposed secrets
3. Update ANTHROPIC_API_KEY environment variable
4. Consider git history rewrite if key is in committed files

**Detection:** Sentry automated scan (15min rotation)
**Status:** OPEN - Requires immediate attention