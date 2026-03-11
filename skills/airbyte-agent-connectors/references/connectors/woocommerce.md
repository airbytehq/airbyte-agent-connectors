<!-- AUTO-GENERATED from connectors/woocommerce/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# WooCommerce

The Woocommerce agent connector is a Python package that equips AI agents to interact with Woocommerce through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-woocommerce` v0.1.1
- **Auth:** Token
- **Docs:** [Official API docs](https://woocommerce.github.io/woocommerce-rest-api-docs/)
- **Status:** complete

## Example Prompts

- List all customers in WooCommerce
- Show me all orders
- List all products
- Show me all coupons
- List all product categories
- Show me the product reviews
- List all shipping zones
- Show me the tax rates
- List all payment gateways
- Find orders placed this month
- What are the top-selling products?
- Show me customers who have made purchases
- Find all coupons expiring this year
- What orders are still processing?

## Unsupported

- Create a new product
- Update an order status
- Delete a customer
- Apply a coupon to an order
- Process a refund

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-woocommerce
```

### OSS Mode

```python
from airbyte_agent_woocommerce import WoocommerceConnector
from airbyte_agent_woocommerce.models import WoocommerceAuthConfig

connector = WoocommerceConnector(
    auth_config=WoocommerceAuthConfig(
        api_key="<WooCommerce REST API consumer key (starts with ck_)>",
        api_secret="<WooCommerce REST API consumer secret (starts with cs_)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@WoocommerceConnector.tool_utils
async def woocommerce_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_woocommerce import WoocommerceConnector, AirbyteAuthConfig

connector = WoocommerceConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@WoocommerceConnector.tool_utils
async def woocommerce_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Customers | List, Get, Search |
| Orders | List, Get, Search |
| Products | List, Get, Search |
| Coupons | List, Get, Search |
| Product Categories | List, Get, Search |
| Product Tags | List, Get, Search |
| Product Reviews | List, Get, Search |
| Product Attributes | List, Get, Search |
| Product Variations | List, Get, Search |
| Order Notes | List, Get, Search |
| Refunds | List, Get, Search |
| Payment Gateways | List, Get, Search |
| Shipping Methods | List, Get, Search |
| Shipping Zones | List, Get, Search |
| Tax Rates | List, Get, Search |
| Tax Classes | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/woocommerce/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/woocommerce/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/woocommerce)*
