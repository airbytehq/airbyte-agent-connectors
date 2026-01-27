# Airbyte Klaviyo AI Connector

Type-safe Klaviyo API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.1.0

**Connector Version:** 0.1.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-klaviyo
```

## Usage

```python
from airbyte_ai_klaviyo import KlaviyoConnector
from airbyte_ai_klaviyo.models import KlaviyoAuthConfig

# Create connector with API key
connector = KlaviyoConnector(auth_config=KlaviyoAuthConfig(api_key="pk_..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Authentication

Klaviyo uses API key authentication. You can generate a private API key from your Klaviyo account settings.

The API key should be passed in the Authorization header with the format: Klaviyo-API-Key {api_key}

## Available Operations

### Profiles Operations
- list_profiles() - Returns a paginated list of all profiles in the account
- get_profile(id) - Get a single profile by ID

### Lists Operations
- list_lists() - Returns a paginated list of all lists in the account
- get_list(id) - Get a single list by ID

### Campaigns Operations
- list_campaigns() - Returns a paginated list of all campaigns in the account
- get_campaign(id) - Get a single campaign by ID

### Flows Operations
- list_flows() - Returns a paginated list of all flows in the account
- get_flow(id) - Get a single flow by ID

### Metrics Operations
- list_metrics() - Returns a paginated list of all metrics in the account
- get_metric(id) - Get a single metric by ID

### Events Operations
- list_events() - Returns a paginated list of all events in the account
- get_event(id) - Get a single event by ID

### Email Templates Operations
- list_templates() - Returns a paginated list of all email templates in the account
- get_template(id) - Get a single email template by ID

## Example Questions

This connector can help answer questions like:

- How many profiles do we have in Klaviyo?
- What are our email marketing lists?
- Show me the recent campaigns we have sent
- What flows are currently active?
- List all metrics being tracked
- What email templates do we have?
- Show me the events for a specific profile

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from airbyte_ai_klaviyo.types.

## Documentation

Generated from OpenAPI 3.1 specification.

For API documentation, see Klaviyo API Documentation at https://developers.klaviyo.com/en/reference/api-overview
