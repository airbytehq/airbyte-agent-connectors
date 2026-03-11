<!-- AUTO-GENERATED from connectors/linkedin-ads/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# LinkedIn Ads

The Linkedin-Ads agent connector is a Python package that equips AI agents to interact with Linkedin-Ads through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-linkedin-ads` v0.1.1
- **Auth:** OAuth
- **Docs:** [Official API docs](https://learn.microsoft.com/en-us/linkedin/marketing/)
- **Status:** complete

## Example Prompts

- List all my LinkedIn ad accounts
- Show me all campaigns in my ad account
- List all campaign groups
- Show me the creatives for my campaigns
- List all conversions configured for my ad accounts
- Show me account users for my LinkedIn ads accounts
- Which campaigns have the highest click-through rate?
- What is the total ad spend across all campaigns this month?
- Show me campaigns with status ACTIVE
- Which creatives have the most impressions?
- Compare campaign performance by cost type

## Unsupported

- Create a new campaign
- Update campaign budgets
- Delete an ad creative
- Pause a campaign

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-linkedin-ads
```

### OSS Mode

```python
from airbyte_agent_linkedin_ads import LinkedinAdsConnector
from airbyte_agent_linkedin_ads.models import LinkedinAdsAuthConfig

connector = LinkedinAdsConnector(
    auth_config=LinkedinAdsAuthConfig(
        refresh_token="<OAuth 2.0 refresh token for automatic renewal>",
        client_id="<OAuth 2.0 application client ID>",
        client_secret="<OAuth 2.0 application client secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@LinkedinAdsConnector.tool_utils
async def linkedin_ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_linkedin_ads import LinkedinAdsConnector, AirbyteAuthConfig

connector = LinkedinAdsConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@LinkedinAdsConnector.tool_utils
async def linkedin_ads_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Accounts | List, Get, Search |
| Account Users | List, Search |
| Campaigns | List, Get, Search |
| Campaign Groups | List, Get, Search |
| Creatives | List, Get, Search |
| Conversions | List, Get, Search |
| Ad Campaign Analytics | List, Search |
| Ad Creative Analytics | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/linkedin-ads/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/linkedin-ads/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/linkedin-ads)*
