# Airbyte Stripe AI Connector

Type-safe Stripe API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.1.22

**Connector Version:** 0.0.1

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-stripe
```

## Usage

```python
from airbyte_ai_stripe import StripeConnector

# Create connector
connector = StripeConnector(auth_config={"api_key": "your_api_key"})

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Customers Operations
- `customers__list()` - Returns a list of customers
- `customers__get()` - Gets the details of an existing customer

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_stripe.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
