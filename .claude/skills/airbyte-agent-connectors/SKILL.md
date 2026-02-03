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

Airbyte Agent Connectors let AI agents call third-party APIs through strongly typed, well-documented tools. Each connector is a standalone Python package that you can use directly in your app, plug into an agent framework (PydanticAI, LangChain), or expose through MCP.

## Quick Start

Install a connector and execute operations in under 10 lines:

```python
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

connector = GithubConnector(
    auth_config=GithubPersonalAccessTokenAuthConfig(token="ghp_your_token")
)

# List open issues
result = await connector.execute("issues", "list", {
    "owner": "airbytehq",
    "repo": "airbyte",
    "states": ["OPEN"],
    "per_page": 10
})
print(result.data)
```

Installation:

```bash
pip install airbyte-agent-github
# or
uv add airbyte-agent-github
```

### File Placement

When creating files (.env, scripts, examples), place them based on context:

| Working in... | Put files in... |
|---------------|-----------------|
| `airbyte-agent-connectors` repo | The specific connector directory (e.g., `connectors/gong/`) |
| Your own project | Your project root |

**In the airbyte-agent-connectors repo:** Each connector directory (`connectors/{name}/`) is self-contained. Put .env files, test scripts, and examples there—not in the repo root.

## Available Connectors

All 21 connectors follow the same entity-action pattern. Each has README.md, AUTH.md, and REFERENCE.md in its directory.

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

## Setup Patterns

### Choosing a Setup Pattern

| If you need... | Use |
|----------------|-----|
| Quick development/prototyping | Local SDK |
| Single-tenant production app | Local SDK |
| Multi-tenant SaaS | Hosted Engine |
| Managed credential storage | Hosted Engine |
| Claude Desktop/Claude Code integration | MCP Server |
| LLM tool discovery | MCP Server |

**Decision flow:**
1. Building for Claude/LLM tools? → MCP Server
2. Multi-tenant or need managed credentials? → Hosted Engine
3. Otherwise → Local SDK

### 1. Local SDK (Open Source)

Run connectors directly in your application with your own API credentials:

```python
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

connector = StripeConnector(
    auth_config=StripeAuthConfig(api_key="sk_live_...")
)
```

Best for: Development, self-hosted deployments, single-tenant applications.

### 2. Hosted Engine (Airbyte Agent Engine)

For multi-tenant apps or managed credential storage.

**Setup options:**
- **Programmatic (terminal/API)**: Create connectors via curl or scripts—see [Programmatic Setup](./skill-references/programmatic-setup.md)
- **Python SDK**: Use `create_hosted()` (shown below)
- **UI**: Sign up at [app.airbyte.ai](https://app.airbyte.ai) for visual configuration

**One-time setup**: Get `airbyte_client_id` and `airbyte_client_secret` from app.airbyte.ai settings.

**Step 1: Create a connector (first time)**
```python
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

connector = await StripeConnector.create_hosted(
    external_user_id="user_123",      # Your identifier for this user/tenant (you define this)
    airbyte_client_id="...",          # From app.airbyte.ai settings
    airbyte_client_secret="...",      # From app.airbyte.ai settings
    auth_config=StripeAuthConfig(api_key="sk_live_...")
)
# Connector is now registered in Airbyte - no UI needed
```

**Step 2: Use existing connector (subsequent calls)**
```python
connector = StripeConnector(
    external_user_id="user_123",      # Same identifier - looks up existing connector
    airbyte_client_id="...",
    airbyte_client_secret="...",
)
result = await connector.execute("customers", "list", {})
```

**Note**: `external_user_id` is YOUR identifier (user ID, tenant name, etc.) that you define. It's used to scope and look up connectors in multi-tenant apps.

Best for: Multi-tenant SaaS, production deployments, credential management at scale.

### 3. MCP Server

Expose connectors through Model Context Protocol for Claude and other LLM tools:

```bash
# Add to Claude Code
claude mcp add airbyte-agent-mcp --scope project
```

Best for: Claude Desktop, Claude Code, any MCP-compatible LLM interface.

## Security Best Practices

**Never commit credentials to git.** Use environment variables or secret managers.

### Environment Variables (Development)
```python
import os
from dotenv import load_dotenv
load_dotenv()

connector = StripeConnector(
    auth_config=StripeAuthConfig(api_key=os.environ["STRIPE_API_KEY"])
)
```

### Secret Manager (Production)
```python
# AWS Secrets Manager example
import boto3
import json

def get_secret(secret_name: str) -> dict:
    client = boto3.client("secretsmanager")
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])

secrets = get_secret("my-app/stripe")
connector = StripeConnector(
    auth_config=StripeAuthConfig(api_key=secrets["api_key"])
)
```

### Credential Rotation
- Use Hosted Engine for automatic credential management
- For local SDK, implement rotation in your deployment pipeline
- Never hardcode credentials in source code

## Common Mistakes

Avoid these patterns when using Airbyte Agent Connectors:

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Hardcoding credentials in code | Security risk, can't rotate | Use environment variables or secret managers |
| Creating new connector on every request | Wastes resources, hits rate limits | Reuse connector instances; use `external_user_id` lookup |
| Ignoring pagination | Missing data on large datasets | Always check `result.meta.has_more` and paginate |
| Not handling rate limits | Requests fail unexpectedly | Implement exponential backoff; check connector's rate limit docs |
| Using `create_hosted()` without caching `connector_id` | Extra API calls on every request | Cache the returned `connector_id` after first creation |
| Mixing token types in API calls | Auth failures | Application token for setup, scoped token for user operations |

## Framework Integration

### Choosing a Framework

| Framework | Best For | Trade-offs |
|-----------|----------|------------|
| **Direct SDK** | Maximum control, minimal overhead | No agent orchestration |
| **PydanticAI** | Type-safe agents, structured outputs | Newer ecosystem |
| **LangChain** | Large ecosystem, many integrations | More abstraction layers |
| **MCP** | Claude-native, tool discovery | Claude-specific |

**Recommendation:** Start with Direct SDK for simple use cases. Add PydanticAI when you need agent orchestration with type safety.

### PydanticAI

```python
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o", system_prompt="You help with GitHub data.")

@agent.tool_plain
@GithubConnector.tool_utils
async def github_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### LangChain

```python
from langchain.tools import StructuredTool

github_tool = StructuredTool.from_function(
    func=lambda entity, action, params: connector.execute(entity, action, params),
    name="github",
    description="Execute GitHub operations"
)
```

## Reference Documentation

For detailed information, see:

- **[Getting Started](./skill-references/getting-started.md)** - Installation, environment setup, first connector
- **[Entity-Action API](./skill-references/entity-action-api.md)** - Core API patterns, actions, pagination
- **[Authentication](./skill-references/authentication.md)** - Auth types overview, OAuth setup
- **[Programmatic Setup](./skill-references/programmatic-setup.md)** - Terminal/curl setup without UI (tokens, HTTP API)
- **[MCP Integration](./skill-references/mcp-integration.md)** - MCP server setup, Claude Code/Desktop config
- **[Troubleshooting](./skill-references/troubleshooting.md)** - Common errors, rate limiting, debugging

## Per-Connector Documentation

Each connector directory contains:

- **README.md** - Overview, example questions, installation, basic usage
- **AUTH.md** - All authentication options (open source and hosted)
- **REFERENCE.md** - Complete entity/action reference with parameters

Example: For GitHub details, see:
- [connectors/github/README.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/github/README.md)
- [connectors/github/AUTH.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/github/AUTH.md)
- [connectors/github/REFERENCE.md](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/github/REFERENCE.md)

## Quick Reference

Common operations across all connectors. Copy-paste these patterns and adapt for your use case.

### List Operations

| Connector | Entity | Example |
|-----------|--------|---------|
| GitHub | issues | `await connector.execute("issues", "list", {"owner": "org", "repo": "name", "states": ["OPEN"]})` |
| GitHub | pull_requests | `await connector.execute("pull_requests", "list", {"owner": "org", "repo": "name", "states": ["OPEN"]})` |
| Stripe | customers | `await connector.execute("customers", "list", {"limit": 10})` |
| Stripe | invoices | `await connector.execute("invoices", "list", {"customer": "cus_xxx"})` |
| Salesforce | accounts | `await connector.execute("accounts", "list", {"limit": 50})` |
| Salesforce | opportunities | `await connector.execute("opportunities", "list", {"limit": 50})` |
| HubSpot | contacts | `await connector.execute("contacts", "list", {"limit": 100})` |
| HubSpot | deals | `await connector.execute("deals", "list", {"limit": 100})` |
| Slack | channels | `await connector.execute("channels", "list", {})` |
| Jira | issues | `await connector.execute("issues", "list", {"project": "PROJ"})` |

### Get Operations

| Connector | Entity | Example |
|-----------|--------|---------|
| GitHub | issues | `await connector.execute("issues", "get", {"owner": "org", "repo": "name", "number": 123})` |
| GitHub | repositories | `await connector.execute("repositories", "get", {"owner": "org", "repo": "name"})` |
| Stripe | customers | `await connector.execute("customers", "get", {"id": "cus_xxx"})` |
| Stripe | invoices | `await connector.execute("invoices", "get", {"id": "in_xxx"})` |
| Salesforce | accounts | `await connector.execute("accounts", "get", {"id": "001xxx"})` |
| HubSpot | contacts | `await connector.execute("contacts", "get", {"id": "123"})` |
| Jira | issues | `await connector.execute("issues", "get", {"issue_key": "PROJ-123"})` |

### Search Operations

| Connector | Entity | Example Query Syntax |
|-----------|--------|---------------------|
| GitHub | repositories | `"language:python stars:>1000 topic:ml"` |
| GitHub | issues | `"is:open label:bug author:username"` |
| Stripe | customers | `"email:'user@example.com' AND metadata['plan']:'pro'"` |
| Salesforce | accounts | `"Industry = 'Technology' AND AnnualRevenue > 1000000"` |
| Salesforce | contacts | `"Email LIKE '%@example.com'"` |

### Create Operations (where supported)

```python
# Stripe: Create customer
await connector.execute("customers", "create", {
    "email": "user@example.com",
    "name": "Jane Doe",
    "metadata": {"source": "agent"}
})

# Stripe: Create product
await connector.execute("products", "create", {
    "name": "Premium Plan",
    "description": "Full access subscription"
})
```

### Pagination Pattern

```python
async def fetch_all(connector, entity, params=None):
    """Fetch all records with automatic pagination."""
    all_records = []
    cursor = None
    params = params or {}

    while True:
        if cursor:
            params["after"] = cursor  # or "starting_after" for Stripe

        result = await connector.execute(entity, "list", params)
        if not result.success:
            break

        all_records.extend(result.data)

        if result.meta and result.meta.get("has_more"):
            cursor = result.meta.get("next_cursor")
        else:
            break

    return all_records
```

## Support

- **Slack Community**: [slack.airbyte.com](https://slack.airbyte.com/)
- **GitHub Issues**: [airbytehq/airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors/issues)
- **Documentation**: [docs.airbyte.com/ai-agents](https://docs.airbyte.com/ai-agents)
