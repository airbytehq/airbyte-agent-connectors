<!-- AUTO-GENERATED from connectors/salesforce/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Salesforce

The Salesforce agent connector is a Python package that equips AI agents to interact with Salesforce through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-salesforce` v0.1.108
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
- **Status:** complete

## Example Prompts

- List recent contacts in my Salesforce account
- List open cases in my Salesforce account
- Show me the notes and attachments for a recent account
- Show me my top 5 opportunities this month
- List all contacts from \{company\} in the last quarter
- Search for leads in the technology sector with revenue over $10M
- What trends can you identify in my recent sales pipeline?
- Summarize the open cases for my key accounts
- Find upcoming events related to my most important opportunities
- Analyze the performance of my recent marketing campaigns
- Identify the highest value opportunities I'm currently tracking

## Unsupported

- Create a new lead for \{person\}
- Update the status of my sales opportunity
- Schedule a follow-up meeting with \{customer\}
- Delete this old contact record
- Send an email to all contacts in this campaign

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-salesforce
```

### OSS Mode

```python
from airbyte_agent_salesforce import SalesforceConnector
from airbyte_agent_salesforce.models import SalesforceAuthConfig

connector = SalesforceConnector(
    auth_config=SalesforceAuthConfig(
        refresh_token="<OAuth refresh token for automatic token renewal>",
        client_id="<Connected App Consumer Key>",
        client_secret="<Connected App Consumer Secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SalesforceConnector.tool_utils
async def salesforce_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_salesforce import SalesforceConnector, AirbyteAuthConfig

connector = SalesforceConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SalesforceConnector.tool_utils
async def salesforce_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Sobjects | List |
| Accounts | List, Get, API Search, Search |
| Contacts | List, Get, API Search, Search |
| Leads | List, Get, API Search, Search |
| Opportunities | List, Get, API Search, Search |
| Tasks | List, Get, API Search, Search |
| Events | List, Get, API Search |
| Campaigns | List, Get, API Search |
| Cases | List, Get, API Search |
| Notes | List, Get, API Search |
| Content Versions | List, Get, Download |
| Attachments | List, Get, Download |
| Query | List |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/salesforce/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/salesforce/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/salesforce)*
