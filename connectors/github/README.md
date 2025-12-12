# Airbyte Github AI Connector

Type-safe Github API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-github
```

## Usage

```python
from airbyte_ai_github import GithubConnector, GithubAuthConfig

connector = GithubConnector(auth_config=GithubAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
result = connector.repositories.get()
```

## Documentation

| Entity | Actions |
|--------|---------|
| Repositories | [Get](./REFERENCE.md#repositories-get), [List](./REFERENCE.md#repositories-list), [Search](./REFERENCE.md#repositories-search) |
| Org Repositories | [List](./REFERENCE.md#org-repositories-list) |
| Branches | [List](./REFERENCE.md#branches-list), [Get](./REFERENCE.md#branches-get) |
| Commits | [List](./REFERENCE.md#commits-list), [Get](./REFERENCE.md#commits-get) |
| Releases | [List](./REFERENCE.md#releases-list), [Get](./REFERENCE.md#releases-get) |
| Issues | [List](./REFERENCE.md#issues-list), [Get](./REFERENCE.md#issues-get), [Search](./REFERENCE.md#issues-search) |
| Pull Requests | [List](./REFERENCE.md#pull-requests-list), [Get](./REFERENCE.md#pull-requests-get), [Search](./REFERENCE.md#pull-requests-search) |
| Reviews | [List](./REFERENCE.md#reviews-list) |
| Comments | [List](./REFERENCE.md#comments-list), [Get](./REFERENCE.md#comments-get) |
| Pr Comments | [List](./REFERENCE.md#pr-comments-list), [Get](./REFERENCE.md#pr-comments-get) |
| Labels | [List](./REFERENCE.md#labels-list), [Get](./REFERENCE.md#labels-get) |
| Milestones | [List](./REFERENCE.md#milestones-list), [Get](./REFERENCE.md#milestones-get) |
| Organizations | [Get](./REFERENCE.md#organizations-get), [List](./REFERENCE.md#organizations-list) |
| Users | [Get](./REFERENCE.md#users-get), [List](./REFERENCE.md#users-list), [Search](./REFERENCE.md#users-search) |
| Teams | [List](./REFERENCE.md#teams-list), [Get](./REFERENCE.md#teams-get) |
| Tags | [List](./REFERENCE.md#tags-list), [Get](./REFERENCE.md#tags-get) |
| Stargazers | [List](./REFERENCE.md#stargazers-list) |
| Viewer | [Get](./REFERENCE.md#viewer-get) |
| Viewer Repositories | [List](./REFERENCE.md#viewer-repositories-list) |


For detailed documentation on available actions and parameters, see [REFERENCE.md](./REFERENCE.md).

For the service's official API docs, see [Github API Reference](https://docs.github.com/en/rest).

## Version Information

**Package Version:** 0.18.7

**Connector Version:** 0.1.0

**Generated with connector-sdk:** 9f7f8a98389c3775a4d22db1aa81fbb03020a65b