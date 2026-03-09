<!-- AUTO-GENERATED from connectors/google-analytics-data-api/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Google Analytics Data API

The Google-Analytics-Data-Api agent connector is a Python package that equips AI agents to interact with Google-Analytics-Data-Api through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-google-analytics-data-api` v0.1.7
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developers.google.com/analytics/devguides/reporting/data/v1/rest)
- **Status:** complete

## Example Prompts

- Show me the website overview report
- List daily active users
- Show weekly active user trends
- Get the four-weekly active users report
- List traffic sources
- Show me page performance metrics
- Get device breakdown data
- List user locations
- What are the top traffic sources by sessions?
- Which pages have the highest bounce rate?
- What devices do most users browse from?
- Which countries send the most traffic?
- How has daily active users changed over the last month?

## Unsupported

- Create a new GA4 property
- Delete analytics data
- Modify tracking configurations
- Run a custom report with arbitrary dimensions
- Access real-time analytics data

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-google-analytics-data-api
```

### OSS Mode

```python
from airbyte_agent_google_analytics_data_api import GoogleAnalyticsDataApiConnector
from airbyte_agent_google_analytics_data_api.models import GoogleAnalyticsDataApiAuthConfig

connector = GoogleAnalyticsDataApiConnector(
    auth_config=GoogleAnalyticsDataApiAuthConfig(
        client_id="<OAuth 2.0 Client ID from Google Cloud Console>",
        client_secret="<OAuth 2.0 Client Secret from Google Cloud Console>",
        refresh_token="<OAuth 2.0 Refresh Token for obtaining new access tokens>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GoogleAnalyticsDataApiConnector.tool_utils
async def google_analytics_data_api_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_google_analytics_data_api import GoogleAnalyticsDataApiConnector, AirbyteAuthConfig

connector = GoogleAnalyticsDataApiConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GoogleAnalyticsDataApiConnector.tool_utils
async def google_analytics_data_api_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Website Overview | List, Search |
| Daily Active Users | List, Search |
| Weekly Active Users | List, Search |
| Four Weekly Active Users | List, Search |
| Traffic Sources | List, Search |
| Pages | List, Search |
| Devices | List, Search |
| Locations | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/google-analytics-data-api/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/google-analytics-data-api/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/google-analytics-data-api)*
