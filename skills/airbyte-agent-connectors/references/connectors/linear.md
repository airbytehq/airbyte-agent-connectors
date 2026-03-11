<!-- AUTO-GENERATED from connectors/linear/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Linear

The Linear agent connector is a Python package that equips AI agents to interact with Linear through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-linear` v0.19.112
- **Auth:** Token
- **Docs:** [Official API docs](https://linear.app/developers/graphql)
- **Status:** complete

## Example Prompts

- Show me the open issues assigned to my team this week
- List out all projects I'm currently involved in
- List all users in my Linear workspace
- Who is assigned to the most recently updated issue?
- Create a new issue titled 'Fix login bug'
- Update the priority of a recent issue to urgent
- Change the title of a recent issue to 'Updated feature request'
- Add a comment to a recent issue saying 'This is ready for review'
- Update my most recent comment to say 'Revised feedback after testing'
- Create a high priority issue about API performance
- Assign a recent issue to a teammate
- Unassign the current assignee from a recent issue
- Reassign a recent issue from one teammate to another
- Analyze the workload distribution across my development team
- What are the top priority issues in our current sprint?
- Identify the most active projects in our organization right now
- Summarize the recent issues for \{team_member\} in the last two weeks
- Compare the issue complexity across different teams
- Which projects have the most unresolved issues?
- Give me an overview of my team's current project backlog

## Unsupported

- Delete an outdated project from our workspace
- Schedule a sprint planning meeting
- Delete this issue
- Remove a comment from an issue

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-linear
```

### OSS Mode

```python
from airbyte_agent_linear import LinearConnector
from airbyte_agent_linear.models import LinearAuthConfig

connector = LinearConnector(
    auth_config=LinearAuthConfig(
        api_key="<Your Linear API key from Settings > API > Personal API keys>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@LinearConnector.tool_utils
async def linear_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_linear import LinearConnector, AirbyteAuthConfig

connector = LinearConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@LinearConnector.tool_utils
async def linear_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Issues | List, Get, Create, Update, Search |
| Projects | List, Get, Search |
| Teams | List, Get, Search |
| Users | List, Get, Search |
| Comments | List, Get, Create, Update, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/linear/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/linear/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/linear)*
