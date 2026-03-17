# Onboarding Funnel — DropAnywhere

**Version:** 2026-03-17-v1
**Status:** DRAFT — Awaiting Joey's review
**Ref:** COMPASS.md Section 6, Joey feedback 03-17

---

## Philosophy

Every email does THREE things: **Educate, Entertain, Collect.**
Every interaction enriches the user's Postgres profile.
The funnel adapts — behavioral triggers override fixed timing.

---

## Digest Analyzer Styles (Live in Hub)

| Style | Internal Key | Personality | Best For |
|-------|-------------|-------------|----------|
| **Clarity Engine** | `clarity` | Organized themes, focus report | Scattered thinkers |
| **Action Catch** | `action` | Prioritized action items | Builders, operators |
| **Pattern Mirror** | `pattern` | Cross-drop thread detection | Explorers, creatives |
| **Deep Mirror** | `reflection` | No actions, just meaning | Processors, journalers |
| **Adaptive** | `adaptive` | System picks best mode | New users (default) |

---

## Profile Fields (Postgres)

Built progressively through onboarding:

| Field | Type | Collected At | Source |
|-------|------|-------------|--------|
| `email` | string | Signup | Waitlist form |
| `name` | string | Email #1 reply | Reply parsing |
| `onboarding_step` | int | Auto | System |
| `first_drop_at` | timestamp | Auto | Drop ingestion |
| `drop_count` | int | Auto | Aggregated |
| `focus_domains` | string[] | Email #4 | CTA click / reply |
| `preferred_digest_style` | string | Email #6 | CTA click |
| `digest_frequency` | enum | Email #9 | CTA click / reply |
| `life_domains` | string[] | Email #5 | CTA click |
| `biggest_challenge` | text | Email #4 | Reply |
| `engagement_score` | float | Auto | Opens + clicks + drops + replies |
| `trial_start` | timestamp | Auto | Admission |
| `trial_end` | timestamp | Auto | trial_start + 21d |
| `converted` | boolean | Auto | Stripe webhook |
| `last_drop_at` | timestamp | Auto | Drop ingestion |
| `nudge_count` | int | Auto | System |

---

## The Funnel: 13 Emails + Behavioral Triggers over 21 Days

### PHASE 1: Welcome + First Drop (Days 0-1)

#### Email #1 — Welcome (Instant on admission)
- **Subject:** Welcome to DropAnywhere — your mind just got an outbox 🧠
- **Purpose:** Educate + First action
- **Showcase:** None (pure welcome)
- **Content:** What DropAnywhere is, how to drop (email drop@drop-anywhere.com), what happens next
- **Data collected:** `onboarding_step = 1`, open tracking
- **CTA:** "Send your first drop right now — just reply to this email or email drop@drop-anywhere.com"
- **Profile update:** `trial_start`, `onboarding_step`

#### Email #2 — First Drop Nudge (4h after #1, IF no drop received)
- **Subject:** Your brain is still holding everything ✋
- **Purpose:** Activate
- **Showcase:** None
- **Content:** Quick prompts ("What's the one thing on your mind right now?"), example drops, reassurance that drops can be anything
- **Data collected:** Behavioral — did they need a nudge? (`nudge_count++`)
- **CTA:** "Just hit reply and type one sentence. That's a drop."
- **Trigger:** Skipped if user already dropped

#### Email #3 — First Drop Confirmation (Instant on first drop)
- **Subject:** 💧 Your first drop just landed — here's what we found
- **Purpose:** Demonstrate value immediately
- **Showcase:** **Clarity Engine** (mini-analysis)
- **Content:** Their actual drop text + a 3-sentence AI analysis: theme detected, one question to think about, one connection hint
- **Data collected:** `first_drop_at`, `drop_count = 1`
- **CTA:** "Drop another thought whenever you're ready. Each one makes your Intelligence Map smarter."

---

### PHASE 2: Education + Data Collection (Days 2-7)

#### Email #4 — "What's on your mind?" (Day 2)
- **Subject:** Quick question — what are you trying to figure out?
- **Purpose:** Collect context
- **Showcase:** None (data collection focus)
- **Content:** "The more we know about what matters to you, the smarter your digests get." Present 5 life domains as clickable options: Work / Health / Relationships / Creativity / Rest
- **Data collected:** `focus_domains[]`, `life_domains[]`, `biggest_challenge` (if they reply)
- **CTA:** Click domain buttons OR reply with what they're working through
- **Profile update:** `focus_domains`, `life_domains`

#### Email #5 — "Meet your digest styles" (Day 4)
- **Subject:** Not all insights look the same — pick your lens 🔍
- **Purpose:** Educate + Collect preference
- **Showcase:** ALL styles (mini previews)
- **Content:** Show a sample snippet from each digest style using their OWN drops (or example data if <3 drops):
  - 🎯 **Clarity Engine** — "Here's your week in focus"
  - ⚡ **Action Catch** — "Here's what to do Monday morning"
  - 🔴 **Pattern Mirror** — "Here's the thread you keep pulling"
  - 🪞 **Deep Mirror** — "Here's what's underneath"
- **Data collected:** `preferred_digest_style`
- **CTA:** "Which one speaks to you? Click to set your default (you can always change it)."

#### Email #6 — "Your first Intelligence Map" (Day 7, requires ≥3 drops)
- **Subject:** 🗺️ Your Intelligence Map is ready
- **Purpose:** Demonstrate core value
- **Showcase:** User's preferred style (or **Adaptive** if no preference set)
- **Content:** Full Intelligence Map digest using their actual drops. Themed sections, connections between drops, patterns emerging.
- **Data collected:** Engagement (open, click, reply), style satisfaction
- **CTA:** "Reply with 'more like this' or 'try a different style' — we'll adapt."
- **Gate:** If <3 drops, send "You're X drops away from your first map" instead

---

### PHASE 3: Depth + Engagement (Days 8-14)

#### Email #7 — Weekly Reflection (Day 8)
- **Subject:** You've dropped {X} thoughts this week — here's the shape of your mind 🧩
- **Purpose:** Engage + Demonstrate value
- **Showcase:** **Pattern Mirror**
- **Content:** Stats (drop count, themes detected, connections found) + pattern analysis. "You keep coming back to [theme]. That's not random."
- **Data collected:** Engagement score update
- **CTA:** "What pattern surprises you? Reply and tell us."

#### Email #8 — "Try a different lens" (Day 10)
- **Subject:** Same thoughts, different angle — try {alternate style} 🔄
- **Purpose:** Educate + Engagement
- **Showcase:** Opposite of their current preference (if Clarity → Deep Mirror, if Action → Pattern Mirror)
- **Content:** Re-analyze their recent drops through a different lens. Show the contrast.
- **Data collected:** Style exploration behavior, `preferred_digest_style` update if they switch
- **CTA:** "Want this as your new default? Click here. Or keep your current style."

#### Email #9 — "Your connections are forming" (Day 12)
- **Subject:** Something interesting is happening in your drops 🔗
- **Purpose:** Demonstrate depth + Hook
- **Showcase:** **Pattern Mirror** (cross-week connections)
- **Content:** Show connections between drops from different days/topics. "Your drop about [X] on Tuesday connects to your [Y] thought from last week. Here's why that matters."
- **Data collected:** Engagement depth
- **CTA:** "Drop more to strengthen these connections. Your map gets sharper with every thought."

#### Email #10 — Premium Teaser (Day 14)
- **Subject:** What if every drop got an instant response? ⚡
- **Purpose:** Introduce premium value
- **Showcase:** **Clarity Engine** (instant mode)
- **Content:** "Right now, your drops get processed into your weekly Intelligence Map. Premium users get something extra: **Instant Clarity.** Every drop gets an immediate AI response — a reflection, a question, a connection — emailed back within seconds. Plus: smart nudges when you haven't dropped in a while, priority processing, and all digest styles unlocked."
- **Data collected:** Click-through on premium interest
- **CTA:** "See what Instant Clarity looks like →" (show example)

---

### PHASE 4: Conversion (Days 15-21)

#### Email #11 — "Your trial so far" (Day 15)
- **Subject:** 15 days of DropAnywhere — here's your story so far 📊
- **Purpose:** Value summary
- **Showcase:** **Deep Mirror** (reflection on their journey)
- **Content:** Full trial summary: total drops, themes discovered, patterns found, connections made, digest style preference. "In 15 days, you've externalized {X} thoughts. Here's what your mind looks like from the outside."
- **Data collected:** Engagement with summary
- **CTA:** "Keep this going? Lite is $7/mo — less than a coffee a week."

#### Email #12 — "Here's what changes" (Day 18)
- **Subject:** Your trial ends in 3 days — here's the before and after
- **Purpose:** Loss aversion + Convert
- **Showcase:** Side-by-side comparison
- **Content:** Two-column comparison:
  - **With DropAnywhere:** Daily Intelligence Maps, pattern detection, {X} insights found, {Y} connections, preferred style ({style})
  - **Without:** Thoughts stay in your head. No patterns. No connections. No mirror.
- **Data collected:** Conversion intent signal
- **CTA:** "Keep your Intelligence Map alive → $7/mo" (Stripe one-click)

#### Email #13 — Final Offer (Day 21)
- **Subject:** Last call — your Intelligence Map goes dark tonight 🌑
- **Purpose:** Final conversion
- **Showcase:** Their best Intelligence Map from the trial
- **Content:** "This was your best digest:" [embed their highest-engagement Intelligence Map]. "After today, your drops stop getting processed. Your patterns stop forming. Your map goes dark."
- **Data collected:** Conversion or churn
- **CTA:** "Stay lit → $7/mo" | "Not ready? Drop to Free (10 drops/mo, weekly only)"

---

## Behavioral Triggers (Always Active)

### Re-engagement Nudge
- **Trigger:** No drop in 72 hours
- **Subject:** Haven't heard from you in a bit — here's a thought prompt 💭
- **Content:** One of 20 rotating prompts: "What's the hardest decision you're avoiding?" / "What would you do if you knew you couldn't fail?" / "What are you grateful for right now?"
- **Limit:** Max 1 nudge per week, max 3 during trial
- **Profile update:** `nudge_count++`, `last_nudge_at`

### Instant Clarity (Premium Feature)
- **Trigger:** Every drop (premium users only)
- **Response time:** <60 seconds
- **Content:** 3-5 sentence AI response: reflection on the drop, one probing question, connection to previous drops if relevant
- **Delivery:** Reply to the drop email (same thread)

### Milestone Celebrations
- **5 drops:** "Your map is getting interesting 🗺️"
- **10 drops:** "Double digits! Here's a bonus pattern analysis"
- **25 drops:** "You're a power dropper — unlock early access to new features?"
- **50 drops:** "You've externalized 50 thoughts. Here's your full mind map."

---

## Technical Implementation

### Email Service
- **Provider:** Resend
- **From:** hello@drop-anywhere.com
- **Reply-to:** drop@drop-anywhere.com (replies become drops)
- **Threading:** Message-ID based, one thread per user

### Profile Enrichment Pipeline
1. Every email open → update `last_active_at`, `engagement_score`
2. Every CTA click → update relevant profile field
3. Every reply → parse for context, update `biggest_challenge` or `focus_domains`
4. Every drop → update `drop_count`, `last_drop_at`, recalculate `engagement_score`

### Sequence Logic (Hub-side)
- Behavioral triggers override time-based sends
- Email #3 (first drop confirmation) is event-driven, not scheduled
- Email #6 (Intelligence Map) gates on drop count, not just time
- Nudges respect quiet hours (no sends 10pm-8am user local time)
- Skip emails user has already satisfied (e.g., skip #2 nudge if they dropped within 4h)

### Digest Style Mapping
- Default: `adaptive` (system picks best)
- User preference stored in `preferred_digest_style`
- Can be changed at any time via reply ("try clarity" / "switch to pattern")
- Each digest email includes footer: "Want a different style? Reply with: clarity / action / pattern / reflection"

---

## Metrics to Track

| Metric | Target | Source |
|--------|--------|--------|
| Welcome → First drop | >60% in 24h | Drop ingestion |
| Email open rate | >45% | Resend |
| Trial → Lite conversion | >8% | Stripe |
| Avg drops per trial user | >10 | Hub |
| Nudge → Drop rate | >20% | Hub |
| Style preference set | >40% by Day 7 | Profile |
| Reply rate | >15% | Resend webhook |

---

*This is the product experience. Every email is a touchpoint. Every interaction builds the profile. Every profile makes the next email better.*
