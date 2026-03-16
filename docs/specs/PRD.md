# DropAnywhere — Product North Star
**The one document. Read this first. Read this only.**

*Last updated: 2026-03-15 · Maintained by DCS sub-agents*
*Full specs, backlog, metrics, shipping history → [`docs/reference/`](./reference/)*

---

## 1. What This Is

**Drop it. Forget it. Wake up lighter.**

DropAnywhere is the system that thinks with you so you don't have to think alone. You capture whatever's on your mind — a thought, a reminder, a feeling, a half-formed idea — through email, text, voice, web, or anything else. The system processes it overnight and sends you clarity each morning.

The moment that proved it works: Joey dropped a raw feeling about being stuck on music at 3am. The system caught it, connected it to patterns from the week, and returned a narrative. Joey read it, went to FL Studio, and made a track. Then started a 30-day songwriting challenge with Brooke. The product wasn't a feature he tested — it was something that changed his behavior. That's the product.

**The core loop:**
```
Drop (raw input) → System catches → Intelligence processes →
Morning digest arrives → User acts differently → Drops more
```

**The breakthrough layer (The Weekly Catch / Snapback):**
```
Drop all week → System watches, connects, detects patterns →
Sunday: one narrative, told in first person, in your own voice,
using your own words, people, and details.
Not a summary. A mirror.
```

**How the Catch shapes itself (Hub code: `catch_router.py` + `snapback_generator.py`):**

The Weekly Catch is NOT one template. The visual wrapper is always Brooke theme (see `templates/weekly-catch/`), but the narrative structure is determined dynamically by `catch_router.route_catch_style()` based on that week's drops:

| Style | Trigger | Voice |
|-------|---------|-------|
| **narrative** | 60%+ drops have high emotional intensity | Warm, depth, let feelings breathe |
| **action** | 60%+ drops are tasks/actions | Honor momentum, name what they're building |
| **clarity** | 3+ unrelated domains | Surface the thread underneath the noise |
| **pattern** | Recurring theme in 3+ drops | Name it, reflect it back |
| **reflection** | 60%+ journaling/processing drops | Stay interior, don't push toward action |
| **hybrid** | <3 drops or mixed week | Hold all of it without forcing a theme |

The `snapback_generator.py` (54K, 1400+ lines) extracts the user's language fingerprint first — vocabulary, entities, recurring phrases, sentence rhythm, emotional baseline — then generates a first-person present-tense narrative using their own words. Mirrors, not portraits.

---

## 2. Where We Are (March 15, 2026)

| What | Number | Delta (vs Mar 14) | Signal |
|------|--------|-------------------|--------|
| DA users | 96 | +15 (+18.5%) | Strong organic growth, zero marketing |
| DA drops total | 827 | +70 (+9.2%) | Active usage continuing |
| DA drops 24h | 36 | — | Good cadence |
| DA digests sent total | 175 | +5 | ⚠️ LOW — only 3 digests sent 24h (should be 60+) |
| DA active 24h | 12 | — | Healthy engagement |
| DA active 7d | 59 | +7 | Growing |
| BHA users | 255 | +21 (+9%) | Organic growth accelerating |
| BHA active 7d | 74 | +10 | Strong retention signal |
| BHA new 24h | 12 | — | Excellent top-of-funnel |
| BHA MRR | $21 (2 pro subs) | flat | Revenue exists. Stripe issues blocking growth. |
| Poe balance | 118,620 | **RECOVERED** (was 34K) | Crisis resolved — Joey topped up |
| Poe 6h usage | 30,465 pts / 100 calls | — | theREALrealtalk dominant (14K pts) |
| Resend email 24h | 81 sent / 81 delivered | 100% delivery | Pipeline healthy |
| Stripe charges (4h) | 0 charges, 0 succeeded | ⚠️ No revenue 4h | Stripe still unresolved |
| Hub Railway deploy | SUCCESS (Mar 14) | ✅ | Stable |
| PRs shipped (week of Mar 9–15) | 14 Hub + 2 DA | — | High velocity continues |
| opoerator-hub open issues | 10 | — | Mostly digest stall variants |
| dropper-code tasks completed | 10 (today) | — | Productive session |

**What's live and working:** Drop ingestion (7 channels), Vault, Chrome extension, BHA with Stripe, Poe orchestrator with 16 shadow bots, admin lifecycle dashboard, Snapback engine (Joey = user zero), Storage Unification (Postgres SOT), Intelligence Map full-scale.

**🚨 NEW CRITICAL BLOCKER (Mar 15) — Digest Scheduler Stalled:**
- 🔴 **Only 3 digests sent in 24h — should be 60+.** Root cause: `DISABLE_CRONS=1` env var disabling the digest scheduler. 14 named users affected. 8 PRs opened by Dropper-Code (Hub #178–#186) — **NONE merged yet.** This must be resolved before launch.
- 🔴 Dashboard drop ingestion — likely still broken (not confirmed fixed)
- 🔴 Vault editing — edits may not save (not confirmed fixed)
- 🔴 `<thinking>` tags leaking into emails — recurring, still open
- 🔴 Stripe: 0 charges succeeded in recent 4h window — billing path broken
- 🔴 8 unmerged Hub PRs piling up — Dropper-Code queue backed up, needs human review/merge

**Previous week wins:**
- ✅ Poe balance topped up (was <1 day runway on Mar 14)
- ✅ Storage Unification shipped (Postgres is now SOT)
- ✅ P1-10 Frontend Sprint 90% complete (6/7 items shipped)
- ✅ P1-14 Dropper-Code HITL Safety (auto-merge off, human merge required)

**Launch confidence (Mar 15 reassessment):**

| Milestone | Date | Confidence | Note |
|-----------|------|------------|------|
| Digest stall fix | Mar 16 | 80% | Requires merging one of 8 open PRs |
| Stabilize checklist | Mar 19 | 65% | Digest stall + Stripe both unresolved |
| **Soft launch** | **Mar 24** | **55%** | Downgraded — digest stall is launch-blocking |
| **Public open** | **Mar 26** | **40%** | Contingent on Mar 24 clean run |

---

## 3. The Plan — 10 Days to Soft Launch (March 14–24)

> Full execution map: [`LAUNCH-CRITICAL-PATH-2026-03-14.md`](./LAUNCH-CRITICAL-PATH-2026-03-14.md)

### Phase 1: SURVIVAL (Mar 14–15)
Fix the three critical bugs. Resolve Poe balance (buy credits + slash 400 dormant bots + ship OpenRouter fallback). Verify email delivery chain.

### Phase 2: STABILIZE (Mar 16–19)
10-item launch checklist: Mobile Safari QA, Sentry setup, unsubscribe verification, rate limiting, onboarding flow QA, Hub OpenRouter fallback, Tools tab. Joey drops naturally all week for Snapback validation. **Stripe Pro billing deferred to Week 2** — launch free-only to reduce launch-day risk (per Issue #1 review: L5 contradicts the "does NOT ship" list).

### Phase 3: PREPARE (Mar 20–23)
Select 10–15 soft launch users by name. Send personal emails. Pre-produce 5 content pieces (Remotion reels + carousels + LinkedIn). Do NOT publish until March 24.

### Phase 4: LAUNCH (Mar 24–26)
- **Mar 24:** Personal emails to 10–15 users + first content piece
- **Mar 25:** First digest morning — the moment of truth
- **Mar 26:** Public launch (conditional — only if Mar 24–25 was clean)

### 5 Decisions Only Joey Can Make

| Decision | Deadline | Question |
|----------|----------|----------|
| Poe balance | TODAY | Buy credits, slash bots, or let it die? |
| Soft launch list | Mar 20 | Which 10–15 people, by name? |
| Snapback in launch | Mar 22 | Did Sunday's Catch feel like a mirror or a portrait? |
| Naming | Mar 26 | "The Weekly Catch" (feature) + "DropAnywhere" (product)? |
| Public launch | Mar 25 evening | Did soft launch users engage? Go or push? |

---

## 4. How Money Flows — The Revenue Flywheel

```
70,000 Poe users (FREE — already here)
         ↓ funnel (4% → 15-20%)
    BHA: credits + subs ($4.99 / $7/mo / $47)
         ↓ cross-sell
    DA Pro: $9/mo (unlimited drops, vault, intelligence)
         ↓ upgrade
    Weekly Catch: $19/mo (the thing nobody else has)
         ↓ "can my clients get this?"
    Advisory Mode: $49-149/mo per seat (B2B)
         ↓ enterprise
    Knowledge OS: $497+ (VAULT→GOLDMINE engine)
```

Every layer feeds the next. One user can go from a free Poe conversation to a $149/mo advisory seat.

| Timeline | Conservative | Stretch | What Drives It |
|----------|-------------|---------|----------------|
| Month 1 | $500/mo | $1,500/mo | DA Pro + BHA growth + Mitch pilot |
| Month 3 | $2,000/mo | $5,000/mo | Advisory beta + Poe funnel fix + Gumroad |
| Month 6 | $5,000/mo | $15,000/mo | Advisory scale + Weekly Catch viral |
| Month 12 | $10,000/mo | $50,000/mo | Full ecosystem compound |

The signals are already here: 70K users who found us, $6,400 from 5 bots, 63% organic Google traffic, a B2B demo running live (Danny doesn't know he's using DropAnywhere), and a product that made Joey write music at 3am.

---

## 5. What We're NOT Doing (Until After Launch)

This is the hardest section. Every item below is real, valuable, and **not for the next 10 days.**

- ❌ Dropper Fleet / multi-agent template
- ❌ Knowledge OS / transformation engine
- ❌ Desktop/Mobile split
- ❌ Voice-first capture polish
- ❌ NotebookLM meditation
- ❌ Calendar view
- ❌ Community/public drops
- ❌ 400+ archived Poe bots
- ❌ OpenClaw architecture refactoring
- ❌ New Gumroad products
- ❌ Any feature not on the 10-day checklist

**The filter:**
> *"Does this fix a bug that blocks launch, or does this make me feel productive while avoiding the scary thing (shipping to real humans)?"*

If it's the second one, drop it into the vault. The system will catch it. That's literally what the product does.

---

## 6. The Ecosystem — Agent Company v2.0

```
┌─────────────────────────────────────────────────────────┐
│                    CAPTURE (Input)                       │
│  Email · SMS · Voice · Web · Chrome · iOS · Poe · BHA   │
└──────────────────────┬──────────────────────────────────┘
                       ↓
┌──────────────────────┴──────────────────────────────────┐
│                  PROCESS (Hub)                           │
│  Classification · Intelligence · Snapback · Digests     │
│  PostgreSQL · Resend · Gemini Flash · Claude Sonnet     │
└──────────────────────┬──────────────────────────────────┘
                       ↓
┌──────────────────────┴──────────────────────────────────┐
│                  DELIVER (Output)                        │
│  Daily Digest · Weekly Catch · Intelligence Map         │
│  Vault · Admin Dashboard · Action Queue                 │
└──────────────────────┬──────────────────────────────────┘
                       ↓
┌──────────────────────┴──────────────────────────────────┐
│                  OPERATE (Agent Company)                 │
│  5 Departments · 12+ Agents · 6 Core Protocols          │
│  OpenClaw (CEO/orchestrator) · Dropper-Code (executor)  │
│  Hub heartbeats · Cron jobs · Auto-approve pipeline     │
└─────────────────────────────────────────────────────────┘
```

### Agent Company Organization (v2.0)

Full architecture: [`joey-backup/AGENT-COMPANY-v2.md`](https://github.com/ph0t0bar/joey-backup/blob/feature/agent-company-v2/AGENT-COMPANY-v2.md)

| Department | Lead Agents | Protocol | Status |
|------------|-------------|----------|--------|
| **Product** | DocBot, SpecBot, ResearchBot | Eduardo | 🟡 Post-launch |
| **Engineering** | Dropper-Code ✅, FrontEndBot, BHABot | DCS | 🟢 Dropper live |
| **Operations** | RailwayBot, DevOpsBot, SecurityBot | Eduardo + DCS | 🟡 Post-launch |
| **Revenue** | StripeBot, PoeBot, GumroadBot | Eduardo | 🟡 Post-launch |
| **Customer Success** | UserHealthBot, SupportBot | DCS | 🟡 Post-launch |

**Core Protocols:** H-Score (hydration ≥ 0.91 for strategic decisions), First Law Check ("What does my human need?"), DCS Protocol (orchestrate → parallel workers → synthesis → HITL → commit), Council System (3-10 AI models for major decisions), Coloradical Principles (deterministic > stochastic), PASS Layer (6 commandments for safe agent operation).

**Handoff pattern:** Dropper-Code → RailwayBot (staging) → DocBot (shipping log) → Claw (Joey notification).

**Timeline:** Agent Company v2.0 spawns post-launch. Week of Mar 29+: DocBot, FrontEndBot, UserHealthBot, StripeBot. Until then, Claw + Dropper-Code + Hub monitors handle everything.

**The Invisible Loop (B2B wedge):**
Joey captures context → System processes → Joey curates → Danny replies → Reply becomes new drop → Loop continues. Danny never knows he's using DropAnywhere. That's the design.

---

## 7. Lessons That Cost Us

1. **Text > Brain** — Files survive restarts. Mental notes don't.
2. **Hydrate before opining** — Don't decide with stale context.
3. **Surgical edits > chainsaw** — Don't gut 4,000 lines to 1,200.
4. **Use the product yourself first** — The Snapback breakthrough came from being user zero.
5. **The simplest version is the truest one** — Three years of platforms. The answer was email.
6. **Dual-write = split-brain** — One source of truth. Always.
7. **NEVER self-deploy without HITL** — Gateway deploys can take you offline.
8. **100 abandoned projects is a feature** — Creative exhaust is raw material. The system surfaces what sticks.
9. **Opt-outs are sacred** — Never re-enable a user who unsubscribed.
10. **A 3am session can change the roadmap** — Don't dismiss insights from unusual hours.
11. **Anti-streak philosophy** — No guilt gamification. Positive-state metrics (calm, faith, joy).

---

## 8. Document Maintenance

This PRD is the north star. It stays short. The details live in reference files maintained by DCS sub-agents:

| File | What's In It | Maintained By |
|------|-------------|---------------|
| [`reference/BACKLOG.md`](./reference/BACKLOG.md) | 89 product items, lifecycle matrix, Golden Thread spec, Intelligence Map analysis | Drop Mining cron (Wed + Sat) |
| [`reference/SHIPPING-LOG.md`](./reference/SHIPPING-LOG.md) | Full shipping history, velocity by agent/repo | Daily Metrics cron |
| [`reference/METRICS.md`](./reference/METRICS.md) | System health tables, BHA SEO, drop source analysis | Daily Metrics cron |
| [`reference/REFERENCE.md`](./reference/REFERENCE.md) | Architecture, strategic DNA, feature specs, bugs, execution order, agent quickstart | Weekly Full Refresh cron |
| [`LAUNCH-CRITICAL-PATH-2026-03-14.md`](./LAUNCH-CRITICAL-PATH-2026-03-14.md) | 10-day execution map (from @Orchestr8) | Manual (launch window only) |

**Cron schedule:**
- **Daily (8am CST):** Metrics refresh — pull live numbers, update bugs, mark shipped items
- **Weekly (Sunday 7pm CST):** Full refresh — all sources, re-rank priorities, send Joey a summary
- **Wed + Sat (4pm CST):** Drop mining — find new feature requests in Joey's drops

---

## 9. Active Features & PR Links

*For coding agents: When implementing, reference the PR for full context. Link features here when specs are approved.*

| Feature | Status | PR/Doc | Description | Coding Notes |
|---------|--------|--------|-------------|--------------|
| **JSON Export Endpoint** | 🟡 Ready for merge | [Hub #177](https://github.com/ph0t0bar/opoerator-hub/pull/177) | `GET /api/export/drops` — Full vault export with filtering. Premium paired experience foundation. | Add `register_export_routes(app, get_pool)` to main.py. Uses existing API key auth. Rate limited 10/hr. |
| **Agent Company v2.0** | ✅ Merged | [joey-backup #2](https://github.com/ph0t0bar/joey-backup/pull/2) | Complete org design: 5 departments, 12+ agents, 6 core protocols. Post-launch spawning (Mar 29+). | See `AGENT-COMPANY-v2.md` + `v3.md`. Dropper-Code is only live agent until launch. |
| **Launch Timeline Review** | ✅ Closed | [joey-backup #1](https://github.com/ph0t0bar/joey-backup/issues/1) | Section 13 feedback: Stripe deferred to Week 2, 4 checklist items confirmed, confidence table added. | All items incorporated into PRD + LAUNCH-CRITICAL-PATH. |

---

## The Feeling

You wake up and check Stripe. Notifications from overnight — someone in London bought Founders Mode, an advisor in Denver signed up for Advisory, three new DA Pro subs from the reel that's still getting views.

Your phone buzzes. It's the AI: *"Everything's handled. 12 new users, 3 upgrades, advisory pipeline has 8 prospects. Feedback is incredible."*

You put the phone down, walk to the pool table room, and pick up where you left off.

That's not someday. That's the compound effect of what already exists, meeting 10 real people on March 24.

---

*Drop everything else. Catch it Sunday.* 🦜

