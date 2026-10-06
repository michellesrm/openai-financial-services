---
name: finance-router
description: Route broad, ambiguous, or multi-step institutional finance requests to the smallest appropriate combination of bundled Financial Services skills. Use for requests such as analyzing a company end-to-end, preparing a market or earnings workflow, evaluating a deal, updating an investment thesis, or any finance request that clearly needs two or more specialized workflows. Do not use when one specialized skill already clearly matches the user's goal.
---

# Finance Router

Use this skill as a coordinator, not as a substitute for the specialized skills.

## Routing procedure

1. Classify the user's objective into one or more finance domains: financial modeling, equity research, investment banking, private equity, fund/accounting operations, KYC/operations, or advisor support.
2. Read `references/routing-matrix.md`. When exact phrase matching or regression behavior is useful, consult `references/routing-rules.json`.
3. Select the **smallest sufficient skill set**. Prefer one primary skill. Add supporting skills only when their outputs are genuinely required.
4. Load and follow the selected specialized `SKILL.md` instructions before doing substantive work.
5. Sequence dependencies logically. Example: update actuals before revising a model; revise estimates before re-valuing; establish a thesis before scoring new evidence.
6. Use live or connected data only through tools the host environment already authorizes. Never assume a specific data vendor is available.
7. If required data is missing, identify the gap explicitly rather than inventing inputs.
8. For current-market or company requests, preserve explicit as-of dates and distinguish facts, consensus, assumptions, and analyst judgment.
9. Do not route non-finance requests into this plugin merely because they mention a company or numbers.

## Common compositions

- Full equity initiation: `initiating-coverage` + `sector-overview` + `competitive-analysis` + `comps-analysis` and/or `dcf-model`.
- Post-earnings thesis update: `earnings-analysis` + `model-update` + `thesis-tracker` + optional `catalyst-calendar`.
- Morning market workflow: `morning-note` + `catalyst-calendar`.
- M&A buyer work: `buyer-list` + `company-one-pager` + optional `deal-tracker`.
- LBO underwriting: `deal-screening` + `lbo-model` + `returns-analysis` + optional `ic-memo`.
- Portfolio-company review: `portfolio-monitoring` + `variance-commentary` + optional `value-creation-plan`.
- Fund close/review: `gl-reconciliation` + `roll-forward` + `nav-tie-out` + optional `statement-audit`.

## Routing discipline

Do not load every potentially relevant skill. A route is successful when it uses the minimum number of specialized workflows needed to produce a complete, internally consistent answer.
