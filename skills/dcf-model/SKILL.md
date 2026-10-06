---
name: dcf-model
description: Build discounted-cash-flow valuations with WACC, terminal value, scenarios, and sensitivities.
---

# DCF Model

1. Establish historical financials and forecast operating drivers rather than extrapolating headline growth blindly.
2. Forecast unlevered free cash flow from revenue, margins, taxes, D&A, capex, and working capital.
3. Calculate WACC using market-value capital weights. Use gross interest-bearing debt for capital weighting; treat cash in the enterprise-to-equity bridge rather than as negative debt in WACC.
4. Estimate terminal value using a defensible perpetual-growth or exit-multiple method; cross-check the implied terminal assumptions.
5. Discount explicit-period cash flows and terminal value to the valuation date.
6. Bridge enterprise value to equity value, diluted shares, and implied per-share value.
7. Produce bear/base/bull cases and at least one two-dimensional sensitivity table around the two most material valuation assumptions.
Checks: FCF sign, discount periods, WACC inputs, terminal-value share of EV, EV-to-equity bridge, circularity, and sensitivity monotonicity.

## Non-negotiable standards

- Treat the work as analyst work product for human review, not as an authorization to trade, transact, approve, post, bind risk, or provide legal/tax/accounting advice.
- Separate facts, assumptions, calculations, and judgments. Label estimates and scenario assumptions explicitly.
- Prefer primary sources for company-specific facts: regulatory filings, audited statements, investor-relations materials, earnings releases, transcripts, debt documents, and official transaction materials. Use current market data when valuation depends on price, rates, FX, commodities, or consensus.
- Cite or otherwise identify the source and as-of date for material hardcoded inputs. Never invent a missing figure. If a required input is unavailable, state the gap and either stop that calculation or use a clearly labeled illustrative assumption.
- Reconcile units, currencies, periods, fiscal calendars, share counts, and accounting definitions before comparing figures.
- Run explicit checks before presenting results. At minimum check arithmetic, sign conventions, internal consistency, and whether conclusions follow from the evidence.
- Where material uncertainty exists, show sensitivities or scenarios instead of implying false precision.
