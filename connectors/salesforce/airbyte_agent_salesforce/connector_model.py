"""
Connector model for salesforce.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""

from __future__ import annotations

from ._vendored.connector_sdk.types import (
    Action,
    AuthConfig,
    AuthType,
    ConnectorModel,
    EndpointDefinition,
    EntityDefinition,
)
from ._vendored.connector_sdk.schema.security import (
    AirbyteAuthConfig,
    AuthConfigFieldSpec,
)
from ._vendored.connector_sdk.schema.components import (
    PathOverrideConfig,
)
from uuid import (
    UUID,
)

SalesforceConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('b117307c-14b6-41aa-9422-947e34922962'),
    name='salesforce',
    version='1.0.8',
    base_url='{instance_url}/services/data/v59.0',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://login.salesforce.com/services/oauth2/token',
            'auth_style': 'body',
            'body_format': 'form',
            'token_extract': ['instance_url'],
        },
        user_config_spec=AirbyteAuthConfig(
            title='Salesforce OAuth 2.0',
            type='object',
            required=['refresh_token', 'client_id', 'client_secret'],
            properties={
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='OAuth refresh token for automatic token renewal',
                ),
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='Connected App Consumer Key',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='Connected App Consumer Secret',
                ),
            },
            auth_mapping={
                'refresh_token': '${refresh_token}',
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
            },
            replication_auth_key_mapping={
                'client_id': 'client_id',
                'client_secret': 'client_secret',
                'refresh_token': 'refresh_token',
            },
        ),
    ),
    entities=[
        EntityDefinition(
            name='accounts',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:accounts',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of accounts via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Account ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for accounts',
                        'properties': {
                            'totalSize': {'type': 'integer', 'description': 'Total number of records'},
                            'done': {'type': 'boolean', 'description': 'Whether all records have been returned'},
                            'nextRecordsUrl': {'type': 'string', 'description': 'URL to fetch next page of results'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Account object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string', 'description': 'Unique identifier'},
                                        'Name': {'type': 'string', 'description': 'Account name'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'accounts',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Account/{id}',
                    action=Action.GET,
                    description='Get a single account by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Account object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string', 'description': 'Unique identifier'},
                            'Name': {'type': 'string', 'description': 'Account name'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'accounts',
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:accounts',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for accounts using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields and objects.\nUse SOQL (list action) for structured queries with specific field conditions.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Account object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string', 'description': 'Unique identifier'},
                    'Name': {'type': 'string', 'description': 'Account name'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'accounts',
            },
        ),
        EntityDefinition(
            name='contacts',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:contacts',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of contacts via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Contact ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for contacts',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Contact object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Name': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'contacts',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Contact/{id}',
                    action=Action.GET,
                    description='Get a single contact by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Contact object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Name': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'contacts',
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:contacts',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for contacts using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Contact object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Name': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'contacts',
            },
        ),
        EntityDefinition(
            name='leads',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:leads',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of leads via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Lead ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for leads',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Lead object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Name': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'leads',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Lead/{id}',
                    action=Action.GET,
                    description='Get a single lead by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Lead object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Name': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'leads',
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:leads',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for leads using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Lead object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Name': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'leads',
            },
        ),
        EntityDefinition(
            name='opportunities',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:opportunities',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of opportunities via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Opportunity ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for opportunities',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Opportunity object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Name': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'opportunities',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Opportunity/{id}',
                    action=Action.GET,
                    description='Get a single opportunity by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Opportunity object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Name': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'opportunities',
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:opportunities',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for opportunities using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Opportunity object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Name': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'opportunities',
            },
        ),
        EntityDefinition(
            name='tasks',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:tasks',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of tasks via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Task ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for tasks',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Task object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Subject': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Task/{id}',
                    action=Action.GET,
                    description='Get a single task by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Task object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Subject': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'tasks',
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:tasks',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for tasks using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Task object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Subject': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'tasks',
            },
        ),
        EntityDefinition(
            name='events',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:events',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of events via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Event ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for events',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Event object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Subject': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'events',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Event/{id}',
                    action=Action.GET,
                    description='Get a single event by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Event object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Subject': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'events',
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:events',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for events using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Event object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Subject': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'events',
            },
        ),
        EntityDefinition(
            name='campaigns',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:campaigns',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of campaigns via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Campaign ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for campaigns',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Campaign object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Name': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'campaigns',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Campaign/{id}',
                    action=Action.GET,
                    description='Get a single campaign by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Campaign object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Name': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'campaigns',
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:campaigns',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for campaigns using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Campaign object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Name': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'campaigns',
            },
        ),
        EntityDefinition(
            name='cases',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:cases',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of cases via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Case ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for cases',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Case object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'CaseNumber': {'type': 'string'},
                                        'Subject': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'cases',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Case/{id}',
                    action=Action.GET,
                    description='Get a single case by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Case object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'CaseNumber': {'type': 'string'},
                            'Subject': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'cases',
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:cases',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for cases using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Case object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'CaseNumber': {'type': 'string'},
                    'Subject': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'cases',
            },
        ),
        EntityDefinition(
            name='notes',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:notes',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of notes via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Note ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for notes',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Note object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Title': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'notes',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Note/{id}',
                    action=Action.GET,
                    description='Get a single note by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Note object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Title': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'notes',
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:notes',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for notes using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Note object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Title': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'notes',
            },
        ),
        EntityDefinition(
            name='content_versions',
            actions=[Action.LIST, Action.GET, Action.DOWNLOAD],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:content_versions',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of content versions (file metadata) via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\nNote: ContentVersion does not support FIELDS(STANDARD), so specific fields must be listed.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT Id, Title, FileExtension, ContentSize, ContentDocumentId, VersionNumber, IsLatest, CreatedDate, LastModifiedDate FROM ContentVersion ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for content versions',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce ContentVersion object - represents a file version in Salesforce Files',
                                    'properties': {
                                        'Id': {'type': 'string', 'description': 'Unique identifier'},
                                        'Title': {'type': 'string', 'description': 'File title/name'},
                                        'FileExtension': {'type': 'string', 'description': 'File extension (e.g., pdf, docx)'},
                                        'ContentSize': {'type': 'integer', 'description': 'File size in bytes'},
                                        'ContentDocumentId': {'type': 'string', 'description': 'ID of the parent ContentDocument'},
                                        'VersionNumber': {'type': 'string', 'description': 'Version number of the file'},
                                        'IsLatest': {'type': 'boolean', 'description': 'Whether this is the latest version'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'content_versions',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/ContentVersion/{id}',
                    action=Action.GET,
                    description="Get a single content version's metadata by ID. Returns file metadata, not the file content.\nUse the download action to retrieve the actual file binary.\n",
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce ContentVersion object - represents a file version in Salesforce Files',
                        'properties': {
                            'Id': {'type': 'string', 'description': 'Unique identifier'},
                            'Title': {'type': 'string', 'description': 'File title/name'},
                            'FileExtension': {'type': 'string', 'description': 'File extension (e.g., pdf, docx)'},
                            'ContentSize': {'type': 'integer', 'description': 'File size in bytes'},
                            'ContentDocumentId': {'type': 'string', 'description': 'ID of the parent ContentDocument'},
                            'VersionNumber': {'type': 'string', 'description': 'Version number of the file'},
                            'IsLatest': {'type': 'boolean', 'description': 'Whether this is the latest version'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'content_versions',
                    },
                ),
                Action.DOWNLOAD: EndpointDefinition(
                    method='GET',
                    path='/sobjects/ContentVersion/{id}/VersionData',
                    action=Action.DOWNLOAD,
                    description='Downloads the binary file content of a content version.\nFirst use the list or get action to retrieve the ContentVersion ID and file metadata (size, type, etc.),\nthen use this action to download the actual file content.\nThe response is the raw binary file data.\n',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce ContentVersion object - represents a file version in Salesforce Files',
                'properties': {
                    'Id': {'type': 'string', 'description': 'Unique identifier'},
                    'Title': {'type': 'string', 'description': 'File title/name'},
                    'FileExtension': {'type': 'string', 'description': 'File extension (e.g., pdf, docx)'},
                    'ContentSize': {'type': 'integer', 'description': 'File size in bytes'},
                    'ContentDocumentId': {'type': 'string', 'description': 'ID of the parent ContentDocument'},
                    'VersionNumber': {'type': 'string', 'description': 'Version number of the file'},
                    'IsLatest': {'type': 'boolean', 'description': 'Whether this is the latest version'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'content_versions',
            },
        ),
        EntityDefinition(
            name='attachments',
            actions=[Action.LIST, Action.GET, Action.DOWNLOAD],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:attachments',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of attachments (legacy) via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\nNote: Attachments are a legacy feature; consider using ContentVersion (Salesforce Files) for new implementations.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT Id, Name, ContentType, BodyLength, ParentId, CreatedDate, LastModifiedDate FROM Attachment ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for attachments',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Attachment object - legacy file attachment on a record',
                                    'properties': {
                                        'Id': {'type': 'string', 'description': 'Unique identifier'},
                                        'Name': {'type': 'string', 'description': 'File name'},
                                        'ContentType': {'type': 'string', 'description': 'MIME type of the file'},
                                        'BodyLength': {'type': 'integer', 'description': 'File size in bytes'},
                                        'ParentId': {'type': 'string', 'description': 'ID of the parent record this attachment is attached to'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'attachments',
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Attachment/{id}',
                    action=Action.GET,
                    description="Get a single attachment's metadata by ID. Returns file metadata, not the file content.\nUse the download action to retrieve the actual file binary.\nNote: Attachments are a legacy feature; consider using ContentVersion for new implementations.\n",
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Attachment object - legacy file attachment on a record',
                        'properties': {
                            'Id': {'type': 'string', 'description': 'Unique identifier'},
                            'Name': {'type': 'string', 'description': 'File name'},
                            'ContentType': {'type': 'string', 'description': 'MIME type of the file'},
                            'BodyLength': {'type': 'integer', 'description': 'File size in bytes'},
                            'ParentId': {'type': 'string', 'description': 'ID of the parent record this attachment is attached to'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'attachments',
                    },
                ),
                Action.DOWNLOAD: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Attachment/{id}/Body',
                    action=Action.DOWNLOAD,
                    description='Downloads the binary file content of an attachment (legacy).\nFirst use the list or get action to retrieve the Attachment ID and file metadata,\nthen use this action to download the actual file content.\nNote: Attachments are a legacy feature; consider using ContentVersion for new implementations.\n',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Attachment object - legacy file attachment on a record',
                'properties': {
                    'Id': {'type': 'string', 'description': 'Unique identifier'},
                    'Name': {'type': 'string', 'description': 'File name'},
                    'ContentType': {'type': 'string', 'description': 'MIME type of the file'},
                    'BodyLength': {'type': 'integer', 'description': 'File size in bytes'},
                    'ParentId': {'type': 'string', 'description': 'ID of the parent record this attachment is attached to'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'attachments',
            },
        ),
        EntityDefinition(
            name='query',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query',
                    action=Action.LIST,
                    description='Execute a custom SOQL query and return results. Use this for querying any Salesforce object.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Generic SOQL query result',
                        'properties': {
                            'totalSize': {'type': 'integer', 'description': 'Total number of records matching the query'},
                            'done': {'type': 'boolean', 'description': 'Whether all records have been returned'},
                            'nextRecordsUrl': {'type': 'string', 'description': 'URL to fetch next page of results (if done is false)'},
                            'records': {
                                'type': 'array',
                                'description': 'Array of record objects',
                                'items': {'type': 'object', 'additionalProperties': True},
                            },
                        },
                        'x-airbyte-entity-name': 'query',
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Generic SOQL query result',
                'properties': {
                    'totalSize': {'type': 'integer', 'description': 'Total number of records matching the query'},
                    'done': {'type': 'boolean', 'description': 'Whether all records have been returned'},
                    'nextRecordsUrl': {'type': 'string', 'description': 'URL to fetch next page of results (if done is false)'},
                    'records': {
                        'type': 'array',
                        'description': 'Array of record objects',
                        'items': {'type': 'object', 'additionalProperties': True},
                    },
                },
                'x-airbyte-entity-name': 'query',
            },
        ),
    ],
    search_field_paths={
        'accounts': [
            'Id',
            'Name',
            'AccountSource',
            'BillingAddress',
            'BillingCity',
            'BillingCountry',
            'BillingPostalCode',
            'BillingState',
            'BillingStreet',
            'CreatedById',
            'CreatedDate',
            'Description',
            'Industry',
            'IsDeleted',
            'LastActivityDate',
            'LastModifiedById',
            'LastModifiedDate',
            'NumberOfEmployees',
            'OwnerId',
            'ParentId',
            'Phone',
            'ShippingAddress',
            'ShippingCity',
            'ShippingCountry',
            'ShippingPostalCode',
            'ShippingState',
            'ShippingStreet',
            'Type',
            'Website',
            'SystemModstamp',
        ],
        'contacts': [
            'Id',
            'AccountId',
            'CreatedById',
            'CreatedDate',
            'Department',
            'Email',
            'FirstName',
            'IsDeleted',
            'LastActivityDate',
            'LastModifiedById',
            'LastModifiedDate',
            'LastName',
            'LeadSource',
            'MailingAddress',
            'MailingCity',
            'MailingCountry',
            'MailingPostalCode',
            'MailingState',
            'MailingStreet',
            'MobilePhone',
            'Name',
            'OwnerId',
            'Phone',
            'ReportsToId',
            'Title',
            'SystemModstamp',
        ],
        'leads': [
            'Id',
            'Address',
            'City',
            'Company',
            'ConvertedAccountId',
            'ConvertedContactId',
            'ConvertedDate',
            'ConvertedOpportunityId',
            'Country',
            'CreatedById',
            'CreatedDate',
            'Email',
            'FirstName',
            'Industry',
            'IsConverted',
            'IsDeleted',
            'LastActivityDate',
            'LastModifiedById',
            'LastModifiedDate',
            'LastName',
            'LeadSource',
            'MobilePhone',
            'Name',
            'NumberOfEmployees',
            'OwnerId',
            'Phone',
            'PostalCode',
            'Rating',
            'State',
            'Status',
            'Street',
            'Title',
            'Website',
            'SystemModstamp',
        ],
        'opportunities': [
            'Id',
            'AccountId',
            'Amount',
            'CampaignId',
            'CloseDate',
            'ContactId',
            'CreatedById',
            'CreatedDate',
            'Description',
            'ExpectedRevenue',
            'ForecastCategory',
            'ForecastCategoryName',
            'IsClosed',
            'IsDeleted',
            'IsWon',
            'LastActivityDate',
            'LastModifiedById',
            'LastModifiedDate',
            'LeadSource',
            'Name',
            'NextStep',
            'OwnerId',
            'Probability',
            'StageName',
            'Type',
            'SystemModstamp',
        ],
        'tasks': [
            'Id',
            'AccountId',
            'ActivityDate',
            'CallDisposition',
            'CallDurationInSeconds',
            'CallType',
            'CompletedDateTime',
            'CreatedById',
            'CreatedDate',
            'Description',
            'IsClosed',
            'IsDeleted',
            'IsHighPriority',
            'LastModifiedById',
            'LastModifiedDate',
            'OwnerId',
            'Priority',
            'Status',
            'Subject',
            'TaskSubtype',
            'Type',
            'WhatId',
            'WhoId',
            'SystemModstamp',
        ],
        'users': [
            'Id',
            'AccountId',
            'Alias',
            'City',
            'CompanyName',
            'ContactId',
            'Country',
            'CreatedById',
            'CreatedDate',
            'Department',
            'Division',
            'Email',
            'EmployeeNumber',
            'FirstName',
            'IsActive',
            'LastLoginDate',
            'LastModifiedById',
            'LastModifiedDate',
            'LastName',
            'ManagerId',
            'MobilePhone',
            'Name',
            'Phone',
            'PostalCode',
            'ProfileId',
            'State',
            'Street',
            'Title',
            'UserRoleId',
            'UserType',
            'Username',
            'SystemModstamp',
        ],
        'opportunity_stages': [
            'Id',
            'ApiName',
            'CreatedById',
            'CreatedDate',
            'DefaultProbability',
            'Description',
            'ForecastCategory',
            'ForecastCategoryName',
            'IsActive',
            'IsClosed',
            'IsWon',
            'LastModifiedById',
            'LastModifiedDate',
            'MasterLabel',
            'SortOrder',
            'SystemModstamp',
        ],
    },
)