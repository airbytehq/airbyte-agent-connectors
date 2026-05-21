"""
Connector model for notion.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""

from __future__ import annotations

from airbyte_agent_sdk.types import (
    Action,
    AuthConfig,
    AuthOption,
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
    CacheConfig,
    CacheEntityConfig,
    CacheFieldConfig,
    EntityRelationshipConfig,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from airbyte_agent_sdk.schema.components import (
    PathOverrideConfig,
)
from uuid import (
    UUID,
)

NotionConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('6e00b415-b02e-4160-bf02-58176a0ae687'),
    name='notion',
    version='0.1.12',
    base_url='https://api.notion.com',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='notionOAuth',
                type=AuthType.OAUTH2,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'refresh_url': 'https://api.notion.com/v1/oauth/token',
                    'auth_style': 'basic',
                    'body_format': 'json',
                },
                user_config_spec=AuthConfigSpec(
                    title='OAuth2.0',
                    type='object',
                    required=['access_token', 'client_id', 'client_secret'],
                    properties={
                        'client_id': AuthConfigFieldSpec(
                            title='Client ID',
                            description="Your Notion OAuth integration's client ID",
                        ),
                        'client_secret': AuthConfigFieldSpec(
                            title='Client Secret',
                            description="Your Notion OAuth integration's client secret",
                        ),
                        'access_token': AuthConfigFieldSpec(
                            title='Access Token',
                            description='OAuth access token obtained through the Notion authorization flow',
                        ),
                    },
                    auth_mapping={
                        'client_id': '${client_id}',
                        'client_secret': '${client_secret}',
                        'access_token': '${access_token}',
                    },
                    replication_auth_key_mapping={
                        'credentials.client_id': 'client_id',
                        'credentials.client_secret': 'client_secret',
                        'credentials.access_token': 'access_token',
                    },
                    replication_auth_key_constants={'credentials.auth_type': 'OAuth2.0'},
                ),
            ),
            AuthOption(
                scheme_name='notionBearerToken',
                type=AuthType.BEARER,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AuthConfigSpec(
                    title='Access Token',
                    type='object',
                    required=['token'],
                    properties={
                        'token': AuthConfigFieldSpec(
                            title='Integration Token',
                            description='Notion internal integration token (starts with ntn_ or secret_)',
                        ),
                    },
                    auth_mapping={'token': '${token}'},
                    replication_auth_key_mapping={'credentials.token': 'token'},
                    replication_auth_key_constants={'credentials.auth_type': 'token'},
                ),
            ),
        ],
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
                            'minimum': 1,
                            'maximum': 100,
                        },
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2025-09-03',
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Notion workspace members and bot users',
                                        'when_to_use': 'Looking up team members or user details in Notion',
                                        'trigger_phrases': ['notion user', 'workspace member'],
                                        'freshness': 'live',
                                        'example_questions': ['Who are the Notion workspace members?'],
                                        'search_strategy': 'Search by name or email',
                                    },
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
                            'default': '2025-09-03',
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Notion workspace members and bot users',
                            'when_to_use': 'Looking up team members or user details in Notion',
                            'trigger_phrases': ['notion user', 'workspace member'],
                            'freshness': 'live',
                            'example_questions': ['Who are the Notion workspace members?'],
                            'search_strategy': 'Search by name or email',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Notion workspace members and bot users',
                    'when_to_use': 'Looking up team members or user details in Notion',
                    'trigger_phrases': ['notion user', 'workspace member'],
                    'freshness': 'live',
                    'example_questions': ['Who are the Notion workspace members?'],
                    'search_strategy': 'Search by name or email',
                },
            },
            ai_hints={
                'summary': 'Notion workspace members and bot users',
                'when_to_use': 'Looking up team members or user details in Notion',
                'trigger_phrases': ['notion user', 'workspace member'],
                'freshness': 'live',
                'example_questions': ['Who are the Notion workspace members?'],
                'search_strategy': 'Search by name or email',
            },
        ),
        EntityDefinition(
            name='pages',
            stream_name='pages',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
            ],
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
                            'default': '2025-09-03',
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
                                                        'data_source_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Data source parent ID',
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
                                        'is_archived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the page is archived (alias for archived)',
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Internal documentation, wiki pages, databases, and company knowledge',
                                        'when_to_use': 'Questions about internal docs, company policies, processes, or wiki content',
                                        'trigger_phrases': [
                                            'is there a doc for',
                                            'Notion page about',
                                            'where is the doc',
                                            'company policy on',
                                            'internal wiki',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Is there a doc for the connector setup process?', 'Find the Notion page about onboarding', 'What does the internal wiki say about release process?'],
                                        'search_strategy': 'Pages have no title field — search the url field which contains the title slug. For multi-word queries, split into separate OR conditions on url.',
                                    },
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
                            'page_or_data_source': {
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
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/pages',
                    action=Action.CREATE,
                    description='Creates a new page as a child of an existing page or data source',
                    body_fields=[
                        'parent',
                        'properties',
                        'children',
                        'icon',
                        'cover',
                    ],
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2025-09-03',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new page as a child of an existing page, data source, or at the workspace level.',
                        'properties': {
                            'parent': {
                                'type': 'object',
                                'description': 'Parent of the page. Provide exactly one of page_id, database_id, data_source_id, or workspace.',
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'required': ['page_id'],
                                        'properties': {
                                            'page_id': {'type': 'string', 'description': 'ID of the parent page'},
                                        },
                                    },
                                    {
                                        'type': 'object',
                                        'required': ['database_id'],
                                        'properties': {
                                            'database_id': {'type': 'string', 'description': 'ID of the parent database'},
                                        },
                                    },
                                    {
                                        'type': 'object',
                                        'required': ['data_source_id'],
                                        'properties': {
                                            'data_source_id': {'type': 'string', 'description': 'ID of the parent data source'},
                                        },
                                    },
                                    {
                                        'type': 'object',
                                        'required': ['workspace'],
                                        'properties': {
                                            'workspace': {'type': 'boolean', 'description': 'Set to true to create at workspace level'},
                                        },
                                    },
                                ],
                            },
                            'properties': {
                                'type': 'object',
                                'description': 'Page properties. For pages under a page, use title property. For data source pages, match the data source schema.',
                                'additionalProperties': True,
                            },
                            'children': {
                                'type': 'array',
                                'description': 'Content blocks to add to the page (max 100)',
                                'items': {'type': 'object', 'additionalProperties': True},
                            },
                            'icon': {
                                'type': ['object', 'null'],
                                'description': 'Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'Icon type: emoji, external, file_upload, custom_emoji, or icon'},
                                    'emoji': {'type': 'string', 'description': 'Emoji character (when type is emoji)'},
                                    'external': {
                                        'type': 'object',
                                        'description': 'External URL icon (when type is external)',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'description': 'Uploaded file icon (when type is file_upload)',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                    'custom_emoji': {
                                        'type': 'object',
                                        'description': 'Custom emoji icon (when type is custom_emoji)',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                    'icon': {
                                        'type': 'object',
                                        'description': 'Notion native icon (when type is icon)',
                                        'properties': {
                                            'name': {'type': 'string'},
                                            'color': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'cover': {
                                'type': ['object', 'null'],
                                'description': 'Cover image. Supports external URL or file upload. Set to null to remove.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'Cover type: external or file_upload'},
                                    'external': {
                                        'type': 'object',
                                        'description': 'External URL cover',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'description': 'Uploaded file cover',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['parent'],
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
                                            'data_source_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Data source parent ID',
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
                            'is_archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the page is archived (alias for archived)',
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Internal documentation, wiki pages, databases, and company knowledge',
                            'when_to_use': 'Questions about internal docs, company policies, processes, or wiki content',
                            'trigger_phrases': [
                                'is there a doc for',
                                'Notion page about',
                                'where is the doc',
                                'company policy on',
                                'internal wiki',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Is there a doc for the connector setup process?', 'Find the Notion page about onboarding', 'What does the internal wiki say about release process?'],
                            'search_strategy': 'Pages have no title field — search the url field which contains the title slug. For multi-word queries, split into separate OR conditions on url.',
                        },
                    },
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
                            'default': '2025-09-03',
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
                                            'data_source_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Data source parent ID',
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
                            'is_archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the page is archived (alias for archived)',
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Internal documentation, wiki pages, databases, and company knowledge',
                            'when_to_use': 'Questions about internal docs, company policies, processes, or wiki content',
                            'trigger_phrases': [
                                'is there a doc for',
                                'Notion page about',
                                'where is the doc',
                                'company policy on',
                                'internal wiki',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Is there a doc for the connector setup process?', 'Find the Notion page about onboarding', 'What does the internal wiki say about release process?'],
                            'search_strategy': 'Pages have no title field — search the url field which contains the title slug. For multi-word queries, split into separate OR conditions on url.',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/v1/pages/{page_id}',
                    action=Action.UPDATE,
                    description='Updates page properties, icon, cover, or archived status',
                    body_fields=[
                        'properties',
                        'icon',
                        'cover',
                        'archived',
                        'in_trash',
                    ],
                    path_params=['page_id'],
                    path_params_schema={
                        'page_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2025-09-03',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating a page. All fields are optional for partial updates.',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': "Page property values to update. Keys must match the page's property schema.",
                                'additionalProperties': True,
                            },
                            'icon': {
                                'type': ['object', 'null'],
                                'description': 'Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'Icon type: emoji, external, file_upload, custom_emoji, or icon'},
                                    'emoji': {'type': 'string', 'description': 'Emoji character (when type is emoji)'},
                                    'external': {
                                        'type': 'object',
                                        'description': 'External URL icon (when type is external)',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'description': 'Uploaded file icon (when type is file_upload)',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                    'custom_emoji': {
                                        'type': 'object',
                                        'description': 'Custom emoji icon (when type is custom_emoji)',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                    'icon': {
                                        'type': 'object',
                                        'description': 'Notion native icon (when type is icon)',
                                        'properties': {
                                            'name': {'type': 'string'},
                                            'color': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'cover': {
                                'type': ['object', 'null'],
                                'description': 'Cover image. Supports external URL or file upload. Set to null to remove.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'Cover type: external or file_upload'},
                                    'external': {
                                        'type': 'object',
                                        'description': 'External URL cover',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'description': 'Uploaded file cover',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'archived': {'type': 'boolean', 'description': 'Set to true to archive the page, false to un-archive'},
                            'in_trash': {'type': 'boolean', 'description': 'Set to true to move the page to trash, false to restore'},
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
                                            'data_source_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Data source parent ID',
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
                            'is_archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the page is archived (alias for archived)',
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Internal documentation, wiki pages, databases, and company knowledge',
                            'when_to_use': 'Questions about internal docs, company policies, processes, or wiki content',
                            'trigger_phrases': [
                                'is there a doc for',
                                'Notion page about',
                                'where is the doc',
                                'company policy on',
                                'internal wiki',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Is there a doc for the connector setup process?', 'Find the Notion page about onboarding', 'What does the internal wiki say about release process?'],
                            'search_strategy': 'Pages have no title field — search the url field which contains the title slug. For multi-word queries, split into separate OR conditions on url.',
                        },
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
                    'is_archived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the page is archived (alias for archived)',
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
                'x-airbyte-ai-hints': {
                    'summary': 'Internal documentation, wiki pages, databases, and company knowledge',
                    'when_to_use': 'Questions about internal docs, company policies, processes, or wiki content',
                    'trigger_phrases': [
                        'is there a doc for',
                        'Notion page about',
                        'where is the doc',
                        'company policy on',
                        'internal wiki',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Is there a doc for the connector setup process?', 'Find the Notion page about onboarding', 'What does the internal wiki say about release process?'],
                    'search_strategy': 'Pages have no title field — search the url field which contains the title slug. For multi-word queries, split into separate OR conditions on url.',
                },
            },
            ai_hints={
                'summary': 'Internal documentation, wiki pages, databases, and company knowledge',
                'when_to_use': 'Questions about internal docs, company policies, processes, or wiki content',
                'trigger_phrases': [
                    'is there a doc for',
                    'Notion page about',
                    'where is the doc',
                    'company policy on',
                    'internal wiki',
                ],
                'freshness': 'live',
                'example_questions': ['Is there a doc for the connector setup process?', 'Find the Notion page about onboarding', 'What does the internal wiki say about release process?'],
                'search_strategy': 'Pages have no title field — search the url field which contains the title slug. For multi-word queries, split into separate OR conditions on url.',
            },
        ),
        EntityDefinition(
            name='data_sources',
            stream_name='data_sources',
            actions=[Action.LIST, Action.GET, Action.UPDATE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v1/search:data_sources',
                    path_override=PathOverrideConfig(
                        path='/v1/search',
                    ),
                    action=Action.LIST,
                    description='Returns data sources shared with the integration using the search endpoint',
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
                            'default': '2025-09-03',
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
                                    'value': {'type': 'string', 'default': 'data_source'},
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
                        'description': 'Paginated list of data sources',
                        'properties': {
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always list',
                            },
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Notion data source object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the data source'},
                                        'object': {
                                            'type': ['string', 'null'],
                                            'description': 'Always data_source',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'description': 'Date and time when the data source was created',
                                        },
                                        'last_edited_time': {
                                            'type': ['string', 'null'],
                                            'description': 'Date and time when the data source was last edited',
                                        },
                                        'created_by': {
                                            'type': ['object', 'null'],
                                            'description': 'User who created the data source',
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
                                            'description': 'User who last edited the data source',
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
                                            'description': 'Title of the data source as rich text',
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
                                            'description': 'Description of the data source as rich text',
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
                                            'description': 'Data source icon',
                                        },
                                        'cover': {
                                            'type': ['object', 'null'],
                                            'description': 'Data source cover image',
                                        },
                                        'properties': {
                                            'type': ['object', 'null'],
                                            'description': 'Schema of properties for the data source',
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
                                                        'data_source_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Data source parent ID',
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
                                            'description': 'Parent database of the data source',
                                        },
                                        'database_parent': {
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
                                                        'data_source_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Data source parent ID',
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
                                            'description': 'Grandparent of the data source (parent of the database)',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL of the data source',
                                        },
                                        'public_url': {
                                            'type': ['string', 'null'],
                                            'description': 'Public URL if published',
                                        },
                                        'archived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the data source is archived',
                                        },
                                        'in_trash': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the data source is in trash',
                                        },
                                        'is_archived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the data source is archived (alias for archived)',
                                        },
                                        'is_inline': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the data source is inline',
                                        },
                                        'is_locked': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the data source is locked',
                                        },
                                        'request_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Request ID for debugging',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'data_sources',
                                    'x-airbyte-stream-name': 'data_sources',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'External data sources connected to Notion',
                                        'when_to_use': 'Questions about connected data sources or integrations',
                                        'trigger_phrases': ['data source', 'connected source', 'notion integration'],
                                        'freshness': 'static',
                                        'example_questions': ['What data sources are connected to Notion?'],
                                        'search_strategy': 'List all data sources',
                                    },
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
                            'page_or_data_source': {
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
                    path='/v1/data_sources/{data_source_id}',
                    action=Action.GET,
                    description='Retrieves a data source object using the ID specified',
                    path_params=['data_source_id'],
                    path_params_schema={
                        'data_source_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2025-09-03',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Notion data source object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique identifier for the data source'},
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always data_source',
                            },
                            'created_time': {
                                'type': ['string', 'null'],
                                'description': 'Date and time when the data source was created',
                            },
                            'last_edited_time': {
                                'type': ['string', 'null'],
                                'description': 'Date and time when the data source was last edited',
                            },
                            'created_by': {
                                'type': ['object', 'null'],
                                'description': 'User who created the data source',
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
                                'description': 'User who last edited the data source',
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
                                'description': 'Title of the data source as rich text',
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
                                'description': 'Description of the data source as rich text',
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
                                'description': 'Data source icon',
                            },
                            'cover': {
                                'type': ['object', 'null'],
                                'description': 'Data source cover image',
                            },
                            'properties': {
                                'type': ['object', 'null'],
                                'description': 'Schema of properties for the data source',
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
                                            'data_source_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Data source parent ID',
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
                                'description': 'Parent database of the data source',
                            },
                            'database_parent': {
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
                                            'data_source_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Data source parent ID',
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
                                'description': 'Grandparent of the data source (parent of the database)',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL of the data source',
                            },
                            'public_url': {
                                'type': ['string', 'null'],
                                'description': 'Public URL if published',
                            },
                            'archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the data source is archived',
                            },
                            'in_trash': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the data source is in trash',
                            },
                            'is_archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the data source is archived (alias for archived)',
                            },
                            'is_inline': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the data source is inline',
                            },
                            'is_locked': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the data source is locked',
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'data_sources',
                        'x-airbyte-stream-name': 'data_sources',
                        'x-airbyte-ai-hints': {
                            'summary': 'External data sources connected to Notion',
                            'when_to_use': 'Questions about connected data sources or integrations',
                            'trigger_phrases': ['data source', 'connected source', 'notion integration'],
                            'freshness': 'static',
                            'example_questions': ['What data sources are connected to Notion?'],
                            'search_strategy': 'List all data sources',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/v1/data_sources/{data_source_id}:update',
                    path_override=PathOverrideConfig(
                        path='/v1/data_sources/{data_source_id}',
                    ),
                    action=Action.UPDATE,
                    description="Updates a data source's title, description, icon, properties, or trash status",
                    body_fields=[
                        'title',
                        'description',
                        'properties',
                        'icon',
                        'cover',
                        'archived',
                        'in_trash',
                    ],
                    path_params=['data_source_id'],
                    path_params_schema={
                        'data_source_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2025-09-03',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating a data source. All fields are optional.',
                        'properties': {
                            'title': {
                                'type': 'array',
                                'description': 'Updated title of the data source as rich text',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'type': {'type': 'string', 'default': 'text'},
                                        'text': {
                                            'type': 'object',
                                            'properties': {
                                                'content': {'type': 'string'},
                                                'link': {
                                                    'type': ['object', 'null'],
                                                    'properties': {
                                                        'url': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                        'mention': {'type': 'object', 'additionalProperties': True},
                                        'equation': {
                                            'type': 'object',
                                            'properties': {
                                                'expression': {'type': 'string'},
                                            },
                                        },
                                        'annotations': {
                                            'type': 'object',
                                            'properties': {
                                                'bold': {'type': 'boolean'},
                                                'italic': {'type': 'boolean'},
                                                'strikethrough': {'type': 'boolean'},
                                                'underline': {'type': 'boolean'},
                                                'code': {'type': 'boolean'},
                                                'color': {'type': 'string'},
                                            },
                                        },
                                    },
                                },
                            },
                            'description': {
                                'type': 'array',
                                'description': 'Updated description of the data source as rich text',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'type': {'type': 'string', 'default': 'text'},
                                        'text': {
                                            'type': 'object',
                                            'properties': {
                                                'content': {'type': 'string'},
                                                'link': {
                                                    'type': ['object', 'null'],
                                                    'properties': {
                                                        'url': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                        'mention': {'type': 'object', 'additionalProperties': True},
                                        'equation': {
                                            'type': 'object',
                                            'properties': {
                                                'expression': {'type': 'string'},
                                            },
                                        },
                                        'annotations': {
                                            'type': 'object',
                                            'properties': {
                                                'bold': {'type': 'boolean'},
                                                'italic': {'type': 'boolean'},
                                                'strikethrough': {'type': 'boolean'},
                                                'underline': {'type': 'boolean'},
                                                'code': {'type': 'boolean'},
                                                'color': {'type': 'string'},
                                            },
                                        },
                                    },
                                },
                            },
                            'properties': {
                                'type': 'object',
                                'description': 'Data source property schema to update. Keys are property names or IDs. Set a property to null to remove it.',
                                'additionalProperties': True,
                            },
                            'icon': {
                                'type': ['object', 'null'],
                                'description': 'Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'Icon type: emoji, external, file_upload, custom_emoji, or icon'},
                                    'emoji': {'type': 'string', 'description': 'Emoji character (when type is emoji)'},
                                    'external': {
                                        'type': 'object',
                                        'description': 'External URL icon (when type is external)',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'description': 'Uploaded file icon (when type is file_upload)',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                    'custom_emoji': {
                                        'type': 'object',
                                        'description': 'Custom emoji icon (when type is custom_emoji)',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                    'icon': {
                                        'type': 'object',
                                        'description': 'Notion native icon (when type is icon)',
                                        'properties': {
                                            'name': {'type': 'string'},
                                            'color': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'cover': {
                                'type': ['object', 'null'],
                                'description': 'Cover image. Supports external URL or file upload. Set to null to remove.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'Cover type: external or file_upload'},
                                    'external': {
                                        'type': 'object',
                                        'description': 'External URL cover',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'description': 'Uploaded file cover',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'archived': {'type': 'boolean', 'description': 'Set to true to archive the data source'},
                            'in_trash': {'type': 'boolean', 'description': 'Set to true to move the data source to trash'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Notion data source object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique identifier for the data source'},
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Always data_source',
                            },
                            'created_time': {
                                'type': ['string', 'null'],
                                'description': 'Date and time when the data source was created',
                            },
                            'last_edited_time': {
                                'type': ['string', 'null'],
                                'description': 'Date and time when the data source was last edited',
                            },
                            'created_by': {
                                'type': ['object', 'null'],
                                'description': 'User who created the data source',
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
                                'description': 'User who last edited the data source',
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
                                'description': 'Title of the data source as rich text',
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
                                'description': 'Description of the data source as rich text',
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
                                'description': 'Data source icon',
                            },
                            'cover': {
                                'type': ['object', 'null'],
                                'description': 'Data source cover image',
                            },
                            'properties': {
                                'type': ['object', 'null'],
                                'description': 'Schema of properties for the data source',
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
                                            'data_source_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Data source parent ID',
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
                                'description': 'Parent database of the data source',
                            },
                            'database_parent': {
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
                                            'data_source_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Data source parent ID',
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
                                'description': 'Grandparent of the data source (parent of the database)',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL of the data source',
                            },
                            'public_url': {
                                'type': ['string', 'null'],
                                'description': 'Public URL if published',
                            },
                            'archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the data source is archived',
                            },
                            'in_trash': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the data source is in trash',
                            },
                            'is_archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the data source is archived (alias for archived)',
                            },
                            'is_inline': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the data source is inline',
                            },
                            'is_locked': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the data source is locked',
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'data_sources',
                        'x-airbyte-stream-name': 'data_sources',
                        'x-airbyte-ai-hints': {
                            'summary': 'External data sources connected to Notion',
                            'when_to_use': 'Questions about connected data sources or integrations',
                            'trigger_phrases': ['data source', 'connected source', 'notion integration'],
                            'freshness': 'static',
                            'example_questions': ['What data sources are connected to Notion?'],
                            'search_strategy': 'List all data sources',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Notion data source object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the data source'},
                    'object': {
                        'type': ['string', 'null'],
                        'description': 'Always data_source',
                    },
                    'created_time': {
                        'type': ['string', 'null'],
                        'description': 'Date and time when the data source was created',
                    },
                    'last_edited_time': {
                        'type': ['string', 'null'],
                        'description': 'Date and time when the data source was last edited',
                    },
                    'created_by': {
                        'type': ['object', 'null'],
                        'description': 'User who created the data source',
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
                        'description': 'User who last edited the data source',
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
                        'description': 'Title of the data source as rich text',
                        'items': {'$ref': '#/components/schemas/RichText'},
                    },
                    'description': {
                        'type': ['array', 'null'],
                        'description': 'Description of the data source as rich text',
                        'items': {'$ref': '#/components/schemas/RichText'},
                    },
                    'icon': {
                        'type': ['object', 'null'],
                        'description': 'Data source icon',
                    },
                    'cover': {
                        'type': ['object', 'null'],
                        'description': 'Data source cover image',
                    },
                    'properties': {
                        'type': ['object', 'null'],
                        'description': 'Schema of properties for the data source',
                        'additionalProperties': True,
                    },
                    'parent': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Parent'},
                            {'type': 'null'},
                        ],
                        'description': 'Parent database of the data source',
                    },
                    'database_parent': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Parent'},
                            {'type': 'null'},
                        ],
                        'description': 'Grandparent of the data source (parent of the database)',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'URL of the data source',
                    },
                    'public_url': {
                        'type': ['string', 'null'],
                        'description': 'Public URL if published',
                    },
                    'archived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the data source is archived',
                    },
                    'in_trash': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the data source is in trash',
                    },
                    'is_archived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the data source is archived (alias for archived)',
                    },
                    'is_inline': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the data source is inline',
                    },
                    'is_locked': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the data source is locked',
                    },
                    'request_id': {
                        'type': ['string', 'null'],
                        'description': 'Request ID for debugging',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'data_sources',
                'x-airbyte-stream-name': 'data_sources',
                'x-airbyte-ai-hints': {
                    'summary': 'External data sources connected to Notion',
                    'when_to_use': 'Questions about connected data sources or integrations',
                    'trigger_phrases': ['data source', 'connected source', 'notion integration'],
                    'freshness': 'static',
                    'example_questions': ['What data sources are connected to Notion?'],
                    'search_strategy': 'List all data sources',
                },
            },
            ai_hints={
                'summary': 'External data sources connected to Notion',
                'when_to_use': 'Questions about connected data sources or integrations',
                'trigger_phrases': ['data source', 'connected source', 'notion integration'],
                'freshness': 'static',
                'example_questions': ['What data sources are connected to Notion?'],
                'search_strategy': 'List all data sources',
            },
        ),
        EntityDefinition(
            name='blocks',
            stream_name='blocks',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
            ],
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
                            'minimum': 1,
                            'maximum': 100,
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
                            'default': '2025-09-03',
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
                                                        'data_source_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Data source parent ID',
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
                                        'column': {
                                            'type': ['object', 'null'],
                                            'description': 'Column block',
                                            'properties': {
                                                'width_ratio': {
                                                    'type': ['number', 'null'],
                                                },
                                            },
                                        },
                                        'column_list': {
                                            'type': ['object', 'null'],
                                            'description': 'Column list block',
                                        },
                                        'synced_block': {
                                            'type': ['object', 'null'],
                                            'description': 'Synced block content',
                                        },
                                        'template': {
                                            'type': ['object', 'null'],
                                            'description': 'Template block',
                                        },
                                        'link_preview': {
                                            'type': ['object', 'null'],
                                            'description': 'Link preview block',
                                            'properties': {
                                                'url': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'link_to_page': {
                                            'type': ['object', 'null'],
                                            'description': 'Link to page block',
                                        },
                                        'breadcrumb': {
                                            'type': ['object', 'null'],
                                            'description': 'Breadcrumb block',
                                        },
                                        'unsupported': {
                                            'type': ['object', 'null'],
                                            'description': 'Unsupported block type',
                                        },
                                        'request_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Request ID for debugging',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'blocks',
                                    'x-airbyte-stream-name': 'blocks',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Content blocks (paragraphs, headings, lists, etc.) within Notion pages',
                                        'when_to_use': 'Looking at page content structure or specific content blocks',
                                        'trigger_phrases': ['notion block', 'page content', 'content block'],
                                        'freshness': 'live',
                                        'example_questions': ['Show the content blocks of a Notion page'],
                                        'search_strategy': 'Filter by parent page',
                                    },
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
                Action.CREATE: EndpointDefinition(
                    method='PATCH',
                    path='/v1/blocks/{block_id}/children',
                    action=Action.CREATE,
                    description='Creates and appends new children blocks to the specified parent block or page',
                    body_fields=['children'],
                    path_params=['block_id'],
                    path_params_schema={
                        'block_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2025-09-03',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for appending child blocks to a parent block or page. The block_id path parameter specifies the parent.',
                        'properties': {
                            'children': {
                                'type': 'array',
                                'description': 'Array of block objects to append (max 100). Each block must specify a type and corresponding content.',
                                'items': {
                                    'type': 'object',
                                    'description': 'A block object. Set type to the block kind and include matching content.',
                                    'properties': {
                                        'type': {'type': 'string', 'description': 'Block type: paragraph, heading_1, heading_2, heading_3, bulleted_list_item, numbered_list_item, to_do, toggle, code, quote, callout, divider, bookmark, embed, equation, table_of_contents, image, video, file, pdf, audio, column_list, column, table, synced_block, link_to_page, etc.'},
                                        'paragraph': {
                                            'type': 'object',
                                            'description': 'Paragraph block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {'type': 'string'},
                                            },
                                        },
                                        'heading_1': {
                                            'type': 'object',
                                            'description': 'Heading 1 block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {'type': 'string'},
                                                'is_toggleable': {'type': 'boolean'},
                                            },
                                        },
                                        'heading_2': {
                                            'type': 'object',
                                            'description': 'Heading 2 block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {'type': 'string'},
                                                'is_toggleable': {'type': 'boolean'},
                                            },
                                        },
                                        'heading_3': {
                                            'type': 'object',
                                            'description': 'Heading 3 block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {'type': 'string'},
                                                'is_toggleable': {'type': 'boolean'},
                                            },
                                        },
                                        'bulleted_list_item': {
                                            'type': 'object',
                                            'description': 'Bulleted list item content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {'type': 'string'},
                                            },
                                        },
                                        'numbered_list_item': {
                                            'type': 'object',
                                            'description': 'Numbered list item content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {'type': 'string'},
                                            },
                                        },
                                        'to_do': {
                                            'type': 'object',
                                            'description': 'To-do block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'checked': {'type': 'boolean'},
                                                'color': {'type': 'string'},
                                            },
                                        },
                                        'toggle': {
                                            'type': 'object',
                                            'description': 'Toggle block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {'type': 'string'},
                                            },
                                        },
                                        'code': {
                                            'type': 'object',
                                            'description': 'Code block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'language': {'type': 'string', 'description': 'Programming language for syntax highlighting'},
                                            },
                                        },
                                        'quote': {
                                            'type': 'object',
                                            'description': 'Quote block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'color': {'type': 'string'},
                                            },
                                        },
                                        'callout': {
                                            'type': 'object',
                                            'description': 'Callout block content',
                                            'properties': {
                                                'rich_text': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'icon': {'type': 'object'},
                                                'color': {'type': 'string'},
                                            },
                                        },
                                        'divider': {'type': 'object', 'description': 'Divider block (empty object)'},
                                        'bookmark': {
                                            'type': 'object',
                                            'description': 'Bookmark block',
                                            'properties': {
                                                'url': {'type': 'string', 'description': 'URL to bookmark'},
                                                'caption': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'default': 'text'},
                                                            'text': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'content': {'type': 'string'},
                                                                    'link': {
                                                                        'type': ['object', 'null'],
                                                                        'properties': {
                                                                            'url': {'type': 'string'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'mention': {'type': 'object', 'additionalProperties': True},
                                                            'equation': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'expression': {'type': 'string'},
                                                                },
                                                            },
                                                            'annotations': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'bold': {'type': 'boolean'},
                                                                    'italic': {'type': 'boolean'},
                                                                    'strikethrough': {'type': 'boolean'},
                                                                    'underline': {'type': 'boolean'},
                                                                    'code': {'type': 'boolean'},
                                                                    'color': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'embed': {
                                            'type': 'object',
                                            'description': 'Embed block',
                                            'properties': {
                                                'url': {'type': 'string', 'description': 'URL to embed'},
                                            },
                                        },
                                        'equation': {
                                            'type': 'object',
                                            'description': 'Equation block',
                                            'properties': {
                                                'expression': {'type': 'string', 'description': 'LaTeX expression'},
                                            },
                                        },
                                        'table_of_contents': {
                                            'type': 'object',
                                            'description': 'Table of contents block',
                                            'properties': {
                                                'color': {'type': 'string'},
                                            },
                                        },
                                        'image': {
                                            'type': 'object',
                                            'description': 'Media file. Use external URL or file upload.',
                                            'properties': {
                                                'type': {'type': 'string', 'description': 'File type: external or file_upload'},
                                                'external': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'url': {'type': 'string'},
                                                    },
                                                },
                                                'file_upload': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                        'video': {
                                            'type': 'object',
                                            'description': 'Media file. Use external URL or file upload.',
                                            'properties': {
                                                'type': {'type': 'string', 'description': 'File type: external or file_upload'},
                                                'external': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'url': {'type': 'string'},
                                                    },
                                                },
                                                'file_upload': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                        'file': {
                                            'type': 'object',
                                            'description': 'Media file. Use external URL or file upload.',
                                            'properties': {
                                                'type': {'type': 'string', 'description': 'File type: external or file_upload'},
                                                'external': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'url': {'type': 'string'},
                                                    },
                                                },
                                                'file_upload': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                        'pdf': {
                                            'type': 'object',
                                            'description': 'Media file. Use external URL or file upload.',
                                            'properties': {
                                                'type': {'type': 'string', 'description': 'File type: external or file_upload'},
                                                'external': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'url': {'type': 'string'},
                                                    },
                                                },
                                                'file_upload': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                        'audio': {
                                            'type': 'object',
                                            'description': 'Media file. Use external URL or file upload.',
                                            'properties': {
                                                'type': {'type': 'string', 'description': 'File type: external or file_upload'},
                                                'external': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'url': {'type': 'string'},
                                                    },
                                                },
                                                'file_upload': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                        'required': ['children'],
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
                                                        'data_source_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Data source parent ID',
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
                                        'column': {
                                            'type': ['object', 'null'],
                                            'description': 'Column block',
                                            'properties': {
                                                'width_ratio': {
                                                    'type': ['number', 'null'],
                                                },
                                            },
                                        },
                                        'column_list': {
                                            'type': ['object', 'null'],
                                            'description': 'Column list block',
                                        },
                                        'synced_block': {
                                            'type': ['object', 'null'],
                                            'description': 'Synced block content',
                                        },
                                        'template': {
                                            'type': ['object', 'null'],
                                            'description': 'Template block',
                                        },
                                        'link_preview': {
                                            'type': ['object', 'null'],
                                            'description': 'Link preview block',
                                            'properties': {
                                                'url': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'link_to_page': {
                                            'type': ['object', 'null'],
                                            'description': 'Link to page block',
                                        },
                                        'breadcrumb': {
                                            'type': ['object', 'null'],
                                            'description': 'Breadcrumb block',
                                        },
                                        'unsupported': {
                                            'type': ['object', 'null'],
                                            'description': 'Unsupported block type',
                                        },
                                        'request_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Request ID for debugging',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'blocks',
                                    'x-airbyte-stream-name': 'blocks',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Content blocks (paragraphs, headings, lists, etc.) within Notion pages',
                                        'when_to_use': 'Looking at page content structure or specific content blocks',
                                        'trigger_phrases': ['notion block', 'page content', 'content block'],
                                        'freshness': 'live',
                                        'example_questions': ['Show the content blocks of a Notion page'],
                                        'search_strategy': 'Filter by parent page',
                                    },
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
                            'default': '2025-09-03',
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
                                            'data_source_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Data source parent ID',
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
                            'column': {
                                'type': ['object', 'null'],
                                'description': 'Column block',
                                'properties': {
                                    'width_ratio': {
                                        'type': ['number', 'null'],
                                    },
                                },
                            },
                            'column_list': {
                                'type': ['object', 'null'],
                                'description': 'Column list block',
                            },
                            'synced_block': {
                                'type': ['object', 'null'],
                                'description': 'Synced block content',
                            },
                            'template': {
                                'type': ['object', 'null'],
                                'description': 'Template block',
                            },
                            'link_preview': {
                                'type': ['object', 'null'],
                                'description': 'Link preview block',
                                'properties': {
                                    'url': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'link_to_page': {
                                'type': ['object', 'null'],
                                'description': 'Link to page block',
                            },
                            'breadcrumb': {
                                'type': ['object', 'null'],
                                'description': 'Breadcrumb block',
                            },
                            'unsupported': {
                                'type': ['object', 'null'],
                                'description': 'Unsupported block type',
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'blocks',
                        'x-airbyte-stream-name': 'blocks',
                        'x-airbyte-ai-hints': {
                            'summary': 'Content blocks (paragraphs, headings, lists, etc.) within Notion pages',
                            'when_to_use': 'Looking at page content structure or specific content blocks',
                            'trigger_phrases': ['notion block', 'page content', 'content block'],
                            'freshness': 'live',
                            'example_questions': ['Show the content blocks of a Notion page'],
                            'search_strategy': 'Filter by parent page',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/v1/blocks/{block_id}',
                    action=Action.UPDATE,
                    description='Updates the content of a block based on its type',
                    body_fields=[
                        'paragraph',
                        'heading_1',
                        'heading_2',
                        'heading_3',
                        'bulleted_list_item',
                        'numbered_list_item',
                        'to_do',
                        'toggle',
                        'code',
                        'quote',
                        'callout',
                        'bookmark',
                        'embed',
                        'equation',
                        'image',
                        'video',
                        'file',
                        'pdf',
                        'audio',
                        'table',
                        'archived',
                    ],
                    path_params=['block_id'],
                    path_params_schema={
                        'block_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2025-09-03',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating a block. Include the block type and its updated content. Omitted fields within the type are unchanged.',
                        'properties': {
                            'paragraph': {
                                'type': 'object',
                                'description': 'Updated paragraph content',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'color': {'type': 'string'},
                                },
                            },
                            'heading_1': {
                                'type': 'object',
                                'description': 'Updated heading 1 content',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'color': {'type': 'string'},
                                    'is_toggleable': {'type': 'boolean'},
                                },
                            },
                            'heading_2': {
                                'type': 'object',
                                'description': 'Updated heading 2 content',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'color': {'type': 'string'},
                                    'is_toggleable': {'type': 'boolean'},
                                },
                            },
                            'heading_3': {
                                'type': 'object',
                                'description': 'Updated heading 3 content',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'color': {'type': 'string'},
                                    'is_toggleable': {'type': 'boolean'},
                                },
                            },
                            'bulleted_list_item': {
                                'type': 'object',
                                'description': 'Updated bulleted list item',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'color': {'type': 'string'},
                                },
                            },
                            'numbered_list_item': {
                                'type': 'object',
                                'description': 'Updated numbered list item',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'color': {'type': 'string'},
                                },
                            },
                            'to_do': {
                                'type': 'object',
                                'description': 'Updated to-do content',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'checked': {'type': 'boolean'},
                                    'color': {'type': 'string'},
                                },
                            },
                            'toggle': {
                                'type': 'object',
                                'description': 'Updated toggle content',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'color': {'type': 'string'},
                                },
                            },
                            'code': {
                                'type': 'object',
                                'description': 'Updated code block content',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'language': {'type': 'string'},
                                    'caption': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'quote': {
                                'type': 'object',
                                'description': 'Updated quote content',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'color': {'type': 'string'},
                                },
                            },
                            'callout': {
                                'type': 'object',
                                'description': 'Updated callout content',
                                'properties': {
                                    'rich_text': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'icon': {'type': 'object'},
                                    'color': {'type': 'string'},
                                },
                            },
                            'bookmark': {
                                'type': 'object',
                                'description': 'Updated bookmark',
                                'properties': {
                                    'url': {'type': 'string'},
                                    'caption': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'default': 'text'},
                                                'text': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'content': {'type': 'string'},
                                                        'link': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'url': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'mention': {'type': 'object', 'additionalProperties': True},
                                                'equation': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'expression': {'type': 'string'},
                                                    },
                                                },
                                                'annotations': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bold': {'type': 'boolean'},
                                                        'italic': {'type': 'boolean'},
                                                        'strikethrough': {'type': 'boolean'},
                                                        'underline': {'type': 'boolean'},
                                                        'code': {'type': 'boolean'},
                                                        'color': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'embed': {
                                'type': 'object',
                                'description': 'Updated embed',
                                'properties': {
                                    'url': {'type': 'string'},
                                },
                            },
                            'equation': {
                                'type': 'object',
                                'description': 'Updated equation',
                                'properties': {
                                    'expression': {'type': 'string'},
                                },
                            },
                            'image': {
                                'type': 'object',
                                'description': 'Media file. Use external URL or file upload.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'File type: external or file_upload'},
                                    'external': {
                                        'type': 'object',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'video': {
                                'type': 'object',
                                'description': 'Media file. Use external URL or file upload.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'File type: external or file_upload'},
                                    'external': {
                                        'type': 'object',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'file': {
                                'type': 'object',
                                'description': 'Media file. Use external URL or file upload.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'File type: external or file_upload'},
                                    'external': {
                                        'type': 'object',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'pdf': {
                                'type': 'object',
                                'description': 'Media file. Use external URL or file upload.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'File type: external or file_upload'},
                                    'external': {
                                        'type': 'object',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'audio': {
                                'type': 'object',
                                'description': 'Media file. Use external URL or file upload.',
                                'properties': {
                                    'type': {'type': 'string', 'description': 'File type: external or file_upload'},
                                    'external': {
                                        'type': 'object',
                                        'properties': {
                                            'url': {'type': 'string'},
                                        },
                                    },
                                    'file_upload': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'table': {
                                'type': 'object',
                                'description': 'Updated table properties',
                                'properties': {
                                    'has_column_header': {'type': 'boolean'},
                                    'has_row_header': {'type': 'boolean'},
                                },
                            },
                            'archived': {'type': 'boolean', 'description': 'Set to true to archive the block (API version 2025-09-03)'},
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
                                            'data_source_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Data source parent ID',
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
                            'column': {
                                'type': ['object', 'null'],
                                'description': 'Column block',
                                'properties': {
                                    'width_ratio': {
                                        'type': ['number', 'null'],
                                    },
                                },
                            },
                            'column_list': {
                                'type': ['object', 'null'],
                                'description': 'Column list block',
                            },
                            'synced_block': {
                                'type': ['object', 'null'],
                                'description': 'Synced block content',
                            },
                            'template': {
                                'type': ['object', 'null'],
                                'description': 'Template block',
                            },
                            'link_preview': {
                                'type': ['object', 'null'],
                                'description': 'Link preview block',
                                'properties': {
                                    'url': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'link_to_page': {
                                'type': ['object', 'null'],
                                'description': 'Link to page block',
                            },
                            'breadcrumb': {
                                'type': ['object', 'null'],
                                'description': 'Breadcrumb block',
                            },
                            'unsupported': {
                                'type': ['object', 'null'],
                                'description': 'Unsupported block type',
                            },
                            'request_id': {
                                'type': ['string', 'null'],
                                'description': 'Request ID for debugging',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'blocks',
                        'x-airbyte-stream-name': 'blocks',
                        'x-airbyte-ai-hints': {
                            'summary': 'Content blocks (paragraphs, headings, lists, etc.) within Notion pages',
                            'when_to_use': 'Looking at page content structure or specific content blocks',
                            'trigger_phrases': ['notion block', 'page content', 'content block'],
                            'freshness': 'live',
                            'example_questions': ['Show the content blocks of a Notion page'],
                            'search_strategy': 'Filter by parent page',
                        },
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
                    'column': {
                        'type': ['object', 'null'],
                        'description': 'Column block',
                        'properties': {
                            'width_ratio': {
                                'type': ['number', 'null'],
                            },
                        },
                    },
                    'column_list': {
                        'type': ['object', 'null'],
                        'description': 'Column list block',
                    },
                    'synced_block': {
                        'type': ['object', 'null'],
                        'description': 'Synced block content',
                    },
                    'template': {
                        'type': ['object', 'null'],
                        'description': 'Template block',
                    },
                    'link_preview': {
                        'type': ['object', 'null'],
                        'description': 'Link preview block',
                        'properties': {
                            'url': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'link_to_page': {
                        'type': ['object', 'null'],
                        'description': 'Link to page block',
                    },
                    'breadcrumb': {
                        'type': ['object', 'null'],
                        'description': 'Breadcrumb block',
                    },
                    'unsupported': {
                        'type': ['object', 'null'],
                        'description': 'Unsupported block type',
                    },
                    'request_id': {
                        'type': ['string', 'null'],
                        'description': 'Request ID for debugging',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'blocks',
                'x-airbyte-stream-name': 'blocks',
                'x-airbyte-ai-hints': {
                    'summary': 'Content blocks (paragraphs, headings, lists, etc.) within Notion pages',
                    'when_to_use': 'Looking at page content structure or specific content blocks',
                    'trigger_phrases': ['notion block', 'page content', 'content block'],
                    'freshness': 'live',
                    'example_questions': ['Show the content blocks of a Notion page'],
                    'search_strategy': 'Filter by parent page',
                },
            },
            ai_hints={
                'summary': 'Content blocks (paragraphs, headings, lists, etc.) within Notion pages',
                'when_to_use': 'Looking at page content structure or specific content blocks',
                'trigger_phrases': ['notion block', 'page content', 'content block'],
                'freshness': 'live',
                'example_questions': ['Show the content blocks of a Notion page'],
                'search_strategy': 'Filter by parent page',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='blocks',
                    target_entity='pages',
                    foreign_key='block_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='comments',
            stream_name='comments',
            actions=[Action.LIST, Action.CREATE],
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
                            'minimum': 1,
                            'maximum': 100,
                        },
                    },
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2025-09-03',
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
                                                        'data_source_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Data source parent ID',
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Comments on Notion pages and blocks',
                                        'when_to_use': 'Looking for discussion or feedback on Notion pages',
                                        'trigger_phrases': ['notion comment', 'page comment', 'feedback'],
                                        'freshness': 'live',
                                        'example_questions': ['What comments are on this Notion page?'],
                                        'search_strategy': 'Filter by page',
                                    },
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
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/comments',
                    action=Action.CREATE,
                    description='Creates a comment on a page or block, or replies to an existing discussion thread',
                    body_fields=['parent', 'discussion_id', 'rich_text'],
                    header_params=['Notion-Version'],
                    header_params_schema={
                        'Notion-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2025-09-03',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a comment. Provide either parent (with page_id or block_id) for a new comment, or discussion_id to reply to an existing thread. Exactly one of parent or discussion_id must be provided.',
                        'properties': {
                            'parent': {
                                'type': 'object',
                                'description': 'Parent of the comment. Provide exactly one of page_id or block_id. Mutually exclusive with discussion_id.',
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'required': ['page_id'],
                                        'properties': {
                                            'page_id': {'type': 'string', 'description': 'ID of the page to comment on'},
                                        },
                                    },
                                    {
                                        'type': 'object',
                                        'required': ['block_id'],
                                        'properties': {
                                            'block_id': {'type': 'string', 'description': 'ID of the block to comment on'},
                                        },
                                    },
                                ],
                            },
                            'discussion_id': {'type': 'string', 'description': 'ID of an existing discussion thread to reply to. Mutually exclusive with parent.'},
                            'rich_text': {
                                'type': 'array',
                                'description': 'Content of the comment as rich text',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'type': {'type': 'string', 'default': 'text'},
                                        'text': {
                                            'type': 'object',
                                            'properties': {
                                                'content': {'type': 'string'},
                                                'link': {
                                                    'type': ['object', 'null'],
                                                    'properties': {
                                                        'url': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                        'mention': {'type': 'object', 'additionalProperties': True},
                                        'equation': {
                                            'type': 'object',
                                            'properties': {
                                                'expression': {'type': 'string'},
                                            },
                                        },
                                        'annotations': {
                                            'type': 'object',
                                            'properties': {
                                                'bold': {'type': 'boolean'},
                                                'italic': {'type': 'boolean'},
                                                'strikethrough': {'type': 'boolean'},
                                                'underline': {'type': 'boolean'},
                                                'code': {'type': 'boolean'},
                                                'color': {'type': 'string'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['rich_text'],
                    },
                    response_schema={
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
                                            'data_source_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Data source parent ID',
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Comments on Notion pages and blocks',
                            'when_to_use': 'Looking for discussion or feedback on Notion pages',
                            'trigger_phrases': ['notion comment', 'page comment', 'feedback'],
                            'freshness': 'live',
                            'example_questions': ['What comments are on this Notion page?'],
                            'search_strategy': 'Filter by page',
                        },
                    },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Comments on Notion pages and blocks',
                    'when_to_use': 'Looking for discussion or feedback on Notion pages',
                    'trigger_phrases': ['notion comment', 'page comment', 'feedback'],
                    'freshness': 'live',
                    'example_questions': ['What comments are on this Notion page?'],
                    'search_strategy': 'Filter by page',
                },
            },
            ai_hints={
                'summary': 'Comments on Notion pages and blocks',
                'when_to_use': 'Looking for discussion or feedback on Notion pages',
                'trigger_phrases': ['notion comment', 'page comment', 'feedback'],
                'freshness': 'live',
                'example_questions': ['What comments are on this Notion page?'],
                'search_strategy': 'Filter by page',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='comments',
                    target_entity='pages',
                    foreign_key='block_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='pages',
                suggested=True,
                x_airbyte_name='pages',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates whether the page is archived or not.',
                    ),
                    CacheFieldConfig(
                        name='cover',
                        type=['null', 'object'],
                        description='URL or reference to the page cover image.',
                    ),
                    CacheFieldConfig(
                        name='created_by',
                        type=['null', 'object'],
                        description='User ID or name of the creator of the page.',
                    ),
                    CacheFieldConfig(
                        name='created_time',
                        type=['null', 'string'],
                        description='Date and time when the page was created.',
                    ),
                    CacheFieldConfig(
                        name='icon',
                        type=['null', 'object'],
                        description='URL or reference to the page icon.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier of the page.',
                    ),
                    CacheFieldConfig(
                        name='in_trash',
                        type=['null', 'boolean'],
                        description='Indicates whether the page is in trash or not.',
                    ),
                    CacheFieldConfig(
                        name='last_edited_by',
                        type=['null', 'object'],
                        description='User ID or name of the last editor of the page.',
                    ),
                    CacheFieldConfig(
                        name='last_edited_time',
                        type=['null', 'string'],
                        description='Date and time when the page was last edited.',
                    ),
                    CacheFieldConfig(
                        name='object',
                        type=['null', 'object'],
                        description='Type or category of the page object.',
                    ),
                    CacheFieldConfig(
                        name='parent',
                        type=['null', 'object'],
                        description='ID or reference to the parent page.',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['null', 'array'],
                        description='Custom properties associated with the page.',
                    ),
                    CacheFieldConfig(
                        name='public_url',
                        type=['null', 'string'],
                        description='Publicly accessible URL of the page.',
                    ),
                    CacheFieldConfig(
                        name='url',
                        type=['null', 'string'],
                        description='URL of the page within the service.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='users',
                x_airbyte_name='users',
                fields=[
                    CacheFieldConfig(
                        name='avatar_url',
                        type=['null', 'string'],
                        description="URL of the user's avatar",
                    ),
                    CacheFieldConfig(
                        name='bot',
                        type=['null', 'object'],
                        description='Bot-specific data',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the user',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description="User's display name",
                    ),
                    CacheFieldConfig(
                        name='object',
                        type=['null', 'object'],
                        description='Always user',
                    ),
                    CacheFieldConfig(
                        name='person',
                        type=['null', 'object'],
                        description='Person-specific data',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'object'],
                        description='Type of user (person or bot)',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='data_sources',
                suggested=True,
                x_airbyte_name='data_sources',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates if the data source is archived or not.',
                    ),
                    CacheFieldConfig(
                        name='cover',
                        type=['null', 'object'],
                        description='URL or reference to the cover image of the data source.',
                    ),
                    CacheFieldConfig(
                        name='created_by',
                        type=['null', 'object'],
                        description='The user who created the data source.',
                    ),
                    CacheFieldConfig(
                        name='created_time',
                        type=['null', 'string'],
                        description='The timestamp when the data source was created.',
                    ),
                    CacheFieldConfig(
                        name='database_parent',
                        type=['null', 'object'],
                        description='The grandparent of the data source (parent of the database).',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'array'],
                        description='Description text associated with the data source.',
                    ),
                    CacheFieldConfig(
                        name='icon',
                        type=['null', 'object'],
                        description='URL or reference to the icon of the data source.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier of the data source.',
                    ),
                    CacheFieldConfig(
                        name='is_inline',
                        type=['null', 'boolean'],
                        description='Indicates if the data source is displayed inline.',
                    ),
                    CacheFieldConfig(
                        name='last_edited_by',
                        type=['null', 'object'],
                        description='The user who last edited the data source.',
                    ),
                    CacheFieldConfig(
                        name='last_edited_time',
                        type=['null', 'string'],
                        description='The timestamp when the data source was last edited.',
                    ),
                    CacheFieldConfig(
                        name='object',
                        type=['null', 'object'],
                        description='The type of object (data_source).',
                    ),
                    CacheFieldConfig(
                        name='parent',
                        type=['null', 'object'],
                        description='The parent database of the data source.',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['null', 'array'],
                        description='Schema of properties for the data source.',
                    ),
                    CacheFieldConfig(
                        name='public_url',
                        type=['null', 'string'],
                        description='Public URL to access the data source.',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'array'],
                        description='Title or name of the data source.',
                    ),
                    CacheFieldConfig(
                        name='url',
                        type=['null', 'string'],
                        description='URL or reference to access the data source.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='blocks',
                suggested=True,
                x_airbyte_name='blocks',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates if the block is archived or not.',
                    ),
                    CacheFieldConfig(
                        name='bookmark',
                        type=['null', 'object'],
                        description='Represents a bookmark within the block',
                    ),
                    CacheFieldConfig(
                        name='breadcrumb',
                        type=['null', 'object'],
                        description='Represents a breadcrumb block.',
                    ),
                    CacheFieldConfig(
                        name='bulleted_list_item',
                        type=['null', 'object'],
                        description='Represents an item in a bulleted list.',
                    ),
                    CacheFieldConfig(
                        name='callout',
                        type=['null', 'object'],
                        description='Describes a callout message or content in the block',
                    ),
                    CacheFieldConfig(
                        name='child_database',
                        type=['null', 'object'],
                        description='Represents a child database block.',
                    ),
                    CacheFieldConfig(
                        name='child_page',
                        type=['null', 'object'],
                        description='Represents a child page block.',
                    ),
                    CacheFieldConfig(
                        name='code',
                        type=['null', 'object'],
                        description='Contains code snippets or blocks in the block content',
                    ),
                    CacheFieldConfig(
                        name='column',
                        type=['null', 'object'],
                        description='Represents a column block.',
                    ),
                    CacheFieldConfig(
                        name='column_list',
                        type=['null', 'object'],
                        description='Represents a list of columns.',
                    ),
                    CacheFieldConfig(
                        name='created_by',
                        type=['null', 'object'],
                        description='The user who created the block.',
                    ),
                    CacheFieldConfig(
                        name='created_time',
                        type=['null', 'string'],
                        description='The timestamp when the block was created.',
                    ),
                    CacheFieldConfig(
                        name='divider',
                        type=['null', 'object'],
                        description='Represents a divider block.',
                    ),
                    CacheFieldConfig(
                        name='embed',
                        type=['null', 'object'],
                        description='Contains embedded content such as videos, tweets, etc.',
                    ),
                    CacheFieldConfig(
                        name='equation',
                        type=['null', 'object'],
                        description='Represents an equation or mathematical formula in the block',
                    ),
                    CacheFieldConfig(
                        name='file',
                        type=['null', 'object'],
                        description='Represents a file block.',
                    ),
                    CacheFieldConfig(
                        name='has_children',
                        type=['null', 'boolean'],
                        description='Indicates if the block has children or not.',
                    ),
                    CacheFieldConfig(
                        name='heading_1',
                        type=['null', 'object'],
                        description='Represents a level 1 heading.',
                    ),
                    CacheFieldConfig(
                        name='heading_2',
                        type=['null', 'object'],
                        description='Represents a level 2 heading.',
                    ),
                    CacheFieldConfig(
                        name='heading_3',
                        type=['null', 'object'],
                        description='Represents a level 3 heading.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='The unique identifier of the block.',
                    ),
                    CacheFieldConfig(
                        name='image',
                        type=['null', 'object'],
                        description='Represents an image block.',
                    ),
                    CacheFieldConfig(
                        name='last_edited_by',
                        type=['null', 'object'],
                        description='The user who last edited the block.',
                    ),
                    CacheFieldConfig(
                        name='last_edited_time',
                        type=['null', 'string'],
                        description='The timestamp when the block was last edited.',
                    ),
                    CacheFieldConfig(
                        name='link_preview',
                        type=['null', 'object'],
                        description='Displays a preview of an external link within the block',
                    ),
                    CacheFieldConfig(
                        name='link_to_page',
                        type=['null', 'object'],
                        description='Provides a link to another page within the block',
                    ),
                    CacheFieldConfig(
                        name='numbered_list_item',
                        type=['null', 'object'],
                        description='Represents an item in a numbered list.',
                    ),
                    CacheFieldConfig(
                        name='object',
                        type=['null', 'object'],
                        description='Represents an object block.',
                    ),
                    CacheFieldConfig(
                        name='paragraph',
                        type=['null', 'object'],
                        description='Represents a paragraph block.',
                    ),
                    CacheFieldConfig(
                        name='parent',
                        type=['null', 'object'],
                        description='The parent block of the current block.',
                    ),
                    CacheFieldConfig(
                        name='pdf',
                        type=['null', 'object'],
                        description='Represents a PDF document block.',
                    ),
                    CacheFieldConfig(
                        name='quote',
                        type=['null', 'object'],
                        description='Represents a quote block.',
                    ),
                    CacheFieldConfig(
                        name='synced_block',
                        type=['null', 'object'],
                        description='Represents a block synced from another source',
                    ),
                    CacheFieldConfig(
                        name='table',
                        type=['null', 'object'],
                        description='Represents a table within the block',
                    ),
                    CacheFieldConfig(
                        name='table_of_contents',
                        type=['null', 'object'],
                        description='Contains information regarding the table of contents',
                    ),
                    CacheFieldConfig(
                        name='table_row',
                        type=['null', 'object'],
                        description='Represents a row in a table within the block',
                    ),
                    CacheFieldConfig(
                        name='template',
                        type=['null', 'object'],
                        description='Specifies a template used within the block',
                    ),
                    CacheFieldConfig(
                        name='to_do',
                        type=['null', 'object'],
                        description='Represents a to-do list or task content',
                    ),
                    CacheFieldConfig(
                        name='toggle',
                        type=['null', 'object'],
                        description='Represents a toggle block.',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'object'],
                        description='The type of the block.',
                    ),
                    CacheFieldConfig(
                        name='unsupported',
                        type=['null', 'object'],
                        description='Represents an unsupported block.',
                    ),
                    CacheFieldConfig(
                        name='video',
                        type=['null', 'object'],
                        description='Represents a video block.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='comments',
                x_airbyte_name='comments',
                fields=[
                    CacheFieldConfig(
                        name='created_by',
                        type=['null', 'object'],
                        description='User who created the comment.',
                    ),
                    CacheFieldConfig(
                        name='created_time',
                        type=['null', 'string'],
                        description='Date and time when the comment was created.',
                    ),
                    CacheFieldConfig(
                        name='discussion_id',
                        type=['null', 'string'],
                        description='Discussion thread ID.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the comment.',
                    ),
                    CacheFieldConfig(
                        name='last_edited_time',
                        type=['null', 'string'],
                        description='Date and time when the comment was last edited.',
                    ),
                    CacheFieldConfig(
                        name='object',
                        type=['null', 'string'],
                        description='Always comment.',
                    ),
                    CacheFieldConfig(
                        name='parent',
                        type=['null', 'object'],
                        description='Parent of the comment.',
                    ),
                    CacheFieldConfig(
                        name='rich_text',
                        type=['null', 'array'],
                        description='Content of the comment as rich text.',
                    ),
                ],
            ),
        ],
    ),
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
        'data_sources': [
            'archived',
            'cover',
            'created_by',
            'created_time',
            'database_parent',
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
        'comments': [
            'created_by',
            'created_time',
            'discussion_id',
            'id',
            'last_edited_time',
            'object',
            'parent',
            'rich_text',
            'rich_text[]',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all users in my Notion workspace',
            'Show me all pages in my Notion workspace',
            'What data sources exist in my Notion workspace?',
            'Get the details of a specific page by ID',
            'List child blocks of a specific page',
            'Show me comments on a specific page',
            'What is the schema of a specific data source?',
            'Who are the bot users in my workspace?',
            "Create a new page titled 'Meeting Notes' under page X",
            'Update the icon of page X to a rocket emoji',
            "Add a paragraph block saying 'Hello World' to page X",
            'Mark the to-do block as completed',
            "Add a comment to page X saying 'Looks good!'",
            'Archive page X',
            "Update the title of data source X to 'Project Tracker'",
        ],
        context_store_search=['Find pages created in the last week', 'List data sources that have been recently edited', 'Show me all archived pages'],
        search=['Find pages created in the last week', 'List data sources that have been recently edited', 'Show me all archived pages'],
        unsupported=[
            'Delete a page permanently',
            'Delete a block permanently',
            'Delete a comment',
            'Create a new user',
        ],
    ),
)