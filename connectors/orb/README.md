# Orb agent connector

Orb is a usage-based billing platform that enables businesses to implement flexible pricing models,
track customer usage, and manage subscriptions. This connector provides access to customers,
subscriptions, plans, and invoices for billing analytics and customer management.


## Example questions

The Orb connector is optimized to handle prompts like these.

- Show me all my customers in Orb
- List all active subscriptions
- What plans are available?
- Show me recent invoices
- Get details for customer \{customer_id\}
- What is the status of subscription \{subscription_id\}?
- List all invoices for a specific customer
- Show me the pricing details for plan \{plan_id\}
- List all subscriptions for customer XYZ
- Show all active subscriptions for a specific customer
- What subscriptions does customer \{external_customer_id\} have?
- Confirm the Stripe ID linked to this customer
- What is the payment provider ID for customer \{customer_id\}?
- Pull all invoices from the last month
- Show invoices created after \{date\}
- List all paid invoices for customer \{customer_id\}
- What invoices are in draft status?
- Show all issued invoices for subscription \{subscription_id\}

## Unsupported questions

The Orb connector isn't currently able to handle prompts like these.

- Create a new customer in Orb
- Update subscription details
- Delete a customer record
- Send an invoice to a customer
- Filter subscriptions by plan name (must filter client-side after listing)
- Pull customers billed for specific products (must examine invoice line_items client-side)

## Installation

```bash
uv pip install airbyte-agent-orb
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

**3. Create connector:**
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/connectors/instances' \
  -H 'Authorization: Bearer <SCOPED_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "connector_definition_id": "7f0455fb-4518-4ec0-b7a3-d808bf8081cc",
    "name": "my-orb-connector",
    "auth_config": {
      "api_key": "<YOUR_API_KEY>"
    }
  }'
```

Save the returned `id` as your `CONNECTOR_ID` for subsequent requests.

## Usage

Connectors can run in open source or hosted mode.

### Open source

In open source mode, you provide API credentials directly to the connector.

```python
from airbyte_agent_orb import OrbConnector
from airbyte_agent_orb.models import OrbAuthConfig

connector = OrbConnector(
    auth_config=OrbAuthConfig(
        api_key="<Your Orb API key>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@OrbConnector.tool_utils
async def orb_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. 

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```python
from airbyte_agent_orb import OrbConnector

connector = OrbConnector(
    external_user_id="<your_external_user_id>",
    airbyte_client_id="<your-client-id>",
    airbyte_client_secret="<your-client-secret>"
)

@agent.tool_plain # assumes you're using Pydantic AI
@OrbConnector.tool_utils
async def orb_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation

### Entities and actions

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](REFERENCE.md).

| Entity | Actions |
|--------|---------|
| Customers | [List](./REFERENCE.md#customers-list), [Get](./REFERENCE.md#customers-get) |
| Subscriptions | [List](./REFERENCE.md#subscriptions-list), [Get](./REFERENCE.md#subscriptions-get) |
| Plans | [List](./REFERENCE.md#plans-list), [Get](./REFERENCE.md#plans-get) |
| Invoices | [List](./REFERENCE.md#invoices-list), [Get](./REFERENCE.md#invoices-get) |


### Authentication and configuration

For all authentication and configuration options, see the connector's [authentication documentation](AUTH.md).

### Orb API docs

See the official [Orb API reference](https://docs.withorb.com/api-reference).

## Version information

- **Package version:** 0.1.7
- **Connector version:** 0.1.1
- **Generated with Connector SDK commit SHA:** 940246757c7476ed4edd7d16b873ebe54ea2b456
- **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/orb/CHANGELOG.md)