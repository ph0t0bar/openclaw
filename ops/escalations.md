# Security Escalations

## 2026-03-17 05:29 UTC — CRITICAL: Exposed Secrets in Git

**Sentry Alert ID:** cron:8dad9141-819b-4775-b8fc-293870b9d386

**Finding:** Secret scan detected exposed API keys in recent git commits (HEAD~3):
- Anthropic API key (sk-ant-oat01-Pg23md...)
- Stripe secret key (sk_live_51PJKTn...)  
- GitHub tokens (github_pat_11A4VNG...)

**Risk Level:** 🔴 CRITICAL
- Live production keys exposed in git history
- Potential unauthorized access to Anthropic, Stripe, and GitHub
- Immediate key rotation required

**Immediate Actions Required:**
1. **Rotate all exposed keys immediately**
2. **Check access logs** for unauthorized usage
3. **Remove secrets from git history** (git filter-branch or BFG)
4. **Implement pre-commit hooks** to prevent future exposure
5. **Review all services** for unauthorized charges/activity

**Next Steps:**
- Joey must be alerted immediately via WhatsApp
- All exposed keys should be considered compromised
- Audit recent activity on all affected services

---