<!-- AUTO-GENERATED from connectors/google-search-console/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Google Search Console

The Google-Search-Console agent connector is a Python package that equips AI agents to interact with Google-Search-Console through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-google-search-console` v0.1.0
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developers.google.com/webmaster-tools/v1/api_reference_index)
- **Status:** complete

## Example Prompts

- List all my verified sites in Search Console
- Show me the sitemaps for my website
- Get search analytics by date for the last 7 days
- Show search performance broken down by country
- What devices are people using to find my site?
- Which pages get the most clicks?
- What queries bring the most traffic to my site?
- Which country has the highest CTR for my site?
- What are my top 10 search queries by impressions?
- Compare mobile vs desktop click-through rates
- Which pages have the worst average position?
- Show me search performance trends over the last month

## Unsupported

- Submit a new sitemap
- Add a new site to Search Console
- Remove a site from Search Console
- Inspect a URL's index status
- Request indexing for a page

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-google-search-console
```

### OSS Mode

```python
from airbyte_agent_google_search_console import GoogleSearchConsoleConnector
from airbyte_agent_google_search_console.models import GoogleSearchConsoleAuthConfig

connector = GoogleSearchConsoleConnector(
    auth_config=GoogleSearchConsoleAuthConfig(
        client_id="<The client ID of your Google Search Console developer application.>",
        client_secret="<The client secret of your Google Search Console developer application.>",
        refresh_token="<The refresh token for obtaining new access tokens.>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GoogleSearchConsoleConnector.tool_utils
async def google_search_console_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_google_search_console import GoogleSearchConsoleConnector, AirbyteAuthConfig

connector = GoogleSearchConsoleConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GoogleSearchConsoleConnector.tool_utils
async def google_search_console_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Sites | List, Get, Search |
| Sitemaps | List, Get, Search |
| Search Analytics By Date | List, Search |
| Search Analytics By Country | List, Search |
| Search Analytics By Device | List, Search |
| Search Analytics By Page | List, Search |
| Search Analytics By Query | List, Search |
| Search Analytics All Fields | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/google-search-console/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/google-search-console/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/google-search-console)*
