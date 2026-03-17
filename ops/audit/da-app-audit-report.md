# DropAnywhere App Audit — Email-Only Pivot

**Date:** 2026-03-16
**Repo:** `ph0t0bar/dropanywhere-app`
**Context:** Frontend being reduced to static landing page after email-only pivot

---

## a) Unnecessary Code Estimate

| Category | Files | Est. Lines | Status |
|----------|-------|-----------|--------|
| Dashboard components | ~50 | ~25,000 | 🔴 CUT |
| API routes (admin, vault, cron, feedback, roadmap) | ~15 | ~5,000 | 🔴 CUT |
| Pages (dashboard, canvas, digests, experimental, help) | ~6 | ~8,000 | 🔴 CUT |
| Hooks (useAnonymousDrop, useUserLayer) | 2 | ~300 | 🔴 CUT |
| Sentry config (edge, client) | 2 | ~50 | 🔴 CUT |
| Lib utilities (nudge, api helpers) | ~10 | ~3,000 | 🔴 CUT |
| **Total removable** | **~85 files** | **~41,000 lines** | |
| **Keep (landing + signup)** | **~10 files** | **~2,000 lines** | |

**Bottom line:** ~67% of code (41K of 61K lines) is dead weight post-pivot.

---

## b) Minimal Landing Page Setup

🟢 **Yes — strip to bare minimum:**

**Keep:**
- `pages/index.tsx` → Landing page with hero + signup form
- `components/SignupModal.tsx` → Email capture
- `components/Footer.tsx` → Standard footer
- `components/ExperientialHero.tsx` → Has signup API call (refactor to simple form)
- `styles/` → Tailwind config + globals
- `next.config.js` → Simplified (remove Sentry plugin)
- `public/` → Assets

**Kill everything else.** The signup should POST to Hub's `/api/signup` endpoint. That's it.

---

## c) Dead Environment Variables

🟡 SHOULD FIX — These reference services no longer needed:

| Variable | Used By | Status |
|----------|---------|--------|
| `ADMIN_KEY` | Admin API routes | 🔴 Dead — remove routes |
| `OPENCLAW_URL` | Admin health check proxy | 🔴 Dead |
| `OPENCLAW_HOOK_URL` / `OPENCLAW_HOOK_TOKEN` | Claw chat proxy | 🔴 Dead |
| `GITHUB_TOKEN` | Deploy trigger | 🔴 Dead |
| `RAILWAY_BACKEND_PROJECT` / `RAILWAY_BACKEND_SERVICE` | Deploy trigger | 🔴 Dead |
| `NEXT_PUBLIC_INGEST_KEY` | Dashboard drop ingestion | 🔴 Dead |
| `NEXT_PUBLIC_SENTRY_DSN` / `SENTRY_ORG` / `SENTRY_PROJECT` | Sentry (overkill for landing) | 🟡 Remove |
| `NEXT_PUBLIC_API_URL` | Multiple components | 🟡 Keep only for signup endpoint |

---

## d) Hardcoded Test Data & Debug Prints

🟡 SHOULD FIX — 18 `console.log` statements found in production code:

| File | Issue |
|------|-------|
| `VisualGoalGallery.tsx:53` | `console.log('[VisualGoal] Full response:', result)` |
| `RoadmapPanel.tsx:420-578` | 6× `console.log` debug statements |
| `VoiceMeetingRecap.tsx:313` | `console.log('Recognition restart failed')` |
| `dashboard.tsx:1136,1187` | `console.log('[Onboarding]...')` |
| `help.tsx:889` | `console.log(data)` — raw data dump |
| `experimental.tsx:91,287` | Admin debug logs |
| `pages/api/admin/proxy.ts:30-31` | Hardcoded `localhost` reference |

No hardcoded test emails found. The `localhost` in proxy.ts is a URL validation check (not a bug, but dead code).

---

## e) Overkill Dependencies

🟡 SHOULD FIX for a static landing page:

| Package | Size | Verdict |
|---------|------|---------|
| `@sentry/nextjs` | Heavy | 🔴 Remove — no need for error tracking on a landing page |
| `d3` + `@types/d3` | ~500KB | 🔴 Remove — was for ThoughtMap/charts |
| `@use-gesture/react` | Moderate | 🔴 Remove — swipe gestures for dashboard |
| `framer-motion` | ~150KB | 🟡 Could keep for landing page animations, or remove |
| `lottie-react` | Moderate | 🔴 Remove — animation library, overkill |
| `dompurify` | Small | 🔴 Remove — HTML sanitization for user content |
| `vitest` | Dev only | 🟡 Keep if you want tests, otherwise remove |

**Minimal deps:** `next`, `react`, `react-dom`, `tailwindcss`, `lucide-react` (icons), `typescript`

---

## f) TODO/FIXME/HACK Results

26 matches found. All are in components/pages being cut:

| Location | Note |
|----------|------|
| `RoadmapPanel.tsx` (5×) | TODO.md integration references |
| `ArchitectureMap.tsx` (9×) | TODO.md visualization |
| `LaunchPanel.tsx` (4×) | TODO.md pending tasks |
| `pages/api/docs/planning.ts` (2×) | TODO.md parser |
| `pages/api/feedback.ts` (3×) | TODO.md routing |
| `pages/api/roadmap/ingest.ts` (3×) | TODO.md ingestion |

**Verdict:** 🟢 All in dead code. Will vanish when files are deleted.

---

## Summary

| Category | Rating | Action |
|----------|--------|--------|
| Code bloat | 🔴 FIX BEFORE LAUNCH | Delete ~85 files, keep ~10 |
| Dead env vars | 🟡 SHOULD FIX | Remove 8 variables from Railway |
| Debug prints | 🟡 SHOULD FIX | In dead code, will vanish with cleanup |
| Dependencies | 🟡 SHOULD FIX | Remove 5 packages, save ~700KB |
| TODOs | 🟢 OK | All in dead code |

**Recommendation:** Create a fresh `landing-page` branch. Copy only the ~10 needed files. Don't try to surgically remove from main — too much entanglement. Clean slate is faster.
