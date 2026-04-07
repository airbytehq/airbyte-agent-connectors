<!-- AUTO-GENERATED from connectors/zoho-crm/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-04-07 -->

# Zoho Crm

The Zoho-Crm agent connector is a Python package that equips AI agents to interact with Zoho-Crm through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-zoho-crm` v0.1.8
- **Auth:** OAuth
- **Docs:** [Official API docs](https://www.zoho.com/crm/developer/docs/api/v2/)
- **Status:** complete

## Example Prompts

- List all leads
- Show me details for a specific lead
- List all contacts
- List all accounts
- List all open deals
- Show me details for a specific deal
- List all campaigns
- List all tasks
- List all events
- List recent calls
- List all products
- List all quotes
- List all invoices
- Show me leads created in the last 30 days
- Which deals have the highest amount?
- List all contacts at a specific company
- What is the total revenue across all deals by stage?
- Show me overdue tasks
- Which campaigns generated the most leads?
- Summarize the deal pipeline by stage
- Show me accounts with the highest annual revenue
- List all events scheduled for this week
- What are the top-performing products by unit price?
- Show me all invoices that are past due
- Break down leads by source and industry

## Unsupported

- Create a new lead in Zoho CRM
- Update a contact's email address
- Delete a deal record
- Send an email to a lead
- Convert a lead to a contact
- Merge duplicate contacts

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-zoho-crm
```

### OSS Mode

```python
from airbyte_agent_zoho_crm import ZohoCrmConnector
from airbyte_agent_zoho_crm.models import ZohoCrmAuthConfig

connector = ZohoCrmConnector(
    auth_config=ZohoCrmAuthConfig(
        client_id="<OAuth 2.0 Client ID from Zoho Developer Console>",
        client_secret="<OAuth 2.0 Client Secret from Zoho Developer Console>",
        refresh_token="<OAuth 2.0 Refresh Token (does not expire)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZohoCrmConnector.tool_utils
async def zoho_crm_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_zoho_crm import ZohoCrmConnector, AirbyteAuthConfig

connector = ZohoCrmConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZohoCrmConnector.tool_utils
async def zoho_crm_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Leads | List, Get, Search |
| Contacts | List, Get, Search |
| Accounts | List, Get, Search |
| Deals | List, Get, Search |
| Campaigns | List, Get, Search |
| Tasks | List, Get, Search |
| Events | List, Get, Search |
| Calls | List, Get, Search |
| Products | List, Get, Search |
| Quotes | List, Get, Search |
| Invoices | List, Get, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zoho-crm/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zoho-crm/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/zoho-crm)*
