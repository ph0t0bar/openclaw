# PRD: Monthly Cash Burn Tracker — Fidelity Rev Trust

**Author:** Joey (with AI assistance)  
**Date:** 2026-03-09  
**Status:** Ready to build spreadsheet  
**Client:** PERSON A & PERSON B  
**Deliverable:** Google Sheets / Excel workbook

---

## Executive Summary

Build a monthly cash-burn tracker for a household operating account (Fidelity Revocable Trust). The model projects forward balances based on recurring deposits, known irregular events, and a spending baseline derived from 3+ years of transaction data. All assumptions are footnoted for auditability.

---

## Account Details

| Item | Value | Footnote |
|------|-------|----------|
| Operating account | Fidelity Revocable Trust | [F1] |
| Current balance | $160,000 (as of March 8, 2026) | [F1] |
| Buffer floor (alert) | $50,000 | [F4] |
| Spending baseline | $39,000–$42,000/month | [F5] |
| Data source | Transaction data 2022–Feb 2026 | [F15] |

---

## Inflows (Recurring)

| Source | Amount | Timing | Footnote |
|--------|--------|--------|----------|
| PERSON B paycheck | $5,000 | 15th each month | [F2] |
| PERSON B paycheck | $5,000 | 30th each month | [F2][F3] |
| PERSON A paycheck | $30,000 | 30th each month | [F2][F3] |
| PERSON B 401(k) loan payoff top-up | $900 | 15th each month, **starting 8/15/2026** | [F25] |
| **Combined monthly (Mar–Jul)** | **$40,000** | | |
| **Combined monthly (Aug–Dec)** | **$40,900** | | |

**February rule [F3]:** When a month has no 30th, "30th" deposits post on the last business day of February.

---

## Inflows (One-Time)

| Event | Amount | Date | Footnote |
|-------|--------|------|----------|
| PERSON B bonus (net, conservative) | $30,000 | April 1, 2026 | [F21] |
| Real estate liquidation (net) | $26,500 | April 30, 2026 (120 days from 12/31/25) | [F24] |

---

## Outflows (One-Time Irregulars)

| Event | Amount | Date | Footnote |
|-------|--------|------|----------|
| Savor CC balance transfer payoff | $12,000 | May 1, 2026 | [F22] |
| Bank of America balance transfer payoff | $12,000 | July 17, 2026 (Friday) | [F23] |

**Client to provide additional irregulars** (property taxes seasonal? travel? medical? club annuals?)

---

## Spending Categories (Top 15 — 2025 Actuals, Monthly Run Rate)

| Category | Monthly | Type | Footnote |
|----------|---------|------|----------|
| Mortgage | $8,100 | Fixed | [F6][F7] |
| Child Care | $4,600 | Recurring | [F9] |
| Shopping | $3,900 | Variable | [F9] |
| Auto Payments | $2,500 | Fixed | [F9] |
| Country Club | $2,100 | Recurring | [F17] |
| Restaurants & Bars | $1,700 | Variable | [F9] |
| Insurance (non-homeowners) | $1,350 | Fixed | [F19] |
| Groceries | $1,250 | Variable | [F9] |
| Clothing | $1,250 | Variable | [F9] |
| Medical | $1,000 | Variable | [F9] |
| Travel & Vacation | $950 | Lumpy | [F9] |
| Entertainment & Recreation | $850 | Variable | [F9] |
| Student Loans | $750 | Fixed | [F18] |
| Fitness | $600 | Recurring | [F9] |
| Gas & Electric | $500 | Recurring | [F9] |
| Home Improvement | $200 | Adjusted | [F8] |
| **Top 15 subtotal** | **~$31,600** | | |
| Remaining categories | $7,500–$9,000 | Variable | [F9] |
| **All-in monthly** | **$39,000–$42,000** | | [F5] |

**Key note [F6]:** Property taxes and homeowners insurance are escrowed and included in the mortgage. No separate lines to avoid double-counting.

**Key note [F8]:** Home improvement reduced 80% from 2025. The Jan 2026 $43,400 check was a 2025 project — excluded from run rate.

---

## Projected Month-End Balances (Base Case: $40,000/mo)

| Month | Starting | Inflows | Outflows | Ending | Alert? |
|-------|----------|---------|----------|--------|--------|
| Mar 31 | $160,000 | $40,000 | $31,000* | **$169,000** | No |
| Apr 30 | $169,000 | $96,500 | $40,000 | **$225,500** | No |
| May 31 | $225,500 | $40,000 | $52,000 | **$213,500** | No |
| Jun 30 | $213,500 | $40,000 | $40,000 | **$213,500** | No |
| Jul 31 | $213,500 | $40,000 | $52,000 | **$201,500** | No |
| Aug 31 | $201,500 | $40,900 | $40,000 | **$202,400** | No |
| Sep 30 | $202,400 | $40,900 | $40,000 | **$203,300** | No |
| Oct 31 | $203,300 | $40,900 | $40,000 | **$204,200** | No |
| Nov 30 | $204,200 | $40,900 | $40,000 | **$205,100** | No |
| Dec 31 | $205,100 | $40,900 | $40,000 | **$206,000** | No |

*March outflows prorated from March 8 start date [F11]*

### Three-Scenario View

| Month-End | Low ($39k) | Base ($40k) | High ($42k) |
|-----------|-----------|-------------|-------------|
| Mar 31 | $169,800 | $169,000 | $167,500 |
| Apr 30 | $227,300 | $225,500 | $222,000 |
| May 31 | $216,300 | $213,500 | $208,000 |
| Jun 30 | $217,300 | $213,500 | $206,000 |
| Jul 31 | $206,300 | $201,500 | $192,000 |
| Aug 31 | $208,100 | $202,400 | $190,900 |
| Sep 30 | $209,900 | $203,300 | $189,800 |
| Oct 31 | $211,700 | $204,200 | $188,700 |
| Nov 30 | $213,500 | $205,100 | $187,600 |
| Dec 31 | $215,300 | $206,000 | $186,500 |

**No months breach the $50,000 buffer under any scenario.**

---

## Spreadsheet Structure

### Tab 1: Dashboard
- Current balance, total inflows/outflows, net burn, projected ending balance, runway
- Scenario selector (Low/Base/High)
- Next cash events timeline
- Alert indicator

### Tab 2: Monthly Projection
- Columns: Month, Starting Balance, Inflows, Outflows, Net Burn, Ending Balance, Alert
- March prorated from 3/8
- Formulas reference Inflows Detail and Outflows Detail tabs

### Tab 3: Inflows Detail
- Each deposit source as a separate row with amount, frequency, date formula
- Business-day adjustment logic built in
- February rule implemented
- One-time items (bonus, real estate) with exact dates

### Tab 4: Outflows Detail
- Baseline monthly spend (scenario-driven)
- Category breakdown for reference
- One-time irregulars (Savor, BofA) with exact dates
- No double-counting with escrowed items [F6]

### Tab 5: Assumptions
- Start date, spend scenario toggle, buffer floor, February rule, holidays range

### Tab 6: Footnotes & Assumptions
- All 25 footnotes [F1]–[F25] with ID, topic, note, last updated
- Referenced throughout all tabs via bracket tags

---

## Footnotes Reference

| ID | Topic | Note |
|----|-------|------|
| F1 | Operating Balance | $160,000 in Fidelity Rev Trust as of March 8, 2026 |
| F2 | Deposit Schedule | PERSON B $5,000 on 15th and 30th; PERSON A $30,000 on 30th |
| F3 | February Rule | "30th" deposits post on last business day of February |
| F4 | Buffer Floor | Alert if projected balance < $50,000 |
| F5 | Spending Methodology | 2026 baseline $39k–$42k/mo; excludes taxes/transfers/CC payments |
| F6 | Escrowed Items | Property taxes + homeowners insurance included in mortgage |
| F7 | Mortgage | $8,100/mo fixed (includes escrow per F6) |
| F8 | Home Improvement | $200/mo after 80% reduction; Jan 2026 $43.4k one-off excluded |
| F9 | Category Baselines | Derived from 2025 actuals |
| F10 | Intra-Month Accrual | Even accrual; troughs pre-30th, lift on 15th |
| F11 | March Proration | Start 3/8/2026; March outflows prorated |
| F12 | Credit Card Treatment | Charges in spend; paydowns excluded except specified payoffs |
| F14 | Holidays/Business Days | Weekend adjustment; optional bank-holiday list |
| F15 | Data Window | 2022–Feb 2026; excludes $28.6k trust txn + $742 IRA rollover |
| F16 | Runway Definition | Ending Balance ÷ Avg Monthly Net Burn (3–6 month lookback) |
| F17 | Country Club | $2,100/mo |
| F18 | Student Loans | $750/mo fixed |
| F19 | Insurance Premiums | Non-homeowners: $1,350/mo fixed |
| F20 | Scenario Toggle | Low $39k / Base $40k / High $42k |
| F21 | PERSON B Bonus | $30,000 net on 4/1/2026 (~$50k gross, conservative) |
| F22 | Savor CC Payoff | $12,000 all-in on 5/1/2026 |
| F23 | BofA CC Payoff | $12,000 on Friday 7/17/2026 |
| F24 | Real Estate Liquidation | $26,500 net on 4/30/2026 (120 days from 12/31/25) |
| F25 | 401(k) Loan Payoff | +$900/mo from PERSON B starting 8/15/2026 |

---

## Key Formulas (Google Sheets / Excel)

### Deposit date with business-day adjustment
```
=IF(WEEKDAY(DATE(Year,Month,15),2)>5, WORKDAY(DATE(Year,Month,15)+1,-1,Holidays), DATE(Year,Month,15))
```

### February rule for "30th" deposits
```
=IF(Month=2, WORKDAY(EOMONTH(DATE(Year,2,1),0)+1,-1,Holidays), IF(WEEKDAY(DATE(Year,Month,30),2)>5, WORKDAY(DATE(Year,Month,30)+1,-1,Holidays), DATE(Year,Month,30)))
```

### PERSON B 15th with 401(k) top-up starting Aug 2026
```
=IF(Month+Year*100>=202608, 5900, 5000)
```

### March proration
```
=IF(Month=DATE(2026,3,1), BaselineSpend*(31-8+1)/31, BaselineSpend)
```

### Alert
```
=IF(EndingBalance < BufferFloor, "ALERT", "")
```

### Runway
```
=EndingBalance / ABS(AVERAGE(last 3-6 months Net Burn))
```

---

## Outstanding Items (Client to Provide)

- [ ] Additional irregular expenses (amount + month): summer travel, club annuals, medical, home projects, tuition changes
- [ ] Credit card mechanics: which card(s), due dates, pay in full?
- [ ] Optional: U.S. bank holiday list for WORKDAY refinement
- [ ] Optional: sweep rule preference (e.g., excess above $200k → brokerage at Altruist)

---

## Delivery

- [ ] Build Google Sheet with all 6 tabs
- [ ] Send via email to client
- [ ] Include PDF summary with key projections and footnotes

---

*Document sanitized: NO PII. All names replaced with PERSON A / PERSON B / LAST NAME placeholders.*

