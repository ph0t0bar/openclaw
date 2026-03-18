# Security Escalations

## 2026-03-18 08:51 UTC - CRITICAL: API Key Exposure

**Finding:** Anthropic API key `sk-ant-oat01-GgOnC1EC...` exposed in multiple workspace files

**Risk:** HIGH - Live API key in version control and health cache
**Locations Found:**
- `skills/heartbeat-consolidator/data/health_cache.json` - Error message containing partial key
- `docs/help/testing.md` - Setup token documentation (example)
- `docs/specs/ESCALATIONS.md` and `docs/ops/escalations.md` - Documentation references

**Immediate Action Required:**
1. Rotate the Anthropic API key immediately
2. Clean health cache files (`skills/heartbeat-consolidator/data/health_cache.json`)
3. Update ANTHROPIC_API_KEY environment variable
4. Review git history for additional exposures
5. Add key redaction to health monitoring systems

**Detection:** GOVERNANCE automated scan (30min rotation)
**Status:** OPEN - Requires immediate attention

**Root Cause:** Dropper-Code task failure included full API key in error message, persisted to health cache