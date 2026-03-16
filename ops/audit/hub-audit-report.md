# oPOErator Hub — Pre-Launch Code Audit

**Date:** 2026-03-16  
**Target:** Soft launch March 24  
**Repo:** `ph0t0bar/opoerator-hub` (main branch)  
**File:** `main.py` — 27,474 lines (monolith)  

---

## Summary

| Metric | Count |
|--------|-------|
| Total API routes | 219 |
| Issues found | 12 |
| 🔴 Fix before launch | 1 |
| 🟡 Should fix | 6 |
| 🟢 OK / acceptable | 5 |

**Critical action items:**
1. 🔴 **Verify `OPENCLAW_HOOK_URL` is set** on Railway (alerts won't forward without it)

---

## A) Dead Endpoints

219 routes registered. The codebase is a monolith — many endpoints exist for internal/agent use rather than frontend calls. Notable potentially unused routes:

| Endpoint | Status | Notes |
|----------|--------|-------|
| `/api/screenshots/capture` | 🟡 SHOULD FIX | Screenshot service — unclear if used by any client |
| `/api/cron/weekly-snapback` | 🟢 OK | Cron endpoint, called externally or by scheduler |
| `/api/cron/snapback-prompts` | 🟢 OK | Same |
| `/api/cron/ambient-organization` | 🟡 SHOULD FIX | Unclear caller — verify if anything triggers this |
| `/api/cron/escalate-actions` | 🟡 SHOULD FIX | Same |
| `/api/checkpoint/*` | 🟢 OK | Used by Poe bots for memory |
| `/api/zapier/*` | 🟢 OK | PR #189 just added Zapier integration |
| `/api/roadmap/*` | 🟢 OK | DCS/TODO.md management — active feature |
| `/api/visual-goal/*` | 🟡 SHOULD FIX | Image generation feature — verify if frontend uses this |
| `/api/language-framework/*` | 🟡 SHOULD FIX | Unclear usage |
| `/dashboard`, `/signup` | 🟢 OK | HTML pages served directly |

**Verdict:** No routes are actively harmful. Several cron/admin endpoints exist for agent/tooling use. The ones flagged 🟡 should be verified against the frontend before launch — dead endpoints increase attack surface.

---

## B) Environment Variables

All env vars are fetched via `os.getenv()` with sensible defaults. Key findings:

| Env Var | Status | Notes |
|---------|--------|-------|
| `OPENCLAW_HOOK_URL` | 🔴 FIX BEFORE LAUNCH | Default is empty string `""`. If not set on Railway, ALL alert forwarding silently fails. Must be `https://openclaw-gateway-production-54a0.up.railway.app/hooks/agent` |
| `STRIPE_PREMIUM_LINK` | 🟡 SHOULD FIX | Default is `https://buy.stripe.com/placeholder` (line 232). Variable is defined but **never used** anywhere — dead code. Remove or set properly. |
| `RAILWAY_STAGING_*` | 🟢 OK | Staging env IDs hardcoded as defaults — fine for admin tooling |
| `ADMIN_USER_ID` | 🟢 OK | Defaults to Joey's ID `b419d8ad5d23513f` — correct |
| `UNSUBSCRIBE_SECRET` | 🟢 OK | Falls back to `INGEST_API_KEY` then `"dropanywhere_unsub"` — acceptable |

**Dead service references:**
- `dropanywhere-cron` appears in `MONITORED_REPOS` list (line 24599) — GitHub CI monitor will check this repo. 🟢 OK — it just monitors, doesn't call the service.

---

## C) Digest Pipeline

The digest system is **well-guarded** and ready to enable:

- `ENABLE_DIGEST_SCHEDULER` gates the background scheduler (startup, line 21412)
- `_monitor_digest_pipeline()` and `_monitor_digest_success_rate()` both short-circuit with `return` when `ENABLE_DIGEST_SCHEDULER != "true"` (lines 24638, 24680)
- PR #192 (merged 2026-03-16) specifically suppressed digest stall alerts during waitlist phase
- Manual trigger via `POST /api/cron/daily-digest` still works regardless of scheduler state
- Digest delivery via `POST /api/digest/deliver` and enhanced variant both functional

**Dead branches:** PRs #186, #190, #191 are unmerged digest-fix PRs. They're safe (not in main) but should be cleaned up post-launch.

🟢 **OK** — Clean, gated, ready to flip on.

---

## D) Alert Monitors

All monitors are in `main.py`. They fire via `_forward_alert_to_openclaw()` → `POST OPENCLAW_HOOK_URL`.

| Monitor | Interval | Threshold | False Positive Risk |
|---------|----------|-----------|-------------------|
| `_monitor_hub_health` | 1h | Latency > 5s | 🟢 Low |
| `_monitor_digest_pipeline` | 1h | No digest in 36h | 🟢 OK — now gated by `ENABLE_DIGEST_SCHEDULER` (PR #192) |
| `_monitor_digest_success_rate` | 1h | > 5% failure rate | 🟢 OK — also gated |
| `_monitor_error_rate` | 1h | > 20 errors/hour | 🟢 Low |
| `_monitor_stripe` | 4h | New sales/failures | 🟢 Low |
| `_monitor_github_repos` | 6h | Failed workflows, dependabot | 🟡 May fire on `dropanywhere-cron` repo (dead) |
| `_monitor_poe_costs` | 6h | Balance < 500, burn > 5K/6h | 🟢 Low |
| `_monitor_resend` | 6h | Bounces, delivery issues | 🟢 Low |
| `_monitor_railway` | 6h | Failed deployments | 🟢 Low |
| `_monitor_ga` | 6h | Traffic data | 🟢 Low (requires google-analytics-data package) |
| `_daily_ops_summary` | 24h | N/A | 🟢 Info only |

🟡 **SHOULD FIX:** Remove `dropanywhere-cron` from `MONITORED_REPOS` (line 24599) to prevent noise from a dead repo's stale CI.

---

## E) Recent PRs (Last 10 Merged)

| PR | Date | Title | Risk |
|----|------|-------|------|
| #193 | 2026-03-16 | Wire email webhook to OpenClaw hook — instant CEO email processing | 🟢 Low — additive, non-blocking (`asyncio.create_task`) |
| #192 | 2026-03-16 | Suppress digest stall alerts — digests intentionally disabled | 🟢 Good — fixes false positives |
| #189 | 2026-03-16 | Zapier Integration - "Drop to DropAnywhere" Action | 🟡 New feature — verify auth is solid on `/api/zapier/*` |
| #188 | 2026-03-16 | Digest Pipeline Error Budget + Alerting | 🟢 Monitoring improvement |
| #187 | 2026-03-16 | Add task dedup guard to POST /api/ops/tasks | 🟢 Bug fix |
| #177 | 2026-03-16 | JSON Export Endpoint for User Drops | 🟢 Admin endpoint |

**No regression risks identified.** All recent PRs are additive or defensive. The Zapier integration (#189) is the only new attack surface — verify the auth model.

---

## F) TODO/FIXME/HACK/XXX

**No actual TODO/FIXME/HACK comments found** in the codebase. All `TODO` references are to `TODO.md` file operations (the roadmap feature) or drop classification labels (`[TODO]` tag). Clean.

🟢 **OK**

---

## G) Test Data / Debug Leaks

| Finding | Status | Location |
|---------|--------|----------|
| Joey's emails hardcoded: `joeyhamer@gmail.com`, `joey@photobarchicago.com` | 🟢 OK | Line 4827 — used for CEO email hook, appropriate |
| Joey's user ID hardcoded as `ADMIN_USER_ID` default | 🟢 OK | Lines 6537, 6753 — falls back to env var |
| `SUPERADMIN_IDS` defaults include `"joey"` | 🟢 OK | Line 18496 |
| Known signup timestamps for 2 specific users | 🟢 OK | Backfill data (line 21460+) — one-time migration, harmless |
| `localhost:8080` / `127.0.0.1` references | 🟢 OK | Lines 17135, 24775, 27395 — self-health checks, correct |
| `STRIPE_PREMIUM_LINK` = `placeholder` | 🟡 Dead code | Defined but never referenced — remove |

**No test emails, fake users, or debug prints that would leak.** The codebase is production-oriented.

---

## H) Webhook Chain: `/api/webhook/email` → OpenClaw

**Flow verified:**

1. `POST /api/webhook/email` receives Resend inbound email
2. Validates Svix signature ✅
3. Loop guard rejects `@drop-anywhere.com` sender ✅
4. Idempotency check prevents duplicate processing ✅
5. Fetches full email content from Resend API if payload is metadata-only ✅
6. Resolves user by email → ingests to vault ✅
7. **For Joey's emails only:** Fires async hook to `https://openclaw-gateway-production-54a0.up.railway.app/hooks/agent` with `OPENCLAW_HOOK_TOKEN` ✅ (PR #193)

**Issue:** The CEO email hook (line 4841) hardcodes the OpenClaw URL rather than using `OPENCLAW_HOOK_URL` env var. This works but is fragile — if the gateway URL changes, this line won't update.

🟡 **SHOULD FIX:** Use `OPENCLAW_HOOK_URL` instead of hardcoded URL on line 4841.

**Non-Joey emails** do NOT fire to OpenClaw — they're silently ingested. This is correct behavior for launch.

---

## Architectural Note

⚠️ `main.py` is **27,474 lines**. This is a significant maintainability risk. Not a launch blocker, but post-launch refactoring into modules (routes, monitors, digest, DCS, auth) should be prioritized.

---

## Action Items (Ordered by Priority)

1. 🔴 **Set `OPENCLAW_HOOK_URL`** on Railway → `https://openclaw-gateway-production-54a0.up.railway.app/hooks/agent`
2. 🟡 **Remove `STRIPE_PREMIUM_LINK`** — dead variable (defined line 232, never used)
3. 🟡 **Line 4841:** Replace hardcoded OpenClaw URL with `OPENCLAW_HOOK_URL` env var
4. 🟡 **Line 24599:** Remove `dropanywhere-cron` from `MONITORED_REPOS`
5. 🟡 **Verify Zapier auth** on `/api/zapier/*` endpoints (PR #189)
6. 🟡 **Verify usage** of `/api/visual-goal/*`, `/api/screenshots/capture`, `/api/cron/ambient-organization`, `/api/cron/escalate-actions`
7. 🟡 **Close stale PRs** #185, #186, #190, #191 (unmerged digest fixes, superseded by #192)

---

*Audit complete. Read-only — no code was modified.*
