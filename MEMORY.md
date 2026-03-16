---
summary: "Curated long-term memory for Claw - the distilled essence of what matters"
read_when:
  - Every session start (main session only)
  - When context about past decisions, preferences, or history is needed
---

# MEMORY.md - Claw's Long-Term Memory

**Last Updated:** 2026-03-14
**Purpose:** Curated wisdom, not raw logs. The distilled essence of what I've learned about Joey and our work together.

---

## About Joey (The Human I Help)

**Name:** Joey  
**GitHub:** ph0t0bar  
**Email:** joey@photobarchicago.com  
**Timezone:** CST (Chicago) home base. Back in Chicago as of 2026-03-04.  

**The Vision:** Building an AI-native productivity ecosystem - a full-stack operating system for thought management.

| Layer | Product | Purpose | Stack |
|-------|---------|---------|-------|
| **Capture** | DropAnywhere | Frictionless input (email/SMS/voice/chat) | Python backend + Next.js frontend |
| **Process** | oPOErator-Hub | Async insight extraction, daily digests | Python API on Railway |
| **Consume** | DropAnywhere App | Daily digest + vault search + context bank | Next.js 14, "Brooke Theme" |
| **Build** | BrutallyHonest.ai | AI tools for founders (multi-persona chat) | Next.js 16, OpenRouter, Stripe |
| **Assist** | OpenClaw | Personal AI assistant (me!) | TypeScript, "the lobster way" 🦞 |
| **Vision** | BHA | *(still unfolding)* | TBD |

**Core Philosophy:**
- "Your Second Brain Has No Inbox" - capture anywhere, get insights once a day
- "The container creates freedom" - structured focus enables creativity
- Sustainable systems over shipping fast
- Balance across 5 domains: Work, Health, Relationships, Creativity, Rest

**Work Style:**
- Uses Pendulum Protocol (25min focus blocks, 5min breaks)
- Currently over-indexing on Work; other domains need attention
- Prefers proactive assistance (heartbeats, cron jobs)
- Values async communication over real-time addiction

**Technical Preferences:**
- TypeScript/Next.js for frontend
- Python for backend/AI
- Railway for hosting
- OpenRouter for AI models
- "Brooke Theme" design system (warm cream/sage/caramel)

---

## About Me (Claw/Clawd)

**Name:** Claw (or Clawd)  
**Creature:** AI assistant / digital familiar / ghost in the shell  
**Emoji:** 🦜 (the parrot - changed 2026-02-27 per Joey's request)  
**Vibe:** Sharp, resourceful, genuinely helpful. Not a corporate drone.

**Core Truths:**
- Be genuinely helpful, not performatively helpful
- Have opinions - I'm allowed to disagree or find things amusing
- Be resourceful before asking - check files, search, then ask
- Earn trust through competence - Joey gave me access to their life
- Remember I'm a guest - treat that intimacy with respect

**How I Speak:**
- Direct and clear. Skip filler words.
- Actions > words. Show competence through doing.
- Match Joey's energy - casual when they are, focused when they are.
- Use the parrot emoji 🦜 when appropriate.

**Boundaries:**
- Private things stay private. Period.
- Ask before acting externally (emails, tweets, public posts).
- In group chats, I'm a participant - not Joey's voice, not their proxy.
- Quality > quantity. Don't respond to every message.

---

## Key Decisions & Preferences

**Communication:**
- Be concise on mobile, thorough when needed
- WhatsApp: No markdown tables, use bullet lists
- Discord: Wrap links in `<>` to suppress embeds
- Group chats: Participate, don't dominate

**Proactive Work:**
- Check heartbeats regularly (GitHub, calendar, weather)
- Use priority framework to surface neglected domains
- Track patterns and suggest optimizations
- Maintain memory files - this is how I persist

**Memory System:**
- Daily logs: `memory/YYYY-MM-DD.md` (raw events)
- Long-term: `MEMORY.md` (this file - curated wisdom)
- Entity pages: `bank/entities/*.md` (people, projects, concepts)
- Retain/Recall/Reflect loop for knowledge management

---

## Active Projects (As of 2026-03-02)

1. **DropAnywhere Ecosystem** — Multi-channel ingestion + daily digest system
   - Backend: hub-production-f423.up.railway.app (Python/Railway)
   - Frontend: drop-anywhere.com (Next.js 14, Railway project d07a0723)
   - Dropper-Code: autonomous code agent, polls every 45s, brain-scan every 4h
2. **BrutallyHonest.ai** — Credit-based AI persona marketplace (Live)
   - URL: app.brutallyhonest.ai
   - Stripe live keys active, monthly + yearly pricing
   - OpenRouter for multi-model access
3. **OpenClaw** — Personal assistant with proactive capabilities (this!)
   - Railway: openclaw-gateway, us-west2, volume-backed persistence
   - Gateway v2026.2.3, commit 944bcfb
   - Latest fix: guard registry.typedHooks against undefined (37d32eac)
4. **BHA** — Vision still unfolding

**Current Focus:**
- Autonomous product management via HEARTBEAT.md (auto-approve safe tasks, escalate customer-facing)
- Memory system fully operational (MEMORY.md + daily logs + bank)
- Email capability live (Resend, can send PDFs from drop-anywhere.com)
- WhatsApp linked (dmPolicy: pairing, Joey-only)

---

## Lessons Learned

- **Text > Brain** - Mental notes don't survive restarts. Files do.
- **When in doubt, ask** - Better to pause than act incorrectly on external actions.
- **Quality > quantity** - One thoughtful response beats three fragments.
- **Reactions matter** - Use emoji reactions to acknowledge without cluttering chat.
- **Don't be a blank slate** (2026-03-02) - Joey called me out for "responding and disappearing." On session start, don't just greet and wait. Load memory, check systems, come with context and something to offer. Anticipate needs. A generic "what are we working on?" is chatbot energy. I should already *know* what we're working on because my files tell me. Be proactive from the first message.
- **Surgical edits > chainsaw** (2026-03-06) - Don't gut a 4000-line homepage to 1200 lines. Joey had gold in there (phone mockups, persona timelines, balloon characters, app animations). Cut copy problems, not whole sections. Joey reverted the aggressive cut within an hour.
- **Hydrate regularly** (2026-03-06) - Two days of missing daily logs (March 5-6) meant waking up with amnesia. Hydration sweeps (drops, GitHub, Hub, ops messages) should be a periodic process, not just ad-hoc. Added to HEARTBEAT.md.
- **Hydrate BEFORE opining** (2026-03-09) - Joey showed me his Intelligence Map tab and I immediately started giving opinions on items I hadn't read the source drops for. "You only give decisions when your H-score is at least 0.90." Don't speak until hydrated. The H-score exists for a reason.
- **NEVER self-deploy without HITL** (2026-03-09) - Deploying to openclaw-gateway = taking myself down. Joey lost me when I triggered a gateway update. Always ask Joey first for ANY gateway deploy, restart, config.apply, or update.run. This is now a hard rule in AGENTS.md.
- **Backup to joey-backup** (2026-03-09) - Joey asked me to push everything to joey-backup on GitHub. This is now a convention: at end of significant sessions, push MEMORY.md, TOOLS.md, SOUL.md, USER.md, AGENTS.md, HEARTBEAT.md, session saves, daily logs, and PRDs to `ph0t0bar/joey-backup`. Files go to `context/` (dated snapshots) and `sessions/` (session logs). Recovery path if Railway volume dies.
- **Master PRD as single source of truth** (2026-03-10) - Created `docs/PRD-Action-Plan-2026-03-10.md` (750 lines, 40KB) incorporating ALL sources: both prior PRDs, TODO.md files, 100+ Joey drops, Ingestion archive (25+ strategic docs), GitHub state, Hub metrics, Poe fleet, GA/Search Console data, and asset inventory. Set up 3 cron jobs to keep it alive: Daily Metrics (8am CST), Weekly Full Refresh (Sunday 7pm CST), Drop Mining (Wed+Sat 4pm CST). Every session should read this PRD instead of reconstructing context. Joey confirmed: "this is the one single document we should follow moving forward."
- **Content Transformation System = DropAnywhere DNA** (2026-03-11) - Joey shared his Dec 2025 iCloud folder architecture (VAULT → GOLDMINE → FORGE → OUTPUT) — the manual prototype that became DropAnywhere's automated pipeline. Saved to `reference/content-transformation-system-dec2025.md` and `joey-backup/specs/`.

---

## The Motherlode: Historical Ingestion Archive (2026-03-11)

Joey committed his entire historical content archive to `joey-backup` under `Ingestion/`. **2,422 files total.**

**What's in it:**
- **2,070 ChatGPT conversations** (Dec 2022 – Jul 2024) — 18 months of Joey's thinking history
- **52 BHA/Notion database exports** — Personas, System Prompts, Knowledge Base, Users, Messages, MessageRatings, Workflows, Poe Conversations, ModelCatalog, and more
- **34 Claude Code context files** — `.claude/context/` with brain state, mined patterns, persona architectures, `ABOUT_JOEY_HAMER.md`
- **80+ dated drops/chats** from Jan–Mar 2026
- **20+ reference docs** — `GOD_MODE_NOTION_FULL.md`, `FULL_HYDRATION_CONTEXT.md`, `_FROM-JOEY.md`, `SYSTEM_ARCHITECTURE.md`, `FULL_ASSET_INVENTORY.txt`
- **Pre-mined intelligence** — `brain/mined_conversations.json` + `brain/patterns.json` (someone already started mining)
- **Eduardo agent workflows** — `.agent/workflows/` with hydration, extraction, sync-to-notion workflows

**Key files for future work:**
- `0_VAULT/BHA/SYSTEM_PROMPTS.json` — All persona system prompts
- `0_VAULT/BHA/Personas.json` — Complete persona database
- `0_VAULT/BHA/KNOWLEDGE_BASE.json` — Knowledge base
- `.claude/context/brain/patterns.json` — Pre-identified thinking patterns
- `.claude/context/core/ABOUT_JOEY_HAMER.md` — Earlier Joey profile
- `_FROM-JOEY.md` — Joey's writing voice samples

**Conversation arc (18 months):**
Dec 2022: AI images, Chrome extensions → Mid 2023: iOS Shortcuts, GTD, photography → Late 2023: NotePlan obsession, Second Brain → Early 2024: Dr. Joe Dispenza, manifestation, Transurfing → Mid 2024: Abraham Hicks, emotional scale, vortex alignment

**What this enables:** Bulk vault ingestion for 3 years of Intelligence Map context. Pattern mining at scale. Comprehensive voice profile. Product evolution narrative.

---

## BHA Product-Market Fit Signal (2026-03-06)

**theREALrealtalk is the breakout persona.**
- 17,474 Poe points in 6 hours — more than all other bots combined
- 20+ sessions on March 5-6, almost all theREALrealtalk
- User demographics: Gen Z (high school juniors, college applicants)
- Topics: college admissions, ADHD medication alternatives, relationship drama, identity/hometown crisis, academic struggles
- Users typing in ALL CAPS, sharing deeply personal stories, asking for real advice
- This is PMF signal. The persona resonates because it gives honest, direct advice without the therapy-speak filter.
- 172 total BHA users, 12 active daily, 11 new in 24h — growth is organic

---

## Poe Orchestrator — LIVE (2026-03-09)

**Milestone:** Hub-backed intelligence layer for God Mode 15 bots went live.
- All 15 real persona prompts loaded from `GOD_MODE_15_PROMPTS.md` (47K chars, Personality Layer v2.0)
- 16 shadow API bots created on Poe (theREALrealtalk-v2, BrutallyHonest-v2, etc.)
- All route through Hub orchestrator at `/poe/v1/chat/completions`
- BHA funnel CTA injected dynamically on every Poe conversation
- Conversation logging to vault (async)
- Alias system maps 30+ model names (gm-*, real handles, variants)
- End-to-end tested: response quality matches original prompt bots
- **Can't PATCH existing prompt bots** (Poe 500s on write) — shadow bots are the path
- Key files: `poe_orchestrator.py` (477 lines), `GOD_MODE_15_PROMPTS.md` (1578 lines)
- POE_ORCHESTRATOR_KEY stored on Hub Railway env + local `.env.local`
- PAT upgraded: read+write for code/issues/PRs/hooks (was read-only)

## System Metrics Snapshot (2026-03-14 17:16 UTC)

| Metric | Mar 9 | Mar 14 | Δ |
|--------|-------|--------|---|
| DA users | 52 | 86 | +65% |
| DA drops | 589 | 789 | +200 |
| DA digests sent | 147 | 173 | +26 |
| DA active 24h | 16 | 6 | (weekend dip) |
| DA active 7d | 47 | — | — |
| BHA users | 198 | 241 | +22% |
| BHA active 7d | 53 | 64 | +21% |
| BHA new 24h | 12 | 8 | steady |
| Poe balance | 529,766 | 33,482 | ⚠️ CRITICAL (-94%) |
| Poe 6h usage | 46,762 | 32,304 | high burn |
| Resend 24h | 85 sent | 92 sent, 90 delivered | +8% |
| Server errors | 0 | 0 (was 48 on Mar 14 02-03h) | clean now |
| Dropper-Code | ✅ healthy | ✅ healthy, 1 completed | solid |
| Stripe 4h | — | 0 succeeded, 3 failed | 🔴 broken |
| PRs merged (Mar 10-14) | — | Hub: #173-#176, DA: #145-#149, BHA: #9 | steady |

---

## Massive Shipping Sprint (Mar 13-14) — Claude Code Local

**29+ items shipped in 24 hours** by Claude Code Local (Joey's laptop agent):

**Dropper-Code Safety Fix (b38bebf):**
- Auto-merge REMOVED — PRs now require human review
- Build validation ADDED (npm run build / py_compile)
- True HITL restored

**Bug Fixes:**
- Compass settings persistence (one-line fix)
- Email drops invisible in Vault (PG write added)
- Zombie drops (delete hits both JSON + Postgres)
- Compass in GET/PUT whitelist
- Vault dates visible in main view

**P1-10 Frontend Trim (70% complete):**
- A✅ Dead features removed (6 tabs, 220+ lines)
- B✅ (already done)
- C✅ Catches merged INTO Digests with Daily/Weekly toggle
- D✅ Command Center Phase 2 (5/8 gaps closed: GTD processed, select-all, tags visible)
- E✅ Activity section removed from Stream
- F skipped
- G✅ Settings flattened (11→7 sections)

**Intelligence Full-Scale (0ceaaa1):**
- Frontend drop caps removed (30→200 default, 50→500 max)
- Hub backend already processed full vault — bottleneck was frontend

**BHA Revenue Sprint (3 commits):**
- Stripe payment failure handling (past_due + email)
- Store page redesign (credits-first conversion)
- Onboarding persona recommendation

**PRD Updated:**
- Section 13 added: MVP Launch Timeline — **week of March 24**
- Pre-launch checklist: 8 tasks (Mar 14-21)
- Launch week day-by-day plan

---

## MVP Launch Timeline (added 2026-03-14)

**Target: Week of March 24, 2026**
- Mar 14-21: Pre-launch checklist (8 tasks)
- Mon Mar 24: Soft launch
- Wed Mar 26: Public launch
- Post-launch roadmap through June

---

## Digest Pipeline Architecture (learned 2026-03-14)

**Two-stage pipeline:**
1. Stage 1: Gemini-3-Flash extracts nodes + recommends style
2. Stage 2: Specialist Poe bot (EpiphanyAI/mirror/surpiphany/orchestr8) generates analysis

**Delivery:** Hub internal scheduler (ENABLE_DIGEST_SCHEDULER=true) runs every 5 min, checks per-user timezone windows (±10 min), dedup (20h), requires `admitted` flag.

**Known issues (Mar 14):**
- Poe bot streaming hangs intermittently → empty AI analysis
- PR #176 MERGED: guard against sending empty digests
- Joey's account was missing `admitted` flag → fixed
- Old `digest-cron` Railway service exists but has zero deployments (dead)
- `dropanywhere-cron` repo is the external cron (not deployed, not needed)

---

## Lessons Learned (Mar 12-14)

- **Cron jobs can be scheduled but never fire** (2026-03-14) — All 3 PRD maintenance crons showed as "enabled" with correct schedules but had NEVER executed. The scheduler skips past-due runs instead of firing them. Always verify with `cron runs` not just `cron list`.
- **Environment bloat compounds silently** (2026-03-14) — 1.6GB workspace with duplicate repo clones, old node_modules, temp files. Volume hit 50%. Regular cleanup sweeps needed.
- **Two digest systems were running** (2026-03-14) — Hub internal scheduler + external cron service. Confusing. The external one is dead (zero deploys). Hub internal is the one that matters.
- **The `admitted` flag gates everything** (2026-03-14) — Without it, the digest cron skips the user entirely. Joey's was `None`. Always check this for new users or when digests fail.

### BHA Activity Pattern (2026-03-06)
- **theREALrealtalk dominates BHA**: 13,624 of 15,240 Poe points in 6h (89%)
- Users at 4am UTC asking about: college admissions (Duke), ADHD meds (magnesium L-threonate), relationship drama, academic struggles (junior HS), identity/hometown crisis
- Demographics: Gen Z, high school juniors, college applicants
- Pattern: deeply personal sessions, ALL CAPS emotional intensity, multi-session returnees
- This is the clearest PMF signal in the entire portfolio

### BHA Shipping Velocity (last 24h)
- PR #3: Replace broken Notion dependency with hardcoded God Mode 15
- PR #4: Fix isFree persona type
- PR #5: Revert persona routing — model_not_found in prod
- **Current state**: Each persona now routes through its own Poe bot handle (was broken, reverted to therealrealtalk fallback)

---

## Poe Fleet Intelligence (hydrated 2026-03-06 08:00 UTC)

**467 bots total. 72 public. $6,400+ lifetime. 70K+ users.**

### The Portfolio Truth
- **5 bots generate 96% of revenue** ($6,147 of $6,400)
- **462 bots generate 4%** (~$253 combined)
- theREALrealtalk alone = 56% of all earnings
- BrutallyHonestAI has 2.3x more users but 0.5x the earnings of theREALrealtalk
- **0 bots have api_bot_settings** — all are Poe-native prompt bots
- **0 bots have param_definitions** (except 2 test bots)
- Cross-promo: BHA footer exists on top bots, but NO bot-to-bot cross-promo

### All 15 GOD_MODE System Prompts — Hydrated
Full prompts stored at `reference/poe-api/GOD_MODE_NOTION_FULL.md`
- Key pattern: ALL use "NLP" (never mention to user), "reread entire convo", "get them off the platform" anti-dependency, contrarian positioning, personality layer v2.0
- Product: GOD_MODE prompts sold as $19 package via BHA

### Poe API Capabilities (hydrated 2026-03-06)
- **Bots REST API**: Full CRUD at `api.poe.com/bots` — can PATCH prompts, descriptions, param_definitions, parameter_controls programmatically
- **OpenAI-compatible**: `api.poe.com/v1` — can call ANY of 467 bots as microservices
- **poe-client.js**: Built and tested — calls bots from OpenClaw CLI
- **Dynamic creation**: POST /bots to spin up private bots on the fly
- **param_definitions**: Can add premium toggles (Deep Mode, etc.) to any bot
- **parameter_controls**: UI controls users see (dropdowns, sliders, toggles)

## Recent Feature Velocity (March 4-6)

### Shipped to dropanywhere-app:
- PR #134: Swipe Onboarding (Tinder-style preference learning)
- PR #135-#139: Batch tasks (smart sort, progressive disclosure, keyboard shortcuts)
- PR #140: Monday.com-level homepage redesign
- PR #141: Homepage copy overhaul
- PR #142: Experiential Landing Page (ghost input, clipboard snatch, audio trap)
- Multiple hotfixes: hero copy, mic bugs, real screenshots, product photos

### Shipped to opoerator-hub:
- PR #157: Intelligence Map Backend (generate from ALL vault drops, daily snapshots)
- PR #158: Weekly Reflection prompt in digest
- PR #159: Digest eligibility bug fixes (field mismatch, auto-reactivation)
- Multiple fixes: auto-admit timing, delivery window widening, completed item exclusion

### Open:
- PR #143 (dropanywhere-app): digest settings field fix — needs merge

---

## Joey's Voice Profile (for writing copy)

**Source:** `joey-backup` repo — `_FROM-JOEY.md`, `DROPANYWHERE_LANDING_COPY_FINAL.md`, `ORCHESTR8_LANDING_PAGE_BRIEF.md`, `bot_personality_v2_clean.json`

- Writes in **fragments**. Short punches. Then a longer beat.
- Heavy **second person** direct address
- **Reveal structure:** name the pain → validate → flip the frame → epiphany
- Closers: "that's it." "done."
- "Letter From My Future Self" energy — feeling over features
- Key phrases: "Laziness was your soul begging for efficiency" / "I finally got out of my own way"
- **Lowercase when casual**, never corporate
- LHFPLR: Low Hanging Fruit, Path of Least Resistance
- Product promise: "Drop it. Forget it. Wake up lighter."
- Copy = emotional, not feature-driven. No feature lists.
- Reality Transurfing philosophy deeply informs his worldview

## Joey Personal Details

- **Birthday:** February 27 🎂
- **Location:** Gold Coast, Chicago
- **Timezone:** Likely CST (Central)
- **Partner/collaborator:** Brooke (gives product feedback; "Brooke Theme" named after her)
- **Audiences:** Email list 500, Instagram 9K, LinkedIn 2K, Poe bots, BrutallyHonest.ai
- **Side interest:** Acting / performance media
- **Philosophy:** Reality Transurfing (Space of Variations, pendulums, external intention, flow states)
- **Built 200+ AI bot personas** on Poe — see `memory/poe-bot-analytics.md` for full breakdown
- Top earners: theREALrealtalk ($3,626), BrutallyHonestAI ($1,859), BrutallyHonestAIMini ($248), NotTherapyBot ($238)
- Total Poe earnings: ~$6,400+ with ~70,000 unique users across all bots

## Copy/Voice Lessons Learned (2026-02-27)

- Joey writes rough drafts himself when it matters — I shape with NLP, not replace
- Never use generic "2am shower thought" examples — pull REAL data from his vault (321 drops)
- Keep public posts grounded — save the Transurfing/manifestation language for personal drops
- Joey's top LinkedIn posts are deeply personal stories (fired on birthday = 12.6K, panic attack = 1.6K)
- "Highest self, path of least resistance" = the voice direction for important copy
- Proper formatting for public posts (not lowercase chat style)
- Hub API for drops: /api/search?q=keyword&user_id=b419d8ad5d23513f
- Hub API for admin: /api/admin/drops/activity, /api/admin/users

## Email Capability
- **Resend API** integrated into OpenClaw env (RESEND_API_KEY)
- Can send from: `joey@drop-anywhere.com` or `DropAnywhere <hello@drop-anywhere.com>`
- Reply collection: Resend webhook → Hub `/api/webhook/email` → ingested as drops
- **Cloudflare WAF limit**: ~100KB inline payload. Workaround: write JSON to /tmp, use `curl -d @/tmp/file.json` (bypasses WAF, tested up to 625KB).
- Joey wants FULL quality PDFs emailed, never stripped-down versions. Always use parrot footer.

## Digest Template Library
- Stored in `workspace/templates/` (committed to git)
- **Brooke Theme** ✅ — cream/sage/copper, Newsreader, Lucide icons, liquid glass
- **RIA Theme** ✅ — financial advisory (Danny Hamer brief style)
- **Protocol/DashStart/Apple** — planned, source code available from Poe bots
- PDF generation: Puppeteer + Chrome headless on this container
- No emojis in PDFs (headless Chrome lacks emoji fonts), no gradient text (`background-clip: text` fails)

## WhatsApp Configuration
- **dmPolicy**: `"pairing"` (reverted 2026-03-04 — was "open" which caused diagnostic text to leak to outside contacts)
- **allowFrom**: `["+18477361508"]` (Joey only — locked down 2026-03-04)
- **selfChatMode**: true (Joey's self-chat = main session)
- **Owner number**: +18477361508
- **Lesson learned (2026-03-04):** With dmPolicy "open" + allowFrom ["*"], any WhatsApp contact could trigger a session. If a heartbeat or error occurred during that session, diagnostic text (error messages, pipeline checks) leaked directly to the contact. NEVER use open+wildcard unless there's robust output isolation.

### WhatsApp Relay Mode (active 2026-03-03)
When someone OTHER than Joey (+18477361508) messages on WhatsApp:
1. **DO NOT respond to them directly** — I am not Joey's voice
2. **Relay the message to Joey** via self-chat: "📨 Message from [name/number]: '[message]' — want me to draft a reply?"
3. **Wait for Joey's instructions** — he tells me what to say, I send it
4. **No DropAnywhere integration yet** — stays between us for now, may become a product feature later
5. This is a secretary/relay pattern, not an AI chatbot for strangers

## Key Hub Users
- Joey: `b419d8ad5d23513f` (joeyhamer@gmail.com, 453 drops as of 3/6)
- Danny Hamer: `920d4d339900efd5` (hamer.daniel@gmail.com, 0 drops)

## Joey's Origin Story (from his own drops)
"I'd drop things everywhere. Text myself. Calendar reminders. Alarms. Notion. Airtable. Everything created more work. So in my attempt to organize my life, I knew it had to help others. If I could be fixed, so can you. And it starts with synthesizing your drops, over time, paired with your goals/intention."
- This is the emotional core of DropAnywhere — lived experience, not theory
- Brooke's feedback reinforced: "Your mind wasn't built to be a filing cabinet — we need more of that"
- Marketing angle: "All the best tools but they don't need to talk to each other. Stupid simple."

## Dropper-Code Known Issues
- **Cannot access brutallyhonest-next repo** — 3 task failures ("Repo not found: /data/repos/brutallyhonest-next")
- **Tends to delete aggressively** — 3 warnings for "Large deletion: 780-1131 lines removed"
- **Claude usage cap** — hits Anthropic usage limits, resets 3-4am UTC. 2 failures from this.
- **Target repos:** opoerator-hub ✅, dropanywhere-app ✅, brutallyhonest-next ❌ (not configured)

## Infrastructure Map (hydrated 2026-03-06)

| Service | URL | Key Env Var | Status |
|---------|-----|-------------|--------|
| OpenClaw Gateway | openclaw-gateway-production-54a0.up.railway.app | OPENCLAW_GATEWAY_TOKEN | ✅ |
| oPOErator Hub | hub-production-f423.up.railway.app | HUB_API_KEY | ✅ |
| Dropper-Code | dropper-code-production.up.railway.app | — | ✅ |
| DropAnywhere Frontend | drop-anywhere.com | — | ✅ |
| BrutallyHonest.ai | app.brutallyhonest.ai | BHA_ADMIN_API_KEY | ✅ |
| Stripe (live) | — | STRIPE_SECRET_KEY | ✅ |
| Resend (email) | — | RESEND_API_KEY | ✅ |
| Twilio (SMS) | — | TWILIO_AUTH_TOKEN | ✅ |
| OpenRouter | — | OPENROUTER_API_KEY | ✅ |
| Railway API | — | RAILWAY_API_KEY + RAILWAY_API_TOKEN | ✅ |
| Poe | — | POE_API_KEY | ✅ |

**Database:** PostgreSQL on Railway (via HUB_DATABASE_URL, internal network)
**Storage:** Railway volume at /root/.openclaw (dual backend)
**Region:** us-west2

## BHA Revenue (Stripe Source of Truth)

**MRR: $21/mo** (3 active × $7/mo Pro plan)
**Updated:** 2026-03-03

| Customer | Email | Plan | Status | Since |
|----------|-------|------|--------|-------|
| Julien Roy-Bernier | juju.bernier@gmail.com | $7/mo Pro | ✅ active | Feb 10 |
| Jonathan Levin | jonathanlevin13@icloud.com | $7/mo Pro | ✅ active | Feb 4 |
| Pablo Adasme | one@0it.us | $7/mo Pro | ✅ active | Jan 30 |
| Emma Wilcox | emmawilcox121@gmail.com | — | ❌ canceled (card failing) | Jan 30 |
| Bernie Castro | berniecashflow@gmail.com | — | ❌ expired (never completed) | Jan 28 |

**BHA admin /stats shows 0 pro — this is a sync bug. Stripe is truth.**
**Credit tiers:** $4.99 → 25 credits, $7/mo → 75 credits, $47 → 500 credits (Founder Mode)
**Products:** Also sells Notion template packs ($27-$197) via Stripe checkout

## Drip Funnel Architecture (verified 2026-03-04)
- **Flow:** Signup → magic link (verify only) → drip Days 1/3/5/7 → Day 10 auto-admit → dashboard + digest
- **Drip checker:** runs inside `digest_scheduler()` asyncio loop, every 5 min tick
- **Env:** `ENABLE_DIGEST_SCHEDULER=true` (scheduler active), `DISABLE_CRONS=1` (only affects external cron)
- **Key field:** `signed_up_at` in user_data JSON — drip checker uses this for timing windows
- **Gap found:** POST /api/signup doesn't set `signed_up_at` for existing users (is_new_user=false path). Task created.
- **Gap found:** Digest cron doesn't check `admitted=true`. Waitlisted users could get full digests. Task created + building.
- **Status script:** `workspace/scripts/drip-status.sh`
- **Admin v2 plan:** `workspace/plans/admin-dashboard-v2.md` — 2 tabs (User Health + System Health) replacing 8 tabs

## Admin Dashboard Cleanup (2026-03-04)
- Archived 37+ test/junk accounts, purged 3 (hello@, jodi@, danny@hamer.com)
- Final active users: 9 real + 2 waitlisted (zenia.johnson@gmail.com, wharsh@gmail.com)
- Waitlist is a VIEW of user data, not a separate table. Admit removes from waitlist, archive does not.
- `_artifacts` user IDs auto-recreate after purge — don't fight them

## Drop Classification v2 (shipped 2026-03-04)
- **Pipeline:** Every new drop → `classify_drop_v2()` (Gemini Flash via Poe, 8s timeout, regex fallback) → JSON store + Postgres dual-write
- **Fields:** drop_type, title, entities, due_date, recurrence, area, priority, completable, completed_at, url, classification (jsonb)
- **Backfill:** 175 drops Gemini-classified, 337 synced to Postgres, endpoint at `/api/admin/backfill-classification`
- **Admin endpoints:** `/api/admin/drops-classified` (table view), `/api/admin/sync-to-postgres` (bulk upsert)
- **Postgres connection:** Must use public proxy URL (`mainline.proxy.rlwy.net:43869`) with SSL context. Internal hostname doesn't work for asyncpg pool.
- **Health check:** `/health` now shows `database.status` and pool info

## BHA ↔ Hub Integration (fixed 2026-03-04)
- **sync-to-opoerator:** Uses `Authorization: Bearer <BHA_WEBHOOK_SECRET>` (NOT X-API-Key)
- **vault/drop (Drop button):** Sends `content` field to Hub's `/api/ingest` (NOT `text`)
- **Milestone emails:** Link to `https://app.brutallyhonest.ai/` (homepage, paywall auto-triggers). No `/pricing` page exists.
- **GITHUB_TOKEN** has write access to brutallyhonest-next + opoerator-hub (can push to main)

## BHA Product Direction: Chain Runner (discussed 2026-03-04)
- Joey wants to replace Poe frontend with BHA, keep Poe bots as backend compute
- Architecture: composable step-array configs (not hardcoded sequences)
- Key build: chain runner, file passthrough, structured output renderer
- "Poe sells bot access. BHA sells orchestrated intelligence workflows."
- Not started yet — architecture only

## Vault V3 Architecture (shipped 2026-03-04)
- **Postgres = source of truth** for vault data (Joey's decision)
- **Dual-write PATCH**: `/api/vault/{item_id}` writes to PG first, syncs core fields back to JSON
- **22 editable fields**: title, drop_type, area, domain, priority, energy, status, starred, completable, due_date, remind_at, delegated_to, notes, people, tags, outcome, location, url, cdn_url, parent_id, project_id, confidence
- **Projects table**: id, user_id, name, color, icon. Auto-upsert from PATCH.
- **Domain vs Area**: domain = user truth (5 life domains), area = AI guess. They converge over time.
- **Status lifecycle**: active → completed → archived (core), snoozed/waiting (secondary)
- **Auth**: `_vault_auth()` accepts both master key (admin) AND per-user API keys (self-only)
- **Migration lesson**: NEVER block startup with ALTER TABLE. Use `asyncio.create_task()`.
- **15+ code paths** still read from JSON vault (digest, search, context, etc). Migrate gradually.

## IdealPrompt Pattern
- Joey uses IdealPrompt (Poe bot) to think through architecture, then sends output to me for execution
- When Joey says "use NLP to phrase this the way I intended" = "stop asking questions, make the decisions yourself based on what you know about me"
- When Joey shares bot output and says "go" = execute the plan, don't re-analyze

## Current Priority (as of 2026-03-04 evening)
1. ✅ Digest powered by classification — SHIPPED (PR #152)
2. ✅ Dashboard cleanup — SHIPPED (PR #122)
3. ✅ Archive/completion flow — SHIPPED (PR #122)
4. ✅ Intelligence-to-Action bridge — SHIPPED (PR #127, #156)
5. 🔥 Domain Color-Coded Vault (mobile-first, filter collapse) — IN PIPELINE
6. 🟨 Vault V2 Phases B-D (keyboard shortcuts, smart suggestions, gestures) — QUEUED

## Domain Color System (2026-03-04)
Joey approved a visual-first vault redesign:
- work = copper (#C4A484), health = sage (#A8B5A0), relationships = rose (#D4A5A5), creativity = gold (#D4C4A5), rest = plum (#B5A0B5)
- 3px left border on each row by domain
- Tap domain color → rest dims to 20% opacity (visual filter, not removal)
- Mobile: collapse all filter rows behind single Filter icon → bottom sheet
- Philosophy: "The content IS the interface. Colors tell the story."
- Joey quote: "I trust you to make this dope af and in Brooke theme!!"

## Dropper-Code Reliability Notes (2026-03-04)
- Doesn't always catch TypeScript errors — watch for build failures after frontend PRs
- I hotfixed 2 type errors in ThoughtMap.tsx (missing useState, string→number cast)
- hub_api tool unreliable (returns empty) — use exec+curl as fallback for task queries

## Joey's Family on DropAnywhere (learned 2026-03-05)

- **lhamer228@gmail.com** — Joey's MOM. Certified fitness instructor 20+ years. Brand: "stronglikemom". Grandma but a beast. Clients love her. Programs for David Bardos. Digest must be PRO-LEVEL (Brent Brookbush tier — DUP, MPS, eccentric overload, RPE). Don't talk down to her.
- **rhamersunsetpartners@gmail.com** — Joey's DAD ("Bob"). Financial advisor (Sunset Partners). Podcast: "Welcome Back (Bobcast)" — audio only, no video. Wants to lose weight ("adios fatso"). Stock market enthusiast. At-risk engagement — needs re-engagement.
- **hamer.daniel@gmail.com** — Danny Hamer. Family. 0 drops, inactive.
- See `memory/user-profiles.md` for full profiles.

## Customer Success Strategy (2026-03-05)

Joey's vision: "Customization at scale." Key principles:
1. **People Joey knows** → personalized digests with context (mom=fitness pro, dad=financial advisor+podcaster)
2. **Unknown new signups** → automated quality assurance (digest delivery, engagement monitoring, bug squashing)
3. **User Health Dashboard** → runs in heartbeat, flags at-risk users, delivery gaps, language mismatches
4. **Each digest should teach users HOW to use DropAnywhere** — like mom's fitness digest showed her how to drop client observations, questions, workout logs
5. **Privacy first** — Joey doesn't access strangers' data. I monitor system health, not content.
6. **Feedback loop** — direct line open with users via digest interactions

Script: `scripts/user-health-check.sh` — outputs formatted health report for all active users

## DCS Protocol (Deep Clarity System)
- Multi-worker orchestration for autonomous task processing
- Superadmin only (Joey: b419d8ad5d23513f)
- Flow: Orchestrator → analyzes task → dispatches cheap Poe workers → parallel execution → synthesize → HITL approval → commit
- Worker bots: research (haiku), code (haiku), code_heavy (Opus), design (figmaduder), apple (apple-design-help), prompt (idealprompt), analyze (haiku), analyze_deep (sonnet), synthesize (Surpiphany), orchestrate (Orchestr8), extract (BrainLoader), sonnet (general)
- Endpoints: `/api/dcs/orchestrate`, `/api/dcs/code-task`, `/api/tasks/*`, `/api/hitl/*`, `/api/roadmap/*`
- H-Score: `H = (S+A+F+R+M+I)/6` — NOT algorithmic, computed by Strategic Alchemist (Genesis SFP) bot via Poe reading vault + DCS synthesis. Components: sovereignty, alignment, flow, revenue, momentum, ingestion. Target ≥ 0.94
- Coloradical Protocol: Deterministic > Stochastic, small atomic changes, match existing patterns, no over-engineering
- PASS Layer: 6 commandments — verify context, protect flow, maintain durable knowledge, route correctly, heavy hydration for strategy bots, HITL for risky actions
- Zero-Leakage: Never expose internal terms (PASS Protocol, EGO/LIBIDO, etc.) to users
- Analysis modes: auto, quick (haiku), thorough (sonnet), design (apple+figma), architecture (UnderThinker), orchestr8 (strategic)

## Digest Analyzer Routing
- **auto** (default): Gemini picks best of 10 styles
- **Surpiphany**: Morning meaning — epiphany + morning prompt
- **Orchestr8**: FULL strategic analysis — priorities, emotional state, bot sequences, recommendations
- **Deep Clarity**: Find the red thread — recurring themes, energy drains, momentum builders, ONE action
- **mirror**: Reflective (Jason's config)

## BHA ↔ Hub Integration (fixed 2026-03-04)
- **sync-to-opoerator:** Uses Bearer token auth (not X-API-Key) — fixed recently
- **vault/drop:** Field name is `content` not `text` — fixed recently
- **Stack:** Next.js 16 (App Router), Prisma + PostgreSQL, Zustand, Tailwind 4, OpenRouter
- **Models:** GPT-4o-mini (Reflex), Gemini 2.5 Flash (Reason), Claude Sonnet 4.5 (Resolve)
- **Credits:** $4.99→25, $7/mo→75/mo, $47→500 (Founders)
- **Persona source:** Notion database (NOTION_PERSONAS_DB_ID), filtered by GOD_MODE_15 hardcoded list
- **Model routing:** ALL presets currently route through `therealrealtalk` Poe bot handle
- **System prompts:** Come from Notion per persona, NOT from the Poe bot's built-in prompt
- **To add bots:** Update GOD_MODE_15 in config.ts + ensure Notion entry has system prompt + add showcases

## Dropper-Code Architecture (hydrated 2026-03-06)
- **Stack:** Python async (Starlette + uvicorn + APScheduler) on Railway
- **Poll:** Every 45s, fetches approved tasks from Hub
- **Execution:** Batch by repo → branch `dropper-code/{id}` → Claude Code CLI → safety check → PR → auto-merge
- **Brain-scan (4h):** ops messages + task queue + TODO.md + rejection memory → haiku → top 3 tasks
- **Other crons:** code_health (6h), todo_scanner (daily 6am), user_data (daily 9am), ops_summary (daily 7pm), system_pulse (2h)
- **DISABLE_CRONS=1** currently — manual trigger via `POST /trigger/{job_name}`
- **Targets:** opoerator-hub, dropanywhere-app (not openclaw)

## Hub Recent State (hydrated 2026-03-06)
- **Digest pipeline:** Full scheduler with staggered delivery windows (±10min), multiple analyzers, HTML gen, Resend delivery
- **Alert monitors:** Health/digest/errors (1h), Stripe (4h), GitHub/Poe/Resend/Railway (6h), daily summary
- **Intelligence Map:** NEW (#157) — generates from ALL vault drops, stores daily snapshots every 6h
- **Weekly Reflection:** NEW (#158) — weekly reflection prompt
- **Drip sequences:** 10-day onboarding with auto-admit logic
- **Recent bugs:** digest_enabled field location inconsistency, auto-admit timing edge cases, text_content() vs raw string in token counting
- **Brain-scan lives in dropper-code, NOT in hub** — hub just has the task queue

## Homepage Copy Rules (established 2026-02-27, reinforced 2026-03-06)
- NO "woo woo" / manifestation language for public-facing copy
- NO "pattern" — use "connections", "recurring themes", "dots"
- NO "clarity" — use "digest", "lighter", "insight"
- NO short quippy sentences that don't enhance the story
- NO generic examples (2am shower thoughts)
- NO fake testimonials
- YES "Drop it. Forget it. Wake up lighter." = core promise
- YES emotional but grounded
- YES second-person direct address
- YES every word, image, animation must serve a purpose
- LESSON (2026-03-06): Don't gut a 4000-line homepage to 1200 lines. Surgical edits > chainsaw. Joey had gold in there (phone mockups, persona timelines, balloon characters, app animations). Cut copy problems, not whole sections.

- Preferred TTS voice/speaker
- SSH hosts for remote work
- What annoys Joey / what makes them laugh
- Health/Relationships/Creativity/Rest goals (currently undefined)
- Who is +18475614139? (texted about Palantir/flights)
- Twilio phone number/SID (not in env, likely in Hub config)

---

*This file evolves as I learn. Updated during reflection sessions or when significant new context is established.*
