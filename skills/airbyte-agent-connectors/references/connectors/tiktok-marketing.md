<!-- AUTO-GENERATED from connectors/tiktok-marketing/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# TikTok Marketing

The Tiktok-Marketing agent connector is a Python package that equips AI agents to interact with Tiktok-Marketing through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-tiktok-marketing` v0.1.16
- **Auth:** OAuth
- **Docs:** [Official API docs](https://business-api.tiktok.com/portal/docs?id=1740302848670722)
- **Status:** complete

## Example Prompts

- List all my TikTok advertisers
- Show me all campaigns for my advertiser account
- List all ad groups
- Show me all ads
- List my custom audiences
- Show me all creative asset images
- List creative asset videos
- Show me daily ad performance reports
- Get campaign performance metrics for the last 30 days
- Show me advertiser spend reports
- Which campaigns have the highest budget?
- Find all paused ad groups
- What ads were created last month?
- Show campaigns with lifetime budget mode
- Which ads had the most impressions yesterday?
- What is my total ad spend this month?
- Which campaigns have the highest click-through rate?

## Unsupported

- Create a new campaign
- Update ad group targeting
- Delete an ad

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-tiktok-marketing
```

### OSS Mode

```python
from airbyte_agent_tiktok_marketing import TiktokMarketingConnector
from airbyte_agent_tiktok_marketing.models import TiktokMarketingAuthConfig

connector = TiktokMarketingConnector(
    auth_config=TiktokMarketingAuthConfig(
        access_token="<Your TikTok Marketing API access token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@TiktokMarketingConnector.tool_utils
async def tiktok_marketing_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_tiktok_marketing import TiktokMarketingConnector, AirbyteAuthConfig

connector = TiktokMarketingConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@TiktokMarketingConnector.tool_utils
async def tiktok_marketing_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Advertisers | List, Search |
| Campaigns | List, Search |
| Ad Groups | List, Search |
| Ads | List, Search |
| Audiences | List, Search |
| Creative Assets Images | List, Search |
| Creative Assets Videos | List, Search |
| Advertisers Reports Daily | List, Search |
| Campaigns Reports Daily | List, Search |
| Ad Groups Reports Daily | List, Search |
| Ads Reports Daily | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/tiktok-marketing/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/tiktok-marketing/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/tiktok-marketing)*
