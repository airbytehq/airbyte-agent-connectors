# Airbyte Greenhouse AI Connector

Type-safe Greenhouse API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-greenhouse
```

## Usage

```python
from airbyte_ai_greenhouse import GreenhouseConnector
from airbyte_ai_greenhouse.models import GreenhouseAuthConfig

connector = GreenhouseConnector(auth_config=GreenhouseAuthConfig(api_key="..."))
result = connector.candidates.list()
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Greenhouse API Reference](https://developers.greenhouse.io/harvest.html).

## Version Information

**Package Version:** 0.17.6

**Connector Version:** 0.1.0

**Generated with connector-sdk:** 8c06aa103e1f805b2e8fad3f0ba7004db3d2773a