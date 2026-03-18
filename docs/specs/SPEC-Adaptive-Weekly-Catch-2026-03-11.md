# Adaptive Weekly Catch — The Intelligence Layer That Makes It Personal

**Author:** Claw + Joey  
**Date:** 2026-03-11  
**Status:** Draft — spec for review  
**Companion to:** `SNAPBACK-INTEGRATION.md` (the engine), `snapback-email-prompts.md` (the 7-day sequence), `SPEC-User-Scenario-Matrix.md` (the lifecycle)  
**Purpose:** Define how the Weekly Catch adapts to WHO the user is, what they need, and where they are — not just what they dropped.

---

## 0. The Problem This Solves

The current Snapback spec assumes one use case: **The Stuck One** ("I have something stuck in my head"). The 7-day sequence asks them to go deep on one problem and delivers a narrative Snapback on Day 8.

That works beautifully for Joey at 3am. It doesn't work for:

| Person | What They'd Say | Why Current Spec Fails |
|--------|----------------|----------------------|
| Danny | "Just send me the brief" | He doesn't have a "problem." He needs organized intelligence. |
| A founder | "I have 12 things going on" | They don't need a meditation. They need clarity on what matters. |
| A journaler | "I just want to write" | They don't need prompts. They need a mirror. |
| Brooke | "I want to track our challenge" | She needs accountability + celebration, not a narrative. |
| A student | "I'm applying to colleges" | They need structure, not soul-searching. |
| Someone's mom | "I just want to stay connected" | She needs a gentle weekly recap of what she shared, not deep therapy. |
| Someone who doesn't know they have a problem | "I dunno, just trying it" | The current "tell me what's stuck" scares them off. |

**The fix:** The Weekly Catch isn't one output. It's the RIGHT output — determined by who the user is, how they entered, what they're dropping, and how they respond to the system over time.

---

## 1. The Three Intelligence Layers

### Layer 1: Entry Persona — Who Shows Up at the Door

Determined at signup (or inferred within 48 hours). This sets the initial **catch mode** and the tone/pacing of email prompts during the first week.

| Entry Persona | Detection Method | Initial Catch Mode | Prompt Tone |
|---------------|-----------------|-------------------|-------------|
| **The Stuck One** | Signup intent = "work through something" OR first drop is emotional/stuck | `narrative` | Deep, provocative, one question per email |
| **The Scattered One** | Signup intent = "too much going on" OR first 3 drops are unrelated topics | `clarity` | Organizing, connecting, "what's the thread?" |
| **The Builder** | Signup intent = "working on a project" OR drops contain tasks/plans | `action` | Direct, progress-focused, "what moved today?" |
| **The Curious One** | No clear intent, minimal first drops, exploratory language | `adaptive` | Warm, casual, low-pressure, "just drop whatever" |
| **The Invisible** | BHA crossover, Danny-style advisory, or referred by someone else | `advisory` | Minimal prompts, system learns silently from ingest |
| **The Journaler** | Drops are long, reflective, self-directed — no questions asked | `mirror` | Sparse, never interrupts their flow, reflects back |

**How it's captured:**

Option A — Explicit (during onboarding):
```
What brings you here?
[ ] I need to work through something     → narrative
[ ] I have too much going on              → clarity  
[ ] I'm building/creating something       → action
[ ] Just curious, show me what you got    → adaptive
[ ] Someone told me to try this           → adaptive
```

Option B — Inferred (for email-only/BHA/invisible users):
- Analyze first 3 drops within 48 hours
- Use drop classification (5.11) to detect: emotional content → narrative, task content → action, mixed → clarity, minimal → adaptive
- Set `catch_mode` automatically. User never has to choose.

Option C — Hybrid: Ask if they come through the web. Infer if they come through email or BHA.

**Key principle:** The user should NEVER feel like they picked the wrong box. The system adjusts regardless of initial selection. This is just the starting point.

---

### Layer 2: Drop Pattern Detection — What They're Actually Saying

After 3+ drops, the system starts reading patterns in WHAT the user is dropping. This can confirm, refine, or completely override the entry persona.

#### Drop Classification at Ingest

Every drop gets classified at ingest time (extends the existing 5.11 Unified Drop Classification):

```python
class DropSignal:
    # Existing fields from 5.11
    drop_type: str        # thought, task, feeling, question, resource, observation
    area: str             # work, health, relationships, creativity, rest, finance, identity
    completable: bool     # is this actionable?
    
    # NEW: Catch-relevant signals
    emotional_intensity: float   # 0.0 (neutral) → 1.0 (raw/intense)
    temporal_intent: str         # past (reflecting), present (processing), future (planning)
    energy_direction: str        # expanding (excited/curious) | contracting (stuck/anxious) | neutral
    self_reference_depth: str    # surface ("I did X") | mid ("I feel X") | deep ("I am X")
    pendulum_markers: list       # comparison, external_validation, fear, urgency, should_language
    entities_mentioned: list     # people, places, projects, dates — extracted
    recurring_theme_match: str   # null or theme_id if matches a pattern from previous weeks
```

#### Weekly Pattern Synthesis (runs before Catch generation)

```python
def synthesize_week(user_id: str, drops: list[Drop]) -> WeeklySignals:
    """
    Reads all drops from the week and produces:
    - dominant_mode: narrative | clarity | action | mirror | advisory
    - emotional_arc: trajectory over the week (rising, falling, cycling, stable)
    - theme_clusters: groups of related drops
    - pendulum_state: captured | aware | aligned | creating
    - energy_balance: which life domains got attention, which got ignored
    - golden_thread: the ONE thing connecting most of their drops
    - surprise_connection: something they dropped that connects to something 
      from 2+ weeks ago that they probably forgot about
    """
```

#### Mode Override Logic

The catch mode for any given week is determined by THIS WEEK'S drops, not the entry persona:

```python
def determine_catch_mode(user: UserProfile, weekly_signals: WeeklySignals) -> str:
    """
    Priority order:
    1. If 60%+ drops are emotional/intense → narrative (they need a snapback)
    2. If 60%+ drops are tasks/plans/projects → action (they need a progress report)
    3. If drops span 4+ unrelated areas → clarity (they need organizing)
    4. If drops are all long, self-reflective → mirror (get out of the way)
    5. If < 3 drops this week → gentle (don't over-generate from thin data)
    6. Fall back to user's preferred mode (learned over time)
    7. Fall back to entry persona default
    """
```

**The key insight:** The same user might get a narrative Catch one week and an action Catch the next. The system flexes to what they actually need THIS week, not what they needed when they signed up.

---

### Layer 3: Progressive Disclosure — The Product Reveals Itself Over Time

The Catch gets smarter the longer someone uses it. This isn't just "more data = better output" — it's **the Catch itself teaching the user how to drop better**.

#### Week 1-2: The Mirror Phase
- Catch reflects back what they said, organized and connected
- Tone: warm, nonjudgmental, "here's what I heard"
- **Embedded prompt:** "💡 Your richest drop this week was the voice note on Tuesday. Something about talking out loud unlocks more detail."
- **Goal:** User learns that raw > polished, and the system actually listens

#### Week 3-4: The Pattern Phase
- Catch starts surfacing recurring themes: "You've mentioned [X] three weeks in a row"
- Connections between drops they didn't see: "The anxiety about the deadline and the thought about your dad — they both use the word 'enough'"
- **Embedded prompt:** "🔄 You tend to drop more on Tuesdays and Thursdays. Something about mid-week opens you up."
- **Goal:** User realizes the system sees what they can't

#### Week 5-8: The Anticipation Phase
- Catch predicts what they might drop next week based on patterns: "Last month you got quiet before a big decision. This week you're quiet again. Is something brewing?"
- Cross-references with their own history: "Remember three weeks ago when you said [X]? Look where that led."
- **Embedded prompt:** "📊 Your 30-day pattern shows you cycle between creative bursts and organizing phases. You're entering a creative phase."
- **Goal:** User starts anticipating their own Catch. "What will it say about this week?"

#### Month 3+: The Oracle Phase
- Catch draws from months of context
- Can reference seasons, anniversaries, growth arcs: "A year ago this month, you wrote [X]. Look at you now."
- Genuinely novel insights because it has a longitudinal view no human friend has
- **Goal:** User can't imagine NOT dropping. The Catch is part of their self-understanding.

#### Progressive Disclosure Prompts — Built Into Every Catch

Every Weekly Catch includes ONE subtle learning prompt. Never more than one. Never preachy. Format:

```
[section break or natural paragraph end]

💡 [Observation about their dropping pattern + suggestion]
```

Examples by week:
- Week 1: "Your longest drop was 3 sentences. The messier you go, the better this gets. Try a voice note next week."
- Week 2: "You dropped 4 times this week — all between 10pm and midnight. Night thoughts hit different. Keep going."
- Week 4: "You've never mentioned [domain] in a drop. Not saying you should — just noticing."
- Week 6: "Your drops shifted from 'I should' language to 'I want' language around Week 4. That's real."
- Week 10: "You've used the word 'stuck' 23 times in 10 weeks. This week: zero. Let that land."

---

## 2. The Five Catch Modes (Output Templates)

Each mode produces a fundamentally different Weekly Catch. Same email. Same sender. Completely different experience.

### Mode 1: NARRATIVE (The Snapback)

**For:** Users in emotional/stuck/creative states. When the dominant signal is feeling, not doing.

**Format:** First-person, present-tense visualization. Written in the user's own language patterns. Uses their real names, places, pets, goals. The original Snapback experience from the 3am session.

**Structure:**
```
Subject: Your Weekly Catch 🧢

[Opening — grounds them in a specific moment from their week]

[Narrative body — 3-5 paragraphs, first person, present tense]
  - Weaves their drops into a coherent emotional arc
  - Surfaces the pattern they couldn't see
  - If pendulum captured → gently reframes using their own words
  - If creative block → puts them IN the moment of creating
  - Uses their actual details (Brooke, FL Studio, the pool, etc.)

[The Snap — the one line that makes them go "oh shit"]

[Soft landing — forward energy, not a to-do list]

💡 [Progressive disclosure prompt]

---
Drop something back → just reply to this email
```

**When to use:** emotional_intensity > 0.6 on 60%+ of drops, OR user is in `narrative` mode and drops confirm it.

**Generation model:** Claude Sonnet (or Opus for premium tier — the quality difference matters here).

**Screenshot opportunity:** The email itself IS the screenshot. Real narrative. Real names. Real emotion. This is what you show people: "This is what YOUR Catch could look like."

---

### Mode 2: CLARITY (The Weekly Clarity Report)

**For:** Scattered users. Multiple unrelated domains. Too much going on. Need someone to organize their week for them.

**Format:** Organized by theme, with connections drawn between seemingly unrelated drops. Reads like a smart friend who says "hey, I notice these three things are actually one thing."

**Structure:**
```
Subject: Your Weekly Catch 🧢

[Opening — acknowledges the scatter: "Big week. Let's untangle it."]

🧵 THE THREAD
[One sentence that connects the disparate drops into a single insight]

📦 WHAT YOU'RE CARRYING (3-5 theme clusters)

[Theme 1: Work/Project Name]
  - What you said: [2-3 drop excerpts]
  - What I notice: [one-line insight]

[Theme 2: Relationship/Person]
  - What you said: [drop excerpts]  
  - What I notice: [insight]

[Theme 3: The thing you mentioned once but it felt big]
  - What you said: [drop excerpt]
  - Why it stood out: [connection to a previous week or another theme]

⚡ THE CATCH
[The one thing they need to see — the connection they missed]

💡 [Progressive disclosure prompt]

---
Drop something back → reply
```

**When to use:** Drops span 4+ areas, no dominant emotional thread, user entered as "scattered" or drops are topically diverse.

**Screenshot opportunity:** The theme clustering. Show a real example of 7 random drops turning into 3 organized themes with a golden thread connecting them.

---

### Mode 3: ACTION (The Progress Catch)

**For:** Builders. Project people. Founders. People whose drops are tasks, plans, milestones, and "I need to do X."

**Format:** Progress-oriented. What moved. What's stuck. What's next. Integrates with the Golden Thread persistent action queue.

**Structure:**
```
Subject: Your Weekly Catch 🧢

[Opening — energy of a co-founder check-in, not a project manager]

✅ WHAT MOVED
  - [Drop-derived accomplishments and progress signals]
  - [Connections: "You said you'd do X on Tuesday. By Thursday you'd done X and Y."]

🔄 WHAT'S CIRCLING
  - [Recurring items: things mentioned multiple times without resolution]
  - [Pattern: "This is the 3rd week you've mentioned [X]. It's either important or it's noise. Which one?"]

🎯 YOUR NEXT MOVE
  - [1-2 priority actions derived from THIS week's drops]
  - [Connected to Golden Thread if persistent actions exist]

⚡ THE CATCH
[One strategic insight they didn't see: "You spent 80% of your drops on [project A] but mentioned [project B] is the one that excites you. Interesting."]

💡 [Progressive disclosure prompt]

---
Drop something back → reply
```

**When to use:** 60%+ drops are tasks/plans/projects, or user entered as "builder."

**Screenshot opportunity:** The "What Moved vs. What's Circling" split. Real tasks. Real progress. Show the difference between a to-do list and an intelligent progress report.

---

### Mode 4: MIRROR (The Quiet Catch)

**For:** Journalers. Self-reflective writers. People who drop long, thoughtful entries and don't need prompts — they need someone to simply show them what they said, organized.

**Format:** Minimal AI voice. Heavy on their own words. The system arranges and highlights but doesn't interpret. Like looking in a mirror that has better lighting.

**Structure:**
```
Subject: Your Weekly Catch 🧢

[No opening commentary. Just straight into it.]

YOUR WORDS THIS WEEK

"[Their most striking sentence, pulled verbatim]"

---

[Their drops, lightly organized by theme, mostly verbatim with
 small connecting phrases. The system's voice is barely there.
 Think: a beautifully edited journal entry, not an AI analysis.]

---

"[Their closing sentence from the last drop of the week]"

---

What I noticed (keeping it brief):
→ [One pattern, stated simply]
→ [One surprise connection]

💡 [Progressive disclosure prompt]

---
Drop something back → reply
```

**When to use:** Drops are long (avg > 150 words), self-reflective, self-directed. User doesn't ask questions — they process through writing.

**Screenshot opportunity:** The verbatim quotes with minimal commentary. Show that the system respects the user's voice and doesn't try to out-think them.

---

### Mode 5: ADVISORY (The Invisible Catch)

**For:** Danny-style recipients. People who are IN the system but didn't necessarily put themselves there. A human curator (Joey, a coach, an advisor) is in the loop.

**Format:** Clean intelligence brief. No therapy. No narrative. Facts, patterns, recommendations.

**Structure:**
```
Subject: Your Weekly Brief 📋

[Opening — professional but warm, like a trusted advisor]

HIGHLIGHTS
  • [Key insight 1 — derived from their email replies/drops]
  • [Key insight 2]
  • [Key insight 3]

PATTERNS
  → [What's changed since last week]
  → [What's consistent — strengths to leverage]

RECOMMENDED FOCUS
  1. [Priority action with brief rationale]
  2. [Secondary action]

[Optional: human curator's note — if the advisor (Joey) has added context]

---
Reply to add more context for next week's brief
```

**When to use:** User's entry path is `advisory` (set by the curator, not the user). Or: user drops are short/sparse and factual — they're reporting in, not reflecting.

**Screenshot opportunity:** Show the Danny use case. An email reply turns into an organized brief. The recipient doesn't even know they're "using a product."

---

### Mode 6: GENTLE (The Sparse Week Catch)

**For:** Weeks with < 3 drops. Not enough data to generate a full Catch. Instead of sending nothing or sending a thin output, acknowledge the quiet and keep the loop alive.

**Structure:**
```
Subject: Your Weekly Catch 🧢

Hey —

Quiet week. That's okay. Sometimes the best thing is just... not.

[If 1-2 drops exist:]
You did drop this:
> "[Their drop, verbatim]"

That's enough. No need to analyze a single thought to death.

[If 0 drops:]
Nothing dropped this week. No judgment. The inbox will be here when something comes up.

One thought from last week that stuck with me:
> "[A notable drop from the previous week]"

Still resonating? Or has it moved? Drop me a line.

💡 Reminder: even a one-sentence drop on a random Tuesday gives next week's Catch something to work with.

---
Reply whenever
```

**When to use:** Fewer than 3 drops in the week. Don't over-generate from thin data. Don't ghost them either.

---

## 3. The Adaptive Email Prompt Sequence

The existing 7-day sequence (in `snapback-email-prompts.md`) is the **narrative** track. Each catch mode needs its own prompt cadence.

### How Prompts Adapt Per Mode

| Day | Narrative (Stuck) | Clarity (Scattered) | Action (Builder) | Mirror (Journaler) | Advisory (Invisible) | Adaptive (New) |
|-----|-------------------|--------------------|-----------------|--------------------|---------------------|----------------|
| 1 | "Tell me what's stuck" | "What's all on your plate?" | "What are you building this week?" | "Write whatever comes to mind" | (No prompt — drops come from email replies to their advisor) | "Hey, just drop anything. Literally anything." |
| 2 | "Why now?" | "Which one is loudest?" | "What moved yesterday?" | (No prompt — they write when they write) | (Silent) | "What's on your mind today?" |
| 3 | "What did you stop doing?" | "What's connected that shouldn't be?" | "What's stuck? What needs unblocking?" | (Silent unless 0 drops) | (Silent) | "Random: what's something you noticed today?" |
| 4 | "What are you avoiding?" | "If you could only keep 2, which ones?" | "Who do you need help from?" | "How's the writing going?" (only prompt) | (Silent) | "Quick one — how are you feeling about things?" |
| 5 | "What would surprise them?" | "What's the one nobody knows about?" | "What would you cut if you had to?" | (Silent) | (Silent) | "Almost done — what's been on repeat in your head?" |
| 6 | "If it resolved overnight..." | "Rank them. Gut feeling." | "End of week: what shipped and what didn't?" | (Silent) | (Silent) | "If you had to describe this week in one word?" |
| 7 | "What surprised you?" | "Look at your list. What's missing?" | "Next week — what's the ONE thing?" | "Read back your drops. What stands out?" | "Quick check-in before your brief" | "Last one before your first Catch. Drop anything." |

### Prompt Cadence Rules

1. **Never send a prompt within 4 hours of a user-initiated drop.** They're already engaged. Don't interrupt.
2. **If they replied to the last prompt within 2 hours, skip the next scheduled prompt.** They're in flow.
3. **If they haven't dropped in 3+ days (during the trial), send a gentle nudge** — not the next prompt. The nudge: *"Hey — no pressure. Even one sentence keeps this going. What's on your mind?"*
4. **Time prompts to the user's natural drop window.** Track when they typically drop and send prompts 30-60 minutes before that window. If they always drop at 10pm, prompt at 9:30pm.
5. **For journalers/mirror users:** Minimal prompts. They don't need encouragement — they need space. One prompt max every 3 days, and only if they've gone silent.
6. **For advisory users:** Zero system prompts. Their drops come from replying to their advisor's emails. The system is invisible.

### Mid-Week Encouragement (During Trial Week)

Between prompts, the system sends **one** micro-acknowledgment per drop. Not a full reply. Just enough to close the loop:

| Drop Type | Acknowledgment |
|-----------|---------------|
| Text drop (short) | "Caught. 🧢" |
| Text drop (long/emotional) | "Caught. That one felt important. 🧢" |
| Voice note | "Caught the voice note. Those always hit different. 🧢" |
| Photo/attachment | "Caught it. 📸🧢" |
| Reply to prompt | "Caught. Keep going." |
| 3rd drop of the week | "That's three this week. Your Catch is going to be good. 🧢" |
| 5th+ drop | "You're feeding the machine. Sunday's going to be interesting. 🧢" |

These are NOT AI-generated. They're templates. Fast, cheap, human-feeling. The acknowledgment matters because it closes the feedback loop — "someone heard me."

---

## 4. The Onboarding Decision Tree

How does the system know which track to put someone on? Here's the complete flow:

```
USER ARRIVES
│
├─ Via web signup
│   ├─ Answered "What brings you here?" → map to entry persona
│   └─ Skipped the question → set to adaptive
│
├─ Via email (reply to "Try it" email, forward, or cold email to hello@)
│   └─ Analyze first drop → infer entry persona within 48h
│
├─ Via BHA crossover (auto-synced conversations)
│   ├─ Has 3+ BHA sessions → set to adaptive (we have data)
│   └─ Has 1-2 BHA sessions → set to adaptive (need more)
│
├─ Via advisory (Joey/coach set them up)
│   └─ Set to advisory (curator chose this)
│
├─ Via Poe DropAnywhere bot
│   └─ Set to adaptive (email verification → full onboarding)
│
└─ Via referral link
    └─ Inherit the referrer's suggestion? Or just adaptive.
    
AFTER 3+ DROPS (within first week):
│
├─ Run drop classification on all drops
├─ Compute: dominant type, emotional intensity, area diversity
├─ Override entry persona if signals are strong:
│   │
│   ├─ 60%+ emotional/intense → switch to narrative
│   ├─ 60%+ tasks/plans → switch to action
│   ├─ 4+ different areas → switch to clarity
│   ├─ Avg drop > 150 words, self-reflective → switch to mirror
│   └─ Mixed/unclear → stay adaptive (system chooses at Catch time)
│
└─ Set catch_mode on user profile. This is now their default.
   But EVERY week, the weekly synthesis can override for that specific Catch.
```

---

## 5. Real Screenshots — Not Fake Ones

Joey's mandate: **"Not fake ones — legit ones that showcase stuff specific to their scenario."**

### Screenshot Strategy

We need real Catch outputs for each of the 5 modes. These become the marketing material. Here's how:

#### Phase 1: Joey = User Zero (Week of Mar 12-18)
1. Joey runs the 7-day cycle himself (P0-8e in Dropper-Code queue)
2. System generates his first Weekly Catch on Day 8
3. **Screenshot 1:** Joey's narrative Catch (real drops → real Snapback story)
4. This is the hero screenshot for the landing page

#### Phase 2: Brooke + Close Circle (Week of Mar 19-25)
1. Invite Brooke (she's doing the songwriting challenge — natural drops)
2. Invite Danny (already in advisory mode — his brief becomes a screenshot)
3. Invite 1-2 friends who represent different personas
4. **Screenshot 2:** Brooke's Catch (different mode — probably action/accountability for the challenge)
5. **Screenshot 3:** Danny's Advisory brief (professional, clean, intelligent)

#### Phase 3: Screenshots From Each Mode
With real users in each track, capture:

| Screenshot | Source | Shows |
|------------|--------|-------|
| **The Narrative Snapback** | Joey's Catch | Raw drops → first-person story with real details |
| **The Clarity Report** | A scattered user | 7 random drops → 3 organized themes + golden thread |
| **The Progress Catch** | A builder user | Tasks/projects → what moved, what's circling, next move |
| **The Mirror** | A journaler | Their own words, beautifully organized, minimal AI voice |
| **The Advisory Brief** | Danny's brief | Email replies → organized intelligence brief |
| **The Email Prompts** | Day 1-7 sequence | Real emails in real inbox. Show the simplicity. |
| **The 🧢 Acknowledgment** | Mid-week | "Caught. 🧢" — show the micro-feedback loop |
| **The Progressive Disclosure** | Week 4+ user | "You've mentioned X 3 weeks in a row" |

#### Screenshot Format
- **Mobile-first** — most people will see the landing page on their phone
- **Real email client** (Apple Mail, Gmail) — not a mockup
- **Personal details redacted minimally** — enough to feel real, not enough to identify someone
- **Annotated** — subtle callouts: "← This came from a voice note at 2am" / "← Your own words, reflected back"

### No Fake Testimonials. No Generic Examples.

Every screenshot on the landing page is from a real user running the real system. If we don't have enough modes covered yet, we leave the space empty and fill it as real users produce real Catches. Authenticity IS the marketing.

---

## 6. Database Schema Changes

Extends the existing schema from `SNAPBACK-INTEGRATION.md`:

```sql
-- Extend user profile with catch intelligence
ALTER TABLE users ADD COLUMN IF NOT EXISTS catch_config JSONB DEFAULT '{
    "entry_persona": null,
    "catch_mode": "adaptive",
    "preferred_mode": null,
    "prompt_cadence": "standard",
    "language_patterns": {},
    "emotional_baseline": null,
    "entities": {},
    "drop_windows": [],
    "transurfing_phase": null,
    "progressive_stage": "mirror",
    "weeks_active": 0,
    "last_mode_used": null
}';

-- Extend drops with catch-relevant classification
ALTER TABLE vault_items ADD COLUMN IF NOT EXISTS catch_signals JSONB DEFAULT '{
    "emotional_intensity": null,
    "temporal_intent": null,
    "energy_direction": null,
    "self_reference_depth": null,
    "pendulum_markers": [],
    "recurring_theme_match": null
}';

-- Extend snapback_stories with mode tracking
ALTER TABLE snapback_stories ADD COLUMN IF NOT EXISTS catch_mode TEXT DEFAULT 'adaptive';
ALTER TABLE snapback_stories ADD COLUMN IF NOT EXISTS mode_signals JSONB;
ALTER TABLE snapback_stories ADD COLUMN IF NOT EXISTS progressive_prompt TEXT;
ALTER TABLE snapback_stories ADD COLUMN IF NOT EXISTS user_responded BOOLEAN DEFAULT FALSE;
ALTER TABLE snapback_stories ADD COLUMN IF NOT EXISTS response_drop_id TEXT;

-- Email prompt tracking
CREATE TABLE IF NOT EXISTS catch_prompts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL REFERENCES users(user_id),
    week_start DATE NOT NULL,
    day_number INTEGER NOT NULL,      -- 1-7
    template_id TEXT NOT NULL,         -- which prompt was sent
    catch_mode TEXT NOT NULL,          -- mode that determined the prompt
    sent_at TIMESTAMP NOT NULL,
    opened_at TIMESTAMP,
    replied_at TIMESTAMP,
    reply_drop_id TEXT,               -- links to the drop created by their reply
    skipped BOOLEAN DEFAULT FALSE,    -- was this prompt skipped (user already active)
    skip_reason TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Track mode transitions over time
CREATE TABLE IF NOT EXISTS catch_mode_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL REFERENCES users(user_id),
    week_start DATE NOT NULL,
    determined_mode TEXT NOT NULL,
    entry_persona TEXT,
    override_reason TEXT,             -- "60% emotional drops" or "user preference"
    signals JSONB,                    -- the raw signals that led to this mode
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 7. The Generation Pipeline

### Step-by-Step: From Drops to Catch

```
WEEKLY CRON (Sunday, user's timezone, configurable)
│
├── 1. GATHER: Pull all drops since last Catch
│       - Vault items where created_at > last_catch_date
│       - Include: text, source, catch_signals, timestamps
│       - Also pull: last 2 Catches (for continuity)
│       - Also pull: user catch_config (profile)
│
├── 2. SYNTHESIZE: Run weekly pattern analysis
│       - Cluster drops by theme (embedding similarity)
│       - Compute emotional arc (intensity over time)
│       - Detect pendulum markers
│       - Identify golden thread (strongest cross-drop connection)
│       - Find surprise connection (this week ↔ 3+ weeks ago)
│       - Calculate energy balance across life domains
│
├── 3. DETERMINE MODE: Pick this week's catch mode
│       - Apply override logic (see Layer 2 above)
│       - Log to catch_mode_history
│       - If mode differs from last week, note it
│
├── 4. GENERATE: Produce the Catch
│       - Select prompt template for determined mode
│       - Inject: user profile, drops, weekly signals, last 2 catches
│       - Generate via Claude Sonnet (or Opus for premium)
│       - Include progressive disclosure prompt for their stage
│
├── 5. QUALITY CHECK: Validate output
│       - Contains user's actual details (not generic)
│       - Matches the mode's format/structure
│       - No hallucinated entities (only reference real drops)
│       - Appropriate length for mode (narrative=long, action=tight, mirror=medium)
│       - Progressive prompt is relevant and not repeated
│
├── 6. RENDER: Build email
│       - Apply mode-appropriate HTML template
│       - Mobile-first responsive design
│       - Include reply CTA
│       - Track open/click via Resend
│
└── 7. DELIVER: Send via Resend
        - Deliver at user's preferred time (or default 9am local)
        - Log to snapback_stories table
        - Update user's progressive_stage if milestone reached
```

### Prompt Architecture (Per Mode)

Each mode has a distinct system prompt. The user-facing content is assembled from their drops and profile.

**Shared preamble (all modes):**
```
You are generating a Weekly Catch for {user_name}.

CRITICAL RULES:
- Only reference things from their actual drops. Never invent details.
- Use their language patterns: {language_sample}
- Their world includes: {entities}
- Their emotional baseline this week: {emotional_arc}
- They've been using this system for {weeks_active} weeks.
- Previous catches for continuity: {last_2_catches_summary}
- Progressive stage: {progressive_stage}

Include exactly ONE progressive disclosure prompt (the 💡 line) based on their stage.
```

**Mode-specific instruction appended:**

- **Narrative:** "Write in first person, present tense. This is a visualization. Put them IN the moment. The goal is to snap them back from {pendulum_state} to their own frequency."
- **Clarity:** "Organize their drops into 2-4 theme clusters. Find the golden thread. The catch is the ONE connection they missed."
- **Action:** "Be a co-founder, not a project manager. What moved, what's circling, what's next. One strategic insight they didn't see."
- **Mirror:** "Minimal voice. Use their words. Organize beautifully. One pattern noticed, one surprise connection. That's it."
- **Advisory:** "Professional intelligence brief. Highlights, patterns, recommended focus. No therapy. No narrative. Clean."
- **Gentle:** "Quiet week. Acknowledge it. Surface one thing from last week. Keep the loop alive."

---

## 8. Implementation Roadmap

### Phase 1: Foundation (This Week — Mar 12-18)

**Goal:** Joey runs the first Catch cycle. One mode (narrative). Real output.

- [ ] P0-8e ships (Joey = user zero) — already in Dropper-Code queue
- [ ] Email prompt scheduler live (Tue/Thu/Sat for Joey)
- [ ] Basic `snapback_generator.py` with narrative mode only
- [ ] Drop acknowledgment system ("Caught. 🧢") 
- [ ] Sunday: Joey's first Weekly Catch generated + delivered
- [ ] **Screenshot #1 captured** — real narrative Catch from real drops

### Phase 2: Multi-Mode (Mar 19-25)

**Goal:** All 5 (+1 gentle) catch modes operational. 5-10 users in different tracks.

- [ ] Drop classification extended with `catch_signals` (emotional intensity, temporal intent, energy direction)
- [ ] Weekly synthesis pipeline (`synthesize_week()`)
- [ ] Mode determination logic (`determine_catch_mode()`)
- [ ] Prompt templates for all 6 modes
- [ ] Catch generation templates for all 6 modes
- [ ] User profile builder with catch_config
- [ ] Invite Brooke, Danny, 3-5 others
- [ ] **Screenshots #2-5 captured** — one per mode, real users

### Phase 3: Progressive Intelligence (Mar 26 - Apr 8)

**Goal:** The system gets smarter over time. Progressive disclosure live.

- [ ] Progressive stage tracking (mirror → pattern → anticipation → oracle)
- [ ] Cross-week pattern detection ("3 weeks in a row...")
- [ ] Surprise connection engine (this week ↔ old drops)
- [ ] Prompt cadence adaptation (send prompts at user's natural drop time)
- [ ] Mode history tracking + visualization
- [ ] User can see their mode history: "This week: Clarity. Last week: Narrative."

### Phase 4: Scale + Revenue (Apr 9+)

**Goal:** Onboarding flow ships. Free vs Pro differentiation. First paying Catch users.

- [ ] Onboarding decision tree implemented (web signup → entry persona)
- [ ] Free tier: basic summary catch (no narrative, no personalization)
- [ ] Pro tier: full adaptive catch (all modes, progressive intelligence)
- [ ] Landing page updated with real screenshots from Phase 1-2
- [ ] "Bring me one problem" offer → 7-day free trial → first Catch → upgrade prompt
- [ ] Advisory mode as separate product ($49/mo white-label Catch for coaches)

---

## 9. The Offer — Revised

The original offer: *"Bring me one problem. Talk about it for a week. I'll show you what you're not seeing."*

The adaptive version:

> **The Weekly Catch** 🧢
> 
> Drop what's on your mind — all week, any way you want.  
> A thought. A task. A rant. A photo. A voice note. Whatever.
>
> On Sunday, you get your Catch:  
> Your week, reflected back to you in a way you can't build for yourself.
>
> Not a summary. Not a to-do list.  
> The thing you need to see that you're too close to see.
>
> **Try it free for a week.** Reply to start.

This works for ALL personas:
- **Stuck:** "Drop what's on your mind" → they dump the stuck thing
- **Scattered:** "Drop what's on your mind" → they dump everything
- **Builder:** "A task. A photo." → they drop project updates  
- **Curious:** "Whatever." → low bar, they can drop anything
- **Journaler:** "All week, any way you want" → permission to write

The offer doesn't prescribe the use case. The system figures it out.

---

## 10. Metrics & Success Criteria

| Metric | Week 1 Target | Month 1 Target | Signal |
|--------|--------------|----------------|--------|
| Joey completes full 7-day cycle | ✅ | — | Engine works for real |
| First external user completes cycle | — | ✅ 5 users | Product works for others |
| Catch open rate | >80% | >60% | People anticipate it |
| Catch reply rate | >30% | >20% | It provokes response |
| Week 1→Week 2 retention | — | >70% | They come back |
| Week 4 retention | — | >50% | It's a habit |
| Drops per user per week | 3+ (Joey) | 4+ avg | Capture is frictionless |
| Mode accuracy (user feedback) | N/A | "This felt right" >70% | Intelligence layer works |
| NPS on first Catch | — | >50 | The moment lands |
| Screenshot portfolio | 1 (narrative) | 5 (all modes) | Marketing arsenal built |
| Conversion: trial → paid | — | >20% | Product-market fit |

---

## 11. Open Questions

1. **Should users be able to choose their mode?** Current design: system determines, user can override via settings. But showing "Your Catch mode this week: Clarity" might create unwanted friction. Lean toward invisible intelligence with a "This didn't feel right" feedback mechanism.

2. **What if someone drops in multiple languages?** Danny sends English. Mom might send English with Spanish phrases. The Catch should match their dominant language. Detect per-drop and match weekly majority.

3. **How does the advisory mode handle curator input?** Joey writes Danny's brief with editorial notes. Where does Joey inject those? Possible: admin UI has a "curator notes" field per user that gets injected into the Catch generation prompt.

4. **Voice Catches?** Joey has TTS capability. A voice-read Weekly Catch could be powerful — especially for narrative mode. Phase 3+, but plant the seed now in the template architecture.

5. **Group Catches?** What if Brooke and Joey are both dropping about the songwriting challenge? A shared Catch that weaves both perspectives? Could be the couples/team feature. Way future, but the data model should support it (tag drops with shared context IDs).

---

## 12. The One-Line Test

If someone asks "What is DropAnywhere?", the answer should be:

> **"You drop what's on your mind all week. On Sunday, it shows you what you couldn't see."**

And if they ask "How?":

> **"You just reply to an email. That's it."**

And if they ask "What do I get?":

> **"Depends on what you need. If you're stuck, you get a story that snaps you back. If you're scattered, you get the thread that connects it all. If you're building, you get a progress report that sees what you missed. The system figures it out."**

That third answer is why this spec exists. The system figures it out.

🧢

---

*"We should absolutely have screenshots captured from the tool — not fake ones — legit ones that showcase stuff that are specific to their scenario."*  
— Joey, March 11, 2026

