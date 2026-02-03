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
curl -X POST 'https://api.airbyte.com/v1/applications/token' \
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
| **B: Workspace** | OAuth connectors, enterprise multi-tenant | `api.airbyte.com` + `api.airbyte.ai` |

### What Each Pattern Creates

| Pattern | Creates | UI Visibility | Best For |
|---------|---------|---------------|----------|
| **A: Scoped Token** | Embedded connector instance | Not visible in UI | API-only, short-lived, multi-tenant |
| **B: Workspace** | Source in workspace | Visible in Sources page | OAuth connectors, visual management |

**Pattern A (Scoped Token):** Creates connector instances tied to a scoped workspace. Managed via API only - they don't appear in the Airbyte Cloud UI. Best for programmatic multi-tenant setups where you don't need visual management.

**Pattern B (Workspace):** Creates traditional Sources that appear in the Airbyte Cloud UI under Sources. Required for OAuth connectors using server-side OAuth flow. Better stability for production workloads.

**Stability Note:** Pattern A connector instances may be recycled during inactivity. Implement token refresh logic for production use, or use Pattern B for long-running workloads.

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
curl -X POST 'https://api.airbyte.ai/api/v1/connectors/instances' \
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

**Note:** The `auth_config` structure varies by connector. See each connector's AUTH.md for exact fields:

| Connector | Auth Type | `auth_config` Fields |
|-----------|-----------|---------------------|
| Stripe | API Key | `{"api_key": "sk_live_..."}` |
| Gong | API Key | `{"access_key": "...", "access_key_secret": "..."}` |
| GitHub | PAT | `{"token": "ghp_..."}` |
| Slack | Bot Token | `{"token": "xoxb-..."}` |
| Jira | API Token | `{"api_token": "...", "email": "...", "domain": "..."}` |
| HubSpot | Private App | `{"access_token": "pat-na1-..."}` |

For the complete auth config structure, see:
- [Gong AUTH.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/gong/AUTH.md)
- [Stripe AUTH.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/stripe/AUTH.md)
- [GitHub AUTH.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/github/AUTH.md)

### Step A4: Execute Operations

**Note:** Execute uses the `APPLICATION_TOKEN` (not the scoped token). The scoped token is only needed for connector creation in Step A3.

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/connectors/instances/<CONNECTOR_ID>/execute' \
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
curl -X POST 'https://api.airbyte.com/v1/workspaces' \
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
curl -X POST 'https://api.airbyte.com/v1/sources/initiateOAuth' \
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
curl -X POST 'https://api.airbyte.com/v1/sources' \
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

- [Authentication](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/references/authentication.md) - SDK-based auth patterns
- [Getting Started](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/references/getting-started.md) - Installation and setup
- [Entity-Action API](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/references/entity-action-api.md) - Core API patterns
