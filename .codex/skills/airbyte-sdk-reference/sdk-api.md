# Airbyte Agent SDK — Public API Reference

## Global Configuration

```python
import airbyte_agent_sdk

# Set global credentials (used as defaults by connect(), Workspace, ask())
airbyte_agent_sdk.configure(
    *,
    client_id: str,           # Airbyte OAuth client ID
    client_secret: str,       # Airbyte OAuth client secret
    organization_id: str | None = None,  # Multi-org routing
    workspace_name: str = "default",
)
# Calling again overwrites. Explicit kwargs to connect() take priority.
# Credential resolution order: explicit arg → configure() → env vars
```

**Environment variables** (fallback when `configure()` not called):
- `AIRBYTE_CLIENT_ID`
- `AIRBYTE_CLIENT_SECRET`
- `AIRBYTE_ORGANIZATION_ID`

## connect() — One-Call Factory

```python
from airbyte_agent_sdk import connect

connector = connect(
    connector_name: str,      # Slug, e.g. "stripe" or "zendesk-support"
    *,
    client_id: str | None = None,
    client_secret: str | None = None,
    workspace_name: str = "default",  # Workspace for connector lookup
    connector_id: str | None = None,  # Direct source ID (skips lookup)
    organization_id: str | None = None,
    auth_config: AirbyteAuthConfig | None = None,
)
# Returns typed connector (e.g. StripeConnector) if package installed,
# otherwise HostedExecutor. Always hosted mode.
# Raises ValueError if connector_name unknown or no credentials resolvable.
```

## list_connectors()

```python
from airbyte_agent_sdk import list_connectors

names: list[str] = list_connectors()
# Returns sorted list of all available connector slugs.
```

## AirbyteAuthConfig

```python
from airbyte_agent_sdk.types import AirbyteAuthConfig

auth = AirbyteAuthConfig(
    workspace_name: str | None = None,       # Aliases: customer_name, external_user_id
    organization_id: str | None = None,
    airbyte_client_id: str | None = None,    # Required for hosted mode
    airbyte_client_secret: str | None = None, # Required for hosted mode
    connector_id: str | None = None,          # Skips workspace lookup if set
)
```

## Connector Methods

### execute()

```python
result = await connector.execute(
    entity: str,              # e.g. "customers", "issues"
    action: str,              # "list", "get", "create", "update", "delete", "api_search"
    params: dict | None = None,
)
# List actions return envelope: result.data (list) + result.meta (has_more, etc.)
# Get/create/update/delete return raw dict.
# Raises RuntimeError on execution failure.
```

### check()

```python
check_result = await connector.check()
# Returns CheckResult with:
#   status: "healthy" | "unhealthy"
#   error: str | None
#   checked_entity: str | None
#   checked_action: str | None
```

### list_entities()

```python
entities = connector.list_entities()
# Returns list of dicts, each with:
#   entity_name: str
#   description: str | None
#   available_actions: list[str]
#   parameters: dict[str, list[dict]]  # action -> param list
```

### entity_schema()

```python
schema = connector.entity_schema("customers")
# Returns JSON schema dict for the entity, or None if not found.
```

**Note**: `list_entities()` and `entity_schema()` are only available on typed connectors, NOT on `HostedExecutor`.

## Connector.tool_utils — AI Framework Integration

`tool_utils` is a `@classmethod` on typed connector classes. It decorates a tool function to:
1. Append connector capabilities to the function's docstring (so the LLM knows what's available)
2. Guard output size and raise `pydantic_ai.ModelRetry` (or `RuntimeError`) if too large

```python
# Bare usage (all defaults):
@agent.tool_plain
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})

# Parameterized usage:
@agent.tool_plain
@StripeConnector.tool_utils(update_docstring=True, enable_hosted_mode_features=True, max_output_chars=50_000)
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

**Works with any framework decorator that reads the function signature and docstring** — PydanticAI's `@agent.tool_plain`, MCP's `@mcp.tool()`, and Anthropic's `@beta_tool` / `@beta_async_tool`. Stack the framework decorator on top and `tool_utils` underneath; the ENTITIES/ACTIONS/PARAMETERS block is appended to `__doc__` and flows into the tool description automatically.

```python
# Anthropic async SDK:
@beta_async_tool
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute a Stripe API operation."""
    return await connector.execute(entity, action, params or {})
```

**Options:**

| Parameter | Default | Effect |
|-----------|---------|--------|
| `update_docstring` | `True` | Appends entity/action/schema descriptions to `__doc__` |
| `enable_hosted_mode_features` | `True` | Includes context-store search guidance in docstring |
| `max_output_chars` | `100_000` | Max serialized output; `None` disables |

**Important**: `tool_utils` is NOT available on `HostedExecutor`. Always import the typed connector class.

## Package Naming

- **Install**: `uv pip install airbyte-agent-sdk` — one package ships every typed connector.
- **Recommended usage**: `from airbyte_agent_sdk import connect; stripe = connect("stripe")` returns a typed connector instance (e.g. `StripeConnector`).
- **Direct class import** (when you need the class itself, e.g. for `@Connector.tool_utils` without an instance): `from airbyte_agent_sdk.connectors.{name} import {Name}Connector`
  - Slug hyphens become underscores: `zendesk-support` → `airbyte_agent_sdk.connectors.zendesk_support`
  - Class name: PascalCase + "Connector": `ZendeskSupportConnector`
- `AirbyteAuthConfig` is importable from `airbyte_agent_sdk.types`.

## close()

```python
await connector.close()
# Release HTTP resources. Call when done with the connector.
```
