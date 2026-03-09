<!-- AUTO-GENERATED from connectors/ashby/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Ashby

The Ashby agent connector is a Python package that equips AI agents to interact with Ashby through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-ashby` v0.1.16
- **Auth:** Token
- **Docs:** [Official API docs](https://developers.ashbyhq.com/reference)
- **Status:** complete

## Example Prompts

- List all open jobs
- Show me all candidates
- List recent applications
- List all departments
- Show me all job postings
- List all users in the organization
- Show me candidates who applied last month
- What are the top sources for job applications?
- Compare the number of applications across different departments
- Find candidates with multiple applications
- Summarize the candidate pipeline for our latest job posting
- Find the most active departments in recruiting this month

## Unsupported

- Create a new job posting
- Schedule an interview for a candidate
- Update a candidates application status
- Delete a candidate profile
- Send an offer letter to a candidate

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-ashby
```

### OSS Mode

```python
from airbyte_agent_ashby import AshbyConnector
from airbyte_agent_ashby.models import AshbyAuthConfig

connector = AshbyConnector(
    auth_config=AshbyAuthConfig(
        api_key="<Your Ashby API key>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AshbyConnector.tool_utils
async def ashby_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_ashby import AshbyConnector, AirbyteAuthConfig

connector = AshbyConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AshbyConnector.tool_utils
async def ashby_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Candidates | List, Get |
| Applications | List, Get |
| Jobs | List, Get |
| Departments | List, Get |
| Locations | List, Get |
| Users | List, Get |
| Job Postings | List, Get |
| Sources | List |
| Archive Reasons | List |
| Candidate Tags | List |
| Custom Fields | List |
| Feedback Form Definitions | List |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/ashby/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/ashby/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/ashby)*
