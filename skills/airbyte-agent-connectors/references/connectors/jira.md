<!-- AUTO-GENERATED from connectors/jira/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Jira

The Jira agent connector is a Python package that equips AI agents to interact with Jira through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-jira` v0.1.106
- **Auth:** Token
- **Docs:** [Official API docs](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- **Status:** complete

## Example Prompts

- Show me all open issues in my Jira instance
- List recent issues created in the last 7 days
- List all projects in my Jira instance
- Show me details for the most recently updated issue
- List all users in my Jira instance
- Show me comments on the most recent issue
- Show me worklogs from the last 7 days
- Assign a recent issue to a teammate
- Unassign a recent issue
- Create a new task called 'Sample task' in a project
- Create a bug with high priority
- Update the summary of a recent issue to 'Updated summary'
- Change the priority of a recent issue to high
- Add a comment to a recent issue saying 'Please investigate'
- Update my most recent comment
- Delete a test issue
- Remove my most recent comment
- What issues are assigned to \{team_member\} this week?
- Find all high priority bugs in our current sprint
- Show me overdue issues across all projects
- What projects have the most issues?
- Search for users named \{user_name\}

## Unsupported

- Log time on \{issue_key\}
- Transition \{issue_key\} to Done

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-jira
```

### OSS Mode

```python
from airbyte_agent_jira import JiraConnector
from airbyte_agent_jira.models import JiraAuthConfig

connector = JiraConnector(
    auth_config=JiraAuthConfig(
        username="<Your Atlassian account email address>",
        password="<Your Jira API token from https://id.atlassian.com/manage-profile/security/api-tokens>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@JiraConnector.tool_utils
async def jira_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_jira import JiraConnector, AirbyteAuthConfig

connector = JiraConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@JiraConnector.tool_utils
async def jira_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Issues | API Search, Create, Get, Update, Delete, Search |
| Projects | API Search, Get, Search |
| Users | Get, List, API Search, Search |
| Issue Fields | List, API Search, Search |
| Issue Comments | List, Create, Get, Update, Delete, Search |
| Issue Worklogs | List, Get, Search |
| Issues Assignee | Update |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/jira/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/jira/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/jira)*
