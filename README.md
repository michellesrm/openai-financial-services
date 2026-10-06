# Financial Services Workflows for OpenAI

An OpenAI-native, skills-first plugin for institutional-style financial workflows across **ChatGPT, Codex, and OpenAI agent environments**.

This package is an independent adaptation inspired by the workflow categories and design patterns in Anthropic's public `anthropics/financial-services` repository. It is not affiliated with, endorsed by, or published by Anthropic or OpenAI.

## What is included

54 skills spanning financial modeling, investment banking, equity research, private equity, fund administration, KYC/operations, and advisor-support workflows.

Key examples: `dcf-model`, `comps-analysis`, `lbo-model`, `three-statement-model`, `earnings-analysis`, `morning-note`, `thesis-tracker`, `catalyst-calendar`, `merger-model`, `ic-memo`, `portfolio-monitoring`, `gl-reconciliation`, and `kyc-document-review`.

## Architecture

This release is intentionally **skills-first**. It has no mandatory MCP dependency, so the workflows can run in environments with different data/tool availability. Skills tell the host model to use the best authorized sources/tools available and to expose data gaps rather than fabricate them.

- `plugin.json` — portable Agent Plugins manifest.
- `.codex-plugin/plugin.json` — Codex compatibility manifest.
- `skills/*/SKILL.md` — reusable workflows.
- `examples/mcp.providers.example.json` — optional examples of finance-data MCP endpoints referenced by the upstream Anthropic project; copy only the providers you are authorized to use into a real `mcp.json` and configure authentication separately.
- `scripts/validate_plugin.py` — lightweight local structural validator.

## Local ChatGPT / Codex testing

OpenAI's current plugin system uses a universal plugin directory shared by ChatGPT and Codex. For local development, point a repo or personal marketplace at this plugin directory, install it from the Plugins directory, then start a new chat/session. The portable root manifest is the canonical package.

For a public release, replace the placeholder developer metadata, add real website/privacy/support fields and review materials, test every skill in a clean environment, then submit the ZIP through OpenAI's plugin submission workflow.

## OpenAI API / Agents environments

OpenAI agent environments can load a plugin package from a capability directory or from an uploaded ZIP. This package is skills-only by default, so it does not require a network connector. Add a real `mcp.json` only when you want a specific authenticated data provider.

## Design principles

1. Primary-source-first financial analysis.
2. Explicit as-of dates and source attribution for material hardcodes.
3. Facts vs assumptions vs judgment are separated.
4. Models include reconciliation and sanity checks.
5. Scenarios/sensitivities replace false precision.
6. Human sign-off remains required for investment, accounting, legal, tax, KYC/AML, and transaction decisions.

## Attribution

See `NOTICE.md`. The upstream repository is Apache-2.0 licensed. This package contains original OpenAI-oriented instructions and workflow adaptations and does not claim compatibility with proprietary data providers unless separately configured.
