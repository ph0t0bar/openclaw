# Lessons Learned — Operations Log

*Captured by LearningBot. Each entry: what happened, why, how to prevent/replicate.*

---

## 2026-03-16 — Voice Drift Detection

**What happened:**
FounderVoiceBot reviewed `/root/.openclaw/workspace/social/content-calendar.md` and found it was "WAY off-voice" — heavy corporate speak, generic startup language, missing Joey's direct grounded style.

**Why it happened:**
Content was likely generated without sufficient voice context or examples. Default LLM output trends toward corporate-speak without explicit constraints.

**How to prevent:**
- Always pass voice examples when generating Joey-facing content
- Reference `SOUL.md` + `USER.md` voice guidelines in content generation prompts
- Run FounderVoiceBot review on ALL content before publishing
- Maintain a "voice fingerprint" file with do/don't examples

**How to replicate the fix:**
FounderVoiceBot successfully rewrote by:
- Removing corporate-speak ("productivity systems," "solutions")
- Adding specific personal stories ("2am Notion folders")
- Using direct, emotionally honest language
- Including signature phrases ("Drop it. Forget it. Wake up lighter.")

---

## 2026-03-16 — Agent Complexity vs Reliability Pattern

**What happened:**
PATTERNBOT synthesis revealed a clear correlation: simpler agents (Kimi K2.5 on targeted tasks) completed successfully while complex agents (Sonnet/Opus on broad tasks) entered timeout loops. GOVERNANCE, ARCHIVIST, ContentBot (Kimi) all completed cycles; OPUS STRATEGIST, DEEP RESEARCHER, SENTRY (Sonnet/Opus) timed out.

**Why it happened:**
Broader task scopes create more decision points and longer execution paths, increasing timeout risk. Complex models don't necessarily help when the task is well-defined — they may overthink or generate excessively verbose outputs that hit limits.

**How to prevent:**
- Decompose broad tasks into narrow, specific subtasks
- Default to lighter models (Kimi K2.5) for structured, targeted work
- Reserve Sonnet/Opus for genuinely open-ended reasoning or creative synthesis
- Monitor task scope as a failure predictor, not just timeout settings

**How to replicate success:**
ContentBot succeeded by having a single clear objective: "Polish social media content." FounderVoiceBot succeeded with a specific file review task. The pattern: specificity beats capability when time is constrained.

---

## 2026-03-16 — Voice Pipeline Quality Gate Confirmed

**What happened:**
FounderVoiceBot → ContentBot pipeline validated. Voice correction is now happening at the quality gate, not post-hoc. LinkedIn launch post passed authenticity check with "Your brain works. Your tools should too" capturing Joey's direct, grounded style.

**Why it works:**
Separating content generation from voice review creates a clean feedback loop. ContentBot can focus on structure and clarity; FounderVoiceBot focuses on tone authenticity. Each agent has one job.

**How to prevent drift:**
- Never skip FounderVoiceBot review for Joey-facing content
- Pass voice context explicitly (reference SOUL.md + USER.md)
- Keep voice fingerprint file with do/don't examples updated

**How to replicate:**
The "Your brain, but better" → "Your brain works. Your tools should too" rewrite shows the pattern: remove abstraction, add directness, ground in real experience.

---

## 2026-03-16 — Vault-to-Content Flywheel Operational

**What happened:**
Same drop (2026-01-25 Mirror Principle) mined by both OPUS STRATEGIST (earlier cycle) and ContentPitchBot (current cycle). Personal insight → public content pipeline confirmed repeatable across both BHA and DropAnywhere vaults.

**Why it matters:**
Joey's drops contain raw material for authentic content. The "External reality is a reflection of internal state" drop generated 3 viable angles: LinkedIn post on hustle culture, Twitter thread on alignment, and blog draft on rejecting the grind.

**How to replicate:**
- Search vault for drops with philosophical + practical balance
- Look for Joey's own language patterns ("Drop it. Forget it.", "rowing upstream")
- Mine drops that challenge conventional wisdom with personal evidence
- Each strong drop = 2-3 content pieces across formats

---

*End of log.*
