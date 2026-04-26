# Airbyte Agent SDK

Type-safe connector execution framework with blessed connectors and full IDE autocomplete.

## Overview

The Airbyte Agent SDK gives AI agents access to 50+ third-party APIs through strongly typed, well-documented tools. Connectors can run through the Airbyte platform (which manages credentials, rate limiting, and execution) or locally in OSS mode.

## How to install

```bash
uv pip install airbyte-agent-sdk
```

## CLI Quickstart

The `airbyte-agent-sdk` console script ships seven subcommands:

```bash
uv run airbyte-agent-sdk --help
```

```bash
uv run airbyte-agent-sdk annotate --help
```

```bash
uv run airbyte-agent-sdk cassette --help
```

```bash
uv run airbyte-agent-sdk connector --help
```

```bash
uv run airbyte-agent-sdk generate-docs --help
```

```bash
uv run airbyte-agent-sdk generate-sdk --help
```

```bash
uv run airbyte-agent-sdk test --help
```

```bash
uv run airbyte-agent-sdk validate --help
```

## Documentation

Full documentation is available at [docs.airbyte.com/ai-agents/about/](https://docs.airbyte.com/ai-agents/about/).

## How to install the skills

The repo ships skills that walk agents through setting up and using the connectors. Three install paths:

**skills.sh** (works for Claude Code, Codex, Cursor, OpenCode, and 40+ other agents):

```bash
npx skills add airbytehq/airbyte-agent-sdk
```

**Claude Code** (native plugin):

```
/plugin marketplace add airbytehq/airbyte-agent-sdk
/plugin install airbyte-agent-sdk@airbyte-agent-sdk
```

**Codex** (clone + symlink):

```bash
git clone https://github.com/airbytehq/airbyte-agent-sdk ~/.codex/skills/airbyte-agent-sdk-src
ln -s ~/.codex/skills/airbyte-agent-sdk-src/connector-sdk/.claude/skills/* ~/.codex/skills/
```

See [docs.airbyte.com/ai-agents/about/](https://docs.airbyte.com/ai-agents/about/) for full documentation.
