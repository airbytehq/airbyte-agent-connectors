# OSS Setup (Open Source / Local SDK)

This guide covers using Airbyte Agent Connectors directly via the Python SDK without platform integration. Use this approach when you want to run connectors locally with your own credential management.

## Contents

- [When to Use OSS Mode](#when-to-use-oss-mode)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [OAuth Connectors (Local Mode)](#oauth-connectors-local-mode)
- [Environment Setup](#environment-setup)
- [MCP Server Setup for Claude](#mcp-server-setup-for-claude)
- [Agent Framework Integration](#agent-framework-integration)
- [Credential Security Best Practices](#credential-security-best-practices)
- [Common Operations Quick Reference](#common-operations-quick-reference)
- [Troubleshooting](#troubleshooting)
- [Setup Workflow](#setup-workflow)
- [Related Documentation](#related-documentation)

## When to Use OSS Mode

Use OSS Mode when you want:
- Quick development and prototyping
- Self-hosted deployments
- Single-tenant applications
- Direct control over credentials
- No dependency on Airbyte Cloud
- Claude Code/Desktop integration via MCP

## Installation

Install connectors individually based on the services you need:

```bash
# Using uv (recommended)
uv add airbyte-agent-github
uv add airbyte-agent-stripe
uv add airbyte-agent-salesforce

# Or using pip in a virtual environment
python3 -m venv .venv && source .venv/bin/activate
pip install airbyte-agent-github
pip install airbyte-agent-stripe
pip install airbyte-agent-salesforce
```

> **Note:** When working in the `airbyte-agent-connectors` repo, packages are already available—no installation needed.

All connectors follow the naming pattern `airbyte-agent-{service}`.

## Basic Usage

### API Key Connectors

```python
import asyncio
import os
from dotenv import load_dotenv
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

load_dotenv()

async def main():
    connector = StripeConnector(
        auth_config=StripeAuthConfig(api_key=os.environ["STRIPE_API_KEY"])
    )

    result = await connector.execute("customers", "list", {"limit": 10})
    for customer in result.data:
        print(f"{customer['id']}: {customer.get('email', 'No email')}")

asyncio.run(main())
```

### GitHub with Personal Access Token

```python
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

connector = GithubConnector(
    auth_config=GithubPersonalAccessTokenAuthConfig(
        token=os.environ["GITHUB_TOKEN"]
    )
)

# List repositories
result = await connector.execute("repositories", "list", {
    "username": "octocat",
    "per_page": 10
})
```

### Gong with API Key

```python
from airbyte_agent_gong import GongConnector
from airbyte_agent_gong.models import GongAccessKeyAuthenticationAuthConfig

connector = GongConnector(
    auth_config=GongAccessKeyAuthenticationAuthConfig(
        access_key=os.environ["GONG_ACCESS_KEY"],
        access_key_secret=os.environ["GONG_ACCESS_KEY_SECRET"]
    )
)

# List calls
result = await connector.execute("calls", "list", {})
```

### Slack with Bot Token

```python
from airbyte_agent_slack import SlackConnector
from airbyte_agent_slack.models import SlackAuthConfig

connector = SlackConnector(
    auth_config=SlackAuthConfig(token=os.environ["SLACK_BOT_TOKEN"])
)

# List channels
result = await connector.execute("channels", "list", {})
```

### HubSpot with Private App Token

```python
from airbyte_agent_hubspot import HubspotConnector
from airbyte_agent_hubspot.models import HubspotPrivateAppAuthConfig

connector = HubspotConnector(
    auth_config=HubspotPrivateAppAuthConfig(
        access_token=os.environ["HUBSPOT_ACCESS_TOKEN"]
    )
)

# List contacts
result = await connector.execute("contacts", "list", {"limit": 100})
```

## OAuth Connectors (Local Mode)

For OAuth connectors in OSS Mode, you need to handle the OAuth flow yourself and provide the tokens directly:

### Salesforce with OAuth

```python
from airbyte_agent_salesforce import SalesforceConnector
from airbyte_agent_salesforce.models import SalesforceOAuthConfig

connector = SalesforceConnector(
    auth_config=SalesforceOAuthConfig(
        client_id=os.environ["SALESFORCE_CLIENT_ID"],
        client_secret=os.environ["SALESFORCE_CLIENT_SECRET"],
        refresh_token=os.environ["SALESFORCE_REFRESH_TOKEN"]
    )
)

# The connector handles token refresh automatically
result = await connector.execute("accounts", "list", {"limit": 50})
```

### HubSpot with OAuth

```python
from airbyte_agent_hubspot import HubspotConnector
from airbyte_agent_hubspot.models import HubspotOAuthConfig

connector = HubspotConnector(
    auth_config=HubspotOAuthConfig(
        client_id=os.environ["HUBSPOT_CLIENT_ID"],
        client_secret=os.environ["HUBSPOT_CLIENT_SECRET"],
        refresh_token=os.environ["HUBSPOT_REFRESH_TOKEN"]
    )
)
```

## Environment Setup

Create a `.env` file in your project root:

```bash
# GitHub (Personal Access Token)
GITHUB_TOKEN=ghp_your_token_here

# Stripe (API Key)
STRIPE_API_KEY=sk_live_your_key_here

# Gong (API Key pair)
GONG_ACCESS_KEY=your_access_key
GONG_ACCESS_KEY_SECRET=your_access_key_secret

# Slack (Bot Token)
SLACK_BOT_TOKEN=xoxb-your-token

# HubSpot (Private App Token)
HUBSPOT_ACCESS_TOKEN=pat-na1-xxx

# Jira (API Token)
JIRA_API_TOKEN=your_api_token
JIRA_EMAIL=your_email@example.com
JIRA_DOMAIN=your-domain.atlassian.net

# Salesforce (OAuth - requires completing OAuth flow first)
SALESFORCE_CLIENT_ID=your_client_id
SALESFORCE_CLIENT_SECRET=your_client_secret
SALESFORCE_REFRESH_TOKEN=your_refresh_token
```

## MCP Server Setup for Claude

Expose your connectors to Claude Code or Claude Desktop via MCP.

### Step 1: Configure Connectors

Create `configured_connectors.yaml` in the `airbyte-agent-mcp` directory:

```yaml
connectors:
  # Stripe - API Key
  - id: stripe
    type: local
    connector_name: stripe
    description: "Stripe payment processing"
    secrets:
      api_key: STRIPE_API_KEY

  # GitHub - Personal Access Token
  - id: github
    type: local
    connector_name: github
    description: "GitHub repositories and issues"
    secrets:
      token: GITHUB_TOKEN

  # Gong - API Key pair
  - id: gong
    type: local
    connector_name: gong
    description: "Gong conversation intelligence"
    secrets:
      access_key: GONG_ACCESS_KEY
      access_key_secret: GONG_ACCESS_KEY_SECRET

  # Slack - Bot Token
  - id: slack
    type: local
    connector_name: slack
    description: "Slack messaging"
    secrets:
      token: SLACK_BOT_TOKEN
```

### Step 2: Create .env File

Create `.env` in the `airbyte-agent-mcp` directory with your credentials:

```bash
STRIPE_API_KEY=sk_live_...
GITHUB_TOKEN=ghp_...
GONG_ACCESS_KEY=...
GONG_ACCESS_KEY_SECRET=...
SLACK_BOT_TOKEN=xoxb-...
```

### Step 3: Add to Claude Code

```bash
cd /path/to/your/project
claude mcp add airbyte-agent-mcp --scope project
```

When prompted, provide the server configuration:

```json
{
  "command": "uv",
  "args": [
    "--directory",
    "/path/to/airbyte-agent-connectors/airbyte-agent-mcp",
    "run",
    "airbyte_agent_mcp"
  ]
}
```

### Step 4: Add to Claude Desktop

Add to your Claude Desktop config:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "airbyte-agent-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/airbyte-agent-connectors/airbyte-agent-mcp",
        "run",
        "airbyte_agent_mcp"
      ]
    }
  }
}
```

Restart Claude Desktop after making changes.

## Agent Framework Integration

### PydanticAI

```python
from pydantic_ai import Agent
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

connector = GithubConnector(
    auth_config=GithubPersonalAccessTokenAuthConfig(token=os.environ["GITHUB_TOKEN"])
)

agent = Agent("openai:gpt-4o", system_prompt="You help with GitHub data.")

@agent.tool_plain
async def list_issues(owner: str, repo: str, limit: int = 10) -> str:
    """List open issues in a repository."""
    result = await connector.execute("issues", "list", {
        "owner": owner,
        "repo": repo,
        "states": ["OPEN"],
        "per_page": limit
    })
    return str(result.data)

@agent.tool_plain
async def get_repository(owner: str, repo: str) -> str:
    """Get repository details."""
    result = await connector.execute("repositories", "get", {
        "owner": owner,
        "repo": repo
    })
    return str(result.data)
```

### LangChain

```python
from langchain.tools import StructuredTool
import asyncio

# For sync contexts, wrap the async call properly
def execute_sync(entity: str, action: str, params: dict):
    """Wrapper for async connector.execute() in sync context."""
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(connector.execute(entity, action, params))

github_tool = StructuredTool.from_function(
    func=execute_sync,
    name="github",
    description="Execute GitHub operations"
)
```

**Note:** If you're already in an async context (e.g., inside an async function), use LangChain's async tool support or call `connector.execute()` directly with `await`.

## Credential Security Best Practices

### Development
- Use `.env` files (add to `.gitignore`)
- Use test/sandbox credentials when possible

### Production
- Use secret managers (AWS Secrets Manager, HashiCorp Vault)
- Never commit credentials to version control
- Rotate credentials regularly

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

## Common Operations Quick Reference

```python
# List operations
await connector.execute("customers", "list", {"limit": 10})
await connector.execute("issues", "list", {"owner": "org", "repo": "name", "states": ["OPEN"]})

# Get operations
await connector.execute("customers", "get", {"id": "cus_xxx"})
await connector.execute("repositories", "get", {"owner": "org", "repo": "name"})

# Search operations
await connector.execute("repositories", "api_search", {"query": "language:python stars:>1000"})
await connector.execute("customers", "api_search", {"query": "email:'user@example.com'"})

# Create operations (where supported)
await connector.execute("customers", "create", {"email": "user@example.com", "name": "Jane"})
```

## Troubleshooting

### "ModuleNotFoundError"
- Ensure the connector package is installed: `pip install airbyte-agent-{connector}`

### "401 Unauthorized"
- Verify credentials are correct and not expired
- Check token scopes/permissions

### "RuntimeWarning: coroutine was never awaited"
- Always use `await` with `connector.execute()`
- Run in async context with `asyncio.run(main())`

### MCP Server not starting
- Verify uv is installed: `uv --version`
- Check paths in configuration are correct
- Test manually: `cd airbyte-agent-mcp && uv run airbyte_agent_mcp`

## Setup Workflow

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

## Related Documentation

- [Platform Setup](platform-setup.md) - Hosted mode with UI visibility
- [MCP Integration](mcp-integration.md) - Detailed MCP server configuration
- [Authentication](authentication.md) - Auth patterns by connector
- [Entity-Action API](entity-action-api.md) - Core API patterns
- [Troubleshooting](troubleshooting.md) - Common errors and solutions
