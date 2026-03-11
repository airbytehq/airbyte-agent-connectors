<!-- AUTO-GENERATED from connectors/hubspot/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# HubSpot

The Hubspot agent connector is a Python package that equips AI agents to interact with Hubspot through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-hubspot` v0.15.117
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm)
- **Status:** complete

## Example Prompts

- List recent deals
- List recent tickets
- List companies in my CRM
- List contacts in my CRM
- Show me all deals from \{company\} this quarter
- What are the top 5 most valuable deals in my pipeline right now?
- Search for contacts in the marketing department at \{company\}
- Give me an overview of my sales team's deals in the last 30 days
- Identify the most active companies in our CRM this month
- Compare the number of deals closed by different sales representatives
- Find all tickets related to a specific product issue and summarize their status

## Unsupported

- Create a new contact record for \{person\}
- Update the contact information for \{customer\}
- Delete the ticket from last week's support case
- Schedule a follow-up task for this deal
- Send an email to all contacts in the sales pipeline

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-hubspot
```

### OSS Mode

```python
from airbyte_agent_hubspot import HubspotConnector
from airbyte_agent_hubspot.models import HubspotAuthConfig

connector = HubspotConnector(
    auth_config=HubspotAuthConfig(
        client_id="<Your HubSpot OAuth2 Client ID>",
        client_secret="<Your HubSpot OAuth2 Client Secret>",
        refresh_token="<Your HubSpot OAuth2 Refresh Token>",
        access_token="<Your HubSpot OAuth2 Access Token (optional if refresh_token is provided)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@HubspotConnector.tool_utils
async def hubspot_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_hubspot import HubspotConnector, AirbyteAuthConfig

connector = HubspotConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@HubspotConnector.tool_utils
async def hubspot_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Contacts | List, Get, API Search, Search |
| Companies | List, Get, API Search, Search |
| Deals | List, Get, API Search, Search |
| Tickets | List, Get, API Search |
| Schemas | List, Get |
| Objects | List, Get |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/hubspot/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/hubspot/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/hubspot)*
