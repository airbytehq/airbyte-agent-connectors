# Stripe

## Supported Entities and Actions

| Entity | Actions |
|--------|---------|
| Customers | [List](#customers-list), [Get](#customers-get) |

### Customers

#### Customers List

Returns a list of customers

**Python SDK**

```python
stripe.customers.list()
```

**API**

```bash
curl --location 'https://api.airbyte.ai/api/v1/connectors/instances/{your_connector_instance_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "customers",
    "action": "list"
}'
```


**Params**

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `limit` | `integer` | No | A limit on the number of objects to be returned |
| `starting_after` | `string` | No | A cursor for use in pagination |
| `ending_before` | `string` | No | A cursor for use in pagination |
| `email` | `string` | No | Filter customers by email address |


<details>
<summary><b>Response Schema</b></summary>

**Records**

| Field Name | Type | Description |
|------------|------|-------------|
| `object` | `"list"` |  |
| `data` | `array<object>` |  |
| `data[].id` | `string` |  |
| `data[].object` | `"customer"` |  |
| `data[].email` | `string` |  |
| `data[].name` | `string` |  |
| `data[].description` | `string \| null` |  |
| `data[].phone` | `string \| null` |  |
| `data[].address` | `object \| null` |  |
| `data[].metadata` | `object` |  |
| `data[].created` | `integer` |  |
| `data[].balance` | `integer` |  |
| `data[].delinquent` | `boolean` |  |
| `data[].currency` | `string \| null` |  |
| `data[].default_currency` | `string \| null` |  |
| `data[].default_source` | `string \| null` |  |
| `data[].discount` | `object \| null` |  |
| `data[].invoice_prefix` | `string \| null` |  |
| `data[].invoice_settings` | `object \| null` |  |
| `data[].livemode` | `boolean` |  |
| `data[].next_invoice_sequence` | `integer \| null` |  |
| `data[].preferred_locales` | `array \| null` |  |
| `data[].shipping` | `object \| null` |  |
| `data[].tax_exempt` | `string \| null` |  |
| `data[].test_clock` | `string \| null` |  |
| `has_more` | `boolean` |  |
| `url` | `string` |  |


</details>

#### Customers Get

Gets the details of an existing customer

**Python SDK**

```python
stripe.customers.get(
    id="<str>"
)
```

**API**

```bash
curl --location 'https://api.airbyte.ai/api/v1/connectors/instances/{your_connector_instance_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "customers",
    "action": "get",
    "params": {
        "id": "<str>"
    }
}'
```


**Params**

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `id` | `string` | Yes | The customer ID |


<details>
<summary><b>Response Schema</b></summary>

**Records**

| Field Name | Type | Description |
|------------|------|-------------|
| `id` | `string` |  |
| `object` | `"customer"` |  |
| `email` | `string` |  |
| `name` | `string` |  |
| `description` | `string \| null` |  |
| `phone` | `string \| null` |  |
| `address` | `object \| null` |  |
| `metadata` | `object` |  |
| `created` | `integer` |  |
| `balance` | `integer` |  |
| `delinquent` | `boolean` |  |
| `currency` | `string \| null` |  |
| `default_currency` | `string \| null` |  |
| `default_source` | `string \| null` |  |
| `discount` | `object \| null` |  |
| `invoice_prefix` | `string \| null` |  |
| `invoice_settings` | `object \| null` |  |
| `livemode` | `boolean` |  |
| `next_invoice_sequence` | `integer \| null` |  |
| `preferred_locales` | `array \| null` |  |
| `shipping` | `object \| null` |  |
| `tax_exempt` | `string \| null` |  |
| `test_clock` | `string \| null` |  |


</details>



## Authentication

The Stripe connector supports the following authentication methods:


### Authentication

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| `token` | `str` | Yes | Authentication bearer token |

#### Example

**Python SDK**

```python
StripeConnector(
  auth_config=StripeAuthConfig(
    token="<Authentication bearer token>"
  )
)
```

**API**

```bash
curl --location 'https://api.airbyte.ai/api/v1/connectors/instances' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
  "connector_definition_id": "e094cb9a-26de-4645-8761-65c0c425d1de",
  "auth_config": {
    "token": "<Authentication bearer token>"
  },
  "name": "My Stripe Connector"
}'
```

