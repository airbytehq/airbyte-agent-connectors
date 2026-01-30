"""
Connector model for airtable.

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
from uuid import (
    UUID,
)

AirtableConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('14c6e7ea-97ed-4f5e-a7b5-25e9a80b8212'),
    name='airtable',
    version='1.0.2',
    base_url='https://api.airtable.com/v0',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
            title='Personal Access Token',
            type='object',
            required=['personal_access_token'],
            properties={
                'personal_access_token': AuthConfigFieldSpec(
                    title='Personal Access Token',
                    description='Airtable Personal Access Token. See https://airtable.com/developers/web/guides/personal-access-tokens',
                ),
            },
            auth_mapping={'token': '${personal_access_token}'},
            replication_auth_key_mapping={'credentials.api_key': 'personal_access_token'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='bases',
            stream_name='bases',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/meta/bases',
                    action=Action.LIST,
                    description='Returns a list of all bases the user has access to',
                    query_params=['offset'],
                    query_params_schema={
                        'offset': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of bases',
                        'properties': {
                            'bases': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An Airtable base (workspace)',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the base'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Name of the base',
                                        },
                                        'permissionLevel': {
                                            'type': ['string', 'null'],
                                            'description': 'Permission level for the base (e.g., owner, editor, commenter, read)',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'bases',
                                    'x-airbyte-stream-name': 'bases',
                                },
                            },
                            'offset': {
                                'type': ['string', 'null'],
                                'description': 'Pagination offset for next page',
                            },
                        },
                    },
                    record_extractor='$.bases',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An Airtable base (workspace)',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the base'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Name of the base',
                    },
                    'permissionLevel': {
                        'type': ['string', 'null'],
                        'description': 'Permission level for the base (e.g., owner, editor, commenter, read)',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'bases',
                'x-airbyte-stream-name': 'bases',
            },
        ),
        EntityDefinition(
            name='tables',
            stream_name='tables',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/meta/bases/{base_id}/tables',
                    action=Action.LIST,
                    description='Returns a list of all tables in the specified base with their schema information',
                    path_params=['base_id'],
                    path_params_schema={
                        'base_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'List of tables in a base',
                        'properties': {
                            'tables': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A table within an Airtable base',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the table'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Name of the table',
                                        },
                                        'primaryFieldId': {
                                            'type': ['string', 'null'],
                                            'description': 'ID of the primary field',
                                        },
                                        'fields': {
                                            'type': ['array', 'null'],
                                            'description': 'List of fields in the table',
                                            'items': {
                                                'type': 'object',
                                                'description': 'A field (column) in a table',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Unique identifier for the field',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Name of the field',
                                                    },
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Type of the field (e.g., singleLineText, number, checkbox)',
                                                    },
                                                    'options': {
                                                        'type': ['object', 'null'],
                                                        'description': 'Field-specific options',
                                                        'additionalProperties': True,
                                                    },
                                                },
                                            },
                                        },
                                        'views': {
                                            'type': ['array', 'null'],
                                            'description': 'List of views in the table',
                                            'items': {
                                                'type': 'object',
                                                'description': 'A view in a table',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Unique identifier for the view',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Name of the view',
                                                    },
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Type of the view (e.g., grid, form, calendar)',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'tables',
                                    'x-airbyte-stream-name': 'tables',
                                },
                            },
                        },
                    },
                    record_extractor='$.tables',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A table within an Airtable base',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the table'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Name of the table',
                    },
                    'primaryFieldId': {
                        'type': ['string', 'null'],
                        'description': 'ID of the primary field',
                    },
                    'fields': {
                        'type': ['array', 'null'],
                        'description': 'List of fields in the table',
                        'items': {'$ref': '#/components/schemas/TableField'},
                    },
                    'views': {
                        'type': ['array', 'null'],
                        'description': 'List of views in the table',
                        'items': {'$ref': '#/components/schemas/View'},
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'tables',
                'x-airbyte-stream-name': 'tables',
            },
        ),
        EntityDefinition(
            name='records',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/{base_id}/{table_id_or_name}',
                    action=Action.LIST,
                    description='Returns a paginated list of records from the specified table',
                    query_params=[
                        'offset',
                        'pageSize',
                        'view',
                        'filterByFormula',
                        'sort',
                    ],
                    query_params_schema={
                        'offset': {'type': 'string', 'required': False},
                        'pageSize': {'type': 'integer', 'required': False},
                        'view': {'type': 'string', 'required': False},
                        'filterByFormula': {'type': 'string', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                    },
                    path_params=['base_id', 'table_id_or_name'],
                    path_params_schema={
                        'base_id': {'type': 'string', 'required': True},
                        'table_id_or_name': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of records',
                        'properties': {
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A record (row) in an Airtable table',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the record'},
                                        'createdTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the record was created',
                                        },
                                        'fields': {
                                            'type': ['object', 'null'],
                                            'description': 'Field values for the record',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'records',
                                },
                            },
                            'offset': {
                                'type': ['string', 'null'],
                                'description': 'Pagination offset for next page',
                            },
                        },
                    },
                    record_extractor='$.records',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/{base_id}/{table_id_or_name}/{record_id}',
                    action=Action.GET,
                    description='Returns a single record by ID from the specified table',
                    path_params=['base_id', 'table_id_or_name', 'record_id'],
                    path_params_schema={
                        'base_id': {'type': 'string', 'required': True},
                        'table_id_or_name': {'type': 'string', 'required': True},
                        'record_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A record (row) in an Airtable table',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique identifier for the record'},
                            'createdTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the record was created',
                            },
                            'fields': {
                                'type': ['object', 'null'],
                                'description': 'Field values for the record',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'records',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A record (row) in an Airtable table',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the record'},
                    'createdTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the record was created',
                    },
                    'fields': {
                        'type': ['object', 'null'],
                        'description': 'Field values for the record',
                        'additionalProperties': True,
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'records',
            },
        ),
    ],
    search_field_paths={
        'bases': ['id', 'name', 'permissionLevel'],
        'tables': [
            'id',
            'name',
            'primaryFieldId',
            'fields',
            'fields[]',
            'views',
            'views[]',
        ],
    },
)