# Airbyte Stripe AI Connector

Type-safe Stripe API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-stripe
```

## Usage

```python
from airbyte_ai_stripe import StripeConnector, StripeAuthConfig

connector = StripeConnector(auth_config=StripeAuthConfig(token="..."))
result = connector.customers.list()
```

## Documentation

| Entity | Actions |
|--------|---------|
| Customers | [List](./REFERENCE.md#customers-list), [Get](./REFERENCE.md#customers-get) |


For detailed documentation on available actions and parameters, see [REFERENCE.md](./REFERENCE.md).

For the service's official API docs, see [Stripe API Reference](https://docs.stripe.com/api).

## Version Information

**Package Version:** 0.5.7

**Connector Version:** 0.1.0

**Generated with connector-sdk:** 9f7f8a98389c3775a4d22db1aa81fbb03020a65b