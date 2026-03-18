# SPEC: The Weekly Catch — Progressive Disclosure & Adaptive Output

**Author:** Claw + Joey  
**Date:** 2026-03-11  
**Status:** Draft — for Joey's review  
**Depends on:** Snapback Engine (shipped), Email Prompt Scheduler (shipped), Reply Capture (shipped)  
**Supersedes:** Nothing — this is ADDITIVE to the Snapback Integration Spec  

---

## 1. The Core Insight

The Weekly Catch can't be one thing for everyone. A meditation for the stuck person is useless for the scattered organizer. An action checklist for the journaler misses the point entirely.

**The product must:**
1. **Listen** — understand what the user is actually dropping (feelings? tasks? ideas?)
2. **Encourage** — mid-week nudges that are specific to THEIR pattern, not generic
3. **Give feedback** — the Weekly Catch is a personalized analysis, not a template fill

**The experience is email-only. Zero app required. But the app is working behind the scenes — and we SHOW them that with real screenshots of their actual data building up throughout the week.**

---

## 2. Entry Points — How People Arrive

### 2a. The Direct Offer (outbound)

Joey or a landing page sends:

> "Bring me one thing on your mind. Talk about it for a week. I'll show you what you're not seeing."

They reply to the email. That reply is their first drop. They're in.

### 2b. The Curious Visitor (inbound)

Someone hits drop-anywhere.com. Instead of a dashboard, they see:

> "What's on your mind right now?"
> [text field] [or just email it to drop@drop-anywhere.com]

Their first drop triggers the 7-day journey.

### 2c. The BHA Crossover

Someone has 5+ BHA conversations. System detects patterns. Sends:

> "You've been thinking about [X] a lot lately. Want to go deeper? Reply to this email with whatever's on your mind about it."

### 2d. The Invisible User (Advisory Mode)

Joey (or any advisor) manually enrolls someone. They get the first email. They never know the system exists. They're just replying to thoughtful emails.

---

## 3. Day 0 — The First Drop & Persona Detection

When the first drop arrives, the system does three things:

### 3a. Classify the Drop

Using lightweight LLM classification (Gemini Flash, ~$0.001):

```
INPUT: "I've been stuck on this career thing for months. I know I should leave but I can't pull the trigger."

CLASSIFICATION:
  type: reflection
  energy: stuck/heavy
  domain: work
  emotional_intensity: high
  actionability: low
  persona_signal: "The Stuck One"
```

```
INPUT: "Need to finish the pitch deck, call investors, update the product roadmap, and figure out Q2 hiring"

CLASSIFICATION:
  type: task_dump
  energy: scattered/overwhelmed  
  domain: work
  emotional_intensity: medium
  actionability: high
  persona_signal: "The Scattered One"
```

```
INPUT: "Had this idea for a podcast about AI and creativity. Also been thinking about how music production has changed. And maybe a newsletter?"

CLASSIFICATION:
  type: ideation
  energy: creative/exploratory
  domain: creativity
  emotional_intensity: low
  actionability: medium
  persona_signal: "The Builder"
```

### 3b. Set Initial Catch Mode (adaptive, not locked)

| Persona Signal | Initial Catch Mode | Output Style |
|---------------|-------------------|-------------|
| **The Stuck One** | `narrative` | Snapback — their own words reflected as a story. First-person, present-tense. Shows them the path they're already on. |
| **The Scattered One** | `clarity` | Weekly Clarity Report — organized themes, what's connected, what's noise, "here's your week in focus." |
| **The Builder** | `action` | Action Catch — prioritized list with context. What moved, what's stuck, what to do Monday morning. |
| **The Explorer** | `pattern` | Pattern Mirror — "here's what you keep coming back to." Threads across drops. The red thread. |
| **The Processor** | `reflection` | Deep Mirror — no action items, just: "here's what you said, here's what it means, here's what's underneath." |
| **Unknown / Mixed** | `adaptive` | System watches for 3+ drops, then picks the best mode. First catch = hybrid (a bit of everything). |

**This is NOT permanent.** The mode recalculates every week based on that week's actual drops. A "Builder" who drops something heavy on Thursday gets a narrative that week, not an action list.

### 3c. Send the Welcome Confirmation

Not a "Welcome to DropAnywhere!" email. Something human:

> **Subject:** Got it. Keep going.
>
> Hey [name],
>
> I caught that. Here's what's going to happen:
>
> Over the next 7 days, I'll check in a few times. Just reply to my emails with whatever comes up — about this, about anything. Don't overthink it. Don't organize it. Just drop it.
>
> On Day 8, I'll send you something back. Think of it as a letter from someone who's been listening carefully.
>
> That's it. No app to download. No account to set up. Just reply to emails.
>
> Talk soon.

---

## 4. Days 1-7 — The Listening Week

### 4a. Email Cadence

| Day | Email Type | Purpose | Tone |
|-----|-----------|---------|------|
| **Day 0** | Welcome confirmation | "Got it. Keep going." | Warm, brief |
| **Day 2** | First nudge | Persona-specific prompt (see 4b) | Curious, encouraging |
| **Day 3** | Screenshot reveal | "Here's what's building" + REAL screenshot | Surprising, concrete |
| **Day 4** | Second nudge | Deeper prompt based on what they've dropped so far | Reflective |
| **Day 6** | Third nudge + anticipation | "Your catch is almost ready" + progress screenshot | Building excitement |
| **Day 8** | **THE WEEKLY CATCH** | The personalized analysis/narrative/report | The payoff |

### 4b. Persona-Specific Nudge Prompts

**The Stuck One (narrative mode):**
- Day 2: "What would change if [the thing] just... resolved? Like, tomorrow. What does that day look like?"
- Day 4: "You mentioned [X]. When did that start? Not the facts — the feeling."
- Day 6: "One more thing before your catch arrives Sunday: what's the version of this where you're proud of how you handled it?"

**The Scattered One (clarity mode):**
- Day 2: "Of everything on your plate right now — what's the one thing that if you handled it, would make the others easier?"
- Day 4: "Quick brain dump: what did you NOT do this week that's nagging at you?"
- Day 6: "Your catch is coming together. Last thing: what felt good this week? Even small."

**The Builder (action mode):**
- Day 2: "What's the first thing you'd finish if you had a completely free day tomorrow?"
- Day 4: "Which of your projects is actually moving vs which are you just thinking about?"
- Day 6: "Your progress report is almost ready. Any wins from this week you want to make sure are captured?"

**The Explorer (pattern mode):**
- Day 2: "What's something you keep coming back to — an idea, a topic, a question — that won't leave you alone?"
- Day 4: "If you had to explain what you're most curious about right now to a stranger in one sentence, what would it be?"
- Day 6: "I'm seeing some interesting threads in what you've shared. Before I connect them — anything else?"

**The Processor (reflection mode):**
- Day 2: "How are you feeling today? Not about anything specific. Just... the temperature."
- Day 4: "Is there something you've been avoiding thinking about? You don't have to go deep — just name it."
- Day 6: "Your reflection is coming together. Last thought: what do you want to feel on Monday morning?"

### 4c. Real Screenshots — The "Holy Shit" Moments

**This is critical. Not mockups. Not illustrations. REAL screenshots of their actual data in the system.**

#### What We Screenshot (Puppeteer/headless Chrome):

1. **Day 3 — The Vault Building** (after 2-3 drops)
   - Screenshot their vault view showing their drops organized
   - Caption: *"This is building while you go about your day. Every reply you send adds to it."*
   - Shows: 2-3 drop cards with their actual text snippets, timestamps, domain tags

2. **Day 6 — The Intelligence Map** (after 4-5 drops)
   - Screenshot their Intelligence Map with nodes and connections
   - Caption: *"See those connections? Those are patterns in what you've been telling me. Your catch on Sunday will unpack them."*
   - Shows: node graph with their actual themes connected, highlighted clusters

3. **Day 8 — The Full Picture** (in the Weekly Catch email itself)
   - Embedded screenshots of: vault summary, intelligence map, action items (if applicable)
   - These aren't decorative — they're proof the system was listening

#### Technical Implementation:

```python
async def capture_user_screenshot(user_id: str, view: str, highlight: dict = None) -> str:
    """
    Render a real screenshot of the user's data in the DA web app.
    
    Args:
        user_id: The user's canonical ID
        view: 'vault' | 'intelligence' | 'actions' | 'digest_preview'
        highlight: Optional dict of elements to highlight/annotate
    
    Returns:
        CDN URL of the captured screenshot
    
    Implementation:
        1. Launch headless Chrome (Puppeteer)
        2. Navigate to DA app with admin session token
        3. Load user's view (vault, intelligence map, etc.)
        4. Apply custom styling: 
           - Blur/redact anything sensitive
           - Add subtle annotation arrows/highlights
           - Apply "email-safe" color scheme (works on white/dark backgrounds)
        5. Capture viewport screenshot
        6. Upload to CDN (Poe CDN or S3)
        7. Return URL for email embedding
    """
```

#### Screenshot Styling Rules:
- Clean, cropped, no browser chrome
- Light theme only (email-safe)
- User's actual text visible but truncated tastefully
- Highlighted connections/patterns get a subtle glow
- Small watermark: "drop-anywhere.com" (not aggressive, just present)
- Mobile-optimized dimensions (600px wide max for email)

---

## 5. Day 8 — The Weekly Catch (Adaptive Output)

### 5a. Output Router

```python
def determine_catch_style(user_profile: dict, week_drops: list) -> str:
    """
    Analyze the week's drops and user profile to pick the best output.
    
    Factors:
    1. User's initial persona (from Day 0 classification)
    2. This week's drop classification distribution
    3. Emotional intensity trend (escalating? de-escalating? stable?)
    4. Actionability ratio (how many drops are task-like vs reflective?)
    5. Drop frequency pattern (did they engage a lot or minimally?)
    
    Returns: 'narrative' | 'clarity' | 'action' | 'pattern' | 'reflection' | 'hybrid'
    """
    
    # If 60%+ drops are high emotional intensity → narrative (Snapback)
    # If 60%+ drops are tasks/actionable → action catch
    # If drops span 3+ unrelated domains → clarity report
    # If user dropped <3 times → hybrid (not enough signal for specialized)
    # If recurring theme appears in 3+ drops → pattern mirror
    # If mostly processing/journaling → reflection
    # If mixed → hybrid (elements of each)
```

### 5b. Output Templates

#### NARRATIVE (Snapback)
The original. First-person, present-tense, their words woven into a story.

> **Subject:** Your Weekly Catch — the story you told this week
>
> *[First-person narrative using their exact phrases, people they mentioned, details from their drops. Not a summary. A story. The version they couldn't see from inside.]*
>
> ---
> 📸 *Your week at a glance:*
> [Intelligence Map screenshot showing this week's connections]
>
> 🎯 *One thing that stood out:*
> [The single most important thread the system detected]
>
> 💬 *What to drop next week:*
> [One prompt based on where the narrative points]

#### CLARITY (Weekly Clarity Report)
For the scattered. Organized, structured, calming.

> **Subject:** Your Weekly Catch — here's what's actually going on
>
> **This week you dropped [N] thoughts across [N] areas.**
>
> 🧭 **The Main Thread:**
> [The dominant theme, with quotes from their drops]
>
> 🔗 **Connected:**
> [2-3 things that are actually related that they might not see]
> [Intelligence Map screenshot with connections highlighted]
>
> 📦 **Parked (not forgotten):**
> [Things they mentioned once but didn't return to — held, not lost]
>
> ⚡ **Your energy was highest when talking about:**
> [Topic/area where their language was most alive]
>
> 📸 *Your vault this week:*
> [Vault screenshot showing organized drops]
>
> 💬 *For next week:*
> "You mentioned [X] three times. Want to go deeper? Just reply."

#### ACTION (Action Catch)
For the builder. Clean, prioritized, momentum-focused.

> **Subject:** Your Weekly Catch — what moved and what's next
>
> **This week: [N] drops. [N] action items detected. [N] projects touched.**
>
> ✅ **What moved:**
> [Things they mentioned completing or progressing]
>
> 🎯 **Your top 3 for Monday:**
> 1. [Highest priority action from their drops]
> 2. [Second priority]
> 3. [Third priority]
>
> ⏸️ **Stalled (mentioned but no movement):**
> [Projects/tasks they brought up but didn't progress]
>
> 📸 *Your action board:*
> [Screenshot of their persistent action queue in DA]
>
> 💡 **Pattern I noticed:**
> "You tend to [pattern]. What if you tried [suggestion]?"
>
> 💬 *Quick drop for next week:*
> "What's the ONE thing on this list that would make the biggest difference?"

#### PATTERN (Pattern Mirror)
For the explorer. Connecting dots across weeks.

> **Subject:** Your Weekly Catch — the thread you keep pulling
>
> **You've been circling something.**
>
> 🔴 **The Red Thread:**
> [The thing that keeps appearing across drops, maybe across weeks]
> [Their exact words from different drops, showing the pattern]
>
> 🗺️ **Your thinking map:**
> [Intelligence Map screenshot — zoomed into the cluster]
>
> 🤔 **What I think this means (you tell me if I'm wrong):**
> [One-paragraph interpretation — honest, not flattering]
>
> 💬 *The question this raises:*
> "[Specific question based on the pattern]"

#### REFLECTION (Deep Mirror)
For the processor. No action items. Just understanding.

> **Subject:** Your Weekly Catch — what you said, and what's underneath
>
> *This isn't a to-do list. It's a mirror.*
>
> 🪞 **What you told me this week:**
> [Curated quotes from their drops — the most revealing ones]
>
> 🌊 **The emotional current:**
> [Trend: were they getting lighter? heavier? was there a shift mid-week?]
>
> 🔑 **The thing you didn't say directly:**
> [The subtext the system detected — what's underneath the surface drops]
>
> 📸 *Where you are:*
> [Simple visualization — maybe a mood/energy chart from their drops]
>
> 💬 *No action needed. But if something stirred:*
> "Just reply to this email. I'm here."

#### HYBRID (First Week / Mixed Signals)
When the system doesn't have enough signal yet, or the drops are genuinely mixed:

> **Subject:** Your first Weekly Catch — here's what I heard
>
> **You dropped [N] times this week. Here's what I caught.**
>
> 📝 **What you said:**
> [Brief organized summary of their drops, grouped by theme]
>
> 🔗 **Connections I see:**
> [1-2 patterns or links between drops]
>
> 📸 *Your vault:*
> [Screenshot]
>
> 💡 **What I'm learning about you:**
> "Based on what you've shared, I think you're someone who [observation]. Next week, I'll tailor your catch to match. Want more [narrative/action/reflection/clarity]? Just tell me."
>
> 💬 *For next week:*
> [One prompt that digs deeper into whatever they dropped most about]

---

## 6. Progressive Disclosure — The Product Reveals Itself

The user should never feel overwhelmed. The product unfolds like a conversation, not a dashboard.

### Week 1: "It's just email"
- They reply to emails. That's it.
- Screenshots show them something is building (vault, intelligence map)
- Weekly Catch arrives. They're surprised by the quality.
- **What they know:** This thing listens and sends me something good.

### Week 2: "Wait, it remembers"
- The Week 2 nudges reference Week 1 drops: "Last week you mentioned [X]. Did anything change?"
- The Weekly Catch references the previous week: "You're still circling [X], but this week the energy shifted from [A] to [B]."
- **What they know:** This thing has memory. It's tracking a thread.

### Week 3: "There's a pattern"
- Mid-week email includes a mini pattern insight: "You've mentioned [Y] in 8 of your 15 drops. Here's what that looks like." + screenshot
- Weekly Catch includes a "3-week view" section
- **What they know:** This thing sees things I don't see about myself.

### Week 4: "I need this"
- The catch includes: "You've been using this for a month. Here's your month in review." + comprehensive Intelligence Map screenshot
- Gentle reveal: "Everything you've dropped is in your vault. Want to explore it? [link]"
- **First time they're invited to the app.** Not pushed. Invited.
- **What they know:** There's a whole system behind this. And it's mine.

### Week 5+: The Full Product
- They're now getting nudges, Weekly Catches, AND have access to:
  - Vault (all their drops, searchable)
  - Intelligence Map (visual connections)
  - Action Queue (persistent to-dos from catches)
  - Daily Digest (opt-in — "Want daily insights too?")
- Progressive reveal of features, never all at once

### Month 2+: Upgrade Prompts (natural, not pushy)
- "You've been dropping 10+ times a week. Free tier caps at 5. Want to keep going? [$9/mo]"
- "Your Intelligence Map has 47 nodes. Want to see cross-week patterns? [Pro feature]"
- Not a paywall. A value wall. They've already felt the value.

---

## 7. Technical Architecture

### 7a. New Components

```
┌─────────────────────────────────────────┐
│           WEEKLY CATCH ENGINE            │
│                                         │
│  ┌─────────────┐  ┌──────────────────┐  │
│  │ Drop         │  │ User Profile     │  │
│  │ Classifier   │  │ Builder          │  │
│  │ (at ingest)  │  │ (continuous)     │  │
│  └──────┬──────┘  └────────┬─────────┘  │
│         │                   │            │
│  ┌──────▼───────────────────▼─────────┐  │
│  │         Catch Router               │  │
│  │  (picks output style per week)     │  │
│  └──────────────┬────────────────────┘  │
│                  │                       │
│  ┌──────────────▼────────────────────┐  │
│  │      Output Generator              │  │
│  │  narrative | clarity | action |     │  │
│  │  pattern | reflection | hybrid     │  │
│  └──────────────┬────────────────────┘  │
│                  │                       │
│  ┌──────────────▼────────────────────┐  │
│  │      Screenshot Capture            │  │
│  │  (Puppeteer, real user data)       │  │
│  └──────────────┬────────────────────┘  │
│                  │                       │
│  ┌──────────────▼────────────────────┐  │
│  │      Email Renderer + Sender       │  │
│  │  (Resend, progressive templates)   │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### 7b. Database Changes

```sql
-- Extend user profile for catch personalization
ALTER TABLE users ADD COLUMN IF NOT EXISTS catch_profile JSONB DEFAULT '{}';
-- catch_profile schema:
-- {
--   "persona": "stuck|scattered|builder|explorer|processor|unknown",
--   "catch_mode": "narrative|clarity|action|pattern|reflection|adaptive",
--   "week_number": 1,
--   "onboarding_complete": false,
--   "entry_point": "direct_offer|website|bha_crossover|advisory",
--   "language_patterns": {...},
--   "emotional_baseline": {...},
--   "drop_type_distribution": {"reflection": 0.4, "task": 0.3, "idea": 0.2, "question": 0.1},
--   "topics_seen": ["career", "relationship", "health"],
--   "previous_catch_style": "narrative",
--   "engagement": {"replies": 5, "opens": 3, "clicks": 1}
-- }

-- Drop classification at ingest
ALTER TABLE vault_items ADD COLUMN IF NOT EXISTS drop_classification JSONB DEFAULT '{}';
-- {
--   "type": "reflection|task|idea|question|resource|session",
--   "emotional_intensity": 0.0-1.0,
--   "actionability": 0.0-1.0,
--   "domain": "work|health|relationships|creativity|rest",
--   "entities": ["Brooke", "the pitch deck"],
--   "sentiment": "positive|negative|neutral|mixed"
-- }

-- Screenshot cache
CREATE TABLE IF NOT EXISTS user_screenshots (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    view_type TEXT NOT NULL, -- 'vault' | 'intelligence' | 'actions' | 'digest_preview'
    screenshot_url TEXT NOT NULL,
    captured_at TIMESTAMPTZ DEFAULT NOW(),
    week_number INTEGER,
    metadata JSONB DEFAULT '{}'
);
```

### 7c. New API Endpoints

```
POST /api/drops/classify          -- Classify a drop at ingest (Gemini Flash)
GET  /api/users/{id}/catch-profile -- Get user's catch profile
POST /api/screenshots/capture     -- Capture a real screenshot for a user
GET  /api/catch/{user_id}/preview -- Preview what the catch will look like
POST /api/catch/{user_id}/generate -- Generate the Weekly Catch
GET  /api/catch/{user_id}/history  -- Previous catches
```

### 7d. Email Infrastructure

All emails go through Resend. No new providers needed.

**From address:** `catch@drop-anywhere.com` (or `hello@` — feels more personal)

**Reply handling:** All replies route to existing Resend webhook → `api/webhook/email` → classified as drops tagged with `source=email_reply`, `catch_week=N`, `catch_day=N`.

**Screenshot embedding:** Inline images via CID or hosted URLs. Must render in Gmail, Apple Mail, Outlook, and mobile.

---

## 8. The 7-Day Trial as Sales Funnel

The free trial IS the product demo. They don't watch a video or read a landing page. They EXPERIENCE the value.

```
Day 0: First drop (entry)                    → "Got it. Keep going."
Day 2: Nudge #1 (persona-specific)           → They reply (drop #2-3)
Day 3: Screenshot reveal                     → "Holy shit, it's organizing my thoughts"
Day 4: Nudge #2 (deeper, based on THEIR drops) → They reply (drop #4-5)
Day 6: Anticipation + screenshot              → "I can't wait to see this"
Day 8: THE WEEKLY CATCH                       → 🤯 "How did it know that?"

Day 9: "Want to keep going?"                  → Not a paywall. A question.
       Free: 3 drops/week, basic catch
       Pro ($9/mo): Unlimited, full catch, Intelligence Map, daily digest option
```

**Conversion thesis:** By Day 8, they've had 6 emails, 3 of which contain real screenshots of their data building up. The Weekly Catch hits differently because they remember dropping those things. It's their words, their patterns, their life — reflected back with intelligence they didn't have.

The free week costs us ~$0.15/user (6 emails via Resend + 1 LLM generation + 3 screenshots). At even a 10% conversion to $9/mo, the unit economics work from Day 1.

---

## 9. What This Replaces / Extends

| Current | After This Spec |
|---------|----------------|
| Daily digest (multi-analyzer) | **Stays.** Proven, users love it. Opt-in after Week 4. |
| Snapback generator (shipped) | **Extended.** Becomes one of 6 output modes in the Catch Router. |
| Email prompt scheduler (shipped) | **Extended.** Prompts become persona-specific, not generic. |
| Reply capture (shipped) | **No change.** Already works. |
| User onboarding (drip sequence) | **Replaced.** The 7-day Catch trial IS the onboarding. |
| Manual admission | **Enhanced.** First drop auto-starts the journey. Manual admit = Day 8 catch generation. |

---

## 10. Implementation Phases

### Phase 1: The Minimum Lovable Trial (1-2 weeks)

**Goal:** One email journey that works for any persona type.

- [ ] Drop classification at ingest (Gemini Flash, ~$0.001/drop)
- [ ] Persona detection from first drop (simple classifier)
- [ ] 5 sets of persona-specific nudge prompts (one per persona type)
- [ ] Catch Router v1 (picks style based on week's drop classifications)
- [ ] 3 output templates: Narrative, Clarity, Hybrid (cover 80% of cases)
- [ ] Screenshot capture pipeline (Puppeteer → CDN → email embed)
- [ ] 7-day email journey orchestrator (replaces current generic drip)
- [ ] Joey runs it first (user zero, already in queue)

### Phase 2: Full Adaptive Engine (2-4 weeks)

- [ ] All 6 output templates (add Action, Pattern, Reflection)
- [ ] Cross-week continuity ("last week you mentioned...")
- [ ] User profile builder with evolving catch_mode
- [ ] Progressive disclosure logic (Week 1-5 feature reveal)
- [ ] A/B test different nudge prompts per persona
- [ ] Screenshot annotations (highlight connections, add captions)
- [ ] "Month in Review" catch template (Week 4)

### Phase 3: Scale & Monetize (Month 2-3)

- [ ] Free vs Pro catch differentiation
- [ ] Conversion flow (Day 9 email → Pro signup)
- [ ] Advisory Mode (white-label catches for coaches)
- [ ] Self-service persona override ("I want more action items, less narrative")
- [ ] Catch rating/feedback loop ("Was this useful? 👍👎")
- [ ] Referral mechanism built into catches ("Know someone who'd benefit?")

---

## 11. Success Metrics

| Metric | Week 1 Target | Month 1 Target | Month 3 Target |
|--------|--------------|----------------|----------------|
| Trial starts (first drops) | 10 (Joey's list) | 50 | 200 |
| Day 8 completion rate | 60%+ | 50%+ | 45%+ |
| Weekly Catch open rate | 80%+ | 70%+ | 65%+ |
| "Holy shit" replies (organic) | 3+ | 15+ | 50+ |
| Free → Pro conversion | N/A | 15%+ | 12%+ |
| Weekly drop frequency (active users) | 5+/week | 4+/week | 4+/week |
| Catch satisfaction (👍 rate) | 80%+ | 75%+ | 70%+ |

---

## 12. The Pitch (One Paragraph)

**For the landing page, for outreach, for everything:**

> You know that thing on your mind? The career question, the relationship, the project that won't unstick, the idea that keeps coming back? Drop it here. Just reply to an email. Do that a few times this week — whenever something comes up, drop it. On Sunday, you'll get your Weekly Catch: a personalized analysis of everything you shared, with connections you didn't see and clarity you didn't expect. No app. No signup form. No learning curve. Just email. Try it free for a week — your first Catch is on us.

---

*This spec is additive to SNAPBACK-INTEGRATION-2026-03-11.md. The Snapback engine, email prompts, and reply capture are already shipped. This adds: persona detection, adaptive output routing, real screenshots, progressive disclosure, and the 7-day trial framework.*

*The product is a mirror, not a portrait. The moment it becomes performative, it loses the thing that makes it hit.*

