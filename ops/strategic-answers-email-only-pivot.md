# Strategic Answers: Email-Only Pivot
**Date:** 2026-03-16  
**Context:** DropAnywhere's foundational product decisions for email-only launch (March 24)  
**Audience:** Joey decision-making  

---

## 1. TRIAGE SYSTEM

### The Practical Answer (What We Do)

DropAnywhere's email triage system is a **smart routing layer** that sits between Resend (our email provider) and user inboxes. When an email arrives, it follows this path:

```
Inbound Email → Resend → Hub Webhook → Triage Router → Processing Queue
```

**How Routing Works:**

| Email Type | Detection Rule | Routing Decision |
|------------|---------------|------------------|
| **User Drop** | `to` matches `drops+*@drop-anywhere.com` | Ingest to vault → analyze → include in next digest |
| **Reply to Digest** | `in-reply-to` header matches digest ID | Thread continuation → add to existing intelligence map group |
| **Joey's Direct Email** | `from: joeyhamer@gmail.com` | **PRIORITY LANE** → instant WhatsApp alert + CEO triage |
| **Reply to Admission** | `to: hello@drop-anywhere.com` + thread match | Human review queue → Joey or auto-response |
| **Unknown/Bounce** | No match above | Spam folder analysis → quarantine if suspicious |

**The Admission Flow (Critical Journey):**

```
Waitlist Signup (landing page)
    ↓
Email 1: Welcome (immediate)
    ↓
Joey admits via Hub admin (manual trigger)
    ↓
Email 2: You're In + Drop Address (immediate)
    ↓
[User sends first drop]
    ↓
Email 3: First Intelligence Map (next morning ~7am)
```

**Email Cadence Rules:**

| User State | Email Frequency | Timing |
|------------|-----------------|--------|
| Waitlisted | 1 email only | Immediate confirmation |
| Admitted, pre-first-drop | 1 email | Immediate after admission |
| Active (has drops) | Daily (max 1) | 7:00 AM user's timezone (default CDT) |
| Dormant (no drops 7+ days) | 1 email | Weekly "We miss you" nudge with summary |
| Unsubscribed | 0 emails | Removed from all lists (compliance) |

**Feedback Incorporation:**
- **Explicit:** Reply to any email → parsed for commands (`pause`, `more often`, `less frequent`, `help`)
- **Implicit:** Email opens, link clicks (tracked via Resend) → digest timing optimization
- **Direct:** Users can request features/changes via reply → drops into Joey's priority lane for manual review

### The Strategic Thinking (Why)

**Why This Routing Architecture:**

1. **Email-First, Not Email-Only Forever** — This system sets up the data pipeline so when dashboard launches, all intelligence is already organized
2. **Joey's Context is Irreplaceable** — The "Joey priority lane" isn't just convenience; it's product research. Every email Joey sends teaches the system what actually matters
3. **Frictionless > Feature-Rich** — Users don't configure cadence; we learn it. Default daily, auto-adjust based on engagement. Reduces decision fatigue
4. **Admission Gate = Quality Control** — Manual admission lets Joey curate early users, gathering qualitative feedback before scaling

**Cadence Philosophy:**
- **Daily default:** The "Intelligence Map" is designed to be *glanceable* — if there's nothing new, the email says so (no noise)
- **Morning timing:** Catches users in "review mode" not "reactive mode" — different psychology than midday emails
- **No batching options:** Intentional constraint. The product teaches users to trust the daily rhythm (`Drop it. Forget it.`)

### The Implementation Path (How)

**Phase 1: Launch-Ready (Mar 24)**

```python
# Hub webhook handler (pseudo-structure)
def handle_inbound_email(email_payload):
    # 1. Identify email type
    email_type = classify_email(email_payload)
    
    # 2. Route accordingly
    if email_type == 'USER_DROP':
        user = extract_user_from_address(email_payload.to)
        drop = ingest_drop(email_payload, user)
        queue_for_digest(drop, user)
        
    elif email_type == 'JOEY_DIRECT':
        ingest_drop(email_payload, user=joey)  # Archive it
        send_whatsapp_alert(f"Email from Joey: {email_payload.subject}")
        
    elif email_type == 'DIGEST_REPLY':
        thread = find_thread(email_payload.in_reply_to)
        append_to_thread(thread, email_payload)
        
    elif email_type == 'REPLY_TO_ADMISSION':
        queue_for_human_review(email_payload)
```

**Key Components:**
1. **Resend Inbound Webhook** (`/api/webhook/email`) — already implemented per MASTER-REPORT-v2
2. **Email Classifier** — simple rule-based for launch (regex patterns, header analysis)
3. **Priority Queue** — Joey's emails bypass normal processing
4. **Digest Scheduler** — runs daily at 7am per `DIGEST-POLICY.md` (currently disabled via `DISABLE_CRONS=1`)

**Phase 2: Smart Cadence (Post-Launch)**

- ML-based open-rate prediction
- Dynamic timing (e.g., this user opens emails at 8:30am, adjust send time)
- Engagement-based frequency (high engagement → option for twice-daily; low → weekly digest)

### Decisions Joey Needs to Make

**Immediate (Before Mar 24):**
1. **Timezone handling** — Default to CDT for all users initially, or ask during waitlist signup?
2. **Joey's WhatsApp urgency threshold** — All emails from you get WhatsApp alerts, or only certain subjects/keywords?
3. **Dormant user definition** — No drops for 7 days triggers "we miss you" email? Or 14 days?

**Post-Launch:**
1. **Auto-admission threshold** — At what volume do we switch from manual admission to automatic?
2. **Cadence customization** — Do we ever let users choose daily/weekly, or do we maintain the "one way" philosophy?

---

## 2. CUSTOM STRIPE PAYMENT

### The Practical Answer (What We Do)

DropAnywhere's payment flow is designed for **zero-friction conversion** with a "freemium → paid" natural progression:

**The Trial Philosophy:**
- **No credit card required** for waitlist admission
- **Full features for 14 days** after first digest
- **Soft paywall** on day 14 — digest still arrives but with "Upgrade" CTA for "priority scheduling" and "unlimited drops"

**What We Allow (Billing Paths):**

| Path | User Journey | Stripe Integration |
|------|--------------|-------------------|
| **Free → Pro** | Waitlist → Admit → 14 days free → Upgrade prompt | Stripe Checkout session, one-click |
| **Gift/Referral** | Joey admits to "Founders" tier directly | Stripe subscription with 100% off coupon |
| **B2B Advisory** | Custom invoicing (outside Stripe) | Manual contract → Stripe subscription later |
| **Poe Bridge** | BHA users discover DA via bots | No direct Stripe linkage — separate conversion flow |

**Most Impactful Billing Path (The No-Brainer):**

```
User receives 3rd digest → Email subject: "Unlock priority timing & unlimited drops"
    ↓
Email body: "Your free week was a taste. Pro users get:
  • Digests at your preferred time (not default 7am)
  • Unlimited drops (free = 10/week)
  • Custom drop addresses (work@, personal@)
  • Priority support"
    ↓
Button: "Upgrade ($9/mo)" → Stripe Checkout (pre-filled email)
    ↓
One click → Card entry → Active subscription
```

**Friction Removers:**
1. **Pre-filled email** — from their drop address, no typing
2. **No plan selection** — Pro is the only paid tier (simpler than tiers)
3. **Monthly default** — Annual option shown but not pre-selected (lower commitment)
4. **Receipt to drop address** — payment confirmation = drop in their vault (trust signal)
5. **One-click downgrade** — downgrade link in every receipt email (removes fear)

**Stripe Setup:**

```javascript
// Stripe Checkout Session creation
const session = await stripe.checkout.sessions.create({
  customer_email: user.email,  // Pre-filled
  line_items: [{
    price: 'price_dropanywhere_pro_monthly', // $9/mo
    quantity: 1,
  }],
  mode: 'subscription',
  success_url: `${BASE_URL}/welcome-pro?session_id={CHECKOUT_SESSION_ID}`,
  cancel_url: `${BASE_URL}/digest-preview`,