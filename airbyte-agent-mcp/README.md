# Airbyte Agent MCP Server

MCP server that exposes the Airbyte Connector SDK as Model Context Protocol tools.

## Features

- **Execute**: Run operations on any connector (primary tool)
- **List Entities**: Discover available entities in a connector
- **Describe Entity**: Get detailed schema for an entity
- **Validate Operation**: Check parameters before execution

## Configuration

### 1. Create configured_connectors.yaml

```yaml
# Connector definitions
connectors:
  # Load connector from the Airbyte registry (recommended)
  - id: stripe
    type: local
    connector_name: stripe
    description: "My Stripe API connector"
    secrets:
      token: STRIPE_API_KEY
```

You can pin to a specific version from the registry:

```yaml
connectors:
  - id: stripe
    type: local
    connector_name: stripe
    version: 0.1.0
    description: "Stripe connector pinned to v0.1.0"
    secrets:
      token: STRIPE_API_KEY
```

You can also load connectors from a local file path (version pinning not supported):

```yaml
connectors:
  - id: my_api
    type: local
    path: ./connectors/my-api/connector.yaml
    description: "My custom API connector"
    secrets:
      token: MY_API_KEY
```

See `configured_connectors.yaml.example` for more examples.

### 2. Create .env file

```bash
STRIPE_API_KEY=sk_test_your_stripe_api_key_here
```

## Running

```bash
uv run airbyte_agent_mcp
```

The server also takes in args for specific paths to the configured_connectors.yaml file and the env file. With custom paths:

```bash
python -m airbyte_agent_mcp path/to/configured_connectors.yaml path/to/.env
```

The default paths are `./configured_connectors.yaml` and `./.env`

## Usage with Claude Code

Add to `~/.claude.json`:

```json
"mcpServers": {
  "airbyte-agent-mcp": {
    "type": "stdio",
    "command": "uv",
    "args": [
      "--directory",
      "/path/to/sonar/airbyte-agent-mcp",
      "run",
      "airbyte_agent_mcp"
    ],
    "env": {}
  }
},
```

## Development / Testing

```bash
# Install dev dependencies
uv sync --all-extras

# Run tests
uv run pytest

# Format code
uv run ruff format .

# Lint code
uv run ruff check .
```
