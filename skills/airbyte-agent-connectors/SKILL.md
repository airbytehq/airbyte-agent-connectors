---
name: airbyte-agent-connectors
description: |
  Documentation and setup guidance for Airbyte Agent Connectors — strongly typed
  Python packages for accessing 21+ third-party APIs (Salesforce, HubSpot, GitHub,
  Slack, Stripe, Jira, and more). Covers Platform Mode (Airbyte Cloud) and OSS Mode
  (local SDK). Includes authentication, entity-action APIs, PydanticAI/LangChain
  integration, and optional MCP integration for Claude Desktop/Code.
license: Elastic-2.0
metadata:
  author: Airbyte
  version: 1.0.0
  repo: https://github.com/airbytehq/airbyte-agent-connectors
  mcp-server: airbyte-agent-mcp
---

# Airbyte Agent Connectors

Airbyte Agent Connectors let AI agents call third-party APIs through strongly typed, well-documented tools. Each connector is a standalone Python package.

> **Important:** This skill provides documentation and setup guidance. When helping users set up connectors, follow the documented workflows in the "Common Workflows" section below. Do NOT attempt to import Python modules, verify package installations, or run code to check configurations—simply guide users through the steps using the code examples provided in this documentation.

## Mode Detection

**First, determine which mode the user needs:**

### Platform Mode (Airbyte Cloud)
Use when:
- Environment has `AIRBYTE_CLIENT_ID` + `AIRBYTE_CLIENT_SECRET`
- User wants connectors visible in the Airbyte UI at app.airbyte.ai
- User needs managed credential storage, entity cache, or multi-tenant deployments

### OSS Mode (Open Source / Local SDK)
Use when:
- User wants to run connectors directly without platform integration
- User is doing quick development or prototyping
- User wants Claude Code/Desktop integration via MCP only

> **Ask if unclear:** "Are you using Airbyte Platform (app.airbyte.ai) or open source connectors?"

---

## Supported Connectors Check

**IMPORTANT:** Before proceeding with any setup, verify the requested connector is in this list:

| Connector | Auth Type |
|-----------|-----------|
| Airtable | API Key |
| Amazon Ads | OAuth |
| Asana | API Key |
| Facebook Marketing | OAuth |
| GitHub | PAT |
| Gong | API Key |
| Google Drive | OAuth |
| Greenhouse | API Key |
| HubSpot | API Key or OAuth |
| Intercom | API Key |
| Jira | API Key |
| Klaviyo | API Key |
| Linear | API Key |
| Mailchimp | API Key |
| Orb | API Key |
| Salesforce | OAuth |
| Shopify | API Key |
| Slack | Bot Token |
| Stripe | API Key |
| Zendesk Chat | OAuth |
| Zendesk Support | API Key |

**If the connector is NOT in this list:** Inform the user that this connector isn't available yet. Point them to:
- GitHub issues: https://github.com/airbytehq/airbyte-agent-connectors/issues
- Request a new connector by opening an issue

---

## Platform Mode Quick Start

For users with Airbyte Platform credentials.

### Prerequisites

Get credentials from [app.airbyte.ai](https://app.airbyte.ai) > Settings > API Keys:
- `AIRBYTE_CLIENT_ID`
- `AIRBYTE_CLIENT_SECRET`

### Create a Connector

```python
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

connector = await StripeConnector.create_hosted(
    external_user_id="user_123",      # Your identifier for this user/tenant
    airbyte_client_id="...",          # From app.airbyte.ai
    airbyte_client_secret="...",
    auth_config=StripeAuthConfig(api_key="sk_live_...")
)
# Connector is created and ready to use programmatically
```

### Register in UI (Required for UI Visibility)

After creating the connector programmatically, register it as a template to make it appear in the Airbyte UI's Connectors page.

**Get an Application Token first:**
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/account/applications/token' \
  -H 'Content-Type: application/json' \
  -d '{"client_id": "<AIRBYTE_CLIENT_ID>", "client_secret": "<AIRBYTE_CLIENT_SECRET>"}'
```

**Then register the template:**
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/templates/sources' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -d '{
    "actor_definition_id": "<CONNECTOR_DEFINITION_ID>",
    "name": "Stripe",
    "partial_default_config": {},
    "mode": "DIRECT"
  }'
```

- Get `actor_definition_id` from the [Connector Definition IDs table](references/programmatic-setup.md#connector-definition-ids)
- If registration fails with "already exists", a template with that name already exists—choose a different name

Your connector now appears in the Connectors page at [app.airbyte.ai](https://app.airbyte.ai) with a "Direct" badge.

### Use Existing Connector

```python
connector = StripeConnector(
    external_user_id="user_123",
    airbyte_client_id="...",
    airbyte_client_secret="...",
)
result = await connector.execute("customers", "list", {"limit": 10})
```

**For OAuth connectors and complete platform setup:** See [Platform Setup Reference](references/platform-setup.md)

---

## OSS Mode Quick Start

For users running connectors locally without platform integration.

### Install

```bash
# Using uv (recommended)
uv add airbyte-agent-github

# Or using pip in a virtual environment
python3 -m venv .venv && source .venv/bin/activate
pip install airbyte-agent-github
```

> **Note:** When working in the `airbyte-agent-connectors` repo, packages are already available—no installation needed.

### Use Directly

```python
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

connector = GithubConnector(
    auth_config=GithubPersonalAccessTokenAuthConfig(token="ghp_your_token")
)

result = await connector.execute("issues", "list", {
    "owner": "airbytehq",
    "repo": "airbyte",
    "states": ["OPEN"],
    "per_page": 10
})
```

### Add to Claude via MCP

```bash
claude mcp add airbyte-agent-mcp --scope project
```

**For MCP configuration and complete OSS setup:** See [OSS Setup Reference](references/oss-setup.md)

---

## Available Connectors

> **Gating Check:** If the user requests a connector NOT in this list, inform them it's not yet supported and suggest they open a GitHub issue at https://github.com/airbytehq/airbyte-agent-connectors/issues.

All 21 connectors follow the same entity-action pattern: `connector.execute(entity, action, params)`

| Connector | Package | Auth Type | Key Entities |
|-----------|---------|-----------|--------------|
| [Airtable](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/airtable) | `airbyte-agent-airtable` | API Key | bases, tables, records |
| [Amazon Ads](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/amazon-ads) | `airbyte-agent-amazon-ads` | OAuth2 | campaigns, ad_groups, ads |
| [Asana](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/asana) | `airbyte-agent-asana` | PAT | projects, tasks, users |
| [Facebook Marketing](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/facebook-marketing) | `airbyte-agent-facebook-marketing` | OAuth2 | campaigns, ad_sets, ads |
| [GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/github) | `airbyte-agent-github` | PAT/OAuth2 | repositories, issues, pull_requests |
| [Gong](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/gong) | `airbyte-agent-gong` | API Key | calls, users, deals |
| [Google Drive](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/google-drive) | `airbyte-agent-google-drive` | OAuth2 | files, folders |
| [Greenhouse](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/greenhouse) | `airbyte-agent-greenhouse` | API Key | applications, candidates, jobs |
| [HubSpot](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/hubspot) | `airbyte-agent-hubspot` | OAuth2/API Key | contacts, companies, deals |
| [Intercom](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/intercom) | `airbyte-agent-intercom` | API Key | contacts, conversations, companies |
| [Jira](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/jira) | `airbyte-agent-jira` | API Key | issues, projects, users |
| [Klaviyo](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/klaviyo) | `airbyte-agent-klaviyo` | API Key | profiles, lists, campaigns |
| [Linear](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/linear) | `airbyte-agent-linear` | API Key | issues, projects, teams |
| [Mailchimp](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/mailchimp) | `airbyte-agent-mailchimp` | API Key | lists, campaigns, members |
| [Orb](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/orb) | `airbyte-agent-orb` | API Key | customers, subscriptions, invoices |
| [Salesforce](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/salesforce) | `airbyte-agent-salesforce` | OAuth2 | accounts, contacts, opportunities |
| [Shopify](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/shopify) | `airbyte-agent-shopify` | API Key | orders, products, customers |
| [Slack](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/slack) | `airbyte-agent-slack` | Bot Token | channels, messages, users |
| [Stripe](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/stripe) | `airbyte-agent-stripe` | API Key | customers, payments, invoices |
| [Zendesk Chat](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/zendesk-chat) | `airbyte-agent-zendesk-chat` | OAuth2 | chats, visitors, agents |
| [Zendesk Support](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/zendesk-support) | `airbyte-agent-zendesk-support` | OAuth2/API Key | tickets, users, organizations |

---

## Entity-Action API Pattern

All connectors use the same interface:

```python
result = await connector.execute(entity, action, params)
# result.data contains the records (list or dict depending on action)
# result.meta contains pagination info for list operations
```

### Actions

| Action | Description | `result.data` Type |
|--------|-------------|-------------------|
| `list` | Get multiple records | `list[dict]` |
| `get` | Get single record by ID | `dict` |
| `create` | Create new record | `dict` |
| `update` | Modify existing record | `dict` |
| `delete` | Remove record | `dict` |
| `api_search` | Native API search syntax | `list[dict]` |

### Quick Examples

```python
# List
await connector.execute("customers", "list", {"limit": 10})

# Get
await connector.execute("customers", "get", {"id": "cus_xxx"})

# Search
await connector.execute("repositories", "api_search", {
    "query": "language:python stars:>1000"
})

# Create
await connector.execute("customers", "create", {
    "email": "user@example.com",
    "name": "Jane Doe"
})
```

### Pagination

```python
async def fetch_all(connector, entity, params=None):
    all_records = []
    cursor = None
    params = params or {}

    while True:
        if cursor:
            params["after"] = cursor
        result = await connector.execute(entity, "list", params)
        all_records.extend(result.data)

        if result.meta and hasattr(result.meta, 'pagination'):
            cursor = getattr(result.meta.pagination, 'cursor', None)
            if not cursor:
                break
        else:
            break

    return all_records
```

**For complete API reference:** See [Entity-Action API Reference](references/entity-action-api.md)

---

## Authentication Quick Reference

### API Key Connectors

```python
# Stripe
from airbyte_agent_stripe.models import StripeAuthConfig
auth_config=StripeAuthConfig(api_key="sk_live_...")

# Gong
from airbyte_agent_gong.models import GongAccessKeyAuthenticationAuthConfig
auth_config=GongAccessKeyAuthenticationAuthConfig(
    access_key="...", access_key_secret="..."
)

# HubSpot (Private App)
from airbyte_agent_hubspot.models import HubspotPrivateAppAuthConfig
auth_config=HubspotPrivateAppAuthConfig(access_token="pat-na1-...")
```

### Personal Access Token

```python
# GitHub
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig
auth_config=GithubPersonalAccessTokenAuthConfig(token="ghp_...")

# Slack
from airbyte_agent_slack.models import SlackAuthConfig
auth_config=SlackAuthConfig(token="xoxb-...")
```

### OAuth (requires refresh token)

```python
# Salesforce
from airbyte_agent_salesforce.models import SalesforceOAuthConfig
auth_config=SalesforceOAuthConfig(
    client_id="...", client_secret="...", refresh_token="..."
)
```

**For complete auth details:** See [Authentication Reference](references/authentication.md)

---

## Platform Mode: Complete Setup Checklist

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

---

## Handling "Already Exists" Errors

When running the Platform workflow multiple times, you may encounter:

| Error | Cause | Solution |
|-------|-------|----------|
| "Template already exists" | Template with this name registered | Use existing template or choose different name |
| "Connector already exists" | `external_user_id` already used | Retrieve existing connector instead of creating |
| "Workspace already exists" | Workspace with this name exists | Use existing workspace |

**Retrieving an existing connector:**
```python
# If connector was previously created, just reference it:
connector = StripeConnector(
    external_user_id="user_123",  # Same ID used during creation
    airbyte_client_id="...",
    airbyte_client_secret="..."
)
# This retrieves the existing connector - no re-auth needed
```

---

## OSS Mode: Setup Workflow

### OSS User: "Set up a [Connector] connector"

1. Ask for connector credentials (e.g., GitHub token, Stripe API key)
2. Guide local SDK usage:
   ```python
   from airbyte_agent_github import GithubConnector
   from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

   connector = GithubConnector(
       auth_config=GithubPersonalAccessTokenAuthConfig(token="ghp_...")
   )
   ```
3. Optionally: Guide MCP server setup for Claude integration

---

## File Placement

> **Important:** When working in the `airbyte-agent-connectors` repo, place ALL files (`.env`, scripts, examples) in the specific connector directory, NOT the repo root.

| Working in... | Put files in... | Example |
|---------------|-----------------|---------|
| `airbyte-agent-connectors` repo | `connectors/{connector}/` | `connectors/gong/.env`, `connectors/gong/example.py` |
| Your own project | Project root | `.env`, `main.py` |

**In the airbyte-agent-connectors repo:**
- `.env` files go in `connectors/{connector}/.env`
- Test scripts go in `connectors/{connector}/`
- Virtual environments should be created in the connector directory if needed
- Each connector directory is self-contained

---

## Framework Integration

### PydanticAI

```python
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o", system_prompt="You help with GitHub data.")

@agent.tool_plain
async def github_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### LangChain

```python
from langchain.tools import StructuredTool
import asyncio

# For sync contexts, wrap the async call
def execute_sync(entity: str, action: str, params: dict):
    return asyncio.get_event_loop().run_until_complete(
        connector.execute(entity, action, params)
    )

github_tool = StructuredTool.from_function(
    func=execute_sync,
    name="github",
    description="Execute GitHub operations"
)
```

**Note:** If you're already in an async context, use LangChain's async tool support instead.

---

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

---

## Reference Documentation

> **Quick Reference:** Connector Definition IDs are inlined in the Platform Mode checklist above (Step 4). For additional HTTP API examples, see [Programmatic Setup](references/programmatic-setup.md).

| Topic | Link |
|-------|------|
| Platform Setup | [references/platform-setup.md](references/platform-setup.md) |
| OSS Setup | [references/oss-setup.md](references/oss-setup.md) |
| Getting Started | [references/getting-started.md](references/getting-started.md) |
| Entity-Action API | [references/entity-action-api.md](references/entity-action-api.md) |
| Authentication | [references/authentication.md](references/authentication.md) |
| Programmatic Setup | [references/programmatic-setup.md](references/programmatic-setup.md) |
| MCP Integration | [references/mcp-integration.md](references/mcp-integration.md) |
| Troubleshooting | [references/troubleshooting.md](references/troubleshooting.md) |

## Per-Connector Documentation

Each connector directory contains:
- **README.md** - Overview, example questions, basic usage
- **AUTH.md** - All authentication options
- **REFERENCE.md** - Complete entity/action reference with parameters

Example: `connectors/github/README.md`, `connectors/github/AUTH.md`, `connectors/github/REFERENCE.md`

---

## Support

- **Slack Community**: [slack.airbyte.com](https://slack.airbyte.com/)
- **GitHub Issues**: [airbytehq/airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors/issues)
- **Documentation**: [docs.airbyte.com/ai-agents](https://docs.airbyte.com/ai-agents)
