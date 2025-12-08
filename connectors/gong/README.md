# Airbyte Gong AI Connector

Type-safe Gong API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.18.0

**Connector Version:** 0.1.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-gong
```

## Usage

```python
from airbyte_ai_gong import GongConnector
from airbyte_ai_gong.models import GongAuthConfig

# Create connector
connector = GongConnector(auth_config=GongAuthConfig(access_key="...", access_key_secret="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Users Operations
- `list_users()` - Returns a list of all users in the Gong account
- `get_user()` - Get a single user by ID

### Calls Operations
- `list_calls()` - Retrieve calls data by date range
- `get_call()` - Get specific call data by ID

### Calls_Extensive Operations
- `list_calls_extensive()` - Retrieve detailed call data including participants, interaction stats, and content

### Call_Audio Operations
- `download_call_audio()` - Downloads the audio media file for a call. Temporarily, the request body must be configured with:
{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}


### Call_Video Operations
- `download_call_video()` - Downloads the video media file for a call. Temporarily, the request body must be configured with:
{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}


### Workspaces Operations
- `list_workspaces()` - List all company workspaces

### Call_Transcripts Operations
- `get_call_transcripts()` - Returns transcripts for calls in a specified date range or specific call IDs

### Stats_Activity_Aggregate Operations
- `get_activity_aggregate()` - Provides aggregated user activity metrics across a specified period

### Stats_Activity_Day_By_Day Operations
- `get_activity_day_by_day()` - Delivers daily user activity metrics across a specified date range

### Stats_Interaction Operations
- `get_interaction_stats()` - Returns interaction stats for users based on calls that have Whisper turned on

### Settings_Scorecards Operations
- `list_scorecards()` - Retrieve all scorecard configurations in the company

### Settings_Trackers Operations
- `list_trackers()` - Retrieve all keyword tracker configurations in the company

### Library_Folders Operations
- `list_library_folders()` - Retrieve the folder structure of the call library

### Library_Folder_Content Operations
- `list_folder_content()` - Retrieve calls in a specific library folder

### Coaching Operations
- `list_coaching_metrics()` - Retrieve coaching metrics for a manager and their direct reports

### Stats_Activity_Scorecards Operations
- `list_answered_scorecards()` - Retrieve answered scorecards for applicable reviewed users or scorecards for a date range

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_gong.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
