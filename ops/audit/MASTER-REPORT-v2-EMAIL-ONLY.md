# 📊 REVISED MASTER REPORT — Email-Only Pivot

**This report supersedes the original Pre-Launch Master Report.**  
**Date:** 2026-03-16  
**Status:** 🟡 REVISED for Email-Only Launch (March 24)  
**New Source of Truth:** Post-pivot priorities and deliverables

---

## 1. EXECUTIVE SUMMARY

### Strategic Pivot: Email-Only Product

Joey approved the email-only pivot. DropAnywhere will launch March 24 as an **email-only experience** — no dashboard, no login, no app. Users sign up on a waitlist, get admitted via email, and receive their Intelligence Map as a gorgeous digest email each morning.

**The 3 Launch Deliverables:**
1. **Intelligence Map Digest Email Template** — The entire product experience
2. **3-Email Admission Sequence** — Waitlist → Admitted → Welcome → First Digest  
3. **Static Landing Page** — Waitlist signup only (no dashboard)

### Revised Scorecard (55 Findings Re-Evaluated)

| Category | Original | Revised | Change |
|----------|----------|---------|--------|
| 🔴 Critical | 12 | **8** | -4 dashboard items |
| 🟡 Should Fix | 23 | **18** | -5 frontend issues |
| 🟢 OK | 20 | **20** | No change |
| **NEW Critical** | — | **3** | +3 email-only items |

### Critical Issues: Now IRRELEVANT (Dashboard Death)

These 4 critical findings from the original audit **no longer matter** for email-only launch:

| Original Critical | Why It's Now Irrelevant |
|-------------------|------------------------|
| Vault rendering bugs | No dashboard = no vault view |
| Intelligence Map tab crashes | Delivered as email, not tab |
| Auth flow / login issues | No user login required |
| Frontend mobile responsiveness | Landing page only (single breakpoint) |

### Critical Issues: NEWLY CRITICAL (Email-Only World)

These **3 new items** become launch blockers:

| New Critical | Why It Matters Now |
|--------------|-------------------|
| **Intelligence Map email template quality** | The ENTIRE product — must be gorgeous |
| **Email deliverability / spam score** | If emails don't land, product doesn't exist |
| **3-email admission sequence** | Undefined flow is Day 1 experience gap |

### Updated Verdict

| Metric | Original | Revised |
|--------|----------|---------|
| **Launch Confidence** | 🟡 65% (dashboard chaos) | 🟢 85% (focused scope) |
| **Launch Date** | At risk | Achievable (March 24) |
| **Required Effort** | 80+ hours | ~20 hours |
| **Burn Impact** | ~$267/mo | ~$145/mo (-45%) |

**Verdict: GO — with focused scope.** The email-only pivot transforms an at-risk launch into an achievable one.

---

## 2. REVISED CRITICAL ISSUES

### 🔴 CRITICAL — Fix Before March 24

#### C1. Poe Balance Near Zero ⬅️ STILL CRITICAL
| | |
|---|---|
| **What's Wrong** | 37,892 points remaining; 37,783 burned in last 6h (~6,300/hour) |
| **Impact** | Bots will error out; users get broken experience |
| **Fix** | Top up Poe points immediately; set up low-balance alerts |
| **Owner** | Joey |
| **Priority** | P0 — Hours remaining |

#### C2. Intelligence Map Email Template ⬅️ NEW CRITICAL
| | |
|---|---|
| **What's Wrong** | No production-ready digest template exists; Brooke theme needs email adaptation |
| **Impact** | The ENTIRE product experience — if this isn't gorgeous, the product fails |
| **Fix** | Build HTML email template: Brooke theme (cream/sage/copper), grouped threads, connections, actionable layout |
| **Owner** | Drop (build) + Joey (approve design) |
| **Priority** | P0 — Must ship March 24 |
| **Requirements** | • Responsive for email clients<br>• Intelligence Map visual hierarchy<br>• "Drop it. Forget it." brand voice<br>• Parrot footer 🦜<br>• Unsubscribe compliant |

#### C3. 3-Email Admission Sequence ⬅️ NEW CRITICAL
| | |
|---|---|
| **What's Wrong** | No documented flow for waitlist → admitted → first digest |
| **Impact** | Day 1 user experience is undefined; admitted users get confusion |
| **Fix** | Build and test 3-email sequence (see Section 6 for spec) |
| **Owner** | Drop (write) + Joey (personal touch) |
| **Priority** | P0 — Core user journey |

#### C4. Email Deliverability Setup ⬅️ NEW CRITICAL
| | |
|---|---|
| **What's Wrong** | No dedicated IP warming; no spam score testing; Resend at free tier limit |
| **Impact** | Emails land in spam = product doesn't exist |
| **Fix** | • Dedicated IP with Resend<br>• Spam score testing (Mail-Tester)<br>• DKIM/SPF verified<br>• Upgrade to paid tier if volume >3K/mo |
| **Owner** | Drop |
| **Priority** | P0 — Existential for email-only |

#### C5. Dropper-Code Safety Issues ⬅️ STILL CRITICAL
| | |
|---|---|
| **What's Wrong** | • `merge_pr()` still exists (auto-merge removed but callable)<br>• `system_pulse` reports "Auto-merge: active" (stale copy)<br>• `--dangerously-skip-permissions` on Claude CLI<br>• `CLAUDE_MAX_BUDGET` read but never passed to CLI |
| **Impact** | Agent could auto-merge; unlimited Claude spend; file access risks |
| **Fix** | • Delete `merge_pr()` from git_ops.py<br>• Fix system_pulse copy<br>• Add cost controls or timeout kills |
| **Owner** | Dropper-Code (via approved task) |
| **Priority** | P0 — Safety |

#### C6. Hub `OPENCLAW_HOOK_URL` ⬅️ STILL CRITICAL
| | |
|---|---|
| **What's Wrong** | Default is empty string; if not set on Railway, ALL alert forwarding fails |
| **Impact** | No alerts reach Joey; silent failures |
| **Fix** | Set `OPENCLAW_HOOK_URL=https://openclaw-gateway-production-54a0.up.railway.app/hooks/agent` on Railway |
| **Owner** | Joey |
| **Priority** | P0 — Observability |

#### C7. Hub Stripe Webhook Disabled ⬅️ STILL CRITICAL
| | |
|---|---|
| **What's Wrong** | Hub's Stripe webhook endpoint is disabled |
| **Impact** | If DropAnywhere Premium subscriptions need events, this is broken |
| **Fix** | Re-enable webhook if DA subscriptions active; otherwise document why disabled |
| **Owner** | Joey (decision) + Drop (execution) |
| **Priority** | P0 — If subscriptions launch |

#### C8. Railway API Token Expired ⬅️ STILL CRITICAL
| | |
|---|---|
| **What's Wrong** | Both `RAILWAY_API_TOKEN` and `RAILWAY_API_KEY` return "Not Authorized" |
| **Impact** | Cannot manage infrastructure programmatically |
| **Fix** | Regenerate tokens in Railway dashboard |
| **Owner** | Joey |
| **Priority** | P1 — Operational |

### 🟡 SHOULD FIX — Post-Launch

These are important but don't block email-only launch:

| Issue | Impact | Fix |
|-------|--------|-----|
| Landing page mobile polish | UX on mobile signups | Responsive pass after core template ships |
| Digest template dark mode | Accessibility | v1.1 enhancement |
| Reply-to-digest functionality | User engagement | Hub webhook already handles replies |
| Archive 18 specs + kill 9 | Clutter | Batch cleanup task |
| MEMORY.md metrics stale | Outdated user counts | Refresh after launch |
| Twilio SMS verification | Channel readiness | Not needed for email-only v1 |

---

## 3. REVISED SPEC TRIAGE

### Re-Triaged Through Email-Only Lens

| # | Spec | Original | **Revised** | Reason |
|---|------|----------|-------------|--------|
| 1 | AGENT-COMPANY-v3.md | ARCHIVE | **KILL** | 40-agent org irrelevant; 27 agents already running |
| 2 | ARI-Styling-Assistant | ARCHIVE | **KILL** | Side project, not DA launch |
| 3 | COMMS-GUIDE.md | KEEP | **KEEP** | Active communication standard |
| 4 | COMPANY-CONSTITUTION (specs/) | KILL | **KILL** | Stale duplicate |
| 5 | Cash-Burn-Tracker | ARCHIVE | **ARCHIVE** | Post-launch advisory kit |
| 6 | GUMROAD-GENESIS | ARCHIVE | **KILL** | Not launching on Gumroad |
| 7 | LAUNCH-CRITICAL-PATH | KEEP | **KEEP** | Active launch execution |
| 8 | LOOPSLAP-MASTER-PRD | KILL | **KILL** | Superseded |
| 9 | PERMISSIONS.md | KEEP | **KEEP** | Security framework |
| 10 | PLATFORM-DEPARTMENT | ARCHIVE | **KILL** | Platform dept irrelevant in email-only |
| 11 | PRD-Action-Plan | KEEP | **KEEP** | Master PRD — needs Section 3 rewrite |
| 12 | PRD-Desktop-Mobile-Split | ARCHIVE | **KILL** | Dashboard split irrelevant |
| 13 | RAILWAY-BOT-MANUAL | KEEP | **ARCHIVE** | RailwayBot idle; merge into Patrol |
| 14 | SNAPBACK-INTEGRATION | KEEP | **KEEP** | Core product — email IS snapback |
| 15 | SOFT-LAUNCH-LIST | KEEP | **KEEP** | 12 users across 3 tiers |
| 16 | SPEC-Adaptive-Weekly-Catch | ARCHIVE | **ARCHIVE** | Post-launch sophistication |
| 17 | SPEC-Admin-User-Lifecycle | ARCHIVE | **KILL** | Admin dashboard irrelevant |
| 18 | SPEC-DigestBot | KILL | **KILL** | Skeleton, never built |
| 19 | SPEC-Human-Insight-Snapshot | ARCHIVE | **ARCHIVE** | Onboarding survey — post-launch |
| 20 | SPEC-Joey-AI-Builder-Pack | ARCHIVE | **KILL** | B2B product — not email-only v1 |
| 21 | SPEC-MOMENTUM-TRACKER | KILL | **KILL** | Skeleton agent |
| 22 | SPEC-Message-Bottle | ARCHIVE | **ARCHIVE** | Interesting architecture — future |
| 23 | SPEC-Mitch-Advisory | ARCHIVE | **ARCHIVE** | Client deliverable — post-launch |
| 24 | SPEC-NARRATIVE-ENGINE | KILL | **KILL** | Skeleton agent |
| 25 | SPEC-PATTERN-WEAVER | KILL | **KILL** | Skeleton agent |
| 26 | SPEC-Snapback-Email-Sequence | KEEP | **KEEP** | Core — 7-day sequence |
| 27 | SPEC-Transurfing-Snapback | ARCHIVE | **ARCHIVE** | Personal viz — not product |
| 28 | SPEC-User-Scenario-Matrix | KEEP | **KEEP** | Launch reference — user journeys |
| 29 | SPEC-VAULT-Archaeologist | ARCHIVE | **KILL** | Vault irrelevant for email-only |
| 30 | SPEC-Weekly-Catch-Progressive | ARCHIVE | **ARCHIVE** | Advanced personalization — future |
| 31 | agent-board.md (specs/) | KILL | **KILL** | Duplicate |
| 32 | content-transformation-system | ARCHIVE | **ARCHIVE** | Historical reference |
| 33 | digest-stall-strategy.md | KILL | **KILL** | Contradicts DIGEST-POLICY |
| 34 | goldmine-index.md | INTERNAL-OPS | **KEEP** | Content mining reference |
| 35 | poe-funnel-paste-ready | ARCHIVE | **ARCHIVE** | Poe CTA copy — good but not blocking |
| 36 | snapback-offer-2026-03-11 | KEEP | **KEEP** | Core offer copy |
| 37 | target-slide-rancho-mirage | ARCHIVE | **ARCHIVE** | Personal viz |
| 38 | transurfing-product-vision | ARCHIVE | **ARCHIVE** | Vision doc |
| 39 | weekly-catch-STYLE-GUIDE | KEEP | **KEEP** | Template styling reference |

### Revised Summary

| Action | Original | Revised | Delta |
|--------|----------|---------|-------|
| **KEEP** | 12 | **13** | +1 (digest policy elevated) |
| **ARCHIVE** | 18 | **14** | -4 (killed instead) |
| **KILL** | 9 | **12** | +3 (dashboard specs killed) |
| **Total** | 39 | **39** | — |

### Key Changes

- **13 KEEP specs** — down from 39 to manageable core
- **Dashboard specs killed:** SPEC-Admin-User-Lifecycle, SPEC-VAULT-Archaeologist, PLATFORM-DEPARTMENT
- **Email specs elevated:** DIGEST-POLICY.md (was implied, now sacred)

---

## 4. REVISED ACTION PLAN (Mar 17-22)

### Day-by-Day Breakdown

#### **Monday Mar 17 — Foundation Day**

| Task | Owner | Output |
|------|-------|--------|
| Regenerate Railway API tokens | Joey | ✅ Infrastructure management restored |
| Top up Poe points | Joey | ✅ 100K+ points secured |
| Set `OPENCLAW_HOOK_URL` on Hub | Joey | ✅ Alert forwarding works |
| Begin Intelligence Map email template | Drop | 🔄 HTML template skeleton (Brooke theme) |
| Write admission sequence copy | Drop | 🔄 Draft: Email 1 (Welcome) |
| Freeze dropanywhere-app dashboard work | Joey | ✅ Frontend repo frozen |

#### **Tuesday Mar 18 — Template Build Day**

| Task | Owner | Output |
|------|-------|--------|
| Complete digest email template v1 | Drop | ✅ Full HTML/CSS template |
| Build landing page skeleton | Drop | ✅ Static HTML + waitlist form |
| Write Email 2 (First Drop Instructions) | Drop | ✅ Copy ready |
| Set up Resend dedicated IP | Drop | ✅ Deliverability foundation |
| Test email rendering (Litmus/Email on Acid) | Drop | 🔄 Cross-client screenshots |
| Dropper-Code safety fixes | Dropper-Code | ✅ PR: Delete merge_pr(), fix system_pulse |

#### **Wednesday Mar 19 — Integration Day**

| Task | Owner | Output |
|------|-------|--------|
| Wire Hub → digest template | Dropper-Code | ✅ Template rendered with live data |
| Build admission flow in Hub | Dropper-Code | ✅ Waitlist → Admitted webhook |
| Write Email 3 (First Digest Preview) | Drop | ✅ Copy ready |
| Landing page polish | Drop | ✅ Brooke theme styling |
| End-to-end test: Signup → Admit → Email 1 | Joey + Drop | ✅ Flow verified |

#### **Thursday Mar 20 — Test Day**

| Task | Owner | Output |
|------|-------|--------|
| Spam score testing (Mail-Tester) | Drop | ✅ 8/10+ score achieved |
| Test digest with Joey's live drops | Joey | ✅ Real data looks gorgeous |
| Soft launch list outreach | Joey | Personal messages to Tier 1 |
| Landing page final review | Joey + Drop | ✅ Approved for deploy |
| Stress test: 100 test digests | Drop | ✅ No Resend rate limits hit |

#### **Friday Mar 21 — Buffer Day**

| Task | Owner | Output |
|------|-------|--------|
| Fix any rendering issues | Drop | ✅ All email clients clean |
| Final copy polish | Joey | ✅ Brand voice perfect |
| Deploy landing page to drop-anywhere.com | Drop | ✅ Live with waitlist |
| Document rollback plan | Drop | ✅ Emergency procedures |
| Team dry-run: Admit test user | Joey + Drop | ✅ Smooth experience |

#### **Saturday Mar 22 — Lock Day**

| Task | Owner | Output |
|------|-------|--------|
| **CODE FREEZE** | All | ✅ No more changes |
| Final admission flow test | Joey | ✅ 3-email sequence perfect |
| Monitor Poe balance | Drop | ✅ >50K points maintained |
| Prepare launch checklist | Drop | ✅ Go/no-go criteria |
| Rest | Joey | ✅ Fresh for Monday |

#### **Sunday Mar 23 — Rest Day**

No work. Joey rests. Drop monitors.

#### **Monday Mar 24 — LAUNCH DAY**

| Time (CDT) | Activity | Owner |
|------------|----------|-------|
| 08:00 | Final systems check | Drop |
| 09:00 | Admit Tier 1 (family) | Joey |
| 10:00 | Monitor first digests | Drop |
| 12:00 | Admit Tier 2 (friends) if Tier 1 clean | Joey |
| 14:00 | Monitor, adjust, observe | Both |
| 17:00 | Admit Tier 3 (power users) if stable | Joey |
| EOD | Launch retrospective | Both |

---

## 5. WHAT GETS CUT

### Frontend/Dashboard Work No Longer Needed

| Feature | Original Est. | Status |
|---------|--------------|--------|
| Vault view (search, browse, filter) | 20h | ❌ CUT — preserve in `phase-2/dashboard` branch |
| Intelligence Map tab | 16h | ❌ CUT — now in email |
| Stream view | 12h | ❌ CUT — email replaces stream |
| Settings page | 10h | ❌ CUT — managed via email replies |
| Auth flows (login, signup, password reset) | 12h | ❌ CUT — waitlist only |
| Mobile app shell / PWA | 15h | ❌ CUT — Phase 2 |
| Onboarding wizard | 8h | ❌ CUT — replaced by 3-email sequence |
| Theme customization UI | 6h | ❌ CUT — Brooke theme fixed |
| Dashboard navigation | 4h | ❌ CUT — single landing page |
| **TOTAL SAVED** | **~103 hours** | **~$8,000+ dev cost** |

### Agents to Pause/Repurpose

| Agent | Current Role | New Role |
|-------|-------------|----------|
| FrontEndBot | Dashboard development | **Email Template Engineer** — perfect digest HTML/CSS |
| RailwayBot | Infrastructure monitoring | **PAUSED** — merge into Kimi Patrol |
| ContentPitchBot | Content pitching | **PAUSED** — activate post-launch |
| VisualGoalBot | Image generation features | **PAUSED** — dashboard feature irrelevant |
| LanguageFrameworkBot | Language processing UI | **PAUSED** — backend only for email |

### Specs to Kill Immediately

See Section 3 for full list. Priority kills:
1. PLATFORM-DEPARTMENT.md (entire department proposal)
2. SPEC-Admin-User-Lifecycle-Dashboard.md
3. SPEC-VAULT-Archaeologist.md
4. PRD-Desktop-Mobile-Split-2026-03-10.md
5. All LOOPSLAP references (old entity name)

---

## 6. WHAT MUST SHIP

### 6.1 Intelligence Map Digest Email Template

**Purpose:** The entire product experience. Must make users excited to open email.

**Design Requirements:**
- **Theme:** Brooke (cream `#FAF9F6`, sage `#87A878`, copper `#B87D5E`)
- **Typography:** Newsreader for headings, system-ui for body
- **Layout:**
  - Header: Logo + date + "Your Second Brain Has No Inbox"
  - Hero: Today's drop count + theme summary
  - Intelligence Map: Visual thread grouping with connection lines
  - Action Items: Checklist format for to-do items
  - Connections: "This connects to..." cross-references
  - Quote/Insight: Daily distilled wisdom
  - Footer: Parrot 🦜, reply prompt, unsubscribe

**Technical Requirements:**
- Responsive for: Apple Mail, Gmail, Outlook, iOS Mail, Android
- Inline CSS (no `<style>` blocks for Gmail)
- Max width: 600px
- Dark mode support (prefers-color-scheme)
- Accessibility: Alt text, semantic HTML, 16px+ font sizes

**Content Requirements:**
- Pull from: user's drops (last 24h), themes, connections
- Group by: thread/intent (not chronological)
- Highlight: action items, insights, patterns
- Tone: "Drop it. Forget it. Wake up lighter."

**Owner:** Drop (template) + Dropper-Code (data wiring)  
**Deadline:** Mar 18 (v1), Mar 20 (polished)  
**Review:** Joey (Mar 19-20)

---

### 6.2 3-Email Admission Sequence

**Flow:** Waitlist signup → Email 1 (Welcome) → Email 2 (First Drop) → Joey admits → Email 3 (First Digest)

#### Email 1: Welcome to the Waitlist
**Trigger:** Immediately after waitlist signup  
**From:** DropAnywhere <hello@drop-anywhere.com>  
**Subject:** "You're on the list — DropAnywhere is coming"

```
Hi [First Name],

Welcome to DropAnywhere.

You're on the waitlist for a new kind of second brain — one that 
works through email. No apps. No dashboards. Just clarity in your 
inbox every morning.

Here's what happens next:
1. We review your request (usually within 48 hours)
2. When admitted, you'll get your "drop address" — just reply to 
   any email or send one to drops@drop-anywhere.com
3. Your first Intelligence Map arrives the next morning

The world is loud. Your thoughts deserve a quiet place.

Drop it. Forget it. Wake up lighter.

— Drop 🦜

P.S. Hit reply if you have questions. I read every one.
```

#### Email 2: Your First Drop (Instructions)
**Trigger:** After admission (Joey clicks "Admit" in Hub)  
**From:** DropAnywhere <hello@drop-anywhere.com>  
**Subject:** "You're in — here's your drop address"

```
[First Name], you're admitted.

Your personal drop address:
📧 drops+{user_id}@drop-anywhere.com

Save this address. Send anything there:
- Ideas that hit you in the shower
- Meeting notes you might need later  
- Links you want to remember
- Voice memos (attachments work!)

Just hit send. We'll handle the rest.

Your first Intelligence Map arrives tomorrow morning. 
It'll show you what we found in your drops — themes, connections, 
and anything that needs your attention.

Try it now. Reply to this email with a thought, idea, or question.

— Drop 🦜
```

#### Email 3: First Digest Preview
**Trigger:** Morning after first drop received  
**From:** DropAnywhere <hello@drop-anywhere.com>  
**Subject:** "[First Name]'s Intelligence Map — March 21, 2026"

[This is the Intelligence Map digest template from 6.1]

**Owner:** Drop (copywriting) + Dropper-Code (automation)  
**Deadline:** Mar 19 (all 3 emails), Mar 20 (tested end-to-end)  
**Review:** Joey (Mar 19 for tone/brand)

---

### 6.3 Landing Page

**Purpose:** Convert visitors to waitlist. Single job: capture email.

**Sections:**
1. **Hero:** "Your Second Brain Has No Inbox" + subhead + email input
2. **Social Proof:** "Join 100+ early access users" (or actual number)
3. **How It Works:** 3-step visual (Drop → Process → Digest)
4. **Preview:** Screenshot of digest email (the product)
5. **FAQ:** 3-4 collapsible questions
6. **Final CTA:** Email input + "Join the waitlist"
7. **Footer:** Brand, social links, privacy

**Technical:**
- Static HTML/CSS (no framework needed)
- Hosted: drop-anywhere.com via Railway or Vercel
- Waitlist: POST to Hub `/api/waitlist` or Resend list API
- Brooke theme throughout

**Owner:** Drop  
**Deadline:** Mar 18 (skeleton), Mar 19 (styled), Mar 20 (polished)  
**Review:** Joey (Mar 20)

---

### 6.4 Hub: Email Webhook → OpenClaw Hook

**Purpose:** Instant processing of Joey's emails for CEO-level responsiveness.

**Flow:**
```
Inbound email to hello@drop-anywhere.com
    ↓
Resend receives → POST to Hub /api/webhook/email
    ↓
Hub validates Svix signature, extracts content
    ↓
If sender = joeyhamer@gmail.com:
    → async POST to OpenClaw /hooks/agent
    → Drop processes immediately (via WhatsApp)
    ↓
All emails: ingest to vault as drops
```

**Status:** PR #193 merged 2026-03-16 — ✅ IMPLEMENTED  
**Verification:** Test with Joey email, confirm WhatsApp alert < 30s  
**Owner:** Drop  
**Deadline:** Mar 17 (verify working)

---

## 7. MONTHLY COST IMPACT

### What We Can Cut (Email-Only Savings)

| Service | Original | Email-Only | Monthly Savings |
|---------|----------|------------|-----------------|
| **Railway Frontend Project** | ~$15/mo | **$0** (static hosting) | **$15** |
| DropAnywhere-CRON service | ~$5/mo | **$0** (confirmed dead) | **$5** |
| Frontend build minutes | ~$5/mo | **$0** | **$5** |
| Database (unused features) | ~$10/mo | **$5** (trimmed) | **$5** |
| **Subtotal Infrastructure** | **~$35/mo** | **~$5/mo** | **$30** |

### What Stays The Same

| Service | Cost | Why Still Needed |
|---------|------|-----------------|
| Railway Hub (backend) | ~$20/mo | Core ingestion + digest generation |
| Railway OpenClaw | ~$15/mo | Gateway service |
| Railway Dropper-Code | ~$10/mo | Autonomous code agent |
| Resend Email | ~$0-20/mo | Free tier + paid if >3K emails |
| Poe Points | ~$20-50/mo | Bot usage |
| OpenRouter | ~$100/mo | AI model access |
| Anthropic (OpenClaw) | ~$20-50/mo | Claude usage |
| GitHub | $0 | Free tier |
| Cloudflare | $0 | Free tier |
| Stripe Fees | ~$2/mo | Payment processing |

### Revised Monthly Burn

| Scenario | Monthly Cost |
|----------|--------------|
| **Original (full dashboard)** | ~$267/mo |
| **Email-Only (conservative)** | ~$145/mo |
| **Email-Only (lean)** | ~$125/mo |
| **Savings** | **~$120-140/mo (-45%)** |

### Revenue vs Burn

| Metric | Value |
|--------|-------|
| Current MRR (Stripe) | ~$14/mo (2 active subs) |
| Past due (recoverable?) | ~$7/mo |
| **Net Burn (email-only)** | **~$130/mo** |
| Runway extension | +45% longer |

### Immediate Actions

1. **Verify dropanywhere-cron service is deleted** from Railway (not just disabled)
2. **Scale down frontend project** to static hosting only
3. **Monitor Resend volume** — upgrade to paid if approaching 3K/mo limit
4. **Set OpenRouter spending limit** — prevent surprise $450/mo spikes

---

## APPENDIX A: Launch Checklist (Mar 24)

### Go/No-Go Criteria

| Criteria | Threshold | Status |
|----------|-----------|--------|
| Poe balance | >50K points | ⬜ |
| Digest template | Joey approved | ⬜ |
| Admission flow | End-to-end tested | ⬜ |
| Landing page | Live, waitlist working | ⬜ |
| Email deliverability | 8/10+ spam score | ⬜ |
| Hub alerts | Forwarding to WhatsApp | ⬜ |
| Soft launch list | Joey reviewed | ⬜ |
| Rollback plan | Documented | ⬜ |

### Soft Launch Tiers

| Tier | Users | When | Criteria |
|------|-------|------|----------|
| Tier 1 | Family (Lisa, Danny, Bob) | Mar 24 09:00 | Immediate personal support |
| Tier 2 | Friends (5-6) | Mar 24 12:00 | If Tier 1 digests clean |
| Tier 3 | Power users (5-6) | Mar 24 17:00 | If Tier 2 stable |

---

## APPENDIX B: Decision Log

| Date | Decision | Made By | Impact |
|------|----------|---------|--------|
| 2026-03-16 | Email-only pivot | Joey | Simplified launch, -45% burn |
| 2026-03-16 | 3 deliverables defined | Strategic poll | Template + sequence + landing page |
| 2026-03-16 | Dashboard → Phase 2 | Joey | 103h frontend work cut |
| 2026-03-16 | FrontEndBot repurposed | Meta recommendation | Email template engineer |

---

*This report supersedes all prior pre-launch audit documents. For questions, reply to this email — Drop reads every reply.* 🦜

**Next Update:** Mar 17 EOD with Day 1 progress report.
