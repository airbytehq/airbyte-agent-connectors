# Airbyte Greenhouse AI Connector

Type-safe Greenhouse API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.8.0

**Connector Version:** 1.0.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-greenhouse
```

## Usage

```python
from airbyte_ai_greenhouse import GreenhouseConnector

# Create connector
connector = GreenhouseConnector(auth_config={"api_key": "your_api_key"})

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Candidates Operations
- `list_candidates()` - List candidates
- `get_candidate()` - Get a candidate

### Applications Operations
- `list_applications()` - List applications
- `get_application()` - Get an application

### Jobs Operations
- `list_jobs()` - List jobs
- `get_job()` - Get a job

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_greenhouse.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
