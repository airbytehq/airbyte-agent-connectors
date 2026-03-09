# Platform Setup (Airbyte Cloud / Hosted Mode)

This guide covers setting up connectors through the Airbyte Platform (app.airbyte.ai), where connectors appear in your dashboard and credentials are managed securely.

## Contents

- [When to Use Platform Mode](#when-to-use-platform-mode)
- [Prerequisites](#prerequisites)
- [Creating Connectors with create_hosted()](#creating-connectors-with-create_hosted)
- [Using Existing Connectors](#using-existing-connectors)
- [OAuth Connectors (Salesforce, HubSpot, Google Drive, etc.)](#oauth-connectors-salesforce-hubspot-google-drive-etc)
- [Making Connectors Visible in the UI](#making-connectors-visible-in-the-ui)
- [Creating Connector Instances](#creating-connector-instances)
- [Verifying Connector in UI](#verifying-connector-in-ui)
- [Entity Cache](#entity-cache)
- [Environment Variables Setup](#environment-variables-setup)
- [Troubleshooting Platform Setup](#troubleshooting-platform-setup)
- [Complete Setup Checklist](#complete-setup-checklist)
- [Related Documentation](#related-documentation)

## When to Use Platform Mode

Use Platform Mode when you want:
- Connectors visible in the Airbyte UI
- Managed credential storage and rotation
- Entity cache for faster repeated queries
- Multi-tenant SaaS deployments
- OAuth flows handled server-side

## Prerequisites

### Get Your Airbyte Platform Credentials

1. Sign up at [app.airbyte.ai](https://app.airbyte.ai)
2. Go to **Settings > API Keys**
3. Create a new API key to get:
   - `AIRBYTE_CLIENT_ID`
   - `AIRBYTE_CLIENT_SECRET`

These are your application-level credentials for creating and managing connectors programmatically.

### Define Your External User ID

The `external_user_id` is YOUR identifier for the user or tenant - you define it:
- `"user_123"` - for user-scoped connectors
- `"acme-corp"` - for organization-scoped connectors
- `"tenant_abc"` - for multi-tenant applications

This ID is used to:
- Scope connectors to specific users/tenants
- Look up existing connectors without storing connector IDs

## Creating Connectors with `create_hosted()`

### API Key Connectors

For connectors using API keys (Stripe, Gong, Jira, etc.):

```python
import os
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

# Create and register a new connector
connector = await StripeConnector.create_hosted(
    external_user_id="user_123",
    airbyte_client_id=os.environ["AIRBYTE_CLIENT_ID"],
    airbyte_client_secret=os.environ["AIRBYTE_CLIENT_SECRET"],
    auth_config=StripeAuthConfig(api_key=os.environ["STRIPE_API_KEY"]),
    name="Stripe Source"  # Optional: display name in UI
)

# Connector is created and ready to use programmatically
# For UI visibility, register a template (see "Making Connectors Visible in the UI" below)

# Use it immediately
result = await connector.execute("customers", "list", {"limit": 10})
```

### Gong Example

```python
from airbyte_agent_gong import GongConnector
from airbyte_agent_gong.models import GongAccessKeyAuthenticationAuthConfig

connector = await GongConnector.create_hosted(
    external_user_id="acme-corp",
    airbyte_client_id=os.environ["AIRBYTE_CLIENT_ID"],
    airbyte_client_secret=os.environ["AIRBYTE_CLIENT_SECRET"],
    auth_config=GongAccessKeyAuthenticationAuthConfig(
        access_key=os.environ["GONG_ACCESS_KEY"],
        access_key_secret=os.environ["GONG_ACCESS_KEY_SECRET"]
    ),
    name="Gong Source"
)
```

### GitHub with Personal Access Token

```python
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

connector = await GithubConnector.create_hosted(
    external_user_id="user_123",
    airbyte_client_id=os.environ["AIRBYTE_CLIENT_ID"],
    airbyte_client_secret=os.environ["AIRBYTE_CLIENT_SECRET"],
    auth_config=GithubPersonalAccessTokenAuthConfig(
        token=os.environ["GITHUB_TOKEN"]
    ),
    name="GitHub Source"
)
```

## Using Existing Connectors

Once a connector is created, you don't need to pass `auth_config` again:

```python
# Option A: Look up by external_user_id
connector = StripeConnector(
    external_user_id="user_123",
    airbyte_client_id=os.environ["AIRBYTE_CLIENT_ID"],
    airbyte_client_secret=os.environ["AIRBYTE_CLIENT_SECRET"],
)

# Option B: Use connector_id directly (if you have it cached)
connector = StripeConnector(
    connector_id="your-connector-uuid",  # From previous create_hosted() or API
    airbyte_client_id=os.environ["AIRBYTE_CLIENT_ID"],
    airbyte_client_secret=os.environ["AIRBYTE_CLIENT_SECRET"],
)

# Operations use credentials stored in Airbyte
result = await connector.execute("customers", "list", {"limit": 10})
```

## OAuth Connectors (Salesforce, HubSpot, Google Drive, etc.)

OAuth connectors require a server-side flow to capture user authorization.

### Step 1: Initiate OAuth

```python
from airbyte_agent_salesforce import SalesforceConnector

# Start the OAuth flow
oauth_response = await SalesforceConnector.initiate_oauth(
    external_user_id="user_123",
    airbyte_client_id=os.environ["AIRBYTE_CLIENT_ID"],
    airbyte_client_secret=os.environ["AIRBYTE_CLIENT_SECRET"],
    redirect_url="https://yourapp.com/oauth/callback"
)

# Redirect user to the consent URL
print(f"Redirect user to: {oauth_response.consent_url}")
```

### Step 2: Handle OAuth Callback

When the user completes authorization, they're redirected to your callback URL with a `secret_id` parameter:

```
https://yourapp.com/oauth/callback?secret_id=abc123
```

### Step 3: Create Connector with OAuth Secret

```python
connector = await SalesforceConnector.create_hosted(
    external_user_id="user_123",
    airbyte_client_id=os.environ["AIRBYTE_CLIENT_ID"],
    airbyte_client_secret=os.environ["AIRBYTE_CLIENT_SECRET"],
    server_side_oauth_secret_id="abc123",  # From callback
    name="Salesforce Source"
)
```

### OAuth Connectors Reference

| Connector | OAuth Required | Notes |
|-----------|----------------|-------|
| Salesforce | Yes | Requires Connected App setup |
| HubSpot | Optional | Can also use Private App token |
| Google Drive | Yes | Requires Google Cloud project |
| Amazon Ads | Yes | Requires Amazon Developer account |
| Facebook Marketing | Yes | Requires Facebook App |
| Zendesk Chat | Yes | Requires Zendesk OAuth app |
| GitHub | Optional | Can also use PAT |

## Making Connectors Visible in the UI

After `create_hosted()` succeeds, the connector is functional programmatically. To make it appear in the Airbyte UI's Connectors page, you must register it as a template.

### Register a UI Template

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

| Parameter | Description |
|-----------|-------------|
| `actor_definition_id` | Connector definition ID from the [Connector Definition IDs table](programmatic-setup.md#connector-definition-ids) |
| `name` | Display name shown in the UI card |
| `original_source_template_id` | Always pass `""` (empty string) — required by the API |
| `partial_default_config` | Pre-filled configuration values (usually `{}`) |
| `mode` | Always use `DIRECT`. If the API rejects the mode, check the error for accepted values |

### Get the Application Token

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/account/applications/token' \
  -H 'Content-Type: application/json' \
  -d '{
    "client_id": "<AIRBYTE_CLIENT_ID>",
    "client_secret": "<AIRBYTE_CLIENT_SECRET>"
  }'
```

Use the `access_token` from the response as `<APPLICATION_TOKEN>`.

### Example: Register Gong Connector

```bash
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

After registration, your connector appears in the Connectors page with a card showing the name and "Direct" badge.

## Creating Connector Instances

After registering a template, you need to create an actual connector instance to access data.

> **Note:** `create_hosted()` has a known URL bug. Use the HTTP API above until the SDK is updated.

### Step 1: List Workspaces

First, find your workspace name:

```bash
curl 'https://api.airbyte.ai/api/v1/workspaces' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>'
```

Use the workspace `name` (not `id`) as your `external_user_id` when creating connectors.

### Step 2: Create Instance

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "external_user_id": "<YOUR_WORKSPACE_NAME>",
    "workspace_name": "<YOUR_WORKSPACE_NAME>",
    "definition_id": "<DEFINITION_ID>",
    "name": "my-connector",
    "credentials": {
      // Connector-specific fields ONLY - no auth_type or credentials_title
    }
  }'
```

### Credentials Format by Connector

| Connector | Credentials Fields |
|-----------|-------------------|
| Gong | `{"access_key": "...", "access_key_secret": "..."}` |
| Stripe | `{"api_key": "sk_live_..."}` |
| GitHub | `{"token": "ghp_..."}` |
| Slack | `{"token": "xoxb-..."}` |

**Do NOT include discriminator fields like `auth_type` or `credentials_title`** — the API infers auth type from the credentials structure and rejects these.

### Step 3: Verify Connection

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors/<CONNECTOR_ID>/execute' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"entity": "users", "action": "list", "params": {"limit": 1}}'
```

A successful response confirms your connector is working.

## Verifying Connector in UI

After registering the template:

1. Go to [app.airbyte.ai](https://app.airbyte.ai)
2. Navigate to **Connectors** page
3. Your connector should appear with the name you specified and a "Direct" badge
4. Click to view status, configuration, and usage

## Entity Cache

Platform connectors support entity caching for faster repeated queries. Entity cache is managed through the Airbyte UI:

1. Go to [app.airbyte.ai](https://app.airbyte.ai)
2. Select your connector
3. Enable entity cache in the connector settings

When entity cache is enabled:
- Common queries are cached and served faster
- Cache syncs automatically in the background
- View cache status in the Airbyte UI

## Environment Variables Setup

Create a `.env` file for your platform credentials:

```bash
# Airbyte Platform (from app.airbyte.ai > Settings > API Keys)
AIRBYTE_CLIENT_ID=your_client_id
AIRBYTE_CLIENT_SECRET=your_client_secret

# Connector credentials (varies by connector)
STRIPE_API_KEY=sk_live_...
GONG_ACCESS_KEY=...
GONG_ACCESS_KEY_SECRET=...
GITHUB_TOKEN=ghp_...
```

Load in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

# Now use os.environ to access credentials
```

## Troubleshooting Platform Setup

### "Invalid client credentials"
- Verify `AIRBYTE_CLIENT_ID` and `AIRBYTE_CLIENT_SECRET` are correct
- Regenerate API keys in app.airbyte.ai > Settings > API Keys

### "Connector not appearing in UI"
- Ensure `create_hosted()` completed without errors
- Check the `external_user_id` matches your workspace
- Refresh the UI page

### "OAuth flow failing"
- Verify redirect URL matches exactly
- Check OAuth app settings in the third-party service
- Ensure required scopes are configured

### "`create_hosted()` not found"
- Update your SDK: `pip install --upgrade airbyte-agent-{connector}`
- `create_hosted()` was added in SDK v0.1.0

## Complete Setup Checklist

Follow these steps IN ORDER. Do not skip ahead.

### Prerequisites
- [ ] Airbyte Cloud account at app.airbyte.ai
- [ ] Connector credentials (API key, OAuth app, etc.)

### Step 1: Get Application Token (REQUIRED)
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/account/applications/token' \
  -H 'Content-Type: application/json' \
  -d '{"client_id": "<CLIENT_ID>", "client_secret": "<CLIENT_SECRET>"}'
```
Save the `access_token` as APPLICATION_TOKEN.

> **Token TTL:** Tokens expire after 15 minutes. Re-run this step if you get unauthorized errors later.

### Step 2: Detect Workspace
```bash
curl 'https://api.airbyte.ai/api/v1/workspaces' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>'
```
- If ONE workspace: use it automatically
- If MULTIPLE: ask user which workspace to use

### Step 3: Check if Template Exists (CRITICAL)
```bash
curl 'https://api.airbyte.ai/api/v1/integrations/templates/sources' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>'
```
Look for an existing template for your connector.
- If template EXISTS: skip to Step 5
- If NO template: proceed to Step 4

### Step 4: Register Template (Required if none exists)

**You need the Definition ID for your connector:**

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

Register the template:
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/templates/sources' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -d '{
    "actor_definition_id": "<DEFINITION_ID>",
    "name": "<CONNECTOR_NAME>",
    "original_source_template_id": "",
    "partial_default_config": {},
    "mode": "DIRECT"
  }'
```
Use `"mode": "DIRECT"` for all connectors. If the API rejects the mode, check the error for accepted values.

**Idempotency Note:** If you get "already exists" error, a template with that name already exists. Either:
- Use a different name, OR
- Skip this step and use the existing template

### Step 5: Create Connector Instance
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "external_user_id": "<WORKSPACE_NAME>",
    "workspace_name": "<WORKSPACE_NAME>",
    "definition_id": "<DEFINITION_ID>",
    "name": "my-connector",
    "credentials": {
      "api_key": "..."
    }
  }'
```
- `external_user_id`: Your identifier for this user/tenant (use workspace name for simplicity)
- `definition_id`: The connector definition ID from the table in Step 4
- **Note:** Do NOT include discriminator fields like `auth_type` or `credentials_title` in credentials — the API infers auth type and rejects these.

> **Note:** `create_hosted()` has a known URL bug. Use the HTTP API above until the SDK is updated.

### Step 6: Verify with Test Query
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors/<CONNECTOR_ID>/execute' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"entity": "users", "action": "list", "params": {"limit": 1}}'
```

### Step 7: Create .env File
Create `.env` in the connector directory:
```bash
AIRBYTE_CLIENT_ID=...
AIRBYTE_CLIENT_SECRET=...
# Connector-specific credentials
API_KEY=...
```

**Confirm**: "Connector created and verified! Pulled [N] records successfully."

## Related Documentation

- [OSS Setup](oss-setup.md) - Local SDK without platform integration
- [Authentication](authentication.md) - Auth patterns by connector
- [Programmatic Setup](programmatic-setup.md) - HTTP API and curl examples
- [Troubleshooting](troubleshooting.md) - Common errors and solutions
- [Entity-Action API](entity-action-api.md) - Core API patterns
