# SPEC: Intersecting Wealth — Cash Flow Template Kit

**Client:** Mitchell Hamer, Intersecting Wealth (Stratos Wealth Advisors)  
**Contact:** mitch@intersectingwealth.com | 847-268-2922  
**Date:** 2026-03-11  
**Status:** Discovery — call scheduled for week of Mar 17  
**Prototype:** Cash Burn Tracker PDF (already delivered, received well)  

---

## 1. What We Know

- Mitch is a wealth advisor at Intersecting Wealth (under Stratos Wealth Advisors, LLC — a Registered Investment Advisor)
- He liked the Cash Burn Tracker PDF Joey built for their personal scenario
- He wants to make it **reusable for every family** while keeping it **highly customized**
- He works in a **regulated environment** — compliance, data security, firm-approved tools only
- Likely on **Microsoft 365** (standard for financial services firms)
- Previous email went to **junk** due to missing unsubscribe button (fixed — PR #162 added List-Unsubscribe headers)
- He's busy this week, wants to chat next week

---

## 2. What We Still Need (The 13 Questions — Unanswered)

Joey already asked these in the March 9 email. The call should get answers to all of them.

### Brand Questions (4)

| # | Question | Why We Need It | Likely Answer |
|---|----------|---------------|---------------|
| 1 | Does the color palette in the PDF feel right? | Template branding | Probably yes with minor tweaks |
| 2 | Specific logo version for client docs? | Header/footer assets | He'll send a file |
| 3 | Font preference — Museo Sans or different? | Typography | May have a compliance-approved font |
| 4 | Footer/disclaimer text for every page? | Compliance requirement | YES — the Stratos disclaimer from his email signature is mandatory |

**Pre-call action:** Pull the IW color palette from intersectingwealth.com so we have a starting point to show him.

### Workflow Questions (5)

| # | Question | Why We Need It | Likely Answer |
|---|----------|---------------|---------------|
| 5 | How do you currently gather client financial data? | Determines intake method | Questionnaire or meeting — probably a mix |
| 6 | Do you pull transaction history or does the client provide? | Data flow direction | Probably aggregator (Orion, eMoney, Black Diamond) |
| 7 | How many clients would you use this with? | Scale requirements | 20-100+ families |
| 8 | Present in meetings or email ahead? | Output format priority | Probably both — screen share + PDF follow-up |
| 9 | Client access to live spreadsheet or just PDF? | Sharing model | PDF only (compliance — clients shouldn't edit) |

### Client Questions (4)

| # | Question | Why We Need It | Likely Answer |
|---|----------|---------------|---------------|
| 10 | Is $40K/month spend typical? | Default values | Varies widely — needs tiers |
| 11 | Google Sheets or Excel? | Platform | **Excel** (Microsoft shop) |
| 12 | Additional spending categories? | Template completeness | Alimony, business expenses, charitable giving, 529s, insurance |
| 13 | Standard time horizon — 12 or 24 months? | Projection length | Probably flexible — some need 12, some need 36+ |

---

## 3. Questions WE Need to Ask (Beyond the Original 13)

### Technical Environment

| # | Question | Why |
|---|----------|-----|
| 14 | What version of Microsoft 365 does your firm use? | Determines Power Automate / Forms availability |
| 15 | Do you use SharePoint for client docs? | Where the template lives |
| 16 | Does your firm allow Power Automate flows? | Automation feasibility — some firms lock this down |
| 17 | Any existing client portal (like Orion, eMoney, Black Diamond)? | Don't duplicate what he already has |
| 18 | Can you install Excel add-ins, or is that locked by IT? | Limits customization options |

### Compliance & Data

| # | Question | Why |
|---|----------|-----|
| 19 | What compliance review does a client-facing document need? | Approval process before we finalize |
| 20 | Is there a required archiving process for client reports? | May need specific naming/storage conventions |
| 21 | Does Stratos have a template/style guide for client communications? | Might override IW branding |
| 22 | Any restrictions on where client data can be stored? | SharePoint only? No cloud drives? |

### Scope & Deliverable

| # | Question | Why |
|---|----------|-----|
| 23 | Walk me through your ideal workflow — new client comes in, what happens? | Understand end-to-end so we build the right thing |
| 24 | What's the most time-consuming part of building a cash flow plan today? | Find the pain we're solving |
| 25 | Do you want to be able to hand this to a junior advisor or assistant to run? | Determines how foolproof it needs to be |
| 26 | How often do you update projections per family? (Monthly? Quarterly? Annually?) | Update cadence = template design |
| 27 | What would make this a "hell yes" for you? | Get the real success criteria |

---

## 4. Call Agenda (30-45 minutes)

### Intro (2 min)
> "I want to make sure I build exactly what you need. I've got the prototype — let's figure out what the production version looks like."

### Section 1: Show the Prototype (5 min)
- Screen share the Cash Burn Tracker PDF
- "Does this level of detail feel right? Too much? Too little?"
- "How does the branding look?"
- Get answers to Q1-4 (brand)

### Section 2: Your Current Workflow (10 min)
- "Walk me through what happens when a new family comes in"
- "What tools are you already using?" (Q5-6, Q17)
- "What's the most painful part of cash flow planning right now?" (Q24)
- "How often do you revisit projections?" (Q26)
- Get answers to Q7-9 (workflow)

### Section 3: Client Needs (5 min)
- "Let's talk about the range of families you work with"
- "What categories am I missing?" (Q10, Q12-13)
- "Excel, right?" (Q11 — confirm)
- "Should this work for a junior team member too?" (Q25)

### Section 4: Tech & Compliance (5 min)
- "Quick tech check — Microsoft 365? SharePoint? Power Automate?" (Q14-16, Q18)
- "What does compliance need to see on every page?" (Q4, Q19-20)
- "Any restrictions on where files live?" (Q22)

### Section 5: The Build Plan (5 min)
- Present the deliverable list (Excel template + Form + walkthrough)
- "Here's what I'm thinking — tell me if this hits or misses"
- Get the "hell yes" criteria (Q27)
- Agree on timeline and price

### Wrap (3 min)
- "I'll have a draft ready in [X days]. We'll do one more call to refine."
- Get brand assets (logo file, any style guide)
- Schedule follow-up

---

## 5. Likely Deliverables (Based on Best Guesses)

### 5a. Excel Workbook Template

```
TAB 1: SETUP & CLIENT PROFILE
├── Family name, advisor name, date
├── Household members (names, ages, working status)
├── Income sources (salary, bonus, investment income, rental, etc.)
├── Assets (checking, savings, brokerage, 401k, real estate)
├── Liabilities (mortgage, cards, loans, HELOC)
├── Goals (retirement age, education funding, major purchases)
├── All input cells highlighted (branded color)
└── Data validation dropdowns where appropriate

TAB 2: MONTHLY CASH FLOW (12-24 months)
├── Auto-populated from Tab 1
├── Income row (all sources summed)
├── Expense categories (housing, transport, food, insurance, medical, 
│   education, lifestyle, charitable, business, misc)
├── Net cash flow per month
├── Running balance
├── Conditional formatting: green (healthy), yellow (watch), red (alert)
└── Buffer threshold alert (configurable, default $50K)

TAB 3: SCENARIO ANALYSIS
├── Three columns: Conservative / Base / Optimistic
├── Adjustable assumptions (spend multiplier, income changes)
├── Side-by-side comparison charts
├── "What if" toggles (lose a job, sell property, major expense)
└── Summary: "In X of 3 scenarios, buffer holds through month 12"

TAB 4: CHARTS & VISUALS
├── Monthly cash flow bar chart
├── Running balance line chart (all 3 scenarios)
├── Expense breakdown pie chart
├── Income vs expense trend
└── All in IW brand colors

TAB 5: CLIENT REPORT (print-ready)
├── IW header (logo, advisor name, date)
├── Executive summary (auto-generated text from formulas)
├── Key metrics boxes (monthly burn, runway, buffer status)
├── Selected charts (embedded from Tab 4)
├── Assumptions & footnotes
├── IW footer (disclaimer, contact info, compliance text)
└── Page breaks set for clean PDF export

TAB 6: INSTRUCTIONS (hidden from client view)
├── How to duplicate for a new family
├── Which cells to fill in
├── How to adjust scenarios
├── How to export PDF
├── Troubleshooting common issues
└── "Built by Joey Hamer — joey@photobarchicago.com"
```

### 5b. Microsoft Form (Client Intake)

A branded form Mitch can send to new families:

```
INTERSECTING WEALTH — FINANCIAL SNAPSHOT

Section 1: About Your Household
- Family name
- Number of income earners
- Names, ages, employment status of each member

Section 2: Income
- Primary salary/wages (each earner)
- Bonus / commission (expected)
- Investment income
- Rental income
- Other income sources

Section 3: Current Assets
- Checking / savings balances
- Brokerage accounts
- Retirement accounts (401k, IRA)
- Real estate (estimated values)
- Other assets

Section 4: Liabilities
- Mortgage balance + monthly payment
- Credit cards (balances + minimum payments)
- Auto loans
- Student loans
- Other debts

Section 5: Monthly Expenses (estimated)
- Housing (beyond mortgage — maintenance, insurance, tax)
- Transportation
- Food / groceries
- Insurance premiums
- Medical / dental
- Education / childcare
- Lifestyle / entertainment
- Charitable giving
- Other recurring

Section 6: Goals & Timeline
- Target retirement age
- Major planned expenses (next 24 months)
- Education funding goals
- Any expected windfalls (inheritance, sale, bonus)

Section 7: Anything Else
- Open text field
```

### 5c. Power Automate Flow (if firm allows)

```
TRIGGER: New Microsoft Form response submitted
ACTION 1: Copy template Excel file in SharePoint
ACTION 2: Rename to "[FamilyName] — Cash Flow Projection — [Date]"
ACTION 3: Write form responses into Tab 1 cells
ACTION 4: Notify Mitch via Teams/email: "New family workbook ready for review"
```

If Power Automate isn't available, the manual process is:
1. Duplicate template file
2. Rename it
3. Fill in Tab 1 from form responses
4. Done

### 5d. Walkthrough

- 30-60 min recorded screen share (Loom or Teams recording)
- Step by step: new family → intake → fill template → review → export → send
- Mitch keeps the recording, shares with team
- Written setup doc as backup

---

## 6. Pricing

| Option | What | Price |
|--------|------|-------|
| **Template Only** | Excel + Form + written instructions | $500 |
| **Full Setup** | Template + Power Automate + 1hr walkthrough + customization | $1,000 |
| **Ongoing Support** | Full Setup + quarterly check-in, updates, new features | $1,000 + $200/quarter |

**For Mitch (family pricing):** Consider doing the Full Setup at $500 as a family rate, with the understanding that if it works well, he becomes the case study for selling the template kit to other advisors.

**For Gumroad (after Mitch validates):**
- "Financial Advisor Cash Flow Kit" — $197
- Generic branding (advisor customizes)
- Includes: Excel template + Form template + Power Automate instructions + video walkthrough
- Target: independent FAs, small RIAs, financial coaches

---

## 7. Timeline

| Step | When | What |
|------|------|------|
| **Pre-call prep** | Before the call | Pull IW branding, prep prototype in Excel (not just PDF) |
| **Discovery call** | Week of Mar 17 | Get answers to all 27 questions |
| **Draft v1** | 3-4 days after call | Excel template with real formulas, branded |
| **Review call** | ~Mar 24 | Walk through with Mitch, refine |
| **Final delivery** | ~Mar 28 | Template + Form + walkthrough recording |
| **Gumroad listing** | April | Genericized version for sale |

---

## 8. What This Validates

Even though this isn't a DropAnywhere SaaS play, it validates:

1. **The advisory loop concept works** — advisor + template + client communication = value
2. **People will pay for productized financial tools** — pricing signal for future products
3. **The "invisible" model resonates** — clients interact through familiar channels (email, forms), never see the machinery
4. **Joey can sell productized services** — not just SaaS, but done-for-you templates with walkthrough
5. **Case study for Gumroad** — "Built for a wealth advisor managing $XXM" is powerful social proof

---

## 9. Pre-Call Checklist

- [ ] Pull IW colors from intersectingwealth.com (exact hex values)
- [ ] Download IW logo variations
- [ ] Check if Museo Sans is available / licensable for Excel
- [ ] Build a rough Excel prototype (even if formulas aren't perfect)
- [ ] Prep screen share with the existing PDF + new Excel draft
- [ ] Have this spec open during the call for reference
- [ ] Record the call (with Mitch's permission)

---

*This is a consulting engagement that feeds the product roadmap. Build for Mitch. Sell to everyone else.*

