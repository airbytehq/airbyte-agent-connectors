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

connector = LinearConnector(auth_config=LinearAuthConfig(api_key="..."))
result = connector.issues.list()
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Linear API Reference](https://linear.app/developers/graphql).

## Version Information

**Package Version:** 0.19.5

**Connector Version:** 0.1.0

**Generated with connector-sdk:** 11427ac330c199db4b55578f96eb18ab6474610e