<!-- AUTO-GENERATED from connectors/amazon-ads/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Amazon Ads

The Amazon-Ads agent connector is a Python package that equips AI agents to interact with Amazon-Ads through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-amazon-ads` v0.1.63
- **Auth:** OAuth
- **Docs:** [Official API docs](https://advertising.amazon.com/API/docs/en-us)
- **Status:** complete

## Example Prompts

- List all my advertising profiles across marketplaces
- Show me the profiles for my seller accounts
- What marketplaces do I have advertising profiles in?
- List all portfolios for one of my profiles
- Show me all sponsored product campaigns
- What campaigns are currently enabled?
- Find campaigns with a specific targeting type

## Unsupported

- Create a new advertising campaign
- Update my campaign budget
- Delete an ad group
- Generate a performance report

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-amazon-ads
```

### OSS Mode

```python
from airbyte_agent_amazon_ads import AmazonAdsConnector
from airbyte_agent_amazon_ads.models import AmazonAdsAuthConfig

connector = AmazonAdsConnector(
    auth_config=AmazonAdsAuthConfig(
        client_id="<The client ID of your Amazon Ads API application>",
        client_secret="<The client secret of your Amazon Ads API application>",
        refresh_token="<The refresh token obtained from the OAuth authorization flow>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmazonAdsConnector.tool_utils
async def amazon_ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_amazon_ads import AmazonAdsConnector, AirbyteAuthConfig

connector = AmazonAdsConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmazonAdsConnector.tool_utils
async def amazon_ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Profiles | List, Get, Search |
| Portfolios | List, Get |
| Sponsored Product Campaigns | List, Get |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/amazon-ads/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/amazon-ads/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/amazon-ads)*
