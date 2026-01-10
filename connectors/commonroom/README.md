# Commonroom agent connector

Commonroom is a community management platform that helps companies understand and engage
with their community members. This connector provides access to API token status, custom fields,
activity types, segments, and tags for community analytics and management.


## Installation

```bash
uv pip install airbyte-agent-commonroom
```

## Usage

```python
from airbyte_agent_commonroom import CommonroomConnector, CommonroomAuthConfig

connector = CommonroomConnector(
  auth_config=CommonroomAuthConfig(
    api_token="..."
  )
)
result = await connector.api_token_status.list()
```


## Full documentation

This connector supports the following entities and actions.

| Entity | Actions |
|--------|---------|
| Api Token Status | [List](./REFERENCE.md#api-token-status-list) |
| Contact Custom Fields | [List](./REFERENCE.md#contact-custom-fields-list) |
| Activity Types | [List](./REFERENCE.md#activity-types-list) |
| Segments | [List](./REFERENCE.md#segments-list) |
| Tags | [List](./REFERENCE.md#tags-list) |


For detailed documentation on available actions and parameters, see this connector's [full reference documentation](./REFERENCE.md).

For the service's official API docs, see the [Commonroom API reference](https://docs.commonroom.io/).

## Version information

- **Package version:** 0.1.0
- **Connector version:** 0.1.0
- **Generated with Connector SDK commit SHA:** unknown