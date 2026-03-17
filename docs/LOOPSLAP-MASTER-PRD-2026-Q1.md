# LoopSlap LLC — Master Product Roadmap
## Q1 2026 (March 10 → March 31)

**CEO perspective. Source of truth. Not a wishlist — a plan.**  
**Author:** Claw (Chief of Staff) + Joey (CEO/Founder)  
**Last Updated:** 2026-03-10  
**Review cadence:** Weekly (Sunday evening)

---

## The Honest Assessment

Let me be direct. Here's where we are:

**Revenue: $21/month.** Three BHA subscribers. That's it. Everything else — the 65 DA users, 211 BHA users, 467 Poe bots, 70K+ bot users, 29 PRs in 6 days — is infrastructure without income. We've built an incredible engine. It's idling.

**What's working:**
- BHA gets **531 organic web visitors/week** from Google. Position 2-4 for "honest ai" queries. 6-minute average sessions. People find us, they stay, they engage. This is real.
- Poe bots generate **14K+ points every 6 hours** of organic traffic. theREALrealtalk has genuine PMF with Gen Z users sharing their deepest problems.
- DA has **65 users** capturing **668 drops**, receiving daily digests. Retention via digest is the stickiest part of the ecosystem.
- Infrastructure is solid. All 16 APIs green. Dropper-Code ready to ship. Orchestrator live.

**What's broken:**
- **Conversion:** 531 BHA web visitors/week → 3 paying users total. That's 0.1% lifetime conversion. Industry standard is 2-5%.
- **Funnel:** 14K+ Poe points/6h of bot usage → only 27 clicks to BHA/week. The bridge from free Poe to paid BHA barely exists.
- **Pricing page:** 50% bounce rate. People check the price and leave.
- **Bot pages:** Near-zero traffic from search. Zero SEO optimization.
- **DA monetization:** None. No pricing, no premium tier. Free forever currently.

**The diagnosis:** We have a **distribution machine** (Poe + Google organic) feeding into a **broken funnel** (no CTAs, bad pricing page, no conversion optimization). Fix the funnel before building more features.

---

## The Strategy: Revenue Before Features

### North Star Metric: **Monthly Recurring Revenue (MRR)**
- Current: $21
- March 31 target: **$200 MRR** (~30 subscribers)
- How: Fix conversion, activate distribution, optimize pricing

### Secondary Metrics:
- BHA free→paid conversion rate (target: 2%)
- Poe→BHA click-through rate (target: 5% of sessions)
- DA daily active users (target: 25)
- Digest open/engagement rate (target: 40%)

---

## Phase 1: ACTIVATE THE FUNNEL (March 10-14)
*Everything here is about connecting existing traffic to existing product.*

### 1.1 Poe Funnel Activation — MANUAL, JOEY (Today)
**Priority: #1. Do this before anything else.**

The Poe bots have thousands of daily users. Zero of them know BHA exists.

- [ ] **Paste funnel CTA into top 5 original bot system prompts** on poe.com
  - theREALrealtalk, BrutallyHonestAI, IdealPrompt, NotTherapyBot, EpiphanyAI
  - Funnel text is ready: `joey-backup/specs/poe-orchestrator/funnel-prompts-draft.md`
  - 10 minutes. Biggest single ROI action available.
- [ ] **Update bot descriptions with v2 cross-links**
  - "✨ Try the upgraded version: poe.com/theREALrealtalk-v2"
  - Must be manual (Poe API 500s on PATCH to prompt bots)
  - 10 minutes.

**Expected impact:** If even 1% of Poe daily users click through → 5-10 new BHA visitors/day → at 2% conversion = 1 new subscriber every few days.

### 1.2 BHA Pricing Page Fix — DROPPER-CODE (This week)
**The data says: 50% bounce on `/pricing`. People look and leave.**

- [ ] **A/B test pricing presentation** — current tiers may be confusing or too expensive for the Gen Z audience
  - Pay-as-you-go ($4.99 → 25 credits) vs Pro ($7/mo → 75/mo) vs Founders ($47 → 500)
  - The Gen Z users on Poe are HIGH SCHOOL STUDENTS. $7/month is real money to them.
  - Consider: $2.99 starter tier, or first 10 credits free
- [ ] **Add social proof to pricing page** — testimonial snippets, "X conversations this week", user count
- [ ] **Add comparison to alternatives** — "vs therapy ($200/session), vs life coach ($150/hour)"
- [ ] **Reduce friction** — can users try one free conversation before paying?

**Task for Dropper-Code:** File after Joey approves pricing strategy direction.

### 1.3 BHA Homepage Conversion Optimization — DROPPER-CODE (This week)
**89% of page views are the homepage. It IS the product page.**

- [ ] **Optimize meta title/description for "honest ai"** — we're position 3.6 for a query with 203 impressions/week. Better meta = more clicks = free growth.
  - Current: generic
  - Target: "BrutallyHonest.ai — The Most Honest AI Chatbot | No Filter, Real Advice"
- [ ] **Add clear CTA above the fold** — "Start a conversation" button, not just "explore bots"
- [ ] **Show social proof** — "531 people used us this week" / "Join 14,000+ conversations"
- [ ] **Homepage → Store flow** — `/store` gets only 25 views despite 758 homepage views. That's a 3.3% click-through. Add prominent "Browse Personas" CTA.

### 1.4 SEO Quick Wins — DROPPER-CODE (This week)
**Google organic is 63% of BHA traffic. Every SEO improvement = free money.**

- [ ] **Optimize bot pages** — `/bots/brutallyhonestai` has 6 search impressions, 0 clicks. These pages need:
  - Unique meta titles with persona name + "honest ai chatbot"
  - Structured data (FAQ schema, Product schema)
  - 200+ words of unique content per bot page
- [ ] **Target question queries** — "what is the most honest ai" has 37 impressions. Create a FAQ or blog post answering this directly.
- [ ] **Internal linking** — homepage → bot pages → pricing. Currently siloed.

---

## Phase 2: OPTIMIZE RETENTION (March 14-21)
*Keep the users we're getting.*

### 2.1 DA Digest Quality — DROPPER-CODE
- [ ] **Intelligence Map: exclude completed items** (task approved, in progress)
- [ ] **Digest analyzer improvements** — the digest IS the product for DA. Every digest should feel like a personal letter, not a summary dump.
- [ ] **Archive completed vault items** — clean vault = happier users

### 2.2 Desktop vs Mobile Split — Phase 1 — DROPPER-CODE
- [ ] **PRD approved:** `specs/PRD-Desktop-Mobile-Split-2026-03-10.md`
- [ ] **"Capture Instrument" (mobile) vs "Reflection Studio" (desktop)** — hide complexity on mobile, surface depth on desktop
- [ ] `useIsMobile()` hook + conditional wrappers. No new components. Pure hide/show.
- [ ] **Status:** ON HOLD pending Joey's PRD review → then approve Dropper-Code task

### 2.3 Droppings — Contextual Auto-Tagging — DROPPER-CODE
- [ ] Auto-tag drops with source, device type, timestamp
- [ ] Display tags in vault and digest
- [ ] Foundation for future: location context, app context, mood detection

### 2.4 Chrome App Enhancement — DROPPER-CODE
- [ ] Right-click "Drop to DropAnywhere"
- [ ] Keyboard shortcut (Ctrl+Shift+D)
- [ ] New digest badge notification

---

## Phase 3: EXPAND DISTRIBUTION (March 21-31)
*Only after funnel is fixed and retention is solid.*

### 3.1 Shadow Bot Full Cutover
- [ ] Monitor v2 bot traffic for 1 week after funnel activation
- [ ] Contact Poe support about prompt→API conversion for original handles
- [ ] If Poe can't convert: accept hybrid model (originals for discovery, shadows for intelligence)
- [ ] Create remaining shadow bots (EpiphanyAI-v2, etc.)

### 3.2 DA Growth
- [ ] **Add GA tag to DA** ✅ (done — G-D6ZQYFT1SQ, deployed today)
- [ ] **DA landing page SEO** — optimize for "thought capture app", "daily digest ai", "second brain"
- [ ] **Referral mechanism** — "Share your digest" → invite friends
- [ ] **DA pricing tier** — define what free vs paid looks like (vault limits? digest frequency? AI depth?)

### 3.3 Content Marketing
- [ ] **Blog/FAQ targeting search queries:** "what is the most honest ai", "honest ai chatbot", "ai life coach"
- [ ] **Case studies from real BHA user patterns** (anonymized) — Gen Z college admissions, relationship advice, career decisions
- [ ] **"Letter From My Future Self"** format content — Joey's signature style

### 3.4 Snap Back Protocol (Product Innovation)
- [ ] Design the "Snap Back" feature — detect pendulum capture in drops → surface recovery prompt
- [ ] theREALrealtalk guided exercise: "You sound captured. Let's snap back."
- [ ] This is a differentiator nobody else has

---

## Phase 4: SCALE (April+)
*Only if Phases 1-3 deliver results.*

- NotebookLM personalized meditation integration
- DA premium tier launch
- PWA with offline drops, push notifications, haptic feedback
- Multi-persona routing intelligence (auto-select best bot for user's issue)
- Productivity metrics dashboard (desktop Reflection Studio)
- Agency in a Box / Genesis Orchestrator ($97-$497 products)

---

## What We're NOT Doing (And Why)

| Idea | Why Not Now |
|------|------------|
| Zapier/integrations | No users asking for it. Premature. |
| Telegram/WhatsApp channels for DA | Channel expansion before conversion = waste. |
| New Poe bots | 467 is enough. Optimize the 5 that matter. |
| Mobile app (native) | PWA is sufficient. React Native is a distraction. |
| Multi-language support | Only if non-English users are a meaningful %. |
| Vault chat / AI conversations | Feature creep. Digest is the product, not a chatbot. |
| Fundraising prep | Revenue first. Investors come to traction. |
| New design system | Brooke theme works. Don't redesign what isn't broken. |

---

## Operating Rhythm

### Daily:
- Heartbeat checks: APIs, Dropper-Code, Hub, GA, Poe balance
- Auto-approve safe tasks (bug fixes, backend, security)
- Escalate customer-facing changes

### Weekly (Sunday evening):
- Review this PRD against metrics
- GA + Search Console report
- Update MRR tracking
- Adjust priorities if data says something different

### Bi-weekly:
- Full hydration sweep
- Memory maintenance
- Backup to joey-backup

---

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-10 | Revenue before features | $21 MRR with 531 weekly visitors = conversion problem, not traffic problem |
| 2026-03-10 | Poe funnel activation = #1 priority | 14K+ points/6h organic, 0 CTAs to BHA. Lowest effort, highest ROI. |
| 2026-03-10 | Gen Z pricing sensitivity | Primary BHA users are high school students. $7/mo may be too high. |
| 2026-03-10 | SEO is the growth engine | 63% of BHA traffic is Google organic. Invest in SEO before paid acquisition. |
| 2026-03-10 | Desktop/Mobile split on hold | Important but Phase 2. Revenue > UX polish right now. |
| 2026-03-10 | No new Poe bots | 467 bots, 5 generate 96% of revenue. Focus on the 5. |

---

## Success Criteria — March 31

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| MRR | $21 | $200 | 🔴 |
| BHA paying users | 3 | 30 | 🔴 |
| BHA free→paid conversion | 0.1% | 2% | 🔴 |
| Poe→BHA weekly referrals | 27 | 150 | 🔴 |
| BHA weekly visitors | 531 | 800 | 🟡 |
| DA daily active users | 19 | 25 | 🟡 |
| DA total users | 65 | 100 | 🟡 |
| Digest engagement rate | unknown | 40% | ⚪ |
| All APIs green | 16/16 | 16/16 | 🟢 |
| Dropper-Code tasks/week | 3 | 5 | 🟡 |

---

## The One-Liner

**We have a distribution machine (Poe + Google) and a product people love (BHA + DA). The only thing missing is the bridge. Build the bridge. Revenue follows.**

---

*This document is the source of truth. Every task, every PR, every decision should trace back to a line item here. If it's not in this doc, it's not a priority.*

*Updated by Claw. Approved by Joey. Reviewed weekly.*

