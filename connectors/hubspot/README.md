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

connector = HubspotConnector(auth_config=HubspotAuthConfig(client_id="...", client_secret="...", refresh_token="...", access_token="..."))
result = connector.contacts.list()
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Hubspot API Reference](https://developers.hubspot.com/docs/api/crm/understanding-the-crm).

## Version Information

**Package Version:** 0.15.6

**Connector Version:** 0.1.1

**Generated with connector-sdk:** 11427ac330c199db4b55578f96eb18ab6474610e