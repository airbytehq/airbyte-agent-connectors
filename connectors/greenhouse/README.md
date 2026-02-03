# Greenhouse agent connector

Greenhouse is an applicant tracking system (ATS) that helps companies manage their
hiring process. This connector provides access to candidates, applications, jobs,
offers, users, departments, offices, job posts, sources, and scheduled interviews
for recruiting analytics and talent acquisition insights.


## Example questions

The Greenhouse connector is optimized to handle prompts like these.

- Show me candidates from \{company\} who applied last month
- What are the top 5 sources for our job applications this quarter?
- List all open jobs in the Sales department
- Analyze the interview schedules for our engineering candidates this week
- Get details of recent job offers for \{team_member\}
- Compare the number of applications across different offices
- Identify candidates who have multiple applications in our system
- Show me upcoming scheduled interviews for our marketing positions
- Summarize the candidate pipeline for our latest job posting
- Find the most active departments in recruiting this month

## Unsupported questions

The Greenhouse connector isn't currently able to handle prompts like these.

- Create a new job posting for the marketing team
- Schedule an interview for \{candidate\}
- Update the status of \{candidate\}'s application
- Delete a candidate profile
- Send an offer letter to \{candidate\}
- Edit the details of a job description

## Installation

```bash
uv pip install airbyte-agent-greenhouse
```

## Quick Setup (Hosted)

Get running with Airbyte's hosted infrastructure in 3 steps.

**Prerequisites:** `AIRBYTE_CLIENT_ID` and `AIRBYTE_CLIENT_SECRET` from [app.airbyte.ai](https://app.airbyte.ai) settings.

**1. Get application token:**
```bash
curl -X POST 'https://api.airbyte.com/v1/applications/token' \
  -H 'Content-Type: application/json' \
  -d '{"client_id": "'"$AIRBYTE_CLIENT_ID"'", "client_secret": "'"$AIRBYTE_CLIENT_SECRET"'"}'
```

**2. Get scoped token:**
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/embedded/scoped-token' \
  -H 'Authorization: Bearer <APPLICATION_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"workspace_name": "<YOUR_USER_ID>"}'
```

**3. Create connector:**
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/connectors/instances' \
  -H 'Authorization: Bearer <SCOPED_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "connector_definition_id": "59f1e50a-331f-4f09-b3e8-2e8d4d355f44",
    "name": "my-greenhouse-connector",
    "auth_config": {
      "api_key": "<YOUR_API_KEY>"
    }
  }'
```

Save the returned `id` as your `CONNECTOR_ID` for subsequent requests.

## Usage

Connectors can run in open source or hosted mode.

### Open source

In open source mode, you provide API credentials directly to the connector.

```python
from airbyte_agent_greenhouse import GreenhouseConnector
from airbyte_agent_greenhouse.models import GreenhouseAuthConfig

connector = GreenhouseConnector(
    auth_config=GreenhouseAuthConfig(
        api_key="<Your Greenhouse Harvest API Key from the Dev Center>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GreenhouseConnector.tool_utils
async def greenhouse_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. 

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```python
from airbyte_agent_greenhouse import GreenhouseConnector

connector = GreenhouseConnector(
    external_user_id="<your_external_user_id>",
    airbyte_client_id="<your-client-id>",
    airbyte_client_secret="<your-client-secret>"
)

@agent.tool_plain # assumes you're using Pydantic AI
@GreenhouseConnector.tool_utils
async def greenhouse_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation

### Entities and actions

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](REFERENCE.md).

| Entity | Actions |
|--------|---------|
| Candidates | [List](./REFERENCE.md#candidates-list), [Get](./REFERENCE.md#candidates-get) |
| Applications | [List](./REFERENCE.md#applications-list), [Get](./REFERENCE.md#applications-get) |
| Jobs | [List](./REFERENCE.md#jobs-list), [Get](./REFERENCE.md#jobs-get) |
| Offers | [List](./REFERENCE.md#offers-list), [Get](./REFERENCE.md#offers-get) |
| Users | [List](./REFERENCE.md#users-list), [Get](./REFERENCE.md#users-get) |
| Departments | [List](./REFERENCE.md#departments-list), [Get](./REFERENCE.md#departments-get) |
| Offices | [List](./REFERENCE.md#offices-list), [Get](./REFERENCE.md#offices-get) |
| Job Posts | [List](./REFERENCE.md#job-posts-list), [Get](./REFERENCE.md#job-posts-get) |
| Sources | [List](./REFERENCE.md#sources-list) |
| Scheduled Interviews | [List](./REFERENCE.md#scheduled-interviews-list), [Get](./REFERENCE.md#scheduled-interviews-get) |
| Application Attachment | [Download](./REFERENCE.md#application-attachment-download) |
| Candidate Attachment | [Download](./REFERENCE.md#candidate-attachment-download) |


### Authentication and configuration

For all authentication and configuration options, see the connector's [authentication documentation](AUTH.md).

### Greenhouse API docs

See the official [Greenhouse API reference](https://developers.greenhouse.io/harvest.html).

## Version information

- **Package version:** 0.17.73
- **Connector version:** 0.1.4
- **Generated with Connector SDK commit SHA:** 940246757c7476ed4edd7d16b873ebe54ea2b456
- **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/greenhouse/CHANGELOG.md)