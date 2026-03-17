# Agent Permissions & Security Framework

**Principle: Least privilege. Every agent gets only what it needs to do its job.**

---

## Data Classification

| Level | Label | Examples | Who Can Access |
|-------|-------|---------|----------------|
| 🔴 **RESTRICTED** | Joey's personal data | MEMORY.md, USER.md, SOUL.md, drops content, phone numbers, emails, financial data, Transurfing slide | Claw, Chief of Staff ONLY |
| 🟠 **CONFIDENTIAL** | Business secrets | API keys, tokens, .env files, Stripe data, user PII, payment records, Hub credentials | Claw, Sentry, StripeBot, DC Manager (read-only for keys they USE) |
| 🟡 **INTERNAL** | Operational data | Agent board, escalations, PRD, specs, metrics, GitHub repos, user health scores | All agents (read), Dept-specific (write) |
| 🟢 **PUBLIC** | Publishable content | Social posts, blog drafts, SEO content, landing page copy, public docs | All agents |

---

## Entry Points (Attack Surface)

### Inbound (data coming IN)
| Channel | Gate | Guardian |
|---------|------|----------|
| **Email** (Resend webhook) | Hub validates sender → drops pipeline | Hub + Sentry monitors |
| **SMS** (Twilio) | Hub validates → drops pipeline | Hub + Sentry |
| **Poe conversations** | Orchestrator routes → Hub logs | PoeBot + Sentry |
| **GitHub webhooks** | Signed webhooks → Hub | DC Manager + Sentry |
| **Stripe webhooks** | Signature verification → Hub | StripeBot + Sentry |
| **Joey direct** (WhatsApp/webchat) | Authenticated by OpenClaw | Claw (me) |
| **Agent board** (internal) | Any agent can write | Sentry audits, Opus quality gates |

### Outbound (data going OUT)
| Channel | Gate | Who Can Use |
|---------|------|-------------|
| **WhatsApp to Joey** | Only Claw sends | Claw ONLY |
| **GitHub push** | joey-backup only, GITHUB_TOKEN | Archivist, DC Manager, DocBot |
| **Hub API writes** | HUB_API_KEY, task creation | DC Manager, Opus (task creation only) |
| **Email send** (Resend) | RESEND_API_KEY | ❌ NO AGENT (only Claw, with Joey approval) |
| **Public content** | Must pass FounderVoice review | ContentBot → FounderVoice → Joey approval |
| **Stripe actions** | STRIPE_SECRET_KEY | ❌ NO AGENT (read-only via Hub dashboard) |
| **Dropper-Code triggers** | POST to dropper-code URL | DC Manager ONLY |

---

## Agent Permission Matrix

### 🔴 RESTRICTED ACCESS (Claw + Chief of Staff only)
These files/APIs are OFF-LIMITS to all other agents:
- MEMORY.md (personal context, private decisions)
- USER.md (Joey's personal info, slide, relationships)
- SOUL.md (identity — no agent should modify this)
- bank/entities/*.md (personal relationships)
- bank/opinions.md (private preferences)
- memory/user-profiles.md (user PII)
- Hub drops content (Joey's raw thoughts)
- openclaw.json (gateway config — NEVER touch)

### 🟠 CONFIDENTIAL ACCESS (role-specific)
| Resource | Agents Allowed | Access Level |
|----------|---------------|-------------|
| .env.local (tokens) | DC Manager, Archivist | Read (for API calls) |
| GITHUB_TOKEN | Archivist, DC Manager, DocBot, Kimi Patrol | Read (for API calls) |
| HUB_API_KEY | Kimi Patrol, DC Manager, UserHealthBot, StripeBot, PoeBot, Opus | Read (for API calls) |
| Stripe data | StripeBot | Read-only (via Hub dashboard) |
| User PII | UserHealthBot, OnboardBot | Read-only, never log raw PII |
| Hub /api/admin/* | UserHealthBot, OnboardBot, Kimi Patrol | Read-only |

### 🟡 INTERNAL ACCESS (all agents, dept-specific write)
| Resource | Read | Write |
|----------|------|-------|
| ops/agent-board.md | All | All (own entries only) |
| ops/escalations.md | All | All |
| ops/COMPANY-CONSTITUTION.md | All | Governance ONLY |
| ops/COMMS-GUIDE.md | All | Governance ONLY |
| ops/goldmine-index.md | All | All (append Discovered Gold) |
| ops/agent-scorecard.md | All | Meta ONLY |
| docs/PRD.md | All | DocBot, Opus |
| docs/reference/*.md | All | Relevant dept |
| docs/*.md specs | All | SpecBot, DocBot, Opus |
| social/*.md | All | ContentBot, SocialBot, FounderVoice |
| memory/YYYY-MM-DD.md daily logs | All | All (append own entries) |

### 🟢 PUBLIC ACCESS
| Resource | Read | Write |
|----------|------|-------|
| docs/reference/wire/*.md | All | Wire, Researcher |
| social/blog/*.md | All | ContentBot |
| social/pitches.md | All | ContentPitchBot |

---

## Security Rules

### The 7 Commandments

1. **NO agent sends external messages without Claw approval.**
   No emails, no WhatsApp, no public posts. Everything goes through Claw → Joey.

2. **NO agent modifies SOUL.md, USER.md, or openclaw.json.**
   These are sacred. Sentry flags any modification attempt.

3. **NO agent exposes secrets in board posts, logs, or commits.**
   Sentry scans every commit and board entry for leaked keys/tokens/PII.

4. **NO agent creates customer-facing content without FounderVoice review.**
   Content pipeline: Create → FounderVoice tone check → Joey approval → Publish.

5. **NO agent deploys to production.**
   Dropper-Code creates PRs. Humans merge. RailwayBot monitors but doesn't deploy.

6. **NO agent accesses data above its classification level.**
   A SEOBot has no business reading MEMORY.md. Sentry audits access patterns.

7. **ALL external API calls are logged.**
   Every curl to Hub, GitHub, Dropper-Code gets logged in the daily log with agent name.

### PII Handling
- User names: OK to use in internal logs
- User emails: NEVER in board posts or commits
- Phone numbers: NEVER anywhere except USER.md
- Payment data: StripeBot only, never raw card numbers (Stripe handles that)
- Drop content: RESTRICTED — only Claw, Researcher (for mining), and ContentPitchBot (for pitches, anonymized)

### Content Publication Flow
```
Idea → ContentPitchBot → ContentBot creates draft
  → FounderVoiceBot tone check (❌ or ✅)
  → Ready Queue (3+ ✅ from agents)
  → Claw reviews
  → Joey approves
  → THEN it goes public
```
**Nothing goes public without Joey's explicit approval.**

### Incident Response
```
Sentry detects violation
  → Posts [SECURITY] to board
  → Writes to ops/escalations.md
  → If active threat: "ESCALATE TO CLAW: SECURITY — [details]"
  → Claw assesses severity
  → If data breach risk: "ALERT JOEY: SECURITY — [details]"
  → Claw takes corrective action (may disable agent)
```

---

## Future: Seeker Integration

When external "seekers" (users, partners, external agents) need access:

### Seeker Gates
| Gate | Purpose | Access Level |
|------|---------|-------------|
| **Email gate** | Inbound drops via email | 🟡 Internal (their own data only) |
| **API gate** | External integrations | 🟡 Internal (scoped by API key) |
| **Poe gate** | Bot conversations | 🟢 Public (persona responses only) |
| **Web gate** | drop-anywhere.com | 🟢 Public (their own dashboard) |

### Seeker Rules
- Seekers NEVER see other users' data
- Seekers NEVER see internal ops (board, escalations, metrics)
- Seekers NEVER trigger internal agents directly
- All seeker data flows through Hub API (the single gateway)
- Hub enforces row-level security (user_id scoping)

---

## Sentry Enforcement

Sentry checks these EVERY cycle:
- [ ] No secrets in git diff
- [ ] No secrets in agent-board.md
- [ ] No modifications to SOUL.md, USER.md, openclaw.json
- [ ] No PII in public-facing files
- [ ] Content publication flow respected
- [ ] No unauthorized external API calls
- [ ] All agents operating within their permission level

---

*This framework evolves as the org grows. Governance maintains it. Sentry enforces it.*

