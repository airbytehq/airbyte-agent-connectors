<!-- AUTO-GENERATED from connectors/github/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# GitHub

The Github agent connector is a Python package that equips AI agents to interact with Github through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-github` v0.18.118
- **Auth:** OAuth, Token
- **Docs:** [Official API docs](https://docs.github.com/en/rest)
- **Status:** complete

## Example Prompts

- Show me all open issues in my repositories this month
- List the top 5 repositories I've starred recently
- Analyze the commit trends in my main project over the last quarter
- Find all pull requests created in the past two weeks
- Search for repositories related to machine learning in my organizations
- Compare the number of contributors across my different team projects
- Identify the most active branches in my main repository
- Get details about the most recent releases in my organization
- List all milestones for our current development sprint
- Show me insights about pull request review patterns in our team

## Unsupported

- Create a new issue in the project repository
- Update the status of this pull request
- Delete an old branch from the repository
- Schedule a team review for this code
- Assign a new label to this issue

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-github
```

### OSS Mode

```python
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

connector = GithubConnector(
    auth_config=GithubPersonalAccessTokenAuthConfig(
        token="<GitHub personal access token (fine-grained or classic)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GithubConnector.tool_utils
async def github_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_github import GithubConnector, AirbyteAuthConfig

connector = GithubConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GithubConnector.tool_utils
async def github_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Repositories | Get, List, API Search |
| Org Repositories | List |
| Branches | List, Get |
| Commits | List, Get |
| Releases | List, Get |
| Issues | List, Get, API Search |
| Pull Requests | List, Get, API Search |
| Reviews | List |
| Comments | List, Get |
| Pr Comments | List, Get |
| Labels | List, Get |
| Milestones | List, Get |
| Organizations | Get, List |
| Users | Get, List, API Search |
| Teams | List, Get |
| Tags | List, Get |
| Stargazers | List |
| Viewer | Get |
| Viewer Repositories | List |
| Projects | List, Get |
| Project Items | List |
| File Content | Get |
| Directory Content | List |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/github/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/github/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/github)*
