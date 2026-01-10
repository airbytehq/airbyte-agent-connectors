# Commonroom full reference

This is the full reference documentation for the Commonroom agent connector.

## Supported entities and actions

The Commonroom connector supports the following entities and actions.

| Entity | Actions |
|--------|---------|
| Api Token Status | [List](#api-token-status-list) |
| Contact Custom Fields | [List](#contact-custom-fields-list) |
| Activity Types | [List](#activity-types-list) |
| Segments | [List](#segments-list) |
| Tags | [List](#tags-list) |

### Api Token Status

#### Api Token Status List

Returns the status and metadata of the current API token

**Python SDK**

```python
await commonroom.api_token_status.list()
```

**API**

```bash
curl --location 'https://api.airbyte.ai/api/v1/connectors/instances/{your_connector_instance_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "api_token_status",
    "action": "list"
}'
```



<details>
<summary><b>Response Schema</b></summary>

**Records**

| Field Name | Type | Description |
|------------|------|-------------|
| `jti` | `string \| null` |  |
| `iat` | `integer \| null` |  |
| `exp` | `integer \| null` |  |
| `sub` | `string \| null` |  |


</details>

### Contact Custom Fields

#### Contact Custom Fields List

Returns all custom fields defined for contacts/members

**Python SDK**

```python
await commonroom.contact_custom_fields.list()
```

**API**

```bash
curl --location 'https://api.airbyte.ai/api/v1/connectors/instances/{your_connector_instance_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "contact_custom_fields",
    "action": "list"
}'
```



### Activity Types

#### Activity Types List

Returns all activity types in the community

**Python SDK**

```python
await commonroom.activity_types.list()
```

**API**

```bash
curl --location 'https://api.airbyte.ai/api/v1/connectors/instances/{your_connector_instance_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "activity_types",
    "action": "list"
}'
```



### Segments

#### Segments List

Returns all segments in the community

**Python SDK**

```python
await commonroom.segments.list()
```

**API**

```bash
curl --location 'https://api.airbyte.ai/api/v1/connectors/instances/{your_connector_instance_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "segments",
    "action": "list"
}'
```



### Tags

#### Tags List

Returns all tags in the community

**Python SDK**

```python
await commonroom.tags.list()
```

**API**

```bash
curl --location 'https://api.airbyte.ai/api/v1/connectors/instances/{your_connector_instance_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "tags",
    "action": "list"
}'
```



<details>
<summary><b>Response Schema</b></summary>

**Records**

| Field Name | Type | Description |
|------------|------|-------------|
| `id` | `string` |  |
| `name` | `string \| null` |  |
| `description` | `string \| null` |  |
| `createdAt` | `string \| null` |  |
| `deletedAt` | `string \| null` |  |
| `entityTypes` | `array \| null` |  |


</details>



## Authentication

The Commonroom connector supports the following authentication methods.


### API Token Authentication

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| `api_token` | `str` | Yes | API token for authenticating with CommonRoom API. Create a token at https://app.commonroom.io/ under Settings | API tokens. |

#### Example

**Python SDK**

```python
CommonroomConnector(
  auth_config=CommonroomAuthConfig(
    api_token="<API token for authenticating with CommonRoom API. Create a token at https://app.commonroom.io/ under Settings | API tokens.>"
  )
)
```

**API**

```bash
curl --location 'https://api.airbyte.ai/api/v1/connectors/instances' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
  "connector_definition_id": "152171eb-bedf-46d7-b2c9-c8a91b9fd5b4",
  "auth_config": {
    "api_token": "<API token for authenticating with CommonRoom API. Create a token at https://app.commonroom.io/ under Settings | API tokens.>"
  },
  "name": "My Commonroom Connector"
}'
```

