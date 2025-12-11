# Airbyte Hubspot AI Connector

Type-safe Hubspot API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-hubspot
```

## Usage

```python
from airbyte_ai_hubspot import HubspotConnector
from airbyte_ai_hubspot.models import HubspotAuthConfig

# Create connector
connector = HubspotConnector(auth_config=HubspotAuthConfig(client_id="...", client_secret="...", refresh_token="...", access_token="..."))

# Use typed methods with full IDE autocomplete
# (See Available Actions below for all methods)
```

## Available Actions

### Contacts Actions
- `list_contacts()` - Returns a paginated list of contacts
- `get_contact()` - Get a single contact by ID
- `search_contacts()` - Search for contacts by filtering on properties, searching through associations, and sorting results.

### Companies Actions
- `list_companies()` - Retrieve all companies, using query parameters to control the information that gets returned.
- `get_company()` - Get a single company by ID
- `search_companies()` - Search for companies by filtering on properties, searching through associations, and sorting results.

### Deals Actions
- `list_deals()` - Returns a paginated list of deals
- `get_deal()` - Get a single deal by ID
- `search_deals()` - Search deals with filters and sorting

### Tickets Actions
- `list_tickets()` - Returns a paginated list of tickets
- `get_ticket()` - Get a single ticket by ID
- `search_tickets()` - Search for tickets by filtering on properties, searching through associations, and sorting results.

### Schemas Actions
- `list_schemas()` - Returns all custom object schemas to discover available custom objects
- `get_schema()` - Get the schema for a specific custom object type

### Objects Actions
- `list_objects()` - Read a page of objects. Control what is returned via the properties query param.
- `get_object()` - Read an Object identified by {objectId}. {objectId} refers to the internal object ID by default, or optionally any unique property value as specified by the idProperty query param. Control what is returned via the properties query param.

## Type Definitions

All response types are fully typed using Pydantic models for IDE autocomplete support.
Import types from `airbyte_ai_hubspot.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.

## Version Information

**Package Version:** 0.15.3

**Connector Version:** 0.1.1

**SDK Version:** 0.1.0