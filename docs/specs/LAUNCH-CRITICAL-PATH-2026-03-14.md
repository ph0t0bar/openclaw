# DropAnywhere: Critical Path to Launch
## The 10-Day Execution Map — March 14–24, 2026

---

## Status Update (Mar 17 10:31 UTC - Launch Coordinator)

**🚨 LAUNCH STATUS: CRITICAL RISK - 7 DAYS REMAINING**

| Phase | Window | Status |
|-------|--------|--------|
| **Phase 1: SURVIVAL** | Mar 14–15 | 🟡 PARTIAL — Poe balance RESTORED ✅, Digest stall persists |
| **Phase 2: STABILIZE** | Mar 16–19 | 🔴 BLOCKED — Cannot test launch items while digest pipeline is broken |
| **Phase 3: PREPARE** | Mar 20–23 | 🔴 AT RISK — 3 days to solve Phase 1+2 |
| **Phase 4: LAUNCH** | Mar 24–26 | 🔴 LAUNCH AT RISK — Digest is make-or-break |

**RECENT WINS (Mar 17 10:31 UTC):**
- ✅ **POE BALANCE RESTORED** — 283,939 points (was 12,522 💀). Burn ~76K/6h.
- ✅ Email webhook → OpenClaw (PR #193 merged Mar 16)
- ✅ Email address fix: noreply@ → hello@drop-anywhere.com (PR #195 merged Mar 17)
- ✅ Drop received emails reply in-thread (PR #198 merged Mar 17)
- ✅ Re-engagement emails disabled - only Joey receives (PR #197 merged Mar 17)
- ✅ Digest stall alerts suppressed (PR #192 merged Mar 16)
- ✅ Auto-response emails fixed — disabled at free tier + `<thinking>` stripped (PR #199 merged Mar 17)
- ✅ **7 HUB PRS MERGED** — #193, #195-199 (email fixes batch)

**CRITICAL BLOCKERS (LAUNCH KILLER):**
- 🚨 **DIGEST STALL UNRESOLVED** — Only 3/103 eligible users received digests in 24h
  - **OPEN PRS:** #190, #191 (opoerator-hub), #151 (dropanywhere-app) — ALL OPEN, NO MERGES
  - **DROPPer-Code QUEUE: EMPTY** — 0 tasks pending/approved/in-progress
  - **NO ACTIVE WORK ON FIX** — Escalation filed ops/escalations.md
  - **ROOT CAUSE:** Scheduler does not recover after Hub redeploy (#191)
- ⚠️ **LAUNCH CHECKLIST ALL BLOCKED** — L1-L10 cannot be tested until digest works

**ESCALATION FILED (ops/escalations.md):**
Digest stall 72+ hours unresolved. PRs open but unmerged, no Dropper-Code tasks active. Manual intervention or emergency task assignment required immediately.

### Decision 2: Fix the Three Critical Bugs

| Bug | Impact | Fix Estimate |
|-----|--------|--------------|
| `<thinking>` tags in emails | User-facing embarrassment | 1h |
| Dashboard drop ingestion broken | Core flow dead | 2–4h |
| Vault item editing broken | Data integrity | 2–4h |

**Sequence:** `<thinking>` first (smallest, highest embarrassment), then ingestion (core flow), then editing (data integrity).

### Decision 3: Verify Email Delivery Chain

- [ ] SPF/DKIM/DMARC green
- [ ] Unsubscribe → opted_out=true → permanent
- [ ] Reply capture working
- [ ] `<thinking>` fix verified in production email

---

## Phase 2: STABILIZE (March 16–19) — 4 Days

### Launch-Ready Checklist (Updated Mar 17 10:31 UTC)

| # | Item | Target Date | Status | GitHub PR/Issue |
|---|------|-------------|--------|--------------------|
| L1 | Mobile Safari QA — full flow | Mar 16 | 🔴 BLOCKED | Cannot test with digest stall |
| L2 | Sentry/error tracking | Mar 17 | 🔴 BLOCKED | Cannot test with digest stall |
| L3 | Unsubscribe verification | Mar 16 | 🔴 BLOCKED | Cannot test with digest stall |
| L4 | Rate limiting on /api/ingest | Mar 17 | 🔴 BLOCKED | Cannot test with digest stall |
| L5 | Hub fallback chain (OpenRouter) | Mar 18 | 🔴 BLOCKED | Cannot test with digest stall |
| L6 | New user onboarding QA | Mar 18 | 🔴 BLOCKED | Cannot test with digest stall |
| L7 | Stripe failed charge investigation | Mar 16 | 🔴 BLOCKED | Cannot test with digest stall |
| L8 | `<thinking>` fix verified in prod | Mar 16 | ✅ DONE | PR #199 merged |
| L9 | Tools tab (P1-10 remaining) | Mar 19 | 🔴 BLOCKED | Cannot test with digest stall |
| L10 | Compass settings verified | Mar 16 | 🔴 BLOCKED | Cannot test with digest stall |

**🚨 SINGLE POINT OF FAILURE: DIGEST STALL**
- 3 open PRs attempting fix: #151 (app), #190, #191 (hub) — ALL UNMERGED
- Dropper-Code queue: EMPTY (0 tasks pending/approved/in-progress)
- **ESCALATION FILED: Manual intervention required**

### Snapback Validation (Mar 16–22)

- Joey drops naturally all week
- Email prompts fire Tue/Thu/Sat
- Sunday March 22: Weekly Catch arrives
- **Decision point March 22:** Mirror → include in launch. Portrait → daily digest only.

---

## Phase 3: PREPARE (March 20–23)

### Soft Launch: 10–15 Hand-Selected Users

| Tier | Who | Count |
|------|-----|-------|
| Inner Circle | Joey, Brooke, Danny | 3 |
| Active DA Users | 5+ drops AND 1+ digest opened in 7d | 5–8 |
| BHA Converts | Explicitly opted in | 3–5 |

### Content Pipeline (Pre-Produce Before Mar 24)

| Piece | Format | Time |
|-------|--------|------|
| "AI that writes me a letter every morning" | 60s Reel | 1h |
| "Drop it. Forget it. Wake up lighter." | Carousel | 30m |
| "My product made me write music again" | Story/Reel | 1h |
| "What if your AI actually knew you?" | Talking head | 1h |
| "The whole product is email" | LinkedIn text | 20m |

---

## Phase 4: LAUNCH (March 24–26)

### March 24 — Soft Launch
- 7am: Systems green check
- 8am: Personal launch emails to 10–15 users
- 9am: First content piece
- 6pm: Error/delivery monitoring
- 9pm: Joey's personal drop (becomes Snapback material)

### March 25 — First Digest Morning (Moment of Truth)
- All digests sent, no `<thinking>` tags, actions clickable, replies captured
- Joey replies personally to anyone who responds

### March 26 — Public Launch (Only if Mar 24–25 clean)

---

## 5 Decisions Only Joey Can Make

1. **Poe Credits** — Buy now or let it die? (Deadline: TODAY)
2. **Soft Launch List** — Who are your 10–15? (Deadline: Mar 20)
3. **Snapback in Launch** — Mirror or portrait? (Deadline: Mar 22)
4. **Naming** — "The Weekly Catch" for feature, "DropAnywhere" for product (Deadline: Mar 26)
5. **Public Launch: Go or Push?** — Did soft launch users engage? (Deadline: Mar 25 evening)

---

## What NOT to Touch Until After Launch

❌ Dropper Fleet, Knowledge OS, Desktop/Mobile split, Voice capture, NotebookLM meditation, Calendar view, Community drops, Poe bot archive, OpenClaw refactoring, New Gumroad products

**The filter:**
> *"Does this fix a bug that blocks launch, or does this make me feel productive while avoiding the scary thing (shipping to real humans)?"*

---

## Revenue Path (90 Days)

**Month 1:** DA Pro $9/mo (5–10 converts = $45–90/mo) + Mitch advisory pilot ($500–1K)
**Month 2–3:** Advisory Mode $49/mo (3–5 pilots) + Gumroad FA template ($197) + Snapback+ $19/mo

**Conservative 90-day MRR:** $300–600/mo
**Stretch:** $700–1,200/mo

---

*Ten days. Three bugs. One fallback chain. One Sunday Catch. Fifteen personal emails.*
*Drop everything else. Catch it Sunday.*
