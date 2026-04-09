<!-- AUTO-GENERATED from connectors/gitlab/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-04-09 -->

# GitLab

The Gitlab agent connector is a Python package that equips AI agents to interact with Gitlab through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-gitlab` v0.1.18
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
| Projects | List, Get, Context Store Search |
| Issues | List, Get, Context Store Search |
| Merge Requests | List, Get, Context Store Search |
| Users | List, Get, Context Store Search |
| Commits | List, Get, Context Store Search |
| Groups | List, Get, Context Store Search |
| Branches | List, Get, Context Store Search |
| Pipelines | List, Get, Context Store Search |
| Group Members | List, Get, Context Store Search |
| Project Members | List, Get, Context Store Search |
| Releases | List, Get, Context Store Search |
| Tags | List, Get, Context Store Search |
| Group Milestones | List, Get, Context Store Search |
| Project Milestones | List, Get, Context Store Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gitlab/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gitlab/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/gitlab)*
