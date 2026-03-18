# BUILD QUEUE — DropAnywhere Launch
# Updated: 2026-03-18
# Owner: BUILD DRIVER
# Target: Soft launch March 24

## Priority Order (work top to bottom)

### P0 — Launch Blockers
- [x] Email-only onboarding flow (new user → first email → first digest) *[DONE: 2026-03-18]*
- [x] Stripe payment fix (3 failed charges, 0 succeeded — investigate) *[DONE: 2026-03-18]*
- [x] Landing page copy finalized for email-only pivot *[DONE: 2026-03-18 - PR #152 ready to merge]*
- [x] Email ingestion reliability (drops via email must never fail) *[DONE: 2026-03-18 - PR #203 open, needs review/merge]*

### P1 — Launch Critical
- [x] Soft launch invite email template (personal, warm, Brooke theme) *[DONE: 2026-03-18 - Confirmed completed]*
- [x] First-run experience: user emails in → gets confirmation → gets first digest *[DONE: 2026-03-18 - Email-only onboarding flow completed]*
- [ ] Digest quality audit (pull a real digest, verify formatting + content) *[TASK: task_1773843015_272 - PENDING APPROVAL]*
- [ ] Error handling: what happens when email parsing fails? *[IN PROGRESS: PR #203 open for email ingestion reliability]*

### P2 — Polish
- [ ] Weekly Catch email template polished
- [ ] Unsubscribe/pause flow working
- [ ] Settings accessible via email reply
- [ ] Mobile email rendering verified

### Completed
- Email-only onboarding flow (2026-03-18) ✅
- Stripe payment fix (2026-03-18) ✅  
- Landing page copy finalized (2026-03-18, PR #152 ready to merge) ✅
- Soft launch invite email template (2026-03-18) ✅
- First-run experience onboarding (2026-03-18) ✅
