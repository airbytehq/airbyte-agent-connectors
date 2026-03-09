<!-- AUTO-GENERATED from connectors/shopify/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Shopify

The Shopify agent connector is a Python package that equips AI agents to interact with Shopify through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-shopify` v0.1.66
- **Auth:** Token
- **Docs:** [Official API docs](https://shopify.dev/docs/api/admin-rest)
- **Status:** complete

## Example Prompts

- List all customers in my Shopify store
- Show me details for a recent customer
- What products do I have in my store?
- List all locations for my store
- Show me inventory levels for a recent location
- Show me all draft orders
- List all custom collections in my store
- Show me details for a recent order
- Show me product variants for a recent product
- Show me orders from the last 30 days
- Show me abandoned checkouts from this week
- What price rules are currently active?

## Unsupported

- Create a new customer in Shopify
- Update product pricing
- Delete an order
- Process a refund
- Send shipping notification to customer
- Create a new discount code

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-shopify
```

### OSS Mode

```python
from airbyte_agent_shopify import ShopifyConnector
from airbyte_agent_shopify.models import ShopifyAuthConfig

connector = ShopifyConnector(
    auth_config=ShopifyAuthConfig(
        api_key="<Your Shopify Admin API access token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ShopifyConnector.tool_utils
async def shopify_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_shopify import ShopifyConnector, AirbyteAuthConfig

connector = ShopifyConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ShopifyConnector.tool_utils
async def shopify_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Customers | List, Get |
| Orders | List, Get |
| Products | List, Get |
| Product Variants | List, Get |
| Product Images | List, Get |
| Abandoned Checkouts | List |
| Locations | List, Get |
| Inventory Levels | List |
| Inventory Items | List, Get |
| Shop | Get |
| Price Rules | List, Get |
| Discount Codes | List, Get |
| Custom Collections | List, Get |
| Smart Collections | List, Get |
| Collects | List, Get |
| Draft Orders | List, Get |
| Fulfillments | List, Get |
| Order Refunds | List, Get |
| Transactions | List, Get |
| Tender Transactions | List |
| Countries | List, Get |
| Metafield Shops | List, Get |
| Metafield Customers | List |
| Metafield Products | List |
| Metafield Orders | List |
| Metafield Draft Orders | List |
| Metafield Locations | List |
| Metafield Product Variants | List |
| Metafield Smart Collections | List |
| Metafield Product Images | List |
| Customer Address | List, Get |
| Fulfillment Orders | List, Get |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/shopify/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/shopify/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/shopify)*
