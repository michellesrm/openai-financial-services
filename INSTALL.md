# Installation notes

## ChatGPT and Codex local development

The recommended package entry point is `plugin.json`. OpenAI also supports the included `.codex-plugin/plugin.json` compatibility manifest.

For a repository-scoped local marketplace, create `.agents/plugins/marketplace.json` in your repo and point its plugin source path at this folder. For a personal marketplace, use the location documented by the current OpenAI plugin documentation. Restart/reload the relevant client after changing a local marketplace.

## Public directory

Before submission, replace `Local Developer` with your verified developer identity and add production website, support, privacy, terms, icons/screenshots, review materials, and any required authentication details. Public publication requires OpenAI review.

## Optional MCP providers

Do not rename `examples/mcp.providers.example.json` to `mcp.json` wholesale unless you intend to configure and use every listed provider. Copy only authorized providers into a root `mcp.json`, then configure provider-required authentication. A plugin containing remote MCP servers has additional review and deployment requirements.
