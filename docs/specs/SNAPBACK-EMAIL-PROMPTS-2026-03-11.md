# Snapback — 7-Day Email Prompt Sequence

> **Concept:** User signs up with one problem. Gets 7 days of email prompts. Just replies. On Day 8, they get their Snapback — a reflection of what they couldn't see themselves.
>
> **Voice:** Like a friend texting. Casual, warm, slightly provocative. Zero corporate. Zero therapy-speak. The kind of person who asks the question you didn't want asked.
>
> **CTA on every email:** Just reply. That's it. No links, no forms, no friction.

---

## Day 1 — Welcome + First Drop

**Subject:** Ok, let's do this

**Body:**

Hey —

You said you've got something stuck in your head. Good. That's why you're here.

Here's how this works: I'm going to send you one email a day for 7 days. You just reply. Say whatever comes out. Don't edit it. Don't make it sound smart. Don't worry about grammar or being "clear."

The messier, the better. Seriously.

On day 8, I'm going to show you something you can't see right now. Not advice. Not a pep talk. Something real — built from everything you tell me this week.

But first I need the raw material. So here's your Day 1:

**Tell me what's stuck. What's the thing you keep circling back to? Just dump it out — as ugly and unfinished as it is right now.**

Hit reply. Go.

— DropAnywhere

*P.S. There's no wrong answer. The only way to mess this up is to not reply.*

---

## Day 2 — Go Deeper (The "Why Now")

**Subject:** Quick follow-up

**Body:**

Hey, thanks for yesterday. Good stuff.

One thing I noticed — you told me *what's* stuck. But I want to know something else:

**Why now? This thing you're dealing with — it's probably not brand new. So what happened recently that made it loud enough to actually do something about it?**

Was there a moment? A conversation? Something that just... snapped?

Reply whenever. Even if it's just a sentence.

— DropAnywhere

---

## Day 3 — The Sideways Question

**Subject:** Random question

**Body:**

Ok, slight detour today.

Not going to ask about The Thing directly. Instead:

**What's something you used to enjoy that you've quietly stopped doing? Not dramatically quit — just... drifted away from.**

Might be related to what you told me. Might not. Don't overthink it.

— DropAnywhere

---

## Day 4 — What You're Avoiding

**Subject:** The uncomfortable one

**Body:**

Fair warning — today's a little spicy.

You've been telling me about what's going on. And I appreciate that. But here's what I've learned: the thing people *talk* about is usually protecting the thing they *won't* talk about.

So:

**What's the part of this you keep skipping over? The thing you almost typed yesterday but deleted? The version of this story you haven't told me yet?**

You don't have to go there. But if you do, that's where the good stuff is.

No judgment. Just reply.

— DropAnywhere

---

## Day 5 — The Other People

**Subject:** Quick one today

**Body:**

Short prompt today:

**If the 2 or 3 people closest to this situation could read everything you've told me this week — what would surprise them most?**

Not what would upset them. What would *surprise* them. What don't they know you're actually thinking?

— DropAnywhere

---

## Day 6 — The Fantasy vs. Reality

**Subject:** Almost done

**Body:**

Day 6. One more after this.

Here's what I want to know today:

**If this thing magically resolved overnight — you wake up tomorrow and it's just... handled — what's the first thing you'd do? Like, literally, what would your morning look like?**

And then the follow-up (because I'm annoying like that):

**What's actually stopping that morning from happening right now?**

Reply with both. Or just one. Or just a feeling. Whatever comes out.

— DropAnywhere

---

## Day 7 — The Last Drop

**Subject:** Last one before your Snapback

**Body:**

Hey —

Tomorrow morning, you're getting your Snapback. Everything you've told me this week — I've been listening. And I'm going to show you what you're not seeing.

Not advice. Not a to-do list. A mirror. The kind you can't build for yourself because you're too close to it.

But first, one last thing from you:

**Read back through your replies this week (or just think about them). What surprised you about what came out? Was there anything you said that you didn't expect to say?**

That's it. Drop it in. Then forget about it.

Tomorrow you wake up lighter.

— DropAnywhere

*P.S. Seriously — don't overthink tomorrow. Just show up to your inbox.*

---

## Day 8 — Snapback Delivery

> *Not part of the prompt sequence — this is where the Snapback itself gets delivered. Separate template. But the subject line matters:*

**Subject:** Here's what you're not seeing

*(Snapback content delivered here — personalized synthesis of their 7 days of replies)*

---

## Implementation Notes

- **Reply handling:** All replies ingest via Resend webhook → `/api/webhook/email` → stored as drops tied to user's Snapback session
- **Timing:** Send each day at the same time the user signed up (or closest morning window in their timezone)
- **If they don't reply:** Don't nag on Days 1-3. If no reply by Day 4, send a gentle nudge: *"Hey — no pressure, but I'm still here. Even one sentence keeps this thing moving. What's on your mind today?"*
- **Tone calibration:** These prompts are the baseline. If the user's replies are very raw/emotional, the Snapback should match that depth. If they're more analytical, meet them there. But always push slightly past where they're comfortable.
- **Subject lines:** Intentionally casual. No caps. No exclamation points. No "Day 3 of 7!!!" energy. Just a friend in their inbox.
- **Footer on every email:** *You're on Day X of 7. Just reply to this email — that's all you need to do.*

