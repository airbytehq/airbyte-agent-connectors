<!-- AUTO-GENERATED from connectors/pylon/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Pylon

The Pylon agent connector is a Python package that equips AI agents to interact with Pylon through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-pylon` v0.1.11
- **Auth:** Token
- **Docs:** [Official API docs](https://docs.usepylon.com/pylon-docs/developer/api/api-reference)
- **Status:** complete

## Example Prompts

- List all open issues in Pylon
- Show me all accounts in Pylon
- List all contacts in Pylon
- What teams are configured in my Pylon workspace?
- Show me all tags used in Pylon
- List all users in my Pylon account
- Show me the custom fields configured for issues
- List all ticket forms in Pylon
- What user roles are available in Pylon?
- Show me details for a specific issue
- Get details for a specific account
- Show me details for a specific contact
- What are the most common issue sources this month?
- Show me issues assigned to a specific team
- Which accounts have the most open issues?
- Analyze issue resolution times over the last 30 days
- List contacts associated with a specific account

## Unsupported

- Delete an issue
- Delete an account
- Send a message to a customer
- Schedule a meeting with a contact

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-pylon
```

### OSS Mode

```python
from airbyte_agent_pylon import PylonConnector
from airbyte_agent_pylon.models import PylonAuthConfig

connector = PylonConnector(
    auth_config=PylonAuthConfig(
        api_token="<Your Pylon API token. Only admin users can create API tokens.>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PylonConnector.tool_utils
async def pylon_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_pylon import PylonConnector, AirbyteAuthConfig

connector = PylonConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PylonConnector.tool_utils
async def pylon_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Issues | List, Create, Get, Update |
| Messages | List |
| Issue Notes | Create |
| Issue Threads | Create |
| Accounts | List, Create, Get, Update |
| Contacts | List, Create, Get, Update |
| Teams | List, Create, Get, Update |
| Tags | List, Create, Get, Update |
| Users | List, Get |
| Custom Fields | List, Get |
| Ticket Forms | List |
| User Roles | List |
| Tasks | Create, Update |
| Projects | Create, Update |
| Milestones | Create, Update |
| Articles | Create, Update |
| Collections | Create |
| Me | Get |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/pylon/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/pylon/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/pylon)*
