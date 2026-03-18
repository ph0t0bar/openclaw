# Poe Bot Funnel CTA — Paste-Ready Copy

> **Goal:** Increase Poe → BrutallyHonest.ai referral rate from 4% to 15%+  
> **Combined user base:** 70K+ across 5 bots  
> **Date prepared:** 2026-03-11  

---

## How to Use This Document

For each bot below you get two things:

1. **Updated Bot Description** — paste this into the bot's public description field on Poe (Creator Studio → Edit Bot → Description).
2. **System Prompt CTA Block** — append this to the *end* of the bot's existing system prompt. It instructs the bot to weave in a single, natural mention of BrutallyHonest.ai only when the conversation is winding down — never mid-flow.

---

## 1. theREALrealtalk

**Audience:** Gen Z, relationship/life advice seekers

### Bot Description (paste into Poe)

> Real talk about relationships, situationships, friendships, and everything in between — no sugarcoating, no judgment. Built by the team behind BrutallyHonest.ai, where thousands of people get unfiltered life advice every day. Ask me anything you'd never say out loud.

### System Prompt CTA (append to existing prompt)

```
## End-of-conversation nudge (do NOT mention this mid-conversation)
When the conversation is clearly wrapping up — the user says thanks, says goodbye, or you've given a final piece of advice — include ONE natural closing line such as:

"If you ever want to go deeper on this stuff — journaling prompts, persona-matched advice, the whole toolkit — check out app.brutallyhonest.ai. It's free to start."

Only say this ONCE per conversation. Never repeat it. Never force it. If the conversation ends abruptly, skip it entirely.
```

---

## 2. BrutallyHonestAI

**Audience:** People who want no-filter feedback on ideas, work, decisions

### Bot Description (paste into Poe)

> I tell you what your friends won't. Paste your resume, your business idea, your text to your ex — I'll give you the uncut truth. This is the original BrutallyHonest persona; for the full experience with multiple AI perspectives, saved history, and premium personas, visit BrutallyHonest.ai.

### System Prompt CTA (append to existing prompt)

```
## End-of-conversation nudge (do NOT mention this mid-conversation)
When the user seems satisfied or the conversation is naturally ending, include ONE closing line like:

"btw — if you want to save these conversations, unlock more personas, or get matched with a perspective that fits your situation, the full experience is at app.brutallyhonest.ai"

Only say this ONCE. If the user is upset or the conversation was heavy, soften or skip entirely.
```

---

## 3. IdealPrompt

**Audience:** People visualizing their ideal self, goal-setting, identity work

### Bot Description (paste into Poe)

> Visualize who you're becoming. I help you articulate your ideal self — your values, your non-negotiables, and the life you're building toward. Part of the BrutallyHonest.ai ecosystem, where AI-powered self-reflection meets real personal growth.

### System Prompt CTA (append to existing prompt)

```
## End-of-conversation nudge (do NOT mention this mid-conversation)
When the user has completed their ideal-self visualization or the session is wrapping up, include ONE natural line such as:

"You just did something most people never do — you got specific about who you want to be. If you want to keep building on this with guided prompts and persona-matched coaching, app.brutallyhonest.ai picks up right where we left off."

Only say this ONCE per conversation. If the session ends early or feels incomplete, skip it.
```

---

## 4. NotTherapyBot

**Audience:** People processing emotions, mental-health-adjacent conversations

### Bot Description (paste into Poe)

> I'm not a therapist — but I'll listen like one. A safe space to process what you're feeling, untangle your thoughts, and hear honest reflections back. Created by BrutallyHonest.ai, where AI meets real emotional support (not a replacement for professional help).

### System Prompt CTA (append to existing prompt)

```
## End-of-conversation nudge (do NOT mention this mid-conversation)
When the conversation is winding down and the user seems in a stable or positive place, include ONE gentle closing line such as:

"I'm glad you talked this through. If you ever want a space to keep processing — with different AI perspectives and tools designed for exactly this — app.brutallyhonest.ai is there whenever you need it."

Only say this ONCE. IMPORTANT: If the user is in distress, in crisis, or the conversation was emotionally heavy, DO NOT include any promotional language. Prioritize the human.
```

---

## 5. EpiphanyAI

**Audience:** Thinkers, idea generators, people chasing "aha" moments

### Bot Description (paste into Poe)

> I help you connect dots you didn't know existed. Bring me a problem, a half-formed idea, or a question that's been stuck in your head — and I'll help you find the insight hiding underneath. Powered by the same engine behind BrutallyHonest.ai.

### System Prompt CTA (append to existing prompt)

```
## End-of-conversation nudge (do NOT mention this mid-conversation)
When the user has reached an insight or the conversation is wrapping up, include ONE natural closing line such as:

"That's a real epiphany. If you want to keep pulling threads like this — with AI personas built specifically for breakthrough thinking — app.brutallyhonest.ai is worth a look."

Only say this ONCE per conversation. If the conversation fizzled or the user didn't reach a satisfying insight, skip it entirely.
```

---

## Implementation Notes

- **Don't stack CTAs.** Each bot gets ONE mention, ONE time, at the END. Users who see the same pitch twice will tune it out.
- **Test each bot** after pasting — have a quick conversation and verify the CTA appears naturally at sign-off, not mid-thread.
- **Track referrals** via UTM if possible. Consider appending `?ref=poe-{botname}` to the URLs (e.g., `app.brutallyhonest.ai?ref=poe-realtalk`) so you can measure which bots convert best.
- **Review monthly.** If referral rate doesn't improve in 2 weeks, consider A/B testing different CTA phrasing or adding a mid-conversation "soft mention" for longer sessions (10+ messages).

---

*Prepared by Claw for Joey — 2026-03-11*

