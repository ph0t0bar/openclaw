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
