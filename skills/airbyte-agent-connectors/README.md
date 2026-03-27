# Airbyte Agent Connectors — Agent Skill

> An agent skill for setting up and operating 51+ Airbyte Agent Connectors
> through a unified entity-action interface.

## What This Skill Does

Once installed, Claude gains the knowledge to help you set up and use Airbyte Agent Connectors in **Platform Mode** (Airbyte Cloud) or **OSS Mode** (local SDK). It covers authentication, the entity-action API, framework integration (PydanticAI, LangChain), and MCP configuration for Claude Desktop/Code.

## Install

```bash
npx skills add airbytehq/airbyte-agent-connectors
```

Or in Claude Code:
```
/install airbytehq/airbyte-agent-connectors
```

## Try It

After installing, ask Claude:

- "Set up a Stripe connector in Platform Mode"
- "Connect to GitHub using OSS Mode"
- "Configure Airbyte MCP tools"

## Supported Connectors

51+ connectors including Airtable, Amazon Ads, Asana, Chargebee, ClickUp, Confluence, Facebook Marketing, Freshdesk, GitHub, GitLab, Gmail, Gong, Google Ads, Google Analytics, Google Drive, Google Search Console, Granola, Greenhouse, Harvest, HubSpot, Incident.io, Intercom, Jira, Klaviyo, Linear, LinkedIn Ads, Mailchimp, Monday, Notion, Orb, PayPal, Pinterest, Pylon, Salesforce, Sendgrid, Sentry, Shopify, Slack, Snapchat Marketing, Stripe, TikTok Marketing, Twilio, Typeform, WooCommerce, Zendesk Chat, Zendesk Support, Zendesk Talk, Zoho CRM, and more.

See the [connector index](references/connector-index.md) for the full list.

## Documentation

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Agent instructions (Claude reads this) |
| [Getting Started](references/getting-started.md) | Installation and first connector |
| [Platform Setup](references/platform-setup.md) | Airbyte Cloud setup |
| [OSS Setup](references/oss-setup.md) | Local SDK setup |
| [Programmatic Setup](references/programmatic-setup.md) | HTTP API setup with curl |
| [Authentication](references/authentication.md) | Auth patterns per connector |
| [Entity-Action API](references/entity-action-api.md) | API usage patterns |
| [MCP Integration](references/mcp-integration.md) | Claude Desktop/Code MCP |
| [Troubleshooting](references/troubleshooting.md) | Common issues |

## Requirements

- Python 3.11+
- `uv` recommended for package management

## License

[Elastic-2.0](../../LICENSE)
