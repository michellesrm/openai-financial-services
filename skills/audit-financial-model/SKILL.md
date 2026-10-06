---
name: audit-financial-model
description: Audit Excel-style financial models for formula, linkage, hardcode, and balance errors.
---

# Audit Financial Model

1. Inventory sheets, named ranges, inputs, formulas, external links, and key outputs.
2. Scan for formula inconsistencies, hardcodes inside calculation blocks, broken references, hidden error values, accidental constants, and suspicious blanks.
3. Trace key outputs back to assumptions and source data.
4. Test balance-sheet, cash-flow, debt, share-count, and valuation checks.
5. Identify circular references and assess whether they are intentional and controlled.
6. Classify findings by severity: critical, material, minor, formatting/documentation.
7. Provide the exact cell/range, issue, consequence, and recommended fix whenever cell-level access exists.

## Non-negotiable standards

- Treat the work as analyst work product for human review, not as an authorization to trade, transact, approve, post, bind risk, or provide legal/tax/accounting advice.
- Separate facts, assumptions, calculations, and judgments. Label estimates and scenario assumptions explicitly.
- Prefer primary sources for company-specific facts: regulatory filings, audited statements, investor-relations materials, earnings releases, transcripts, debt documents, and official transaction materials. Use current market data when valuation depends on price, rates, FX, commodities, or consensus.
- Cite or otherwise identify the source and as-of date for material hardcoded inputs. Never invent a missing figure. If a required input is unavailable, state the gap and either stop that calculation or use a clearly labeled illustrative assumption.
- Reconcile units, currencies, periods, fiscal calendars, share counts, and accounting definitions before comparing figures.
- Run explicit checks before presenting results. At minimum check arithmetic, sign conventions, internal consistency, and whether conclusions follow from the evidence.
- Where material uncertainty exists, show sensitivities or scenarios instead of implying false precision.
