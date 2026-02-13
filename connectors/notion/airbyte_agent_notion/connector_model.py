"""
Connector model for notion.

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

NotionConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('6e00b415-b02e-4160-bf02-58176a0ae687'),
    name='notion',
    version='0.1.1',
    base_url='https://api.notion.com',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
            title='API Token Authentication',
            type='object',
            required=['token'],
            properties={
                'token': AuthConfigFieldSpec(
                    title='Integration Token',
                    description='Notion internal integration token (starts with ntn_ or secret_)',
                ),
            },
            auth_mapping={'token': '${token}'},
            replication_auth_key_mapping={'credentials.access_token': 'token'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='users',
            stream_name='users',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/users',
                    action=Action.LIST,
                    description='Returns a paginated list of users for the workspace',
                    query_params=['start_cursor', 'page_size'],
                    query_params_schema={
                        'start_cursor': {'type': 'string', 'required': False},
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2022-06-28',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of users',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always list',
                            },
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Notion user object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the user'},
                                        'object': {
                                            'type': ['string', 'null'],
                                            'description': 'Always user',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of user (person or bot)',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': "User's display name",
                                        },
                                        'avatar_url': {
                                            'type': ['string', 'null'],
                                            'description': "URL of the user's avatar",
                                        },
                                        'person': {
                                            'type': ['object', 'null'],
                                            'description': 'Person-specific data',
                                            'properties': {
                                                'email': {
                                                    'type': ['string', 'null'],
                                                    'description': "Person's email address",
                                                },
                                            },
                                        },
                                        'bot': {
                                            'type': ['object', 'null'],
                                            'description': 'Bot-specific data',
                                            'properties': {
                                                'owner': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Bot owner information',
                                                },
                                                'workspace_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Name of the workspace the bot belongs to',
                                                },
                                            },
                                        },
                                        'request_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Request ID for debugging',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'users',
                                    'x-airbyte-stream-name': 'users',
                                },
                            },
                            'next_cursor': {
                                'type': ['string', 'null'],
                                'description': 'Cursor for next page',
                            },
                            'has_more': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether more results exist',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of results',
                            },
                            'user': {
                                'type': ['object', 'null'],
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.next_cursor', 'has_more': '$.has_more'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/users/{user_id}',
                    action=Action.GET,
                    description='Retrieves a single user by ID',
                    path_params=['user_id'],
                    path_params_schema={
                        'user_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2022-06-28',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Notion user object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique identifier for the user'},
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always user',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of user (person or bot)',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': "User's display name",
                            },
                            'avatar_url': {
                                'type': ['string', 'null'],
                                'description': "URL of the user's avatar",
                            },
                            'person': {
                                'type': ['object', 'null'],
                                'description': 'Person-specific data',
                                'properties': {
                                    'email': {
                                        'type': ['string', 'null'],
                                        'description': "Person's email address",
                                    },
                                },
                            },
                            'bot': {
                                'type': ['object', 'null'],
                                'description': 'Bot-specific data',
                                'properties': {
                                    'owner': {
                                        'type': ['object', 'null'],
                                        'description': 'Bot owner information',
                                    },
                                    'workspace_name': {
                                        'type': ['string', 'null'],
                                        'description': 'Name of the workspace the bot belongs to',
                                    },
                                },
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'users',
                        'x-airbyte-stream-name': 'users',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Notion user object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the user'},
                    'object': {
                        'type': ['string', 'null'],
                        'description': 'Always user',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Type of user (person or bot)',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': "User's display name",
                    },
                    'avatar_url': {
                        'type': ['string', 'null'],
                        'description': "URL of the user's avatar",
                    },
                    'person': {
                        'type': ['object', 'null'],
                        'description': 'Person-specific data',
                        'properties': {
                            'email': {
                                'type': ['string', 'null'],
                                'description': "Person's email address",
                            },
                        },
                    },
                    'bot': {
                        'type': ['object', 'null'],
                        'description': 'Bot-specific data',
                        'properties': {
                            'owner': {
                                'type': ['object', 'null'],
                                'description': 'Bot owner information',
                            },
                            'workspace_name': {
                                'type': ['string', 'null'],
                                'description': 'Name of the workspace the bot belongs to',
                            },
                        },
                    },
                    'request_id': {
                        'type': ['string', 'null'],
                        'description': 'Request ID for debugging',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'users',
                'x-airbyte-stream-name': 'users',
            },
        ),
        EntityDefinition(
            name='pages',
            stream_name='pages',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v1/search:pages',
                    path_override=PathOverrideConfig(
                        path='/v1/search',
                    ),
                    action=Action.LIST,
                    description='Returns pages shared with the integration using the search endpoint',
                    body_fields=[
                        'filter',
                        'sort',
                        'start_cursor',
                        'page_size',
                    ],
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2022-06-28',
                        },
                    },
                    request_body_defaults={'page_size': 100},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filter': {
                                'type': 'object',
                                'properties': {
                                    'property': {'type': 'string', 'default': 'object'},
                                    'value': {'type': 'string', 'default': 'page'},
                                },
                            },
                            'sort': {
                                'type': 'object',
                                'properties': {
                                    'direction': {'type': 'string', 'default': 'descending'},
                                    'timestamp': {'type': 'string', 'default': 'last_edited_time'},
                                },
                            },
                            'start_cursor': {'type': 'string', 'description': 'Pagination cursor'},
                            'page_size': {
                                'type': 'integer',
                                'minimum': 1,
                                'maximum': 100,
                                'default': 100,
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of pages',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always list',
                            },
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Notion page object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the page'},
                                        'object': {
                                            'type': ['string', 'null'],
                                            'description': 'Always page',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'description': 'Date and time when the page was created',
                                        },
                                        'last_edited_time': {
                                            'type': ['string', 'null'],
                                            'description': 'Date and time when the page was last edited',
                                        },
                                        'created_by': {
                                            'type': ['object', 'null'],
                                            'description': 'User who created the page',
                                            'properties': {
                                                'object': {
                                                    'type': ['string', 'null'],
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'last_edited_by': {
                                            'type': ['object', 'null'],
                                            'description': 'User who last edited the page',
                                            'properties': {
                                                'object': {
                                                    'type': ['string', 'null'],
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'cover': {
                                            'type': ['object', 'null'],
                                            'description': 'Page cover image',
                                        },
                                        'icon': {
                                            'type': ['object', 'null'],
                                            'description': 'Page icon',
                                        },
                                        'parent': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Parent object reference',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of parent (database_id, page_id, block_id, workspace)',
                                                        },
                                                        'database_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Database parent ID',
                                                        },
                                                        'page_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Page parent ID',
                                                        },
                                                        'block_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Block parent ID',
                                                        },
                                                        'workspace': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether parent is workspace',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Parent of the page',
                                        },
                                        'archived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the page is archived',
                                        },
                                        'in_trash': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the page is in trash',
                                        },
                                        'is_locked': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the page is locked',
                                        },
                                        'properties': {
                                            'type': ['object', 'null'],
                                            'description': 'Property values of the page',
                                            'additionalProperties': True,
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL of the page',
                                        },
                                        'public_url': {
                                            'type': ['string', 'null'],
                                            'description': 'Public URL of the page if published',
                                        },
                                        'request_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Request ID for debugging',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'pages',
                                    'x-airbyte-stream-name': 'pages',
                                },
                            },
                            'next_cursor': {
                                'type': ['string', 'null'],
                                'description': 'Cursor for next page',
                            },
                            'has_more': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether more results exist',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of results',
                            },
                            'page_or_database': {
                                'type': ['object', 'null'],
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.next_cursor', 'has_more': '$.has_more'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/pages/{page_id}',
                    action=Action.GET,
                    description='Retrieves a page object using the ID specified',
                    path_params=['page_id'],
                    path_params_schema={
                        'page_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2022-06-28',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Notion page object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique identifier for the page'},
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always page',
                            },
                            'created_time': {
                                'type': ['string', 'null'],
                                'description': 'Date and time when the page was created',
                            },
                            'last_edited_time': {
                                'type': ['string', 'null'],
                                'description': 'Date and time when the page was last edited',
                            },
                            'created_by': {
                                'type': ['object', 'null'],
                                'description': 'User who created the page',
                                'properties': {
                                    'object': {
                                        'type': ['string', 'null'],
                                    },
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'last_edited_by': {
                                'type': ['object', 'null'],
                                'description': 'User who last edited the page',
                                'properties': {
                                    'object': {
                                        'type': ['string', 'null'],
                                    },
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'cover': {
                                'type': ['object', 'null'],
                                'description': 'Page cover image',
                            },
                            'icon': {
                                'type': ['object', 'null'],
                                'description': 'Page icon',
                            },
                            'parent': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Parent object reference',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of parent (database_id, page_id, block_id, workspace)',
                                            },
                                            'database_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Database parent ID',
                                            },
                                            'page_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Page parent ID',
                                            },
                                            'block_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Block parent ID',
                                            },
                                            'workspace': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether parent is workspace',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Parent of the page',
                            },
                            'archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the page is archived',
                            },
                            'in_trash': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the page is in trash',
                            },
                            'is_locked': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the page is locked',
                            },
                            'properties': {
                                'type': ['object', 'null'],
                                'description': 'Property values of the page',
                                'additionalProperties': True,
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL of the page',
                            },
                            'public_url': {
                                'type': ['string', 'null'],
                                'description': 'Public URL of the page if published',
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'pages',
                        'x-airbyte-stream-name': 'pages',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Notion page object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the page'},
                    'object': {
                        'type': ['string', 'null'],
                        'description': 'Always page',
                    },
                    'created_time': {
                        'type': ['string', 'null'],
                        'description': 'Date and time when the page was created',
                    },
                    'last_edited_time': {
                        'type': ['string', 'null'],
                        'description': 'Date and time when the page was last edited',
                    },
                    'created_by': {
                        'type': ['object', 'null'],
                        'description': 'User who created the page',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                            },
                            'id': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'last_edited_by': {
                        'type': ['object', 'null'],
                        'description': 'User who last edited the page',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                            },
                            'id': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'cover': {
                        'type': ['object', 'null'],
                        'description': 'Page cover image',
                    },
                    'icon': {
                        'type': ['object', 'null'],
                        'description': 'Page icon',
                    },
                    'parent': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Parent'},
                            {'type': 'null'},
                        ],
                        'description': 'Parent of the page',
                    },
                    'archived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the page is archived',
                    },
                    'in_trash': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the page is in trash',
                    },
                    'is_locked': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the page is locked',
                    },
                    'properties': {
                        'type': ['object', 'null'],
                        'description': 'Property values of the page',
                        'additionalProperties': True,
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'URL of the page',
                    },
                    'public_url': {
                        'type': ['string', 'null'],
                        'description': 'Public URL of the page if published',
                    },
                    'request_id': {
                        'type': ['string', 'null'],
                        'description': 'Request ID for debugging',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'pages',
                'x-airbyte-stream-name': 'pages',
            },
        ),
        EntityDefinition(
            name='databases',
            stream_name='databases',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v1/search:databases',
                    path_override=PathOverrideConfig(
                        path='/v1/search',
                    ),
                    action=Action.LIST,
                    description='Returns databases shared with the integration using the search endpoint',
                    body_fields=[
                        'filter',
                        'sort',
                        'start_cursor',
                        'page_size',
                    ],
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2022-06-28',
                        },
                    },
                    request_body_defaults={'page_size': 100},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filter': {
                                'type': 'object',
                                'properties': {
                                    'property': {'type': 'string', 'default': 'object'},
                                    'value': {'type': 'string', 'default': 'database'},
                                },
                            },
                            'sort': {
                                'type': 'object',
                                'properties': {
                                    'direction': {'type': 'string', 'default': 'descending'},
                                    'timestamp': {'type': 'string', 'default': 'last_edited_time'},
                                },
                            },
                            'start_cursor': {'type': 'string', 'description': 'Pagination cursor'},
                            'page_size': {
                                'type': 'integer',
                                'minimum': 1,
                                'maximum': 100,
                                'default': 100,
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of databases',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always list',
                            },
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Notion database object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the database'},
                                        'object': {
                                            'type': ['string', 'null'],
                                            'description': 'Always database',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'description': 'Date and time when the database was created',
                                        },
                                        'last_edited_time': {
                                            'type': ['string', 'null'],
                                            'description': 'Date and time when the database was last edited',
                                        },
                                        'created_by': {
                                            'type': ['object', 'null'],
                                            'description': 'User who created the database',
                                            'properties': {
                                                'object': {
                                                    'type': ['string', 'null'],
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'last_edited_by': {
                                            'type': ['object', 'null'],
                                            'description': 'User who last edited the database',
                                            'properties': {
                                                'object': {
                                                    'type': ['string', 'null'],
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'title': {
                                            'type': ['array', 'null'],
                                            'description': 'Title of the database as rich text',
                                            'items': {
                                                'type': 'object',
                                                'description': 'A rich text object',
                                                'properties': {
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Type of rich text (text, mention, equation)',
                                                    },
                                                    'text': {
                                                        'type': ['object', 'null'],
                                                        'description': 'Text content',
                                                        'properties': {
                                                            'content': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text content',
                                                            },
                                                            'link': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Link object',
                                                            },
                                                        },
                                                    },
                                                    'annotations': {
                                                        'type': ['object', 'null'],
                                                        'description': 'Text annotations (bold, italic, etc.)',
                                                        'properties': {
                                                            'bold': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'italic': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'strikethrough': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'underline': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'code': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'color': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'plain_text': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Plain text without annotations',
                                                    },
                                                    'href': {
                                                        'type': ['string', 'null'],
                                                        'description': 'URL if the text is a link',
                                                    },
                                                },
                                            },
                                        },
                                        'description': {
                                            'type': ['array', 'null'],
                                            'description': 'Description of the database as rich text',
                                            'items': {
                                                'type': 'object',
                                                'description': 'A rich text object',
                                                'properties': {
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Type of rich text (text, mention, equation)',
                                                    },
                                                    'text': {
                                                        'type': ['object', 'null'],
                                                        'description': 'Text content',
                                                        'properties': {
                                                            'content': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text content',
                                                            },
                                                            'link': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Link object',
                                                            },
                                                        },
                                                    },
                                                    'annotations': {
                                                        'type': ['object', 'null'],
                                                        'description': 'Text annotations (bold, italic, etc.)',
                                                        'properties': {
                                                            'bold': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'italic': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'strikethrough': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'underline': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'code': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'color': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'plain_text': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Plain text without annotations',
                                                    },
                                                    'href': {
                                                        'type': ['string', 'null'],
                                                        'description': 'URL if the text is a link',
                                                    },
                                                },
                                            },
                                        },
                                        'icon': {
                                            'type': ['object', 'null'],
                                            'description': 'Database icon',
                                        },
                                        'cover': {
                                            'type': ['object', 'null'],
                                            'description': 'Database cover image',
                                        },
                                        'properties': {
                                            'type': ['object', 'null'],
                                            'description': 'Schema of properties for the database',
                                            'additionalProperties': True,
                                        },
                                        'parent': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Parent object reference',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of parent (database_id, page_id, block_id, workspace)',
                                                        },
                                                        'database_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Database parent ID',
                                                        },
                                                        'page_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Page parent ID',
                                                        },
                                                        'block_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Block parent ID',
                                                        },
                                                        'workspace': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether parent is workspace',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Parent of the database',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL of the database',
                                        },
                                        'public_url': {
                                            'type': ['string', 'null'],
                                            'description': 'Public URL if published',
                                        },
                                        'archived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the database is archived',
                                        },
                                        'in_trash': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the database is in trash',
                                        },
                                        'is_inline': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the database is inline',
                                        },
                                        'is_locked': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the database is locked',
                                        },
                                        'request_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Request ID for debugging',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'databases',
                                    'x-airbyte-stream-name': 'databases',
                                },
                            },
                            'next_cursor': {
                                'type': ['string', 'null'],
                                'description': 'Cursor for next page',
                            },
                            'has_more': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether more results exist',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of results',
                            },
                            'page_or_database': {
                                'type': ['object', 'null'],
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.next_cursor', 'has_more': '$.has_more'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/databases/{database_id}',
                    action=Action.GET,
                    description='Retrieves a database object using the ID specified',
                    path_params=['database_id'],
                    path_params_schema={
                        'database_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2022-06-28',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Notion database object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique identifier for the database'},
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always database',
                            },
                            'created_time': {
                                'type': ['string', 'null'],
                                'description': 'Date and time when the database was created',
                            },
                            'last_edited_time': {
                                'type': ['string', 'null'],
                                'description': 'Date and time when the database was last edited',
                            },
                            'created_by': {
                                'type': ['object', 'null'],
                                'description': 'User who created the database',
                                'properties': {
                                    'object': {
                                        'type': ['string', 'null'],
                                    },
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'last_edited_by': {
                                'type': ['object', 'null'],
                                'description': 'User who last edited the database',
                                'properties': {
                                    'object': {
                                        'type': ['string', 'null'],
                                    },
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'title': {
                                'type': ['array', 'null'],
                                'description': 'Title of the database as rich text',
                                'items': {
                                    'type': 'object',
                                    'description': 'A rich text object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of rich text (text, mention, equation)',
                                        },
                                        'text': {
                                            'type': ['object', 'null'],
                                            'description': 'Text content',
                                            'properties': {
                                                'content': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text content',
                                                },
                                                'link': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Link object',
                                                },
                                            },
                                        },
                                        'annotations': {
                                            'type': ['object', 'null'],
                                            'description': 'Text annotations (bold, italic, etc.)',
                                            'properties': {
                                                'bold': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'italic': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'strikethrough': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'underline': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'code': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'plain_text': {
                                            'type': ['string', 'null'],
                                            'description': 'Plain text without annotations',
                                        },
                                        'href': {
                                            'type': ['string', 'null'],
                                            'description': 'URL if the text is a link',
                                        },
                                    },
                                },
                            },
                            'description': {
                                'type': ['array', 'null'],
                                'description': 'Description of the database as rich text',
                                'items': {
                                    'type': 'object',
                                    'description': 'A rich text object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of rich text (text, mention, equation)',
                                        },
                                        'text': {
                                            'type': ['object', 'null'],
                                            'description': 'Text content',
                                            'properties': {
                                                'content': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text content',
                                                },
                                                'link': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Link object',
                                                },
                                            },
                                        },
                                        'annotations': {
                                            'type': ['object', 'null'],
                                            'description': 'Text annotations (bold, italic, etc.)',
                                            'properties': {
                                                'bold': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'italic': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'strikethrough': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'underline': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'code': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'plain_text': {
                                            'type': ['string', 'null'],
                                            'description': 'Plain text without annotations',
                                        },
                                        'href': {
                                            'type': ['string', 'null'],
                                            'description': 'URL if the text is a link',
                                        },
                                    },
                                },
                            },
                            'icon': {
                                'type': ['object', 'null'],
                                'description': 'Database icon',
                            },
                            'cover': {
                                'type': ['object', 'null'],
                                'description': 'Database cover image',
                            },
                            'properties': {
                                'type': ['object', 'null'],
                                'description': 'Schema of properties for the database',
                                'additionalProperties': True,
                            },
                            'parent': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Parent object reference',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of parent (database_id, page_id, block_id, workspace)',
                                            },
                                            'database_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Database parent ID',
                                            },
                                            'page_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Page parent ID',
                                            },
                                            'block_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Block parent ID',
                                            },
                                            'workspace': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether parent is workspace',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Parent of the database',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL of the database',
                            },
                            'public_url': {
                                'type': ['string', 'null'],
                                'description': 'Public URL if published',
                            },
                            'archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the database is archived',
                            },
                            'in_trash': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the database is in trash',
                            },
                            'is_inline': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the database is inline',
                            },
                            'is_locked': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the database is locked',
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'databases',
                        'x-airbyte-stream-name': 'databases',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Notion database object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the database'},
                    'object': {
                        'type': ['string', 'null'],
                        'description': 'Always database',
                    },
                    'created_time': {
                        'type': ['string', 'null'],
                        'description': 'Date and time when the database was created',
                    },
                    'last_edited_time': {
                        'type': ['string', 'null'],
                        'description': 'Date and time when the database was last edited',
                    },
                    'created_by': {
                        'type': ['object', 'null'],
                        'description': 'User who created the database',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                            },
                            'id': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'last_edited_by': {
                        'type': ['object', 'null'],
                        'description': 'User who last edited the database',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                            },
                            'id': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'title': {
                        'type': ['array', 'null'],
                        'description': 'Title of the database as rich text',
                        'items': {'$ref': '#/components/schemas/RichText'},
                    },
                    'description': {
                        'type': ['array', 'null'],
                        'description': 'Description of the database as rich text',
                        'items': {'$ref': '#/components/schemas/RichText'},
                    },
                    'icon': {
                        'type': ['object', 'null'],
                        'description': 'Database icon',
                    },
                    'cover': {
                        'type': ['object', 'null'],
                        'description': 'Database cover image',
                    },
                    'properties': {
                        'type': ['object', 'null'],
                        'description': 'Schema of properties for the database',
                        'additionalProperties': True,
                    },
                    'parent': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Parent'},
                            {'type': 'null'},
                        ],
                        'description': 'Parent of the database',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'URL of the database',
                    },
                    'public_url': {
                        'type': ['string', 'null'],
                        'description': 'Public URL if published',
                    },
                    'archived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the database is archived',
                    },
                    'in_trash': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the database is in trash',
                    },
                    'is_inline': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the database is inline',
                    },
                    'is_locked': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the database is locked',
                    },
                    'request_id': {
                        'type': ['string', 'null'],
                        'description': 'Request ID for debugging',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'databases',
                'x-airbyte-stream-name': 'databases',
            },
        ),
        EntityDefinition(
            name='blocks',
            stream_name='blocks',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/blocks/{block_id}/children',
                    action=Action.LIST,
                    description='Returns a paginated list of child blocks for the specified block',
                    query_params=['start_cursor', 'page_size'],
                    query_params_schema={
                        'start_cursor': {'type': 'string', 'required': False},
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                    },
                    path_params=['block_id'],
                    path_params_schema={
                        'block_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2022-06-28',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of blocks',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always list',
                            },
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Notion block object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the block'},
                                        'object': {
                                            'type': ['string', 'null'],
                                            'description': 'Always block',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of block (paragraph, heading_1, to_do, etc.)',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'description': 'Date and time when the block was created',
                                        },
                                        'last_edited_time': {
                                            'type': ['string', 'null'],
                                            'description': 'Date and time when the block was last edited',
                                        },
                                        'created_by': {
                                            'type': ['object', 'null'],
                                            'description': 'User who created the block',
                                            'properties': {
                                                'object': {
                                                    'type': ['string', 'null'],
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'last_edited_by': {
                                            'type': ['object', 'null'],
                                            'description': 'User who last edited the block',
                                            'properties': {
                                                'object': {
                                                    'type': ['string', 'null'],
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'has_children': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the block has child blocks',
                                        },
                                        'archived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the block is archived',
                                        },
                                        'in_trash': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the block is in trash',
                                        },
                                        'parent': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Parent object reference',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of parent (database_id, page_id, block_id, workspace)',
                                                        },
                                                        'database_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Database parent ID',
                                                        },
                                                        'page_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Page parent ID',
                                                        },
                                                        'block_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Block parent ID',
                                                        },
                                                        'workspace': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether parent is workspace',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Parent of the block',
                                        },
                                        'paragraph': {
                                            'type': ['object', 'null'],
                                            'description': 'Paragraph block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'heading_1': {
                                            'type': ['object', 'null'],
                                            'description': 'Heading 1 block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                                'is_toggleable': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                        'heading_2': {
                                            'type': ['object', 'null'],
                                            'description': 'Heading 2 block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                                'is_toggleable': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                        'heading_3': {
                                            'type': ['object', 'null'],
                                            'description': 'Heading 3 block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                                'is_toggleable': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                        'bulleted_list_item': {
                                            'type': ['object', 'null'],
                                            'description': 'Bulleted list item content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'numbered_list_item': {
                                            'type': ['object', 'null'],
                                            'description': 'Numbered list item content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'to_do': {
                                            'type': ['object', 'null'],
                                            'description': 'To-do block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'checked': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'toggle': {
                                            'type': ['object', 'null'],
                                            'description': 'Toggle block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'code': {
                                            'type': ['object', 'null'],
                                            'description': 'Code block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'caption': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'language': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'child_page': {
                                            'type': ['object', 'null'],
                                            'description': 'Child page block',
                                            'properties': {
                                                'title': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'child_database': {
                                            'type': ['object', 'null'],
                                            'description': 'Child database block',
                                            'properties': {
                                                'title': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'callout': {
                                            'type': ['object', 'null'],
                                            'description': 'Callout block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'icon': {
                                                    'type': ['object', 'null'],
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'quote': {
                                            'type': ['object', 'null'],
                                            'description': 'Quote block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'divider': {
                                            'type': ['object', 'null'],
                                            'description': 'Divider block',
                                        },
                                        'table_of_contents': {
                                            'type': ['object', 'null'],
                                            'description': 'Table of contents block',
                                            'properties': {
                                                'color': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'bookmark': {
                                            'type': ['object', 'null'],
                                            'description': 'Bookmark block',
                                            'properties': {
                                                'caption': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'A rich text object',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of rich text (text, mention, equation)',
                                                            },
                                                            'text': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text content',
                                                                'properties': {
                                                                    'content': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Plain text content',
                                                                    },
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'description': 'Link object',
                                                                    },
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Text annotations (bold, italic, etc.)',
                                                                'properties': {
                                                                    'bold': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'italic': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'strikethrough': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'underline': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'code': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'color': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'plain_text': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text without annotations',
                                                            },
                                                            'href': {
                                                                'type': ['string', 'null'],
                                                                'description': 'URL if the text is a link',
                                                            },
                                                        },
                                                    },
                                                },
                                                'url': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'image': {
                                            'type': ['object', 'null'],
                                            'description': 'Image block',
                                        },
                                        'video': {
                                            'type': ['object', 'null'],
                                            'description': 'Video block',
                                        },
                                        'file': {
                                            'type': ['object', 'null'],
                                            'description': 'File block',
                                        },
                                        'pdf': {
                                            'type': ['object', 'null'],
                                            'description': 'PDF block',
                                        },
                                        'embed': {
                                            'type': ['object', 'null'],
                                            'description': 'Embed block',
                                            'properties': {
                                                'url': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'equation': {
                                            'type': ['object', 'null'],
                                            'description': 'Equation block',
                                            'properties': {
                                                'expression': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'table': {
                                            'type': ['object', 'null'],
                                            'description': 'Table block',
                                            'properties': {
                                                'table_width': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'has_column_header': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'has_row_header': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                        'table_row': {
                                            'type': ['object', 'null'],
                                            'description': 'Table row block',
                                            'properties': {
                                                'cells': {
                                                    'type': ['array', 'null'],
                                                },
                                            },
                                        },
                                        'request_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Request ID for debugging',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'blocks',
                                    'x-airbyte-stream-name': 'blocks',
                                },
                            },
                            'next_cursor': {
                                'type': ['string', 'null'],
                                'description': 'Cursor for next page',
                            },
                            'has_more': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether more results exist',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of results',
                            },
                            'block': {
                                'type': ['object', 'null'],
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.next_cursor', 'has_more': '$.has_more'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/blocks/{block_id}',
                    action=Action.GET,
                    description='Retrieves a block object using the ID specified',
                    path_params=['block_id'],
                    path_params_schema={
                        'block_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2022-06-28',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Notion block object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique identifier for the block'},
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always block',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of block (paragraph, heading_1, to_do, etc.)',
                            },
                            'created_time': {
                                'type': ['string', 'null'],
                                'description': 'Date and time when the block was created',
                            },
                            'last_edited_time': {
                                'type': ['string', 'null'],
                                'description': 'Date and time when the block was last edited',
                            },
                            'created_by': {
                                'type': ['object', 'null'],
                                'description': 'User who created the block',
                                'properties': {
                                    'object': {
                                        'type': ['string', 'null'],
                                    },
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'last_edited_by': {
                                'type': ['object', 'null'],
                                'description': 'User who last edited the block',
                                'properties': {
                                    'object': {
                                        'type': ['string', 'null'],
                                    },
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'has_children': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the block has child blocks',
                            },
                            'archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the block is archived',
                            },
                            'in_trash': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the block is in trash',
                            },
                            'parent': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Parent object reference',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of parent (database_id, page_id, block_id, workspace)',
                                            },
                                            'database_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Database parent ID',
                                            },
                                            'page_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Page parent ID',
                                            },
                                            'block_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Block parent ID',
                                            },
                                            'workspace': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether parent is workspace',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Parent of the block',
                            },
                            'paragraph': {
                                'type': ['object', 'null'],
                                'description': 'Paragraph block content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'heading_1': {
                                'type': ['object', 'null'],
                                'description': 'Heading 1 block content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                    'is_toggleable': {
                                        'type': ['boolean', 'null'],
                                    },
                                },
                            },
                            'heading_2': {
                                'type': ['object', 'null'],
                                'description': 'Heading 2 block content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                    'is_toggleable': {
                                        'type': ['boolean', 'null'],
                                    },
                                },
                            },
                            'heading_3': {
                                'type': ['object', 'null'],
                                'description': 'Heading 3 block content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                    'is_toggleable': {
                                        'type': ['boolean', 'null'],
                                    },
                                },
                            },
                            'bulleted_list_item': {
                                'type': ['object', 'null'],
                                'description': 'Bulleted list item content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'numbered_list_item': {
                                'type': ['object', 'null'],
                                'description': 'Numbered list item content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'to_do': {
                                'type': ['object', 'null'],
                                'description': 'To-do block content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'checked': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'toggle': {
                                'type': ['object', 'null'],
                                'description': 'Toggle block content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'code': {
                                'type': ['object', 'null'],
                                'description': 'Code block content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'caption': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'language': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'child_page': {
                                'type': ['object', 'null'],
                                'description': 'Child page block',
                                'properties': {
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'child_database': {
                                'type': ['object', 'null'],
                                'description': 'Child database block',
                                'properties': {
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'callout': {
                                'type': ['object', 'null'],
                                'description': 'Callout block content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'icon': {
                                        'type': ['object', 'null'],
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'quote': {
                                'type': ['object', 'null'],
                                'description': 'Quote block content',
                                'properties': {
                                    'rich_text': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'divider': {
                                'type': ['object', 'null'],
                                'description': 'Divider block',
                            },
                            'table_of_contents': {
                                'type': ['object', 'null'],
                                'description': 'Table of contents block',
                                'properties': {
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'bookmark': {
                                'type': ['object', 'null'],
                                'description': 'Bookmark block',
                                'properties': {
                                    'caption': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A rich text object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of rich text (text, mention, equation)',
                                                },
                                                'text': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text content',
                                                    'properties': {
                                                        'content': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plain text content',
                                                        },
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Link object',
                                                        },
                                                    },
                                                },
                                                'annotations': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Text annotations (bold, italic, etc.)',
                                                    'properties': {
                                                        'bold': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'italic': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'strikethrough': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'underline': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'code': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                'plain_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text without annotations',
                                                },
                                                'href': {
                                                    'type': ['string', 'null'],
                                                    'description': 'URL if the text is a link',
                                                },
                                            },
                                        },
                                    },
                                    'url': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'image': {
                                'type': ['object', 'null'],
                                'description': 'Image block',
                            },
                            'video': {
                                'type': ['object', 'null'],
                                'description': 'Video block',
                            },
                            'file': {
                                'type': ['object', 'null'],
                                'description': 'File block',
                            },
                            'pdf': {
                                'type': ['object', 'null'],
                                'description': 'PDF block',
                            },
                            'embed': {
                                'type': ['object', 'null'],
                                'description': 'Embed block',
                                'properties': {
                                    'url': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'equation': {
                                'type': ['object', 'null'],
                                'description': 'Equation block',
                                'properties': {
                                    'expression': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'table': {
                                'type': ['object', 'null'],
                                'description': 'Table block',
                                'properties': {
                                    'table_width': {
                                        'type': ['integer', 'null'],
                                    },
                                    'has_column_header': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'has_row_header': {
                                        'type': ['boolean', 'null'],
                                    },
                                },
                            },
                            'table_row': {
                                'type': ['object', 'null'],
                                'description': 'Table row block',
                                'properties': {
                                    'cells': {
                                        'type': ['array', 'null'],
                                    },
                                },
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'blocks',
                        'x-airbyte-stream-name': 'blocks',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Notion block object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the block'},
                    'object': {
                        'type': ['string', 'null'],
                        'description': 'Always block',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Type of block (paragraph, heading_1, to_do, etc.)',
                    },
                    'created_time': {
                        'type': ['string', 'null'],
                        'description': 'Date and time when the block was created',
                    },
                    'last_edited_time': {
                        'type': ['string', 'null'],
                        'description': 'Date and time when the block was last edited',
                    },
                    'created_by': {
                        'type': ['object', 'null'],
                        'description': 'User who created the block',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                            },
                            'id': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'last_edited_by': {
                        'type': ['object', 'null'],
                        'description': 'User who last edited the block',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                            },
                            'id': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'has_children': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the block has child blocks',
                    },
                    'archived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the block is archived',
                    },
                    'in_trash': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the block is in trash',
                    },
                    'parent': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Parent'},
                            {'type': 'null'},
                        ],
                        'description': 'Parent of the block',
                    },
                    'paragraph': {
                        'type': ['object', 'null'],
                        'description': 'Paragraph block content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'color': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'heading_1': {
                        'type': ['object', 'null'],
                        'description': 'Heading 1 block content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'color': {
                                'type': ['string', 'null'],
                            },
                            'is_toggleable': {
                                'type': ['boolean', 'null'],
                            },
                        },
                    },
                    'heading_2': {
                        'type': ['object', 'null'],
                        'description': 'Heading 2 block content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'color': {
                                'type': ['string', 'null'],
                            },
                            'is_toggleable': {
                                'type': ['boolean', 'null'],
                            },
                        },
                    },
                    'heading_3': {
                        'type': ['object', 'null'],
                        'description': 'Heading 3 block content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'color': {
                                'type': ['string', 'null'],
                            },
                            'is_toggleable': {
                                'type': ['boolean', 'null'],
                            },
                        },
                    },
                    'bulleted_list_item': {
                        'type': ['object', 'null'],
                        'description': 'Bulleted list item content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'color': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'numbered_list_item': {
                        'type': ['object', 'null'],
                        'description': 'Numbered list item content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'color': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'to_do': {
                        'type': ['object', 'null'],
                        'description': 'To-do block content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'checked': {
                                'type': ['boolean', 'null'],
                            },
                            'color': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'toggle': {
                        'type': ['object', 'null'],
                        'description': 'Toggle block content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'color': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'code': {
                        'type': ['object', 'null'],
                        'description': 'Code block content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'caption': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'language': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'child_page': {
                        'type': ['object', 'null'],
                        'description': 'Child page block',
                        'properties': {
                            'title': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'child_database': {
                        'type': ['object', 'null'],
                        'description': 'Child database block',
                        'properties': {
                            'title': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'callout': {
                        'type': ['object', 'null'],
                        'description': 'Callout block content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'icon': {
                                'type': ['object', 'null'],
                            },
                            'color': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'quote': {
                        'type': ['object', 'null'],
                        'description': 'Quote block content',
                        'properties': {
                            'rich_text': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'color': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'divider': {
                        'type': ['object', 'null'],
                        'description': 'Divider block',
                    },
                    'table_of_contents': {
                        'type': ['object', 'null'],
                        'description': 'Table of contents block',
                        'properties': {
                            'color': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'bookmark': {
                        'type': ['object', 'null'],
                        'description': 'Bookmark block',
                        'properties': {
                            'caption': {
                                'type': ['array', 'null'],
                                'items': {'$ref': '#/components/schemas/RichText'},
                            },
                            'url': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'image': {
                        'type': ['object', 'null'],
                        'description': 'Image block',
                    },
                    'video': {
                        'type': ['object', 'null'],
                        'description': 'Video block',
                    },
                    'file': {
                        'type': ['object', 'null'],
                        'description': 'File block',
                    },
                    'pdf': {
                        'type': ['object', 'null'],
                        'description': 'PDF block',
                    },
                    'embed': {
                        'type': ['object', 'null'],
                        'description': 'Embed block',
                        'properties': {
                            'url': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'equation': {
                        'type': ['object', 'null'],
                        'description': 'Equation block',
                        'properties': {
                            'expression': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'table': {
                        'type': ['object', 'null'],
                        'description': 'Table block',
                        'properties': {
                            'table_width': {
                                'type': ['integer', 'null'],
                            },
                            'has_column_header': {
                                'type': ['boolean', 'null'],
                            },
                            'has_row_header': {
                                'type': ['boolean', 'null'],
                            },
                        },
                    },
                    'table_row': {
                        'type': ['object', 'null'],
                        'description': 'Table row block',
                        'properties': {
                            'cells': {
                                'type': ['array', 'null'],
                            },
                        },
                    },
                    'request_id': {
                        'type': ['string', 'null'],
                        'description': 'Request ID for debugging',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'blocks',
                'x-airbyte-stream-name': 'blocks',
            },
        ),
        EntityDefinition(
            name='comments',
            stream_name='comments',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/comments',
                    action=Action.LIST,
                    description='Returns a list of comments for a specified block or page',
                    query_params=['block_id', 'start_cursor', 'page_size'],
                    query_params_schema={
                        'block_id': {'type': 'string', 'required': True},
                        'start_cursor': {'type': 'string', 'required': False},
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2022-06-28',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of comments',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always list',
                            },
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Notion comment object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the comment'},
                                        'object': {
                                            'type': ['string', 'null'],
                                            'description': 'Always comment',
                                        },
                                        'parent': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Parent object reference',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of parent (database_id, page_id, block_id, workspace)',
                                                        },
                                                        'database_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Database parent ID',
                                                        },
                                                        'page_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Page parent ID',
                                                        },
                                                        'block_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Block parent ID',
                                                        },
                                                        'workspace': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether parent is workspace',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Parent of the comment',
                                        },
                                        'discussion_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Discussion thread ID',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'description': 'Date and time when the comment was created',
                                        },
                                        'last_edited_time': {
                                            'type': ['string', 'null'],
                                            'description': 'Date and time when the comment was last edited',
                                        },
                                        'created_by': {
                                            'type': ['object', 'null'],
                                            'description': 'User who created the comment',
                                            'properties': {
                                                'object': {
                                                    'type': ['string', 'null'],
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'rich_text': {
                                            'type': ['array', 'null'],
                                            'description': 'Content of the comment as rich text',
                                            'items': {
                                                'type': 'object',
                                                'description': 'A rich text object',
                                                'properties': {
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Type of rich text (text, mention, equation)',
                                                    },
                                                    'text': {
                                                        'type': ['object', 'null'],
                                                        'description': 'Text content',
                                                        'properties': {
                                                            'content': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Plain text content',
                                                            },
                                                            'link': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Link object',
                                                            },
                                                        },
                                                    },
                                                    'annotations': {
                                                        'type': ['object', 'null'],
                                                        'description': 'Text annotations (bold, italic, etc.)',
                                                        'properties': {
                                                            'bold': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'italic': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'strikethrough': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'underline': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'code': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'color': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'plain_text': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Plain text without annotations',
                                                    },
                                                    'href': {
                                                        'type': ['string', 'null'],
                                                        'description': 'URL if the text is a link',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'comments',
                                    'x-airbyte-stream-name': 'comments',
                                },
                            },
                            'next_cursor': {
                                'type': ['string', 'null'],
                                'description': 'Cursor for next page',
                            },
                            'has_more': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether more results exist',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of results',
                            },
                            'comment': {
                                'type': ['object', 'null'],
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.next_cursor', 'has_more': '$.has_more'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Notion comment object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the comment'},
                    'object': {
                        'type': ['string', 'null'],
                        'description': 'Always comment',
                    },
                    'parent': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Parent'},
                            {'type': 'null'},
                        ],
                        'description': 'Parent of the comment',
                    },
                    'discussion_id': {
                        'type': ['string', 'null'],
                        'description': 'Discussion thread ID',
                    },
                    'created_time': {
                        'type': ['string', 'null'],
                        'description': 'Date and time when the comment was created',
                    },
                    'last_edited_time': {
                        'type': ['string', 'null'],
                        'description': 'Date and time when the comment was last edited',
                    },
                    'created_by': {
                        'type': ['object', 'null'],
                        'description': 'User who created the comment',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                            },
                            'id': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'rich_text': {
                        'type': ['array', 'null'],
                        'description': 'Content of the comment as rich text',
                        'items': {'$ref': '#/components/schemas/RichText'},
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'comments',
                'x-airbyte-stream-name': 'comments',
            },
        ),
    ],
    search_field_paths={
        'pages': [
            'archived',
            'cover',
            'created_by',
            'created_time',
            'icon',
            'id',
            'in_trash',
            'last_edited_by',
            'last_edited_time',
            'object',
            'parent',
            'properties',
            'properties[]',
            'public_url',
            'url',
        ],
        'users': [
            'avatar_url',
            'bot',
            'id',
            'name',
            'object',
            'person',
            'type',
        ],
        'databases': [
            'archived',
            'cover',
            'created_by',
            'created_time',
            'description',
            'description[]',
            'icon',
            'id',
            'is_inline',
            'last_edited_by',
            'last_edited_time',
            'object',
            'parent',
            'properties',
            'properties[]',
            'public_url',
            'title',
            'title[]',
            'url',
        ],
        'blocks': [
            'archived',
            'bookmark',
            'breadcrumb',
            'bulleted_list_item',
            'callout',
            'child_database',
            'child_page',
            'code',
            'column',
            'column_list',
            'created_by',
            'created_time',
            'divider',
            'embed',
            'equation',
            'file',
            'has_children',
            'heading_1',
            'heading_2',
            'heading_3',
            'id',
            'image',
            'last_edited_by',
            'last_edited_time',
            'link_preview',
            'link_to_page',
            'numbered_list_item',
            'object',
            'paragraph',
            'parent',
            'pdf',
            'quote',
            'synced_block',
            'table',
            'table_of_contents',
            'table_row',
            'template',
            'to_do',
            'toggle',
            'type',
            'unsupported',
            'video',
        ],
    },
)