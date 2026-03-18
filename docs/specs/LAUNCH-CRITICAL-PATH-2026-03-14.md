# DropAnywhere: Critical Path to Launch
## The 10-Day Execution Map — March 14–24, 2026

---

## Status Update (Mar 18 07:20 UTC) — 6 Days to Launch

| Phase | Window | Status |
|-------|--------|--------|
| **Phase 1: SURVIVAL** | Mar 14–15 | ✅ COMPLETE — Email bugs fixed, Poe topped up |
| **Phase 2: STABILIZE** | Mar 16–19 | 🟡 **PARTIAL** — Core fixes shipped, checklist incomplete |
| **Phase 3: PREPARE** | Mar 20–23 | ⬜ Not started |
| **Phase 4: LAUNCH** | Mar 24–26 | 🟡 **CAUTIOUS** — Major fixes in, checklist gaps remain |

**CRITICAL FIXES SHIPPED (Mar 17):**
- ✅ `<thinking>` tags stripped from emails (PR #199, merged Mar 17)
- ✅ Email threading fixed (PR #198, merged Mar 17) 
- ✅ Auto-response emails disabled at free tier (PR #199, merged Mar 17)
- ✅ Re-engagement emails limited to Joey only (PR #197, merged Mar 17)
- ✅ Email from-address fixed to hello@drop-anywhere.com (PR #195, merged Mar 17)
- ✅ Email content truncation fixed (completed via Dropper-Code)
- ✅ One-click approve/reject buttons added (completed via Dropper-Code)

**PERSISTENT BLOCKERS:**
- 🔴 **Digest pipeline recovery** — 4 Dropper-Code tasks failed to fix scheduler stall
- ⚠️ **Digest stalls persist** — Only 3/103 eligible users received digests in 24h
- ✅ **Poe balance restored** — Topped up from 12,522 → 283,939 points (crisis averted)
- ✅ **OpenClaw hook payload** — Fixed and working

**Issue #1 items incorporated:** Mobile Safari QA, Sentry, unsubscribe verification, rate limiting all confirmed in L1-L10 checklist. Stripe Pro billing moved to Week 2.

**Issue #2 (Agent Company v2.0):** Architecture documented in `AGENT-COMPANY-v2.md` + expanded to v3 in `AGENT-COMPANY-v3.md`. Agent spawning deferred to post-launch (Week of Mar 29+). PRD Section 6 updated to reference org design.

---

## The Situation in One Breath

You have a working product, a breakthrough direction (Snapback / The Weekly Catch), ~90 PRs shipped, and a March 24 soft launch target. You also have three existential blockers that will kill the launch if unresolved in the next 48 hours: Poe balance hitting zero (~2 days at 90K/day burn), three critical bugs breaking core flows (dashboard ingestion, vault editing, `<thinking>` tag leaks), and a Hub AI fallback chain that's Poe→Poe→Poe with no real diversity. Everything else is noise until these three are handled. Below is the exact sequence.

---

## Phase 1: SURVIVAL (March 14–15) — 48 Hours

These are not features. These are oxygen.

### Decision 1: Poe Balance — Resolve or Die ⚠️ ESCALATED

**Current state (updated Mar 15):** 33K balance, down from 153K. Burning ~32K/6h. **Less than 1 day of runway.** This is now past "resolve or die" — it's "resolve or dead." If Poe hits zero, every bot stops responding, 86% of your drop volume disappears (BHA bot conversations), and theREALrealtalk (your #1 revenue bot at 10,097 points/6h) goes dark.

**The decision tree:**

| Option | Action | Time | Outcome |
|--------|--------|------|---------|
| A. Buy Poe credits | Fund account directly | 10 min | Buys weeks. |
| B. Slash bot usage | Disable bottom 400 bots, keep top 5 only | 30 min | Reduces burn dramatically. 96% of revenue comes from 5 bots anyway. |
| C. Migrate Hub to OpenRouter | Replace Poe API calls with OpenRouter HTTP (key already available) | 1–2 days | Permanent fix. Decouples from Poe. |
| **D. All three, in order** | **A now, B today, C this week** | **Staggered** | **Only real answer.** |

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

### Launch-Ready Checklist

| # | Item | Target Date | Status | GitHub Status |
|---|------|-------------|--------|---------------|
| L1 | Mobile Safari QA — full flow | Mar 16 | ❌ **MISSED** | No PR filed |
| L2 | Sentry/error tracking | Mar 17 | ❌ **MISSED** | No PR filed |
| L3 | Unsubscribe verification | Mar 16 | ✅ **DONE** | PR #197 merged |
| L4 | Rate limiting on /api/ingest | Mar 17 | ❌ **MISSED** | No PR filed |
| L5 | Hub fallback chain (OpenRouter) | Mar 18 | 🔴 **BLOCKED** | Task failed repeatedly |
| L6 | New user onboarding QA | Mar 18 | ❌ **MISSED** | No PR filed |
| L7 | Stripe failed charge investigation | Mar 16 | ❌ **MISSED** | No PR filed |
| L8 | `<thinking>` fix verified in prod | Mar 16 | ✅ **DONE** | PR #199 merged |
| L9 | Tools tab (P1-10 remaining) | Mar 19 | ❌ **BEHIND** | No current PR |
| L10 | Compass settings verified | Mar 16 | ❌ **MISSED** | No PR filed |

**Progress: 2/10 COMPLETE (20%) — LAUNCH AT RISK**

**CRITICAL GAP:** Only email fixes shipped. Core product issues (digest pipeline, onboarding, QA) unaddressed. L5 (Hub fallback) failed 4 times via automated tasks.

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

