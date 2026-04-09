<!-- AUTO-GENERATED from connectors/clickup-api/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-04-09 -->

# Clickup Api

The Clickup-Api agent connector is a Python package that equips AI agents to interact with Clickup-Api through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-clickup-api` v0.1.18
- **Auth:** Token
- **Docs:** [Official API docs](https://developer.clickup.com/reference)
- **Status:** complete

## Example Prompts

- List all workspaces I have access to
- Show me the spaces in my workspace
- List the folders in a space
- Show me the lists in a folder
- Get the tasks in a list
- Get details for a specific task
- Search for tasks containing 'bug' across my workspace
- Find all urgent priority tasks in my workspace
- Show me tasks assigned to a specific user
- List comments on a task
- Get threaded replies on a comment
- Create a comment on a task
- Update a comment to mark it resolved
- List all goals in my workspace
- Get details for a specific goal
- Show me all workspace-level views
- Get tasks matching a saved view
- List time entries for my workspace this week
- Get details for a specific time entry
- Show me the members assigned to a task
- List all docs in my workspace
- Get details for a specific doc
- What tasks are overdue in my workspace?
- Which tasks were updated in the last 24 hours?
- Show me all high-priority tasks across all projects
- How much time has been tracked this week?
- What are the most commented tasks?

## Unsupported

- Delete a task
- Delete a comment
- Delete a goal

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-clickup-api
```

### OSS Mode

```python
from airbyte_agent_clickup_api import ClickupApiConnector
from airbyte_agent_clickup_api.models import ClickupApiAuthConfig

connector = ClickupApiConnector(
    auth_config=ClickupApiAuthConfig(
        api_key="<Your ClickUp personal API token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ClickupApiConnector.tool_utils
async def clickup_api_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_clickup_api import ClickupApiConnector, AirbyteAuthConfig

connector = ClickupApiConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ClickupApiConnector.tool_utils
async def clickup_api_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| User | Get |
| Teams | List |
| Spaces | List, Get |
| Folders | List, Get |
| Lists | List, Get |
| Tasks | List, Get, API Search |
| Comments | List, Create, Get, Update |
| Goals | List, Get |
| Views | List, Get |
| View Tasks | List |
| Time Tracking | List, Get |
| Members | List |
| Docs | List, Get |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/clickup-api/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/clickup-api/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/clickup-api)*
