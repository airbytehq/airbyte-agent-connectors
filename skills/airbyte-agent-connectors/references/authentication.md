# Authentication

Airbyte Agent Connectors support multiple authentication methods depending on the underlying API. This guide covers the authentication types, how to configure them, and best practices for credential management.

## Contents

- [Authentication Overview](#authentication-overview)
- [API Key Authentication](#api-key-authentication)
- [Personal Access Token (PAT)](#personal-access-token-pat)
- [OAuth 2.0](#oauth-20)
- [Hosted Execution (Airbyte Agent Engine)](#hosted-execution-airbyte-agent-engine)
- [Multi-Auth Connectors](#multi-auth-connectors)
- [Best Practices](#best-practices)
- [Security Best Practices](#security-best-practices)
- [Connector-Specific Documentation](#connector-specific-documentation)

## Authentication Overview

### Authentication Types by Connector

| Connector | API Key | OAuth 2.0 | Personal Access Token |
|-----------|:-------:|:---------:|:---------------------:|
| Airtable | ✓ | | |
| Amazon Ads | | ✓ | |
| Asana | | | ✓ |
| Facebook Marketing | | ✓ | |
| GitHub | | ✓ | ✓ |
| Gong | ✓ | | |
| Google Drive | | ✓ | |
| Greenhouse | ✓ | | |
| HubSpot | ✓ | ✓ | |
| Intercom | ✓ | | |
| Jira | ✓ | | |
| Klaviyo | ✓ | | |
| Linear | ✓ | | |
| Mailchimp | ✓ | | |
| Orb | ✓ | | |
| Salesforce | | ✓ | |
| Shopify | ✓ | | |
| Slack | | | ✓ (Bot Token) |
| Stripe | ✓ | | |
| Zendesk Chat | | ✓ | |
| Zendesk Support | ✓ | ✓ | |

## API Key Authentication

The simplest authentication method. You provide an API key directly to the connector.

### Configuration

```python
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

connector = StripeConnector(
    auth_config=StripeAuthConfig(
        api_key="sk_live_your_api_key"
    )
)
```

### Obtaining API Keys

| Connector | Where to Get Key |
|-----------|------------------|
| Stripe | [Dashboard > Developers > API keys](https://dashboard.stripe.com/apikeys) |
| HubSpot | Settings > Integrations > Private Apps |
| Jira | Account Settings > Security > API tokens |
| Intercom | Settings > Developers > Access tokens |
| Airtable | Account > Developer hub > Personal access tokens |

### Environment Variables

Store API keys in environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()

connector = StripeConnector(
    auth_config=StripeAuthConfig(
        api_key=os.environ["STRIPE_API_KEY"]
    )
)
```

## Personal Access Token (PAT)

Similar to API keys but typically scoped to a user account rather than an application.

### GitHub PAT

```python
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

connector = GithubConnector(
    auth_config=GithubPersonalAccessTokenAuthConfig(
        token="ghp_your_personal_access_token"
    )
)
```

**Creating a GitHub PAT:**
1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token" (classic or fine-grained)
3. Select required scopes (e.g., `repo`, `read:org`)
4. Copy the token immediately (it won't be shown again)

### Slack Bot Token

```python
from airbyte_agent_slack import SlackConnector
from airbyte_agent_slack.models import SlackAuthConfig

connector = SlackConnector(
    auth_config=SlackAuthConfig(
        token="xoxb-your-bot-token"
    )
)
```

**Creating a Slack Bot Token:**
1. Go to [Slack API Apps](https://api.slack.com/apps)
2. Create a new app or select existing
3. Navigate to OAuth & Permissions
4. Add required scopes (e.g., `channels:read`, `chat:write`)
5. Install to workspace
6. Copy the Bot User OAuth Token

## OAuth 2.0

OAuth provides delegated access without sharing credentials. Connectors handle token refresh automatically.

### OAuth with Access Token

If you already have an OAuth access token:

```python
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubOauth2AuthConfig

connector = GithubConnector(
    auth_config=GithubOauth2AuthConfig(
        access_token="gho_your_oauth_token"
    )
)
```

### OAuth with Refresh Token

For long-lived access with automatic token refresh:

```python
from airbyte_agent_salesforce import SalesforceConnector
from airbyte_agent_salesforce.models import SalesforceOAuthConfig

connector = SalesforceConnector(
    auth_config=SalesforceOAuthConfig(
        client_id="your_client_id",
        client_secret="your_client_secret",
        refresh_token="your_refresh_token"
    )
)
```

The connector automatically refreshes the access token when it expires.

### Setting Up OAuth Credentials

#### Salesforce

1. Create a Connected App in Salesforce Setup
2. Enable OAuth settings
3. Add required scopes (`api`, `refresh_token`, `offline_access`)
4. Use the Consumer Key (client_id) and Consumer Secret (client_secret)
5. Complete OAuth flow to obtain refresh_token

#### HubSpot

```python
from airbyte_agent_hubspot import HubspotConnector
from airbyte_agent_hubspot.models import HubspotOAuthConfig

connector = HubspotConnector(
    auth_config=HubspotOAuthConfig(
        client_id="your_client_id",
        client_secret="your_client_secret",
        refresh_token="your_refresh_token"
    )
)
```

#### Google Drive

```python
from airbyte_agent_google_drive import GoogleDriveConnector
from airbyte_agent_google_drive.models import GoogleDriveOAuthConfig

connector = GoogleDriveConnector(
    auth_config=GoogleDriveOAuthConfig(
        client_id="your_client_id",
        client_secret="your_client_secret",
        refresh_token="your_refresh_token"
    )
)
```

## Hosted Execution (Airbyte Agent Engine)

> **Note:** `AirbyteHostedAuthConfig` has been renamed to `AirbyteAuthConfig` in the SDK.

For production deployments, you can store credentials in Airbyte Agent Engine and execute operations via API. **Sign up once, then everything is programmatic.**

### Getting Started

**One-time manual step**: Sign up at [app.airbyte.ai](https://app.airbyte.ai) and get your `airbyte_client_id` and `airbyte_client_secret` from the settings page.

After this, you can create connectors, manage credentials, and execute operations entirely through code - no UI needed.

**Prefer terminal/curl over Python?** See [Programmatic Setup](./programmatic-setup.md) for HTTP API examples with curl commands.

### Understanding `external_user_id`

The `external_user_id` is **your identifier** for the user or tenant - you define it (e.g., `"user_123"`, `"acme-corp"`, `"tenant_abc"`). It's used to:
- Scope connectors to specific users in multi-tenant applications
- Look up existing connectors when you don't have the `connector_id` cached

### Creating a New Hosted Connector

Use `create_hosted()` to register a new connector with credentials stored in Airbyte:

```python
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

# Create and register a new connector
connector = await StripeConnector.create_hosted(
    external_user_id="user_123",      # Your identifier for this user/tenant
    airbyte_client_id="...",          # From app.airbyte.ai settings
    airbyte_client_secret="...",      # From app.airbyte.ai settings
    auth_config=StripeAuthConfig(api_key="sk_live_...")
)

# Connector is now registered - use it immediately
result = await connector.execute("customers", "list", {"limit": 10})
```

### Using an Existing Hosted Connector

Once a connector is created, instantiate it without `auth_config` to use the stored credentials:

```python
from airbyte_agent_stripe import StripeConnector

# Option A: Look up by external_user_id
connector = StripeConnector(
    external_user_id="user_123",      # Looks up existing connector for this user
    airbyte_client_id="...",
    airbyte_client_secret="...",
)

# Option B: Use connector_id directly (if you have it cached)
connector = StripeConnector(
    connector_id="your-connector-uuid",  # From previous create_hosted() or API
    airbyte_client_id="...",
    airbyte_client_secret="...",
)

# Operations use credentials stored in Airbyte
result = await connector.execute("customers", "list", {"limit": 10})
```

### Complete Hosted Flow Example

Here's the full flow from zero to working:

```python
import os
from airbyte_agent_gong import GongConnector
from airbyte_agent_gong.models import GongAccessKeyAuthenticationAuthConfig

# Airbyte credentials (from app.airbyte.ai settings)
AIRBYTE_CLIENT_ID = os.environ["AIRBYTE_CLIENT_ID"]
AIRBYTE_CLIENT_SECRET = os.environ["AIRBYTE_CLIENT_SECRET"]

# First time: Create the connector
connector = await GongConnector.create_hosted(
    external_user_id="acme-corp",     # Your tenant identifier
    airbyte_client_id=AIRBYTE_CLIENT_ID,
    airbyte_client_secret=AIRBYTE_CLIENT_SECRET,
    auth_config=GongAccessKeyAuthenticationAuthConfig(
        access_key=os.environ["GONG_ACCESS_KEY"],
        access_key_secret=os.environ["GONG_ACCESS_KEY_SECRET"]
    ),
)

# Subsequent calls: Just reference the existing connector
connector = GongConnector(
    external_user_id="acme-corp",
    airbyte_client_id=AIRBYTE_CLIENT_ID,
    airbyte_client_secret=AIRBYTE_CLIENT_SECRET,
)

# Execute operations
calls = await connector.execute("calls", "list", {})
```

### Server-Side OAuth Flow

For OAuth connectors, implement the OAuth flow on your server:

**Step 1: Initiate OAuth**

```bash
curl -X POST "https://api.airbyte.ai/api/v1/integrations/connectors/oauth/initiate" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "external_user_id": "user_123",
    "definition_id": "b117307c-14b6-41aa-9422-947e34922962",
    "redirect_url": "https://yourapp.com/oauth/callback"
  }'
```

**Step 2: Redirect user to consent URL**

The response contains a `consent_url`. Redirect your user there to authorize.

**Step 3: Handle callback and create connector**

After authorization, the user is redirected to your callback URL with a `secret_id`. Use it to create the connector:

```bash
curl -X POST "https://api.airbyte.ai/api/v1/integrations/connectors" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "external_user_id": "user_123",
    "definition_id": "b117307c-14b6-41aa-9422-947e34922962",
    "name": "User Salesforce",
    "server_side_oauth_secret_id": "<secret_id_from_callback>"
  }'
```

## Multi-Auth Connectors

Some connectors support multiple authentication methods. Choose based on your use case.

### Zendesk Support (API Token vs OAuth)

**API Token:**
```python
from airbyte_agent_zendesk_support import ZendeskSupportConnector
from airbyte_agent_zendesk_support.models import ZendeskAPITokenAuthConfig

connector = ZendeskSupportConnector(
    auth_config=ZendeskAPITokenAuthConfig(
        subdomain="yourcompany",
        email="admin@yourcompany.com",
        api_token="your_api_token"
    )
)
```

**OAuth:**
```python
from airbyte_agent_zendesk_support.models import ZendeskOAuthConfig

connector = ZendeskSupportConnector(
    auth_config=ZendeskOAuthConfig(
        subdomain="yourcompany",
        access_token="oauth_access_token"
    )
)
```

### HubSpot (Private App vs OAuth)

> **Platform Mode note:** The Airbyte API only recognizes the OAuth auth scheme for HubSpot. Private App tokens work in OSS Mode but not in Platform Mode. Use OAuth credentials (`client_id`, `client_secret`, `refresh_token`) when creating connectors via the HTTP API or `create_hosted()`. See the [HubSpot OAuth setup](#hubspot) above for a code example, or [HubSpot AUTH.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/hubspot/AUTH.md) for step-by-step credential setup.

**Private App Token (OSS Mode only):**
```python
from airbyte_agent_hubspot.models import HubspotPrivateAppAuthConfig

connector = HubspotConnector(
    auth_config=HubspotPrivateAppAuthConfig(
        access_token="pat-na1-xxx"
    )
)
```

**OAuth (OSS and Platform Mode):**
```python
from airbyte_agent_hubspot.models import HubspotOAuthConfig

connector = HubspotConnector(
    auth_config=HubspotOAuthConfig(
        client_id="...",
        client_secret="...",
        refresh_token="..."
    )
)
```

## Best Practices

### Credential Security

1. **Never commit credentials** to version control
2. **Use environment variables** or secret managers
3. **Rotate credentials** regularly
4. **Use minimum required scopes** for OAuth/PAT

### Environment Configuration

```python
# .env file
GITHUB_TOKEN=ghp_xxx
STRIPE_API_KEY=sk_live_xxx
SALESFORCE_CLIENT_ID=xxx
SALESFORCE_CLIENT_SECRET=xxx
SALESFORCE_REFRESH_TOKEN=xxx

# Python
import os
from dotenv import load_dotenv

load_dotenv()

# Access credentials
github_token = os.environ["GITHUB_TOKEN"]
stripe_key = os.environ["STRIPE_API_KEY"]
```

### Production Recommendations

| Environment | Recommendation |
|-------------|----------------|
| Development | `.env` file with test/sandbox credentials |
| Staging | Environment variables from CI/CD |
| Production | Secret manager (AWS Secrets Manager, HashiCorp Vault, etc.) or Airbyte Cloud hosted execution |

## Security Best Practices

- **Never commit credentials** to git
- Use `.env` files for development (add to `.gitignore`)
- Use secret managers for production (AWS Secrets Manager, HashiCorp Vault)
- Rotate credentials regularly

```python
import os
from dotenv import load_dotenv
load_dotenv()

connector = StripeConnector(
    auth_config=StripeAuthConfig(api_key=os.environ["STRIPE_API_KEY"])
)
```

## Connector-Specific Documentation

Each connector's AUTH.md has complete authentication details:

- [GitHub AUTH.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/github/AUTH.md) - PAT and OAuth
- [Stripe AUTH.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/stripe/AUTH.md) - API Key
- [Salesforce AUTH.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/salesforce/AUTH.md) - OAuth with refresh
- [HubSpot AUTH.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/hubspot/AUTH.md) - Private App and OAuth
- [Zendesk Support AUTH.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/zendesk-support/AUTH.md) - API Token and OAuth

See the connector's AUTH.md for:
- All supported authentication methods
- Required fields for each auth type
- Step-by-step credential setup
- Example code for open source and hosted execution
