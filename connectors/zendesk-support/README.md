# Airbyte Zendesk-Support AI Connector

Type-safe Zendesk-Support API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-zendesk-support
```

## Usage

```python
from airbyte_ai_zendesk_support import ZendeskSupportConnector, ZendeskSupportAuthConfig

connector = ZendeskSupportConnector(
  auth_config=ZendeskSupportAuthConfig(
    access_token="...",
    refresh_token="..."
  )
)
result = connector.tickets.list()
```

## Documentation

| Entity | Actions |
|--------|---------|
| Tickets | [List](./REFERENCE.md#tickets-list), [Get](./REFERENCE.md#tickets-get) |
| Users | [List](./REFERENCE.md#users-list), [Get](./REFERENCE.md#users-get) |
| Organizations | [List](./REFERENCE.md#organizations-list), [Get](./REFERENCE.md#organizations-get) |
| Groups | [List](./REFERENCE.md#groups-list), [Get](./REFERENCE.md#groups-get) |
| Ticket Comments | [List](./REFERENCE.md#ticket-comments-list) |
| Attachments | [Get](./REFERENCE.md#attachments-get), [Download](./REFERENCE.md#attachments-download) |
| Ticket Audits | [List](./REFERENCE.md#ticket-audits-list), [List](./REFERENCE.md#ticket-audits-list) |
| Ticket Metrics | [List](./REFERENCE.md#ticket-metrics-list) |
| Ticket Fields | [List](./REFERENCE.md#ticket-fields-list), [Get](./REFERENCE.md#ticket-fields-get) |
| Brands | [List](./REFERENCE.md#brands-list), [Get](./REFERENCE.md#brands-get) |
| Views | [List](./REFERENCE.md#views-list), [Get](./REFERENCE.md#views-get) |
| Macros | [List](./REFERENCE.md#macros-list), [Get](./REFERENCE.md#macros-get) |
| Triggers | [List](./REFERENCE.md#triggers-list), [Get](./REFERENCE.md#triggers-get) |
| Automations | [List](./REFERENCE.md#automations-list), [Get](./REFERENCE.md#automations-get) |
| Tags | [List](./REFERENCE.md#tags-list) |
| Satisfaction Ratings | [List](./REFERENCE.md#satisfaction-ratings-list), [Get](./REFERENCE.md#satisfaction-ratings-get) |
| Group Memberships | [List](./REFERENCE.md#group-memberships-list) |
| Organization Memberships | [List](./REFERENCE.md#organization-memberships-list) |
| Sla Policies | [List](./REFERENCE.md#sla-policies-list), [Get](./REFERENCE.md#sla-policies-get) |
| Ticket Forms | [List](./REFERENCE.md#ticket-forms-list), [Get](./REFERENCE.md#ticket-forms-get) |
| Articles | [List](./REFERENCE.md#articles-list), [Get](./REFERENCE.md#articles-get) |
| Article Attachments | [List](./REFERENCE.md#article-attachments-list), [Get](./REFERENCE.md#article-attachments-get), [Download](./REFERENCE.md#article-attachments-download) |


For detailed documentation on available actions and parameters, see [REFERENCE.md](./REFERENCE.md).

For the service's official API docs, see [Zendesk-Support API Reference](https://developer.zendesk.com/api-reference/ticketing/introduction/).

## Version Information

**Package Version:** 0.18.8

**Connector Version:** 0.1.1

**Generated with connector-sdk:** dc79dc8b685e9d8cb980ea80f12595e31c88fdf7