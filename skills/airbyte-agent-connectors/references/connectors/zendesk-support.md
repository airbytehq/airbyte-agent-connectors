<!-- AUTO-GENERATED from connectors/zendesk-support/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Airbyte Zendesk-Support AI Connector

# Package: airbyte-ai-zendesk-support v0.18.0

Type-safe Zendesk-Support API connector with full IDE autocomplete support for AI applications.

**Key metadata:**

- **Package:** `airbyte-ai-zendesk-support` v0.18.0
- **Auth:** ZendeskSupportAuthConfig (access_token, refresh_token, client_id, client_secret)
- **Docs:** [Official API docs](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/zendesk-support)
- **Status:** docs pending

## Quick Start

### Installation

```bash
uv pip install airbyte-ai-zendesk-support
```

### Usage

```python
from airbyte_ai_zendesk_support import ZendeskSupportConnector
from airbyte_ai_zendesk_support.models import ZendeskSupportAuthConfig

# Create connector
connector = ZendeskSupportConnector(auth_config=ZendeskSupportAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Entities and Actions

| Entity | Action | Description |
|--------|--------|-------------|
| Tickets | `list_tickets()` | Returns a list of all tickets in your account |
| Tickets | `get_ticket()` | Returns a ticket by its ID |
| Users | `list_users()` | Returns a list of all users in your account |
| Users | `get_user()` | Returns a user by their ID |
| Organizations | `list_organizations()` | Returns a list of all organizations in your account |
| Organizations | `get_organization()` | Returns an organization by its ID |
| Groups | `list_groups()` | Returns a list of all groups in your account |
| Groups | `get_group()` | Returns a group by its ID |
| Ticket_Comments | `list_ticket_comments()` | Returns a list of comments for a specific ticket |
| Attachments | `get_attachment()` | Returns an attachment by its ID |
| Attachments | `download_attachment()` | Downloads the file content of a ticket attachment |
| Ticket_Audits | `list_ticket_audits()` | Returns a list of all ticket audits |
| Ticket_Audits | `list_audits_for_ticket()` | Returns a list of audits for a specific ticket |
| Ticket_Metrics | `list_ticket_metrics()` | Returns a list of all ticket metrics |
| Ticket_Fields | `list_ticket_fields()` | Returns a list of all ticket fields |
| Ticket_Fields | `get_ticket_field()` | Returns a ticket field by its ID |
| Brands | `list_brands()` | Returns a list of all brands for the account |
| Brands | `get_brand()` | Returns a brand by its ID |
| Views | `list_views()` | Returns a list of all views for the account |
| Views | `get_view()` | Returns a view by its ID |
| Macros | `list_macros()` | Returns a list of all macros for the account |
| Macros | `get_macro()` | Returns a macro by its ID |
| Triggers | `list_triggers()` | Returns a list of all triggers for the account |
| Triggers | `get_trigger()` | Returns a trigger by its ID |
| Automations | `list_automations()` | Returns a list of all automations for the account |
| Automations | `get_automation()` | Returns an automation by its ID |
| Tags | `list_tags()` | Returns a list of all tags used in the account |
| Satisfaction_Ratings | `list_satisfaction_ratings()` | Returns a list of all satisfaction ratings |
| Satisfaction_Ratings | `get_satisfaction_rating()` | Returns a satisfaction rating by its ID |
| Group_Memberships | `list_group_memberships()` | Returns a list of all group memberships |
| Organization_Memberships | `list_organization_memberships()` | Returns a list of all organization memberships |
| Sla_Policies | `list_sla_policies()` | Returns a list of all SLA policies |
| Sla_Policies | `get_sla_policy()` | Returns an SLA policy by its ID |
| Ticket_Forms | `list_ticket_forms()` | Returns a list of all ticket forms for the account |
| Ticket_Forms | `get_ticket_form()` | Returns a ticket form by its ID |
| Articles | `list_articles()` | Returns a list of all articles in the Help Center |
| Articles | `get_article()` | Retrieves the details of a specific article |
| Article_Attachments | `list_article_attachments()` | Returns a list of all attachments for a specific article |
| Article_Attachments | `get_article_attachment_metadata()` | Retrieves the metadata of a specific attachment for a specific article |
| Article_Attachments | `download_article_attachment()` | Downloads the file content of a specific attachment |

## Authentication

Auth class: `ZendeskSupportAuthConfig`

Required fields:

- `access_token`
- `refresh_token`
- `client_id`
- `client_secret`

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/zendesk-support)*
