---
name: airbyte-agent-connectors
description: |
  MCP server and tools for Claude to access third-party APIs (Salesforce, HubSpot,
  GitHub, Slack, Stripe, Jira, and 15+ more). Use for Claude Desktop integration,
  Claude Code MCP setup, or building AI agents with data connectors. Covers
  authentication, entity-action APIs, PydanticAI/LangChain integration, and
  programmatic connector setup.
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
curl -X POST 'https://api.airbyte.com/v1/applications/token' \
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

## Common Workflows

### Platform User: "Set up a Gong connector"

1. Check for platform credentials: "Do you have your Airbyte credentials (`AIRBYTE_CLIENT_ID`, `AIRBYTE_CLIENT_SECRET`)?"
2. If NO: "Go to [app.airbyte.ai](https://app.airbyte.ai) > Settings > API Keys to get them."
3. If YES: Ask for Gong credentials (access_key, access_key_secret)
4. Use `create_hosted()`:
   ```python
   connector = await GongConnector.create_hosted(
       external_user_id="your_tenant_id",
       airbyte_client_id=AIRBYTE_CLIENT_ID,
       airbyte_client_secret=AIRBYTE_CLIENT_SECRET,
       auth_config=GongAccessKeyAuthenticationAuthConfig(
           access_key="...", access_key_secret="..."
       ),
       name="Gong Source"
   )
   ```
5. Register the connector template so it appears in the UI (see [Programmatic Setup](references/programmatic-setup.md#pattern-c-ui-template-registration) for the API call). Use Gong's definition ID from the [Connector Definition IDs table](references/programmatic-setup.md#connector-definition-ids).
6. Confirm: "Connector created and registered! It now appears in your Airbyte Connectors page at [app.airbyte.ai](https://app.airbyte.ai)."

### OSS User: "Set up a GitHub connector"

1. Ask for GitHub token (Personal Access Token)
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
