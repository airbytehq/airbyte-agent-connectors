# Gong agent connector

Gong is a revenue intelligence platform that captures and analyzes customer interactions
across calls, emails, and web conferences. This connector provides access to users,
recorded calls with transcripts, activity statistics, scorecards, trackers, workspaces,
coaching metrics, and library content for sales performance analysis and revenue insights.


## Example questions

The Gong connector is optimized to handle prompts like these.

- List all users in my Gong account
- Show me calls from last week
- Get the transcript for call abc123
- What are the activity stats for our sales team?
- List all workspaces in Gong
- Show me the scorecard configurations
- What trackers are set up in my account?
- Get coaching metrics for manager user123

## Unsupported questions

The Gong connector isn't currently able to handle prompts like these.

- Create a new user in Gong
- Delete a call recording
- Update scorecard questions
- Schedule a new meeting
- Send feedback to a team member
- Modify tracker keywords

## Installation

```bash
uv pip install airbyte-agent-gong
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
    "connector_definition_id": "32382e40-3b49-4b99-9c5c-4076501914e7",
    "name": "my-gong-connector",
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
from airbyte_agent_gong import GongConnector
from airbyte_agent_gong.models import GongAccessKeyAuthenticationAuthConfig

connector = GongConnector(
    auth_config=GongAccessKeyAuthenticationAuthConfig(
        access_key="<Your Gong API Access Key>",
        access_key_secret="<Your Gong API Access Key Secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GongConnector.tool_utils
async def gong_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted

In hosted mode, API credentials are stored securely in Airbyte Cloud. You provide your Airbyte credentials instead. 

This example assumes you've already authenticated your connector with Airbyte. See [Authentication](AUTH.md) to learn more about authenticating. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

```python
from airbyte_agent_gong import GongConnector

connector = GongConnector(
    external_user_id="<your_external_user_id>",
    airbyte_client_id="<your-client-id>",
    airbyte_client_secret="<your-client-secret>"
)

@agent.tool_plain # assumes you're using Pydantic AI
@GongConnector.tool_utils
async def gong_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Full documentation

### Entities and actions

This connector supports the following entities and actions. For more details, see this connector's [full reference documentation](REFERENCE.md).

| Entity | Actions |
|--------|---------|
| Users | [List](./REFERENCE.md#users-list), [Get](./REFERENCE.md#users-get) |
| Calls | [List](./REFERENCE.md#calls-list), [Get](./REFERENCE.md#calls-get) |
| Calls Extensive | [List](./REFERENCE.md#calls-extensive-list) |
| Call Audio | [Download](./REFERENCE.md#call-audio-download) |
| Call Video | [Download](./REFERENCE.md#call-video-download) |
| Workspaces | [List](./REFERENCE.md#workspaces-list) |
| Call Transcripts | [List](./REFERENCE.md#call-transcripts-list) |
| Stats Activity Aggregate | [List](./REFERENCE.md#stats-activity-aggregate-list) |
| Stats Activity Day By Day | [List](./REFERENCE.md#stats-activity-day-by-day-list) |
| Stats Interaction | [List](./REFERENCE.md#stats-interaction-list) |
| Settings Scorecards | [List](./REFERENCE.md#settings-scorecards-list) |
| Settings Trackers | [List](./REFERENCE.md#settings-trackers-list) |
| Library Folders | [List](./REFERENCE.md#library-folders-list) |
| Library Folder Content | [List](./REFERENCE.md#library-folder-content-list) |
| Coaching | [List](./REFERENCE.md#coaching-list) |
| Stats Activity Scorecards | [List](./REFERENCE.md#stats-activity-scorecards-list) |


### Authentication and configuration

For all authentication and configuration options, see the connector's [authentication documentation](AUTH.md).

### Gong API docs

See the official [Gong API reference](https://gong.app.gong.io/settings/api/documentation).

## Version information

- **Package version:** 0.19.82
- **Connector version:** 0.1.14
- **Generated with Connector SDK commit SHA:** 940246757c7476ed4edd7d16b873ebe54ea2b456
- **Changelog:** [View changelog](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gong/CHANGELOG.md)