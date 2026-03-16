# Pre-Launch Audit — Must Complete Before March 24

**Created:** 2026-03-16
**Owner:** Drop (with Joey approval on cuts)
**Deadline:** March 22 (2 days buffer before soft launch)

---

## Phase 1: Code Audit

### Hub (opoerator-hub)
- [ ] List all API endpoints — which are used, which are dead?
- [ ] Check env vars — any referencing services that don't exist?
- [ ] Remove dropanywhere-cron references if service is dead
- [ ] Verify digest pipeline code is clean (even if disabled)
- [ ] Check for hardcoded test data, debug prints, TODO comments
- [ ] Alert monitors — remove false positive triggers (digest stall)
- [ ] Verify email webhook → OpenClaw hook chain works
- [ ] Review all recent Dropper-Code PRs (#180-190) — any regressions?

### DropAnywhere App (dropanywhere-app)
- [ ] Dead features removed in P1-10 trim — verify nothing's broken
- [ ] Frontend references to features that don't exist in Hub?
- [ ] Settings page — does every option actually work?
- [ ] Vault view — verified working after recent PRs?
- [ ] Email-only flow — is there dashboard functionality that contradicts this?
- [ ] Remove any "coming soon" that's not coming soon

### BrutallyHonest.ai (brutallyhonest-next)
- [ ] Verify BHA users are NOT auto-admitted to DA
- [ ] Stripe integration — payment flows working?
- [ ] Persona system — all 15 God Mode personas loading correctly?
- [ ] No cross-contamination between BHA and DA user data

### OpenClaw (this workspace)
- [ ] Agent prompts referencing old file paths?
- [ ] Scripts that reference things that don't exist?
- [ ] Memory files with stale/wrong information?

## Phase 2: Data Audit

### Users (100 in Hub)
- [ ] How many are real humans vs test accounts?
- [ ] Which test accounts should be purged before launch?
- [ ] Family members (lhamer228, rhamersunsetpartners, hamer.daniel) — status?
- [ ] Anyone who should NOT be in the system?

### Drops (843 total)
- [ ] Test drops that should be cleaned?
- [ ] BHA drops that leaked into DA vault?
- [ ] Duplicate or corrupted drops?

### Waitlist
- [ ] Waitlist mechanism verified — new signups land on waitlist, not admitted
- [ ] Admission flow tested — when Joey admits someone, what happens?

## Phase 3: PRD Reconciliation

### For every PRD item:
- [ ] Map to: SHIPPED (code exists + works) / IN PROGRESS / CUT / ASPIRATIONAL
- [ ] Remove aspirational items from launch scope
- [ ] Update all metrics to actuals (not projections)
- [ ] Shipping log reflects reality

### Specs (39 total — most need triage):
| Action | Criteria |
|--------|----------|
| KEEP | Directly maps to shipped or in-progress code |
| ARCHIVE | Good idea but not launching with it |
| KILL | Contradicts current direction or redundant |

## Phase 4: Source of Truth Lock

- [ ] PRD updated and locked as canonical
- [ ] LAUNCH-CRITICAL-PATH verified against code
- [ ] One checklist, no conflicts
- [ ] Joey reviews and signs off

---

## Execution Plan

| Phase | Agent | Model | Approach |
|-------|-------|-------|----------|
| 1a: Hub | Dedicated subagent | Sonnet | Clone repo, grep dead code, map endpoints |
| 1b: DA App | Dedicated subagent | Sonnet | Clone repo, check frontend/backend alignment |
| 1c: BHA | Dedicated subagent | Sonnet | Verify isolation from DA |
| 2: Data | Ops Monitor + UserHealth | Kimi | API calls to Hub, categorize users/drops |
| 3: PRD | Opus Strategist | Opus | Deep reconciliation, spec triage |
| 4: Lock | Joey + Drop | — | Final review and sign-off |

## Output
Each phase produces a report emailed to Joey with:
- What was found
- What was fixed
- What needs Joey's decision
- Updated PRD section
