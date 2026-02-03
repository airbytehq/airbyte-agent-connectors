---
name: airbyte-agent-connectors
description: |
  Set up and configure Airbyte Agent Connectors for AI agent applications.
  Use when working with Airbyte, agent connectors, data integration for agents,
  connecting to Salesforce/HubSpot/GitHub/Slack/Stripe via agents, or building
  agentic data pipelines. Helps with authentication, connector selection,
  entity-action APIs, framework integration (PydanticAI, LangChain), and MCP setup.
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

## Available Connectors

All 21 connectors follow the same entity-action pattern. Each has README.md, AUTH.md, and REFERENCE.md in its directory.

| Connector | Package | Auth Type | Key Entities |
|-----------|---------|-----------|--------------|
| [Airtable](./connectors/airtable/) | `airbyte-agent-airtable` | API Key | bases, tables, records |
| [Amazon Ads](./connectors/amazon-ads/) | `airbyte-agent-amazon-ads` | OAuth2 | campaigns, ad_groups, ads |
| [Asana](./connectors/asana/) | `airbyte-agent-asana` | PAT | projects, tasks, users |
| [Facebook Marketing](./connectors/facebook-marketing/) | `airbyte-agent-facebook-marketing` | OAuth2 | campaigns, ad_sets, ads |
| [GitHub](./connectors/github/) | `airbyte-agent-github` | PAT/OAuth2 | repositories, issues, pull_requests |
| [Gong](./connectors/gong/) | `airbyte-agent-gong` | API Key | calls, users, deals |
| [Google Drive](./connectors/google-drive/) | `airbyte-agent-google-drive` | OAuth2 | files, folders |
| [Greenhouse](./connectors/greenhouse/) | `airbyte-agent-greenhouse` | API Key | applications, candidates, jobs |
| [HubSpot](./connectors/hubspot/) | `airbyte-agent-hubspot` | OAuth2/API Key | contacts, companies, deals |
| [Intercom](./connectors/intercom/) | `airbyte-agent-intercom` | API Key | contacts, conversations, companies |
| [Jira](./connectors/jira/) | `airbyte-agent-jira` | API Key | issues, projects, users |
| [Klaviyo](./connectors/klaviyo/) | `airbyte-agent-klaviyo` | API Key | profiles, lists, campaigns |
| [Linear](./connectors/linear/) | `airbyte-agent-linear` | API Key | issues, projects, teams |
| [Mailchimp](./connectors/mailchimp/) | `airbyte-agent-mailchimp` | API Key | lists, campaigns, members |
| [Orb](./connectors/orb/) | `airbyte-agent-orb` | API Key | customers, subscriptions, invoices |
| [Salesforce](./connectors/salesforce/) | `airbyte-agent-salesforce` | OAuth2 | accounts, contacts, opportunities |
| [Shopify](./connectors/shopify/) | `airbyte-agent-shopify` | API Key | orders, products, customers |
| [Slack](./connectors/slack/) | `airbyte-agent-slack` | Bot Token | channels, messages, users |
| [Stripe](./connectors/stripe/) | `airbyte-agent-stripe` | API Key | customers, payments, invoices |
| [Zendesk Chat](./connectors/zendesk-chat/) | `airbyte-agent-zendesk-chat` | OAuth2 | chats, visitors, agents |
| [Zendesk Support](./connectors/zendesk-support/) | `airbyte-agent-zendesk-support` | OAuth2/API Key | tickets, users, organizations |

## Setup Patterns

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

### 2. Hosted Engine (Airbyte Cloud)

Store credentials securely in Airbyte Cloud and execute via API:

```python
from airbyte_agent_stripe import StripeConnector

connector = StripeConnector(
    external_user_id="user_123",
    airbyte_client_id="your_client_id",
    airbyte_client_secret="your_client_secret"
)
```

Best for: Multi-tenant SaaS, production deployments, credential management at scale.

### 3. MCP Server

Expose connectors through Model Context Protocol for Claude and other LLM tools:

```bash
# Add to Claude Code
claude mcp add airbyte-agent-mcp --scope project
```

Best for: Claude Desktop, Claude Code, any MCP-compatible LLM interface.

## Framework Integration

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
- **[MCP Integration](./skill-references/mcp-integration.md)** - MCP server setup, Claude Code/Desktop config
- **[Troubleshooting](./skill-references/troubleshooting.md)** - Common errors, rate limiting, debugging

## Per-Connector Documentation

Each connector directory contains:

- **README.md** - Overview, example questions, installation, basic usage
- **AUTH.md** - All authentication options (open source and hosted)
- **REFERENCE.md** - Complete entity/action reference with parameters

Example: For GitHub details, see:
- [connectors/github/README.md](./connectors/github/README.md)
- [connectors/github/AUTH.md](./connectors/github/AUTH.md)
- [connectors/github/REFERENCE.md](./connectors/github/REFERENCE.md)

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
