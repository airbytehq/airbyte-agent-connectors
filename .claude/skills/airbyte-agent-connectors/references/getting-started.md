# Getting Started with Airbyte Agent Connectors

This guide walks you through installing your first connector, setting up authentication, and executing your first operation.

## Prerequisites

- Python 3.11 or later
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- API credentials for the service you want to connect to

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

All connectors follow the naming pattern `airbyte-agent-{service}`:

| Service | Package |
|---------|---------|
| Airtable | `airbyte-agent-airtable` |
| Amazon Ads | `airbyte-agent-amazon-ads` |
| Asana | `airbyte-agent-asana` |
| Facebook Marketing | `airbyte-agent-facebook-marketing` |
| GitHub | `airbyte-agent-github` |
| Gong | `airbyte-agent-gong` |
| Google Drive | `airbyte-agent-google-drive` |
| Greenhouse | `airbyte-agent-greenhouse` |
| HubSpot | `airbyte-agent-hubspot` |
| Intercom | `airbyte-agent-intercom` |
| Jira | `airbyte-agent-jira` |
| Klaviyo | `airbyte-agent-klaviyo` |
| Linear | `airbyte-agent-linear` |
| Mailchimp | `airbyte-agent-mailchimp` |
| Orb | `airbyte-agent-orb` |
| Salesforce | `airbyte-agent-salesforce` |
| Shopify | `airbyte-agent-shopify` |
| Slack | `airbyte-agent-slack` |
| Stripe | `airbyte-agent-stripe` |
| Zendesk Chat | `airbyte-agent-zendesk-chat` |
| Zendesk Support | `airbyte-agent-zendesk-support` |

### Version Pinning (Recommended for Production)

For production stability, pin connector versions in your `pyproject.toml` or `requirements.txt`:

```bash
# Pin to specific version
uv add airbyte-agent-github==0.18.78
pip install airbyte-agent-stripe==0.5.75

# Or specify in requirements.txt
airbyte-agent-github==0.18.78
airbyte-agent-stripe==0.5.75
airbyte-agent-salesforce>=0.1.0,<0.2.0
```

Check connector versions in their CHANGELOG.md files or on PyPI.

## Environment Setup

### Using .env Files

Create a `.env` file in your project root:

```bash
# GitHub
GITHUB_ACCESS_TOKEN=ghp_your_token_here

# Stripe
STRIPE_API_KEY=sk_live_your_key_here

# Salesforce (OAuth)
SALESFORCE_CLIENT_ID=your_client_id
SALESFORCE_CLIENT_SECRET=your_client_secret
SALESFORCE_REFRESH_TOKEN=your_refresh_token

# OpenAI (for LLM-based agents)
OPENAI_API_KEY=sk-your_key_here
```

Load environment variables in your code:

```python
from dotenv import load_dotenv
import os

load_dotenv()

github_token = os.environ["GITHUB_ACCESS_TOKEN"]
```

### Obtaining Credentials

Each connector's AUTH.md file documents how to obtain credentials:

| Connector | Credential Type | How to Obtain |
|-----------|-----------------|---------------|
| GitHub | Personal Access Token | [GitHub Settings > Developer settings > Tokens](https://github.com/settings/tokens) |
| Stripe | API Key | [Stripe Dashboard > Developers > API keys](https://dashboard.stripe.com/apikeys) |
| Slack | Bot Token | [Slack API > Create App > OAuth & Permissions](https://api.slack.com/apps) |
| HubSpot | Private App Token | [HubSpot > Settings > Integrations > Private Apps](https://developers.hubspot.com/docs/api/private-apps) |
| Salesforce | OAuth Credentials | [Salesforce Setup > App Manager > Connected App](https://help.salesforce.com/s/articleView?id=sf.connected_app_create.htm) |

For detailed authentication instructions, see the connector's AUTH.md:
- [GitHub AUTH.md](../connectors/github/AUTH.md)
- [Stripe AUTH.md](../connectors/stripe/AUTH.md)
- [Salesforce AUTH.md](../connectors/salesforce/AUTH.md)

## Your First Connector: GitHub Example

### Step 1: Create Project

```bash
uv init my-agent-app --app
cd my-agent-app
uv add airbyte-agent-github python-dotenv
```

### Step 2: Configure Credentials

Create `.env`:

```bash
GITHUB_ACCESS_TOKEN=ghp_your_personal_access_token
```

### Step 3: Basic Usage (No Agent Framework)

Create `main.py`:

```python
import asyncio
import os
from dotenv import load_dotenv
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

load_dotenv()

async def main():
    # Initialize connector
    connector = GithubConnector(
        auth_config=GithubPersonalAccessTokenAuthConfig(
            token=os.environ["GITHUB_ACCESS_TOKEN"]
        )
    )

    # List repositories for a user
    result = await connector.execute("repositories", "list", {
        "username": "airbytehq",
        "per_page": 5
    })

    if result.success:
        for repo in result.data:
            print(f"- {repo['name']}: {repo.get('description', 'No description')}")
    else:
        print(f"Error: {result.error}")

if __name__ == "__main__":
    asyncio.run(main())
```

Run:

```bash
uv run main.py
```

### Step 4: With PydanticAI Agent

Create `agent.py`:

```python
import asyncio
import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

load_dotenv()

# Initialize connector
connector = GithubConnector(
    auth_config=GithubPersonalAccessTokenAuthConfig(
        token=os.environ["GITHUB_ACCESS_TOKEN"]
    )
)

# Create agent
agent = Agent(
    "openai:gpt-4o",
    system_prompt=(
        "You help users explore GitHub repositories. "
        "Use the available tools to answer questions about repos, issues, and PRs."
    )
)

# Register tools
@agent.tool_plain
async def list_issues(owner: str, repo: str, limit: int = 10) -> str:
    """List open issues in a GitHub repository."""
    result = await connector.execute("issues", "list", {
        "owner": owner,
        "repo": repo,
        "states": ["OPEN"],
        "per_page": limit
    })
    return str(result.data) if result.success else f"Error: {result.error}"

@agent.tool_plain
async def list_pull_requests(owner: str, repo: str, limit: int = 10) -> str:
    """List open pull requests in a GitHub repository."""
    result = await connector.execute("pull_requests", "list", {
        "owner": owner,
        "repo": repo,
        "states": ["OPEN"],
        "per_page": limit
    })
    return str(result.data) if result.success else f"Error: {result.error}"

@agent.tool_plain
async def get_repository(owner: str, repo: str) -> str:
    """Get details about a specific GitHub repository."""
    result = await connector.execute("repositories", "get", {
        "owner": owner,
        "repo": repo
    })
    return str(result.data) if result.success else f"Error: {result.error}"

async def main():
    print("GitHub Agent Ready! Ask questions about repositories.")
    print("Example: 'List open issues in airbytehq/airbyte'")
    print("Type 'quit' to exit.\n")

    history = None
    while True:
        prompt = input("You: ")
        if prompt.lower() in ('quit', 'exit', 'q'):
            break
        result = await agent.run(prompt, message_history=history)
        history = result.all_messages()
        print(f"\nAgent: {result.output}\n")

if __name__ == "__main__":
    asyncio.run(main())
```

Add dependencies and run:

```bash
uv add pydantic-ai
uv run agent.py
```

## Quick Reference: Common Operations

### GitHub

```python
# List user's repositories
await connector.execute("repositories", "list", {"username": "octocat"})

# Get specific repo
await connector.execute("repositories", "get", {"owner": "org", "repo": "name"})

# List open issues
await connector.execute("issues", "list", {
    "owner": "org", "repo": "name", "states": ["OPEN"]
})

# Search repositories
await connector.execute("repositories", "api_search", {
    "query": "language:python stars:>1000"
})
```

### Stripe

```python
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

connector = StripeConnector(
    auth_config=StripeAuthConfig(api_key=os.environ["STRIPE_API_KEY"])
)

# List customers
await connector.execute("customers", "list", {"limit": 10})

# Get customer
await connector.execute("customers", "get", {"id": "cus_xxx"})

# Search customers
await connector.execute("customers", "api_search", {
    "query": "email:'user@example.com'"
})
```

### Slack

```python
from airbyte_agent_slack import SlackConnector
from airbyte_agent_slack.models import SlackAuthConfig

connector = SlackConnector(
    auth_config=SlackAuthConfig(token=os.environ["SLACK_BOT_TOKEN"])
)

# List channels
await connector.execute("channels", "list", {})

# List messages in channel
await connector.execute("messages", "list", {"channel": "C01234567"})
```

### HubSpot

```python
from airbyte_agent_hubspot import HubspotConnector
from airbyte_agent_hubspot.models import HubspotPrivateAppAuthConfig

connector = HubspotConnector(
    auth_config=HubspotPrivateAppAuthConfig(
        access_token=os.environ["HUBSPOT_ACCESS_TOKEN"]
    )
)

# List contacts
await connector.execute("contacts", "list", {"limit": 100})

# List deals
await connector.execute("deals", "list", {"limit": 50})
```

## Next Steps

- **[Entity-Action API](./entity-action-api.md)** - Understand the core API patterns
- **[Authentication](./authentication.md)** - Deep dive into auth options
- **[MCP Integration](./mcp-integration.md)** - Set up MCP server for Claude
- **[Troubleshooting](./troubleshooting.md)** - Common issues and solutions

## Connector-Specific Documentation

Each connector has detailed documentation in its directory:

```
connectors/{connector}/
├── README.md      # Overview, example questions, basic usage
├── AUTH.md        # All authentication options
└── REFERENCE.md   # Complete entity/action reference
```

For example:
- [GitHub README](../connectors/github/README.md)
- [Stripe README](../connectors/stripe/README.md)
- [Salesforce README](../connectors/salesforce/README.md)

## Version Management

### Checking for Updates
```bash
# Check current version
pip show airbyte-agent-stripe

# Check latest on PyPI
pip index versions airbyte-agent-stripe
```

### Upgrade Strategy
1. Pin versions in production: `airbyte-agent-stripe==0.5.75`
2. Test upgrades in staging first
3. Check connector's CHANGELOG.md for breaking changes
4. Update one connector at a time

### Breaking Changes
Connectors follow semantic versioning:
- **Patch** (0.5.74 → 0.5.75): Bug fixes, safe to upgrade
- **Minor** (0.5.x → 0.6.0): New features, usually backward compatible
- **Major** (0.x → 1.0): Breaking changes, review changelog
