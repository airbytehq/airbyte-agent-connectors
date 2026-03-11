<!-- AUTO-GENERATED from connectors/freshdesk/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Freshdesk

The Freshdesk agent connector is a Python package that equips AI agents to interact with Freshdesk through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-freshdesk` v0.1.12
- **Auth:** Token
- **Docs:** [Official API docs](https://developers.freshdesk.com/api/)
- **Status:** complete

## Example Prompts

- List all open tickets in Freshdesk
- Show me all agents in the support team
- List all groups configured in Freshdesk
- Get the details of ticket #26
- Show me all companies in Freshdesk
- List all roles defined in the helpdesk
- Show me the ticket fields and their options
- List time entries for tickets
- What are the high priority tickets from last week?
- Which tickets have breached their SLA due date?
- Show me tickets assigned to agent \{agent_name\}
- Find all tickets from company \{company_name\}
- How many tickets were created this month by status?
- What are the satisfaction ratings for resolved tickets?

## Unsupported

- Create a new ticket in Freshdesk
- Update the status of ticket #\{ticket_id\}
- Delete a contact from Freshdesk
- Assign a ticket to a different agent

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-freshdesk
```

### OSS Mode

```python
from airbyte_agent_freshdesk import FreshdeskConnector
from airbyte_agent_freshdesk.models import FreshdeskAuthConfig

connector = FreshdeskConnector(
    auth_config=FreshdeskAuthConfig(
        api_key="<Your Freshdesk API key (found in Profile Settings)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@FreshdeskConnector.tool_utils
async def freshdesk_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_freshdesk import FreshdeskConnector, AirbyteAuthConfig

connector = FreshdeskConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@FreshdeskConnector.tool_utils
async def freshdesk_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Tickets | List, Get, Search |
| Contacts | List, Get |
| Agents | List, Get, Search |
| Groups | List, Get, Search |
| Companies | List, Get |
| Roles | List, Get |
| Satisfaction Ratings | List |
| Surveys | List |
| Time Entries | List |
| Ticket Fields | List |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/freshdesk/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/freshdesk/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/freshdesk)*
