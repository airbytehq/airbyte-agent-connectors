<!-- AUTO-GENERATED from connectors/stripe/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Airbyte Stripe AI Connector

# Package: airbyte-ai-stripe v0.5.0

Type-safe Stripe API connector with full IDE autocomplete support for AI applications.

**Key metadata:**

- **Package:** `airbyte-ai-stripe` v0.5.0
- **Auth:** StripeAuthConfig (token)
- **Docs:** [Official API docs](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/stripe)
- **Status:** docs pending

## Quick Start

### Installation

```bash
uv pip install airbyte-ai-stripe
```

### Usage

```python
from airbyte_ai_stripe import StripeConnector
from airbyte_ai_stripe.models import StripeAuthConfig

# Create connector
connector = StripeConnector(auth_config=StripeAuthConfig(token="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Entities and Actions

| Entity | Action | Description |
|--------|--------|-------------|
| Customers | `customers__list()` | Returns a list of customers |
| Customers | `customers__get()` | Gets the details of an existing customer |

## Authentication

Auth class: `StripeAuthConfig`

Required fields:

- `token`

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/stripe)*
