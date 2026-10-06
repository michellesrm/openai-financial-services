# Financial Services Workflows for OpenAI

An installable, skills-first OpenAI plugin for institutional-style financial workflows across **ChatGPT, Codex, and OpenAI agent environments**.

This package is an independent adaptation inspired by the workflow categories and design patterns in Anthropic's public `anthropics/financial-services` repository. It is not affiliated with, endorsed by, or published by Anthropic or OpenAI.

## v0.2.0

The plugin now contains **55 skills**: 54 specialized finance workflows plus `finance-router`, a coordination skill for broad or multi-step requests.

OpenAI's native skill discovery exposes each skill's `name` and `description` to the model. The model selects relevant workflows from that metadata. `finance-router` activates only for broad, ambiguous, or composite finance requests and then selects the smallest sufficient combination of specialized skills.

Examples:

- “Build a DCF for NVDA” → `dcf-model`
- “JPM reported earnings. Update my model and thesis.” → `earnings-analysis` + `model-update` + `thesis-tracker`
- “Prepare a morning market note and tomorrow's catalysts.” → `morning-note` + `catalyst-calendar`
- “Screen this PE deal, build an LBO, and draft an IC memo.” → `deal-screening` + `lbo-model` + `returns-analysis` + `ic-memo`

## Architecture

- `plugin.json` — portable Agent Plugins manifest
- `.codex-plugin/plugin.json` — Codex compatibility manifest
- `skills/*/SKILL.md` — 55 discoverable workflows
- `skills/finance-router/references/` — routing matrix and deterministic route registry
- `.agents/plugins/marketplace.json` — Git-backed marketplace entry for installation/testing
- `.codex/config.toml` — enables the plugin for this trusted repository
- `tests/routing_evals.json` — positive and negative routing cases
- `scripts/validate_plugin.py` — manifest/skill/inventory validation
- `scripts/test_routing.py` — route registry and eval-fixture validation
- `scripts/package_plugin.py` — deterministic distributable ZIP builder
- `.github/workflows/validate.yml` — CI validation and packaging
- `examples/mcp.providers.example.json` — optional finance-data MCP endpoints; not loaded by default

## Installation

See `INSTALL.md`. The repository itself can be added as a Git marketplace source with Codex CLI, and the included marketplace catalog exposes the plugin for local testing in supported ChatGPT/Codex clients.

## Automatic routing

Automatic routing is intentionally based on OpenAI's native skill discovery rather than a hard-coded runtime dispatcher. This keeps the plugin portable across OpenAI surfaces. The `finance-router` skill adds orchestration for requests that require multiple workflows while avoiding indiscriminate loading of all skills.

The routing eval fixture currently covers DCF, comps, LBO, earnings, morning notes, initiation, thesis updates, M&A, pitch books, CIMs, buyer lists, PE screening, IC memos, portfolio monitoring, fund NAV work, KYC, advisor reviews, and negative non-routing cases.

## Design principles

1. Primary-source-first financial analysis.
2. Explicit as-of dates and source attribution for material hardcodes.
3. Facts, assumptions, calculations, and judgment remain distinct.
4. Models include reconciliation and sanity checks.
5. Scenarios and sensitivities replace false precision.
6. Human sign-off remains required for investment, accounting, legal, tax, KYC/AML, and transaction decisions.

## Attribution

See `NOTICE.md`. The upstream repository is Apache-2.0 licensed. This package contains original OpenAI-oriented instructions and workflow adaptations.
