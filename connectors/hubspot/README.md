# Airbyte Hubspot AI Connector

Connector for HubSpot CRM API

## Installation

```bash
uv pip install airbyte-ai-hubspot
```

## Usage

```python
from airbyte_ai_hubspot import HubspotConnector, HubspotAuthConfig

connector = HubspotConnector(
  auth_config=HubspotAuthConfig(
    client_id="...",
    client_secret="...",
    refresh_token="...",
    access_token="..."
  )
)
result = connector.contacts.list()
```

## Documentation

| Entity | Actions |
|--------|---------|
| Contacts | [List](./REFERENCE.md#contacts-list), [Get](./REFERENCE.md#contacts-get), [Search](./REFERENCE.md#contacts-search) |
| Companies | [List](./REFERENCE.md#companies-list), [Get](./REFERENCE.md#companies-get), [Search](./REFERENCE.md#companies-search) |
| Deals | [List](./REFERENCE.md#deals-list), [Get](./REFERENCE.md#deals-get), [Search](./REFERENCE.md#deals-search) |
| Tickets | [List](./REFERENCE.md#tickets-list), [Get](./REFERENCE.md#tickets-get), [Search](./REFERENCE.md#tickets-search) |
| Schemas | [List](./REFERENCE.md#schemas-list), [Get](./REFERENCE.md#schemas-get) |
| Objects | [List](./REFERENCE.md#objects-list), [Get](./REFERENCE.md#objects-get) |


For detailed documentation on available actions and parameters, see [REFERENCE.md](./REFERENCE.md).

For the service's official API docs, see [Hubspot API Reference](https://developers.hubspot.com/docs/api/crm/understanding-the-crm).

## Version Information

**Package Version:** 0.15.9

**Connector Version:** 0.1.1

**Generated with connector-sdk:** dc79dc8b685e9d8cb980ea80f12595e31c88fdf7