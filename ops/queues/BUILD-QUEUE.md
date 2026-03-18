# BUILD QUEUE — DropAnywhere Launch
# Updated: 2026-03-18
# Owner: BUILD DRIVER
# Target: Soft launch March 24

## Priority Order (work top to bottom)

### P0 — Launch Blockers
- [x] Email-only onboarding flow (new user → first email → first digest) *[DONE: 2026-03-18]*
- [x] Stripe payment fix (3 failed charges, 0 succeeded — investigate) *[DONE: 2026-03-18]*
- [x] Landing page copy finalized for email-only pivot *[DONE: 2026-03-18 - PR #152 ready to merge]*
- [ ] Email ingestion reliability (drops via email must never fail) *[TASK: task_1773835740_369 - APPROVED]*

### P1 — Launch Critical
- [ ] Soft launch invite email template (personal, warm, Brooke theme) *[TASK: task_1773835770_833 - APPROVED]*
- [ ] First-run experience: user emails in → gets confirmation → gets first digest
- [ ] Digest quality audit (pull a real digest, verify formatting + content)
- [ ] Error handling: what happens when email parsing fails?

### P2 — Polish
- [ ] Weekly Catch email template polished
- [ ] Unsubscribe/pause flow working
- [ ] Settings accessible via email reply
- [ ] Mobile email rendering verified

### Completed
- Email-only onboarding flow (2026-03-18) ✅
- Stripe payment fix (2026-03-18) ✅  
- Landing page copy finalized (2026-03-18, PR #152 ready to merge) ✅
