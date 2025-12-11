# Airbyte Stripe AI Connector

Type-safe Stripe API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-stripe
```

## Usage

```python
from airbyte_ai_stripe import StripeConnector
from airbyte_ai_stripe.models import StripeAuthConfig

connector = StripeConnector(auth_config=StripeAuthConfig(token="..."))
result = connector.customers.list()
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Stripe API Reference](https://docs.stripe.com/api).

## Version Information

**Package Version:** 0.5.5

**Connector Version:** 0.1.0

**Generated with connector-sdk:** 11427ac330c199db4b55578f96eb18ab6474610e