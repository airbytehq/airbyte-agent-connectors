<!-- AUTO-GENERATED from connectors/granola/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Granola

The Granola agent connector is a Python package that equips AI agents to interact with Granola through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-granola` v0.1.13
- **Auth:** Token
- **Docs:** [Official API docs](https://docs.granola.ai/introduction)
- **Status:** complete

## Example Prompts

- List all meeting notes from Granola
- Show me recent meeting notes
- Get the details of a specific note
- List notes created in the last week
- Find meeting notes from last month
- Which meetings had the most attendees?
- Show me notes that mention budget reviews
- What meetings happened this quarter?

## Unsupported

- Create a new meeting note
- Delete a meeting note
- Update an existing note
- Share a note with someone

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-granola
```

### OSS Mode

```python
from airbyte_agent_granola import GranolaConnector
from airbyte_agent_granola.models import GranolaAuthConfig

connector = GranolaConnector(
    auth_config=GranolaAuthConfig(
        api_key="<Granola Enterprise API key generated from Settings > Workspaces > API tab>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GranolaConnector.tool_utils
async def granola_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_granola import GranolaConnector, AirbyteAuthConfig

connector = GranolaConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GranolaConnector.tool_utils
async def granola_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Notes | List, Get, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/granola/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/granola/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/granola)*
