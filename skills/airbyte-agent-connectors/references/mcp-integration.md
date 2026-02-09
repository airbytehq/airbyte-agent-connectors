# MCP Integration

Model Context Protocol (MCP) enables AI assistants like Claude to interact with external tools and data sources. This guide covers setting up the Airbyte Agent MCP server for use with Claude Code and Claude Desktop.

## Contents

- [Overview](#overview)
- [MCP Server Location](#mcp-server-location)
- [Available MCP Tools](#available-mcp-tools)
- [Configuration](#configuration)
- [Claude Code Setup](#claude-code-setup)
- [Claude Desktop Setup](#claude-desktop-setup)
- [Running the Server Manually](#running-the-server-manually)
- [Example Usage with Claude](#example-usage-with-claude)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [Related Documentation](#related-documentation)

## Overview

The `airbyte-agent-mcp` server exposes Airbyte Agent Connectors as MCP tools, allowing Claude to:

- Discover available connectors
- Describe connector capabilities (entities, actions, parameters)
- Execute operations on any configured connector

## MCP Server Location

The MCP server is included in this repository:

```
airbyte-agent-connectors/
└── airbyte-agent-mcp/
    ├── airbyte_agent_mcp/         # Server implementation
    ├── configured_connectors.yaml.example
    ├── pyproject.toml
    └── README.md
```

## Available MCP Tools

### execute

Execute an operation on a configured connector.

```json
{
  "tool": "execute",
  "arguments": {
    "connector_id": "stripe",
    "entity": "customers",
    "action": "list",
    "params": {"limit": 10}
  }
}
```

**Parameters:**
- `connector_id` (required): ID of the configured connector
- `entity` (required): Entity to operate on (e.g., `customers`, `issues`)
- `action` (required): Action to perform (e.g., `list`, `get`, `create`)
- `params` (optional): Parameters for the operation

**Returns:** Operation result with data or error message.

### list_entities

List all available entities for a connector.

```json
{
  "tool": "list_entities",
  "arguments": {
    "connector_id": "github"
  }
}
```

**Returns:** Array of entity names with descriptions.

### describe_entity

Get detailed schema for an entity including available actions and parameters.

```json
{
  "tool": "describe_entity",
  "arguments": {
    "connector_id": "stripe",
    "entity": "customers"
  }
}
```

**Returns:** Entity schema with actions, parameters, and types.

### validate_operation

Check if an operation is valid before executing.

```json
{
  "tool": "validate_operation",
  "arguments": {
    "connector_id": "stripe",
    "entity": "customers",
    "action": "get",
    "params": {"id": "cus_xxx"}
  }
}
```

**Returns:** Validation result with any errors.

## Configuration

### Step 1: Create configured_connectors.yaml

Copy the example and customize:

```bash
cd airbyte-agent-mcp
cp configured_connectors.yaml.example configured_connectors.yaml
```

Edit `configured_connectors.yaml`:

```yaml
connectors:
  # Stripe - API Key authentication
  - id: stripe
    type: local
    connector_name: stripe
    description: "Stripe payment processing"
    secrets:
      api_key: STRIPE_API_KEY

  # GitHub - Personal Access Token
  - id: github
    type: local
    connector_name: github
    description: "GitHub repositories and issues"
    secrets:
      token: GITHUB_ACCESS_TOKEN

  # Salesforce - OAuth
  - id: salesforce
    type: local
    connector_name: salesforce
    description: "Salesforce CRM"
    secrets:
      client_id: SALESFORCE_CLIENT_ID
      client_secret: SALESFORCE_CLIENT_SECRET
      refresh_token: SALESFORCE_REFRESH_TOKEN

  # HubSpot - Private App
  - id: hubspot
    type: local
    connector_name: hubspot
    description: "HubSpot CRM and marketing"
    secrets:
      access_token: HUBSPOT_ACCESS_TOKEN

  # Slack - Bot Token
  - id: slack
    type: local
    connector_name: slack
    description: "Slack messaging"
    secrets:
      token: SLACK_BOT_TOKEN
```

### Step 2: Create .env File

Create `.env` in the `airbyte-agent-mcp` directory (no template provided, create from scratch):

```bash
# Stripe
STRIPE_API_KEY=sk_live_your_key_here

# GitHub
GITHUB_ACCESS_TOKEN=ghp_your_token_here

# Salesforce
SALESFORCE_CLIENT_ID=your_client_id
SALESFORCE_CLIENT_SECRET=your_client_secret
SALESFORCE_REFRESH_TOKEN=your_refresh_token

# HubSpot
HUBSPOT_ACCESS_TOKEN=pat-na1-xxx

# Slack
SLACK_BOT_TOKEN=xoxb-your-token
```

### Configuration Options

#### Loading from Registry (Recommended)

```yaml
- id: stripe
  type: local
  connector_name: stripe  # Loads from Airbyte registry
  secrets:
    api_key: STRIPE_API_KEY
```

#### Pinning to Specific Version

```yaml
- id: stripe
  type: local
  connector_name: stripe
  version: 0.1.6  # Pin to specific version
  secrets:
    api_key: STRIPE_API_KEY
```

#### Loading from Local Path

```yaml
- id: my_api
  type: local
  path: ./connectors/my-api/connector.yaml  # Local file path
  secrets:
    token: MY_API_KEY
```

#### Multi-Auth Connectors

For connectors with multiple auth methods, specify the scheme:

```yaml
# Zendesk with OAuth
- id: zendesk-oauth
  type: local
  connector_name: zendesk-support
  auth_scheme: zendeskOAuth
  config_values:
    subdomain: yourcompany
  secrets:
    access_token: ZENDESK_ACCESS_TOKEN

# Zendesk with API Token
- id: zendesk-api
  type: local
  connector_name: zendesk-support
  auth_scheme: zendeskAPIToken
  config_values:
    subdomain: yourcompany
  secrets:
    email: ZENDESK_EMAIL
    api_token: ZENDESK_API_TOKEN
```

## Claude Code Setup

### Option 1: Project-Scoped (Recommended)

Add the MCP server to your project:

```bash
cd /path/to/your/project
claude mcp add airbyte-agent-mcp --scope project
```

When prompted, provide the server configuration:

```json
{
  "command": "uv",
  "args": [
    "--directory",
    "/path/to/airbyte-agent-connectors/airbyte-agent-mcp",
    "run",
    "airbyte_agent_mcp"
  ]
}
```

### Option 2: Global Configuration

Add to `~/.claude.json`:

```json
{
  "mcpServers": {
    "airbyte-agent-mcp": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/airbyte-agent-connectors/airbyte-agent-mcp",
        "run",
        "airbyte_agent_mcp"
      ],
      "env": {}
    }
  }
}
```

### Option 3: With Custom Paths

If your config files are in different locations:

```json
{
  "mcpServers": {
    "airbyte-agent-mcp": {
      "type": "stdio",
      "command": "python",
      "args": [
        "-m",
        "airbyte_agent_mcp",
        "/path/to/configured_connectors.yaml",
        "/path/to/.env"
      ],
      "cwd": "/path/to/airbyte-agent-connectors/airbyte-agent-mcp"
    }
  }
}
```

## Claude Desktop Setup

Add to your Claude Desktop configuration file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "airbyte-agent-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/airbyte-agent-connectors/airbyte-agent-mcp",
        "run",
        "airbyte_agent_mcp"
      ]
    }
  }
}
```

Restart Claude Desktop after making changes.

## Running the Server Manually

For testing or development:

```bash
cd airbyte-agent-connectors/airbyte-agent-mcp

# Install dependencies
uv sync

# Run the server
uv run airbyte_agent_mcp
```

With custom paths:

```bash
uv run python -m airbyte_agent_mcp /path/to/config.yaml /path/to/.env
```

## Example Usage with Claude

Once configured, you can ask Claude to interact with your connectors. Here are example conversations showing how Claude uses the MCP tools.

### Discovering Available Connectors

**You:** "What connectors are available?"

**Claude:** *Uses list_entities tool to discover configured connectors*

> I can see you have the following connectors configured:
> - **stripe** - Stripe payment processing
> - **github** - GitHub repositories and issues
> - **hubspot** - HubSpot CRM and marketing

### Exploring Connector Capabilities

**You:** "What can I do with the Stripe connector?"

**Claude:** *Uses describe_entity tool for each entity*

> The Stripe connector supports these entities and actions:
>
> **customers**
> - `list` - List all customers (params: limit, starting_after)
> - `get` - Get customer by ID (params: id)
> - `create` - Create new customer (params: email, name, metadata)
> - `api_search` - Search customers (params: query)
>
> **invoices**
> - `list` - List invoices (params: limit, customer)
> - `get` - Get invoice by ID (params: id)
>
> Would you like me to perform any of these operations?

### Executing Operations

**You:** "List my top 10 Stripe customers"

**Claude:** *Uses execute tool*

```json
{
  "tool": "execute",
  "arguments": {
    "connector_id": "stripe",
    "entity": "customers",
    "action": "list",
    "params": {"limit": 10}
  }
}
```

> Here are your top 10 Stripe customers:
> 1. Jane Smith (jane@example.com) - Created Jan 15, 2024
> 2. Acme Corp (billing@acme.com) - Created Jan 10, 2024
> ...

### Using Validation Before Execution

**You:** "Search for customers with email containing 'acme'"

**Claude:** *Uses validate_operation first, then execute*

```json
{
  "tool": "validate_operation",
  "arguments": {
    "connector_id": "stripe",
    "entity": "customers",
    "action": "api_search",
    "params": {"query": "email~'acme'"}
  }
}
```

> Validation passed. Executing search...

### Multi-Connector Workflows

**You:** "Find GitHub issues labeled 'bug' and check if they have matching Jira tickets"

**Claude:** *Uses execute on github connector, then jira connector*

> I found 5 GitHub issues labeled 'bug':
> 1. #123 - Login timeout issue
> 2. #124 - Dashboard not loading
> ...
>
> Checking Jira for matching tickets...
> - #123 matches PROJ-456 (In Progress)
> - #124 has no matching Jira ticket

### Common Prompts

| Task | Example Prompt |
|------|----------------|
| Discovery | "What connectors do I have?" |
| Explore | "What entities are in the GitHub connector?" |
| List | "Show me recent Stripe invoices" |
| Get | "Get details for GitHub issue #42 in org/repo" |
| Search | "Find Salesforce contacts in California" |
| Multi-step | "List HubSpot deals over $10k and find related Stripe customers" |

## Troubleshooting

### Server Not Starting

1. **Check Python/uv installation:**
   ```bash
   uv --version
   python --version
   ```

2. **Verify paths in configuration:**
   - Ensure the `--directory` path points to `airbyte-agent-mcp`
   - Check that `configured_connectors.yaml` exists

3. **Check for syntax errors:**
   ```bash
   cd airbyte-agent-mcp
   uv run python -c "import yaml; yaml.safe_load(open('configured_connectors.yaml'))"
   ```

### Connection Errors

1. **Environment variables not loaded:**
   - Ensure `.env` file exists in `airbyte-agent-mcp` directory
   - Check variable names match those in `configured_connectors.yaml`

2. **Invalid credentials:**
   - Verify API keys are valid and not expired
   - Check OAuth tokens haven't expired

### Tool Execution Failures

1. **Entity not found:**
   - Use `list_entities` to see available entities
   - Check spelling and case sensitivity

2. **Missing parameters:**
   - Use `describe_entity` to see required parameters
   - Ensure all required fields are provided

## Development

### Running Tests

```bash
cd airbyte-agent-mcp
uv sync --all-extras
uv run pytest
```

### Code Formatting

```bash
uv run ruff format .
uv run ruff check .
```

### Adding a New Connector

1. Add connector to `configured_connectors.yaml`:
   ```yaml
   - id: new_connector
     type: local
     connector_name: new-connector
     secrets:
       token: NEW_CONNECTOR_TOKEN
   ```

2. Add credentials to `.env`:
   ```bash
   NEW_CONNECTOR_TOKEN=your_token
   ```

3. Restart the MCP server

## Related Documentation

- [Getting Started](./getting-started.md) - Install and configure connectors
- [Entity-Action API](./entity-action-api.md) - Understand the API patterns
- [Authentication](./authentication.md) - Set up credentials
- [Troubleshooting](./troubleshooting.md) - Common issues and solutions
- [airbyte-agent-mcp README](../airbyte-agent-mcp/README.md) - Server-specific documentation
