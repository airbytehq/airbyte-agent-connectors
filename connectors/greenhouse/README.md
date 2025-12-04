# Airbyte Greenhouse AI Connector

Type-safe Greenhouse API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.11.0

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
- `list_candidates()` - Returns a paginated list of all candidates in the organization
- `get_candidate()` - Get a single candidate by ID

### Applications Operations
- `list_applications()` - Returns a paginated list of all applications
- `get_application()` - Get a single application by ID

### Jobs Operations
- `list_jobs()` - Returns a paginated list of all jobs in the organization
- `get_job()` - Get a single job by ID

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_greenhouse.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
