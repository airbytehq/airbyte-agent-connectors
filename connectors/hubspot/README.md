# Airbyte Hubspot AI Connector

Type-safe Hubspot API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.5.0

**Connector Version:** 1.0.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-hubspot
```

## Usage

```python
from airbyte_ai_hubspot import HubspotConnector

# Create connector
connector = HubspotConnector(auth_config={"api_key": "your_api_key"})

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Contacts Operations
- `list_contacts()` - List contacts
- `get_contact()` - Get a contact

### Companies Operations
- `list_companies()` - List companies
- `get_company()` - Get a company

### Deals Operations
- `list_deals()` - List deals
- `get_deal()` - Get a deal

### Tickets Operations
- `list_tickets()` - List tickets
- `get_ticket()` - Get a ticket

### Schemas Operations
- `list_schemas()` - List custom object schemas

### Objects Operations
- `list_objects()` - List objects
- `get_object()` - Get an object

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_hubspot.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
