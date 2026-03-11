<!-- AUTO-GENERATED from connectors/snapchat-marketing/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Snapchat Marketing

The Snapchat-Marketing agent connector is a Python package that equips AI agents to interact with Snapchat-Marketing through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-snapchat-marketing` v0.1.0
- **Auth:** Token
- **Docs:** [Official API docs](https://developers.snap.com/api/marketing-api/Ads-API/introduction)
- **Status:** complete

## Example Prompts

- List all organizations I belong to
- Show me all ad accounts for my organization
- List all campaigns in my ad account
- Show me the ad squads for my ad account
- List all ads in my ad account
- Show me the creatives for my ad account
- List all media files in my ad account
- Show me the audience segments in my ad account
- Which campaigns are currently active?
- What ad squads have the highest daily budget?
- Show me ads that are pending review
- Find campaigns created in the last month

## Unsupported

- Create a new campaign
- Update an ad's status
- Delete a creative
- Show me ad performance statistics

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-snapchat-marketing
```

### OSS Mode

```python
from airbyte_agent_snapchat_marketing import SnapchatMarketingConnector
from airbyte_agent_snapchat_marketing.models import SnapchatMarketingAuthConfig

connector = SnapchatMarketingConnector(
    auth_config=SnapchatMarketingAuthConfig(
        client_id="<The Client ID of your Snapchat developer application>",
        client_secret="<The Client Secret of your Snapchat developer application>",
        refresh_token="<Refresh Token to renew the expired Access Token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SnapchatMarketingConnector.tool_utils
async def snapchat_marketing_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_snapchat_marketing import SnapchatMarketingConnector, AirbyteAuthConfig

connector = SnapchatMarketingConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SnapchatMarketingConnector.tool_utils
async def snapchat_marketing_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Organizations | List, Get, Search |
| Adaccounts | List, Get, Search |
| Campaigns | List, Get, Search |
| Adsquads | List, Get, Search |
| Ads | List, Get, Search |
| Creatives | List, Get, Search |
| Media | List, Get, Search |
| Segments | List, Get, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/snapchat-marketing/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/snapchat-marketing/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/snapchat-marketing)*
