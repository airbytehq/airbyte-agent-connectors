# Platform Setup (Airbyte Cloud / Hosted Mode)

This guide covers setting up connectors through the Airbyte Platform (app.airbyte.ai), where connectors appear in your dashboard and credentials are managed securely.

## When to Use Platform Mode

Use platform mode when you want:
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

# Connector is now registered and visible in your Airbyte dashboard
# The connector object can be used immediately for operations

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
    "partial_default_config": {},
    "mode": "DIRECT"
  }'
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `actor_definition_id` | Connector definition ID from the [Connector Definition IDs table](programmatic-setup.md#connector-definition-ids) |
| `name` | Display name shown in the UI card |
| `partial_default_config` | Pre-filled configuration values (usually `{}`) |
| `mode` | Template mode: `DIRECT` for API-key connectors, `OAUTH` for OAuth connectors |

### Get the Application Token

```bash
curl -X POST 'https://api.airbyte.com/v1/applications/token' \
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
    "partial_default_config": {},
    "mode": "DIRECT"
  }'
```

After registration, your connector appears in the Connectors page with a card showing the name and "Direct" badge.

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

## Related Documentation

- [OSS Setup](oss-setup.md) - Local SDK without platform integration
- [Authentication](authentication.md) - Auth patterns by connector
- [Programmatic Setup](programmatic-setup.md) - HTTP API and curl examples
- [Troubleshooting](troubleshooting.md) - Common errors and solutions
- [Entity-Action API](entity-action-api.md) - Core API patterns
