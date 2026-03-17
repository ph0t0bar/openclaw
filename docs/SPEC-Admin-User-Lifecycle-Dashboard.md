# Spec: Admin User Lifecycle Dashboard

**Author:** Claw + Joey  
**Date:** 2026-03-11  
**Status:** Draft — ready for Dropper-Code  
**Target:** opoerator-hub (API) + dropanywhere-app (frontend)  
**Priority:** High — 48 users stuck in limbo right now

---

## The Problem

The admin page shows aggregate numbers but can't answer basic questions:

1. **Who is clicking "Drop" and do they know what it is?** — 13 users have exactly 1 drop and stopped. Did they understand the product? Did onboarding fail?
2. **How did they get here?** — Most pending users came from BHA (`signup_source: bha`) but the admin can't filter or sort by acquisition channel.
3. **What feedback is trapped?** — 48 users are pending admission. Their drops sit in a vault they can't access. Some may contain feedback, questions, or cries for help that nobody reads.
4. **What's their real health?** — Engagement score exists but isn't visible per-user on the admin page. Can't see the lifecycle stage.

### Current State (March 11, 2026)

| Segment | Count | Problem |
|---------|-------|---------|
| Total users | 68 | — |
| Waiting for admission | **48** | Dropping into a void. No digest. No access. |
| Exactly 1 drop | 13 | Tried once, stopped. Onboarding failure? |
| Zero drops | 3 | Signed up, never dropped. |
| Low engagement (<40) | 1 | Churning |
| Digest disabled | 3 | Opted out or never opted in |
| BHA-sourced (pending) | ~40 | Came from Poe bots, may not understand DA |

---

## The Solution: User Lifecycle View

### Lifecycle Stages

Every user should be in exactly one stage:

```
[NEW] → [ONBOARDING] → [PENDING] → [ADMITTED] → [ACTIVE] → [AT-RISK] → [CHURNED]
                                                      ↓
                                                  [PAUSED]
```

| Stage | Definition | Admin Action |
|-------|-----------|-------------|
| **New** | Signed up, 0 drops | Auto-nudge or manual outreach |
| **Onboarding** | 1-2 drops, < 48h old | Monitor — drip sequence should be working |
| **Pending** | Has drops but not admitted | Review & admit, or auto-admit if criteria met |
| **Admitted** | Admitted, receiving digests | Happy path |
| **Active** | Admitted + engaged in last 7 days | Healthy |
| **At-Risk** | No engagement in 7+ days, or 5+ digests without interaction | Win-back nudge |
| **Paused** | Auto-paused or self-paused | Re-engagement email |
| **Churned** | No activity in 30+ days | Archive candidate |

### New API Endpoint: `/api/admin/users/lifecycle`

Returns users grouped by lifecycle stage with rich context:

```json
{
  "stages": {
    "pending": [
      {
        "user_id": "abc123",
        "email": "user@example.com",
        "signup_source": "bha",       // How they found us
        "signup_date": "2026-03-08",
        "days_waiting": 3,
        "drop_count": 8,
        "last_drop_date": "2026-03-10",
        "last_drop_preview": "I love this app but...",  // First 100 chars
        "has_feedback_drops": true,    // Contains feedback keywords
        "onboarding_complete": false,
        "intent": "",                  // From signup profile
        "engagement_score": 65,
        "referral_chain": "theREALrealtalk → BHA welcome email → DA signup"
      }
    ],
    "active": [...],
    "at_risk": [...],
    ...
  },
  "summary": {
    "new": 3,
    "onboarding": 5,
    "pending": 48,
    "admitted": 20,
    "active": 15,
    "at_risk": 3,
    "paused": 0,
    "churned": 2
  }
}
```

### Enhanced Admin Frontend Sections

#### 1. User Lifecycle Funnel (top of page)
Visual funnel showing conversion at each stage:
```
New (3) → Onboarding (5) → Pending (48) ← BOTTLENECK → Admitted (20) → Active (15)
```
The bottleneck is immediately visible: 48 pending vs 20 admitted.

#### 2. Per-User Card (click to expand)
For each user, show:
- **Identity:** email, signup source, signup date
- **Journey:** acquisition channel → first drop → current stage
- **Drops:** count, last drop date, preview of last 3 drops
- **Feedback:** any feedback-tagged drops (highlight these!)
- **Digests:** count received, last opened, thumbs up/down history
- **Health:** engagement score, days since last activity
- **Actions:** [Admit] [Send Nudge] [View Drops] [Archive]

#### 3. Feedback Inbox (replaces current broken feedback view)
Only show REAL feedback:
- Digest thumbs down (with digest content preview)
- Drops with `source: "feedback"`
- Drops with `category: "feedback"` or matching explicit feedback keywords from ADMITTED users only
- `!feedback` command submissions
- **Exclude:** BHA conversation logs, pending user emotional language

#### 4. Pending Users Queue (priority view)
Sort pending users by:
1. Drop count (more drops = more engaged = admit first)
2. Days waiting (longer wait = higher urgency)
3. Has feedback drops (they're trying to tell us something!)
4. Signup source (organic web > BHA referral for intent signal)

One-click "Admit" button. Batch "Admit All" for users meeting criteria (3+ drops, email verified).

#### 5. Acquisition Source Breakdown
| Source | Users | Conversion to Active | Avg Drops |
|--------|-------|---------------------|-----------|
| BHA (Poe bots) | 40 | 12% | 7.2 |
| Web (organic) | 15 | 60% | 14.5 |
| Email | 8 | 45% | 11.0 |
| API | 5 | 80% | 22.0 |

This tells you immediately: BHA users need different onboarding than organic web users. They arrived through a chatbot — they may not understand "drop" as a concept.

---

## Implementation Plan

### Phase 1: API (opoerator-hub) — 4-6h
- [ ] New endpoint `/api/admin/users/lifecycle` with stage grouping
- [ ] Add `lifecycle_stage` computed field to user data
- [ ] Fix feedback endpoint: exclude BHA/Poe sources from keyword scan (task already filed)
- [ ] Add `last_drop_preview` field (first 100 chars of most recent drop)
- [ ] Add `signup_source` to admin users list (already tracked, just not exposed)

### Phase 2: Frontend (dropanywhere-app) — 8-12h
- [ ] Lifecycle funnel visualization at top of admin page
- [ ] User cards with expand/collapse
- [ ] Feedback inbox (real feedback only)
- [ ] Pending users queue with batch admit
- [ ] Acquisition source breakdown table

### Phase 3: Automation — 4h
- [ ] Auto-admit users meeting criteria (3+ drops, email verified, 24h+ since signup)
- [ ] Surface "trapped feedback" from pending users to Joey (daily brief or admin alert)
- [ ] BHA-specific onboarding email: "You found us through [bot name]. Here's how DropAnywhere works..."

---

## Immediate Action (Tonight)

The 48 pending users need attention. Top candidates for admission right now:
- `mattilaben@gmail.com` — 10 drops, from BHA
- `emmawilcox121@gmail.com` — 8 drops, from BHA  
- `aaryashreeisharma@gmail.com` — 8 drops, from BHA
- `jamesruckers10@outlook.com` — 8 drops
- `kieranlewisai@gmail.com` — 8 drops

These people are actively using the product without being able to see their digests.

---

## Section B: Unified Feedback Inbox

### The Problem

Feedback is scattered across 6 places and nobody's reading most of it:

| Source | Where it lives now | Who can see it? |
|--------|-------------------|-----------------|
| Digest thumbs up/down | `*_digests.json` | Admin page (aggregate only) |
| `!feedback` command | User's `feedback[]` array | Nobody checks this |
| Drops with feedback intent | User's vault | Mixed in with everything else |
| BHA conversations (emotional) | User's vault | Misclassified as negative feedback |
| Welcome email replies | Resend inbox? | Probably nobody |
| Direct replies to digest emails | Resend/Gmail | Joey manually |

### The Solution: One Inbox

New endpoint: `/api/admin/feedback/inbox`

Every feedback item gets:

```json
{
  "id": "fb_12345",
  "user_id": "abc123",
  "user_email": "user@example.com",
  "source": "digest_rating",          // digest_rating | feedback_command | drop | email_reply | bha_session
  "sentiment": "negative",            // positive | negative | neutral | question
  "content": "The digest didn't mention my project ideas at all",
  "content_preview": "The digest didn't mention...",
  "timestamp": "2026-03-10T14:00:00Z",
  "context": {
    "signup_source": "web",            // How they found us
    "lifecycle_stage": "active",       // Where they are now
    "days_as_user": 14,
    "total_drops": 23,
    "digests_received": 10,
    "last_active": "2026-03-10",
    "products_used": ["da", "bha"],    // Which products they actually use
    "recent_drops_preview": [          // Last 3 drops for context
      "Working on my startup pitch deck...",
      "Meeting with investors went well...",
      "Need to figure out pricing..."
    ]
  },
  "responded": false,                  // Has Joey replied?
  "response": null                     // Joey's response if sent
}
```

### What counts as feedback (and what doesn't)

**Include:**
- Digest thumbs down (with the digest content so you know what they didn't like)
- Digest thumbs up (positive signal — still useful)
- `!feedback` command submissions
- Drops explicitly tagged `source: "feedback"` or `category: "feedback"`
- Replies to digest/welcome/drip emails (need Resend webhook for this)
- BHA conversations where user explicitly mentions DropAnywhere, the app, the digest, etc.

**Exclude:**
- BHA therapy conversations (emotional keywords ≠ product feedback)
- Random vault drops with incidental keyword matches
- Automated system entries

### Outreach: Talk to Users from Admin

For each user in the feedback inbox, Joey should be able to:

1. **See full context** — who they are, how they got here, what they've been doing, what they've said
2. **Send a personal email** — with context-aware suggested templates:

**Templates (auto-generated based on user context):**

For a churning DA user:
> Hey [name], I noticed you stopped getting digests a few days ago. Was something off? I'm the founder and I genuinely want to know — even if it's "the whole thing sucks." Reply to this email and it goes straight to me.

For a BHA user who's never seen DA:
> Hey [name], you've been having some great conversations with [persona]. Did you know those insights are being saved? DropAnywhere turns them into a daily digest — one email, every morning, connecting the dots across everything you've been thinking about. Want to try it? [one-click activate link]

For a user who thumbs-downed a digest:
> Hey [name], I saw you weren't happy with yesterday's digest. What would have made it better? Was it missing something? Too generic? I read every piece of feedback personally.

For a pending user with 8+ drops:
> Hey [name], you've been dropping a lot of great stuff. I just activated your daily digest — you'll get your first one tomorrow morning. Let me know what you think.

3. **One-click actions:**
   - [Admit] — activate their digest immediately
   - [Reply] — send personalized email
   - [View Vault] — see their drops
   - [Archive] — remove from inbox (not from system)
   - [Mark Responded] — track that you've reached out

### API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/admin/feedback/inbox` | GET | Paginated feedback inbox, filterable by source/sentiment/responded |
| `/api/admin/feedback/{id}/respond` | POST | Send email response + mark as responded |
| `/api/admin/feedback/{id}/dismiss` | POST | Dismiss from inbox |
| `/api/admin/user/{id}/outreach` | POST | Send templated email with context |
| `/api/admin/user/{id}/admit` | POST | Admit + send activation email |
| `/api/admin/user/{id}/context` | GET | Full user context card |

### Implementation

**Phase 1 (API):** Build `/feedback/inbox` and `/user/{id}/context` endpoints. Fix feedback classification. Tag real feedback vs noise.

**Phase 2 (Frontend):** Feedback inbox tab on admin page. User context cards. Reply button with template suggestions.

**Phase 3 (Outreach):** Email send from admin. Template library. Track responses. Close the loop.

---

## Section C: User Pool Segmentation

### The Truth About "68 Users"

These aren't 68 DA users. They're 3 different populations:

| Pool | Count | Reality | Admin Treatment |
|------|-------|---------|-----------------|
| **DA-native** | ~16-20 | Signed up on drop-anywhere.com, dropping intentionally | Full lifecycle management |
| **BHA crossover** | ~32 | Chatbot users on Poe/BHA. Never visited DA. Conversations auto-synced via webhook. | Separate conversion funnel |
| **Admitted active** | ~20 | Real product users getting digests | Retain & delight |

The admin page MUST separate these. A BHA user with 8 "drops" is not the same as a DA user with 8 drops. The BHA user's drops are therapy conversations — they didn't "drop" anything. The DA user intentionally captured thoughts.

### Per-Pool Admin Views

**DA-native users:** Standard lifecycle funnel. These people chose DA. Focus on activation and retention.

**BHA crossover:** Conversion funnel. These people chose a chatbot. The question is: do they want a digest? Show:
- Which persona they use most
- Whether they opened the welcome email
- Whether they clicked the activate link
- Whether they've ever visited drop-anywhere.com

**Admitted active:** Retention dashboard. These are your real users. Show:
- Digest open rates (if trackable)
- Thumbs up/down history
- Drop frequency trends
- Feature usage (intelligence map, settings, etc.)

---

*This spec connects to Joey's "Unified Feedback Funnel" drop (2026-03-11) and the PRD Section 6b backlog.*

