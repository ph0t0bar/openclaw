# SPEC-7Day-Sprint-SEO-Poe-Snapback — Execution Roadmap

**Status:** ACTIVE — Created 2026-03-16 by SpecBot  
**Sprint:** March 17–23, 2026  
**Owner:** Joey (with dropper-code support)  
**Related:** `PRD-Action-Plan-2026-03-11.md` (Section 5: Critical Path)

---

## The Gap

The PRD reveals strategic clarity: SEO meta tags (5.4), Poe cross-promo (5.1), and Snapback MVP (5.12) are the highest-leverage moves. But there's **no daily execution plan**. Poe points burn at 43K/6h while we debate architecture.

This spec bridges strategy → tactics → commits.

---

## Day-by-Day Breakdown

### **Day 1 — Tuesday, March 17**  
*Focus: Foundation + Quick Wins*

| Task | Time | Deliverable | Repo |
|------|------|-------------|------|
| Meta tag audit | 2h | Spreadsheet of all routes needing meta | dropanywhere-app |
| OG image template | 2h | Single OG image component (1200x630) | dropanywhere-app |
| Poe bot audit | 1h | List of 14 bots with drop counts, engagement | poe-orchestrator (Hub) |
| Snapback wireframe | 2h | Figma/wireframe of 7-day trial flow | design-docs |
| PR prep | 1h | Branch `feat/seo-meta-tags` created | dropanywhere-app |

**End of Day 1 Success:**  
- [ ] Every route that needs meta tags is listed  
- [ ] OG image component exists (even if hardcoded)  
- [ ] Poe bot list shows which have highest engagement (cross-promo candidates)  
- [ ] Snapback wireframe shows: landing → signup → day 1 task → day 7 outcome

---

### **Day 2 — Wednesday, March 18**  
*Focus: SEO Implementation*

| Task | Time | Deliverable | Repo |
|------|------|-------------|------|
| Dynamic meta tags | 3h | `generateMetadata()` for /, /about, /pricing, /blog/* | dropanywhere-app |
| OG image generation | 2h | Route-based OG images (title auto-injected) | dropanywhere-app |
| Sitemap.xml | 1h | Auto-generated sitemap at /sitemap.xml | dropanywhere-app |
| robots.txt | 30m | Proper robots.txt with sitemap reference | dropanywhere-app |
| JSON-LD structured data | 1.5h | Organization + Product schema | dropanywhere-app |

**End of Day 2 Success:**  
- [ ] Every page has unique, accurate meta title/description  
- [ ] OG images render correctly in social preview tools  
- [ ] Sitemap includes all public routes  
- [ ] Structured data passes Google's Rich Results Test

---

### **Day 3 — Thursday, March 19**  
*Focus: Poe Cross-Promo*

| Task | Time | Deliverable | Repo |
|------|------|-------------|------|
| Bot CTA copy | 2h | "Try DropAnywhere" CTA text for top 5 bots | poe-funnel-copy.md |
| Bot description updates | 2h | Updated descriptions with DA mention | poe.com (manual) |
| Funnel tracking | 2h | `?ref=[bot-name]` params on all DA links | Hub + dropanywhere-app |
| Conversion event | 2h | PostHog/GA event: `poe_crossover_signup` | dropanywhere-app |

**End of Day 3 Success:**  
- [ ] Top 5 bots have DA mention in description  
- [ ] All Poe→DA links have trackable `?ref=` params  
- [ ] Signup flow fires `poe_crossover_signup` event  
- [ ] Dashboard shows: Poe referrals → signups (even if 0)

---

### **Day 4 — Friday, March 20**  
*Focus: Snapback MVP Backend*

| Task | Time | Deliverable | Repo |
|------|------|-------------|------|
| Trial schema | 2h | `trial_config` table: start_date, day, task, completed | opoerator-hub |
| Trial API | 3h | POST /trial/start, GET /trial/day/:n, POST /trial/complete | opoerator-hub |
| Email sequence | 2h | 7 emails (day 0 welcome → day 6 preview → day 7 outcome) | Hub email templates |
| Progress tracking | 1h | Webhook fires on task completion → progress update | opoerator-hub |

**End of Day 4 Success:**  
- [ ] Database can store trial state per user  
- [ ] API endpoints return correct day/task for a user  
- [ ] Email templates exist for all 7 days  
- [ ] Completing a task updates progress (visible in email or UI)

---

### **Day 5 — Saturday, March 21**  
*Focus: Snapback MVP Frontend*

| Task | Time | Deliverable | Repo |
|------|------|-------------|------|
| Trial dashboard | 3h | /trial page: current day, task, progress bar | dropanywhere-app |
| Task completion UI | 2h | Checkbox/button to mark task done → confetti | dropanywhere-app |
| Day navigation | 2h | Can view past days, locked future days | dropanywhere-app |
| Mobile polish | 1h | Works on phone (primary use case) | dropanywhere-app |

**End of Day 5 Success:**  
- [ ] /trial page exists and shows correct state  
- [ ] Completing a task feels rewarding  
- [ ] Can't peek ahead (maintains integrity)  
- [ ] Mobile experience is smooth

---

### **Day 6 — Sunday, March 22**  
*Focus: Integration + Testing*

| Task | Time | Deliverable | Repo |
|------|------|-------------|------|
| End-to-end test | 3h | Joey runs through full 7-day flow as user | staging |
| Bug fixes | 2h | P0/P1 issues from testing | both repos |
| Beta list prep | 1h | 5 beta users identified, emails drafted | n/a |
| Analytics verify | 2h | Confirm all events fire, dashboard shows data | PostHog/GA |

**End of Day 6 Success:**  
- [ ] Joey has completed Day 1-2 of trial as test user  
- [ ] No blocking bugs for beta release  
- [ ] 5 beta users selected (mix of BHA + DA users)  
- [ ] Dashboard shows: signups → trial starts → completions

---

### **Day 7 — Monday, March 23**  
*Focus: Ship + Measure*

| Task | Time | Deliverable | Repo |
|------|------|-------------|------|
| Deploy SEO | 1h | Merge `feat/seo-meta-tags` → main → prod | dropanywhere-app |
| Deploy Poe updates | 1h | Update bot descriptions on poe.com | manual |
| Deploy Snapback | 2h | Merge trial feature branches → prod | both repos |
| Beta invites | 1h | Send "You're in: 7-day Snapback beta" to 5 users | Hub email |
| Baseline metrics | 2h | Document: organic traffic, Poe referrals, trial starts | metrics doc |
| Post-mortem | 1h | What worked, what didn't, Week 2 plan | notion/loom |

**End of Day 7 Success:**  
- [ ] SEO changes live, Google indexing requested  
- [ ] Poe bots updated with DA CTAs  
- [ ] Snapback live for beta users  
- [ ] Metrics baseline captured  
- [ ] Week 2 plan written

---

## Success Metrics (Week 1 Targets)

| Metric | Baseline | Week 1 Target | Measurement |
|--------|----------|---------------|-------------|
| Organic search impressions | TBD | +50% vs baseline | Google Search Console |
| Organic search clicks | TBD | +25% vs baseline | Google Search Console |
| Poe referrals to DA | ~0 | 50 visits | `?ref=poe_*` in logs |
| Poe → DA signups | ~0 | 5 signups | `poe_crossover_signup` event |
| Snapback trial starts | 0 | 5 (beta) | `trial_start` event |
| Trial Day 7 completions | 0 | 2 (40% retention) | `trial_complete` event |

---

## Risk Mitigation

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| SEO takes weeks to show results | High | Ship Day 2, measure in Week 3-4, don't expect instant lift |
| Poe users ignore CTAs | Medium | Test 2-3 CTA variants in Week 2 if no clicks |
| Snapback trial too complex | Medium | Start with 3-day trial if 7 feels heavy |
| Joey gets pulled into other work | High | Block calendar 9am-5pm daily. No meetings except standup. |
| Technical blockers | Low | Dropper-code on call for 30min each morning. |

---

## Dependencies

- **Dropper-code:** Available for 30min each morning if blocked  
- **Design:** Wireframes can be rough (Joey or AI-generated)  
- **Copy:** Joey writes or refines AI-drafted copy  
- **Beta users:** 5 people who already use BHA or DA  
- **Poe access:** Admin access to update bot descriptions  

---

## Daily Standup Template (Slack/WhatsApp to Joey)

> **Day X — [Date]**
> ✅ Completed: [list]
> 🔄 In Progress: [list]
> 🚫 Blocked: [list or "None"]
> 📊 Metrics: [if any to report]
> 🎯 Tomorrow: [top 3 priorities]

---

## Post-Sprint Review (March 24)

Questions to answer:
1. Did we ship all 3 initiatives? (SEO, Poe, Snapback)
2. Which moved the needle most?
3. What should Week 2 focus on?
4. What should we kill/delay?
5. Did the daily execution format work?

---

*Created by SpecBot — 2026-03-16*  
*Next review: March 24, 2026*
