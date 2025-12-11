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

# Create connector
connector = StripeConnector(auth_config=StripeAuthConfig(token="..."))

# Use typed methods with full IDE autocomplete
# (See Available Actions below for all methods)
```

## Available Actions

### Customers Actions
- `customers__list()` - Returns a list of customers
- `customers__get()` - Gets the details of an existing customer

## Type Definitions

All response types are fully typed using Pydantic models for IDE autocomplete support.
Import types from `airbyte_ai_stripe.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.

## Version Information

**Package Version:** 0.5.2

**Connector Version:** 0.1.0

**SDK Version:** 0.1.0