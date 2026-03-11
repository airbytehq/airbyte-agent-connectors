<!-- AUTO-GENERATED from connectors/monday/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Monday

The Monday agent connector is a Python package that equips AI agents to interact with Monday through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-monday` v0.1.7
- **Auth:** OAuth, Token
- **Docs:** [Official API docs](https://developer.monday.com/api-reference/docs)
- **Status:** complete

## Example Prompts

- List all users in the Monday.com account
- Show me all boards
- Get the details of board 18395979459
- List all teams
- Show me all tags
- List recent updates
- Which boards were updated in the last week?
- Find all items assigned to a specific group
- What are the most active boards by update count?
- Show me all users who are admins
- List items with their column values from a specific board

## Unsupported

- Create a new board
- Delete an item
- Update a column value
- Add a new user to the account
- Create a webhook subscription

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-monday
```

### OSS Mode

```python
from airbyte_agent_monday import MondayConnector
from airbyte_agent_monday.models import MondayApiTokenAuthenticationAuthConfig

connector = MondayConnector(
    auth_config=MondayApiTokenAuthenticationAuthConfig(
        api_key="<Your Monday.com personal API token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@MondayConnector.tool_utils
async def monday_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_monday import MondayConnector, AirbyteAuthConfig

connector = MondayConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@MondayConnector.tool_utils
async def monday_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Users | List, Get, Search |
| Boards | List, Get, Search |
| Items | List, Get, Search |
| Teams | List, Get, Search |
| Tags | List, Search |
| Updates | List, Get, Search |
| Workspaces | List, Get, Search |
| Activity Logs | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/monday/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/monday/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/monday)*
