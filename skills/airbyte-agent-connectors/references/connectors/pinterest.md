<!-- AUTO-GENERATED from connectors/pinterest/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Pinterest

The Pinterest agent connector is a Python package that equips AI agents to interact with Pinterest through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-pinterest` v0.1.0
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developers.pinterest.com/docs/api/v5/)
- **Status:** complete

## Example Prompts

- List all my Pinterest ad accounts
- List all my Pinterest boards
- Show me all campaigns in my ad account
- List all ads in my ad account
- Show me all ad groups in my ad account
- List all audiences for my ad account
- Show me my catalog feeds
- Which campaigns are currently active?
- What are the top boards by pin count?
- Show me ads that have been rejected
- Find campaigns with the highest daily spend cap

## Unsupported

- Create a new Pinterest board
- Update a campaign budget
- Delete an ad group
- Post a new pin
- Show me campaign analytics or performance metrics

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-pinterest
```

### OSS Mode

```python
from airbyte_agent_pinterest import PinterestConnector
from airbyte_agent_pinterest.models import PinterestAuthConfig

connector = PinterestConnector(
    auth_config=PinterestAuthConfig(
        refresh_token="<Pinterest OAuth2 refresh token.>",
        client_id="<Pinterest OAuth2 client ID.>",
        client_secret="<Pinterest OAuth2 client secret.>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PinterestConnector.tool_utils
async def pinterest_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_pinterest import PinterestConnector, AirbyteAuthConfig

connector = PinterestConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PinterestConnector.tool_utils
async def pinterest_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Ad Accounts | List, Get, Search |
| Boards | List, Get, Search |
| Campaigns | List, Search |
| Ad Groups | List, Search |
| Ads | List, Search |
| Board Sections | List, Search |
| Board Pins | List, Search |
| Catalogs | List, Search |
| Catalogs Feeds | List, Search |
| Catalogs Product Groups | List, Search |
| Audiences | List, Search |
| Conversion Tags | List, Search |
| Customer Lists | List, Search |
| Keywords | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/pinterest/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/pinterest/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/pinterest)*
