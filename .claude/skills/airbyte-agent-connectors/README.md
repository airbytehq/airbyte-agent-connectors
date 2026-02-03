<p align="center">
  <a href="https://airbyte.com">
    <img src="https://raw.githubusercontent.com/airbytehq/airbyte/master/.github/octavia-ai-agent.png" alt="Airbyte" width="180" />
  </a>
</p>

<h1 align="center">Airbyte Agent Connectors</h1>

<p align="center">
  <strong>Give your AI agents access to 21 third-party APIs</strong>
</p>

<p align="center">
  <a href="https://github.com/airbytehq/airbyte-agent-connectors/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Elastic--2.0-blue" alt="License"></a>
  <a href="https://github.com/airbytehq/airbyte-agent-connectors"><img src="https://img.shields.io/badge/version-1.0.0-green" alt="Version"></a>
  <a href="#available-connectors"><img src="https://img.shields.io/badge/connectors-21-purple" alt="Connectors"></a>
  <a href="https://slack.airbyte.com/"><img src="https://img.shields.io/badge/slack-join-orange" alt="Slack"></a>
</p>

<p align="center">
  Salesforce, HubSpot, GitHub, Slack, Stripe, Jira, and more — all through strongly typed, well-documented tools. Use them directly in your app, plug into agent frameworks (PydanticAI, LangChain), or expose through MCP for Claude.
</p>

---

## Requirements

- Python 3.9+
- pip or uv

---

## Quick Start

### Installation

**Project Scope** (recommended for teams):
```bash
# Clone the skill into your project's .claude/skills/ directory
mkdir -p .claude/skills
git clone --depth 1 https://github.com/airbytehq/airbyte-agent-connectors.git /tmp/airbyte-skill
cp -r /tmp/airbyte-skill/.claude/skills/airbyte-agent-connectors .claude/skills/
rm -rf /tmp/airbyte-skill
```
> Available only in this project. Version-controlled with your code. Best for team collaboration and CI/CD.

**Global Scope** (for personal use):
```bash
# Clone to your home directory for all Claude Code sessions
mkdir -p ~/.claude/skills
git clone --depth 1 https://github.com/airbytehq/airbyte-agent-connectors.git /tmp/airbyte-skill
cp -r /tmp/airbyte-skill/.claude/skills/airbyte-agent-connectors ~/.claude/skills/
rm -rf /tmp/airbyte-skill
```
> Available in all your Claude Code sessions. Best for personal productivity and experimentation.

### Your First Connector

Install a connector and start making API calls:

```bash
pip install airbyte-agent-github
# or: uv add airbyte-agent-github
```

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

See the [full documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/SKILL.md) for all setup patterns and examples.

---

## What You Can Do

| Use Case | Example | Connectors |
|----------|---------|------------|
| **CRM Automation** | Sync contacts, enrich leads, update deal stages | Salesforce, HubSpot |
| **Support Ticket Analysis** | Analyze ticket patterns, auto-categorize issues | Zendesk, Intercom, Jira |
| **Sales Intelligence** | Transcribe calls, track deals, research accounts | Gong, Salesforce, HubSpot |
| **Marketing Ops** | Manage campaigns, sync audiences, track metrics | Klaviyo, Mailchimp, Facebook Marketing |
| **Developer Workflows** | Triage issues, review PRs, track projects | GitHub, Jira, Linear, Asana |
| **Data Integration** | Sync records, manage files, automate workflows | Airtable, Google Drive, Shopify |
| **Billing & Payments** | Customer management, invoice tracking, subscriptions | Stripe, Orb |
| **Team Communication** | Channel management, message search, user sync | Slack |

---

## Available Connectors

<details>
<summary><strong>View all 21 connectors</strong></summary>

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

</details>

---

## Architecture

Choose the right setup pattern for your use case:

```
                    ┌─────────────────────────────────────────┐
                    │           What are you building?        │
                    └─────────────────────────────────────────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    ▼                   ▼                   ▼
            ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
            │ Claude/LLM    │   │ Multi-tenant  │   │ Single-tenant │
            │ Integration   │   │ SaaS App      │   │ App/Script    │
            └───────┬───────┘   └───────┬───────┘   └───────┬───────┘
                    │                   │                   │
                    ▼                   ▼                   ▼
            ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
            │  MCP Server   │   │ Hosted Engine │   │   Local SDK   │
            └───────────────┘   └───────────────┘   └───────────────┘
```

| Pattern | Best For | Setup |
|---------|----------|-------|
| **Local SDK** | Development, scripts, single-tenant apps | `pip install airbyte-agent-{connector}` |
| **Hosted Engine** | Multi-tenant SaaS, managed credentials | [app.airbyte.ai](https://app.airbyte.ai) + SDK |
| **MCP Server** | Claude Desktop, Claude Code, LLM tools | `claude mcp add airbyte-agent-mcp` |

See the [full documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/SKILL.md#setup-patterns) for detailed setup instructions.

---

## Documentation

| Document | Description |
|----------|-------------|
| **[Full Documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/SKILL.md)** | Complete reference — quick start, all patterns, code examples |
| **[Getting Started](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/references/getting-started.md)** | Installation, environment setup, first connector |
| **[Entity-Action API](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/references/entity-action-api.md)** | Core API patterns, actions, pagination |
| **[Authentication](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/references/authentication.md)** | Auth types overview, OAuth setup |
| **[Programmatic Setup](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/references/programmatic-setup.md)** | Terminal/curl setup without UI |
| **[MCP Integration](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/references/mcp-integration.md)** | Claude Code/Desktop configuration |
| **[Troubleshooting](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/.claude/skills/airbyte-agent-connectors/references/troubleshooting.md)** | Common errors, debugging |

### Per-Connector Documentation

Each connector directory includes:
- **README.md** — Overview, example questions, basic usage
- **AUTH.md** — All authentication options
- **REFERENCE.md** — Complete entity/action reference

Example: [connectors/github/](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/github)

---

## Support

- **Slack Community**: [slack.airbyte.com](https://slack.airbyte.com/)
- **GitHub Issues**: [airbytehq/airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors/issues)
- **Documentation**: [docs.airbyte.com/ai-agents](https://docs.airbyte.com/ai-agents)

---

## License

[Elastic License 2.0](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/LICENSE) — Free for most uses. See license for details.

---

<p align="center">
  <sub>Built with ❤️ by <a href="https://airbyte.com">Airbyte</a></sub>
</p>
