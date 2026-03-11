<!-- AUTO-GENERATED from connectors/facebook-marketing/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Facebook Marketing

The Facebook-Marketing agent connector is a Python package that equips AI agents to interact with Facebook-Marketing through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-facebook-marketing` v0.1.52
- **Auth:** OAuth, Token
- **Docs:** [Official API docs](https://developers.facebook.com/docs/marketing-api/)
- **Status:** complete

## Example Prompts

- List all active campaigns in my ad account
- What ads are currently running in a recent campaign?
- List all ad creatives in my account
- What is the status of my campaigns?
- List all custom conversion events in my account
- Show me all ad images in my account
- What videos are available in my ad account?
- Create a new campaign called 'Summer Sale 2026' with traffic objective
- Pause my most recent campaign
- Create a new ad set with a $50 daily budget in my latest campaign
- Update the daily budget of my top performing ad set to $100
- Rename my most recent ad set to 'Holiday Promo'
- Create a new ad in my latest ad set
- Pause all ads in my most recent ad set
- List all pixels in my ad account
- Show me the event stats for my pixel
- What events is my Facebook pixel tracking?
- Search the Ad Library for political ads in the US
- Find ads about climate change in the Ad Library
- Show me Ad Library ads from a specific Facebook page
- Show me the ad sets with the highest daily budget
- Show me the performance insights for the last 7 days
- Which campaigns have the most spend this month?
- Show me ads with the highest click-through rate

## Unsupported

- Delete this ad creative
- Delete this campaign
- Delete this ad set
- Delete this ad

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-facebook-marketing
```

### OSS Mode

```python
from airbyte_agent_facebook_marketing import FacebookMarketingConnector
from airbyte_agent_facebook_marketing.models import FacebookMarketingServiceAccountKeyAuthenticationAuthConfig

connector = FacebookMarketingConnector(
    auth_config=FacebookMarketingServiceAccountKeyAuthenticationAuthConfig(
        account_key="<Facebook long-lived access token for Service Account authentication>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@FacebookMarketingConnector.tool_utils
async def facebook_marketing_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_facebook_marketing import FacebookMarketingConnector, AirbyteAuthConfig

connector = FacebookMarketingConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@FacebookMarketingConnector.tool_utils
async def facebook_marketing_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Current User | Get |
| Ad Accounts | List, Search |
| Campaigns | List, Create, Get, Update, Search |
| Ad Sets | List, Create, Get, Update, Search |
| Ads | List, Create, Get, Update, Search |
| Ad Creatives | List, Search |
| Ads Insights | List, Search |
| Ad Account | Get, Search |
| Custom Conversions | List, Search |
| Images | List, Search |
| Videos | List, Search |
| Pixels | List, Get |
| Pixel Stats | List |
| Ad Library | List |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/facebook-marketing/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/facebook-marketing/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/facebook-marketing)*
