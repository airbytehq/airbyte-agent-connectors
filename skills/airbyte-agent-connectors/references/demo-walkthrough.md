# Demo Walkthrough

End-to-end demos showing Airbyte Agent Connectors in action with Claude Code. Each scenario shows exactly what the developer types, what Claude does behind the scenes, and what appears in the terminal.

## Contents

- [Demo 1: Set Up Stripe in Platform Mode](#demo-1-set-up-stripe-in-platform-mode)
  - [Prerequisites](#prerequisites)
  - [The Conversation](#the-conversation)
  - [What Happened Behind the Scenes](#what-happened-behind-the-scenes)
- [Demo 2: Set Up GitHub in OSS Mode](#demo-2-set-up-github-in-oss-mode)
  - [Prerequisites](#prerequisites-1)
  - [The Conversation](#the-conversation-1)
  - [What Happened Behind the Scenes](#what-happened-behind-the-scenes-1)
- [Key Takeaways](#key-takeaways)

---

## Demo 1: Set Up Stripe in Platform Mode

A SaaS developer wants to connect their Stripe account to Airbyte Platform so they can query customer and payment data from their AI agent. They have Airbyte Cloud credentials and a Stripe API key.

### Prerequisites

- Airbyte Cloud account with API keys from [app.airbyte.ai](https://app.airbyte.ai) > Settings > API Keys
- Stripe API key from [Stripe Dashboard](https://dashboard.stripe.com/apikeys)
- Claude Code installed with the `airbyte-agent-connectors` skill

### The Conversation

**Developer types:**

```
Set up a Stripe connector on Airbyte Platform. My client ID is abc123def and my
client secret is sec_456xyz. My Stripe API key is sk_live_51ABC.
```

**Claude responds:**

> I'll set up your Stripe connector on Airbyte Platform. This involves getting an application token, detecting your workspace, registering a connector template, creating a connector instance, and verifying it works.
>
> **Step 1: Getting application token...**

Claude runs:

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/account/applications/token' \
  -H 'Content-Type: application/json' \
  -d '{"client_id": "abc123def", "client_secret": "sec_456xyz"}'
```

Terminal output:

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

> **Step 2: Detecting workspace...**

Claude runs:

```bash
curl 'https://api.airbyte.ai/api/v1/workspaces' \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
```

Terminal output:

```json
{
  "data": [
    {
      "workspaceId": "ws_8f3a2b1c",
      "name": "Acme Corp Production"
    }
  ]
}
```

> Found one workspace: **Acme Corp Production**. Using it automatically.
>
> **Step 3: Checking for existing Stripe template...**

Claude runs:

```bash
curl 'https://api.airbyte.ai/api/v1/integrations/templates/sources' \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
```

Terminal output:

```json
{
  "data": []
}
```

> No existing template found. I'll register one now.
>
> **Step 4: Registering Stripe template...**

Claude runs:

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/templates/sources' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...' \
  -d '{
    "actor_definition_id": "e094cb9a-26de-4645-8761-65c0c425d1de",
    "name": "Stripe",
    "original_source_template_id": "",
    "partial_default_config": {},
    "mode": "DIRECT"
  }'
```

Terminal output:

```json
{
  "sourceTemplateId": "tmpl_stripe_9x7w",
  "name": "Stripe",
  "mode": "DIRECT"
}
```

> Template registered. Your Stripe connector now appears in the Airbyte UI with a "Direct" badge.
>
> **Step 5: Creating connector instance...**

Claude runs:

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors' \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...' \
  -H 'Content-Type: application/json' \
  -d '{
    "external_user_id": "Acme Corp Production",
    "workspace_name": "Acme Corp Production",
    "definition_id": "e094cb9a-26de-4645-8761-65c0c425d1de",
    "name": "stripe-production",
    "credentials": {
      "api_key": "sk_live_51ABC"
    }
  }'
```

Terminal output:

```json
{
  "connectorId": "conn_stripe_4k2m",
  "name": "stripe-production",
  "status": "active"
}
```

> **Step 6: Verifying with a test query...**

Claude runs:

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors/conn_stripe_4k2m/execute' \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...' \
  -H 'Content-Type: application/json' \
  -d '{"entity": "customers", "action": "list", "params": {"limit": 2}}'
```

Terminal output:

```json
{
  "success": true,
  "data": [
    {
      "id": "cus_R1a2b3c4d5",
      "email": "jane@acmecorp.com",
      "name": "Jane Rodriguez",
      "created": 1706140800
    },
    {
      "id": "cus_Q9z8y7x6w5",
      "email": "alex@widgets.io",
      "name": "Alex Chen",
      "created": 1705968000
    }
  ]
}
```

> **Step 7: Creating .env file...**

Claude creates `.env`:

```bash
AIRBYTE_CLIENT_ID=abc123def
AIRBYTE_CLIENT_SECRET=sec_456xyz
STRIPE_API_KEY=sk_live_51ABC
```

> **Connector created and verified!** Pulled 2 customer records successfully.
>
> Here's what you have now:
> - Stripe connector visible in the [Airbyte UI](https://app.airbyte.ai) under Connectors
> - Connector ID: `conn_stripe_4k2m`
> - `.env` file with your credentials
>
> You can now query Stripe data programmatically:
>
> ```python
> from airbyte_agent_stripe import StripeConnector
> from airbyte_agent_stripe.models import StripeAuthConfig
>
> connector = StripeConnector(
>     external_user_id="Acme Corp Production",
>     airbyte_client_id="abc123def",
>     airbyte_client_secret="sec_456xyz",
> )
>
> result = await connector.execute("customers", "list", {"limit": 10})
> result = await connector.execute("payments", "list", {"limit": 5})
> result = await connector.execute("invoices", "list", {"limit": 5})
> ```

**Developer types:**

```
Show me all payments over $100 from the last month.
```

**Claude responds:**

> I'll query your Stripe connector for recent payments.

Claude runs:

```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors/conn_stripe_4k2m/execute' \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...' \
  -H 'Content-Type: application/json' \
  -d '{
    "entity": "payments",
    "action": "list",
    "params": {"limit": 100}
  }'
```

Terminal output:

```json
{
  "success": true,
  "data": [
    {
      "id": "pi_3PxY12ABC",
      "amount": 24900,
      "currency": "usd",
      "status": "succeeded",
      "customer": "cus_R1a2b3c4d5",
      "created": 1706659200
    },
    {
      "id": "pi_3PwK45DEF",
      "amount": 15000,
      "currency": "usd",
      "status": "succeeded",
      "customer": "cus_Q9z8y7x6w5",
      "created": 1706572800
    },
    {
      "id": "pi_3PvN78GHI",
      "amount": 8500,
      "currency": "usd",
      "status": "succeeded",
      "customer": "cus_M3n4o5p6q7",
      "created": 1706486400
    }
  ]
}
```

> Here are the payments over $100 from the last month:
>
> | Payment ID | Amount | Customer | Date |
> |------------|--------|----------|------|
> | `pi_3PxY12ABC` | $249.00 | Jane Rodriguez (`cus_R1a2b3c4d5`) | Jan 31, 2025 |
> | `pi_3PwK45DEF` | $150.00 | Alex Chen (`cus_Q9z8y7x6w5`) | Jan 30, 2025 |
>
> 2 payments over $100. Total: **$399.00**. (1 payment of $85.00 was excluded.)

### What Happened Behind the Scenes

Claude followed the [Platform Mode Complete Setup Checklist](platform-setup.md#complete-setup-checklist) end-to-end:

1. **Token acquisition** -- exchanged client credentials for an application token
2. **Workspace detection** -- found one workspace and used it automatically
3. **Template check** -- verified no Stripe template existed yet
4. **Template registration** -- registered Stripe with its definition ID (`e094cb9a-26de-4645-8761-65c0c425d1de`) from the built-in lookup table
5. **Connector creation** -- created an instance with credentials (no discriminator fields like `auth_type`)
6. **Verification** -- pulled live data to confirm the connection works
7. **Environment file** -- created `.env` for future use

The developer went from zero to querying live Stripe data in a single conversation turn.

---

## Demo 2: Set Up GitHub in OSS Mode

A developer wants to use GitHub data in a local Python project. No Airbyte Cloud needed -- just install the package, write some code, and start pulling data.

### Prerequisites

- Python 3.11+ with [uv](https://github.com/astral-sh/uv) installed
- GitHub Personal Access Token from [GitHub Settings](https://github.com/settings/tokens)
- Claude Code installed with the `airbyte-agent-connectors` skill

### The Conversation

**Developer types:**

```
I want to pull GitHub issues and PRs from our repo myorg/backend using OSS Mode.
My GitHub token is ghp_abc123xyz789.
```

**Claude responds:**

> I'll set up a GitHub connector in OSS Mode. This means running the connector locally with the Python SDK -- no Airbyte Cloud needed.
>
> **Step 1: Installing the package...**

Claude runs:

```bash
uv add airbyte-agent-github python-dotenv
```

Terminal output:

```
Resolved 12 packages in 1.2s
Installed 12 packages in 0.8s
 + airbyte-agent-github==0.18.78
 + python-dotenv==1.0.1
 + httpx==0.27.0
 + pydantic==2.6.1
 + ...
```

> **Step 2: Creating .env file...**

Claude creates `.env`:

```bash
GITHUB_TOKEN=ghp_abc123xyz789
```

> **Step 3: Creating the connector script...**

Claude creates `main.py`:

```python
import asyncio
import os
from dotenv import load_dotenv
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

load_dotenv()

async def main():
    connector = GithubConnector(
        auth_config=GithubPersonalAccessTokenAuthConfig(
            token=os.environ["GITHUB_TOKEN"]
        )
    )

    # List open issues
    issues = await connector.execute("issues", "list", {
        "owner": "myorg",
        "repo": "backend",
        "states": ["OPEN"],
        "per_page": 10
    })

    if issues.success:
        print(f"Found {len(issues.data)} open issues:\n")
        for issue in issues.data:
            print(f"  #{issue['number']} - {issue['title']}")
    else:
        print(f"Error: {issues.error}")

    # List open pull requests
    prs = await connector.execute("pull_requests", "list", {
        "owner": "myorg",
        "repo": "backend",
        "states": ["OPEN"],
        "per_page": 10
    })

    if prs.success:
        print(f"\nFound {len(prs.data)} open PRs:\n")
        for pr in prs.data:
            print(f"  #{pr['number']} - {pr['title']} (by {pr['author']['login']})")
    else:
        print(f"Error: {prs.error}")

if __name__ == "__main__":
    asyncio.run(main())
```

> **Step 4: Running it...**

Claude runs:

```bash
uv run main.py
```

Terminal output:

```
Found 7 open issues:

  #342 - Rate limiter not respecting burst config
  #338 - Add OpenTelemetry tracing to auth service
  #335 - Upgrade postgres driver to v5.2
  #331 - Flaky test in test_webhook_handler
  #328 - Document new retry behavior in README
  #325 - Support custom headers in API gateway
  #319 - Memory leak in connection pool under load

Found 4 open PRs:

  #341 - Fix rate limiter token bucket algorithm (by sarah-dev)
  #340 - Add OTEL spans to middleware chain (by marcus-k)
  #337 - Bump postgres-driver to 5.2.1 (by dependabot)
  #336 - Add integration tests for webhook retry (by priya-eng)
```

> Your GitHub connector is working. Here's a summary:
>
> - **7 open issues** -- including a rate limiter bug (#342) and a memory leak (#319)
> - **4 open PRs** -- the rate limiter fix (#341) looks related to issue #342
>
> The project is set up at:
> - `main.py` -- connector script
> - `.env` -- your GitHub token
>
> You can query any GitHub entity:
> ```python
> # Get a specific issue
> await connector.execute("issues", "get", {"owner": "myorg", "repo": "backend", "number": 342})
>
> # Search repositories
> await connector.execute("repositories", "api_search", {"query": "language:python stars:>1000"})
>
> # List commits
> await connector.execute("commits", "list", {"owner": "myorg", "repo": "backend", "per_page": 5})
> ```

**Developer types:**

```
Can you also set this up as an MCP server so I can query GitHub directly from Claude?
```

**Claude responds:**

> I'll add the GitHub connector to Claude Code via MCP so you can query it conversationally.

Claude runs:

```bash
claude mcp add airbyte-agent-mcp --scope project
```

> When prompted, I'll use this server configuration:
>
> ```json
> {
>   "command": "uv",
>   "args": [
>     "--directory",
>     "/path/to/airbyte-agent-connectors/airbyte-agent-mcp",
>     "run",
>     "airbyte_agent_mcp"
>   ]
> }
> ```
>
> And I've created `configured_connectors.yaml` in the MCP directory:
>
> ```yaml
> connectors:
>   - id: github
>     type: local
>     connector_name: github
>     description: "GitHub repositories and issues"
>     secrets:
>       token: GITHUB_TOKEN
> ```
>
> After restarting Claude Code, you can ask things like:
> - "List open issues in myorg/backend"
> - "Show me PRs by sarah-dev"
> - "Search for Python repos with over 1000 stars"
>
> Claude will call the GitHub connector directly through MCP.

### What Happened Behind the Scenes

Claude followed the [OSS Mode Setup Workflow](oss-setup.md#setup-workflow) workflow:

1. **Package installation** -- `uv add airbyte-agent-github` pulled the connector and its dependencies
2. **Credential setup** -- created `.env` with the GitHub token (never hardcoded in source)
3. **Code generation** -- wrote a complete async script using the entity-action API pattern
4. **Verification** -- ran the script and confirmed live data came back
5. **MCP setup** -- optionally configured the MCP server for conversational access from Claude

The developer went from zero to pulling live GitHub data in under 60 seconds.

---

## Key Takeaways

| Aspect | Platform Mode (Demo 1) | OSS Mode (Demo 2) |
|--------|------------------------|---------------------|
| **Setup time** | ~2 minutes (7 API calls) | ~30 seconds (install + run) |
| **Credentials stored** | Managed by Airbyte Cloud | Local `.env` file |
| **UI visibility** | Connector appears in app.airbyte.ai | No UI -- code only |
| **Best for** | Production SaaS, multi-tenant apps | Prototyping, local dev, MCP integration |
| **Claude's role** | Executes full HTTP API workflow | Generates code and runs it locally |

Both modes use the same entity-action API (`connector.execute(entity, action, params)`), so switching between them requires only changing how the connector is initialized -- not how you query data.

---

## Related Documentation

- [Platform Setup](platform-setup.md) -- Complete Platform Mode reference
- [OSS Setup](oss-setup.md) -- Complete OSS Mode reference
- [Entity-Action API](entity-action-api.md) -- All entities, actions, and parameters
- [Authentication](authentication.md) -- Auth patterns for every connector
- [MCP Integration](mcp-integration.md) -- Detailed MCP server configuration
- [Troubleshooting](troubleshooting.md) -- Common errors and solutions
