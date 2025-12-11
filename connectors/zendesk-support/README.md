# Airbyte Zendesk-Support AI Connector

Type-safe Zendesk-Support API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-zendesk-support
```

## Usage

```python
from airbyte_ai_zendesk_support import ZendeskSupportConnector
from airbyte_ai_zendesk_support.models import ZendeskSupportAuthConfig

# Create connector
connector = ZendeskSupportConnector(auth_config=ZendeskSupportAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))

# Use typed methods with full IDE autocomplete
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Zendesk-Support API Reference](https://developer.zendesk.com/api-reference/ticketing/introduction/).

## Version Information

**Package Version:** 0.18.3

**Connector Version:** 0.1.1

**Generated with connector-sdk:** f2497f7128da08585d1470953e773671d33f348f