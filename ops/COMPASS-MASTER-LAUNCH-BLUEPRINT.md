# 🧭 THE COMPASS — Complete Pre-Launch Blueprint

**Version:** 2026-03-17 FINAL  
**Status:** Single Source of Truth for March 24 Launch  
**Supersedes:** All prior Compass emails, audit reports, and strategic docs

---

## 1. EXECUTIVE SUMMARY

**The decision is made.** DropAnywhere launches March 24 as an **email-only product** — no dashboard, no login, no app. The agency voted 9-1 in favor (10 departments surveyed, 1 conditional). This isn't a compromise — it's a sharper product.

**Three deliverables:**
1. Intelligence Map Digest Email Template (the entire product)
2. Expanded Onboarding Funnel (13 emails over 21 days)
3. Static Landing Page (waitlist signup only)

**What this saves:** ~103 hours of frontend work, ~$120-140/mo in burn, and the launch itself.

**Launch confidence:** 🟢 85% (up from 65% with full dashboard scope)

---

## 2. THE PRODUCT

### What It Is
An **email-only Intelligence Map**. Users email their thoughts to `drop@drop-anywhere.com`. AI extracts themes, finds connections, surfaces patterns. Users receive a beautiful digest email — their Intelligence Map — each morning.

### How It Works
```
DROP → PROCESS → DELIVER

1. User sends email/text/voice to drop@drop-anywhere.com
2. Hub ingests, classifies, extracts themes + connections
3. AI generates Intelligence Map (themed sections, cross-references, action items)
4. Delivered as gorgeous Brooke-themed email digest (daily or weekly)
```

### Core Promise
**"Drop it. Forget it. Wake up lighter."**

That was always an email promise, not a dashboard promise. The Danny Advisory Package already proved the invisible loop works — "the recipient never knows they're using DropAnywhere."

### What Dies (Phase 2)
- Dashboard UI (all tabs)
- Authentication system (OAuth, sessions)
- Settings page, Vault view, Stream view
- Activity feed, Compass page
- Real-time features, push notifications

### What Must Work Perfectly
1. Email deliverability (inbox, not spam)
2. Intelligence Map quality (themes, connections, patterns)
3. Admission flow (waitlist → welcome → first digest)
4. Stripe billing (trial → payment without friction)
5. Hub webhook → instant processing

---

## 3. ONBOARDING FUNNEL

### Philosophy
Every email does THREE things: **Educate, Entertain, Collect.**  
Every interaction enriches the user's Postgres profile.  
The funnel adapts — behavioral triggers override fixed timing.

### Digest Analyzer Styles (Live in Hub)

| Style | Key | Personality | Best For |
|-------|-----|-------------|----------|
| Clarity Engine | `clarity` | Organized themes, focus report | Scattered thinkers |
| Action Catch | `action` | Prioritized action items | Builders, operators |
| Pattern Mirror | `pattern` | Cross-drop thread detection | Explorers, creatives |
| Deep Mirror | `reflection` | No actions, just meaning | Processors, journalers |
| Adaptive | `adaptive` | System picks best mode | New users (default) |

### The 13-Email Sequence

#### PHASE 1: Welcome + First Drop (Days 0-1)

| # | Email | Trigger | Subject | Purpose | Data Collected |
|---|-------|---------|---------|---------|----------------|
| 1 | Welcome | Instant on admission | "Welcome to DropAnywhere — your mind just got an outbox 🧠" | Educate + First action | `onboarding_step`, `trial_start` |
| 2 | First Drop Nudge | 4h after #1, IF no drop | "Your brain is still holding everything ✋" | Activate | `nudge_count++` |
| 3 | First Drop Confirmation | Instant on first drop | "💧 Your first drop just landed — here's what we found" | Demonstrate value | `first_drop_at`, `drop_count` |

#### PHASE 2: Education + Data Collection (Days 2-7)

| # | Email | Trigger | Subject | Purpose | Data Collected |
|---|-------|---------|---------|---------|----------------|
| 4 | What's on your mind? | Day 2 | "Quick question — what are you trying to figure out?" | Collect context | `focus_domains[]`, `life_domains[]`, `biggest_challenge` |
| 5 | Meet your digest styles | Day 4 | "Not all insights look the same — pick your lens 🔍" | Educate + preference | `preferred_digest_style` |
| 6 | First Intelligence Map | Day 7 (≥3 drops) | "🗺️ Your Intelligence Map is ready" | Core value demo | Engagement, style satisfaction |

#### PHASE 3: Depth + Engagement (Days 8-14)

| # | Email | Trigger | Subject | Purpose | Data Collected |
|---|-------|---------|---------|---------|----------------|
| 7 | Weekly Reflection | Day 8 | "You've dropped {X} thoughts this week — here's the shape of your mind 🧩" | Engage + value | Engagement score |
| 8 | Try a different lens | Day 10 | "Same thoughts, different angle — try {alternate style} 🔄" | Style exploration | Style preference update |
| 9 | Connections forming | Day 12 | "Something interesting is happening in your drops 🔗" | Demonstrate depth | Engagement depth |
| 10 | Premium Teaser | Day 14 | "What if every drop got an instant response? ⚡" | Introduce premium | Premium interest click |

#### PHASE 4: Conversion (Days 15-21)

| # | Email | Trigger | Subject | Purpose | Data Collected |
|---|-------|---------|---------|---------|----------------|
| 11 | Trial so far | Day 15 | "15 days of DropAnywhere — here's your story so far 📊" | Value summary | Summary engagement |
| 12 | Before and after | Day 18 | "Your trial ends in 3 days — here's the before and after" | Loss aversion | Conversion intent |
| 13 | Final Offer | Day 21 | "Last call — your Intelligence Map goes dark tonight 🌑" | Final conversion | Conversion or churn |

### Behavioral Triggers (Always Active)

- **Re-engagement Nudge:** No drop in 72h → thought prompt. Max 1/week, max 3 during trial.
- **Instant Clarity (Premium):** Every drop gets <60s AI response. Reflection, question, connection.
- **Milestone Celebrations:** 5 drops ("map getting interesting"), 10 ("bonus pattern analysis"), 25 ("power dropper"), 50 ("full mind map")

### Postgres Profile Schema

| Field | Type | Source |
|-------|------|--------|
| `email` | string | Signup |
| `name` | string | Email #1 reply |
| `onboarding_step` | int | Auto |
| `first_drop_at` | timestamp | Drop ingestion |
| `drop_count` | int | Aggregated |
| `focus_domains` | string[] | Email #4 CTA |
| `preferred_digest_style` | string | Email #6 CTA |
| `digest_frequency` | enum | Email #9 CTA |
| `life_domains` | string[] | Email #5 CTA |
| `biggest_challenge` | text | Email #4 reply |
| `engagement_score` | float | Opens + clicks + drops + replies |
| `trial_start` | timestamp | Admission |
| `trial_end` | timestamp | trial_start + 21d |
| `converted` | boolean | Stripe webhook |
| `last_drop_at` | timestamp | Drop ingestion |
| `nudge_count` | int | System |

### Funnel Metrics Targets

| Metric | Target |
|--------|--------|
| Welcome → First drop | >60% in 24h |
| Email open rate | >45% |
| Trial → Lite conversion | >8% |
| Avg drops per trial user | >10 |
| Nudge → Drop rate | >20% |
| Style preference set | >40% by Day 7 |
| Reply rate | >15% |

---

## 4. PRICING & BILLING

### Trial Structure
- **Length:** 21 days (aligns with onboarding funnel)
- **Includes:** 50 drops, full Intelligence Map, daily or weekly digest
- **No credit card required**

### Tiers

| Tier | Price | Drops | Features |
|------|-------|-------|----------|
| **Free** | $0 | 10/mo | Weekly digest, basic themes |
| **Lite** | $7/mo | 100/mo | Daily or weekly, full Intelligence Map |
| **Pro** | $15/mo | 500/mo | Multiple emails, API access |
| **Custom** | $49/mo | Unlimited | Team features, custom templates, dedicated domain |

### Stripe Setup
- One-click upgrade (Stripe link, no checkout flow)
- Pay-as-you-go overages: $0.10/drop above limit
- Pause anytime (data retained, resume later)
- Annual option: TBD (Joey to decide)

### Alternative Simpler Model (from Strategic Answers)
Some analysis suggests launching with just **Free ($0) + Pro ($9/mo)** to reduce complexity. Free = 10 drops/week, 3x/week digest. Pro = unlimited, daily, custom timing. Joey needs to decide which tier structure to use.

---

## 5. EMAIL LISTS & SEGMENTATION

### 4 Foundational Lists

| List | Purpose | How They Join |
|------|---------|---------------|
| **Feedback** | Beta testers, power users | Personal invite by Joey |
| **BHA** | BrutallyHonest.ai cross-sell | Auto-sync from BHA (opt-in) |
| **DA Interested** | Waitlist, prospects | Landing page signup |
| **Friends & Family** | Inner circle | Joey adds manually |

### Segmentation Rules
- One person can be on multiple lists
- Each list gets different email content/CTAs
- Friends & Family get "skip the waitlist" priority

### Soft Launch Tiers

| Tier | Segment | When | Criteria |
|------|---------|------|----------|
| **Tier 1** | Friends & Family | Mar 24 09:00 | Immediate personal support (Lisa, Danny, Bob) |
| **Tier 2** | Feedback Core subset | Mar 24 12:00 | If Tier 1 digests clean |
| **Tier 3** | BHA Engaged subset | Mar 24 17:00 | If Tier 2 stable |

---

## 6. DATA ARCHITECTURE

### User Data Separation
- **Row-level isolation** — each user is an isolated database row
- **Scoped access** — data access scoped to `user_id` only
- **Encryption** — AES-256 at rest (Railway volumes)
- **Backups** — daily to S3, encrypted
- **Retention** — soft delete, 30-day recovery
- **Export** — GDPR-compliant data portability

### Profile Enrichment Pipeline
1. Every email open → update `last_active_at`, `engagement_score`
2. Every CTA click → update relevant profile field
3. Every reply → parse for context, update `biggest_challenge` or `focus_domains`
4. Every drop → update `drop_count`, `last_drop_at`, recalculate `engagement_score`

### The "Smaller Slice" Philosophy
- Each user's data = one PostgreSQL row + one Resend contact
- Intelligence = ephemeral (generated, emailed, discarded)
- Vault = user's email inbox (we don't store history at scale)
- Analytics = aggregate only (no individual tracking)
- No cross-user queries possible
- API keys rotate monthly
- Webhook tokens unique per user
- Full audit log: who accessed what, when

---

## 7. PRE-LAUNCH AUDIT RESULTS

### 6-Audit Scorecard

| Audit | Findings | 🔴 Critical | 🟡 Should Fix | 🟢 OK |
|-------|----------|-------------|---------------|-------|
| **Hub (opoerator-hub)** | 12 | 1 | 6 | 5 |
| **Dropper-Code** | 18 | 5 | 8 | 5 |
| **Workforce & Ops** | 39 specs + 5 policy conflicts | 2 | 5 | — |
| **Services & Infra** | 9 services | 3 | 5 | 4 |
| **DA App (Frontend)** | ~85 files removable | 1 | 3 | — |
| **BHA Isolation** | 5 areas checked | 1 | 2 | 3 |

### Revised Scorecard (Post Email-Only Pivot)

| Category | Original | Revised |
|----------|----------|---------|
| 🔴 Critical | 12 | **8** (-4 dashboard items now irrelevant) |
| 🟡 Should Fix | 23 | **18** (-5 frontend issues) |
| 🟢 OK | 20 | **20** |
| **NEW** Critical | — | **+3** (email template, deliverability, admission sequence) |

### Top 14 Critical Issues

| # | Issue | Status | Owner |
|---|-------|--------|-------|
| 1 | **Poe balance near zero** (~37K points, burning ~6,300/hr) | 🔴 OPEN | Joey |
| 2 | **Intelligence Map email template** doesn't exist yet | 🔴 OPEN | Drop |
| 3 | **Admission email sequence** undefined | 🔴 OPEN (now designed — 13 emails) | Drop |
| 4 | **Email deliverability** — no dedicated IP warming | 🔴 OPEN | Drop |
| 5 | **Dropper-Code `merge_pr()`** still callable | 🔴 OPEN | Dropper-Code |
| 6 | **Hub `OPENCLAW_HOOK_URL`** empty — alerts don't forward | 🔴 OPEN | Joey |
| 7 | **Hub Stripe webhook disabled** | 🔴 OPEN | Joey |
| 8 | **Railway API tokens expired** | 🔴 OPEN | Joey |
| 9 | **Dropper-Code `system_pulse`** says "Auto-merge: active" (stale) | 🟡 OPEN | Dropper-Code |
| 10 | **No Claude cost controls** in Dropper-Code | 🟡 OPEN | Dropper-Code |
| 11 | **BHA→DA data sync** — cross-contamination via sync-to-opoerator | 🟡 OPEN | Joey (decision) |
| 12 | **18 console.log statements** in DA frontend prod code | 🟡 LOW | N/A (frontend frozen) |
| 13 | **Shared HUB_API_KEY** between BHA and DA | 🟡 OPEN | Drop |
| 14 | **Stripe past_due subscription** ($7/mo, 8+ failed charges) | 🟡 OPEN | Joey |

### Dropper-Code Tasks Completed Tonight (Mar 16-17)
4 tasks were completed during the audit sprint:
1. ✅ Hook fix (webhook forwarding)
2. ✅ Truncation fix (message length)
3. ✅ From-address standardization
4. ✅ Re-engagement guard (prevents over-nudging)

---

## 8. SPEC TRIAGE

### Summary: 39 Specs Re-Evaluated

| Action | Count | Examples |
|--------|-------|---------|
| **KEEP** | 13 | PRD-Action-Plan, LAUNCH-CRITICAL-PATH, SNAPBACK-INTEGRATION, DIGEST-POLICY (elevated), SOFT-LAUNCH-LIST, COMMS-GUIDE, PERMISSIONS, SPEC-Snapback-Email-Sequence, SPEC-User-Scenario-Matrix, weekly-catch-STYLE-GUIDE, snapback-offer, goldmine-index |
| **ARCHIVE** | 14 | Cash-Burn-Tracker, RAILWAY-BOT-MANUAL, SPEC-Adaptive-Weekly-Catch, SPEC-Human-Insight-Snapshot, SPEC-Message-Bottle, SPEC-Mitch-Advisory, SPEC-Transurfing-Snapback, SPEC-Weekly-Catch-Progressive, content-transformation-system, poe-funnel-paste-ready, transurfing-product-vision, target-slide-rancho-mirage |
| **KILL** | 12 | AGENT-COMPANY-v3, ARI-Styling-Assistant, COMPANY-CONSTITUTION (dupe), GUMROAD-GENESIS, LOOPSLAP-MASTER-PRD, PLATFORM-DEPARTMENT, PRD-Desktop-Mobile-Split, SPEC-Admin-User-Lifecycle, SPEC-DigestBot, SPEC-MOMENTUM-TRACKER, SPEC-NARRATIVE-ENGINE, SPEC-PATTERN-WEAVER, SPEC-Joey-AI-Builder-Pack, SPEC-VAULT-Archaeologist |

---

## 9. WHAT GETS CUT

### 67% of DA Frontend — Gone

| Feature | Est. Hours | Status |
|---------|-----------|--------|
| Vault view (search, browse, filter) | 20h | ❌ CUT |
| Intelligence Map tab | 16h | ❌ CUT |
| Stream view | 12h | ❌ CUT |
| Settings page | 10h | ❌ CUT |
| Auth flows (login, signup, password reset) | 12h | ❌ CUT |
| Mobile app shell / PWA | 15h | ❌ CUT |
| Onboarding wizard | 8h | ❌ CUT |
| Theme customization UI | 6h | ❌ CUT |
| Dashboard navigation | 4h | ❌ CUT |
| **TOTAL SAVED** | **~103 hours** | **~$8,000+ dev cost** |

### Recommendation
- Create `phase-2/dashboard` branch to preserve all frontend work
- Freeze `dropanywhere-app` main repo for dashboard features
- Fresh landing-page branch: strip to ~10 files / ~2,000 lines (from 85 files / 41K lines)

---

## 10. SOCIAL MEDIA & MARKETING

### MEGA Campaign — "Make Email Great Again"

**Tagline:** "Your inbox isn't broken. The 47 apps you downloaded to fix it are."  
**Tone:** Satirical but warm. Anti-productivity-industrial-complex.  
**Visual:** Red MEGA caps with parrot 🦜. Campaign Red (#C41E3A) + Brooke Cream.

### Campaign Pillars

| Pillar | Message | Format |
|--------|---------|--------|
| The Problem | You downloaded 47 apps to replace email | Social, ads |
| The Truth | Email was always the answer | Manifesto, LinkedIn |
| The Product | DropAnywhere = email as superpower | Demo, carousel |
| The Vibe | MEGA caps, parrot energy, anti-app rebellion | Merch, visual identity |

### Launch Sequence (15-Day MEGA Campaign)
- **Day -7:** Teaser ("Something's coming. Not another app.")
- **Day -5:** Clue ("Tool invented in 1971. You checked it 47 times today.")
- **Day -3:** MEGA Reveal ("Make Email Great Again 🦜")
- **Day 0:** Launch Day (full blast across all platforms)
- **Day +1-7:** Victory lap, use cases, FAQ, founder story

### Content Calendar (Launch Week Mar 24-30)

| Day | Platform | Post | Status |
|-----|----------|------|--------|
| Mar 23 (Pre) | LinkedIn | Teaser — "I built 12 note-taking systems" | ✅ Draft ready |
| Mar 24 (Launch) | LinkedIn | Announcement — launch-day-final-REWRITE (9/10) | ✅ **BEST VERSION** |
| Mar 24 | Twitter/X | "Your brain doesn't have folders" | ✅ Ready |
| Mar 24 PM | LinkedIn | Behind the scenes | ✅ Ready |
| Mar 25 | LinkedIn | Use case thread (voice notes, screenshots, 2am ideas) | ✅ Ready (8.5/10) |
| Mar 26 | LinkedIn | "We Broke Productivity" philosophy | ✅ Ready (8.5/10) |
| Mar 27 AM | LinkedIn | Comparison vs Notion/Obsidian/Apple Notes | ✅ Ready |
| Mar 27 PM | LinkedIn | "The Moment It Clicked" (9/10) | ✅ **SHIP THIS** |
| Mar 28 | LinkedIn | Founder story — shower idea origin | ✅ Ready |
| Mar 29 | LinkedIn | Week 1 numbers reflection | ✅ Draft ready |

### Additional Assets Ready

| Asset | File | Rating |
|-------|------|--------|
| MEGA overview & strategy | mega-campaign/MEGA-OVERVIEW.md | ✅ Complete |
| Email sequence (MEGA) | mega-campaign/mega-email-sequence.md | ✅ Complete |
| Instagram carousel | mega-campaign/mega-instagram-carousel.md | ✅ Complete |
| Twitter thread | mega-campaign/mega-twitter-thread.md | ✅ Complete |
| LinkedIn launch | mega-campaign/mega-linkedin-launch.md | ✅ Complete |
| One-liner variations | mega-campaign/mega-one-liner-variations.md | ✅ Complete |
| Freedom from busy work | freedom-from-busy-work-linkedin.md | ✅ Week 2+ (8/10) |
| Mirror principle | mirror-principle-linkedin-POLISHED.md | ✅ Week 3+ (8.5/10) |
| Stop rowing upstream | stop-rowing-upstream-linkedin-POLISHED.md | ✅ Week 2-3 (8.5/10) |
| Captain metaphor | the-captain-metaphor-linkedin-POLISHED.md | ✅ Ready |
| Simplicity wins | simplicity-wins-linkedin-POLISHED.md | ✅ Ready |

**Coverage:** 11 posts drafted for 8-day launch week. 6+ posts ready for Weeks 2-3. MEGA campaign fully built with cross-platform assets.

---

## 11. LIVE METRICS

| Metric | Value | Note |
|--------|-------|------|
| **DA Users** | 101 | Hub database |
| **DA Drops** | 874 | Total ingested |
| **BHA Users** | 260 | BrutallyHonest.ai |
| **BHA Active (7d)** | 65 | Weekly active |
| **Poe Balance** | ~20K points | 🔴 CRITICAL — burning fast |
| **Stripe MRR** | ~$14/mo | 2 active subscriptions |
| **Stripe Past Due** | ~$7/mo | 1 sub, 8+ failed charges |
| **Monthly Burn** | ~$145/mo | Email-only (down from ~$267) |
| **Net Burn** | ~$130/mo | After revenue |
| **Runway Extension** | +45% | vs full dashboard plan |

### Family User Status (Tier 1 Soft Launch)
- **Lisa:** 12 days inactive ⚠️ needs outreach
- **Danny:** 0 drops ever ⚠️ needs personal invite
- **Bob:** 9 days inactive ⚠️ needs outreach

---

## 12. ACTION PLAN (Mar 17-22)

### Monday Mar 17 — Foundation Day
| Task | Owner |
|------|-------|
| Regenerate Railway API tokens | Joey |
| Top up Poe points (100K+) | Joey |
| Set `OPENCLAW_HOOK_URL` on Hub Railway | Joey |
| Begin Intelligence Map email template (Brooke theme) | Drop |
| Write admission sequence copy (Email #1 draft) | Drop |
| Freeze dropanywhere-app dashboard work | Joey |

### Tuesday Mar 18 — Template Build Day
| Task | Owner |
|------|-------|
| Complete digest email template v1 (full HTML/CSS) | Drop |
| Build landing page skeleton (static HTML + waitlist form) | Drop |
| Write Email #2 (First Drop Instructions) | Drop |
| Set up Resend dedicated IP | Drop |
| Test email rendering (cross-client) | Drop |
| Dropper-Code safety fixes (delete merge_pr, fix system_pulse) | Dropper-Code |

### Wednesday Mar 19 — Integration Day
| Task | Owner |
|------|-------|
| Wire Hub → digest template (live data) | Dropper-Code |
| Build admission flow in Hub (waitlist → admitted webhook) | Dropper-Code |
| Write Email #3 (First Digest Preview) | Drop |
| Landing page polish (Brooke theme) | Drop |
| End-to-end test: Signup → Admit → Email 1 | Joey + Drop |

### Thursday Mar 20 — Test Day
| Task | Owner |
|------|-------|
| Spam score testing (Mail-Tester, target 8/10+) | Drop |
| Test digest with Joey's live drops | Joey |
| Soft launch list outreach (personal messages to Tier 1) | Joey |
| Landing page final review | Joey + Drop |
| Stress test: 100 test digests | Drop |

### Friday Mar 21 — Buffer Day
| Task | Owner |
|------|-------|
| Fix any rendering issues across email clients | Drop |
| Final copy polish (brand voice) | Joey |
| Deploy landing page to drop-anywhere.com | Drop |
| Document rollback plan | Drop |
| Team dry-run: admit test user end-to-end | Joey + Drop |

### Saturday Mar 22 — Lock Day
| Task | Owner |
|------|-------|
| **CODE FREEZE** — no more changes | All |
| Final admission flow test | Joey |
| Monitor Poe balance (>50K maintained) | Drop |
| Prepare go/no-go checklist | Drop |
| **REST** | Joey |

### Sunday Mar 23 — Rest Day
No work. Joey rests. Drop monitors.

### Monday Mar 24 — 🚀 LAUNCH DAY

| Time (CDT) | Activity | Owner |
|------------|----------|-------|
| 08:00 | Final systems check | Drop |
| 09:00 | Admit Tier 1 (family: Lisa, Danny, Bob) | Joey |
| 10:00 | Monitor first digests | Drop |
| 12:00 | Admit Tier 2 (feedback friends) if Tier 1 clean | Joey |
| 14:00 | Monitor, adjust, observe | Both |
| 17:00 | Admit Tier 3 (power users) if stable | Joey |
| EOD | Launch retrospective | Both |

---

## 13. DECISIONS JOEY NEEDS TO MAKE

### Before March 24 (Blocking)

| # | Decision | Options | Recommendation |
|---|----------|---------|----------------|
| 1 | **Tier structure** | 4-tier (Free/Lite/Pro/Custom) vs 2-tier (Free/Pro $9) | Start with 2-tier for simplicity, expand later |
| 2 | **Trial length** | 7 / 14 / 21 / 30 days | 21 days (matches onboarding funnel) |
| 3 | **Free tier** — keep or remove? | Keep (conversion funnel) vs Remove (everyone pays) | Keep — it's the hook |
| 4 | **Poe balance** — add credits NOW | Top up immediately vs pause heavy bots | Top up 100K+ points TODAY |
| 5 | **Tier 1 soft launch list** | Confirm family: Lisa, Danny, Bob + who else? | Personal outreach this week |
| 6 | **Tier 2 list** | Which 5-6 "feedback core" users? | Joey picks |
| 7 | **BHA cross-sell timing** | Email BHA list about DA at launch? Or wait? | Wait until DA stable |
| 8 | **First digest timing** | Immediate vs overnight vs user-scheduled | Overnight (next morning) |
| 9 | **Railway API tokens** | Regenerate in dashboard | Do it Monday |
| 10 | **OPENCLAW_HOOK_URL** | Set on Hub Railway vars | Do it Monday |
| 11 | **Hub Stripe webhook** | Re-enable or keep disabled? | Re-enable if subscriptions launch |
| 12 | **BHA→DA data sync** | Keep sync-to-opoerator or remove? | Remove for clean isolation |

### Post-Launch

| # | Decision |
|---|----------|
| 13 | Admission velocity — how many users/day after launch? |
| 14 | Waitlist cap — soft limit at 50? 100? |
| 15 | Dashboard timeline — commit to Q2 publicly? |
| 16 | Team tier priority — is B2B the growth engine? |
| 17 | BHA migration — automated campaign or personal outreach? |
| 18 | Annual pricing — when to introduce? |

---

## 14. COST BREAKDOWN & SAVINGS

### Monthly Burn Comparison

| Service | Full Dashboard | Email-Only | Savings |
|---------|---------------|------------|---------|
| Railway Hub (backend) | ~$20 | ~$20 | $0 |
| Railway OpenClaw | ~$15 | ~$15 | $0 |
| Railway Dropper-Code | ~$10 | ~$10 | $0 |
| Railway Frontend | ~$15 | **$0** (static) | **$15** |
| Railway dropanywhere-cron | ~$5 | **$0** (dead) | **$5** |
| Frontend build minutes | ~$5 | **$0** | **$5** |
| Database (unused features) | ~$10 | ~$5 | **$5** |
| Resend Email | ~$0-20 | ~$0-20 | $0 |
| Poe Points | ~$20-50 | ~$20-50 | $0 |
| OpenRouter | ~$100 | ~$50 | **$50** |
| Anthropic (OpenClaw) | ~$20-50 | ~$20-50 | $0 |
| GitHub | $0 | $0 | $0 |
| Cloudflare | $0 | $0 | $0 |
| Stripe fees | ~$2 | ~$2 | $0 |
| **TOTAL** | **~$267/mo** | **~$145/mo** | **~$122/mo** |

### Revenue
- Current MRR: ~$14/mo (2 active Stripe subs)
- Past due (recoverable): ~$7/mo
- Net burn: ~$130/mo

### Dev Time Saved
- Frontend work eliminated: **~103 hours** (~$8,000+ at market rates)
- Specs killed/archived: 26 of 39 (focus restored)
- Agent roles simplified: 5 agents paused/repurposed

### Go/No-Go Checklist (Mar 24)

| Criteria | Threshold | Status |
|----------|-----------|--------|
| Poe balance | >50K points | ⬜ |
| Digest template | Joey approved | ⬜ |
| Admission flow | End-to-end tested | ⬜ |
| Landing page | Live, waitlist working | ⬜ |
| Email deliverability | 8/10+ spam score | ⬜ |
| Hub alerts | Forwarding to WhatsApp | ⬜ |
| Soft launch list | Joey reviewed | ⬜ |
| Rollback plan | Documented | ⬜ |

---

## SOURCE FILES

| Document | Location |
|----------|----------|
| This Blueprint | `ops/COMPASS-MASTER-LAUNCH-BLUEPRINT.md` |
| COMPASS (strategic) | `ops/COMPASS.md` |
| Onboarding Funnel | `ops/ONBOARDING-FUNNEL.md` |
| Agency Poll (9-1) | `ops/strategic-poll-email-only-pivot.md` |
| Strategic Answers | `ops/strategic-answers-email-only-pivot.md` |
| Master Audit v2 | `ops/audit/MASTER-REPORT-v2-EMAIL-ONLY.md` |
| Hub Audit | `ops/audit/hub-audit-report.md` |
| Dropper-Code Audit | `ops/audit/dropper-code-audit-report.md` |
| Workforce Audit | `ops/audit/workforce-audit-report.md` |
| Infra Audit | `ops/audit/services-infra-audit-report.md` |
| DA App Audit | `ops/audit/da-app-audit-report.md` |
| BHA Audit | `ops/audit/bha-audit-report.md` |
| Brand Guide | `ops/BRAND-GUIDE.md` |
| Email Standards | `ops/EMAIL-STANDARDS.md` |
| Digest Policy | `ops/DIGEST-POLICY.md` |
| CEO Email OS | `ops/CEO-EMAIL-OS.md` |
| Content Calendar | `social/content-calendar.md` |
| MEGA Campaign | `social/mega-campaign/MEGA-OVERVIEW.md` |

---

*This is THE document. Everything in one place. The single source of truth for DropAnywhere's March 24 launch.*

*Reply to this email — Drop reads every reply. 🦜*

*DropAnywhere · Chicago, IL · USA*
