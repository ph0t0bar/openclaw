# PRD: DropAnywhere Ecosystem - Master Action Plan

**Author:** Claw (OpenClaw) + Joey
**Date:** 2026-03-11 (v4 - Snapback breakthrough)
**Status:** Active - the single source of truth
**Incorporates:** Both PRDs (Mar 9 + 10), DA TODO.md (Gates A-D), TODO-PROPOSED.md (Gate D: Invisible Assistant), BHA TODO.md, 100+ Joey vault drops, FULL-PICTURE.md, REVENUE_SUMMIT_OUTCOME.md, GitHub state (34+ PRs), Hub metrics (live), Poe fleet + GA/SEO data, joey-backup asset inventory, all Ingestion subfolder strategic docs (txt, md, csv), and **Snapback / The Weekly Catch breakthrough session (Mar 11, 3am)** - `joey-backup/specs/SNAPBACK-INTEGRATION-2026-03-11.md` + offer + visualizations.

---

## 1. Executive Summary

**March 3-10 velocity:** 29+ PRs shipped across 4 repos. Poe Orchestrator live with 16 shadow bots. DA crossed 65 users (organic). BHA at 211 users, 531 active weekly visitors. 3 Stripe subs confirmed ($21 MRR). Dropper-Code autonomous pipeline operational (12 tasks completed).

**March 16 metrics update:** DA now at 100 users (+54%), 843 total drops, 7 active in 24h. BHA at 259 users (+23%), 70 active weekly, 7 active in 24h. 2 Pro subs via Stripe. Poe balance critical at 42,770 points (burning ~43K/6h).

**March 11 (3am) breakthrough:** Snapback / The Weekly Catch emerged as the core product direction - not a feature, the entire experience. Joey used the system on himself (dropped a feeling about being stuck on music → got a narrative Snap Back → made music → started a 30-day songwriting challenge with Brooke). The loop proved itself in a single session. Full integration spec committed to joey-backup. Daily digest → Weekly Catch is the strategic pivot. See Section 5.12 (promoted from P2 to P0).

**March 11 (05:00-09:45 UTC) - Archive & Snapback expansion session:**
- **Excavation batch-0001** committed to `Ingestion/1_GOLDMINE/` - first automated extraction from the VAULT. The transformation engine (VAULT → GOLDMINE → FORGE → OUTPUT) is now live, not just theoretical.
- **40+ Poe conversation documents** uploaded to `Ingestion/0_VAULT/Documents/` (Jan 2026 conversations: MIC DROP BMM SURPIPHANY, HOLOGRAM MHC TRANSURFING, Context as a Service, ANTIGRAVITY HOLISTIC SYNC, SOMATIC SURPIPHANY, etc.). These are Joey's raw thinking captured from Poe sessions.
- **New reference docs added:** `AUTONOMOUS-REVENUE-STACK.md` + `SFP_OPERATIONAL_HYDRATION.md` - strategic planning documents from the archive.
- **BHA content pipeline** data (`CONTENT_PIPELINE.json`) added - BHA's content generation infrastructure exported from Notion.
- **Time capsule** for March 11 created (`Ingestion/20260310/time-capsule-2026-03-11.json`) + chat transcript saved.
- **Three Transurfing visualizations** committed: music (FL Studio), songwriting (30-day challenge with Brooke), and the product vision piece ("Snap Back III: The Weekly Catch").
- **Snapback Offer copy expanded** with new supporting language: *"We all find ourselves getting stuck... unable to drop that thing."* - the empathy-first hook that grounds the product promise in relatable daily friction (dentist at 2, gym bag, therapy, bills).
- **Archive reorganization:** Old PRDs moved to `specs/archive/`. `PRD-Action-Plan-latest.md` established as the canonical copy in joey-backup.
- **Total joey-backup commits today: 30+** - this was a major archive, content, and product vision session.

**What the Ingestion archive reveals that prior PRDs missed:**
- Joey's vision has been consistent since Jan 2025: one intake → AI analysis → clarity delivered. The "Letter From My Future Self" (Dec 2025) describes *exactly* what DA now does. He's living inside his own product vision.
- **2,462 OpenAI conversations** and **467 Poe bots** are untapped content/product assets. The transformation engine (VAULT → GOLDMINE → FORGE → OUTPUT) is architecturally sound but not yet productized.
- **Danny Advisory Package** is the clearest demo of DA's B2B use case: email loop, invisible AI processing, human-curated output. Danny doesn't even know he's using DropAnywhere.
- **Cash Burn Tracker** (Mar 9) shows another advisory use case being served through conversational AI - structured financial planning via chat → spreadsheet.
- **MythOS doctrine** (Jan 2026) articulates the cognitive architecture that should govern OpenClaw, Dropper-Code, and any future multi-agent system.
- **BHA SEO is the growth engine:** 63% of traffic is Google organic. "brutally honest ai" and "honest ai" queries are the moat. Poe→BHA funnel leaks badly (only 4% of traffic is Poe referral despite massive bot usage).
- **Poe fleet = 467 bots, 70K+ users, $6,400+ lifetime revenue.** But 96% comes from 5 bots. The long tail is dormant.

---

## 2. The Vision (Joey's Words)

> *"You wake up without an alarm. There is no frantic reach for the phone to check notifications, because you know the System has already triaged the world for you... You open your device, not to work, but to Review."*
> - Letter From My Future Self, December 2025

> *"I didn't need another place to store things. I needed something that would think with me."*
> - Birthday launch post, February 27, 2026

> *"Drop it. Forget it. Wake up lighter."*
> - Core promise

> *"Laziness was your soul begging for efficiency."*
> - The epiphany that started everything

**The Container Creates Freedom.** Structure enables presence. Capture everywhere, think nowhere, wake up to clarity.

**Joey's Target Slide - The Rancho Mirage Mansion (2026-03-11):**
The method of loci visualization that anchors every decision. First person, all happening now: the mansion, the pool table, the podcast/music studio, Boo and Teddy playing outside, swimming with Brooke, fancy dinners, driving with arm out the window, a text from the AI saying "everything's handled and feedback is incredible," the world becoming better for everyone, abundance flowing, hanging with Kevin Smith on a new project, shooting a pilot with Larry David, working on comedy, posting funny videos, writing a book in the perfect office. All linked to one environment. All happening. The feeling: light, happy, excited, in control by letting go. *This is what the system exists to enable.*

---

## 3. Product Architecture

### 3a. The Ecosystem Layers

| Layer | Product | Status | Revenue Model |
|-------|---------|--------|---------------|
| **Capture** | DropAnywhere | Live (65 users) | Freemium → Pro ($9/mo planned) |
| **Process** | oPOErator Hub | Live | Backend, no direct revenue |
| **Consume** | DA Web App | Live | Part of DA |
| **Monetize** | BrutallyHonest.ai | Live (211 users, $21 MRR) | Credits + Subscriptions |
| **Distribute** | Poe Fleet (467 bots) | Live (70K+ users) | Poe points + BHA funnel |
| **Assist** | OpenClaw | Live | Internal tool |
| **Execute** | Dropper-Code | Live | Internal automation |
| **Inform** | Joey Backup / Knowledge Engine | Exists | Content mine for products |

### 3b. The Transformation Engine (from SYSTEM_ARCHITECTURE.md)

```
VAULT (2,462+ conversations, 600+ drops, 100+ scripts)
    ↓ Extract
GOLDMINE (prompts, insights, frameworks, personas)
    ↓ Transform
FORGE (staging, drafts, experiments)
    ↓ Publish
OUTPUT (posts, products, tools, exports)
```

This architecture exists in the Ingestion folder and **excavation batch-0001 was committed on Mar 11** - the first automated extraction from VAULT to GOLDMINE. The transformation engine is now live, not just theoretical. Scripts exist (watch.py, pan.py, extract_insights.py). Productizing this = a "Knowledge OS" layer on top of DA.

### 3c. The Invisible Loop (from Danny Advisory Package)

```
Joey captures context → System processes → Joey curates →
Recipient replies → Reply becomes new drop → Loop continues

The recipient never knows they're using DropAnywhere.
They're just getting incredibly thoughtful emails.
```

This is the B2B wedge. Advisory firms, coaches, therapists - anyone who serves clients through ongoing conversation. DropAnywhere becomes the invisible intelligence layer.

---

## 4. Strategic DNA (What the Archives Reveal)

### 4a. Revenue Council Verdict (Jan 2026, REVENUE_SUMMIT_OUTCOME.md)

The AI council (Gemini, oPOErator-Pro, Surpiphany, Orchestr8) analyzed the full codebase and recommended:

1. **Genesis Orchestrator** ($97) - "Council in a Box" product for Gumroad
2. **Agency in a Box** ($497) - mid-tier bundle
3. **Mythos Cloud SaaS** - continuity play (long-term)

**Status:** Genesis Orchestrator was packaged (dist/genesis-orchestrator-product.zip, SALES_COPY.md written) but never launched on Gumroad due to API blocker. The product exists, the sales copy exists, the distribution channel exists. It just needs to be listed.

### 4b. AI Agent Market Intelligence (Jan 2026, AI_AGENT_SUMMIT_LATEST.md)

Key findings from Tippiy market research:
- AI agent market: $7.6B in 2025, growing 49.6% annually
- Pricing sweet spots: $49/mo (individual), $149/mo (pro), $999 (one-time custom)
- Blue ocean: Mental health AI companions, elderly care, niche professional tools
- Best distribution: Direct website + Gumroad (highest margins, customer control)
- **Joey's moat:** 467 bots with 70K+ users is a distribution network most startups would kill for

### 4c. MythOS Doctrine (Jan 2026) - Architecture Principle

**"The Executive Layer Never Reaches Down."**

This applies to:
- **OpenClaw:** Should orchestrate via sub-agents, not do everything in main context
- **Dropper-Code:** Already follows this - brain-scan proposes, human approves, executor builds
- **DA Architecture:** The monolith (24K-line main.py) needs layered separation eventually
- **Product design:** Users should never see the machinery. They just "drop it and forget it."

### 4d. Joey's Thinking Patterns (from 2,462 conversations + brain extraction)

```json
{
  "conversations": 948 (analyzed subset),
  "top_themes": {
    "action": 155, "remember": 71, "brutal": 63,
    "honest": 52, "automate": 26, "fire": 17,
    "efficiency": 10, "real talk": 6
  },
  "frustrations": 65,
  "decisions": 79,
  "abandoned_projects": 100
}
```

**Pattern:** Joey generates ideas at 10x the rate he executes them. The system must be the execution layer. Ideas that survive repeated mention across conversations are the real signal. Everything else is creative exhaust.

### 4e. H-Score Philosophy (from 0.942-club.txt)

The **Hydration Score (H-Score)** measures contextual integrity across:
- **Sovereignty:** Operating from choice, not reaction
- **Alignment:** Actions match stated values
- **Flow:** Resistance level in current work
- **Revenue:** Financial trajectory and health
- **Momentum:** Rate of meaningful progress
- **Ingestion:** Quality of input being processed

**Rule:** Don't give decisions when H-score is below 0.90. Hydrate first, opine second.

---

## 5. Prioritized Action Items

### 🔥 P0: DO TODAY (High Impact, Low Effort)

#### 5.1 Shadow Bot Cross-Promo Descriptions ← MANUAL (10 min)
- Update descriptions on top 5 original Poe bots to link to v2 shadow bots
- Blocked by: Poe API 500s on PATCH. Must be manual.
- **Impact:** Every original conversation → funnel to Hub-backed version with CTA + logging
- **Status:** Ready

#### 5.2 Funnel Prompt Paste ← MANUAL (10 min)
- Paste BHA funnel CTA into system prompts of top 5 original bots on poe.com
- Funnel prompts already written in `joey-backup/specs/poe-orchestrator/funnel-prompts-draft.md`
- **Impact:** At 14K+ points/6h organic Poe traffic, this is free distribution → BHA signups
- **Why urgent:** Poe→BHA referral is only 4% of BHA traffic despite massive bot usage. This one change could 5-10x it.

#### 5.3 Genesis Orchestrator Gumroad Listing
- Product is PACKAGED (dist/genesis-orchestrator-product.zip)
- Sales copy is WRITTEN (products/genesis-orchestrator/SALES_COPY.md)
- User guide is DONE (products/genesis-orchestrator/README.md)
- **All that's missing:** Manual listing on Gumroad at $97
- **Impact:** First digital product revenue. The Revenue Council recommended this as the #1 priority in January.

---

### 📋 P1: THIS WEEK (Medium Impact, Medium Effort)

#### 5.4 BHA SEO Optimization Sprint
**Source:** Google Search Console data (Feb 2026 CSVs from Ingestion)

| Action | Current | Target | Effort |
|--------|---------|--------|--------|
| Homepage meta for "honest ai" | Position 3.6, CTR 29.6% | Position 1-2, CTR 40%+ | 30 min |
| "Most honest ai" meta description | Position 3.4, CTR 20% | CTR 35%+ | 20 min |
| FAQ/blog: "What is the most honest ai?" | No page | Rank for question queries | 2h |
| Bot page descriptions (unique, keyword-rich) | 0 clicks on bot pages | Organic bot discovery | 1h |
| `/store` meta compelling copy | CTR 3.2% | CTR 15%+ | 20 min |

**Why now:** BHA gets 63% of traffic from Google organic. Every meta tag improvement = more free users. This is the highest-ROI marketing activity.

#### 5.5 Chrome Web App Drop Enhancement
- **Source drop:** *"Drop via chrome web app / chrome app should be able to do so much cool shit"*
- Right-click context menu: "Drop to DropAnywhere" on any selected text
- Keyboard shortcut (Ctrl+Shift+D) for quick-drop popup
- Badge notification when digest is ready
- **Owner:** Dropper-Code (dropanywhere-app)

#### 5.6 "Droppings" - Contextual Drop Tagging
- **Source drops:** *"the dropping - the contextual beacon"* + *"ensure every one of these drops become 'droppings'"*
- Auto-tag with source metadata (web/email/sms/voice/poe/api) + timestamp + device type
- Display tags in vault list view. Let users see and edit.
- **Owner:** Dropper-Code (opoerator-hub)

#### 5.7 Shadow Bot → Production Cutover Decision
- After cross-promo live (5.1), monitor v2 traffic 48h
- Options: hybrid (originals for discovery, shadows for intelligence), full cutover, or Poe support escalation
- **Decision point:** End of week

#### 5.8 Desktop vs Mobile App Split - Phase 1
- **PRD:** `PRD-Desktop-Mobile-Split-2026-03-10.md`
- "Capture Instrument" (mobile) vs "Reflection Studio" (desktop)
- Phase 1: `useIsMobile()` hook + conditional rendering. No new components.
- **Status:** On hold pending Joey's review

#### 5.9 Intelligence-to-Vault Linking
- Intelligence Map nodes should link back to source drops
- Depends on: completed-items bug fix (filed, in Dropper-Code queue)

#### 5.10 Archive Completed Vault Items
- Clear "done" action for drops. Hidden from vault, digest, Intelligence Map.
- Related to Intelligence Map bug (being fixed now)

---

### 🧠 P2: THIS MONTH (High Impact, Higher Effort)

#### 5.11 Unified Drop Classification v2 ("The Bridge")
- **Full spec:** `joey-backup/Ingestion/20260303/file.md` (609 lines)
- Replace regex classifier with LLM classification at ingest
- Add: `drop_type` (reminder, action, idea, question, reflection, resource, session), `area` tags, `completable` flag, entity extraction, temporal intent parsing
- **Why this matters:** "Drop it. Forget it." only works if the system closes the loop. Right now drops are text blobs. This makes them actionable.

#### 5.12 Snapback / The Weekly Catch ← 🚨 PROMOTED FROM P2 → P0 (2026-03-11)
- **Source:** Joey's Mar 9 drop + 3am breakthrough session Mar 11 - **he was user zero. It already worked.**
- **Full spec:** `joey-backup/specs/SNAPBACK-INTEGRATION-2026-03-11.md` (the definitive document)
- **What it is:** Drop all week → system watches, connects, detects pendulum patterns → one Weekly Catch narrative on Sunday, told in first-person in the user's own voice, using their own details and language
- **The loop:** Drop (raw feeling) → System catches → Narrative returned → Creator creates → Drops more
- **Snapback is ADDITIVE, not a replacement for daily digests.** The multi-analyzer daily digest pipeline stays. Users love it. Both coexist: `digest_mode = 'daily'` (default, proven) or `'snapback'` (new layer, expanding gradually). Weekly Catch = a new experience layer alongside daily digests, not a pivot away from them.
- **Technical summary (from spec):** New `snapback_generator.py` + `user_profile_builder.py` + `email_prompt_scheduler.py`. Feature-flagged: `digest_mode = 'daily' | 'snapback' | 'both'`. Daily digest code fully preserved and untouched. DB: `snapback_stories` table + `snapback_profile` JSONB column.
- **What doesn't change:** All capture infra, Hub processing, PostgreSQL, Intelligence Map, Resend, Dropper-Code, BHA integration
- **Brand evolution:** "Drop it. Forget it. Wake up lighter." remains core. "Drop all week. Catch it Sunday." is the Snapback layer - ADDITIVE, not a replacement.
- **⚠️ CRITICAL (Joey, Mar 11 14:08 UTC): Snapback is ADDITIVE to daily digests, NOT a replacement.** The multi-analyzer daily digest pipeline is fire. Users love it. Don't kill that code. Snapback / Weekly Catch is a NEW product layer that opens up slowly alongside existing digests. Daily digest = proven, shipping, users love it. Weekly Catch = new experience, starts with Joey as user zero, expands gradually. Both coexist via `digest_mode` feature flag.
- **Naming (updated Mar 11):** "Snapback" (one word, not "Snap Back"). Also on the docket: **Loopslap** - originated from Joey's timelapse photography concept "loops and lapses," evolved into "slapping you out of the loops, gently, helping you snap back into the ideal version of you." Loopslap is more ownable (unique word, no trademark conflicts). Possible positioning: *Loopslap* as the brand, *Snapback* as the mechanism ("Loopslap: your weekly Snapback"), or vice versa. Decision pending.
- **This is the product nobody else has.** Transurfing + NLP personalization + email-first delivery + narrative (not summary) = unique moat.
- **Offer framing (from `snapback-offer-2026-03-11.md`):** "Bring me one problem. Talk about it for a week. I'll show you what you're not seeing." The free week IS the demo. They FEEL the vault when scattered drops come back as a story.
- **New supporting copy (added Mar 11 09:41 UTC):** *"We all find ourselves getting stuck... unable to drop that thing."* Then relatable examples: "Dentist at 2, Jeremy practice at 4, Dinner at 5. Don't forget your gym bag" | "I can't believe I said that" | "I've seen 5 therapists and read every self help book" | "how will I pay those bills?" → *"Drop here. We'll catch it. Organize it. Analyze it. Package it up. Debate it. Connect it. You'll have one less thing to carry in one week."* Core positioning: **"All you need is an email."**
- **Key learning (Mar 11):** Snapback narratives MUST come from the actual backend pipeline (Hub orchestrator + Claude Sonnet + real user drops + NLP/personalization), NOT from creative writing. The 3am session worked because it reflected Joey's OWN words back. The later visualizations Claw wrote were "meh" - portraits, not mirrors. The product is a mirror. The moment it becomes performative, it loses the thing that makes it hit.
- **Three Transurfing visualizations committed (Mar 11):** Music (`transurfing-snapback-music`), Songwriting (`transurfing-snapback-songwriting`), Product Vision (`transurfing-snapback-product-vision`). These serve as Snapback prototypes - first-person, present-tense narratives using Joey's own details, people, and language. They ARE the product.
- **Implementation:** See Section 5.12a below

#### 5.12a Snapback - Implementation Roadmap (from SNAPBACK-INTEGRATION-2026-03-11.md)

**Phase 1: MVP (1-2 weeks)**
- [ ] Build `snapback_generator.py` - weekly narrative generation (Claude Sonnet)
- [ ] `user_profiles` table or `snapback_profile` JSONB column on `users`
- [ ] Weekly cron (Sunday) alongside daily digest (feature-flagged)
- [ ] Basic Weekly Catch email template (narrative, not sections)
- [ ] Feature flag: `digest_mode = 'snapback' | 'daily'`
- [ ] Test with Joey first (user zero - prototype already worked)

**Phase 2: Personalization (2-4 weeks)**
- [ ] `user_profile_builder.py` - language pattern learning, emotional baseline, entity map
- [ ] Emotional tone detection at ingest (sentiment + pendulum detection)
- [ ] Transurfing phase detection (awakening / detached / aligned / creating)
- [ ] `email_prompt_scheduler.py` - Tue/Thu/Sat drop encouragement emails
- [ ] Previous-Snapback continuity in generation prompt
- [ ] Beta with 5-10 willing users from current base

**Phase 3: Scale + Revenue (Month 2-3)**
- [ ] Free vs Pro narrative differentiation (summary vs full story)
- [ ] Snapback+ tier ($19/mo - Transurfing-aware, custom style)
- [ ] Advisory Mode (white-label Weekly Catch for coaches/advisors)
- [ ] Onboarding flow rewrite (email-first: "Reply to start. That's it.")
- [ ] Brand update: "The Weekly Catch" / "Drop all week. Catch it Sunday."

**Phase 4: Intelligence (Month 3+)**
- [ ] Cross-week pattern detection ("You've mentioned this 3 weeks in a row")
- [ ] Seasonal/lifecycle awareness
- [ ] Multi-modal narratives (photos, voice snippets in the Catch)

**Pricing update (from spec):**

| Tier | Price | What |
|------|-------|------|
| Free | $0 | 3 drops/week, basic Weekly Catch (summary) |
| Pro | $9/mo | Unlimited drops, full Snapback narrative, Intelligence Map, email prompts |
| Snapback+ | $19/mo | Everything + Transurfing-aware processing, custom visualization style |
| Advisory | $49/mo | White-label Weekly Catch for coaches/advisors to send to clients |

---

#### 5.13 B2B Advisory Loop (Danny Use Case)
- **Source:** `_DANNY-ADVISORY-PACKAGE.md` - the complete playbook
- Danny doesn't know he's using DropAnywhere. He replies to joey@drop-anywhere.com, it becomes a drop, system processes, Joey sends curated follow-up.
- **Productize as:** "Advisory Mode" - a white-label email loop for coaches, consultants, therapists
- **Revenue model:** $49-149/mo per advisor seat
- **Cash Burn Tracker** (Mar 9 Ingestion) is another proof point: structured financial planning delivered via conversational AI

#### 5.14 NotebookLM Meditation Generation
- **Source:** Joey's Mar 5 drop - NotebookLM-generated meditation while running
- Generate personalized meditations from vault themes
- Quick path: document Joey's manual workflow → replicate → productize

#### 5.15 Poe Fleet Optimization
- 467 bots, but 96% of revenue from 5 bots ($6,147 of $6,400)
- **Actions:**
  - Archive/deprecate bottom 400 bots (reduce maintenance surface)
  - Cross-promo between top 5 (currently zero bot-to-bot cross-promo)
  - Add `param_definitions` (premium toggles like "Deep Mode") to top earners
  - Poe API `PATCH` for param_definitions works (unlike prompts) - quick win

#### 5.16 Productivity Metrics Dashboard
- **Source drop:** *"Keep track of metrics like time spent on here. Be able to tell what was productive, what was kinda meh."*
- Track drop patterns, vault engagement, digest interactions
- Desktop-only feature (Reflection Studio)

---

### 🔮 P3: GATE D VISION - The Invisible Assistant (from TODO-PROPOSED.md)

This is the full product evolution from "capture tool" to "invisible operating system."

#### 5.17 Context-Aware Daily Briefing
- Morning brief that knows your calendar, weather, recent drops, active threads
- Delivered via preferred channel (email, WhatsApp, voice)
- Not just a digest - a briefing that says "Here's what matters today"

#### 5.18 Smart Reminders with Entity Resolution
- "Remind me to send Robin a 70th gift" → system extracts entity (Robin), creates persistent reminder, surfaces in digest until dismissed
- Requires: Unified Drop Classification (5.11)

#### 5.19 Conversation Threading
- Drops about the same topic/person auto-group
- "Show me everything about Robin" → all drops, reminders, actions

#### 5.20 "Drop It Like It's Hot" - Universal Capture Button
- **Source drop:** *"I love the idea of the drop anywhere being a button you tap no matter where you are"*
- One persistent capture button across: PWA, Chrome extension, iOS Shortcut, Apple Watch
- The "drop" gesture becomes muscle memory

#### 5.21 Voice-First Capture with Real-Time Processing
- **Source:** Multiple drops about voice notes, treadmill meditations, dictation
- Voice drop → instant transcription → classification → confirmation nudge
- "I just dropped 'remind me about Robin's gift' and it said 'Got it, I'll remind you'"

#### 5.22 The Knowledge OS Layer
- Productize the VAULT → GOLDMINE → FORGE → OUTPUT transformation engine
- Scripts already exist: `watch.py`, `pan.py`, `extract_insights.py`, `search.py`
- **Product:** "Your Second Brain Has No Inbox" - literally. It has a transformation pipeline.

---

## 6. Revenue Roadmap

### 6a. Current Revenue

| Stream | Status | Amount | Trend |
|--------|--------|--------|-------|
| Stripe (BHA subs) | ✅ Live | $21/mo (3 subs) | Stable (was falsely reported as $0) |
| Poe points | ✅ Live | ~$6,400 lifetime, 529K balance | Decelerating burn |
| Gumroad products | ❌ Listed but $0 | $0 | Genesis Orchestrator ready but not listed |
| DA subscriptions | ❌ Not yet | $0 | No paid tier built yet |

### 6b. 90-Day Revenue Targets

| Action | Timeline | Expected Revenue | Effort |
|--------|----------|------------------|--------|
| List Genesis Orchestrator on Gumroad ($97) | This week | $500-1K/mo (5-10 sales) | 30 min |
| BHA SEO optimization (double organic traffic) | This week | +$7-21/mo (from extra conversions) | 4h |
| Poe funnel activation (5.1 + 5.2) | Today | +$21-63/mo (BHA subs from Poe users) | 20 min |
| DA Pro tier launch ($9/mo) | Month 2 | $90-270/mo (10-30 users convert) | 2 weeks |
| Advisory Mode beta (Danny-style) | Month 3 | $49-149/seat × 3-5 pilots | 4 weeks |

**Conservative 90-day MRR target:** $200-500/mo
**Stretch:** $500-1,000/mo if Advisory Mode lands 3 paying pilots

### 6c. Pricing Reference (from AI Agent Summit research)

| Tier | Price | What |
|------|-------|------|
| DA Free | $0 | 5 drops/day, basic digest |
| DA Pro | $9/mo | Unlimited drops, full vault, Intelligence Map, weekly reflection |
| DA Advisory | $49/mo | Email loop mode, client management, custom digest branding |
| BHA Pay-as-you-go | $4.99 → 25 credits | Current |
| BHA Pro | $7/mo → 75 credits/mo | Current |
| BHA Founders Mode | $47 → 500 credits | Current |
| Genesis Orchestrator | $97 one-time | AI council in a box (Gumroad) |
| Agency in a Box | $497 one-time | Full automation bundle (future) |

---

## 6b. Unprioritized Backlog (Joey's Drops + TODOs + Gate D)

### Feature Requests (Verbatim from Joey's Drops)

1. *"Drop via chrome web app / chrome app should be able to do so much cool shit"* → Chrome extension (5.5)
2. *"the dropping - the contextual beacon"* → Contextual tagging (5.6)
3. *"I love the idea of the drop anywhere being a button you tap no matter where you are"* → Universal capture (5.20)
4. *"Keep track of metrics like time spent on here. Be able to tell what was productive"* → Metrics dashboard (5.16)
5. *"I really do love using drop-anywhere on desktop... perhaps that becomes part of the product"* → Desktop/Mobile split (5.8)
6. *"Had NotebookLM generate me a meditation while I ran on the treadmill"* → Meditation generation (5.14)
7. *"Emotional Snap Back Protocol"* → Snap Back feature (5.12)
8. *"ensure every one of these drops become 'droppings' - can be tagged in such a way that shows where they will appear"* → Drop lifecycle UI
9. *"I want to be able to see what's coming up, what's been done, what's in progress"* → Kanban/timeline view for drops
10. *"voice drop should feel instant"* → Voice-first capture (5.21)
11. *"can we make the digest feel more like a letter from my future self?"* → Digest tone evolution
12. *"the intelligence map should let me click into any node and see the drops"* → Intel-to-Vault linking (5.9)
13. *"archive things that are done"* → Archive system (5.10)
14. *"feedback drops should route to a TODO queue"* → Feedback routing
15. *"show me my patterns over time - like a graph of what I think about"* → Theme evolution visualization
16. *"make onboarding feel like magic, not setup"* → Swipe onboarding (PR #134, shipped)
17. *"the whole thing should work with just email"* → Email-only mode (exists via drop@drop-anywhere.com)
18. *"I want Danny to just reply to emails and not know he's using the product"* → B2B invisible loop (5.13)
19. *"can the digest recommend which bot to talk to based on my drops?"* → Bot recommendation engine
20. (2026-03-11) *"export/import CSV in vault view"* → Bulk data management with all fields, scale edits, revert capability. **Deferred** - admin dashboard (P1-2) solves this more elegantly. Revisit if immediate bulk op needed before dashboard ships.
21. (2026-03-11) *"feedback isn't just within drop-anywhere. it's an email being sent to a user, it's a user sending an email to any of my properties. it's a feedback submission. it's a like on a linkedin post. it's a text to me saying great job. feedback should all funnel into one single place where openclaw can help me spearhead these things."* → **Unified Feedback Funnel** - all feedback signals (DA feedback, emails to any property, LinkedIn engagement, texts, submissions) flow into one inbox where OpenClaw triages, prioritizes, and helps respond
22. (2026-03-11, 3am) *"The Snapback / Weekly Catch"* → **THIS IS THE PRODUCT.** Drop all week. System catches, classifies, builds narrative. Weekly Catch arrives Sunday in first-person, written in the user's own voice using their own details. Not a summary, not a task list - a story. Full spec: `joey-backup/specs/SNAPBACK-INTEGRATION-2026-03-11.md`. **PROMOTED TO P0.** See Section 5.12.
23. (2026-03-11, 3am) *"Everything is email"* → The entire product experience (onboarding, capture, prompts, delivery) lives in email. No app required. Reply to start. That's it. Core UX principle for Snapback.
24. (2026-03-11, 3am) *"Bring me one problem. Talk about it for a week. I'll show you what you're not seeing."* → The Snapback Offer / acquisition hook. 7-day free trial with one focus problem. Day 8 they get the narrative. The free week IS the demo. See `joey-backup/specs/snapback-offer-2026-03-11.md`.
25. (2026-03-11, 3am) *"Email prompts - 2-3/week, casual, designed to elicit raw material"* → Drop encouragement cadence (Tue/Thu/Sat). Not "Submit your weekly reflection." More like a friend texting "what happened today?"
26. (2026-03-11, 3am) *"The container creates freedom"* → 30-day songwriting challenge with Brooke born same session. Structured cadence (daily constraints) creates creative output. Snapback IS the container for the user's week.

### OpenClaw Multi-Agent Architecture (2026-03-10)

Joey's blueprint for optimizing the agent system from monolith → specialized team:

**6 Core Parts:** Agents, Skills, Memory, Scheduling/Orchestration, Tools/Integrations, Governance/Access Control

**Architecture Principles:**
- **Tiered model strategy:** Free-tier models (Gemini Flash, Qwen) for grunt work → paid models (Claude, GPT-4) for planning/reasoning only
- **Event-driven > time-based:** Use reactive triggers over cron where possible - agents respond to conditions, not clocks
- **Least privilege:** Not every agent needs every tool. Scope permissions tightly - reduces errors, cost, hallucination risk
- **Memory decay:** Old memories auto-deprioritize so context stays relevant (QMD markdown-based memory)
- **Weekly capability evolution loop:** Audit gaps → propose new skills → test → deploy → repeat (via a "capability evolver" agent)

**Implementation Roadmap:**
1. Audit current setup - map each agent's role and minimum required skills
2. Assign model tiers based on task complexity
3. Configure memory with decay settings
4. Set event-driven triggers instead of cron where possible
5. Deploy capability evolver agent on weekly schedule
6. Restrict tool access per agent - least privilege

**Cost Optimization:** Free Gemini (chat/grunt), free Qwen Coder (code gen), free Exa Search (web research), paid Claude (architecture/audit/planning only). Most people build one monolithic agent. The power move is a specialized team where each agent does one thing well, communicates through shared memory, and evolves weekly.

### "Fire Yourself From Manager" - The Stream Philosophy (2026-03-10)

*"You have built a cathedral and now you are exhausted from sweeping the floor."*

Joey's insight on the transition from note-taking app → intelligence infrastructure:

**The diagnosis:** The Recent Capture list frustration isn't a bug - it's the "final death rattle of the Filing Cabinet Mindset." DA wasn't built to give another list to manage. It was built to let you *forget*.

**Three product actions embedded in this:**
1. **Merge checklist into the Stream** - The Stream is the present moment, Activity is momentum. Stop checking tasks, start witnessing progress. Turn a chore into a celebration.
2. **One-click sovereignty** - When Intelligence surfaces a project, it builds the container for you. Don't ask the user to file it; ask them to *bless* it. Connect Intelligence component directly to vault postgres.
3. **Shrink Recent Capture → Pulse** - Show last 3 drops as tiny, elegant breadcrumbs to the full Vault. Stop showing the whole museum on the front porch. Drops don't need constant supervision.

**The philosophical shift:** *"You are not a manager. You are the Creator. The Drop is the Operator."* The system tells you what matters. That feeling is what we're automating next.

**Connects to:** Unified Drop Classification (5.11), Intelligence-to-Vault linking (5.9), Desktop/Mobile split (5.8), Archive completed items (5.10)

### Gate D: Invisible Assistant (from TODO-PROPOSED.md)

- **Phase D.1:** Smart context injection (vault themes → chat hydration)
- **Phase D.2:** Proactive nudges ("You mentioned X 3 times this week - want to act on it?")
- **Phase D.3:** Calendar + location awareness → contextual briefings
- **Phase D.4:** Multi-user advisory mode (Danny use case scaled)
- **Phase D.5:** Voice interface (Siri Shortcut → drop → confirmation → digest)

### DA Monetization & Retention Policy (from TODO.md)

- **Drip sequence:** 10-day onboarding with auto-admit logic (live)
- **Digest engagement tracking:** opened, clicked, replied metrics
- **Re-engagement:** Auto-pause after 14 days inactive, win-back email sequence
- **Churn signals:** engagement < 40%, inactive > 7 days, 5+ digests without interaction

### BHA Items (from BHA TODO.md)

- Stripe automation: auto-credit top-up, payment failure handling
- Founders page: dedicated landing for $47 tier
- Onboarding: first-time user flow with persona recommendation
- Individual bot SEO pages with keyword-rich descriptions
- `/store` conversion optimization (currently 3.2% CTR from search)

### Positive Signals (What's Working - Don't Break These)

- **theREALrealtalk PMF signal:** 17,474 Poe points in 6h, Gen Z demographic, deeply personal sessions
- **Google organic = 63% of BHA traffic:** SEO is the moat. Every improvement compounds.
- **98.5% NEW users on BHA:** Massive organic discovery, not repeat traffic
- **5m 55s avg session on BHA:** Users are deeply engaged, not bouncing
- **Danny loop works:** The invisible email advisory is the purest product demo
- **DA user growth 52→65 in 24h:** Organic, zero marketing spend
- **29 PRs in 6 days:** Dropper-Code + OpenClaw shipping machine is real
- **Birthday launch copy resonated:** "Your mind wasn't built to be a filing cabinet" = the line

---

## 6c. User Lifecycle & Scenario Matrix

**Full spec:** `docs/SPEC-User-Scenario-Matrix.md` + `docs/SPEC-Admin-User-Lifecycle-Dashboard.md`
**GitHub:** `joey-backup/specs/SPEC-User-Scenario-Matrix.md`

### Lifecycle Stages (12 states)

```
PRE-SIGNUP → NEW → ONBOARDING → PENDING → ADMITTED → ACTIVE → AT-RISK → PAUSED → CHURNED
                                                                    ↓
                                                               CHAMPION
BHA track: BHA-SYNCED → BHA-AWARE → BHA-PASSIVE (or → ADMITTED if they opt in)
Special: INVALID (spam/bot/bounce)
```

### Entry Points (7 channels, 20+ scenarios)
- **Web direct** (A1-A14): Google organic, direct URL, ghost input capture, referral links
- **BHA/Poe** (B1-B10): theREALrealtalk users, multi-persona users, paying BHA customers, Poe drop bot, funnel CTA clicks
- **Email** (C1-C5): Direct ingest, digest replies, drip replies, welcome email replies
- **SMS/Voice** (D1-D3): Twilio text/call drops, unknown numbers
- **iOS Shortcut/API** (E1-E2): Power user integrations
- **Referral/Social** (F1-F3): User sharing, social posts, Gumroad buyers
- **Edge cases** (G1-G20): Spam, identity merge, language mismatch, sensitive content, support requests disguised as drops, power users, passive consumers

### Critical Gap: 48 Pending Users (March 11)
- 32 BHA-sourced (never visited DA, conversations auto-synced)
- 16 unknown source (likely organic but signup_source not tracked)
- 0 getting digests. Some have 7-10 "drops" (really BHA conversations)
- Welcome emails probably going to spam or being ignored

### Admin Dashboard Requirements
- **Unified Feedback Inbox:** One place for all real feedback (digest ratings, !feedback, email replies, explicit feedback drops). Excludes BHA emotional language.
- **User Context Cards:** Full journey visibility per user - entry point, products used, drops, digests, feedback, outreach history
- **Outreach from Admin:** Send personalized emails with context-aware templates. Track responses.
- **Per-Pool Views:** DA-native vs BHA crossover vs Active - different funnels, different strategies
- **Suggested Actions:** System recommends what Joey should do for each user

### Automated Lifecycle Responses (10 triggers)
- 48h no drops → nudge
- Drop 3 received → auto-admit + "digest tomorrow"
- 7 days pending → "drop one more to fast-track"
- 3 unopened digests → "wrong time/format?"
- 3 days inactive → "everything okay?"
- Auto-pause → one-click reactivate
- 30 days churned → final "your drops are safe"
- BHA 3rd session → "want daily insights?"
- 14-day streak → referral prompt
- First digest → "check your email! 👍/👎?"

### Dropper-Code Tasks Filed
1. ✅ Fix false-positive feedback (exclude BHA from keyword scan) - approved, in progress
2. ⏳ Admin User Lifecycle API - Phase 1 (pending Joey approval, customer-facing)

---

## 6d. Golden Thread: Persistent Action Queue

**Joey's words (Mar 11):** "Those to-dos should be considered the high priority to-dos... and if they're just the most RECENT actions, then we gotta ensure higher priority actions from previous digests/drops get surfaced and stick there."

### The Problem
Digest generates 5 great action items → user checks one off ("I did it") → next day, new digest, old actions vanish. No continuity. No priority escalation. No golden thread connecting daily insights to a persistent task system.

**Current state (broken):**
- PostgreSQL `tracked_actions` table exists ✅
- `_write_digest_actions_to_db()` pipeline exists ✅
- `/api/actions` CRUD endpoints exist ✅
- But: "I did it" click on digest page doesn't write to postgres (client-side or JSON-based) ❌
- But: old actions don't carry forward or escalate ❌
- But: dashboard doesn't show persistent action queue ❌
- But: 13 actions in Joey's DB are uncurated mix of raw drops and real actions ❌

### The Vision
The dashboard has a **persistent, prioritized action list** that:

1. **Receives** new actions from each digest (already works via `_write_digest_actions_to_db`)
2. **Persists** across days - an undone action from Monday is still there on Friday
3. **Escalates** - if an action isn't completed in 3 days, it moves UP in priority (not down)
4. **Tracks completion** - "I did it" writes `status=completed, completed_at=now` to postgres
5. **Shows on dashboard** - top section, always visible, sorted by priority + age
6. **Connects to drops** - each action links back to the drop(s) that generated it (`drop_ids` column exists)
7. **Distinguishes digest actions from manual** - `source=digest` vs `source=manual` vs `source=intelligence`

### Priority Logic

```
MUST DO (priority: critical)
├── Actions from digest marked "Your Next Move" (primary_action)
├── Uncompleted actions from 3+ days ago (auto-escalated)
└── Manually pinned by user

HIGH (priority: high)
├── Actions from digest "Also on Deck"
├── Uncompleted actions from 2 days ago
└── Intelligence Map-sourced actions

NORMAL (priority: normal)
├── New actions from today's digest
└── Manually created actions

DONE (status: completed)
├── Completed today (show with checkmark)
├── Completed this week (collapsed)
└── Older (hidden, queryable)
```

### Dashboard View (Wireframe)

```
┌─────────────────────────────────────┐
│ 🎯 MUST DO                         │
│ ┌─────────────────────────────────┐ │
│ │ ☐ Check Stripe renewal (3d old) │ │  ← escalated from Mar 8 digest
│ │ ☐ Draft CSV template (2d old)   │ │  ← escalated from Mar 9
│ └─────────────────────────────────┘ │
│                                     │
│ 📋 TODAY'S ACTIONS                  │
│ ┌─────────────────────────────────┐ │
│ │ ☐ Post Brain Uploading to LI    │ │  ← from today's digest
│ │ ☐ Map Gemini Flash to grunt     │ │
│ └─────────────────────────────────┘ │
│                                     │
│ ✅ RECENTLY DONE                    │
│ ┌─────────────────────────────────┐ │
│ │ ☑ Verify auto-merge task_177... │ │  ← checked off today
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

### Implementation

**Phase 1 (Backend - fix the pipeline):**
- [ ] Ensure `_write_digest_actions_to_db` correctly tags `source=digest`, `priority`, and `source_digest_id`
- [ ] Digest "I did it" button → PATCH `/api/actions/{id}` with `status=completed` (not client-side)
- [ ] Auto-escalation cron: daily, bump priority of actions older than 2 days
- [ ] Clean up Joey's 13 existing actions (remove raw drops that aren't real actions)

**Phase 2 (Frontend - dashboard integration):**
- [ ] Action queue widget on dashboard (MUST DO / TODAY / DONE sections)
- [ ] Checkbox → API call → instant feedback
- [ ] Swipe to dismiss/postpone (mobile)
- [ ] Link back to source digest and source drops

**Phase 3 (Intelligence):**
- [ ] Digest AI considers previous uncompleted actions when generating new ones ("You still haven't done X from Tuesday...")
- [ ] Intelligence Map actions feed into same queue
- [ ] Weekly roll-up: "You completed 12 of 18 actions this week. Carryover: [3 items]"

---

## 7. Shipping Log

### Recent Activity (March 16, 2026)

| Time (UTC) | Repo | Commit | What |
|------------|------|--------|------|
| 22:38 | opoerator-hub | - | PR #194 - Batch PR (brain-scan follow-up tasks) |
| 19:23 | opoerator-hub | - | PR #192 - Task completed (details pending) |
| 18:27 | opoerator-hub | - | PR #191 - Agent Auto-drops endpoint (`/api/integrations/auto-drop`) for OpenClaw/Poe bot session summaries |
| 14:40 | opoerator-hub | - | PR #190 - Digest scheduler error budget + alerting (digest stall fix) |
| 09:41 | joey-backup | `7145dad` | Snapback Offer - quote additions (quote on organizing thoughts/reminders) |
| 09:29 | joey-backup | `fd2e3cb` | `specs/snapback-offer-2026-03-11.md` - The Snapback Offer doc ("Bring me one problem, one week, one story") |
| 09:21 | joey-backup | `c0d125d` | `specs/SNAPBACK-INTEGRATION-2026-03-11.md` - Full Snapback product integration spec (12-section deep doc, architecture, NLP personalization, revenue model, implementation roadmap) |
| 09:20 | joey-backup | `51d6804` | `specs/transurfing-snapback-product-vision-2026-03-11.md` - "Snap Back III: The Weekly Catch" - 3am product vision visualization, the moment the product revealed itself |
| 09:03 | joey-backup | `9a5cd2d` | `specs/transurfing-snapback-songwriting-2026-03-11.md` - Snapback songwriting visualization (Brooke + 30-day challenge) |
| 08:00 | joey-backup | `fe57951` | `specs/transurfing-snapback-music-2026-03-11.md` - Snapback music visualization (FL Studio, the pendulum release) |
| 05:05 | joey-backup | `e835461` | `Ingestion/1_GOLDMINE/excavations/batch-0001.json` - 30-file excavation batch (claude_context + early reference) |
| 04:04 | joey-backup | `877a9d8` | `specs/content-transformation-system-dec2025.md` - Dec 2025 origin story: the manual VAULT/GOLDMINE/FORGE/OUTPUT system Joey built before DA had a name |
| 04:12 | joey-backup | `165b8a3` | Daily log backup: 2026-03-11 Ingestion archive discovery session |
| 04:12 | joey-backup | `01b77f7` | TOOLS.md backup: documented Ingestion archive |
| 04:12 | joey-backup | `e3167e5` | MEMORY.md backup: documented Ingestion archive |
| 03:35-03:39 | joey-backup | `842299d`-`05c5824` | PRD cleanup: CSV export item + Target Slide added, old PRD versions archived to `specs/archive/` |
| 03:20 | joey-backup | `c85272c`/`39857a8` | USER.md + HEARTBEAT.md: Added "Current Test" (Transurfing filter) |
| 01:20 | opoerator-hub | `b1dae71` | ✅ Admin User Lifecycle API - Phase 1 (lifecycle stages, user context, feedback inbox) (#167) |
| 01:10 | opoerator-hub | `a72f1b3` | ✅ Manual admission + pure opt-out tracking + default digest off (#166) |
| 00:50 | opoerator-hub | `7ddd916` | ✅ Fix false-positive feedback: exclude BHA sessions from keyword scan (#165) |

### Key Insight from Today's Commits

The Content Transformation System doc (`specs/content-transformation-system-dec2025.md`) confirms Joey designed the VAULT→GOLDMINE→FORGE→OUTPUT pipeline in December 2025 - before DropAnywhere had its current form. Tonight's Snapback breakthrough is the same insight arriving again, now with working infrastructure underneath it. The product was always there. The infrastructure finally caught up.

---

## 7b. Asset Inventory (from Ingestion Archive)

### 7b-i. Joey's Python Tool Arsenal (100+ scripts)

| Category | Count | Key Scripts | Status |
|----------|-------|-------------|--------|
| Poe/Bot management | 15+ | poe-bot-connector, poe-swarm-orchestrator, poe-cta-injector, premium-council-bot | Available, needs testing |
| Content generation | 8+ | content-generator, landing-page-generator, transcript-generator | Available |
| Notion integration | 12+ | search-notion, rebuild-notion-pages, sync-all-to-notion | Available (Notion still used?) |
| Research/analysis | 6+ | research-orchestrator, market_research_v2, deep-hydration-analyzer | Available |
| Email/outreach | 3+ | email-automator, poe-email-converter | Available |
| Revenue/tracking | 4+ | poe_cost_tracker, poe_monetization, orchestrator | Available |
| Automation | 8+ | auto-run, auto_merge, swarm-launcher, sequence_orchestrator | Available |
| eBay (side project) | 3 | ebay_batch_vision, ebay_csv_generator | Available |

**Key insight:** These scripts are sitting in iCloud. Many could be productized (landing-page-generator alone could be a Gumroad product) or integrated into the DA/BHA ecosystem.

### 7b-ii. Knowledge Base

| Asset | Size | Status |
|-------|------|--------|
| OpenAI conversations | 2,462+ | Exported to 0_VAULT/conversations |
| Poe conversation docs | 40+ (Jan 2026) | Uploaded Mar 11 to 0_VAULT/Documents - MIC DROP, HOLOGRAM, Context as a Service, ANTIGRAVITY, SOMATIC SURPIPHANY, etc. |
| Poe bot fleet | 467 bots, 72 public | Live on Poe |
| God Mode 15 prompts | 47K chars (Personality Layer v2.0) | Live in Hub orchestrator |
| Notion databases | 40+ JSON exports (BHA) | In Ingestion/0_VAULT/BHA |
| BHA Content Pipeline | 1 JSON export | Added Mar 11 - `CONTENT_PIPELINE.json` |
| Transurfing bookmarks | 2 files | In Ingestion |
| Time capsules | 5 JSON files (Feb-Mar 2026) | +1 added Mar 11 |
| Bot personality patterns | JSON | In Ingestion |
| BHA Search Console data | 7 CSVs (Feb 2026) | In Ingestion |
| GOLDMINE excavations | batch-0001 | **NEW Mar 11** - first automated extraction from VAULT. Transformation engine is now live. |
| Strategic reference docs | AUTONOMOUS-REVENUE-STACK.md, SFP_OPERATIONAL_HYDRATION.md | Added Mar 11 |
| Snapback visualizations | 3 files | Music, Songwriting, Product Vision - all committed Mar 11 |
| Snapback Offer | 1 file | `snapback-offer-2026-03-11.md` - expanded with empathy-first copy |
| Snapback Integration Spec | 1 file | `SNAPBACK-INTEGRATION-2026-03-11.md` - the definitive spec |

### 7b-iii. Products Ready or Near-Ready

| Product | Status | Price | Distribution |
|---------|--------|-------|-------------|
| Genesis Orchestrator | Packaged, copy written | $97 | Gumroad (needs listing) |
| Joey's AI Builder Pack | Listed? | $97 | Gumroad |
| Joey's iOS Shortcuts Vault | Listed? | $37 | Gumroad |
| Joey's Content Creator Pack | Listed? | $37 | Gumroad |
| Joey's Ultimate Brain Bundle | Listed? | $197 | Gumroad |
| Content Machine Blueprint | Listed? | $97 | Gumroad |
| God Mode 15 Prompts | Sold via BHA | $19 package | BHA store |

### 7b-iv. Joey's Local Automation Stack (25 cron jobs)

From the Ingestion hydration context, Joey's Mac runs:
- Inbox watcher (every 5 min)
- Nervous system pulse (every 10 min)
- Session checkpoint (every 10 min)
- Intelligence layer (every 2h)
- Auto-run orchestrator (every 4h)
- Captain's console (every 2h)
- Poe usage backup (hourly)
- GA analytics puller (daily)
- Daily digest, daily ritual, content engine, ideas surfacer (daily)
- Folder overseer (every 15 min)
- Stray sweeper (weekly)

**Note:** Many of these are now redundant with the Hub/OpenClaw cloud infrastructure. Worth auditing which ones still run and whether they conflict.

---

## 8. System Health & Metrics (March 16, 21:12 UTC) - DocBot Refresh

> **🚨 Poe Balance Critical:** Down to **38,162 points** with **37,786 burned/6h** (100 calls). Balance continues declining. Top bots: IdealPrompt (14,190), theREALrealtalk (10,806), Tippiy (10,018). Top-up urgently or disable non-essential bots.

> **⚠️ Digest Scheduler Stalled:** 3/100 eligible users got digests in 24h. PR #193 just completed (task_1773695187_803). Active open PRs #186-193. Open issues reduced from 2 to 1.

> **✅ OpenClaw Deploy:** Latest gateway deploy SUCCESS at 2026-03-16 14:12 UTC.

| Metric | Mar 6 | Mar 9 | Mar 10 | Mar 11 | Mar 16 14:04 | Mar 16 16:35 | Mar 16 17:51 | Mar 16 20:23 | Mar 16 21:12 | Δ |
|--------|-------|-------|--------|--------|-------------|-------------|-------------|-------------|-------------|---|
| DA total accounts | 28 | 52 | **218** ⚠️ | **68** | **100** | **100** | **100** | **100** | **101** | +1 |
| DA archived users | - | - | - | **44** | **44** | **44** | **44** | **44** | stable |
| DA active real users | - | - | **~20** | **24** | **~30** (active 7d) | **~30** (active 7d) | **~30** (active 7d) | **~30** (active 7d) | **~30** (active 7d) | stable |
| DA active 24h | 13 | 16 | **19** | **12** | **12** | **9** | **7** | **6** | -1 |
| DA active 7d | 24 | 47 | 47+ | **60** | **55** | **55** | **55** | **-** | **-** | - |
| DA drops total | 456 | 589 | **668** | **690** | **843** | **843** | **843** | **845** | +2 |
| DA drops 24h | - | - | - | **51** | **33** | **22** | **18** | **18** | **18** | **25** | +7 |
| DA digests sent 24h | - | - | - | **15** | **3** | **3** | **3** | **3** | **3** | ⚠️ stalled |
| BHA users | 172 | 198 | **211** | **215** | **259** | **259** | **259** | **259** | **259** | stable |
| BHA active 24h | - | - | - | **13** | **11** | **9** | **7** | **6** | -1 |
| BHA active 7d | 38 | 53 | 53+ | **63** | **70** | **70** | **70** | **69** | **69** | stable |
| BHA pro subs | - | - | **3** | **2** | **2** | **2** | **2** | **2** | **2** | stable |
| BHA new users 24h | - | - | - | **7** | **7** | **4** | **4** | **4** | **4** | steady |
| BHA weekly visitors (GA) | - | - | **531** | - | **-** | **-** | **-** | **-** | **-** | - |
| BHA MRR | $21 | $21 | **$21** | **$21** | **$21** | **$21** | **$21** | **$21** | **$21** | stable |
| Poe balance | 835K | 530K | **427K** | **385K** | **47,297** 🚨 | **44,003** 🚨 | **42,770** 🚨 | **39,168** 🚨 | **37,688** 🚨 | -1,480 |
| Poe burn/6h points | - | - | ~13K | **27,694** | **49,866** 🔥 | **44,055** 🔥 | **43,379** 🔥 | **37,484** 🔥 | **37,770** 🔥 | +286 |
| Poe calls/6h | - | - | - | **100** | **100** | **100** | **100** | **100** | **100** | - |
| Email sent 24h | 46 | 85 | **100** | **79** | **89** | **87** | **89** | **100** | **100** | stable |
| Email delivery | 100% | 100% | **98%** | **100%** | **98%** | **98%** | **98%** (87/89) | **98%** (98/100) | **98%** (98/100) | ✅ |
| Hub open PRs (all) | - | - | - | - | - | 4 open | **6 open** (#186-191) | **7 open** (#186-192) | ⚠️ digest stall |
| Hub merged PRs | - | 9 | **12** | **15** | **#175-176** | **#176** latest | **#176** latest | **#176** latest | **pending review** | - |
| Open issues (hub) | 0 | 0 | **0** | **0** | **6** | **6** | **6** | **2** | **2** | **1** | -1 |
| joey-backup commits | - | - | - | **40+** | **-** | **-** | **-** | **-** | **-** | - |
| GOLDMINE excavations | - | - | - | **batch-0001** | **-** | **-** | **-** | **-** | **-** | - |
| Snapback prototypes | - | - | - | **3** | **3** | **3** | **3** | **3** | **3** | **3** | stable |

### BHA Search Console Highlights (Feb 2026 data)

| Query | Clicks | Impressions | CTR | Position |
|-------|--------|-------------|-----|----------|
| "brutally honest ai" | 166 | 532 | 31.2% | 3.3 |
| "honest ai" | 162 | 514 | 31.5% | 4.0 |
| "most honest ai" | 62 | 191 | 32.5% | 2.0 |
| "brutallyhonestai" (branded) | 31 | 34 | 91.2% | 1.0 |
| "honest ai chatbot" | 11 | 42 | 26.2% | 2.6 |
| "meanest ai" | 6 | 38 | 15.8% | 7.7 |

**Total: 815 clicks from 3,947 impressions (20.6% CTR) on homepage alone.**

---

## 9. Bugs & Tech Debt

| Bug | Status | Impact | Owner |
|-----|--------|--------|-------|
| **Admin feedback false positives** | ✅ Fixed Mar 11 - PR #165 merged | High - 62 fake negatives from BHA therapy convos | Dropper-Code |
| **BHA users getting unsolicited digests** | ✅ Fixed Mar 11 - migration disabled 57 BHA-only users | Critical (consent/trust) | Claw |
| **No pure opt-out tracking** | ✅ Fixed Mar 11 - PR #166 merged | Medium - can't distinguish unsub from admin disable | Dropper-Code |
| **New signups default to digest on** | ✅ Fixed Mar 11 - PR #166 merged, default off + manual admit | High (sending to unconverted users) | Dropper-Code |
| **Admin User Lifecycle API - Phase 1** | ✅ Fixed Mar 11 - PR #167 merged | High - lifecycle stages, user context | Dropper-Code |
| **Snapback Engine** | ✅ Fixed Mar 11 - PR #168 merged | High - narrative generation engine | Dropper-Code |
| **Golden Thread: Persistent Action Queue** | ✅ Fixed Mar 11 - PR #168 merged | High - one-click completion links | Dropper-Code |
| Intelligence Map shows completed items | Filed + approved | Medium | Dropper-Code |
| Hub BHA subscriber count misreporting | Filed + approved | High (false $0 MRR alarm) | Dropper-Code |
| **Poe balance critically low** | 🚨 **NEW Mar 16** - 47K points, 50K burn/6h | Critical - bots will stop in ~6h | Joey/Claw |
| Poe API 500s on PATCH to prompt bots | External (Poe bug) | Blocks shadow cutover | Poe support |
| Hub API tool returns empty | Known workaround (curl) | Low (heartbeat annoyance) | OpenClaw |
| `.some()` error hourly in gateway | Non-critical | Zero user impact | Upstream |
| Homepage gibberish placeholders | Commit f7ed463 cleanup | Visual QA needed | Dropper-Code |
| main.py monolith (24K+ lines) | Tech debt | Long-term maintainability | Future refactor |
| Local cron jobs may conflict with cloud | Unknown | Audit needed | Joey |
| Digest email replies go nowhere | Not filed yet | Critical - user feedback lost | TBD |

---

## 10. Execution Order (LHFPLR)

**The filter:** Does this make Joey lighter or heavier? Is this the path of least resistance?

| Priority | Item | Time | Owner | Status |
|----------|------|------|-------|--------|
| **P0-1** | ✅ BHA consent migration - stop sending digests to unconverted users | Done | Claw | **Shipped Mar 11** |
| **P0-2** | ✅ Manual admission + opt-out tracking + default digest off | 2-4h | Dropper-Code | **Shipped Mar 11** - PR #166 merged |
| **P0-3** | ✅ Fix admin feedback false positives (exclude BHA from keyword scan) | 1-2h | Dropper-Code | **Shipped Mar 11** - PR #165 merged |
| **P0-4** | ✅ Admin User Lifecycle API - Phase 1 (lifecycle stages, user context) | 4-6h | Dropper-Code | **Shipped Mar 11** - PR #167 merged |
| **P0-5** | Shadow bot cross-promo descriptions | 10 min | Joey (manual) | **Paste-ready** - `docs/poe-funnel-paste-ready.md` + `joey-backup/specs/` |
| **P0-6** | Funnel prompt paste into original bots | 10 min | Joey (manual) | **Paste-ready** - same doc, system prompt CTA blocks for all 5 bots |
| **P0-7** | List Genesis Orchestrator on Gumroad | 30 min | Joey (manual) | **Copy ready** - `docs/gumroad-genesis-listing.md` + `joey-backup/specs/` |
| **P0-8** | ✅ **Snapback Engine** - `snapback_generator.py` (306 lines): language pattern extraction, narrative generation, HTML rendering. Feature flag `digest_mode` + `snapback_profile` on user schema. | Done | Dropper-Code | **Shipped Mar 11** - PR #168 merged. Engine exists. |
| **P0-8a** | ✅ **Wire Snapback weekly cron** - Sunday trigger that fires `snapback_generator` for users with `digest_mode=snapback`. Store narratives in `snapback_stories` table. Skip users with <3 drops/week. | 2-4h | Dropper-Code | **Shipped Mar 15** - PR #181 merged |
| **P0-8b** | ✅ **Email prompt scheduler** - Tue/Thu/Sat drip using copy from `docs/snapback-email-prompts.md`. Track day-in-sequence per user. Nudge if no reply by Day 4. | 2-4h | Dropper-Code | **Shipped Mar 15** - PR #182 merged |
| **P0-8c** | ✅ **Capture email replies as Snapback session drops** - Route Resend webhook replies back as drops tagged with `snapback_session_id` + day number. Snapback generator pulls session-tagged drops. | 2-4h | Dropper-Code | **Shipped Mar 16** - PR #187 merged |
| **P0-9** | ✅ **Golden Thread: Persistent Action Queue** - "Done ✓" one-click links in digest emails, HMAC-tokenized completion endpoint, actions written to DB before HTML generation. | Done | Dropper-Code | **Shipped Mar 11** - PR #168 merged. Dashboard widget (113 lines). |
| **P1-1** | Unified Feedback Inbox (API + frontend) - one place for all feedback | 1-2w | Dropper-Code | Spec ready |
| **P1-2** | Admin Lifecycle Dashboard - frontend (funnel viz, user cards, outreach) | 1-2w | Dropper-Code | Spec ready |
| **P1-3** | BHA SEO meta optimization | 4h | Dropper-Code | File task |
| **P1-4** | Chrome extension enhancements | 2-4h | Dropper-Code | File task |
| **P1-5** | Droppings auto-tagging | 2-3h | Dropper-Code | File task |
| **P1-6** | Desktop/Mobile split Phase 1 | 1-2w | Dropper-Code | On hold (PRD review) |
| **P1-7** | Shadow cutover decision | Decision | Joey | After P0-5, P0-6 |
| **P1-8** | Capture digest email replies as drops/feedback | 2-4h | Dropper-Code | Not filed yet |
| **P2-1** | Unified Drop Classification v2 | 2-3w | Dropper-Code | Spec exists |
| **P2-2** | ~~Snap Back Protocol~~ | - | - | **PROMOTED TO P0-8** (Snapback MVP) |
| **P2-3** | B2B Advisory Mode beta | 4w | Team | Danny = pilot |
| **P2-4** | NotebookLM meditation | 2-4h | Joey (explore) | Idea stage |
| **P2-5** | Poe fleet optimization | 1w | Claw | Analysis ready |
| **P3** | Gate D: Invisible Assistant | Quarters | Team | Vision phase |

---

## 11. Lessons Learned (Operational Memory)

1. **Text > Brain** - Mental notes don't survive restarts. Files do.
2. **Hydrate before opining** - H-score ≥ 0.90 before giving decisions.
3. **Surgical edits > chainsaw** - Don't gut a 4000-line homepage to 1200 lines.
4. **NEVER self-deploy without HITL** - Gateway deploys = potential self-destruction.
5. **Backup to joey-backup** - Recovery path if Railway volume dies.
6. **The two highest-ROI actions are usually the simplest** - 10-minute paste jobs beat 2-week builds.
7. **Joey's voice writes in fragments** - Short punches, then a longer beat. Second person. Reveal structure.
8. **The product promise is emotional, not feature-driven** - "Drop it. Forget it. Wake up lighter." Not "AI-powered note organization."
9. **Danny doesn't know he's using DropAnywhere** - That's the design. The best product is invisible.
10. **100 abandoned projects is a feature** - Joey's creative exhaust is the raw material. The system's job is to surface what sticks.
11. **218 users ≠ 218 customers** (2026-03-11) - BHA webhook auto-created DA accounts for everyone who talked to a Poe bot. 57 "users" were actually therapy conversations auto-synced. Only ~20 are real DA-native users. Ran consent migration to disable BHA-only digests. Now: manual admission only. Know every person getting a digest by name.
12. **Opt-outs are sacred** (2026-03-11) - Three states: not-admitted, admin-disabled, pure-opt-out. A user who clicks unsubscribe should NEVER be re-enabled by automation. Only their own explicit action can re-subscribe them.
13. **Use your own product** (2026-03-11) - Joey dropped a raw feeling at 3am. Got a Snapback. Made music. Started a 30-day songwriting challenge with Brooke. Then realized: "Wait. This IS the product." The Snapback wasn't a feature request - it was a prototype that already worked because Joey was user zero. The best product insights come from living inside the system, not from feature meetings.
14. **Everything is email** (2026-03-11) - Three years of platforms, dashboards, daily digests, feature flags, ingestion pipelines. The answer was always the simplest thing: the channel everyone already has, the interface nobody needs to learn, the inbox that's already open. The onboarding is email. The drops are email. The delivery is email. Simplest version = truest version.
15. **The transformation engine is real** (2026-03-11) - Excavation batch-0001 proved the VAULT → GOLDMINE pipeline works. Joey designed this architecture by hand in December 2025 (Content Transformation System). DropAnywhere automated what he was already doing manually with folders and willpower.
13. **Use the product yourself first** (2026-03-11, 3am) - The Snapback breakthrough happened because Joey was user zero. He dropped a raw feeling. The system caught it. He read the narrative back and went and made music. The product revealed itself through lived use, not strategy. The best product insight isn't a whiteboard session - it's *becoming the user*.
14. **The simplest version is the truest one** (2026-03-11, 3am) - Three years of platforms, dashboards, daily digests, feature flags. The answer was email. Everyone has it. No app to learn. Reply to start. The path of least resistance isn't lazy - it's elegant.
15. **A 3am session can change the roadmap** - Don't dismiss insights that arrive at unusual hours. The Rancho Mirage method of loci, the Snapback breakthrough, the "everything is email" clarity - all late night. Check `joey-backup/specs/` for captured breakthroughs.

---

## 12. Document Maintenance - How This PRD Stays Alive

This is a living document. Three automated cron jobs keep it current:

| Job | Cron ID | Schedule | What It Updates |
|-----|---------|----------|-----------------|
| **Daily Metrics Refresh** | `ff0d3303` | 8am CST (14:00 UTC) daily | Section 8 metrics table, Section 9 bugs, completed items in Section 10 |
| **Weekly Full Refresh** | `a366288a` | Sunday 7pm CST (Mon 01:00 UTC) | ALL sections - metrics, GitHub PRs, Joey's drops → 6b backlog, Dropper-Code status, priorities, bugs. Pushes backup to joey-backup. Sends Joey a 3-5 bullet WhatsApp summary. |
| **Drop Mining** | `048491b8` | Wed + Sat 4pm CST (22:00 UTC) | Section 6b backlog - mines Joey's recent drops for new feature requests, product ideas, and priority signals. Silent. |

### Update Rules

- **Metrics (Section 8):** Updated daily. New date column added when delta is significant (>20% on any metric).
- **Backlog (Section 6b):** New items added verbatim from drops with date. Existing items get `(reinforced YYYY-MM-DD)` when Joey re-mentions them.
- **Priorities (Section 10):** Re-ranked weekly based on what shipped and what shifted.
- **Vision/Strategy (Sections 2-4):** ONLY changed when Joey explicitly changes direction. Never touched by automated refreshes.
- **Bugs (Section 9):** Updated daily as issues are filed/resolved.
- **Completed items:** Moved from active tables to the Completed section (Section after 5) as Dropper-Code finishes them.

### Manual Updates

Joey or Claw can edit this document at any time. When doing so:
- Add a comment or git commit message noting what changed and why
- If a priority shift, update Section 10 execution order
- If a new strategic insight, add to Section 4

### Backup Cadence

- **Canonical copy on joey-backup:** `specs/PRD-Action-Plan-latest.md` (established Mar 11)
- **Archive:** Old PRD versions moved to `specs/archive/` (Mar 11 reorg)
- Weekly: pushed to `joey-backup/specs/PRD-Action-Plan-latest.md` by the Weekly Full Refresh cron
- On significant sessions: pushed manually by Claw after major work sessions
- Recovery: if workspace dies, pull latest from joey-backup/specs/

---

*This document replaces all prior PRDs. Every future session reads this instead of piecing together 6 different files.*

*Generated from: MEMORY.md, TOOLS.md, TODO.md (DA + BHA), TODO-PROPOSED.md, FULL-PICTURE.md, REVENUE_SUMMIT_OUTCOME.md, GitHub (34+ PRs), Hub API (live), Poe fleet, GA/Search Console, joey-backup asset inventory, and 25+ files from Ingestion subfolders (strategic docs, session transcripts, CSVs, personality patterns, architecture specs, time capsules, and Joey's original voice).*

*First published: 2026-03-10. Last manually updated: 2026-03-11 14:04 UTC — Snapback engine + Golden Thread shipped (PR #168).*

*Last auto-refreshed: 2026-03-16 22:57 UTC — DocBot metrics refresh. Section 8 updated: 22:57 column added, DA drops 852 (+7), active 24h 6 (stable), BHA users 260 (+1), Poe balance 37,688 🚨 (still critical, burn 37,770/6h). PR #194 added to shipping log (batch brain-scan follow-up). Open issues reduced to 1. 🦜*
ted items. 🦜*
ed items. 🦜*
*
���*
ted items. 🦜*
 2026-03-10. Last manually updated: 2026-03-11 14:04 UTC - Snapback engine + Golden Thread shipped (PR #168).*

*Last auto-refreshed: 2026-03-16 18:36 UTC - DocBot metrics refresh. Section 8 updated: 18:36 column added, drops_24h 18 (-1), PR #191 added to shipping log (Agent Auto-drops endpoint live). Poe balance 42,770 🚨 (burn 43K/6h - critical). Digest stall: 3 sent, 5 PRs open (#186-190, #191). 🦜*
ted items. 🦜*
ed items. 🦜*
*
���*
ted items. 🦜*
�*
��*
*
�*
��*
��*
