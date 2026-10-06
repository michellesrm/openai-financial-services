# Financial Services routing matrix

This matrix supports the `finance-router` coordination skill. Native OpenAI skill activation still begins from each skill's name and description; this file is for ambiguous or composite requests.

| Domain | User intent | Primary skill | Common supporting skills |
|---|---|---|---|
| Modeling | DCF / intrinsic valuation | dcf-model | three-statement-model, model-update, comps-analysis |
| Modeling | Trading comps / peer valuation | comps-analysis | company-one-pager, competitive-analysis |
| Modeling | LBO / sponsor returns | lbo-model | returns-analysis, deal-screening |
| Modeling | Integrated statements | three-statement-model | clean-financial-data, audit-financial-model |
| Modeling | Audit model | audit-financial-model | clean-financial-data |
| Modeling | Clean source data | clean-financial-data | datapack-builder |
| IB | Merger accretion/dilution | merger-model | comps-analysis, three-statement-model |
| IB | Pitch materials | pitch-deck | company-one-pager, comps-analysis, deck-qc |
| IB | CIM | cim-builder | company-one-pager, competitive-analysis, datapack-builder |
| IB | Teaser | teaser | company-one-pager |
| IB | Buyer universe | buyer-list | company-one-pager, competitive-analysis |
| IB | Process instructions | process-letter | deal-tracker |
| IB | Deal execution tracker | deal-tracker | dd-checklist |
| IB | Company profile | company-one-pager | competitive-analysis |
| IB | Deck QA | deck-qc | audit-financial-model |
| Research | Post-earnings | earnings-analysis | model-update, thesis-tracker, catalyst-calendar |
| Research | Earnings preview | earnings-preview | catalyst-calendar, thesis-tracker |
| Research | Initiating coverage | initiating-coverage | sector-overview, competitive-analysis, comps-analysis, dcf-model |
| Research | Morning note | morning-note | catalyst-calendar |
| Research | Sector work | sector-overview | competitive-analysis |
| Research | Competitive landscape | competitive-analysis | sector-overview |
| Research | Idea generation | idea-generation | thesis-tracker, catalyst-calendar |
| Research | Thesis update | thesis-tracker | earnings-analysis, catalyst-calendar |
| Research | Catalyst tracking | catalyst-calendar | thesis-tracker |
| Research | Existing model update | model-update | earnings-analysis, three-statement-model |
| PE | Source targets | deal-sourcing | deal-screening |
| PE | Screen an opportunity | deal-screening | lbo-model, dd-checklist |
| PE | Diligence request list | dd-checklist | dd-meeting-prep |
| PE | Diligence meeting | dd-meeting-prep | dd-checklist |
| PE | IC memorandum | ic-memo | lbo-model, returns-analysis, dd-checklist |
| PE | Returns bridge | returns-analysis | lbo-model |
| PE | Unit economics | unit-economics | competitive-analysis |
| PE | Portfolio monitoring | portfolio-monitoring | variance-commentary, value-creation-plan |
| PE | Value creation | value-creation-plan | portfolio-monitoring |
| PE | AI readiness | ai-readiness | value-creation-plan |
| Fund ops | GL reconciliation | gl-reconciliation | break-tracing |
| Fund ops | Trace breaks | break-tracing | gl-reconciliation |
| Fund ops | Accruals | accrual-review | variance-commentary |
| Fund ops | Roll-forward | roll-forward | gl-reconciliation |
| Fund ops | NAV tie-out | nav-tie-out | valuation-review, statement-audit |
| Fund ops | Private valuation review | valuation-review | nav-tie-out |
| Fund ops | Investor statement audit | statement-audit | nav-tie-out |
| Fund ops | Variance commentary | variance-commentary | accrual-review |
| KYC/Ops | Review KYC documents | kyc-document-review | kyc-rules-grid |
| KYC/Ops | Apply KYC rules | kyc-rules-grid | kyc-document-review |
| Data/Diligence | Build diligence datapack | datapack-builder | clean-financial-data |
| Advisor | Client meeting prep | advisor-meeting-prep | client-review |
| Advisor | Periodic client review | client-review | rebalance-review |
| Advisor | Prospect intake | prospect-intake | advisor-meeting-prep |
| Advisor | Compliance pre-check | advisor-compliance-precheck | client-review |
| Advisor | Rebalancing review | rebalance-review | tax-loss-harvesting-review |
| Advisor | Tax-lot harvesting review | tax-loss-harvesting-review | rebalance-review |
| Advisor | Alternatives brief | alternatives-brief | advisor-compliance-precheck |
| Advisor | Estate issue brief | estate-brief | advisor-meeting-prep |

## Selection rule

Choose one primary skill whenever possible. Add supporting skills only when the user explicitly requests their output or the primary workflow cannot be completed coherently without them.
