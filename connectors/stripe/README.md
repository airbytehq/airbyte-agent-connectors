# Airbyte Stripe AI Connector

Type-safe Stripe API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-stripe
```

## Usage

```python
from airbyte_ai_stripe import StripeConnector, StripeAuthConfig

connector = StripeConnector(
  auth_config=StripeAuthConfig(
    token="..."
  )
)
result = connector.customers.list()
```

## Documentation

| Entity | Actions |
|--------|---------|
| Customers | [List](./REFERENCE.md#customers-list), [Get](./REFERENCE.md#customers-get) |


For detailed documentation on available actions and parameters, see [REFERENCE.md](./REFERENCE.md).

For the service's official API docs, see [Stripe API Reference](https://docs.stripe.com/api).

## Version Information

**Package Version:** 0.5.8

**Connector Version:** 0.1.0

**Generated with connector-sdk:** dc79dc8b685e9d8cb980ea80f12595e31c88fdf7