"""
Connector model for confluence.

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
    CacheConfig,
    CacheEntityConfig,
    CacheFieldConfig,
    CacheFieldProperty,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

ConfluenceConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('cf40a7f8-71f8-45ce-a7fa-fca053e4028c'),
    name='confluence',
    version='1.0.1',
    base_url='https://{subdomain}.atlassian.net',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AuthConfigSpec(
            title='Confluence API Token Authentication',
            description='Authenticate using your Atlassian account email and API token',
            type='object',
            required=['username', 'password'],
            properties={
                'username': AuthConfigFieldSpec(
                    title='Email Address',
                    description='Your Atlassian account email address',
                    format='email',
                ),
                'password': AuthConfigFieldSpec(
                    title='API Token',
                    description='Your Confluence API token from https://id.atlassian.com/manage-profile/security/api-tokens',
                ),
            },
            auth_mapping={'username': '${username}', 'password': '${password}'},
            replication_auth_key_mapping={'email': 'username', 'api_token': 'password'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='spaces',
            stream_name='space',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/wiki/api/v2/spaces',
                    action=Action.LIST,
                    description='Returns all spaces. Only spaces that the user has permission to view will be returned.',
                    query_params=[
                        'cursor',
                        'limit',
                        'type',
                        'status',
                        'keys',
                        'sort',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'type': {
                            'type': 'string',
                            'required': False,
                            'enum': ['global', 'personal'],
                        },
                        'status': {
                            'type': 'string',
                            'required': False,
                            'enum': ['current', 'archived'],
                        },
                        'keys': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'string'},
                        },
                        'sort': {
                            'type': 'string',
                            'required': False,
                            'enum': [
                                'id',
                                '-id',
                                'key',
                                '-key',
                                'name',
                                '-name',
                            ],
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of spaces',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Confluence space object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique space identifier'},
                                        'key': {'type': 'string', 'description': 'Space key'},
                                        'name': {'type': 'string', 'description': 'Space name'},
                                        'type': {'type': 'string', 'description': 'Space type (global or personal)'},
                                        'status': {'type': 'string', 'description': 'Space status (current or archived)'},
                                        'authorId': {'type': 'string', 'description': 'ID of the user who created the space'},
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Timestamp when the space was created',
                                        },
                                        'homepageId': {'type': 'string', 'description': 'ID of the space homepage'},
                                        'spaceOwnerId': {'type': 'string', 'description': 'ID of the space owner'},
                                        'currentActiveAlias': {'type': 'string', 'description': 'Currently active alias for the space'},
                                        'description': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'plain': {'type': 'object'},
                                                        'view': {'type': 'object'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Space description in various formats',
                                        },
                                        'icon': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'path': {'type': 'string', 'description': 'Path to the icon'},
                                                        'apiDownloadLink': {'type': 'string', 'description': 'API download link for the icon'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Space icon information',
                                        },
                                        '_links': {
                                            'type': 'object',
                                            'description': 'Links related to the space',
                                            'properties': {
                                                'webui': {'type': 'string', 'description': 'Web UI link'},
                                                'base': {'type': 'string', 'description': 'Base URL'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'spaces',
                                    'x-airbyte-stream-name': 'space',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Confluence spaces organizing pages and documentation',
                                        'when_to_use': 'Questions about available documentation spaces or project wikis',
                                        'trigger_phrases': ['confluence space', 'wiki space', 'documentation area'],
                                        'freshness': 'live',
                                        'example_questions': ['What Confluence spaces are available?', 'Find the engineering wiki space'],
                                        'search_strategy': 'Search by name or key',
                                    },
                                },
                            },
                            '_links': {
                                'type': 'object',
                                'properties': {
                                    'next': {'type': 'string', 'description': 'URL for the next page of results'},
                                    'base': {'type': 'string', 'description': 'Base URL'},
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next': '$._links.next'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/wiki/api/v2/spaces/{id}',
                    action=Action.GET,
                    description='Returns a specific space.',
                    query_params=['description-format'],
                    query_params_schema={
                        'description-format': {
                            'type': 'string',
                            'required': False,
                            'enum': ['plain', 'view'],
                        },
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Confluence space object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique space identifier'},
                            'key': {'type': 'string', 'description': 'Space key'},
                            'name': {'type': 'string', 'description': 'Space name'},
                            'type': {'type': 'string', 'description': 'Space type (global or personal)'},
                            'status': {'type': 'string', 'description': 'Space status (current or archived)'},
                            'authorId': {'type': 'string', 'description': 'ID of the user who created the space'},
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Timestamp when the space was created',
                            },
                            'homepageId': {'type': 'string', 'description': 'ID of the space homepage'},
                            'spaceOwnerId': {'type': 'string', 'description': 'ID of the space owner'},
                            'currentActiveAlias': {'type': 'string', 'description': 'Currently active alias for the space'},
                            'description': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'plain': {'type': 'object'},
                                            'view': {'type': 'object'},
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Space description in various formats',
                            },
                            'icon': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'path': {'type': 'string', 'description': 'Path to the icon'},
                                            'apiDownloadLink': {'type': 'string', 'description': 'API download link for the icon'},
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Space icon information',
                            },
                            '_links': {
                                'type': 'object',
                                'description': 'Links related to the space',
                                'properties': {
                                    'webui': {'type': 'string', 'description': 'Web UI link'},
                                    'base': {'type': 'string', 'description': 'Base URL'},
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'spaces',
                        'x-airbyte-stream-name': 'space',
                        'x-airbyte-ai-hints': {
                            'summary': 'Confluence spaces organizing pages and documentation',
                            'when_to_use': 'Questions about available documentation spaces or project wikis',
                            'trigger_phrases': ['confluence space', 'wiki space', 'documentation area'],
                            'freshness': 'live',
                            'example_questions': ['What Confluence spaces are available?', 'Find the engineering wiki space'],
                            'search_strategy': 'Search by name or key',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Confluence space object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique space identifier'},
                    'key': {'type': 'string', 'description': 'Space key'},
                    'name': {'type': 'string', 'description': 'Space name'},
                    'type': {'type': 'string', 'description': 'Space type (global or personal)'},
                    'status': {'type': 'string', 'description': 'Space status (current or archived)'},
                    'authorId': {'type': 'string', 'description': 'ID of the user who created the space'},
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Timestamp when the space was created',
                    },
                    'homepageId': {'type': 'string', 'description': 'ID of the space homepage'},
                    'spaceOwnerId': {'type': 'string', 'description': 'ID of the space owner'},
                    'currentActiveAlias': {'type': 'string', 'description': 'Currently active alias for the space'},
                    'description': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'plain': {'type': 'object'},
                                    'view': {'type': 'object'},
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Space description in various formats',
                    },
                    'icon': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'path': {'type': 'string', 'description': 'Path to the icon'},
                                    'apiDownloadLink': {'type': 'string', 'description': 'API download link for the icon'},
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Space icon information',
                    },
                    '_links': {
                        'type': 'object',
                        'description': 'Links related to the space',
                        'properties': {
                            'webui': {'type': 'string', 'description': 'Web UI link'},
                            'base': {'type': 'string', 'description': 'Base URL'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'spaces',
                'x-airbyte-stream-name': 'space',
                'x-airbyte-ai-hints': {
                    'summary': 'Confluence spaces organizing pages and documentation',
                    'when_to_use': 'Questions about available documentation spaces or project wikis',
                    'trigger_phrases': ['confluence space', 'wiki space', 'documentation area'],
                    'freshness': 'live',
                    'example_questions': ['What Confluence spaces are available?', 'Find the engineering wiki space'],
                    'search_strategy': 'Search by name or key',
                },
            },
            ai_hints={
                'summary': 'Confluence spaces organizing pages and documentation',
                'when_to_use': 'Questions about available documentation spaces or project wikis',
                'trigger_phrases': ['confluence space', 'wiki space', 'documentation area'],
                'freshness': 'live',
                'example_questions': ['What Confluence spaces are available?', 'Find the engineering wiki space'],
                'search_strategy': 'Search by name or key',
            },
        ),
        EntityDefinition(
            name='pages',
            stream_name='pages',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/wiki/api/v2/pages',
                    action=Action.LIST,
                    description='Returns all pages. Only pages that the user has permission to view will be returned.',
                    query_params=[
                        'cursor',
                        'limit',
                        'space-id',
                        'title',
                        'status',
                        'sort',
                        'body-format',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'space-id': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                        },
                        'title': {'type': 'string', 'required': False},
                        'status': {
                            'type': 'array',
                            'required': False,
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'current',
                                    'archived',
                                    'trashed',
                                    'draft',
                                ],
                            },
                        },
                        'sort': {
                            'type': 'string',
                            'required': False,
                            'enum': [
                                'id',
                                '-id',
                                'title',
                                '-title',
                                'created-date',
                                '-created-date',
                                'modified-date',
                                '-modified-date',
                            ],
                        },
                        'body-format': {
                            'type': 'string',
                            'required': False,
                            'enum': ['storage', 'atlas_doc_format', 'view'],
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of pages',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Confluence page object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique page identifier'},
                                        'status': {'type': 'string', 'description': 'Page status (current, archived, trashed, draft)'},
                                        'title': {'type': 'string', 'description': 'Page title'},
                                        'spaceId': {'type': 'string', 'description': 'ID of the space containing this page'},
                                        'parentId': {
                                            'oneOf': [
                                                {'type': 'string'},
                                                {'type': 'null'},
                                            ],
                                            'description': 'ID of the parent page',
                                        },
                                        'parentType': {
                                            'oneOf': [
                                                {'type': 'string'},
                                                {'type': 'null'},
                                            ],
                                            'description': 'Type of the parent (page or space)',
                                        },
                                        'position': {'type': 'integer', 'description': 'Position of the page among siblings'},
                                        'authorId': {'type': 'string', 'description': 'ID of the user who created the page'},
                                        'ownerId': {'type': 'string', 'description': 'ID of the current page owner'},
                                        'lastOwnerId': {
                                            'oneOf': [
                                                {'type': 'string'},
                                                {'type': 'null'},
                                            ],
                                            'description': 'ID of the previous page owner',
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Timestamp when the page was created',
                                        },
                                        'version': {
                                            'type': 'object',
                                            'description': 'Version information',
                                            'properties': {
                                                'createdAt': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Version creation timestamp',
                                                },
                                                'message': {'type': 'string', 'description': 'Version message'},
                                                'number': {'type': 'integer', 'description': 'Version number'},
                                                'minorEdit': {'type': 'boolean', 'description': 'Whether this was a minor edit'},
                                                'authorId': {'type': 'string', 'description': 'ID of the version author'},
                                                'ncsStepVersion': {
                                                    'oneOf': [
                                                        {'type': 'string'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'NCS step version',
                                                },
                                            },
                                        },
                                        'body': {
                                            'type': 'object',
                                            'description': 'Page body content',
                                            'properties': {
                                                'storage': {'type': 'object', 'description': 'Storage format body'},
                                                'atlas_doc_format': {'type': 'object', 'description': 'Atlas doc format body'},
                                            },
                                        },
                                        '_links': {
                                            'type': 'object',
                                            'description': 'Links related to the page',
                                            'properties': {
                                                'webui': {'type': 'string', 'description': 'Web UI link'},
                                                'editui': {'type': 'string', 'description': 'Edit UI link'},
                                                'edituiv2': {'type': 'string', 'description': 'Edit UI v2 link'},
                                                'tinyui': {'type': 'string', 'description': 'Tiny UI link'},
                                                'base': {'type': 'string', 'description': 'Base URL'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'pages',
                                    'x-airbyte-stream-name': 'pages',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Confluence pages with titles, content, and version history',
                                        'when_to_use': 'Looking for documentation, wiki pages, or internal knowledge',
                                        'trigger_phrases': [
                                            'confluence page',
                                            'wiki page',
                                            'documentation',
                                            'internal doc',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Find the Confluence page about onboarding', 'What docs are in the engineering space?'],
                                        'search_strategy': 'Search by title across spaces for best results',
                                    },
                                },
                            },
                            '_links': {
                                'type': 'object',
                                'properties': {
                                    'next': {'type': 'string', 'description': 'URL for the next page of results'},
                                    'base': {'type': 'string', 'description': 'Base URL'},
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next': '$._links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/wiki/api/v2/pages/{id}',
                    action=Action.GET,
                    description='Returns a specific page.',
                    query_params=['body-format', 'version'],
                    query_params_schema={
                        'body-format': {
                            'type': 'string',
                            'required': False,
                            'enum': ['storage', 'atlas_doc_format', 'view'],
                        },
                        'version': {'type': 'integer', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Confluence page object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique page identifier'},
                            'status': {'type': 'string', 'description': 'Page status (current, archived, trashed, draft)'},
                            'title': {'type': 'string', 'description': 'Page title'},
                            'spaceId': {'type': 'string', 'description': 'ID of the space containing this page'},
                            'parentId': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                                'description': 'ID of the parent page',
                            },
                            'parentType': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                                'description': 'Type of the parent (page or space)',
                            },
                            'position': {'type': 'integer', 'description': 'Position of the page among siblings'},
                            'authorId': {'type': 'string', 'description': 'ID of the user who created the page'},
                            'ownerId': {'type': 'string', 'description': 'ID of the current page owner'},
                            'lastOwnerId': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                                'description': 'ID of the previous page owner',
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Timestamp when the page was created',
                            },
                            'version': {
                                'type': 'object',
                                'description': 'Version information',
                                'properties': {
                                    'createdAt': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Version creation timestamp',
                                    },
                                    'message': {'type': 'string', 'description': 'Version message'},
                                    'number': {'type': 'integer', 'description': 'Version number'},
                                    'minorEdit': {'type': 'boolean', 'description': 'Whether this was a minor edit'},
                                    'authorId': {'type': 'string', 'description': 'ID of the version author'},
                                    'ncsStepVersion': {
                                        'oneOf': [
                                            {'type': 'string'},
                                            {'type': 'null'},
                                        ],
                                        'description': 'NCS step version',
                                    },
                                },
                            },
                            'body': {
                                'type': 'object',
                                'description': 'Page body content',
                                'properties': {
                                    'storage': {'type': 'object', 'description': 'Storage format body'},
                                    'atlas_doc_format': {'type': 'object', 'description': 'Atlas doc format body'},
                                },
                            },
                            '_links': {
                                'type': 'object',
                                'description': 'Links related to the page',
                                'properties': {
                                    'webui': {'type': 'string', 'description': 'Web UI link'},
                                    'editui': {'type': 'string', 'description': 'Edit UI link'},
                                    'edituiv2': {'type': 'string', 'description': 'Edit UI v2 link'},
                                    'tinyui': {'type': 'string', 'description': 'Tiny UI link'},
                                    'base': {'type': 'string', 'description': 'Base URL'},
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'pages',
                        'x-airbyte-stream-name': 'pages',
                        'x-airbyte-ai-hints': {
                            'summary': 'Confluence pages with titles, content, and version history',
                            'when_to_use': 'Looking for documentation, wiki pages, or internal knowledge',
                            'trigger_phrases': [
                                'confluence page',
                                'wiki page',
                                'documentation',
                                'internal doc',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find the Confluence page about onboarding', 'What docs are in the engineering space?'],
                            'search_strategy': 'Search by title across spaces for best results',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Confluence page object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique page identifier'},
                    'status': {'type': 'string', 'description': 'Page status (current, archived, trashed, draft)'},
                    'title': {'type': 'string', 'description': 'Page title'},
                    'spaceId': {'type': 'string', 'description': 'ID of the space containing this page'},
                    'parentId': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'null'},
                        ],
                        'description': 'ID of the parent page',
                    },
                    'parentType': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'null'},
                        ],
                        'description': 'Type of the parent (page or space)',
                    },
                    'position': {'type': 'integer', 'description': 'Position of the page among siblings'},
                    'authorId': {'type': 'string', 'description': 'ID of the user who created the page'},
                    'ownerId': {'type': 'string', 'description': 'ID of the current page owner'},
                    'lastOwnerId': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'null'},
                        ],
                        'description': 'ID of the previous page owner',
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Timestamp when the page was created',
                    },
                    'version': {
                        'type': 'object',
                        'description': 'Version information',
                        'properties': {
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Version creation timestamp',
                            },
                            'message': {'type': 'string', 'description': 'Version message'},
                            'number': {'type': 'integer', 'description': 'Version number'},
                            'minorEdit': {'type': 'boolean', 'description': 'Whether this was a minor edit'},
                            'authorId': {'type': 'string', 'description': 'ID of the version author'},
                            'ncsStepVersion': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                                'description': 'NCS step version',
                            },
                        },
                    },
                    'body': {
                        'type': 'object',
                        'description': 'Page body content',
                        'properties': {
                            'storage': {'type': 'object', 'description': 'Storage format body'},
                            'atlas_doc_format': {'type': 'object', 'description': 'Atlas doc format body'},
                        },
                    },
                    '_links': {
                        'type': 'object',
                        'description': 'Links related to the page',
                        'properties': {
                            'webui': {'type': 'string', 'description': 'Web UI link'},
                            'editui': {'type': 'string', 'description': 'Edit UI link'},
                            'edituiv2': {'type': 'string', 'description': 'Edit UI v2 link'},
                            'tinyui': {'type': 'string', 'description': 'Tiny UI link'},
                            'base': {'type': 'string', 'description': 'Base URL'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'pages',
                'x-airbyte-stream-name': 'pages',
                'x-airbyte-ai-hints': {
                    'summary': 'Confluence pages with titles, content, and version history',
                    'when_to_use': 'Looking for documentation, wiki pages, or internal knowledge',
                    'trigger_phrases': [
                        'confluence page',
                        'wiki page',
                        'documentation',
                        'internal doc',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Find the Confluence page about onboarding', 'What docs are in the engineering space?'],
                    'search_strategy': 'Search by title across spaces for best results',
                },
            },
            ai_hints={
                'summary': 'Confluence pages with titles, content, and version history',
                'when_to_use': 'Looking for documentation, wiki pages, or internal knowledge',
                'trigger_phrases': [
                    'confluence page',
                    'wiki page',
                    'documentation',
                    'internal doc',
                ],
                'freshness': 'live',
                'example_questions': ['Find the Confluence page about onboarding', 'What docs are in the engineering space?'],
                'search_strategy': 'Search by title across spaces for best results',
            },
        ),
        EntityDefinition(
            name='blog_posts',
            stream_name='blog_posts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/wiki/api/v2/blogposts',
                    action=Action.LIST,
                    description='Returns all blog posts. Only blog posts that the user has permission to view will be returned.',
                    query_params=[
                        'cursor',
                        'limit',
                        'space-id',
                        'title',
                        'status',
                        'sort',
                        'body-format',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'space-id': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                        },
                        'title': {'type': 'string', 'required': False},
                        'status': {
                            'type': 'array',
                            'required': False,
                            'items': {
                                'type': 'string',
                                'enum': ['current', 'draft', 'trashed'],
                            },
                        },
                        'sort': {
                            'type': 'string',
                            'required': False,
                            'enum': [
                                'id',
                                '-id',
                                'title',
                                '-title',
                                'created-date',
                                '-created-date',
                                'modified-date',
                                '-modified-date',
                            ],
                        },
                        'body-format': {
                            'type': 'string',
                            'required': False,
                            'enum': ['storage', 'atlas_doc_format', 'view'],
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of blog posts',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Confluence blog post object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique blog post identifier'},
                                        'status': {'type': 'string', 'description': 'Blog post status (current, draft, trashed)'},
                                        'title': {'type': 'string', 'description': 'Blog post title'},
                                        'spaceId': {'type': 'string', 'description': 'ID of the space containing this blog post'},
                                        'authorId': {'type': 'string', 'description': 'ID of the user who created the blog post'},
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Timestamp when the blog post was created',
                                        },
                                        'version': {
                                            'type': 'object',
                                            'description': 'Version information',
                                            'properties': {
                                                'createdAt': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Version creation timestamp',
                                                },
                                                'message': {'type': 'string', 'description': 'Version message'},
                                                'number': {'type': 'integer', 'description': 'Version number'},
                                                'minorEdit': {'type': 'boolean', 'description': 'Whether this was a minor edit'},
                                                'authorId': {'type': 'string', 'description': 'ID of the version author'},
                                                'ncsStepVersion': {
                                                    'oneOf': [
                                                        {'type': 'string'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'NCS step version',
                                                },
                                            },
                                        },
                                        'body': {
                                            'type': 'object',
                                            'description': 'Blog post body content',
                                            'properties': {
                                                'storage': {'type': 'object', 'description': 'Storage format body'},
                                                'atlas_doc_format': {'type': 'object', 'description': 'Atlas doc format body'},
                                            },
                                        },
                                        '_links': {
                                            'type': 'object',
                                            'description': 'Links related to the blog post',
                                            'properties': {
                                                'webui': {'type': 'string', 'description': 'Web UI link'},
                                                'editui': {'type': 'string', 'description': 'Edit UI link'},
                                                'edituiv2': {'type': 'string', 'description': 'Edit UI v2 link'},
                                                'tinyui': {'type': 'string', 'description': 'Tiny UI link'},
                                                'base': {'type': 'string', 'description': 'Base URL'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'blog_posts',
                                    'x-airbyte-stream-name': 'blog_posts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Blog posts published in Confluence spaces',
                                        'when_to_use': 'Looking for team blog posts, announcements, or updates',
                                        'trigger_phrases': ['confluence blog', 'blog post', 'team announcement'],
                                        'freshness': 'live',
                                        'example_questions': ['Show recent Confluence blog posts'],
                                        'search_strategy': 'Search by title or filter by space and date',
                                    },
                                },
                            },
                            '_links': {
                                'type': 'object',
                                'properties': {
                                    'next': {'type': 'string', 'description': 'URL for the next page of results'},
                                    'base': {'type': 'string', 'description': 'Base URL'},
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next': '$._links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/wiki/api/v2/blogposts/{id}',
                    action=Action.GET,
                    description='Returns a specific blog post.',
                    query_params=['body-format', 'version'],
                    query_params_schema={
                        'body-format': {
                            'type': 'string',
                            'required': False,
                            'enum': ['storage', 'atlas_doc_format', 'view'],
                        },
                        'version': {'type': 'integer', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Confluence blog post object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique blog post identifier'},
                            'status': {'type': 'string', 'description': 'Blog post status (current, draft, trashed)'},
                            'title': {'type': 'string', 'description': 'Blog post title'},
                            'spaceId': {'type': 'string', 'description': 'ID of the space containing this blog post'},
                            'authorId': {'type': 'string', 'description': 'ID of the user who created the blog post'},
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Timestamp when the blog post was created',
                            },
                            'version': {
                                'type': 'object',
                                'description': 'Version information',
                                'properties': {
                                    'createdAt': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Version creation timestamp',
                                    },
                                    'message': {'type': 'string', 'description': 'Version message'},
                                    'number': {'type': 'integer', 'description': 'Version number'},
                                    'minorEdit': {'type': 'boolean', 'description': 'Whether this was a minor edit'},
                                    'authorId': {'type': 'string', 'description': 'ID of the version author'},
                                    'ncsStepVersion': {
                                        'oneOf': [
                                            {'type': 'string'},
                                            {'type': 'null'},
                                        ],
                                        'description': 'NCS step version',
                                    },
                                },
                            },
                            'body': {
                                'type': 'object',
                                'description': 'Blog post body content',
                                'properties': {
                                    'storage': {'type': 'object', 'description': 'Storage format body'},
                                    'atlas_doc_format': {'type': 'object', 'description': 'Atlas doc format body'},
                                },
                            },
                            '_links': {
                                'type': 'object',
                                'description': 'Links related to the blog post',
                                'properties': {
                                    'webui': {'type': 'string', 'description': 'Web UI link'},
                                    'editui': {'type': 'string', 'description': 'Edit UI link'},
                                    'edituiv2': {'type': 'string', 'description': 'Edit UI v2 link'},
                                    'tinyui': {'type': 'string', 'description': 'Tiny UI link'},
                                    'base': {'type': 'string', 'description': 'Base URL'},
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'blog_posts',
                        'x-airbyte-stream-name': 'blog_posts',
                        'x-airbyte-ai-hints': {
                            'summary': 'Blog posts published in Confluence spaces',
                            'when_to_use': 'Looking for team blog posts, announcements, or updates',
                            'trigger_phrases': ['confluence blog', 'blog post', 'team announcement'],
                            'freshness': 'live',
                            'example_questions': ['Show recent Confluence blog posts'],
                            'search_strategy': 'Search by title or filter by space and date',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Confluence blog post object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique blog post identifier'},
                    'status': {'type': 'string', 'description': 'Blog post status (current, draft, trashed)'},
                    'title': {'type': 'string', 'description': 'Blog post title'},
                    'spaceId': {'type': 'string', 'description': 'ID of the space containing this blog post'},
                    'authorId': {'type': 'string', 'description': 'ID of the user who created the blog post'},
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Timestamp when the blog post was created',
                    },
                    'version': {
                        'type': 'object',
                        'description': 'Version information',
                        'properties': {
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Version creation timestamp',
                            },
                            'message': {'type': 'string', 'description': 'Version message'},
                            'number': {'type': 'integer', 'description': 'Version number'},
                            'minorEdit': {'type': 'boolean', 'description': 'Whether this was a minor edit'},
                            'authorId': {'type': 'string', 'description': 'ID of the version author'},
                            'ncsStepVersion': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                                'description': 'NCS step version',
                            },
                        },
                    },
                    'body': {
                        'type': 'object',
                        'description': 'Blog post body content',
                        'properties': {
                            'storage': {'type': 'object', 'description': 'Storage format body'},
                            'atlas_doc_format': {'type': 'object', 'description': 'Atlas doc format body'},
                        },
                    },
                    '_links': {
                        'type': 'object',
                        'description': 'Links related to the blog post',
                        'properties': {
                            'webui': {'type': 'string', 'description': 'Web UI link'},
                            'editui': {'type': 'string', 'description': 'Edit UI link'},
                            'edituiv2': {'type': 'string', 'description': 'Edit UI v2 link'},
                            'tinyui': {'type': 'string', 'description': 'Tiny UI link'},
                            'base': {'type': 'string', 'description': 'Base URL'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'blog_posts',
                'x-airbyte-stream-name': 'blog_posts',
                'x-airbyte-ai-hints': {
                    'summary': 'Blog posts published in Confluence spaces',
                    'when_to_use': 'Looking for team blog posts, announcements, or updates',
                    'trigger_phrases': ['confluence blog', 'blog post', 'team announcement'],
                    'freshness': 'live',
                    'example_questions': ['Show recent Confluence blog posts'],
                    'search_strategy': 'Search by title or filter by space and date',
                },
            },
            ai_hints={
                'summary': 'Blog posts published in Confluence spaces',
                'when_to_use': 'Looking for team blog posts, announcements, or updates',
                'trigger_phrases': ['confluence blog', 'blog post', 'team announcement'],
                'freshness': 'live',
                'example_questions': ['Show recent Confluence blog posts'],
                'search_strategy': 'Search by title or filter by space and date',
            },
        ),
        EntityDefinition(
            name='groups',
            stream_name='group',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/wiki/rest/api/group',
                    action=Action.LIST,
                    description='Returns all user groups.',
                    query_params=['start', 'limit'],
                    query_params_schema={
                        'start': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                            'minimum': 0,
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 200,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of groups',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Confluence group object',
                                    'properties': {
                                        'type': {'type': 'string', 'description': 'Type of the group'},
                                        'id': {'type': 'string', 'description': 'Unique group identifier'},
                                        'name': {'type': 'string', 'description': 'Group name'},
                                        'managedBy': {'type': 'string', 'description': 'Entity managing this group'},
                                        'usageType': {'type': 'string', 'description': 'Usage type of the group'},
                                        'resourceAri': {'type': 'string', 'description': 'Atlassian Resource Identifier for the group'},
                                        '_links': {
                                            'type': 'object',
                                            'description': 'Links related to the group',
                                            'properties': {
                                                'self': {'type': 'string', 'description': 'Self link'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'groups',
                                    'x-airbyte-stream-name': 'group',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'User groups in Confluence for permission management',
                                        'when_to_use': 'Questions about user groups or access permissions',
                                        'trigger_phrases': ['confluence group', 'user group', 'permissions group'],
                                        'freshness': 'static',
                                        'example_questions': ['What user groups exist in Confluence?'],
                                        'search_strategy': 'Search by group name',
                                    },
                                },
                            },
                            'start': {'type': 'integer', 'description': 'Starting index'},
                            'limit': {'type': 'integer', 'description': 'Number of results per page'},
                            'size': {'type': 'integer', 'description': 'Number of results returned'},
                            '_links': {
                                'type': 'object',
                                'properties': {
                                    'base': {'type': 'string'},
                                    'context': {'type': 'string'},
                                    'next': {'type': 'string'},
                                    'self': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={
                        'next': '$._links.next',
                        'start': '$.start',
                        'limit': '$.limit',
                        'size': '$.size',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Confluence group object',
                'properties': {
                    'type': {'type': 'string', 'description': 'Type of the group'},
                    'id': {'type': 'string', 'description': 'Unique group identifier'},
                    'name': {'type': 'string', 'description': 'Group name'},
                    'managedBy': {'type': 'string', 'description': 'Entity managing this group'},
                    'usageType': {'type': 'string', 'description': 'Usage type of the group'},
                    'resourceAri': {'type': 'string', 'description': 'Atlassian Resource Identifier for the group'},
                    '_links': {
                        'type': 'object',
                        'description': 'Links related to the group',
                        'properties': {
                            'self': {'type': 'string', 'description': 'Self link'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'groups',
                'x-airbyte-stream-name': 'group',
                'x-airbyte-ai-hints': {
                    'summary': 'User groups in Confluence for permission management',
                    'when_to_use': 'Questions about user groups or access permissions',
                    'trigger_phrases': ['confluence group', 'user group', 'permissions group'],
                    'freshness': 'static',
                    'example_questions': ['What user groups exist in Confluence?'],
                    'search_strategy': 'Search by group name',
                },
            },
            ai_hints={
                'summary': 'User groups in Confluence for permission management',
                'when_to_use': 'Questions about user groups or access permissions',
                'trigger_phrases': ['confluence group', 'user group', 'permissions group'],
                'freshness': 'static',
                'example_questions': ['What user groups exist in Confluence?'],
                'search_strategy': 'Search by group name',
            },
        ),
        EntityDefinition(
            name='audit',
            stream_name='audit',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/wiki/rest/api/audit',
                    action=Action.LIST,
                    description='Returns audit log records.',
                    query_params=[
                        'start',
                        'limit',
                        'startDate',
                        'endDate',
                        'searchString',
                    ],
                    query_params_schema={
                        'start': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                            'minimum': 0,
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 1000,
                        },
                        'startDate': {'type': 'string', 'required': False},
                        'endDate': {'type': 'string', 'required': False},
                        'searchString': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of audit records',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Confluence audit record',
                                    'properties': {
                                        'author': {
                                            'type': 'object',
                                            'description': 'User who triggered the audit event',
                                            'properties': {
                                                'type': {'type': 'string', 'description': 'Author type'},
                                                'displayName': {'type': 'string', 'description': 'Display name of the author'},
                                                'publicName': {'type': 'string', 'description': 'Public name of the author'},
                                                'accountType': {'type': 'string', 'description': 'Account type'},
                                                'isExternalCollaborator': {'type': 'boolean', 'description': 'Whether the author is an external collaborator'},
                                                'externalCollaborator': {'type': 'boolean', 'description': 'Whether the author is an external collaborator'},
                                                'operations': {
                                                    'oneOf': [
                                                        {'type': 'object'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Operations available for the author',
                                                },
                                            },
                                        },
                                        'remoteAddress': {'type': 'string', 'description': 'IP address from which the event originated'},
                                        'creationDate': {'type': 'integer', 'description': 'Timestamp of the audit event'},
                                        'summary': {'type': 'string', 'description': 'Brief summary of the audit event'},
                                        'description': {'type': 'string', 'description': 'Detailed description of the audit event'},
                                        'category': {'type': 'string', 'description': 'Category of the audit event'},
                                        'sysAdmin': {'type': 'boolean', 'description': 'Whether the user is a system admin'},
                                        'superAdmin': {'type': 'boolean', 'description': 'Whether the user is a super admin'},
                                        'affectedObject': {
                                            'type': 'object',
                                            'description': 'Object affected by the audit event',
                                            'properties': {
                                                'name': {'type': 'string', 'description': 'Name of the affected object'},
                                                'objectType': {'type': 'string', 'description': 'Type of the affected object'},
                                            },
                                        },
                                        'changedValues': {'type': 'array', 'description': 'Values changed during the audit event'},
                                        'associatedObjects': {
                                            'type': 'array',
                                            'description': 'Objects associated with the audit event',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {'type': 'string', 'description': 'Name of the associated object'},
                                                    'objectType': {'type': 'string', 'description': 'Type of the associated object'},
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'audit',
                                    'x-airbyte-stream-name': 'audit',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Audit log entries tracking actions in Confluence',
                                        'when_to_use': 'Questions about recent activity or changes in Confluence',
                                        'trigger_phrases': [
                                            'audit log',
                                            'who changed',
                                            'activity log',
                                            'recent changes',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What changes were made in Confluence recently?'],
                                        'search_strategy': 'Filter by date range or action type',
                                    },
                                },
                            },
                            'start': {'type': 'integer', 'description': 'Starting index'},
                            'limit': {'type': 'integer', 'description': 'Number of results per page'},
                            'size': {'type': 'integer', 'description': 'Number of results returned'},
                            '_links': {
                                'type': 'object',
                                'properties': {
                                    'base': {'type': 'string'},
                                    'context': {'type': 'string'},
                                    'next': {'type': 'string'},
                                    'self': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={
                        'next': '$._links.next',
                        'start': '$.start',
                        'limit': '$.limit',
                        'size': '$.size',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Confluence audit record',
                'properties': {
                    'author': {
                        'type': 'object',
                        'description': 'User who triggered the audit event',
                        'properties': {
                            'type': {'type': 'string', 'description': 'Author type'},
                            'displayName': {'type': 'string', 'description': 'Display name of the author'},
                            'publicName': {'type': 'string', 'description': 'Public name of the author'},
                            'accountType': {'type': 'string', 'description': 'Account type'},
                            'isExternalCollaborator': {'type': 'boolean', 'description': 'Whether the author is an external collaborator'},
                            'externalCollaborator': {'type': 'boolean', 'description': 'Whether the author is an external collaborator'},
                            'operations': {
                                'oneOf': [
                                    {'type': 'object'},
                                    {'type': 'null'},
                                ],
                                'description': 'Operations available for the author',
                            },
                        },
                    },
                    'remoteAddress': {'type': 'string', 'description': 'IP address from which the event originated'},
                    'creationDate': {'type': 'integer', 'description': 'Timestamp of the audit event'},
                    'summary': {'type': 'string', 'description': 'Brief summary of the audit event'},
                    'description': {'type': 'string', 'description': 'Detailed description of the audit event'},
                    'category': {'type': 'string', 'description': 'Category of the audit event'},
                    'sysAdmin': {'type': 'boolean', 'description': 'Whether the user is a system admin'},
                    'superAdmin': {'type': 'boolean', 'description': 'Whether the user is a super admin'},
                    'affectedObject': {
                        'type': 'object',
                        'description': 'Object affected by the audit event',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Name of the affected object'},
                            'objectType': {'type': 'string', 'description': 'Type of the affected object'},
                        },
                    },
                    'changedValues': {'type': 'array', 'description': 'Values changed during the audit event'},
                    'associatedObjects': {
                        'type': 'array',
                        'description': 'Objects associated with the audit event',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'name': {'type': 'string', 'description': 'Name of the associated object'},
                                'objectType': {'type': 'string', 'description': 'Type of the associated object'},
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'audit',
                'x-airbyte-stream-name': 'audit',
                'x-airbyte-ai-hints': {
                    'summary': 'Audit log entries tracking actions in Confluence',
                    'when_to_use': 'Questions about recent activity or changes in Confluence',
                    'trigger_phrases': [
                        'audit log',
                        'who changed',
                        'activity log',
                        'recent changes',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What changes were made in Confluence recently?'],
                    'search_strategy': 'Filter by date range or action type',
                },
            },
            ai_hints={
                'summary': 'Audit log entries tracking actions in Confluence',
                'when_to_use': 'Questions about recent activity or changes in Confluence',
                'trigger_phrases': [
                    'audit log',
                    'who changed',
                    'activity log',
                    'recent changes',
                ],
                'freshness': 'live',
                'example_questions': ['What changes were made in Confluence recently?'],
                'search_strategy': 'Filter by date range or action type',
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='audit',
                x_airbyte_name='audit',
                fields=[
                    CacheFieldConfig(
                        name='affectedObject',
                        type=['null', 'object'],
                        description='The object that was affected by the audit event.',
                    ),
                    CacheFieldConfig(
                        name='associatedObjects',
                        type=['null', 'array'],
                        description='Any associated objects related to the audit event.',
                    ),
                    CacheFieldConfig(
                        name='author',
                        type=['null', 'object'],
                        description='The user who triggered the audit event.',
                    ),
                    CacheFieldConfig(
                        name='category',
                        type=['null', 'string'],
                        description='The category under which the audit event falls.',
                    ),
                    CacheFieldConfig(
                        name='changedValues',
                        type=['null', 'array'],
                        description='Details of the values that were changed during the audit event.',
                    ),
                    CacheFieldConfig(
                        name='creationDate',
                        type=['null', 'integer'],
                        description='The date and time when the audit event was created.',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='A detailed description of the audit event.',
                    ),
                    CacheFieldConfig(
                        name='remoteAddress',
                        type=['null', 'string'],
                        description='The IP address from which the audit event originated.',
                    ),
                    CacheFieldConfig(
                        name='summary',
                        type=['null', 'string'],
                        description='A brief summary or title describing the audit event.',
                    ),
                    CacheFieldConfig(
                        name='superAdmin',
                        type=['null', 'boolean'],
                        description='Indicates if the user triggering the audit event is a super admin.',
                    ),
                    CacheFieldConfig(
                        name='sysAdmin',
                        type=['null', 'boolean'],
                        description='Indicates if the user triggering the audit event is a system admin.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='blog_posts',
                suggested=True,
                x_airbyte_name='blog_posts',
                fields=[
                    CacheFieldConfig(
                        name='_links',
                        type=['null', 'object'],
                        description='Links related to the blog post',
                        properties={
                            'webui': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'editui': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'tinyui': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='authorId',
                        type=['null', 'string'],
                        description='ID of the user who created the blog post',
                    ),
                    CacheFieldConfig(
                        name='body',
                        type=['null', 'object'],
                        description='Blog post body content',
                        properties={
                            'storage': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                            'atlas_doc_format': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the blog post was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique blog post identifier',
                    ),
                    CacheFieldConfig(
                        name='spaceId',
                        type=['null', 'string'],
                        description='ID of the space containing this blog post',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Blog post status (current, draft, trashed)',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Blog post title',
                    ),
                    CacheFieldConfig(
                        name='version',
                        type=['null', 'object'],
                        description='Version information',
                        properties={
                            'createdAt': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'message': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'number': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'minorEdit': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'authorId': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='groups',
                x_airbyte_name='group',
                fields=[
                    CacheFieldConfig(
                        name='_links',
                        type=['null', 'object'],
                        description='Links related to the group',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='The unique identifier of the group',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='The name of the group',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='The type of group',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='pages',
                suggested=True,
                x_airbyte_name='pages',
                fields=[
                    CacheFieldConfig(
                        name='_links',
                        type=['null', 'object'],
                        description='Links related to the page',
                        properties={
                            'webui': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'editui': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'tinyui': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='authorId',
                        type=['null', 'string'],
                        description='ID of the user who created the page',
                    ),
                    CacheFieldConfig(
                        name='body',
                        type=['null', 'object'],
                        description='Page body content',
                        properties={
                            'storage': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                            'atlas_doc_format': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the page was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique page identifier',
                    ),
                    CacheFieldConfig(
                        name='lastOwnerId',
                        type=['null', 'string'],
                        description='ID of the previous page owner',
                    ),
                    CacheFieldConfig(
                        name='ownerId',
                        type=['null', 'string'],
                        description='ID of the current page owner',
                    ),
                    CacheFieldConfig(
                        name='parentId',
                        type=['null', 'string'],
                        description='ID of the parent page',
                    ),
                    CacheFieldConfig(
                        name='parentType',
                        type=['null', 'string'],
                        description='Type of the parent (page or space)',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'integer'],
                        description='Position of the page among siblings',
                    ),
                    CacheFieldConfig(
                        name='spaceId',
                        type=['null', 'string'],
                        description='ID of the space containing this page',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Page status (current, archived, trashed, draft)',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Page title',
                    ),
                    CacheFieldConfig(
                        name='version',
                        type=['null', 'object'],
                        description='Version information',
                        properties={
                            'createdAt': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'message': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'number': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'minorEdit': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'authorId': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='spaces',
                suggested=True,
                x_airbyte_name='space',
                fields=[
                    CacheFieldConfig(
                        name='_links',
                        type=['null', 'object'],
                        description='Links related to the space',
                        properties={
                            'webui': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='authorId',
                        type=['null', 'string'],
                        description='ID of the user who created the space',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the space was created',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'object'],
                        description='Space description in various formats',
                        properties={
                            'plain': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                            'view': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='homepageId',
                        type=['null', 'string'],
                        description='ID of the space homepage',
                    ),
                    CacheFieldConfig(
                        name='icon',
                        type=['null', 'object'],
                        description='Space icon information',
                        properties={
                            'path': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'apiDownloadLink': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique space identifier',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['null', 'string'],
                        description='Space key',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Space name',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Space status (current or archived)',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Space type (global or personal)',
                    ),
                ],
            ),
        ],
        disable_compaction=True,
    ),
    search_field_paths={
        'audit': [
            'affectedObject',
            'associatedObjects',
            'associatedObjects[]',
            'author',
            'category',
            'changedValues',
            'changedValues[]',
            'creationDate',
            'description',
            'remoteAddress',
            'summary',
            'superAdmin',
            'sysAdmin',
        ],
        'blog_posts': [
            '_links',
            '_links.webui',
            '_links.editui',
            '_links.tinyui',
            'authorId',
            'body',
            'body.storage',
            'body.atlas_doc_format',
            'createdAt',
            'id',
            'spaceId',
            'status',
            'title',
            'version',
            'version.createdAt',
            'version.message',
            'version.number',
            'version.minorEdit',
            'version.authorId',
        ],
        'groups': [
            '_links',
            'id',
            'name',
            'type',
        ],
        'pages': [
            '_links',
            '_links.webui',
            '_links.editui',
            '_links.tinyui',
            'authorId',
            'body',
            'body.storage',
            'body.atlas_doc_format',
            'createdAt',
            'id',
            'lastOwnerId',
            'ownerId',
            'parentId',
            'parentType',
            'position',
            'spaceId',
            'status',
            'title',
            'version',
            'version.createdAt',
            'version.message',
            'version.number',
            'version.minorEdit',
            'version.authorId',
        ],
        'spaces': [
            '_links',
            '_links.webui',
            'authorId',
            'createdAt',
            'description',
            'description.plain',
            'description.view',
            'homepageId',
            'icon',
            'icon.path',
            'icon.apiDownloadLink',
            'id',
            'key',
            'name',
            'status',
            'type',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all spaces in my Confluence instance',
            'Show me the most recently created pages',
            'List all blog posts',
            'Show me details for a specific page',
            'List all groups in Confluence',
            'Show me recent audit log entries',
            'Get details about a specific space',
            'Show me blog post details',
        ],
        context_store_search=[
            'Find pages created in the last 7 days',
            'What spaces have the most pages?',
            'Show me all pages in a specific space',
            'Find blog posts by a specific author',
            'What audit events happened this week?',
        ],
        search=[
            'Find pages created in the last 7 days',
            'What spaces have the most pages?',
            'Show me all pages in a specific space',
            'Find blog posts by a specific author',
            'What audit events happened this week?',
        ],
        unsupported=[
            'Create a new page in Confluence',
            'Update an existing page',
            'Delete a space',
            'Upload an attachment to a page',
            'Manage space permissions',
        ],
    ),
    server_variable_defaults={'subdomain': '{subdomain}'},
)