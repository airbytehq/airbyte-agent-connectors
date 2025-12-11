# Airbyte Gong AI Connector

Type-safe Gong API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-gong
```

## Usage

```python
from airbyte_ai_gong import GongConnector
from airbyte_ai_gong.models import GongAuthConfig

connector = GongConnector(auth_config=GongAuthConfig(access_key="...", access_key_secret="..."))
result = connector.users.list()
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Gong API Reference](https://gong.app.gong.io/settings/api/documentation).

## Version Information

**Package Version:** 0.19.7

**Connector Version:** 0.1.1

**Generated with connector-sdk:** 38493f4df1859089d0c051397632481b41429c7c