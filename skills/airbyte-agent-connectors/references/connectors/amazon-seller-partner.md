<!-- AUTO-GENERATED from connectors/amazon-seller-partner/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Amazon Seller Partner

The Amazon-Seller-Partner agent connector is a Python package that equips AI agents to interact with Amazon-Seller-Partner through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-amazon-seller-partner` v0.1.1
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developer-docs.amazon.com/sp-api/)
- **Status:** complete

## Example Prompts

- List all recent orders
- Show me order items for a specific order
- List financial event groups
- Show recent financial events
- Search catalog items by keyword
- List recent reports
- What are my top-selling products by order volume?
- Show orders from the last 30 days with status Shipped
- Find financial events related to refunds
- Which orders have the highest total value?

## Unsupported

- Create a new order
- Cancel an order
- Submit a new report request
- Update product listings

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-amazon-seller-partner
```

### OSS Mode

```python
from airbyte_agent_amazon_seller_partner import AmazonSellerPartnerConnector
from airbyte_agent_amazon_seller_partner.models import AmazonSellerPartnerAuthConfig

connector = AmazonSellerPartnerConnector(
    auth_config=AmazonSellerPartnerAuthConfig(
        lwa_app_id="<Your Login with Amazon Client ID.>",
        lwa_client_secret="<Your Login with Amazon Client Secret.>",
        refresh_token="<The Refresh Token obtained via the OAuth authorization flow.>",
        access_token="<Access token (optional if refresh_token is provided).>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmazonSellerPartnerConnector.tool_utils
async def amazon_seller_partner_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_amazon_seller_partner import AmazonSellerPartnerConnector, AirbyteAuthConfig

connector = AmazonSellerPartnerConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AmazonSellerPartnerConnector.tool_utils
async def amazon_seller_partner_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Orders | List, Get, Search |
| Order Items | List, Search |
| List Financial Event Groups | List, Search |
| List Financial Events | List, Search |
| Catalog Items | List, Get |
| Reports | List, Get |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/amazon-seller-partner/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/amazon-seller-partner/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/amazon-seller-partner)*
