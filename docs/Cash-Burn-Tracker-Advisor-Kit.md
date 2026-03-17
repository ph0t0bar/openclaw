# Cash Burn Tracker — Advisor Kit

**Purpose:** Everything an advisor needs to turn the Cash Burn Tracker into their own repeatable client tool.

---

## Part 1: Questions for the Advisor

*Send these before building anything else. His answers determine the template, the branding, and the workflow.*

---

### Branding & Design

1. **Firm name** — What should appear on the PDF header and spreadsheet?
2. **Logo** — Do you have a logo file (PNG or SVG) you'd like on the reports?
3. **Brand colors** — What are your firm's primary and secondary colors? (Hex codes if you have them, or just describe: "navy and gold," "forest green and cream," etc.)
4. **Font preference** — Do you use a specific font in your client materials? (e.g., your letterhead, website, slide decks)
5. **Tagline or footer text** — Anything you want at the bottom of every report? (e.g., "Prepared by [Firm Name]" or a compliance disclosure)

### Client Workflow

6. **How do you currently gather client financial data?** (Questionnaire? In-person meeting? Pull from aggregator like Orion/Black Diamond/eMoney?)
7. **Do you pull transaction history yourself** (from custodian feeds) **or does the client provide it?**
8. **How many clients would you use this with?** (Ballpark — helps us decide Google Sheets vs Excel vs something more robust)
9. **Do you present this in meetings** (screen share / printed) **or email it to the client ahead of time?**
10. **Do you want the client to have view/edit access to the live spreadsheet**, or just receive the PDF summary?

### Client Profile

11. **Are most of your clients dual-income households**, single-income, retirees, or a mix?
12. **Typical account structure?** (Revocable trust, joint checking, separate accounts, brokerage sweep, etc.)
13. **Income range** — Is the $40K/month spend level representative of your average client, or should we build in lower/higher tiers?
14. **Do your clients typically have irregular events** (bonuses, RSU vests, real estate, balance transfers, etc.) or is cash flow mostly steady?

### Spreadsheet Preferences

15. **Google Sheets or Excel?** (Or both?)
16. **Do you want a scenario toggle** (Low/Base/High spend) or do you prefer a single projection with sensitivity notes?
17. **Alert threshold** — Is $50K a typical buffer floor, or does that vary by client? Should it be configurable per client?
18. **Time horizon** — 12 months standard? Or do some clients need 24-month or multi-year projections?
19. **Any categories you'd add or remove** from the standard Top 15? (e.g., alimony, business expenses, charitable giving, 529 contributions)

### Compliance & Disclosure

20. **Do you need a compliance disclaimer** on the PDF? (e.g., "This projection is for planning purposes only and does not constitute financial advice.")
21. **Any regulatory requirements** for how projections are labeled or presented?

---

## Part 2: Client Intake Form

*This is what the advisor fills out (or sends to the client) for each new engagement. Every field maps directly to the spreadsheet and PDF.*

---

### Client Intake: Monthly Cash Burn Tracker

**Client Name(s):** _______________________________________________

**Date:** _______________

**Prepared by:** _______________________________________________

---

#### A. Account Details

| Field | Value |
|-------|-------|
| Operating account name | |
| Account type (trust, joint checking, etc.) | |
| Current balance | $ |
| As-of date | |
| Minimum buffer (alert threshold) | $ |
| Time horizon (months) | |

#### B. Recurring Deposits

*List every regular deposit into the operating account.*

| Source | Net Amount | Frequency | Deposit Date(s) | Notes |
|--------|-----------|-----------|-----------------|-------|
| | $ | | | |
| | $ | | | |
| | $ | | | |
| | $ | | | |

**February rule:** When a deposit date falls on the 29th/30th/31st of a month that doesn't have that day, post on: [ ] Last business day  [ ] First of next month  [ ] Other: ______

**Known upcoming changes to deposits** (raises, job changes, 401(k) loan payoffs, etc.):

_________________________________________________________________

_________________________________________________________________

#### C. One-Time Inflows

| Description | Net Amount | Expected Date | Notes |
|-------------|-----------|---------------|-------|
| | $ | | |
| | $ | | |
| | $ | | |

#### D. Monthly Spending

**Method:** [ ] Client-provided estimate  [ ] Pulled from transaction data  [ ] Aggregator export

| If transaction data available: | |
|------|------|
| Data source | |
| Date range | |
| Monthly average (ex-taxes/transfers) | $ |
| Planning range (low / base / high) | $ / $ / $ |

**Top spending categories** (fill in if using transaction data):

| Category | Monthly Amount | Type (Fixed/Variable/Lumpy) |
|----------|--------------|---------------------------|
| | $ | |
| | $ | |
| | $ | |
| | $ | |
| | $ | |
| | $ | |
| | $ | |
| | $ | |
| | $ | |
| | $ | |

**Escrowed items** (included in another line, e.g., property tax in mortgage): 

_________________________________________________________________

#### E. One-Time Outflows (Irregulars)

| Description | Amount | Expected Date | Notes |
|-------------|--------|---------------|-------|
| | $ | | |
| | $ | | |
| | $ | | |
| | $ | | |

#### F. Credit Card Mechanics

| Card | Statement Due Date | Paid From | Pay in Full? |
|------|--------------------|-----------|-------------|
| | | | [ ] Yes  [ ] No |
| | | | [ ] Yes  [ ] No |

#### G. Cash Management

| Question | Answer |
|----------|--------|
| Do paychecks land directly in the operating account? | |
| Any automatic sweeps/transfers to other accounts? | |
| Sweep rule preference (e.g., excess above $X to brokerage)? | |

#### H. Additional Notes

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

## Part 3: Setup Instructions

*How to use the template once the advisor has the client's intake form filled out.*

---

### Step-by-Step: New Client Setup

**1. Duplicate the template**
- Open the master template spreadsheet
- File > Make a Copy (Sheets) or Save As (Excel)
- Rename: "[Client Last Name] — Cash Burn Tracker [Year]"

**2. Fill in the Assumptions tab** (Tab 5)
- Start date
- Spend scenario (Low/Base/High amounts from intake)
- Buffer floor (from intake Section A)
- Time horizon

**3. Fill in the Inflows Detail tab** (Tab 3)
- Enter each recurring deposit from intake Section B
- Enter one-time inflows from intake Section C
- Enter any future changes (e.g., 401(k) top-up starting on a specific date)
- Dates auto-adjust for weekends and the February rule

**4. Fill in the Outflows Detail tab** (Tab 4)
- Set baseline monthly spend from intake Section D
- Enter spending categories if doing detailed breakdowns
- Enter one-time irregulars from intake Section E
- Note any escrowed items to avoid double-counting

**5. Review the Monthly Projection tab** (Tab 2)
- Verify March (or start month) proration looks correct
- Check that one-time events appear in the right months
- Confirm no months trigger the buffer alert

**6. Review the Dashboard** (Tab 1)
- Current balance, projected year-end, runway, alerts
- Toggle scenarios to show client the range

**7. Generate the PDF**
- Export the HTML report template with this client's data
- Or: print the Dashboard tab to PDF for a quick summary
- Attach firm logo and brand colors (configured once in the template)

**8. Present to client**
- Share PDF in meeting or email ahead
- Walk through: "Here's your current position, here's what's coming, here's where you'll be"
- Collect any missing irregulars or corrections
- Update spreadsheet, regenerate PDF if needed

### Ongoing Maintenance

- **Monthly:** Reconcile actual balance vs. projected. Update if off by >5%.
- **Quarterly:** Re-pull transaction data. Adjust baseline spend if trends shift.
- **As-needed:** Add new irregulars, deposit changes, life events.
- **Annually:** Duplicate template for next year. Carry forward December ending balance.

---

## Part 4: What We Deliver

| # | Deliverable | Format | Status |
|---|-------------|--------|--------|
| 1 | Advisor Questions (this doc, Part 1) | Markdown / PDF | Ready to send |
| 2 | Client Intake Form (Part 2) | Google Form or PDF | Ready to send |
| 3 | Template Spreadsheet (6 tabs, all formulas) | Google Sheets + Excel | Build after Q&A |
| 4 | Branded PDF Template | HTML + Puppeteer | Build after branding answers |
| 5 | Setup Instructions (Part 3) | PDF | Ready to send |
| 6 | Category Library (pre-loaded typical ranges) | Sheet tab or reference doc | Build after client profile answers |

---

*Prepared via Drop-Anywhere. All client data placeholders — no PII in this template.*

