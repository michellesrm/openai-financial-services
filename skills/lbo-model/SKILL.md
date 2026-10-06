---
name: lbo-model
description: Build leveraged-buyout models with debt schedules, cash sweeps, returns, and sensitivities.
---

# LBO Model

1. Define entry valuation, transaction adjustments, financing sources/uses, fees, and sponsor equity.
2. Forecast operating performance with explicit revenue, margin, capex, working-capital, and tax drivers.
3. Build tranche-level debt schedules with cash interest, amortization, mandatory/optional paydown, revolver logic, and minimum cash.
4. Calculate exit enterprise value using an explicit exit multiple and bridge to sponsor equity proceeds.
5. Calculate MOIC and IRR by hold period and scenario.
6. Show sensitivities for entry multiple, exit multiple, leverage, EBITDA growth/margin, and hold period as relevant.
Checks: sources=uses, cash sweep logic, debt never pays below zero, interest references opening/average balances consistently, exit bridge, and IRR/MOIC tie.

## Non-negotiable standards

- Treat the work as analyst work product for human review, not as an authorization to trade, transact, approve, post, bind risk, or provide legal/tax/accounting advice.
- Separate facts, assumptions, calculations, and judgments. Label estimates and scenario assumptions explicitly.
- Prefer primary sources for company-specific facts: regulatory filings, audited statements, investor-relations materials, earnings releases, transcripts, debt documents, and official transaction materials. Use current market data when valuation depends on price, rates, FX, commodities, or consensus.
- Cite or otherwise identify the source and as-of date for material hardcoded inputs. Never invent a missing figure. If a required input is unavailable, state the gap and either stop that calculation or use a clearly labeled illustrative assumption.
- Reconcile units, currencies, periods, fiscal calendars, share counts, and accounting definitions before comparing figures.
- Run explicit checks before presenting results. At minimum check arithmetic, sign conventions, internal consistency, and whether conclusions follow from the evidence.
- Where material uncertainty exists, show sensitivities or scenarios instead of implying false precision.
