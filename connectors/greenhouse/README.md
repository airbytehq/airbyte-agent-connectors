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

# Create connector
connector = GreenhouseConnector(auth_config=GreenhouseAuthConfig(api_key="..."))

# Use typed methods with full IDE autocomplete
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Greenhouse API Reference](https://developers.greenhouse.io/harvest.html).

## Version Information

**Package Version:** 0.17.3

**Connector Version:** 0.1.0

**Generated with connector-sdk:** f2497f7128da08585d1470953e773671d33f348f