<!-- AUTO-GENERATED from connectors/intercom/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Intercom

The Intercom agent connector is a Python package that equips AI agents to interact with Intercom through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-intercom` v0.1.85
- **Auth:** Token
- **Docs:** [Official API docs](https://developers.intercom.com/docs/references/rest-api/api.intercom.io)
- **Status:** complete

## Example Prompts

- List all contacts in my Intercom workspace
- List all companies in Intercom
- What teams are configured in my workspace?
- Show me all admins in my Intercom account
- List all tags used in Intercom
- Show me all customer segments
- Show me details for a recent contact
- Show me details for a recent company
- Show me details for a recent conversation
- Create a new lead contact named 'Jane Smith' with email jane@example.com
- Create an internal article titled 'Onboarding Guide' with instructions for new team members
- Create a company named 'Acme Corp' with company_id 'acme-001'
- Create a tag named 'VIP Customer'
- Update the name of contact \{id\} to 'John Updated'
- Add a note to contact \{id\} saying 'Followed up on support request'
- Show me conversations from the last week
- List conversations assigned to team \{team_id\}
- Show me open conversations

## Unsupported

- Send a message to a customer
- Delete a conversation
- Delete a contact
- Delete a company
- Assign a conversation to an admin

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-intercom
```

### OSS Mode

```python
from airbyte_agent_intercom import IntercomConnector
from airbyte_agent_intercom.models import IntercomAuthConfig

connector = IntercomConnector(
    auth_config=IntercomAuthConfig(
        access_token="<Your Intercom API Access Token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@IntercomConnector.tool_utils
async def intercom_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_intercom import IntercomConnector, AirbyteAuthConfig

connector = IntercomConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@IntercomConnector.tool_utils
async def intercom_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Contacts | List, Create, Get, Update, Search |
| Conversations | List, Get, Search |
| Companies | List, Create, Get, Update, Search |
| Teams | List, Get, Search |
| Admins | List, Get |
| Tags | List, Create, Get |
| Notes | Create |
| Segments | List, Get |
| Internal Articles | Create |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/intercom/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/intercom/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/intercom)*
