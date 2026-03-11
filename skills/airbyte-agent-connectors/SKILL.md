---
name: airbyte-agent-connectors
description: |
  Sets up and operates Airbyte Agent Connectors -- strongly typed Python packages
  for accessing 49+ third-party APIs (Salesforce, HubSpot, GitHub, Slack, Stripe,
  Jira, and more) through a unified entity-action interface. Use when the user wants
  to connect to a SaaS API, set up an Airbyte connector, integrate third-party data
  into an AI agent, or configure MCP tools for Claude. Covers Platform Mode (Airbyte
  Cloud) and OSS Mode (local SDK).
---

# Airbyte Agent Connectors

Airbyte Agent Connectors let AI agents call third-party APIs through strongly typed, well-documented tools. Each connector is a standalone Python package.

> **Terminology:** **Platform Mode** = Airbyte Cloud at app.airbyte.ai (managed credentials, UI visibility). **OSS Mode** = local Python SDK (self-managed credentials, no cloud dependency). **Definition ID** = UUID that identifies a connector type in the Airbyte API (used in `definition_id` fields, not `connector_type` or `connector_definition_id`).

> **Important:** This skill provides documentation and setup guidance. When helping users set up connectors, follow the documented workflows below. Do NOT attempt to import Python modules, verify package installations, or run code to check configurations -- simply guide users through the steps using the code examples provided.

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

## Supported Connectors

49 connectors available. All connectors follow the same entity-action pattern: `connector.execute(entity, action, params)`

| Connector | Package | Auth Type | Key Entities |
|-----------|---------|-----------|--------------|
| [Stripe](references/connectors/stripe.md) | `airbyte-agent-stripe` | Token | Customers, Invoices, Charges, Subscri... |
| [HubSpot](references/connectors/hubspot.md) | `airbyte-agent-hubspot` | OAuth | Contacts, Companies, Deals, Tickets, ... |
| [GitHub](references/connectors/github.md) | `airbyte-agent-github` | OAuth, Token | Repositories, Org Repositories, Branc... |
| [Salesforce](references/connectors/salesforce.md) | `airbyte-agent-salesforce` | OAuth | Sobjects, Accounts, Contacts, Leads, ... |
| [Gong](references/connectors/gong.md) | `airbyte-agent-gong` | OAuth, Token | Users, Calls, Calls Extensive, Call A... |

> **Full table:** See [references/connector-index.md](references/connector-index.md) for all 49 connectors with auth types, key entities, and documentation status.

**If the connector is NOT in the index:** Inform the user that this connector isn't available yet. Point them to [GitHub issues](https://github.com/airbytehq/airbyte-agent-connectors/issues).

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
    external_user_id="user_123",
    airbyte_client_id="...",
    airbyte_client_secret="...",
    auth_config=StripeAuthConfig(api_key="sk_live_...")
)
```

### Use Existing Connector

```python
connector = StripeConnector(
    external_user_id="user_123",
    airbyte_client_id="...",
    airbyte_client_secret="...",
)
result = await connector.execute("customers", "list", {"limit": 10})
```

---

## OSS Mode Quick Start

### Install

```bash
# Using uv (recommended)
uv add airbyte-agent-github

# Or using pip in a virtual environment
python3 -m venv .venv && source .venv/bin/activate
pip install airbyte-agent-github
```

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
from airbyte_agent_salesforce.models import SalesforceAuthConfig
auth_config=SalesforceAuthConfig(
    client_id="...", client_secret="...", refresh_token="..."
)
```

> **Per-connector auth details:** Each connector reference in [references/connectors/](references/connectors/) includes the specific auth class name and fields.

---

## Security Best Practices

- Never hard-code credentials in source files. Use environment variables or `.env` files.
- Use `.env` pattern: `from dotenv import load_dotenv; load_dotenv()`
- Rotate tokens regularly. Use short-lived tokens where possible.
- For production, use Platform Mode for managed credential storage.

---

## Per-Connector Reference Documentation

- [Connector Index](references/connector-index.md) -- full table of all connectors
- Per-connector references: [references/connectors/](references/connectors/)

Each per-connector reference includes: package name and version, authentication details, available entities and actions, quick-start code snippets, and links to full GitHub documentation.

## Reference Documentation

| Topic | Reference |
|-------|----------|
| Getting Started | [references/getting-started.md](references/getting-started.md) |
| Platform Setup | [references/platform-setup.md](references/platform-setup.md) |
| OSS Setup | [references/oss-setup.md](references/oss-setup.md) |
| Entity-Action API | [references/entity-action-api.md](references/entity-action-api.md) |
| Authentication | [references/authentication.md](references/authentication.md) |
| Programmatic Setup | [references/programmatic-setup.md](references/programmatic-setup.md) |
| MCP Integration | [references/mcp-integration.md](references/mcp-integration.md) |
| Troubleshooting | [references/troubleshooting.md](references/troubleshooting.md) |

## How References Are Generated

Reference docs are auto-generated by `scripts/generate_skill_references.py`.
Run `python scripts/generate_skill_references.py --all` to regenerate all
references, or `--connector <name>` for a specific connector.

---

## Skill Metadata

- **Author:** Airbyte
- **Version:** 1.2.0
- **License:** Elastic-2.0
- **Compatibility:** Requires Python 3.11+. Recommends uv for package management.
- **Repository:** https://github.com/airbytehq/airbyte-agent-connectors
- **MCP Server:** airbyte-agent-mcp

## Support

- **Slack Community**: [slack.airbyte.com](https://slack.airbyte.com/)
- **GitHub Issues**: [airbytehq/airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors/issues)
- **Documentation**: [docs.airbyte.com/ai-agents](https://docs.airbyte.com/ai-agents)
