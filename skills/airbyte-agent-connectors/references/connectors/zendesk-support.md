<!-- AUTO-GENERATED from connectors/zendesk-support/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Zendesk Support

The Zendesk-Support agent connector is a Python package that equips AI agents to interact with Zendesk-Support through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-zendesk-support` v0.18.117
- **Auth:** OAuth, Token
- **Docs:** [Official API docs](https://developer.zendesk.com/api-reference/ticketing/introduction/)
- **Status:** complete

## Example Prompts

- Show me the tickets assigned to me last week
- List all unresolved tickets
- Show me the details of recent tickets
- What are the top 5 support issues our organization has faced this month?
- Analyze the satisfaction ratings for our support team in the last 30 days
- Compare ticket resolution times across different support groups
- Identify the most common ticket fields used in our support workflow
- Summarize the performance of our SLA policies this quarter

## Unsupported

- Create a new support ticket for \{customer\}
- Update the priority of this ticket
- Assign this ticket to \{team_member\}
- Delete these old support tickets
- Send an automatic response to \{customer\}

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-zendesk-support
```

### OSS Mode

```python
from airbyte_agent_zendesk_support import ZendeskSupportConnector
from airbyte_agent_zendesk_support.models import ZendeskSupportApiTokenAuthConfig

connector = ZendeskSupportConnector(
    auth_config=ZendeskSupportApiTokenAuthConfig(
        email="<Your Zendesk account email address>",
        api_token="<Your Zendesk API token from Admin Center>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskSupportConnector.tool_utils
async def zendesk_support_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_zendesk_support import ZendeskSupportConnector, AirbyteAuthConfig

connector = ZendeskSupportConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskSupportConnector.tool_utils
async def zendesk_support_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Tickets | List, Get, Search |
| Users | List, Get, Search |
| Organizations | List, Get, Search |
| Groups | List, Get, Search |
| Ticket Comments | List, Search |
| Attachments | Get, Download |
| Ticket Audits | List, List, Search |
| Ticket Metrics | List, Search |
| Ticket Fields | List, Get, Search |
| Brands | List, Get, Search |
| Views | List, Get |
| Macros | List, Get |
| Triggers | List, Get |
| Automations | List, Get |
| Tags | List, Search |
| Satisfaction Ratings | List, Get, Search |
| Group Memberships | List |
| Organization Memberships | List |
| Sla Policies | List, Get |
| Ticket Forms | List, Get, Search |
| Articles | List, Get |
| Article Attachments | List, Get, Download |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zendesk-support/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zendesk-support/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/zendesk-support)*
