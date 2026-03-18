# AGENT ROSTER — DropAnywhere Agent Company

**Last Updated**: 2026-03-18 00:47 UTC (GOVERNANCE REALITY CHECK)  
**Company Status**: ✅ OPERATIONAL — 40 enabled agents out of 50 total cron jobs (Mature ecosystem)

---

## Real-Time Operations (2-15min cycles)

| Agent | Cron ID | Cadence | Model | Department | Status | Notes |
|-------|---------|---------|-------|-------------|--------|-------|
| **AUTO-ACK BOT** | — | 2min | Kimi K2.5 | Email | ✅ ACTIVE | Immediate email acknowledgment |
| **DASHBOARD MESSENGER** | — | 2min | Sonnet 4 | Ops | ✅ ACTIVE | Dashboard inbox/outbox handling |
| **DECISIONBOT** | — | 10min | Kimi K2.5 | Email | ✅ ACTIVE | Processes Joey's email replies |
| **DEEP RESEARCHER** | 8bb0afbe | 10min | Sonnet 4 | Intelligence | ✅ ACTIVE | Competitive intel, market research |
| **OPUS STRATEGIST** | 3c97502c | 15min | Opus 4 | Meta | ✅ ACTIVE | Strategic oversight, quality gate |
| **SENTRY AI** | 8dad9141 | 15min | Sonnet 4 | Security | ✅ ACTIVE | Security scans, integrity checks |

## Medium Frequency Operations (20-40min cycles)

| Agent | Cron ID | Cadence | Model | Department | Status | Notes |
|-------|---------|---------|-------|-------------|--------|-------|
| **CHIEF OF STAFF** | 19e65c33 | 20min | Opus 4 | Executive | ⚠️ RUNNING | Gap finder, escalations (has errors) |
| **META** | dc28069f | 20min | Sonnet 4 | Meta | ✅ ACTIVE | Agent performance grading |
| **DOCBOT** | 1cf8f9ae | 40min | Kimi K2.5 | Product | 🔴 CRITICAL | PRD updates, documentation (6x timeout) |
| **USERHEALTHBOT** | b238fc7f | 40min | Kimi K2.5 | Customer Success | ✅ ACTIVE | User retention monitoring |
| **CONTENTBOT** | f35e88e1 | 20min | Sonnet 4 | Marketing | ✅ ACTIVE | Content creation pipeline |
| **ARCHIVIST** | e0a92bbb | 40min | Kimi K2.5 | Operations | ✅ ACTIVE | Backup to joey-backup GitHub |
| **UNIFIED OPS MONITOR** | — | 30min | Kimi K2.5 | Operations | ✅ ACTIVE | Consolidated monitoring (replaces 5 bots) |

## Department Specialists (30min-1hr cycles)

| Agent | Cron ID | Cadence | Model | Department | Status | Focus |
|-------|---------|---------|-------|-------------|--------|-------|
| **GOVERNANCE** | aac7b675 | 30min | Sonnet 4 | Meta | ✅ ACTIVE | Constitutional keeper (this session) |
| **FRONTENDBOT** | e0e87bdb | 1hr | Kimi K2.5 | Engineering | ✅ ACTIVE | dropanywhere-app monitoring |
| **BHABOT** | f1876ffc | 1hr | Kimi K2.5 | Engineering | ✅ ACTIVE | brutallyhonest-next monitoring |
| **SPECBOT** | e7c1962d | 1hr | Kimi K2.5 | Product | ✅ ACTIVE | Requirements engineering |
| **ONBOARDBOT** | 39971b02 | 1hr | Kimi K2.5 | Customer Success | ✅ ACTIVE | New user activation tracking |
| **SOCIALBOT** | — | 1hr | Kimi K2.5 | Marketing | ✅ ACTIVE | Social media strategy |
| **SEOBOT** | 09d8fe79 | 1hr | Kimi K2.5 | Marketing | ✅ ACTIVE | Search optimization |
| **FOUNDERVOICEBOT** | eb5df9b7 | 30min | Sonnet 4 | Communications | ✅ ACTIVE | Voice/tone guardian |
| **CONTENTPITCHBOT** | b36fc606 | 1hr | Kimi K2.5 | Intelligence | ✅ ACTIVE | Content strategy generation |
| **PATTERNBOT** | 08ec61b5 | 1hr | Kimi K2.5 | Intelligence | ✅ ACTIVE | Pattern recognition |
| **LEARNINGBOT** | 828ec8a4 | 1hr | Kimi K2.5 | Meta | ⚠️ DEGRADED | Lessons learned documentation (1 timeout) |
| **SKILLMINER** | 1b98e23c | 30min | Sonnet 4 | Meta | ✅ ACTIVE | Mines skills from sessions/GitHub |

## Email Workflow Agents

| Agent | Cron ID | Cadence | Model | Department | Status | Purpose |
|-------|---------|---------|-------|-------------|--------|---------|
| **AUTO-ACK BOT** | — | 2min | Kimi K2.5 | Email | ✅ ACTIVE | Immediate email acknowledgment |
| **DECISIONBOT** | — | 10min | Kimi K2.5 | Email | ✅ ACTIVE | Processes Joey's email replies |
| **FEEDBACKBOT** | — | 2hr | Kimi K2.5 | Email | ✅ ACTIVE | Routes creative feedback |
| **TASK APPROVAL EMAILER** | — | 2hr | Kimi K2.5 | Email | ✅ ACTIVE | Pending task notifications (dual instances) |
| **CREATIVE REVIEW EMAILER** | — | 4hr | Kimi K2.5 | Email | 🔴 CRITICAL | Content review workflow (3x timeout) |
| **CEO MORNING BRIEF** | — | Daily 8am CST | Kimi K2.5 | Email | ✅ ACTIVE | Comprehensive daily summary |

## Specialized Operations

| Agent | Cron ID | Cadence | Model | Department | Status | Focus |
|-------|---------|---------|-------|-------------|--------|-------|
| **LAUNCH COORDINATOR** | — | 2hr | Sonnet 4 | Product | ✅ ACTIVE | March 24 launch tracking (6 days remaining) |
| **SYNC AUDITOR** | — | 4hr | Kimi K2.5 | Operations | ✅ ACTIVE | Ensures no local data loss |
| **DC MANAGER** | b644d0fe | 30min | Kimi K2.5 | Engineering | ✅ ACTIVE | Dropper-Code oversight |

## Daily Scheduled Maintenance

| Job | Cron ID | Schedule | Model | Status | Purpose |
|-----|---------|----------|-------|--------|---------|
| **METRICS SNAPSHOT** | a1bcf313 | 02,08,14,20 UTC | Kimi K2.5 | ✅ Scheduled | PRD Section 8 metrics |
| **DAILY GITHUB SYNC** | eee4cb1f | 11:00 UTC | Kimi K2.5 | ⚠️ TIMEOUT | 2 consecutive 300s timeouts |
| **DAILY METRICS REFRESH** | 1ef071a5 | 14:00 UTC | Kimi K2.5 | ✅ Scheduled | Full PRD refresh |

## Weekly Operations

| Job | Cron ID | Schedule | Model | Status | Purpose |
|-----|---------|----------|-------|--------|---------|
| **WEEKLY FULL REFRESH** | c5222e50 | 01:00 Mon UTC | Kimi K2.5 | ⚠️ WhatsApp Error | Complete PRD audit (functional) |
| **WEEKLY OPUS SWEEP** | 73fcb0c6 | 03:00 Mon UTC | Opus 4 | ⚠️ WhatsApp Error | Deep audit/sync (functional) |
| **DROP MINING** | e0cb7ab1 | 22:00 Wed/Sat UTC | Kimi K2.5 | ✅ Scheduled | Feature extraction from drops |

## ⚠️ DELIVERY ISSUES (Non-Operational)

| Job | Issue | Status |
|-----|-------|--------|
| DAILY GITHUB SYNC | Timeout + WhatsApp delivery fails | Functional, notifications broken |
| WEEKLY FULL REFRESH | WhatsApp delivery fails | Functional, notifications broken |
| WEEKLY OPUS SWEEP | WhatsApp delivery fails | Functional, notifications broken |

## 🔴 DISABLED/CONSOLIDATED AGENTS

| Agent | Reason | Replacement |
|-------|--------|-------------|
| **KIMI PATROL** | Consolidated | UNIFIED OPS MONITOR |
| **RailwayBot** | Idle | UNIFIED OPS MONITOR |
| **StripeBot** | Idle | UNIFIED OPS MONITOR |
| **Wire** | Consolidated | DEEP RESEARCHER |
| **PoeBot** | Consolidated | UNIFIED OPS MONITOR |
| **DC Manager** | Idle | UNIFIED OPS MONITOR |

---

## Current Statistics (2026-03-18 00:47 UTC — GOVERNANCE REALITY CHECK)

- **Total Cron Jobs**: 50 configured
- **Enabled Agents**: 40 active agents (Governance confirmed active)
- **Disabled/Consolidated**: 10 agents
- **Operational Rate**: 95% of enabled agents running (2 agents with timeout errors)
- **WhatsApp Delivery Issues**: 3 scheduled jobs affected (non-operational)
- **System Maturity**: Mature ecosystem with full email workflow automation

## 🔴 CURRENT SYSTEM ISSUES (Updated 2026-03-18 00:47 UTC)

| Issue | Severity | Status | Details |
|-------|----------|--------|---------|
| **DocBot** | 🔴 HIGH | 🚨 6 TIMEOUTS | 6 consecutive timeout errors (180s limit) — documentation pipeline at risk |
| **Creative Review Emailer** | 🔴 HIGH | 🚨 3 TIMEOUTS | 3 consecutive timeout errors (240s limit) — creative review stalled |
| **Daily GitHub Sync** | ⚠️ MEDIUM | ⚠️ 2 TIMEOUTS | 300s timeout errors (functional but slow) |
| **LearningBot** | ⚠️ LOW | ⚠️ 1 TIMEOUT | 1 timeout error on last run |
| **OnboardBot** | ⚠️ LOW | ⚠️ 1 TIMEOUT | 1 timeout error on last run |
| **FounderVoiceBot** | 🟢 LOW | ⚠️ 1 ERROR | File edit failure (not critical) |
| **WhatsApp Delivery** | ⚠️ MEDIUM | ⚠️ FUNCTIONAL | 2 weekly scheduled jobs work but notifications fail |

## Department Coverage Summary

| Department | Agents | Status |
|------------|--------|--------|
| **Email** | 6 | ✅ Complete workflow automation |
| **Operations** | 4 | ✅ Dashboard + monitoring + backup |
| **Intelligence** | 4 | ✅ Research + pattern recognition |
| **Engineering** | 3 | ✅ Frontend + BHA + specs (DC consolidated) |
| **Marketing** | 3 | ✅ Content + social + SEO |
| **Meta** | 5 | ✅ Strategy + governance + learning + skill mining |
| **Customer Success** | 2 | ✅ Onboarding + user health |
| **Product** | 3 | ✅ Specs + docs + launch coord |
| **Security** | 1 | ✅ Sentry AI active |
| **Executive** | 1 | ⚠️ Chief of Staff (has errors) |
| **Communications** | 1 | ✅ FounderVoice active |
| **Revenue** | 0 | 🔴 Consolidated into Unified Ops |

## Resource Allocation

| Model | Agents | Est. Daily Cost | Notes |
|-------|--------|-----------------|-------|
| **Kimi K2.5** | ~23 | ~$0.16 | High volume, low cost |
| **Sonnet 4** | ~9 | ~$0.90 | Balanced performance |
| **Opus 4** | ~4 | ~$3.00 | Strategic oversight |
| **Total** | 36 | ~$4.06 | Full ecosystem coverage |

---

*This roster is maintained by GOVERNANCE agent. Updates reflect constitutional reality, cron list, and operational status.*
