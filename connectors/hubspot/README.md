# Airbyte Hubspot AI Connector

Type-safe Hubspot API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.11.0

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
- `list_contacts()` - Returns a paginated list of contacts
- `get_contact()` - Get a single contact by ID

### Companies Operations
- `list_companies()` - Returns a paginated list of companies
- `get_company()` - Get a single company by ID

### Deals Operations
- `list_deals()` - Returns a paginated list of deals
- `get_deal()` - Get a single deal by ID

### Tickets Operations
- `list_tickets()` - Returns a paginated list of tickets
- `get_ticket()` - Get a single ticket by ID

### Schemas Operations
- `list_schemas()` - Returns all custom object schemas to discover available custom objects

### Objects Operations
- `list_objects()` - Returns a paginated list of objects for any custom object type
- `get_object()` - Get a single object by ID for any custom object type

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_hubspot.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
