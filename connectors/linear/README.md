# Airbyte Linear AI Connector

Connector for Linear GraphQL API

## Installation

```bash
uv pip install airbyte-ai-linear
```

## Usage

```python
from airbyte_ai_linear import LinearConnector, LinearAuthConfig

connector = LinearConnector(auth_config=LinearAuthConfig(api_key="..."))
result = connector.issues.list()
```

## Documentation

| Entity | Actions |
|--------|---------|
| Issues | [List](./REFERENCE.md#issues-list), [Get](./REFERENCE.md#issues-get) |
| Projects | [List](./REFERENCE.md#projects-list), [Get](./REFERENCE.md#projects-get) |
| Teams | [List](./REFERENCE.md#teams-list), [Get](./REFERENCE.md#teams-get) |


For detailed documentation on available actions and parameters, see [REFERENCE.md](./REFERENCE.md).

For the service's official API docs, see [Linear API Reference](https://linear.app/developers/graphql).

## Version Information

**Package Version:** 0.19.7

**Connector Version:** 0.1.0

**Generated with connector-sdk:** 9f7f8a98389c3775a4d22db1aa81fbb03020a65b