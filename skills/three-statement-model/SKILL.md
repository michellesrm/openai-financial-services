---
name: three-statement-model
description: Build or populate integrated income statement, balance sheet, and cash-flow models.
---

# Three Statement Model

1. Normalize historical statements and map source line items to model lines.
2. Build operating schedules for revenue, margins, working capital, capex/PPE, debt, interest, taxes, and equity where material.
3. Forecast the income statement from operating drivers.
4. Forecast balance-sheet accounts from explicit turnover/day/ratio assumptions and supporting schedules.
5. Build cash flow from net income through non-cash items and working-capital changes to investing/financing flows.
6. Roll ending cash and debt back to the balance sheet.
Checks: balance sheet balances, ending cash ties across statements, retained earnings roll-forward, debt roll-forward, cash-flow sign conventions, and no calculation hardcodes where formulas should exist.

## Non-negotiable standards

- Treat the work as analyst work product for human review, not as an authorization to trade, transact, approve, post, bind risk, or provide legal/tax/accounting advice.
- Separate facts, assumptions, calculations, and judgments. Label estimates and scenario assumptions explicitly.
- Prefer primary sources for company-specific facts: regulatory filings, audited statements, investor-relations materials, earnings releases, transcripts, debt documents, and official transaction materials. Use current market data when valuation depends on price, rates, FX, commodities, or consensus.
- Cite or otherwise identify the source and as-of date for material hardcoded inputs. Never invent a missing figure. If a required input is unavailable, state the gap and either stop that calculation or use a clearly labeled illustrative assumption.
- Reconcile units, currencies, periods, fiscal calendars, share counts, and accounting definitions before comparing figures.
- Run explicit checks before presenting results. At minimum check arithmetic, sign conventions, internal consistency, and whether conclusions follow from the evidence.
- Where material uncertainty exists, show sensitivities or scenarios instead of implying false precision.
