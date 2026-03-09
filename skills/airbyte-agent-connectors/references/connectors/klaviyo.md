<!-- AUTO-GENERATED from connectors/klaviyo/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Klaviyo

The Klaviyo agent connector is a Python package that equips AI agents to interact with Klaviyo through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-klaviyo` v0.1.41
- **Auth:** Token
- **Docs:** [Official API docs](https://developers.klaviyo.com/en/reference/api_overview)
- **Status:** complete

## Example Prompts

- List all profiles in my Klaviyo account
- Show me details for a recent profile
- Show me all email lists
- Show me details for a recent email list
- What campaigns have been created?
- Show me details for a recent campaign
- Show me all email campaigns
- List all events for tracking customer actions
- Show me all metrics (event types)
- Show me details for a recent metric
- What automated flows are configured?
- Show me details for a recent flow
- List all email templates
- Show me details for a recent email template

## Unsupported

- Create a new profile
- Update a profile's email address
- Delete a list
- Send an email campaign
- Add a profile to a list

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-klaviyo
```

### OSS Mode

```python
from airbyte_agent_klaviyo import KlaviyoConnector
from airbyte_agent_klaviyo.models import KlaviyoAuthConfig

connector = KlaviyoConnector(
    auth_config=KlaviyoAuthConfig(
        api_key="<Your Klaviyo private API key>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@KlaviyoConnector.tool_utils
async def klaviyo_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_klaviyo import KlaviyoConnector, AirbyteAuthConfig

connector = KlaviyoConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@KlaviyoConnector.tool_utils
async def klaviyo_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Profiles | List, Get, Search |
| Lists | List, Get, Search |
| Campaigns | List, Get, Search |
| Events | List, Search |
| Metrics | List, Get, Search |
| Flows | List, Get, Search |
| Email Templates | List, Get, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/klaviyo/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/klaviyo/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/klaviyo)*
