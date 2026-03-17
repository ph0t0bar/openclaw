# User Scenario Matrix — Every Path Into & Through DropAnywhere

**Author:** Claw  
**Date:** 2026-03-11  
**Purpose:** Exhaustive map of every possible user journey. Every scenario has a lifecycle stage, admin visibility, and system response.

---

## Entry Points (How Users Arrive)

### A. Web Direct (drop-anywhere.com)

| # | Scenario | What Happens Now | What Should Happen | Lifecycle Stage |
|---|----------|-----------------|-------------------|-----------------|
| A1 | **Google organic → landing page → signup** | 3-step signup (email, intent, focus areas). Gets drip sequence. Pending admission. | ✅ Best path. Track UTM/referrer. Onboarding email Day 1. | `onboarding` |
| A2 | **Google organic → landing page → bounces** | Nothing. Lost forever. | Add retargeting pixel. Exit-intent capture? Low priority. | `lost` |
| A3 | **Google organic → landing page → drops without signing up** | Can't drop without account. Ghost input on homepage captures text but requires signup to save. | If ghost input captured text → carry it through signup (already works via `?drop=` param). Show value before asking for email. | `pre-signup` |
| A4 | **Direct URL (someone shared drop-anywhere.com)** | Same as A1. No referral tracking. | Track `?ref=` param. Know who's sharing. | `onboarding` |
| A5 | **Google → "honest ai" → BHA → cross-link to DA** | Lands on DA, signs up. No connection to their BHA account yet. | Identity merge: if same email used on BHA + DA, unify accounts. Their BHA conversations should appear in their DA vault. | `onboarding` |
| A6 | **Signup but never drops** | Account created. Drip emails fire. Sits in pending. | After 48h with 0 drops, send nudge: "Your first drop is the hardest. Here's an idea: tell us what's on your mind right now." | `new` |
| A7 | **Signup, drops once, never returns** | 1 drop in vault. Drip continues. May get admitted if auto-admit criteria met. | Day 2 email: "Your first drop is safe. Drop another and we'll start connecting dots." If no return in 7 days, win-back email. | `onboarding` |
| A8 | **Signup, drops 3+, pending admission** | Waiting for manual admit or auto-admit criteria. Getting drip emails. | Auto-admit at 3+ drops + 24h. No human should be needed here. | `pending` → `admitted` |
| A9 | **Signup, admitted, never opens digest** | Digest sent, 0 opens (if we track). | After 3 unopened digests: "Your digests are piling up. Wrong time of day? Wrong format? Reply and tell us." | `at-risk` |
| A10 | **Signup, admitted, opens digest, thumbs up** | Positive feedback recorded. | 🎉 Happy user. Occasional prompt: "Know someone who'd love this? Share your link." | `active` |
| A11 | **Signup, admitted, opens digest, thumbs down** | Negative feedback recorded. Shows in admin (correctly). | Auto-add to feedback inbox with digest content. Joey can see what they didn't like and respond. | `active` (needs attention) |
| A12 | **Signup, active, drops daily for 2 weeks, then stops** | Engagement score drops. Eventually auto-paused. | Day 3 of silence: "Hey, you were on a streak. Everything okay?" Day 7: "Miss you. Your vault has [N] drops waiting to become insights." | `at-risk` |
| A13 | **Signup, active, explicitly unsubscribes** | Digest disabled. Still has account. | Respect it. One final email: "Understood. Your drops are still safe if you ever want to come back." Remove from all outreach. | `churned` (voluntary) |
| A14 | **Signup, auto-paused after 5 digests without engagement** | digest_config.auto_paused = true. | Re-engagement email: "We paused your digests since you haven't been checking in. Want to restart? [One-click reactivate]" | `paused` |

### B. BHA / Poe Bots (Indirect Entry)

| # | Scenario | What Happens Now | What Should Happen | Lifecycle Stage |
|---|----------|-----------------|-------------------|-----------------|
| B1 | **Uses theREALrealtalk on Poe, has BHA account** | BHA webhook syncs conversation to DA vault. DA account auto-created. signup_source="bha". Welcome email sent ("Your conversation was saved ✓"). NOT admitted. | This person doesn't know DA exists. The welcome email is confusing without context. Needs BHA-specific welcome: "Your convo with [persona] was saved. Want daily insights from ALL your conversations? [Activate]" | `bha-synced` (new stage) |
| B2 | **BHA user, opened welcome email, clicked activate** | Digest enabled. Admitted. Starts getting digests based on BHA conversations. | Great — they opted in! First digest should reference their BHA conversations by name: "Based on your session with theREALrealtalk about [topic]..." | `admitted` |
| B3 | **BHA user, opened welcome email, did NOT activate** | Still pending. Conversations keep syncing. | Don't keep emailing. They saw it and chose not to. Maybe one follow-up after 3 more sessions: "You've had [N] conversations now. The patterns are getting interesting. Want to see them? [Activate]" | `bha-aware` |
| B4 | **BHA user, never opened welcome email** | Email sent, probably in spam or ignored. Conversations keep syncing silently. | These users don't know about DA at all. Don't email again. They're BHA users, not DA prospects. Only re-approach if they independently visit DA or use the Poe drop bot. | `bha-passive` |
| B5 | **BHA user, uses multiple personas** | Each conversation synced separately. All go to same vault via canonical identity. | Good data. If they ever activate, their digest will be rich. Track which personas they use for personalization. | `bha-synced` |
| B6 | **BHA user who ALSO signs up on DA independently** | Two accounts? Same email should merge via canonical identity. | Verify identity merge works. Their BHA conversations + DA drops should be in one vault. Welcome them as a power user: "We see you've been chatting with [persona] AND dropping on DA. Your digest will pull from everything." | `admitted` |
| B7 | **Poe DropAnywhere bot user (not BHA)** | Links email via verification code. Drops go to vault. Can view dashboard. | These ARE intentional DA users, just using Poe as the interface. Treat like DA-native. Auto-admit after 3+ drops. | `onboarding` |
| B8 | **Poe user who sees funnel CTA ("Try DropAnywhere")** | Clicks link to drop-anywhere.com. Signs up. No connection to Poe identity unless same email. | Track `?ref=poe` or `?ref=[botname]`. If they verify email on Poe bot later, merge identities. | `onboarding` |
| B9 | **BHA paying customer ($4.99/$7/$47)** | Has Stripe subscription. Uses BHA. Conversations sync to DA. | VIP treatment. These people are paying! If they haven't activated DA digest, personal outreach from Joey. They're already in the ecosystem. | `bha-synced` (VIP flag) |
| B10 | **BHA user whose conversations contain actual DA feedback** | Currently: keyword scanner flags as "negative feedback" (false positive). | New: Only flag if they explicitly mention "DropAnywhere", "the app", "my digest", "this email" — not emotional therapy language. | `bha-synced` |

### C. Email Ingest

| # | Scenario | What Happens Now | What Should Happen | Lifecycle Stage |
|---|----------|-----------------|-------------------|-----------------|
| C1 | **Existing user emails hello@drop-anywhere.com** | Resend webhook → ingest → vault. source="email". | Works. Make sure email reply confirms: "Got it ✓ — added to your vault." | `active` |
| C2 | **Unknown email sends to hello@drop-anywhere.com** | Creates new user? Or bounces? | Should auto-create account, send welcome: "We saved your email as a drop. Want daily insights? [Sign up to activate]" | `new` |
| C3 | **User replies to digest email** | Currently: unclear if this goes anywhere. Resend may not have reply webhook. | Critical gap. Digest replies should be captured as drops with source="email_reply" and flagged in feedback inbox. This is golden feedback. | `active` |
| C4 | **User replies to drip email** | Same issue — reply may go nowhere. | Same fix. All email replies should be captured. | `onboarding` |
| C5 | **User replies to welcome email (BHA)** | Probably goes to a no-reply or gets lost. | Capture these! A BHA user replying to "Your conversation was saved" is expressing interest. Flag in admin. | `bha-aware` |

### D. SMS/Voice

| # | Scenario | What Happens Now | What Should Happen | Lifecycle Stage |
|---|----------|-----------------|-------------------|-----------------|
| D1 | **User texts Twilio number** | Ingest → vault. source="sms". | Confirm: "Saved ✓". If new number, create account + ask for email to link. | `active` or `new` |
| D2 | **User calls Twilio number (voice drop)** | Transcribe → vault. source="voice". | Same. Voice is the most frictionless capture. Celebrate it. | `active` |
| D3 | **Unknown number texts** | New user created by phone. No email. Can't send digest. | Ask for email: "Hey! I saved your thought. Want daily insights? Reply with your email." | `new` |

### E. iOS Shortcut / API

| # | Scenario | What Happens Now | What Should Happen | Lifecycle Stage |
|---|----------|-----------------|-------------------|-----------------|
| E1 | **User sends via iOS Shortcut** | POST /api/ingest, source="api". Goes to vault. | Works. Power user behavior. Track shortcut usage as engagement signal. | `active` |
| E2 | **User sends via API directly** | Same as E1. | Same. These are developers/power users. | `active` |

### F. Referral / Social

| # | Scenario | What Happens Now | What Should Happen | Lifecycle Stage |
|---|----------|-----------------|-------------------|-----------------|
| F1 | **Existing user shares DA with a friend** | No referral tracking. Friend signs up independently. | Add `?ref=USER_ID` links. Track referral chains. Thank the referrer: "Someone you shared DA with just signed up!" | `onboarding` (referred) |
| F2 | **Joey tweets/posts about DA, someone clicks** | UTM params if set, otherwise no tracking. | Always use UTM links. Track social → signup conversion. | `onboarding` |
| F3 | **Gumroad buyer (Genesis Orchestrator $97)** | Gets product. Has email. No DA account created. | Email capture → auto-create DA account → special welcome: "As a Genesis owner, you get early access to DropAnywhere." | `new` (premium) |

### G. Edge Cases & Failure Modes

| # | Scenario | What Happens Now | What Should Happen | Lifecycle Stage |
|---|----------|-----------------|-------------------|-----------------|
| G1 | **User signs up with throwaway/spam email** | Account created. Drip emails bounce. | Detect bounce → flag in admin. Don't count as real user. | `invalid` |
| G2 | **Same person, multiple emails** | Multiple accounts, no merge. | Canonical identity should handle this — but only if they verify both emails on same Poe account or explicitly link them. | needs merge |
| G3 | **User in non-English language** | Drops in Spanish/French/etc. Digest generated in English (probably). | Detect language from drops. Generate digest in user's language. Flag in admin if mismatch. (Known issue: one@0it.us drops in Spanish) | `active` (language flag) |
| G4 | **User drops sensitive/NSFW content** | Stored as-is. Included in digest. | Content moderation flag? At minimum, don't include in admin previews without warning. | `active` |
| G5 | **Bot/spam signup** | Account created. May trigger drip sequence. | Detect: no real drops after 72h + email bounce + no login = auto-archive. | `invalid` |
| G6 | **User forgets password / can't log in** | Login is email-based magic link? Or password? | If they email hello@ saying "can't log in" → should be captured as support request, not a drop. | `active` (support) |
| G7 | **Family/friends (mom, dad, Danny)** | Same system as everyone else. | Special handling in admin. Flag as "Joey's circle." Surface issues to Joey proactively. Already in user-profiles.md. | `active` (VIP) |
| G8 | **User was active, archived, wants to come back** | Can be restored via admin. | One-click restore in admin. Welcome-back email. Catch them up: "While you were gone, we added [features]. Your [N] drops are still here." | `churned` → `active` |
| G9 | **User drops a URL/link** | Stored as text. No link preview or content extraction. | Future: extract page title, summary. Add as metadata. Richer digest context. | `active` |
| G10 | **User drops an image/screenshot** | Not handled (iOS Shortcut limitation noted). | Future: OCR/vision → extract text → store as enriched drop. | `active` |
| G11 | **User tries to use DA features (intel map, settings) while pending** | May see empty states or errors. | Clear messaging: "You're almost in! Drop [N] more times to activate your account." Progress bar toward admission. | `pending` |
| G12 | **Two users share a device/email** | One account, mixed drops. | Out of scope for now. Not a realistic problem at current scale. | — |
| G13 | **User gives feedback via !feedback in Poe bot** | Stored in user's feedback[] array. | Must flow to unified feedback inbox. Currently nobody checks this. | `active` |
| G14 | **User DMs Joey on Twitter/Instagram about DA** | Manual, no system capture. | Future: social listening. For now, Joey manually creates a drop via admin: "Feedback from @handle: [content]" | — |
| G15 | **User's digest email goes to spam** | They never see it. Think DA stopped working. | Track Resend delivery status. If bounced/spam → flag in admin. Send nudge via different channel if possible. | `at-risk` |
| G16 | **User on waitlist gives up** | Stops dropping. Eventually goes silent. | Track "days pending without activity." After 7 days pending with no new drops: "Still want in? Drop one more thought and we'll fast-track your digest." | `churned` (never activated) |
| G17 | **Power user who drops 20+/day** | All stored. Big digest. | May need digest summary mode. Flag as power user in admin. Potential champion/advocate. | `active` (power user) |
| G18 | **User who only reads digests, never drops** | engagement_score stays high (they're "engaging" by opening). But vault is stale. | Nudge in digest footer: "Your vault has [N] drops from [date range]. Fresh thoughts make better insights. [Drop now]" | `active` (passive consumer) |
| G19 | **User asks a question in a drop ("how do I use this?")** | Stored as a regular drop. Included in next digest. | Detect question intent. Flag as support request. Route to feedback inbox or auto-respond. | `active` (support) |
| G20 | **BHA user who has ONLY had 1 short conversation** | Account created. 1 "drop" (the convo). Welcome email sent. | Don't create DA account for single short conversations (<5 messages). Wait until they're a repeat user. Reduces noise. | `bha-passive` |

---

## Lifecycle State Machine (Complete)

```
                                    ┌──────────────┐
                                    │   INVALID    │ (spam/bounce/bot)
                                    └──────────────┘
                                           ↑
                                      auto-detect
                                           │
┌─────────┐    signup    ┌─────────────┐  drop  ┌────────────┐  3+drops  ┌──────────┐
│ PRE-     │ ──────────→ │    NEW      │ ─────→ │ ONBOARDING │ ────────→ │ PENDING  │
│ SIGNUP   │             │ (0 drops)   │        │ (1-2 drops) │          │(awaiting) │
└─────────┘              └─────────────┘        └────────────┘          └──────────┘
                              │                                              │
                              │ 48h no drop                          auto-admit (3+drops, 24h+)
                              ↓                                              │
                         ┌─────────┐                                         ↓
                         │ NUDGE   │                                  ┌────────────┐
                         └─────────┘                                  │  ADMITTED  │
                                                                      │(digest on) │
                                                                      └────────────┘
                                                                           │
                                                              ┌───────────┴───────────┐
                                                              ↓                       ↓
                                                       ┌──────────┐            ┌───────────┐
                                                       │  ACTIVE  │            │ AT-RISK   │
                                                       │(engaged) │            │(7d silent)│
                                                       └──────────┘            └───────────┘
                                                              │                       │
                                                              │                       ↓
                                                              │                ┌──────────┐
                                                              │                │ PAUSED   │
                                                              │                │(auto/self)│
                                                              │                └──────────┘
                                                              │                       │
                                                              │          30d inactive  │
                                                              ↓                       ↓
                                                       ┌──────────┐            ┌──────────┐
                                                       │ CHAMPION │            │ CHURNED  │
                                                       │(advocate) │            │(gone)    │
                                                       └──────────┘            └──────────┘

BHA PARALLEL TRACK:
┌─────────────┐  welcome email  ┌────────────┐  clicked activate  ┌──────────┐
│ BHA-SYNCED  │ ──────────────→ │ BHA-AWARE  │ ─────────────────→ │ ADMITTED │
│(auto-created)│                │(saw email) │                    │(DA user) │
└─────────────┘                 └────────────┘                    └──────────┘
      │                              │
      │ never opened email           │ saw but didn't activate
      ↓                              ↓
┌─────────────┐               ┌────────────┐
│ BHA-PASSIVE │               │ BHA-AWARE  │ (don't email again)
│(don't email)│               │ (1 follow-up after 3 sessions)
└─────────────┘               └────────────┘
```

---

## Admin Visibility Requirements

For EVERY user in the system, the admin should show:

| Field | Source | Purpose |
|-------|--------|---------|
| `lifecycle_stage` | Computed | Where they are in the journey |
| `entry_point` | signup_source + first vault item source + referrer | How they found us |
| `products_used` | Vault item sources | DA only? BHA only? Both? Poe? Email? |
| `days_in_stage` | Computed from timestamps | How long they've been stuck |
| `drop_count` | Vault length | Engagement depth |
| `drop_sources` | Unique sources in vault | Which channels they use |
| `last_drop_preview` | Last vault item, truncated | Quick context |
| `digests_received` | Digest store count | Are they getting value? |
| `digest_feedback` | Thumbs history | What do they think? |
| `email_status` | Resend delivery data | Are emails even landing? |
| `welcome_email_opened` | Track via Resend | BHA users: did they see it? |
| `onboarding_complete` | signup_profile fields | Did they fill out intent/focus? |
| `flags` | Computed | VIP, power-user, language-mismatch, support-request, feedback-pending |
| `suggested_action` | Computed | What Joey should do next for this user |
| `outreach_history` | New tracking | Has Joey reached out? When? What happened? |

---

## Automated Responses Per Stage

| Stage | Trigger | Auto-Response |
|-------|---------|---------------|
| `new` | 48h, 0 drops | Nudge email: "Your first drop is the hardest..." |
| `onboarding` | Drop 1 received | Confirm: "Got it ✓ — drop 2 more and your daily digest activates." |
| `onboarding` | Drop 3 received | "You're in! First digest tomorrow morning." + auto-admit |
| `pending` | 7 days waiting | "Still want in? Drop one more thought and we'll fast-track you." |
| `admitted` | First digest sent | "Your first digest just went out! Check your email. 👍/👎 to tell us how we did." |
| `active` | 14-day streak | "You're on a 14-day streak! Know someone who'd love this?" |
| `at-risk` | 3 days no activity | Gentle: "Haven't heard from you — everything okay?" |
| `at-risk` | 3 unopened digests | "Your digests are piling up. Wrong time? Wrong format? Reply to tell us." |
| `paused` | Auto-pause triggered | "We paused your digests. One click to restart: [reactivate]" |
| `churned` | 30 days gone | Final: "Your [N] drops are still safe. Come back anytime. [reactivate]" |
| `bha-synced` | After 3rd BHA session | "You've had [N] conversations. Want daily insights? [Activate digest]" |

---

---

## Opt-Out Tracking (Mandatory)

### Three distinct states for digest delivery:

| State | Field | Meaning | Can re-enable? |
|-------|-------|---------|----------------|
| **Not admitted** | `digest_enabled=false`, no `opted_out` | New user, never activated | Admin admits manually |
| **Admin disabled** | `digest_enabled=false`, `disabled_by="admin"` | Joey turned off for a reason | Admin re-enables |
| **Pure opt-out** | `opted_out=true`, `opted_out_at=timestamp` | User clicked unsubscribe | ONLY the user can re-enable (via resubscribe link) |

### Rules:
- `opted_out=true` is sacred. Never override it programmatically. Never re-enable without the user's explicit click on a resubscribe link.
- Admin page should show opt-out status clearly: 🚫 = opted out, distinct from ⏸️ = admin disabled
- Both unsubscribe endpoints (`/api/unsubscribe` and `/api/digest/unsubscribe`) must set `opted_out=true` + `opted_out_at`
- The admin "Admit" button should be grayed out for opted-out users with a note: "User opted out on [date]"

### Current state (March 11, 2026):
- 3 users have `digest_enabled=false` (sjksjsss5055, jasonscotthand, chriswkiser) — unclear if these are opt-outs or admin actions
- 57 BHA-only users just disabled via migration — these are NOT opt-outs, they never opted IN
- Need to retrofit `opted_out` tracking on the 3 existing disabled users

---

## Manual Admission Protocol (effective March 11, 2026)

**All new users start with `digest_enabled=false`.** No auto-admit. No drip-triggered admission.

**To admit a user, Joey must:**
1. See them in the admin pending queue
2. Review their drops, source, and intent
3. Click "Admit" — sets `digest_enabled=true`, `admitted=true`, `admitted_at=timestamp`, `admitted_by="joey"`
4. User gets welcome email: "Your daily digest is now active. First one tomorrow morning."

**Why manual for now:**
- 68 users total — manageable
- Need to understand who's real vs noise
- BHA crossover users need different treatment than DA-native
- Once patterns are clear, re-introduce smart auto-admit with guardrails

---

*This matrix should be integrated into the PRD Section 6b and referenced by the Admin Lifecycle Dashboard spec.*

