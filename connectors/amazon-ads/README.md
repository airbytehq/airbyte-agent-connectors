# Amazon-Ads agent connector

Amazon Ads is Amazon's advertising platform that enables sellers and vendors to promote their
products across Amazon's marketplace. This connector provides access to advertising profiles
for managing and analyzing advertising campaigns across different marketplaces.


## Example questions

The Amazon-Ads connector is optimized to handle prompts like these.

- List all my advertising profiles across marketplaces
- Show me the profiles for my seller accounts
- What marketplaces do I have advertising profiles in?
- List all portfolios for a specific profile
- Show me all sponsored product campaigns
- What campaigns are currently enabled?
- Find campaigns with a specific targeting type

## Unsupported questions

The Amazon-Ads connector isn't currently able to handle prompts like these.

- Create a new advertising campaign
- Update my campaign budget
- Delete an ad group
- Generate a performance report

## Installation

```bash
uv pip install airbyte-agent-amazon-ads
```

## Quick Setup (Hosted)

Get running with Airbyte's hosted infrastructure in 3 steps.

**Prerequisites:** `AIRBYTE_CLIENT_ID` and `AIRBYTE_CLIENT_SECRET` from [app.airbyte.ai](https://app.airbyte.ai) settings.

**1. Get application token:**
```bash
curl -X POST 'https://api.airbyte.com/v1/applications/token' \
  -H 'Content-Type: application/json' \
  -d '{"client_id": "'"$AIRBYTE_CLIENT_ID"'", "client_secret": "'"$AIRBYTE_CLIENT_SECRET"'"}'
```

**2. Get scoped token:**
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/embedded/scoped-token' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"workspace_name": "<YOUR_USER_ID>"}'
```

**3. Create connector (OAuth):**

OAuth connectors require a server-side flow. See [AUTH.md](./AUTH.md#hosted-execution) for the complete setup.

## Usage

Connectors can run in open source or hosted mode.

### Open source

In open source mode, you provide API credentials directly to the connector.

```python
from airbyte_agent_amazon-ads import AmazonAdsConnector
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
async def amazon-ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. 

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```python
from airbyte_agent_amazon-ads import AmazonAdsConnector

connector = AmazonAdsConnector(
    external_user_id="<your_external_user_id>",
    airbyte_client_id="<your-client-id>",
    airbyte_client_secret="<your-client-secret>"
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmazonAdsConnector.tool_utils
async def amazon-ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation

### Entities and actions

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](REFERENCE.md).

| Entity | Actions |
|--------|---------|
| Profiles | [List](./REFERENCE.md#profiles-list), [Get](./REFERENCE.md#profiles-get) |
| Portfolios | [List](./REFERENCE.md#portfolios-list), [Get](./REFERENCE.md#portfolios-get) |
| Sponsored Product Campaigns | [List](./REFERENCE.md#sponsored-product-campaigns-list), [Get](./REFERENCE.md#sponsored-product-campaigns-get) |


### Authentication and configuration

For all authentication and configuration options, see the connector's [authentication documentation](AUTH.md).

### Amazon-Ads API docs

See the official [Amazon-Ads API reference](https://advertising.amazon.com/API/docs/en-us).

## Version information

- **Package version:** 0.1.26
- **Connector version:** 1.0.5
- **Generated with Connector SDK commit SHA:** 940246757c7476ed4edd7d16b873ebe54ea2b456
- **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/amazon-ads/CHANGELOG.md)