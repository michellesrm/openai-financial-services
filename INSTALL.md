# Installation

## Fastest local install

This repository is both the plugin source and a Git-backed marketplace.

With current Codex CLI:

```bash
codex plugin marketplace add michellesrm/openai-financial-services --ref main
codex plugin marketplace list
```

Then use the ChatGPT desktop app's Plugins Directory to select the marketplace and install **Financial Services for OpenAI**. Restart/reload the client after changing local marketplace configuration.

The repository includes `.codex/config.toml` to enable `financial-services-workflows@financial-services` when the repository is trusted.

## Repository marketplace

The catalog lives at:

```
.agents/plugins/marketplace.json
```

It points to the Git repository root, where `plugin.json` is located. The plugin has no mandatory MCP server and therefore does not require financial-data credentials to install.

## Self-hosted/OpenAI agent environments

The plugin root can be placed in an environment capability directory or packaged with:

```bash
python scripts/package_plugin.py
```

The resulting ZIP is:

```
dist/financial-services-workflows.zip
```

For environments using the Codex compatibility manifest, `.codex-plugin/plugin.json` points to `./skills/`.

## Validate before installation

```bash
python scripts/validate_plugin.py
python scripts/test_routing.py
python scripts/package_plugin.py
```

GitHub Actions runs the same checks on every pull request and every push to `main`.

## Optional MCP providers

The core plugin is skills-only. `examples/mcp.providers.example.json` lists optional finance-data endpoints referenced by the upstream ecosystem. Do not enable providers you are not authorized to use. Authentication, subscriptions, permissions, and provider-specific review remain separate.

## Public OpenAI directory

Before public submission, provide production publisher metadata, privacy/support/terms URLs where required, review materials, and clean-environment test evidence. Public plugins are subject to OpenAI review.
