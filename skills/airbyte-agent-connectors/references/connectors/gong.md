<!-- AUTO-GENERATED from connectors/gong/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Airbyte Gong AI Connector

# Package: airbyte-ai-gong v0.19.0

Type-safe Gong API connector with full IDE autocomplete support for AI applications.

**Key metadata:**

- **Package:** `airbyte-ai-gong` v0.19.0
- **Auth:** GongAuthConfig (access_key, access_key_secret)
- **Docs:** [Official API docs](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/gong)
- **Status:** docs pending

## Quick Start

### Installation

```bash
uv pip install airbyte-ai-gong
```

### Usage

```python
from airbyte_ai_gong import GongConnector
from airbyte_ai_gong.models import GongAuthConfig

# Create connector
connector = GongConnector(auth_config=GongAuthConfig(access_key="...", access_key_secret="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Entities and Actions

| Entity | Action | Description |
|--------|--------|-------------|
| Users | `list_users()` | Returns a list of all users in the Gong account |
| Users | `get_user()` | Get a single user by ID |
| Calls | `list_calls()` | Retrieve calls data by date range |
| Calls | `get_call()` | Get specific call data by ID |
| Calls_Extensive | `list_calls_extensive()` | Retrieve detailed call data including participants, interaction stats, and content |
| Call_Audio | `download_call_audio()` | Downloads the audio media file for a call. Temporarily, the request body must be configured with: |
| Call_Video | `download_call_video()` | Downloads the video media file for a call. Temporarily, the request body must be configured with: |
| Workspaces | `list_workspaces()` | List all company workspaces |
| Call_Transcripts | `get_call_transcripts()` | Returns transcripts for calls in a specified date range or specific call IDs |
| Stats_Activity_Aggregate | `get_activity_aggregate()` | Provides aggregated user activity metrics across a specified period |
| Stats_Activity_Day_By_Day | `get_activity_day_by_day()` | Delivers daily user activity metrics across a specified date range |
| Stats_Interaction | `get_interaction_stats()` | Returns interaction stats for users based on calls that have Whisper turned on |
| Settings_Scorecards | `list_scorecards()` | Retrieve all scorecard configurations in the company |
| Settings_Trackers | `list_trackers()` | Retrieve all keyword tracker configurations in the company |
| Library_Folders | `list_library_folders()` | Retrieve the folder structure of the call library |
| Library_Folder_Content | `list_folder_content()` | Retrieve calls in a specific library folder |
| Coaching | `list_coaching_metrics()` | Retrieve coaching metrics for a manager and their direct reports |
| Stats_Activity_Scorecards | `list_answered_scorecards()` | Retrieve answered scorecards for applicable reviewed users or scorecards for a date range |

## Authentication

Auth class: `GongAuthConfig`

Required fields:

- `access_key`
- `access_key_secret`

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/gong)*
