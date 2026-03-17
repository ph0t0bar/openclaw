# Snapback: The Weekly Catch

**Product Integration Document — DropAnywhere's Hero Feature**

**Author:** Claw + Joey (3am session, March 11, 2026)
**Status:** Draft — born from a real moment, not a meeting
**Companion to:** `PRD-Action-Plan-2026-03-10.md` (Section 5.12, 5.1, 5.4, 5.11, 5.17, Gate D)

---

## 0. What Happened Tonight (The Proof)

At 3am on March 11, Joey dropped a raw feeling: *stuck on music, hasn't opened FL Studio, feels the pendulum pulling him away from creation.*

The system caught the drop. Recognized the Transurfing pattern — pendulum capture, comparison, low energy. Generated a first-person, present-tense visualization using details FROM HIS OWN DROPS: Brooke beside him, Boo and Teddy on the couch, FL Studio open, the Rancho Mirage mansion on the vision board behind the monitors.

Joey read it. Went and made music. Started a 30-day lyric challenge with Brooke. Asked for another Snapback about the songwriting moment — it landed harder.

Then:

> "Wait. This IS the product."

**The loop:**
```
Drop (raw feeling) → System catches → Narrative returned → Creator creates
```

That's not a feature request. That's a prototype that already worked.

---

## 1. Product Vision

**DropAnywhere is not a note-taking app with daily digests.**

DropAnywhere is a system that catches everything you throw at it all week, then snaps you back to yourself on Sunday.

The Snapback is the moment. The Weekly Catch is the delivery. The daily digest is NOT dead — it's proven and users love it. Snapback is ADDITIVE. Both coexist via `digest_mode` feature flag. Daily digest = the foundation. Weekly Catch = the new layer that opens up gradually.

### The Name (Triple Meaning)

| Layer | Meaning | Energy |
|-------|---------|--------|
| **Snapback hat** | Sports, culture, style. You catch a snapback. You wear one. It's yours. | Familiar. Cool. Not corporate. |
| **Snap back** | Transurfing: snapping back from pendulum capture to your own frequency | Deep. Personal. The real mechanism. |
| **The catch** | Reaching over the fence and grabbing something that was flying by | Visceral. That feeling of *getting it*. |

> *"Snapback is like a hat right? Sports are just so relatable. But if done the right way it's just clever, not too sportsy."*
> — Joey, 3am

### What Changes

**Before:** Drop → classify → daily digest (summary, bullet points, action items) → repeat tomorrow.

**After:** Drop all week → system watches, learns, connects → **one Weekly Catch narrative** that tells you the story of your own week in a way that makes you go *"oh shit, I see it now."*

Not a summary. A story. YOUR story, told back to you through the lens of what you actually need to see.

---

## 2. How It Works

### The Weekly Loop

```
MONDAY – SATURDAY
│
│  Email prompts arrive (2-3/week, casual, encouraging)
│  "What's on your mind today? Just reply."
│  "Anything weird happen this week? Drop it."
│  "What are you avoiding? (That's usually the good stuff.)"
│
│  User replies. Attaches photos. Forwards emails. Sends voice notes.
│  Zero friction. No app. No login. Just respond.
│
│  System silently:
│  ├── Classifies each drop (5.11 Unified Classification)
│  ├── Extracts emotional tone, entities, themes
│  ├── Detects pendulum patterns (comparison, fear, avoidance)
│  ├── Connects to previous weeks' patterns
│  └── Builds the narrative thread
│
SUNDAY
│
│  THE WEEKLY CATCH arrives.
│
│  Not bullet points. Not a task list.
│  A first-person, present-tense narrative.
│  Written in YOUR language patterns.
│  Using YOUR details, YOUR people, YOUR vision.
│  
│  It snaps you back.
│
│  If you dropped about being stuck on music →
│    you get a visualization of yourself IN the studio, creating.
│
│  If you dropped 4 anxious thoughts about money →
│    you get the pattern surfaced, reframed, and a line back to your own words
│    from 3 weeks ago when you felt abundant.
│
│  If you dropped random observations about your partner →
│    you see the thread: you mentioned her laugh three times.
│    Maybe that's the thing this week.
│
└── User reads. Feels something. Creates. Drops more next week.
    The loop feeds itself.
```

---

## 3. The Three Layers

### Layer 1: Drop (The Capture)

**What exists today:** Email, SMS, voice, web, API, Poe bot → drops into vault.
**What changes:** Almost nothing. Capture infra stays exactly as-is.

**What's new:**
- **Email prompts** — 2-3 per week, rotated, casual, designed to elicit raw material
- **Tone:** Not "Submit your weekly reflection." More like a friend texting "what happened today?"
- **Onboarding:** Reply to this email. That's it. You're in.
- **Attach anything:** Photos, screenshots, voice memos, forwarded emails. Whatever's on your mind.

> *"Keep it simple. You just respond there. No platform. You attach whatever."*

**The philosophy:** The quality of the Snapback is directly proportional to the rawness of the drops. We don't want polished entries. We want the 2am brain dump, the screenshot of a weird sign, the voice note from the car. That's the gold.

### Layer 2: The Weekly Catch (The Snapback Story)

This is the product. Everything else is infrastructure for this moment.

**What it IS:**
- A narrative — first person, present tense, written in the user's own cadence
- NLP-driven: emotional tone detection, phase-of-life awareness, language pattern matching
- Personalized: uses the user's actual names, places, goals, fears, language
- Connective: surfaces patterns the user didn't see — "you mentioned X three times this week"
- Reframing: when pendulum patterns are detected, applies Transurfing snap-back principles

**What it is NOT:**
- A summary ("This week you dropped 7 items about work, 3 about health...")
- A task list ("Your action items: 1. Call mom, 2. Check budget...")
- A generic wellness email ("Remember to practice self-care!")
- AI-generated slop with no connection to the actual human

**Delivery:** Email (HTML, beautiful, the Brooke theme energy but evolved for narrative). Also viewable on web dashboard.

**Cadence:** Weekly. Sunday delivery. This is intentional:
- Daily = noise. Another inbox to dread.
- Weekly = anticipation. "My Catch arrives tomorrow."
- Weekly = higher quality. More data points. Richer narrative.
- Weekly = less compute cost. One generation per user per week vs seven.

### Layer 3: The Intelligence Tab (The Vault)

**What exists today:** Vault search + Intelligence Map (the 3rd tab on the dashboard).
**What changes:** Nothing architecturally.

**What's new in context:** The Intelligence Tab becomes the "long game" view. The Snapback is your weekly pulse. The Intelligence Tab is your patterns over months, your themes over quarters, the meta-narrative of who you're becoming.

> *"The thing that we have on our third tab to organize it, the Snapback story to give you a narrative and digest the way you need to see it. It's there."*

---

## 4. What Changes From Current Architecture

| Component | Current | Snapback | Migration Difficulty |
|-----------|---------|----------|---------------------|
| **Digest cadence** | Daily | Weekly (Sunday) | Config change |
| **Digest format** | Multi-analyzer HTML (Brooke theme, bullet points, action items) | Narrative story (first-person, present tense, NLP-personalized) | New generation pipeline |
| **Digest name** | "Daily Digest" | "The Weekly Catch" / "Your Snapback" | Brand update |
| **Email prompts** | None (user-initiated drops only) | 2-3/week encouraging drops | New cron + templates |
| **Onboarding** | Web signup → drip sequence → first digest | "Reply to this email" → you're in | Simplified flow |
| **Brand position** | "Your Second Brain Has No Inbox" | "Drop all week. Catch it Sunday." | Evolution, not pivot |
| **Action items** | Extracted per-digest, Golden Thread queue | Woven into narrative, optional persistent queue | Compatible |
| **Analyzers** | Brutally Honest, Transurfing, Mom, Coach, etc. | Merged into ONE personalized voice per user | Major change |

### What Stays (Don't Touch)

- ✅ All capture infrastructure (email, SMS, voice, web, API, Poe)
- ✅ Hub classification and processing pipeline
- ✅ PostgreSQL vault + drop storage
- ✅ Intelligence Map (3rd tab)
- ✅ User management, lifecycle, admission
- ✅ Resend email infrastructure
- ✅ Dropper-Code autonomous pipeline
- ✅ BHA integration (separate product, cross-pollination remains)
- ✅ iOS Shortcut / API ingestion

---

## 5. Technical Integration

### 5a. Where Snapback Fits in the Existing Pipeline

```
CURRENT PIPELINE:
Drop → Hub ingests → Classify → Store → Daily digest cron → 
Multi-analyzer generation → HTML email → Send via Resend

SNAPBACK PIPELINE:
Drop → Hub ingests → Classify → Store → [NEW: NLP enrichment at ingest] → 
Weekly cron (Sunday) → Snapback narrative generation → HTML email → Send via Resend
                                                  ↑
                                    User Profile (language patterns,
                                    emotional baseline, entities,
                                    vision/goals, Transurfing phase)
```

### 5b. New Components

#### 1. `snapback_generator.py` — Core Narrative Engine

Adds a new narrative layer alongside the existing multi-analyzer digest system. The daily digest pipeline stays intact for all dashboard users — Snapback is additive, not a replacement. Core function:

```python
def generate_weekly_catch(user_id: str, week_start: date, week_end: date) -> SnapbackStory:
    """
    Generates the Weekly Catch narrative for a user.
    
    Pipeline:
    1. Pull all drops from the week (Hub API)
    2. Load user profile (language patterns, emotional baseline, entities)
    3. Detect themes, patterns, pendulum states
    4. Generate first-person narrative using user's own language
    5. Apply Transurfing snap-back reframing where appropriate
    6. Return formatted story with optional action threads
    """
```

**Model:** Claude Sonnet (cost-effective for weekly generation). Opus for users who need deeper narrative threading (premium tier, future).

**Prompt architecture:**
```
SYSTEM: You are writing a first-person narrative for {user_name}. 
Use their language patterns: {language_sample}.
Their world includes: {entities - people, places, projects, pets, goals}.
Their emotional baseline this week: {tone_analysis}.
Transurfing phase: {phase - awakening, detached, aligned, creating}.

INSTRUCTION: Write a present-tense visualization that:
- Addresses the dominant emotional thread of the week
- Surfaces patterns they may not see
- Uses their own words and details (not generic)
- If pendulum capture detected, gently reframe without being preachy
- Ends with forward energy, not a to-do list

DROPS THIS WEEK:
{drops}

PREVIOUS SNAPBACKS (for continuity):
{last_2_snapbacks_summary}
```

#### 2. `user_profile_builder.py` — The "How They Need To See It" Engine

This is the NLP personalization layer. Builds and maintains a living profile per user:

```python
class UserProfile:
    language_patterns: dict     # word frequency, sentence length, tone markers
    emotional_baseline: str     # "anxious-creative", "calm-productive", etc.
    entities: dict              # people, places, projects, pets — with context
    transurfing_phase: str      # where they are in the awakening arc
    vision_anchors: list        # their stated goals/dreams (Rancho Mirage, etc.)
    pendulum_triggers: list     # what pulls them off-center (comparison, money fear, etc.)
    drop_cadence: dict          # when they drop, how much, what types
    narrative_preference: str   # direct, gentle, funny, poetic — learned over time
```

**Updated:** On every drop ingestion (lightweight) + full rebuild weekly before Snapback generation.

**Storage:** New `user_profiles` table in PostgreSQL, or as structured JSON in the existing `user_metadata` column.

#### 3. `email_prompt_scheduler.py` — Drop Encouragement

```python
PROMPT_TEMPLATES = [
    "What's on your mind today? Just reply to this email.",
    "Anything weird happen this week? Drop it.",
    "What are you avoiding right now? (That's usually the good stuff.)",
    "Forward me something that made you think today.",
    "One word for how you're feeling. Go.",
    "What would you tell yourself from last week?",
    "Anything you want to remember about today?",
]

# Schedule: Tue, Thu, Sat — varied times, casual tone
# Rotated per user to avoid repetition
# Replies → standard drop ingestion pipeline (already works)
```

#### 4. `snapback_template.html` — The Weekly Catch Email

Not the current Brooke theme multi-section layout. Something new:

- Clean, readable, mobile-first
- No sections/headers — it's a narrative, reads like a letter
- Subtle visual metaphors (the catch, the snapback, momentum)
- One CTA at the bottom: "Drop something back" (reply = new drop)
- Optional: "View your Intelligence Map" link

### 5c. Database Changes

```sql
-- User profile for NLP personalization
ALTER TABLE users ADD COLUMN IF NOT EXISTS snapback_profile JSONB DEFAULT '{}';

-- Track Snapback stories (alongside existing digest tracking)
CREATE TABLE IF NOT EXISTS snapback_stories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL REFERENCES users(user_id),
    week_start DATE NOT NULL,
    week_end DATE NOT NULL,
    narrative TEXT NOT NULL,
    themes JSONB,          -- detected themes
    patterns JSONB,        -- detected patterns
    pendulum_state TEXT,   -- "captured", "aware", "aligned", "creating"
    drops_used INTEGER,    -- how many drops fed this story
    opened_at TIMESTAMP,   -- email tracking
    replied BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, week_start)
);

-- Index for quick weekly lookups
CREATE INDEX idx_snapback_user_week ON snapback_stories(user_id, week_start DESC);
```

### 5d. Cron Changes

| Current | Snapback |
|---------|----------|
| Daily digest cron (Hub scheduler) | Weekly Snapback cron (Sunday, configurable time per user timezone) |
| No email prompts | Tue/Thu/Sat drop encouragement emails |
| Daily metrics refresh (PRD maintenance) | Unchanged |

**Migration:** Don't delete the daily digest code. Feature-flag it. Some users (or B2B advisory use case) may still want daily. Snapback is the default for consumer users.

```python
# In digest scheduler:
if user.digest_mode == 'snapback':
    # Weekly generation (Sunday)
    if today.weekday() == 6:  # Sunday
        generate_weekly_catch(user.id, week_start, week_end)
elif user.digest_mode == 'daily':
    # Legacy daily digest
    generate_daily_digest(user.id)
```

---

## 6. NLP & Personalization: "The Way They Need To See It"

This is the moat. Anyone can build a weekly summary email. Nobody else has this:

### 6a. Emotional Tone Detection

**At ingest (every drop):**
- Sentiment analysis (positive/negative/neutral + intensity)
- Emotional state markers: anxious, excited, stuck, flowing, grieving, celebrating
- Pendulum detection: comparison language, fear patterns, external validation seeking

**At weekly synthesis:**
- Dominant emotional thread of the week
- Trajectory: getting better, getting worse, cycling, stable
- Pendulum capture events (if any)

### 6b. Language Pattern Matching

**The system learns how the user talks:**
- Vocabulary level and style (casual, intellectual, poetic, terse)
- Sentence rhythm (short punches vs. long flowing thoughts)
- Key phrases they repeat ("I feel like...", "the thing is...", "it's wild that...")
- Humor markers (sarcasm, self-deprecation, absurdism)

**The Snapback is written in THEIR voice, not the AI's.** Joey's Snapback sounds like Joey. Brooke's would sound like Brooke. Danny's would sound like a financial brief, because that's how Danny communicates.

### 6c. Transurfing Integration

For users who opt into Transurfing-aware processing (or show patterns consistent with it):

| Detection | Response |
|-----------|----------|
| Excessive importance → pendulum capture | Reduce importance. Show the pattern. Reframe. |
| Comparison to others | Mirror their own progress back. "Three weeks ago you said X. Look where you are." |
| Future anxiety | Present-tense visualization. Put them IN the desired state. |
| Flow state detected | Amplify. Don't interrupt. Celebrate the momentum. |
| Creative block | Surface previous creative moments from their own drops. "Remember March 11, 3am?" |

### 6d. Phase-of-Life Awareness

The system recognizes where the user IS, not where a generic AI thinks they should be:

- **Building phase:** More action-oriented catch. "You mentioned the project 5 times. Here's what you're actually building."
- **Healing phase:** Gentler. More reflective. "You used the word 'tired' four times. Let's look at what's underneath."
- **Creating phase:** Get out of the way. "You're on fire. Here's what you made this week. Keep going."
- **Stuck phase:** The core Snapback visualization. First person, present tense, their details. Snap them back.

---

## 7. The Email-First Experience

> *"You just respond there. No platform. You attach whatever."*

### Onboarding Flow

```
Step 1: User signs up (web, referral, BHA crossover, whatever)
Step 2: First email arrives:
        "Hey [name]. I'm your Snapback. 
         Reply to this email with literally anything on your mind. 
         A thought. A photo. A rant. A question. Whatever.
         I'll catch it."
Step 3: User replies.
Step 4: Auto-response: "Caught. 🧢 Drop more this week. Your first Weekly Catch arrives Sunday."
Step 5: Prompts arrive Tue/Thu/Sat. User replies to some, ignores others.
Step 6: Sunday: First Weekly Catch arrives.
Step 7: User reads it. Feels something. Replies with a reaction or a new drop.
Step 8: Loop continues.
```

**No app download.** No dashboard to learn. No onboarding tutorial. No feature walkthrough.

Just: reply to emails. Get your story on Sunday.

The dashboard (vault, Intelligence Map) exists for power users who want to dig deeper. But the core product lives entirely in email.

### Why Email Wins

- Zero friction capture (reply = drop)
- Universal (everyone has email)
- Async (drop whenever, catch on Sunday)
- Intimate (feels like a letter, not a notification)
- Attachable (photos, voice notes, forwards)
- Already built (Resend infra is production-ready)

---

## 8. Brand & Marketing

### The Weekly Catch

**Positioning:** "Drop all week. Catch it Sunday."

**Visual metaphor:** A snapback hat. A ball sailing over the fence. A hand reaching up to grab something that was flying by. Sports energy but not sports — universal.

**Tone:** Casual. Smart. Never corporate. Never "wellness." Never "productivity hack." More like a friend who actually listens and then says the thing you needed to hear.

### Copy Direction

**Homepage:**
> Your week is full of moments that fly by.
> Random thoughts. Late-night feelings. Screenshots of things that mattered for a second.
> 
> Drop them all week. We catch everything.
> Sunday, you get The Weekly Catch — your week, told back to you as a story.
> Not a summary. Not a task list. The narrative you need to see.
> 
> **Reply to start. That's it.**

**Tagline options:**
- "Drop it. Catch it Sunday."
- "The Weekly Catch."
- "Your week has a story. We tell it back to you."
- "Snapback. 🧢"

### Brand Evolution (Not a Pivot)

DropAnywhere → DropAnywhere with Snapback. The name stays. The capture stays. The promise evolves:

| Old | New |
|-----|-----|
| "Your Second Brain Has No Inbox" | "Drop all week. Catch it Sunday." |
| Daily digest | Weekly Catch |
| Summary + action items | First-person narrative |
| Multiple analyzer voices | One personalized voice (yours) |
| Productivity tool | Self-awareness tool that drives creation |

---

## 9. Revenue Model

### Why Weekly > Daily for the Business

| Factor | Daily | Weekly |
|--------|-------|--------|
| **Compute cost** | 7 LLM generations/user/week | 1 generation/user/week (86% reduction) |
| **Quality** | Thin (1 day of data) | Rich (7 days of data, real patterns) |
| **User anticipation** | "Another email" | "My Catch arrives tomorrow" |
| **Engagement** | Digest fatigue after 2 weeks | Weekly ritual, higher open rates |
| **Churn** | Missing one day = missed digest | Missing a day = no consequence |
| **Email volume** | 7/week + prompts | 1/week + 3 prompts = 4/week total |

### Pricing (Updated)

| Tier | Price | What |
|------|-------|------|
| **Free** | $0 | 3 drops/week, basic Weekly Catch (summary, not full narrative) |
| **Pro** | $9/mo | Unlimited drops, full Snapback narrative, Intelligence Map, email prompts |
| **Snapback+** | $19/mo | Everything in Pro + Transurfing-aware processing, custom visualization style, priority generation |
| **Advisory** | $49/mo | B2B: white-label Weekly Catch for coaches/advisors to send to their clients |

**Key insight:** The free→Pro conversion is driven by the difference between a summary and a story. When someone gets the free version and sees what the narrative COULD be, they upgrade. The Snapback IS the paywall.

### Unit Economics (at Scale)

- **Cost per Snapback:** ~$0.02-0.05 (Sonnet, one generation per user per week)
- **Cost per email prompt:** ~$0.001 (template, no LLM)
- **Cost per user per month:** ~$0.10-0.25
- **Pro revenue per user per month:** $9.00
- **Gross margin:** >97%

---

## 10. Connection to Existing PRD Sections

| PRD Section | Connection to Snapback |
|-------------|----------------------|
| **5.12 Emotional "Snap Back" Protocol** | **This IS it.** Section 5.12 described it as a future P2 feature. Tonight proved it's the entire product. Promote from P2 to the core experience. |
| **5.1 Smart Ingestion / Classification v2** | Required. The Snapback narrative quality depends on drop classification. Emotional tone, entity extraction, temporal intent — all feed the story. |
| **5.4 Digest Personalization** | Compatible. Multi-analyzer daily digest stays intact for dashboard users. Snapback adds a weekly narrative layer alongside it. Users choose via `digest_mode` flag. |
| **5.17 Context-Aware Daily Briefing** | Compatible. Daily briefing can coexist with Weekly Catch — different cadence, different purpose. Daily = operational, Weekly = reflective narrative. |
| **5.11 Unified Drop Classification v2** | Dependency. The `drop_type`, `area` tags, `completable` flag, entity extraction — all required for narrative generation quality. |
| **5.13 B2B Advisory Loop** | Compatible. Advisory Mode = white-label Weekly Catch. Danny gets his own Snapback, curated by Joey. |
| **Gate D: Invisible Assistant** | Snapback IS the invisible assistant in email form. No app, no UI, no platform — just email in, story out. |
| **6d Golden Thread** | Compatible. Persistent actions can be woven INTO the narrative ("You said you'd call Robin. Did you?") instead of a separate dashboard widget. |
| **Section 2: The Vision** | "Drop it. Forget it. Wake up lighter." → "Drop it. Forget it. Catch it Sunday." Same energy. More specific. |

---

## 11. Implementation Roadmap

### Phase 1: MVP (1-2 weeks)

- [ ] Build `snapback_generator.py` with basic narrative generation
- [ ] Create `user_profiles` table (or JSON column)
- [ ] Weekly cron job (Sunday) replacing/alongside daily digest
- [ ] Basic email template for Weekly Catch
- [ ] Feature flag: `digest_mode = 'snapback' | 'daily'`
- [ ] Test with Joey (he's user zero — the prototype already worked tonight)

### Phase 2: Personalization (2-4 weeks)

- [ ] User profile builder with language pattern learning
- [ ] Emotional tone detection at ingest
- [ ] Transurfing phase detection
- [ ] Email prompt scheduler (Tue/Thu/Sat)
- [ ] Previous-Snapback continuity in generation prompt
- [ ] Beta with 5-10 willing users from current base

### Phase 3: Scale + Revenue (Month 2-3)

- [ ] Free vs Pro narrative differentiation
- [ ] Snapback+ tier with Transurfing-aware processing
- [ ] Advisory Mode (white-label Weekly Catch)
- [ ] Onboarding flow rewrite (email-first, no app)
- [ ] Brand update: "The Weekly Catch" positioning
- [ ] Marketing site copy refresh

### Phase 4: Intelligence (Month 3+)

- [ ] Cross-week pattern detection ("You've mentioned this 3 weeks in a row")
- [ ] Seasonal/lifecycle awareness ("It's been a year since you started dropping about X")
- [ ] Multi-modal narratives (include user's photos, voice snippets in the Catch)
- [ ] Community features (opt-in anonymous pattern sharing: "312 people snapped back from creative blocks this week")

---

## 12. The Moment

This document exists because of a real moment. Not a whiteboard session, not a strategy meeting, not a competitive analysis.

Joey was stuck at 3am. He dropped a feeling. The system caught it and told him his own story in a way that made him get up and create.

Then he did it again. And again. And then he saw it:

**The capture infrastructure exists.** 52 users, 589 drops, 147 digests, email/SMS/voice/web/API ingestion — all live.

**The processing exists.** Hub classification, entity extraction, vault storage, Intelligence Map — all live.

**The delivery exists.** Resend email, Brooke theme, HTML templates, cron scheduling — all live.

**The only thing that didn't exist was the narrative.** The story told back in first person. The snap back.

Now it does.

```
Drop → Catch → Snap Back → Create → Drop
```

That's the loop. That's the product. That's DropAnywhere.

**🧢**

---

*"Then I send you the good stuff. The Snapback story to give you a narrative and digest the way you need to see it. It's there."*
— Joey, 3:00 AM, March 11, 2026

