# Airbyte Gong AI Connector

Type-safe Gong API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.7.0
**Connector Version:** 1.0.0
**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-gong
```

## Usage

```python
from airbyte_ai_gong import GongConnector

# Create connector
connector = GongConnector.create(auth_config={"api_key": "your_api_key"})

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Users Operations
- `list_users()` - List users
- `get_user()` - Get a user

### Calls Operations
- `list_calls()` - List calls
- `get_call()` - Get a call

### Calls_Extensive Operations
- `list_calls_extensive()` - List calls with extensive data

### Workspaces Operations
- `list_workspaces()` - List workspaces

### Call_Transcripts Operations
- `get_call_transcripts()` - Retrieve call transcripts

### Stats_Activity_Aggregate Operations
- `get_activity_aggregate()` - Retrieve aggregated activity statistics

### Stats_Activity_Day_By_Day Operations
- `get_activity_day_by_day()` - Retrieve daily activity statistics

### Stats_Interaction Operations
- `get_interaction_stats()` - Retrieve interaction statistics

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_gong.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
