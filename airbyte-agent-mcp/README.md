# Airbyte MCP Server

Connect AI assistants to a growing catalog of data sources through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

This project provides an MCP server that exposes [Airbyte](https://airbyte.com/) connectors as tools, enabling AI assistants like Claude, Cursor, and Codex to interact with your data sources directly.

## Features

- **Growing Connector Catalog**: Access any Airbyte connector (Salesforce, HubSpot, Stripe, databases, and more)
- **Two Execution Modes**:
  - **Local Mode**: Direct API calls using your credentials
  - **Cloud Mode**: Execute through Airbyte Cloud for managed infrastructure
- **AI Tool Integration**: One-command setup for Claude Code, Claude Desktop, Cursor, and Codex

## Quick Start

1. **List available connectors**:

```bash
uv run adp connectors list-oss
```

2. **Generate a connector configuration** (e.g., Gong):

```bash
uv run adp connectors configure --package airbyte-agent-gong
```

3. **Set your connector credentials** in `.env`:

```bash
GONG_ACCESS_KEY=your-access-key
GONG_ACCESS_KEY_SECRET=your-secret
```

4. **Register with your AI tool**:

```bash
# Claude Code
uv run adp mcp add-to claude-code connector-gong-package.yaml

# Claude Desktop
uv run adp mcp add-to claude-desktop connector-gong-package.yaml

# Cursor
uv run adp mcp add-to cursor connector-gong-package.yaml

# OpenAI Codex
uv run adp mcp add-to codex connector-gong-package.yaml
```

5. **Restart your AI tool** and start asking questions like "List all users from Gong" or "Search for calls from last week".

## Configuration

### Local Mode (Direct API Access)

For local execution with your own credentials. This mode calls the data source API directly and only supports operations that the API provides (e.g., list, get by ID).

> **Info:** Arbitrary search/filter queries are not supported unless the underlying API supports them.

```yaml
connector:
  package: airbyte-agent-gong
  version: 0.1.13  # optional, defaults to latest
credentials:
  access_key: ${env.GONG_ACCESS_KEY}
  access_key_secret: ${env.GONG_ACCESS_KEY_SECRET}
```

### Cloud Mode (Airbyte Cloud)

For execution through Airbyte Cloud. This mode supports arbitrary search and filter queries across all entities, as data is kept up to date and indexed in Airbyte's infrastructure.

```yaml
connector:
  connector_id: <connector-id>
credentials:
  airbyte_client_id: ${env.AIRBYTE_CLIENT_ID}
  airbyte_client_secret: ${env.AIRBYTE_CLIENT_SECRET}
```

Credentials use `${env.VAR_NAME}` syntax and are resolved from `.env` files, which the CLI loads automatically.

You can also point the connector to a local path or a git repository — run `uv run adp connectors configure --help` for all options.

## CLI Commands

All commands are run with `uv run adp <command>`. Use `--help` on any command for full options.

### Login

Save your Airbyte Cloud credentials so they are available to all commands without a local `.env` file:

```bash
uv run adp login <organization-id>
```

This prints a link to the Airbyte authentication page for your organization where you can find your Client ID and Secret, then prompts for both values. Credentials are written to `~/.airbyte_agent_mcp/orgs/<organization-id>/.env` and the organization is set as the default.

You can log into multiple organizations and switch between them:

```bash
uv run adp orgs list              # List logged-in organizations
uv run adp orgs default org-xyz   # Switch default organization
uv run adp --org org-abc <cmd>    # Override for a single command
```

### Connectors

```bash
# List available connectors
uv run adp connectors list-oss
uv run adp connectors list-oss --pattern salesforce

# List cloud connectors
uv run adp connectors list-cloud
uv run adp connectors list-cloud --customer acme

# Generate a connector configuration
uv run adp connectors configure --package airbyte-agent-gong
uv run adp connectors configure --connector-id <id>
```

### MCP Server

```bash
# Start with stdio transport (default)
uv run adp mcp serve connector-gong-package.yaml

# Start with HTTP transport
uv run adp mcp serve connector-gong-package.yaml --transport http --port 8080

# Register with an AI tool
uv run adp mcp add-to claude-code connector-gong-package.yaml
```

### Chat

Chat with your connector data using natural language, powered by Claude. Requires `ANTHROPIC_API_KEY`.

```bash
# One-shot mode (great for piping)
uv run adp chat connector-gong-package.yaml "show me 5 users"

# Interactive REPL
uv run adp chat connector-gong-package.yaml
```

## Development

```bash
# Install dependencies
uv sync --group dev

# Run tests
uv run poe test

# Format and lint
uv run poe format
uv run poe check
```

## Links

- [Airbyte](https://airbyte.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Claude Code](https://claude.ai/code)
- [GitHub Issues](https://github.com/airbytehq/airbyte-agent-connectors/issues)
- [Airbyte Community Slack](https://airbyte.com/community)
