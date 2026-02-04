# Airbyte MCP Server

Connect AI assistants to a growing catalog of data sources through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

This project provides an MCP server that exposes [Airbyte](https://airbyte.com/) connectors as tools, enabling AI assistants like Claude to interact with your data sources directly.

## Features

- **Growing Connector Catalog**: Access any Airbyte connector (Salesforce, HubSpot, Stripe, databases, and more)
- **Two Execution Modes**:
  - **Local Mode**: Direct API calls using your credentials
  - **Cloud Mode**: Execute through Airbyte Cloud for managed infrastructure
- **IDE Integration**: One-command setup for Claude Code, Claude Desktop, Cursor, and Codex

## Quick Start

1. **List available connectors**:

```bash
uv run adp connectors list
```

2. **Generate a connector configuration** (e.g., Gong):

```bash
uv run adp connectors configure --package airbyte-agent-gong -o connector-config.yaml
```

3. **Set your credentials** in `.env`:

```bash
GONG_ACCESS_KEY=your-access-key
GONG_ACCESS_KEY_SECRET=your-secret
```

4. **Register with Claude Code**:

```bash
uv run adp mcp add-to claude-code connector-config.yaml
```

5. **Restart Claude Code** and start using your connector!

For **Claude Desktop**, use `add-to claude-desktop` instead in step 4. For **Cursor**, use `add-to cursor`.

## Configuration

### Local Mode (Direct API Access)

For local execution with your own credentials. This mode calls the data source API directly and only supports operations that the API provides (e.g., list, get by ID). 

Arbitrary search/filter queries are not supported unless the underlying API supports them.

```yaml
connector:
  type: package
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
  type: cloud
  connector_id: <connector-id>
credentials:
  airbyte_external_user_id: ${env.AIRBYTE_EXTERNAL_USER_ID}
  airbyte_client_id: ${env.AIRBYTE_CLIENT_ID}
  airbyte_client_secret: ${env.AIRBYTE_CLIENT_SECRET}
```

### Local Development

For testing with a local connector (pass a local path as the package):

```yaml
connector:
  type: package
  package: /path/to/your/connector
credentials:
  # connector-specific credentials
```

## CLI Commands

All commands are run with `uv run adp <command>`.

### Connector Commands

```bash
# List available connectors
uv run adp connectors list

# Filter by name
uv run adp connectors list --pattern salesforce

# Generate configuration for a package connector
uv run adp connectors configure --package airbyte-agent-gong -o connector-config.yaml

# Configure with specific version
uv run adp connectors configure --package airbyte-agent-gong --version 0.1.13 -o connector-config.yaml

# Generate configuration for an Airbyte Cloud connector (using connector ID)
uv run adp connectors configure --connector-id <connector-id> -o connector-config.yaml

# Configure a local connector (pass a local path as --package)
uv run adp connectors configure --package /path/to/connector -o connector-config.yaml
```

### Cloud Commands

Manage Airbyte Cloud resources. Requires `AIRBYTE_CLIENT_ID` and `AIRBYTE_CLIENT_SECRET` environment variables.

```bash
# List workspaces
uv run adp cloud workspaces list

# List cloud connector sources for a workspace
uv run adp cloud connectors list --workspace-id <workspace-id>

# Get details for a cloud connector source
uv run adp cloud connectors get <connector-id>
```

### MCP Server Commands

```bash
# Start with stdio transport (default, for Claude Code/Desktop)
uv run adp mcp serve connector-config.yaml

# Start with HTTP transport
uv run adp mcp serve connector-config.yaml --transport http --port 8080

# Start with SSE transport
uv run adp mcp serve connector-config.yaml --transport sse --port 8080
```

### Chat Commands

Chat with your connector data using natural language, powered by Claude. Supports two modes:

```bash
# One-shot: pass a prompt and get a single answer (great for piping)
uv run adp chat connector-config.yaml "show me 5 users"

# Interactive REPL: omit the prompt for a conversation loop
uv run adp chat connector-config.yaml

# Options
uv run adp chat connector-config.yaml --model claude-opus-4-20250514
uv run adp chat connector-config.yaml "list recent calls" --quiet  # hide tool call details
```

In one-shot mode, tool call progress goes to stderr and the final answer to stdout, so you can pipe the output: `uv run adp chat connector-config.yaml "summarize calls" > summary.md`.

Requires the `ANTHROPIC_API_KEY` environment variable to be set.

### IDE Integration Commands

```bash
# Register with Claude Code (user scope)
uv run adp mcp add-to claude-code connector-config.yaml

# Register with Claude Code (project scope, for team sharing)
uv run adp mcp add-to claude-code connector-config.yaml --scope project

# Register with Claude Desktop
uv run adp mcp add-to claude-desktop connector-config.yaml

# Register with Cursor (user scope)
uv run adp mcp add-to cursor connector-config.yaml

# Register with Cursor (project scope)
uv run adp mcp add-to cursor connector-config.yaml --scope project

# Register with OpenAI Codex CLI
uv run adp mcp add-to codex connector-config.yaml

# Custom server name (works with all commands)
uv run adp mcp add-to claude-code connector-config.yaml --name my-gong-server
```

## MCP Tools

When running, the server exposes the following tools:

| Tool | Description |
|------|-------------|
| `current_datetime` | Get the current date and time in UTC |
| `get_instructions` | Get best-practice rules for action selection, filtering, and field selection |
| `connector_info` | Get connector metadata, version, and available entities/actions |
| `execute` | Execute operations on entities (list, get, search, etc.) |
| `entity_schema` | Get JSON schema for a specific entity |

### Example Usage in Claude

Once configured, you can ask Claude things like:

- "List all users from Gong"
- "Get the details of call ID abc123"
- "Search for calls from last week"
- "What entities are available in this connector?"

## Available Connectors

Airbyte connectors are published as separate packages with the naming convention `airbyte-agent-<name>`. Some popular ones:

| Connector | Package | Description |
|-----------|---------|-------------|
| Gong | `airbyte-agent-gong` | Sales conversation intelligence |
| Salesforce | `airbyte-agent-salesforce` | CRM platform |
| HubSpot | `airbyte-agent-hubspot` | Marketing & sales platform |
| Stripe | `airbyte-agent-stripe` | Payment processing |
| GitHub | `airbyte-agent-github` | Code collaboration |

Find more connectors:

```bash
uv run adp connectors list
```

## Environment Variables

Credentials support environment variable interpolation using `${env.VAR_NAME}` syntax:

```yaml
credentials:
  api_key: ${env.MY_API_KEY}
  secret: ${env.MY_SECRET}
```

Create a `.env` file in your project root:

```bash
MY_API_KEY=your-key
MY_SECRET=your-secret
```

The CLI automatically loads `.env` files.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/airbytehq/airbyte-agent-connectors.git
cd airbyte-agent-connectors

# Install dependencies
uv sync --group dev
```

### Running Tests

```bash
uv run poe test
```

### Code Style

```bash
# Format and lint
uv run poe check

# Auto-format
uv run poe format
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Links

- [Airbyte](https://airbyte.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Claude Code](https://claude.ai/code)
- [Airbyte Connectors](https://docs.airbyte.com/integrations/)

## Support

- [GitHub Issues](https://github.com/airbytehq/airbyte-agent-connectors/issues)
- [Airbyte Community Slack](https://airbyte.com/community)
