# COMPASS — DropAnywhere Strategic North Star

**Version:** 2026-03-17-v2 (Onboarding Expansion)
**Status:** APPROVED by Joey — this supersedes PRD.md for launch decisions
**Next Review:** Post-launch (Mar 31, 2026)

> ⚠️ **v2 Changes (Joey feedback 03-17 02:43 UTC):** Onboarding sequence expanded beyond 3 emails. See Section 6 below.

---

## The Product (Email-Only)

**What we ship:** Intelligence delivered as email. No dashboard at launch.

- **Capture:** Users email drop@drop-anywhere.com
- **Process:** AI extracts themes, finds connections, surfaces patterns
- **Deliver:** Intelligence Map sent as beautiful digest email
- **Frequency:** Daily or weekly (user chooses)
- **Frontend:** Static landing page + waitlist signup only

**Core Promise:** "Drop it. Forget it. Wake up lighter."

---

## The Three Launch Deliverables

| Deliverable | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| Intelligence Map Email Template | Drop | Mar 20 | ⬜ Not started |
| Expanded Onboarding Sequence (>3 emails) | Drop | Mar 21 | ⬜ Not started |
| Static Landing Page | Dropper-Code | Mar 22 | ⬜ Not started |

---

## Strategic Decisions (The 5 Questions)

### 1. TRIAGE SYSTEM
**Decision:** Automated routing with manual override

**How it works:**
- All inbound → `drop@drop-anywhere.com`
- Hub webhook → instant processing (PR #193)
- Classification: drop vs support vs billing vs personal
- Routing: digest queue vs priority inbox vs Joey
- Cadence detection: AI analyzes drop patterns, suggests daily/weekly
- Feedback loop: reply to any digest with "daily" / "weekly" / "pause"

**Trial structure:**
- Week 1: Daily (high touch, prove value)
- Week 2+: Recommend cadence based on drop volume
- User can override anytime

---

### 2. STRIPE & BILLING
**Decision:** Generous trial → usage-based tiers

**Trial (14 days):**
- 50 drops included
- Full Intelligence Map
- Daily or weekly digest
- No credit card required

**Post-trial Tiers:**
| Tier | Price | Drops | Features |
|------|-------|-------|----------|
| Free | $0 | 10/mo | Weekly digest, basic themes |
| Lite | $7/mo | 100/mo | Daily or weekly, full Intelligence Map |
| Pro | $15/mo | 500/mo | Multiple emails, API access |
| Custom | $49/mo | Unlimited | Team features, custom templates, dedicated domain |

**Friction removal:**
- One-click upgrade (Stripe link, no checkout flow)
- Pay-as-you-go overages ($0.10/drop above limit)
- Pause anytime (data retained, resume later)

---

### 3. EMAIL LISTS
**Decision:** 4 foundational segments

| List | Purpose | How They Join |
|------|---------|---------------|
| **Feedback** | Beta testers, power users | Personal invite by Joey |
| **BHA** | BrutallyHonest.ai cross-sell | Auto-sync from BHA (opt-in) |
| **DA Interested** | Waitlist, prospects | Landing page signup |
| **Friends & Family** | Inner circle | Joey adds manually |

**Segmentation rules:**
- One person can be on multiple lists
- Each list gets different email content/CTAs
- Friends & Family get "skip the waitlist" priority

---

### 4. TIERS & UPGRADE PATH
**Decision:** Land with Lite ($7/mo), expand later

**Launch scope:**
- Free: teaser, limited value
- Lite: the main product
- Pro: for power users
- Custom: enterprise/teams (post-launch)

**Future upgrades (not launch):**
- More crons → API access
- More projects → team workspaces
- More powerful models → Pro tier
- Bring your own API → self-hosted option
- Dashboard → Phase 2 (if users demand)
- Outbound email address → custom drop@yourdomain.com
- Custom templates → white-label
- Public dashboard → business tier

**Pricing principle:** Charge for value delivered (insights), not features (dashboards)

---

### 5. DATA SEPARATION
**Decision:** Row-level isolation, encrypted at rest

**Architecture:**
- Each user: isolated database row
- Data access: scoped to user_id only
- Encryption: AES-256 at rest (Railway volumes)
- Backups: daily to S3, encrypted
- Retention: soft delete, 30-day recovery
- Export: GDPR-compliant data portability

**Security:**
- No cross-user queries possible
- API keys rotate monthly
- Webhook tokens unique per user
- Audit log: who accessed what, when

**The "smaller slice":**
- Each user's data = one PostgreSQL row + one Resend contact
- Intelligence = ephemeral (generated, emailed, discarded)
- Vault = user's email inbox (we don't store history)
- Analytics = aggregate only (no individual tracking)

---

## What We Cut (No Longer Launch Scope)

- Dashboard UI (all tabs)
- Authentication system (OAuth, sessions)
- Settings page
- Vault view
- Stream view
- Activity feed
- Compass page (ironically)
- Public-facing Intelligence Map
- Real-time features
- Push notifications

**Time saved:** ~103 hours frontend work

---

## What Must Work Perfectly

1. Email deliverability (inbox, not spam)
2. Intelligence Map quality (themes, connections, patterns)
3. Admission flow (waitlist → welcome → first digest)
4. Stripe billing (trial → payment without friction)
5. Hub webhook → instant processing (no polling delays)

---

## Open Decisions (Joey to decide)

- [ ] **Soft launch list:** Confirm 12 users across 3 tiers
- [ ] **Trial length:** 7 days vs 14 days vs 30 days
- [ ] **Free tier:** Keep or remove? (Some say it's a crutch)
- [ ] **First digest timing:** Immediate vs overnight vs user-scheduled
- [ ] **Poe balance:** Add credits or pause heavy bots before depletion

---

## Source Files

| Document | Location | Purpose |
|----------|----------|---------|
| This COMPASS | `ops/COMPASS.md` | Single source of truth |
| Revised Audit | `ops/audit/MASTER-REPORT-v2-EMAIL-ONLY.md` | Full technical findings |
| Agency Poll | `ops/strategic-poll-email-only-pivot.md` | 10 department votes |
| 5 Questions | `ops/strategic-answers-email-only-pivot.md` | Detailed answers |
| Daily Log | `memory/YYYY-MM-DD.md` | Execution updates |

---

---

## 6. ONBOARDING SEQUENCE (Joey Modifications — v2)

**Decision:** Onboarding is MORE than 3 emails. Collect user context first.

**Joey's feedback (03-17 02:43 UTC):**
> "I believe we need to consider more than a 3 email onboarding. We have to collect info from them so we can understand what they need (this is where varying digests will come in handy - the ones we already created and live in hub code). Ideally we educate, entertain, ask questions."

**Updated onboarding philosophy:**
- **Educate** — teach them how to drop, what the Intelligence Map is, why it works
- **Entertain** — make them look forward to the next email
- **Ask questions** — collect context so we know which digest variant to use

**Intelligence Map gate:**
- Generated and always available once enough drops are collected (not time-gated)
- Users earn it by dropping, not by waiting

**Digest variants in Hub (existing, to be activated):**
- Use existing digest type variants already in `opoerator-hub` codebase
- FeedbackBot to pull list from Hub code — not reinvent this

**Sequence structure (to be designed):**
1. Welcome + "How to drop" (immediate)
2. First drop confirmation + what happens next
3. Educate: "What your Intelligence Map will look like"
4. Ask: "What are you trying to figure out?" (context collection)
5. Entertain: Example Intelligence Map + real user story
6. Engage: "You're almost there — X more drops to unlock your map"
7. Unlock: First Intelligence Map delivery
8. Ask again: "Daily or weekly? What topics matter most?"
- ... (ongoing based on behavior)

**Key constraint:** Sequence must use existing Hub digest variants — don't build new infrastructure.

---

## Version History

| Date | Version | Change |
|------|---------|--------|
| Mar 16 | v1 | Email-only pivot approved |
| Mar 17 | v2 | Onboarding expanded (Joey feedback) — >3 emails, educate/entertain/ask model, Intelligence Map unlocked by drops |

---

*Reply to this file's email thread for updates. Drop maintains this as the single source of truth for launch decisions.*

---

## Joey's Feedback (Mar 16, 10:28 PM) — APPROVED WITH MODIFICATIONS

### Deliverable #2 EXPANDED: Onboarding Funnel (not just 3 emails)

**Joey's direction:** More than 3 emails. The onboarding should:
- Collect info from users to build profiles (→ Postgres)
- Educate on how to use DropAnywhere
- Entertain (keep them engaged)
- Ask questions (data collection = better digests)
- Use varying digest styles (already built in Hub code)
- Premium users get instant "clarity responses" on drops
- Include reminders and nudges

**Profile building:** All user data collected during onboarding flows into Postgres profiles. Foundation already exists in Hub.

**Claude Code budget:** Joey on $100 plan, likely upgrading to $200.

**Landing page:** Confirmed — lots of great stuff already built, just trim.

**Storage/flow/lifecycle:** Needs further hashing out. Joey excited: "I can see it all happening and happening well!"

### Updated Deliverables

| Deliverable | Owner | Deadline | Status | Change |
|-------------|-------|----------|--------|--------|
| Intelligence Map Email Template | Drop | Mar 20 | ⬜ | No change |
| Onboarding Funnel (10+ emails) | Drop | Mar 21 | ⬜ | EXPANDED from 3 emails |
| Static Landing Page | Dropper-Code | Mar 22 | ⬜ | Confirmed, trim existing |
