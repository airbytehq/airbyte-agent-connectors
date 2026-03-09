"""
Connector model for confluence.

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

ConfluenceConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('cf40a7f8-71f8-45ce-a7fa-fca053e4028c'),
    name='confluence',
    base_url='https://{subdomain}.atlassian.net',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AirbyteAuthConfig(
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
                        },
                        'type': {'type': 'string', 'required': False},
                        'status': {'type': 'string', 'required': False},
                        'keys': {'type': 'array', 'required': False},
                        'sort': {'type': 'string', 'required': False},
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
                        'description-format': {'type': 'string', 'required': False},
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
            },
        ),
        EntityDefinition(
            name='pages',
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
                        },
                        'space-id': {'type': 'array', 'required': False},
                        'title': {'type': 'string', 'required': False},
                        'status': {'type': 'array', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                        'body-format': {'type': 'string', 'required': False},
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
                        'body-format': {'type': 'string', 'required': False},
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
            },
        ),
        EntityDefinition(
            name='blog_posts',
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
                        },
                        'space-id': {'type': 'array', 'required': False},
                        'title': {'type': 'string', 'required': False},
                        'status': {'type': 'array', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                        'body-format': {'type': 'string', 'required': False},
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
                        'body-format': {'type': 'string', 'required': False},
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
            },
        ),
        EntityDefinition(
            name='groups',
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
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
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
            },
        ),
        EntityDefinition(
            name='audit',
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
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
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
            },
        ),
    ],
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
    server_variable_defaults={'subdomain': '{subdomain}'},
)