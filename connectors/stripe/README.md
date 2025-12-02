# Airbyte Stripe AI Connector

Type-safe Stripe API connector with full IDE autocomplete support for AI applications.

**Version:** 0.0.3

## Installation

```bash
uv pip install airbyte-ai-stripe
```

## Usage

```python
from airbyte_ai_stripe import StripeConnector

# Create connector
connector = StripeConnector.create(secrets={"api_key": "your_api_key"})

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Customers Operations
- `customers__list()` - List all customers
- `customers__get()` - Get a customer

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_stripe.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
