"""
Connector model for airtable.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""

from __future__ import annotations

from airbyte_agent_sdk.types import (
    Action,
    AuthConfig,
    AuthType,
    ConnectorModel,
    EndpointDefinition,
    EntityDefinition,
)
from airbyte_agent_sdk.schema.security import (
    AuthConfigFieldSpec,
    AuthConfigSpec,
)
from airbyte_agent_sdk.schema.extensions import (
    EntityRelationshipConfig,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

AirtableConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('14c6e7ea-97ed-4f5e-a7b5-25e9a80b8212'),
    name='airtable',
    version='1.0.8',
    base_url='https://api.airtable.com/v0',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AuthConfigSpec(
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
            replication_auth_key_constants={'credentials.auth_method': 'api_key'},
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
                    meta_extractor={'offset': '$.offset'},
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
                    no_pagination='Airtable Metadata API returns all tables for a base in a single response with no pagination support.',
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
            relationships=[
                EntityRelationshipConfig(
                    source_entity='tables',
                    target_entity='bases',
                    foreign_key='base_id',
                    cardinality='many_to_one',
                ),
            ],
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
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'minimum': 1,
                            'maximum': 100,
                        },
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
                    meta_extractor={'offset': '$.offset'},
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
            relationships=[
                EntityRelationshipConfig(
                    source_entity='records',
                    target_entity='bases',
                    foreign_key='base_id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='records',
                    target_entity='tables',
                    foreign_key='table_id_or_name',
                    cardinality='many_to_one',
                ),
            ],
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
    example_questions=ExampleQuestions(
        direct=[
            'List all my Airtable bases',
            'What tables are in my first base?',
            'Show me the schema for tables in a base',
            'List records from a table in my base',
            'Show me recent records from a table',
            'What fields are in a table?',
        ],
        context_store_search=["List records where Status is 'Done' in table tblXXX", 'Find records created last week in table tblXXX', 'Show me records updated in the last 30 days in base appXXX'],
        search=["List records where Status is 'Done' in table tblXXX", 'Find records created last week in table tblXXX', 'Show me records updated in the last 30 days in base appXXX'],
        unsupported=[
            'Create a new record in Airtable',
            'Update a record in Airtable',
            'Delete a record from Airtable',
            'Create a new table',
            'Modify table schema',
        ],
    ),
)