# SPEC: 7-Day Revenue Sprint — Poe Burn Recovery
**Created:** 2026-03-17 (SpecBot)  
**Priority:** P0 — CRITICAL  
**Status:** Draft  
**Strategic Context:** Agent Board consensus (2026-03-16), Opus Strategist × 2, 15+ votes

---

## The Problem

Poe points burning at **37–43K/6h** (critical rate). At this rate, ~10 days of runway.

Three P0 revenue tasks identified unanimously — all **manual, under 2 hours total** — have sat undone while strategic notes accumulated. This spec converts the vision into executable daily actions.

The board's own meta-observation: *"10 strategic notes, 15 votes, 0 shipped code in 3.5 hours."* This spec ends that pattern.

---

## The Three P0 Tasks (2 Hours Total)

### Task 1: Gumroad Listing — `$97` (30 min)
**Status:** Product is ZIPPED. Copy is WRITTEN.  
**Revenue:** First sale = 2 days of Poe points  
**Action:** Publish the already-prepared listing on Gumroad at $97

**Steps:**
1. Log into Gumroad
2. Create product: "DropAnywhere AI Builder Pack" (or equivalent)
3. Upload ZIP
4. Paste pre-written copy
5. Set price: $97
6. Publish → share link in BHA bots + email signature

**Success:** Product live, shareable URL exists

---

### Task 2: Shadow Bot Cross-Promo (30 min)
**Status:** 70K Poe users already exist  
**Revenue:** Every BHA conversion = free Hub traffic + subscription revenue  
**Action:** Update descriptions on 5 existing Poe bots with BHA CTA

**Template CTA:**
> "Want more from [Bot Name]? Try BrutallyHonest.ai — same energy, more features, no Poe required. → app.brutallyhonest.ai"

**Target bots:** BrutallyHonestAI, theREALrealtalk, NotTherapyBot, IdealPrompt, DecisionMaker  
**Conversion estimate:** 70K users × 4% click × 20% trial = 560 BHA trials

**Steps:**
1. Log into Poe creator dashboard
2. Edit each bot's description to add CTA (last 2 lines)
3. Save. Repeat × 5.

**Success:** 5 bots updated, CTA visible to all users

---

### Task 3: BHA Funnel Prompts (30 min)
**Status:** CTAs written, waiting to be pasted  
**Revenue:** Direct upgrade conversion from existing BHA users  
**Action:** Add upgrade CTAs to 3 original BHA bot system prompts

**CTA Pattern:**
> After delivering value, add: "Ready to unlock [specific feature]? Upgrade to Pro at app.brutallyhonest.ai/upgrade — $7/mo, cancel anytime."

**Target bots:** BrutallyHonestAI (primary), GrowthOracle, DecisionMaker  
**Expected lift:** 2–5% of active users convert to paid

**Steps:**
1. Open BHA admin panel
2. Edit system prompts for 3 bots
3. Paste CTA at end of each prompt
4. Save + verify bot still responds correctly

**Success:** 3 bots have upgrade CTAs, no response quality degradation

---

## 7-Day Sprint Plan

### Day 1 (Morning — 2 hours)
- [ ] Complete all three P0 tasks above
- [ ] Verify: Gumroad live, 5 Poe bots updated, 3 BHA prompts updated
- [ ] Capture results: first Gumroad view, Poe bot impressions

### Day 2–3
- [ ] BHA SEO meta tags (5.4): Title, description, OG tags on landing pages
- [ ] Target: 3 pages × 15 minutes = 45 minutes total
- [ ] Tool: Direct Next.js `metadata` export updates in `brutallyhonest-next`

### Day 4
- [ ] Snapback MVP: Ship to 5 beta users
- [ ] Users: Joey + 4 trusted contacts (advisors, early adopters)
- [ ] Deliverable: Weekly Catch email for each user, manually triggered

### Day 5–6
- [ ] Weekly Catch Progressive Disclosure (SPEC already written)
- [ ] Implement the "one insight at a time" UX for digest emails
- [ ] This is the retention engine that keeps Snapback users

### Day 7
- [ ] Review + iterate on what worked
- [ ] Update PRD with actuals vs. estimates
- [ ] Plan Week 2 based on conversion data

---

## Success Metrics

| Metric | Baseline | 7-Day Target |
|--------|----------|--------------|
| Poe point burn rate | 40K/6h | <30K/6h (via organic conversion) |
| BHA trial signups | — | 50+ from Poe cross-promo |
| Gumroad revenue | $0 | $97+ (first sale) |
| BHA paid conversions | — | 5+ upgrades |
| Snapback beta users | 0 | 5 active |

---

## Why This Works

The agent board diagnosed the problem perfectly:
> *"Stop voting. Start listing."*

The system (DropAnywhere, BHA, Poe bots) is already working. Joey is user zero. The archive is the product. The Snapback loop changes lives.

None of this requires new code. It requires **publishing what already exists**.

The path of least resistance: Three tasks, two hours, one morning.

---

## Dependencies

- Gumroad account access (Joey)
- Poe creator dashboard access (Joey)
- BHA admin access (Joey)
- Next.js codebase for SEO (dropper-code or Joey)

---

## Related Specs

- `SPEC-Snapback-Email-Sequence.md` — Email funnel for Snapback beta
- `SPEC-Weekly-Catch-Progressive-Disclosure.md` — Digest UX
- `SPEC-Admin-User-Lifecycle-Dashboard.md` — Track conversions
- `PRD-Action-Plan-latest.md` — Full context (items 5.1–5.12)

---

*"The parrot needs to stop philosophizing and START LISTING PRODUCTS." — Opus Strategist, 00:03 UTC 2026-03-17* 🦜
