<!-- AUTO-GENERATED from connectors/asana/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Asana

The Asana agent connector is a Python package that equips AI agents to interact with Asana through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-asana` v0.19.118
- **Auth:** OAuth, Token
- **Docs:** [Official API docs](https://developers.asana.com/reference/rest-api-reference)
- **Status:** complete

## Example Prompts

- What tasks are assigned to me this week?
- List all projects in my workspace
- Show me the tasks for a recent project
- Who are the team members in one of my teams?
- Show me details of my current workspace and its users
- Summarize my team's workload and task completion rates
- Find all tasks related to \{client_name\} across my workspaces
- Analyze the most active projects in my workspace last month
- Compare task completion rates between my different teams
- Identify overdue tasks across all my projects

## Unsupported

- Create a new task for [TeamMember]
- Update the priority of this task
- Delete the project [ProjectName]
- Schedule a new team meeting
- Add a new team member to [Workspace]
- Move this task to another project

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-asana
```

### OSS Mode

```python
from airbyte_agent_asana import AsanaConnector
from airbyte_agent_asana.models import AsanaPersonalAccessTokenAuthConfig

connector = AsanaConnector(
    auth_config=AsanaPersonalAccessTokenAuthConfig(
        token="<Your Asana Personal Access Token. Generate one at https://app.asana.com/0/my-apps>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AsanaConnector.tool_utils
async def asana_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_asana import AsanaConnector, AirbyteAuthConfig

connector = AsanaConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AsanaConnector.tool_utils
async def asana_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Tasks | List, Get, Search |
| Project Tasks | List |
| Workspace Task Search | List |
| Projects | List, Get, Search |
| Task Projects | List |
| Team Projects | List |
| Workspace Projects | List |
| Workspaces | List, Get, Search |
| Users | List, Get, Search |
| Workspace Users | List |
| Team Users | List |
| Teams | Get, Search |
| Workspace Teams | List |
| User Teams | List |
| Attachments | List, Get, Download, Search |
| Workspace Tags | List |
| Tags | Get, Search |
| Project Sections | List |
| Sections | Get, Search |
| Task Subtasks | List |
| Task Dependencies | List |
| Task Dependents | List |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/asana/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/asana/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/asana)*
