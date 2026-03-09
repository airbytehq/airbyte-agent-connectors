<!-- AUTO-GENERATED from connectors/harvest/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Harvest

The Harvest agent connector is a Python package that equips AI agents to interact with Harvest through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-harvest` v0.1.0
- **Auth:** OAuth, Token
- **Docs:** [Official API docs](https://help.getharvest.com/api-v2/)
- **Status:** complete

## Example Prompts

- List all users in Harvest
- Show me all active projects
- List all clients
- Show me recent time entries
- List all invoices
- Show me all tasks
- List all expense categories
- Get company information
- How many hours were logged last week?
- Which projects have the most time entries?
- Show me all unbilled time entries
- What are the active projects for a specific client?
- List all overdue invoices
- Which users logged the most hours this month?

## Unsupported

- Create a new time entry in Harvest
- Update a project budget
- Delete an invoice
- Start a timer for a task

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-harvest
```

### OSS Mode

```python
from airbyte_agent_harvest import HarvestConnector
from airbyte_agent_harvest.models import HarvestPersonalAccessTokenAuthConfig

connector = HarvestConnector(
    auth_config=HarvestPersonalAccessTokenAuthConfig(
        token="<Your Harvest personal access token>",
        account_id="<Your Harvest account ID>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@HarvestConnector.tool_utils
async def harvest_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_harvest import HarvestConnector, AirbyteAuthConfig

connector = HarvestConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@HarvestConnector.tool_utils
async def harvest_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Users | List, Get, Search |
| Clients | List, Get, Search |
| Contacts | List, Get, Search |
| Company | Get, Search |
| Projects | List, Get, Search |
| Tasks | List, Get, Search |
| Time Entries | List, Get, Search |
| Invoices | List, Get, Search |
| Invoice Item Categories | List, Get, Search |
| Estimates | List, Get, Search |
| Estimate Item Categories | List, Get, Search |
| Expenses | List, Get, Search |
| Expense Categories | List, Get, Search |
| Roles | List, Get, Search |
| User Assignments | List, Search |
| Task Assignments | List, Search |
| Time Projects | List, Search |
| Time Tasks | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/harvest/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/harvest/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/harvest)*
