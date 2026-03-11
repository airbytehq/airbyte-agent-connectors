<!-- AUTO-GENERATED from connectors/google-ads/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Google Ads

The Google-Ads agent connector is a Python package that equips AI agents to interact with Google-Ads through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-google-ads` v0.1.10
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developers.google.com/google-ads/api/rest/reference/rest)
- **Status:** complete

## Example Prompts

- List all accessible Google Ads customer accounts
- Show me all campaigns and their statuses
- List all ad groups across my campaigns
- What ads are running in my ad groups?
- Show me campaign labels
- List all ad group labels
- What labels are applied to my ads?
- Pause campaign 'Summer Sale 2025'
- Enable the ad group 'Brand Keywords'
- Create a label called 'High Priority'
- Apply the 'Q4 Campaigns' label to my search campaign
- Update the name of campaign 123456 to 'Winter Promo'
- Which campaigns have the highest cost this month?
- Show me all paused campaigns
- Find ad groups with the most impressions
- What are my top performing ads by click-through rate?
- Show campaigns with budget over $100 per day

## Unsupported

- Create a new campaign
- Delete an ad
- Delete a campaign
- Delete a label

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-google-ads
```

### OSS Mode

```python
from airbyte_agent_google_ads import GoogleAdsConnector
from airbyte_agent_google_ads.models import GoogleAdsAuthConfig

connector = GoogleAdsConnector(
    auth_config=GoogleAdsAuthConfig(
        client_id="<OAuth2 client ID from Google Cloud Console>",
        client_secret="<OAuth2 client secret from Google Cloud Console>",
        refresh_token="<OAuth2 refresh token>",
        developer_token="<Google Ads API developer token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GoogleAdsConnector.tool_utils
async def google_ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_google_ads import GoogleAdsConnector, AirbyteAuthConfig

connector = GoogleAdsConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GoogleAdsConnector.tool_utils
async def google_ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Accessible Customers | List |
| Accounts | List, Search |
| Campaigns | List, Update, Search |
| Ad Groups | List, Update, Search |
| Ad Group Ads | List, Search |
| Campaign Labels | List, Create, Search |
| Ad Group Labels | List, Create, Search |
| Ad Group Ad Labels | List, Search |
| Labels | Create |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/google-ads/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/google-ads/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/google-ads)*
