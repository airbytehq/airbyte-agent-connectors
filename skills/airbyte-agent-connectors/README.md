# Airbyte Agent Connectors — Claude Code Skill

> A Claude Code skill for setting up and operating 21 Airbyte Agent Connectors
> through a unified entity-action interface.

## What This Skill Does

Once installed, Claude gains the knowledge to help you set up and use Airbyte Agent Connectors in **Platform Mode** (Airbyte Cloud) or **OSS Mode** (local SDK). It covers authentication, the entity-action API, framework integration (PydanticAI, LangChain), and MCP configuration for Claude Desktop/Code.

## Install

### Via plugin marketplace

In Claude Code, run:
```
/plugin marketplace add airbytehq/airbyte-agent-connectors
```
Then install the plugin:
```
/plugin install airbyte-agent-connectors@airbyte-agent-connectors
```

### Manual

```bash
mkdir -p .claude/skills
git clone --depth 1 https://github.com/airbytehq/airbyte-agent-connectors.git /tmp/airbyte-skills
cp -r /tmp/airbyte-skills/skills/airbyte-agent-connectors .claude/skills/
rm -rf /tmp/airbyte-skills
```

## Try It

After installing, ask Claude:

- "Set up a Stripe connector in Platform Mode"
- "Connect to GitHub using OSS Mode"
- "Configure Airbyte MCP tools"

## Supported Connectors

Airtable, Amazon Ads, Asana, Facebook Marketing, GitHub, Gong, Google Drive, Greenhouse, HubSpot, Intercom, Jira, Klaviyo, Linear, Mailchimp, Orb, Salesforce, Shopify, Slack, Stripe, Zendesk Chat, Zendesk Support

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
