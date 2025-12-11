# Airbyte Linear AI Connector

Type-safe Linear API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-linear
```

## Usage

```python
from airbyte_ai_linear import LinearConnector
from airbyte_ai_linear.models import LinearAuthConfig

# Create connector
connector = LinearConnector(auth_config=LinearAuthConfig(api_key="..."))

# Use typed methods with full IDE autocomplete
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Linear API Reference](https://linear.app/developers/graphql).

## Version Information

**Package Version:** 0.19.3

**Connector Version:** 0.1.0

**Generated with connector-sdk:** f2497f7128da08585d1470953e773671d33f348f