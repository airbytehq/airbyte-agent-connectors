<!-- AUTO-GENERATED from connectors/gitlab/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# GitLab

The Gitlab agent connector is a Python package that equips AI agents to interact with Gitlab through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-gitlab` v0.1.1
- **Auth:** OAuth, Token
- **Docs:** [Official API docs](https://docs.gitlab.com/ee/api/rest/)
- **Status:** complete

## Example Prompts

- List all projects I have access to
- Get the details of a specific project
- List all open issues in a project
- Show merge requests for a project
- List all groups I belong to
- Show recent commits in a project
- List pipelines for a project
- Show all branches in a project
- Find issues updated in the last week
- What are the most active projects?
- Show merge requests that are still open
- List projects with the most commits

## Unsupported

- Create a new project
- Delete an issue
- Merge a merge request
- Trigger a pipeline

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-gitlab
```

### OSS Mode

```python
from airbyte_agent_gitlab import GitlabConnector
from airbyte_agent_gitlab.models import GitlabPersonalAccessTokenAuthConfig

connector = GitlabConnector(
    auth_config=GitlabPersonalAccessTokenAuthConfig(
        access_token="<Log into your GitLab account and generate a personal access token.>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GitlabConnector.tool_utils
async def gitlab_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_gitlab import GitlabConnector, AirbyteAuthConfig

connector = GitlabConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GitlabConnector.tool_utils
async def gitlab_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Projects | List, Get, Search |
| Issues | List, Get, Search |
| Merge Requests | List, Get, Search |
| Users | List, Get, Search |
| Commits | List, Get, Search |
| Groups | List, Get, Search |
| Branches | List, Get, Search |
| Pipelines | List, Get, Search |
| Group Members | List, Get, Search |
| Project Members | List, Get, Search |
| Releases | List, Get, Search |
| Tags | List, Get, Search |
| Group Milestones | List, Get, Search |
| Project Milestones | List, Get, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gitlab/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gitlab/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/gitlab)*
