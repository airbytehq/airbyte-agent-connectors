# Programmatic Connector Setup

Set up connectors entirely from the terminal or via HTTP APIs—no UI required.

## When to Use This Guide

| If you want to... | Use |
|-------------------|-----|
| Create connectors from scripts/automation | This guide |
| Use curl, Postman, or HTTP clients | This guide |
| Build with Claude Code, Codex, or terminal | This guide |
| Use a visual interface | [app.airbyte.ai](https://app.airbyte.ai) |

## Prerequisites

You need Airbyte application credentials:
- `AIRBYTE_CLIENT_ID` - from app.airbyte.ai settings (one-time)
- `AIRBYTE_CLIENT_SECRET` - from app.airbyte.ai settings (one-time)


## Step 1: Get Application Token

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/account/applications/token' \
  -H 'Content-Type: application/json' \
  -d '{
    "client_id": "<AIRBYTE_CLIENT_ID>",
    "client_secret": "<AIRBYTE_CLIENT_SECRET>"
  }'
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1..."
}
```

Save this as `APPLICATION_TOKEN`. Use it for all subsequent requests.

## Choose Your Pattern

| Pattern | Best For | API Base |
|---------|----------|----------|
| **A: Scoped Token** | API key connectors, simpler flow | `api.airbyte.ai` |
| **B: Workspace** | OAuth connectors, enterprise multi-tenant | `api.airbyte.ai` |
| **C: UI Template** | Making connectors visible in Airbyte UI | `api.airbyte.ai` |

---

## Pattern A: Scoped Token Flow (Recommended for API Key Connectors)

### Step A2: Get Scoped Token

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/embedded/scoped-token' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -d '{
    "workspace_name": "<EXTERNAL_USER_ID>"
  }'
```

The `workspace_name` is your identifier for the user/tenant (you define this).

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1..."
}
```

Save this as `SCOPED_TOKEN`.

### Step A3: Create Connector

For API Key Connectors (Stripe, Gong, Jira, etc.):

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <SCOPED_TOKEN>' \
  -d '{
    "connector_definition_id": "<CONNECTOR_DEFINITION_ID>",
    "name": "my-stripe-connector",
    "auth_config": {
      "api_key": "<YOUR_API_KEY>"
    }
  }'
```

Response:
```json
{
  "id": "abc123-connector-id",
  "name": "my-stripe-connector",
  ...
}
```

Save the `id` as `CONNECTOR_ID`.

### Step A4: Execute Operations

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors/<CONNECTOR_ID>/execute' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -d '{
    "entity": "customers",
    "action": "list",
    "params": {"limit": 10}
  }'
```

---

## Pattern B: Workspace Flow (For OAuth Connectors)

Use this pattern when you need OAuth (Salesforce, HubSpot, Google Drive, Intercom, etc.).

### Step B2: Create Workspace

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/workspaces' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "customer_<UNIQUE_ID>"
  }'
```

Response:
```json
{
  "workspaceId": "a1b2c3d4-...",
  "name": "customer_12345"
}
```

Save `workspaceId`.

### Step B3: Initiate OAuth

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/sources/initiateOAuth' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "workspaceId": "<WORKSPACE_ID>",
    "sourceType": "intercom",
    "redirectUrl": "https://your-app.com/oauth/callback"
  }'
```

Response:
```json
{
  "consentUrl": "https://app.intercom.com/oauth/..."
}
```

Redirect user to `consentUrl`. After authorization, they return to your `redirectUrl` with a `secret_id` parameter.

### Step B4: Create Source with OAuth Secret

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/sources' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "workspaceId": "<WORKSPACE_ID>",
    "name": "intercom-connector",
    "secretId": "<SECRET_ID_FROM_CALLBACK>",
    "configuration": {
      "sourceType": "intercom",
      "start_date": "2021-01-01T00:00:00Z"
    }
  }'
```

Response includes `sourceId`.

### Step B5: Execute Operations

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/connectors/sources/<SOURCE_ID>/execute' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -d '{
    "entity": "contacts",
    "action": "list",
    "params": {"per_page": 50}
  }'
```

---

## Pattern C: UI Template Registration

Use this pattern to make connectors appear in the Airbyte UI's Connectors page. Run this after creating a connector with Pattern A or B.

### Why Register a Template?

When you create a connector programmatically via `create_hosted()` or the HTTP API, it's functional but **not visible in the UI**. Registering a template creates a card in the Connectors page at [app.airbyte.ai](https://app.airbyte.ai).

### Step C1: Register the Template

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/templates/sources' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -d '{
    "actor_definition_id": "<CONNECTOR_DEFINITION_ID>",
    "name": "Gong",
    "original_source_template_id": "",
    "partial_default_config": {},
    "mode": "DIRECT"
  }'
```

### Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `actor_definition_id` | Connector type ID from the table below | `32382e40-3b49-4b99-9c5c-4076501914e7` (Gong) |
| `name` | Display name shown on the UI card | `"Gong"`, `"My Stripe Connector"` |
| `original_source_template_id` | Always pass `""` (empty string) — required by the API | `""` |
| `partial_default_config` | Pre-filled configuration values | `{}` or `{"start_date": "2024-01-01"}` |
| `mode` | Always use `DIRECT`. If the API rejects the mode, check the error for accepted values | `"DIRECT"` |

### Example: Register Gong Connector

```bash
# Using the APPLICATION_TOKEN from Step 1
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/templates/sources' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1...' \
  -d '{
    "actor_definition_id": "32382e40-3b49-4b99-9c5c-4076501914e7",
    "name": "Gong",
    "original_source_template_id": "",
    "partial_default_config": {},
    "mode": "DIRECT"
  }'
```

### Example: Register Salesforce Connector

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/templates/sources' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -d '{
    "actor_definition_id": "b117307c-14b6-41aa-9422-947e34922962",
    "name": "Salesforce",
    "original_source_template_id": "",
    "partial_default_config": {},
    "mode": "DIRECT"
  }'
```

### Troubleshooting Template Registration

| Error | Cause | Solution |
|-------|-------|----------|
| `"already exists"` | Template with that name exists | Choose a different `name` value |
| `"invalid actor_definition_id"` | Wrong connector definition ID | Check the [Connector Definition IDs table](#connector-definition-ids) |
| `"unauthorized"` | Invalid or expired token | Regenerate the APPLICATION_TOKEN |

### Verify in UI

After successful registration:
1. Go to [app.airbyte.ai](https://app.airbyte.ai)
2. Navigate to the **Connectors** page
3. Your connector appears as a card with the name and a "Direct" or "OAuth" badge

---

## Connector Definition IDs

| Connector | Definition ID |
|-----------|---------------|
| Airtable | `14c6e7ea-97ed-4f5e-a7b5-25e9a80b8212` |
| Amazon Ads | `c6b0a29e-1da9-4512-9002-7bfd0cba2246` |
| Asana | `d0243522-dccf-4978-8ba0-37ed47a0bdbf` |
| Facebook Marketing | `e7778cfc-e97c-4458-9ecb-b4f2bba8946c` |
| GitHub | `ef69ef6e-aa7f-4af1-a01d-ef775033524e` |
| Gong | `32382e40-3b49-4b99-9c5c-4076501914e7` |
| Google Drive | `9f8dda77-1048-4368-815b-269bf54ee9b8` |
| Greenhouse | `59f1e50a-331f-4f09-b3e8-2e8d4d355f44` |
| HubSpot | `36c891d9-4bd9-43ac-bad2-10e12756272c` |
| Intercom | `d8313939-3782-41b0-be29-b3ca20d8dd3a` |
| Jira | `68e63de2-bb83-4c7e-93fa-a8a9051e3993` |
| Klaviyo | `95e8cffd-b8c4-4039-968e-d32fb4a69bde` |
| Linear | `1c5d8316-ed42-4473-8fbc-2626f03f070c` |
| Mailchimp | `b03a9f3e-22a5-11eb-adc1-0242ac120002` |
| Orb | `7f0455fb-4518-4ec0-b7a3-d808bf8081cc` |
| Salesforce | `b117307c-14b6-41aa-9422-947e34922962` |
| Shopify | `9da77001-af33-4bcd-be46-6252bf9342b9` |
| Slack | `c2281cee-86f9-4a86-bb48-d23286b4c7bd` |
| Stripe | `e094cb9a-26de-4645-8761-65c0c425d1de` |
| Zendesk Chat | `40d24d0f-b8f9-4fe0-9e6c-b06c0f3f45e4` |
| Zendesk Support | `79c1aa37-dae3-42ae-b333-d1c105477715` |

## Token Reference

| Token Type | Endpoint | Use For |
|------------|----------|---------|
| Application Token | `/v1/applications/token` | App-level API access |
| Scoped Token | `/api/v1/embedded/scoped-token` | User-scoped operations |

## SDK vs HTTP API vs UI Decision Guide

| Factor | SDK | HTTP API | UI |
|--------|-----|----------|-----|
| **Best for** | Python apps, type safety | Any language, scripts, curl | Visual exploration |
| **Auth handling** | Automatic token management | Manual token management | Built-in |
| **OAuth connectors** | Use `create_hosted()` | Use Pattern B (workspace flow) | Built-in flow |
| **API key connectors** | Use `create_hosted()` | Use Pattern A (scoped token) | Built-in |
| **Multi-tenant** | `external_user_id` param | `workspace_name` in scoped token | Manual workspace switching |
| **Learning curve** | Low | Medium | Lowest |

**Recommendation:**
- **Python apps**: Use the SDK (`create_hosted()`)—it handles tokens automatically
- **Non-Python or scripts**: Use HTTP API with this guide
- **Exploration/debugging**: Use the UI at app.airbyte.ai

## Troubleshooting

### "Invalid token" errors
- Application tokens expire; regenerate if needed
- Ensure you're using the right token type for each endpoint:
  - Application token: workspace creation, OAuth initiation
  - Scoped token: connector instance creation

### "Connector not found" errors
- Verify `CONNECTOR_ID` from creation response
- Check you're using the correct `SCOPED_TOKEN` for that user

### "Unauthorized" errors
- Verify your `AIRBYTE_CLIENT_ID` and `AIRBYTE_CLIENT_SECRET`
- Regenerate the application token

## Related Documentation

- [Authentication](./authentication.md) - SDK-based auth patterns
- [Getting Started](./getting-started.md) - Installation and setup
- [Entity-Action API](./entity-action-api.md) - Core API patterns
