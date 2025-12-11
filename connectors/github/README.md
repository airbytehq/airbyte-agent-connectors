# Airbyte Github AI Connector

Type-safe Github API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-github
```

## Usage

```python
from airbyte_ai_github import GithubConnector
from airbyte_ai_github.models import GithubAuthConfig

connector = GithubConnector(auth_config=GithubAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
result = connector.repositories.get()
```

## Documentation

For available actions and detailed API documentation, see [DOCS.md](./DOCS.md).

For the service's official API docs, see [Github API Reference](https://docs.github.com/en/rest).

## Version Information

**Package Version:** 0.18.5

**Connector Version:** 0.1.0

**Generated with connector-sdk:** 11427ac330c199db4b55578f96eb18ab6474610e