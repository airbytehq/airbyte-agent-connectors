"""
Connector model for monday.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""

from __future__ import annotations

from ._vendored.connector_sdk.types import (
    Action,
    AuthConfig,
    AuthOption,
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

MondayConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('80a54ea2-9959-4040-aac1-eee42423ec9b'),
    name='monday',
    version='1.0.1',
    base_url='https://api.monday.com',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='mondayOAuth',
                type=AuthType.OAUTH2,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'refresh_url': 'https://auth.monday.com/oauth2/token',
                },
                user_config_spec=AirbyteAuthConfig(
                    title='OAuth 2.0 Authentication',
                    type='object',
                    required=['access_token', 'client_id', 'client_secret'],
                    properties={
                        'access_token': AuthConfigFieldSpec(
                            title='Access Token',
                            description='Access token obtained via OAuth 2.0 flow',
                        ),
                        'client_id': AuthConfigFieldSpec(
                            title='Client ID',
                            description='The Client ID of your Monday.com OAuth application',
                        ),
                        'client_secret': AuthConfigFieldSpec(
                            title='Client Secret',
                            description='The Client Secret of your Monday.com OAuth application',
                        ),
                    },
                    auth_mapping={
                        'access_token': '${access_token}',
                        'client_id': '${client_id}',
                        'client_secret': '${client_secret}',
                    },
                    replication_auth_key_mapping={
                        'credentials.access_token': 'access_token',
                        'credentials.client_id': 'client_id',
                        'credentials.client_secret': 'client_secret',
                    },
                    replication_auth_key_constants={'credentials.auth_type': 'oauth2.0'},
                ),
            ),
            AuthOption(
                scheme_name='mondayApiToken',
                type=AuthType.BEARER,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AirbyteAuthConfig(
                    title='API Token Authentication',
                    type='object',
                    required=['api_key'],
                    properties={
                        'api_key': AuthConfigFieldSpec(
                            title='API Token',
                            description='Your Monday.com personal API token',
                        ),
                    },
                    auth_mapping={'token': '${api_key}'},
                    replication_auth_key_mapping={'credentials.api_token': 'api_key'},
                    replication_auth_key_constants={'credentials.auth_type': 'api_token'},
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
                    method='POST',
                    path='/graphql:users:list',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.LIST,
                    description='Returns all users in the Monday.com account',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'users': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com user object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique user identifier',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's display name",
                                                },
                                                'email': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's email address",
                                                },
                                                'enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user account is enabled',
                                                },
                                                'birthday': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's birthday",
                                                },
                                                'country_code': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's country code",
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the user was created',
                                                },
                                                'join_date': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the user joined',
                                                },
                                                'is_admin': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user is an admin',
                                                },
                                                'is_guest': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user is a guest',
                                                },
                                                'is_pending': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user is pending',
                                                },
                                                'is_view_only': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user is view-only',
                                                },
                                                'is_verified': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user is verified',
                                                },
                                                'location': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's location",
                                                },
                                                'mobile_phone': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's mobile phone number",
                                                },
                                                'phone': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's phone number",
                                                },
                                                'photo_original': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to original size photo',
                                                },
                                                'photo_small': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to small photo',
                                                },
                                                'photo_thumb': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to thumbnail photo',
                                                },
                                                'photo_thumb_small': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to small thumbnail photo',
                                                },
                                                'photo_tiny': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to tiny photo',
                                                },
                                                'time_zone_identifier': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's timezone identifier",
                                                },
                                                'title': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's job title",
                                                },
                                                'url': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's Monday.com profile URL",
                                                },
                                                'utc_hours_diff': {
                                                    'type': ['null', 'integer'],
                                                    'description': "UTC hours difference for the user's timezone",
                                                },
                                            },
                                            'x-airbyte-entity-name': 'users',
                                            'x-airbyte-stream-name': 'users',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={'type': 'graphql', 'query': 'query {\n  users {\n    id\n    name\n    email\n    enabled\n    birthday\n    country_code\n    created_at\n    join_date\n    is_admin\n    is_guest\n    is_pending\n    is_view_only\n    is_verified\n    location\n    mobile_phone\n    phone\n    photo_original\n    photo_small\n    photo_thumb\n    photo_thumb_small\n    photo_tiny\n    time_zone_identifier\n    title\n    url\n    utc_hours_diff\n  }\n}\n'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:users:get',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.GET,
                    description='Returns a single user by ID',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'users': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com user object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique user identifier',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's display name",
                                                },
                                                'email': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's email address",
                                                },
                                                'enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user account is enabled',
                                                },
                                                'birthday': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's birthday",
                                                },
                                                'country_code': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's country code",
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the user was created',
                                                },
                                                'join_date': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the user joined',
                                                },
                                                'is_admin': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user is an admin',
                                                },
                                                'is_guest': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user is a guest',
                                                },
                                                'is_pending': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user is pending',
                                                },
                                                'is_view_only': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user is view-only',
                                                },
                                                'is_verified': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Whether the user is verified',
                                                },
                                                'location': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's location",
                                                },
                                                'mobile_phone': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's mobile phone number",
                                                },
                                                'phone': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's phone number",
                                                },
                                                'photo_original': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to original size photo',
                                                },
                                                'photo_small': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to small photo',
                                                },
                                                'photo_thumb': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to thumbnail photo',
                                                },
                                                'photo_thumb_small': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to small thumbnail photo',
                                                },
                                                'photo_tiny': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to tiny photo',
                                                },
                                                'time_zone_identifier': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's timezone identifier",
                                                },
                                                'title': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's job title",
                                                },
                                                'url': {
                                                    'type': ['null', 'string'],
                                                    'description': "User's Monday.com profile URL",
                                                },
                                                'utc_hours_diff': {
                                                    'type': ['null', 'integer'],
                                                    'description': "UTC hours difference for the user's timezone",
                                                },
                                            },
                                            'x-airbyte-entity-name': 'users',
                                            'x-airbyte-stream-name': 'users',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($ids: [ID!]) {\n  users(ids: $ids) {\n    id\n    name\n    email\n    enabled\n    birthday\n    country_code\n    created_at\n    join_date\n    is_admin\n    is_guest\n    is_pending\n    is_view_only\n    is_verified\n    location\n    mobile_phone\n    phone\n    photo_original\n    photo_small\n    photo_thumb\n    photo_thumb_small\n    photo_tiny\n    time_zone_identifier\n    title\n    url\n    utc_hours_diff\n  }\n}\n',
                        'variables': {'ids': '{{ id }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Monday.com user object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique user identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': "User's display name",
                    },
                    'email': {
                        'type': ['null', 'string'],
                        'description': "User's email address",
                    },
                    'enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user account is enabled',
                    },
                    'birthday': {
                        'type': ['null', 'string'],
                        'description': "User's birthday",
                    },
                    'country_code': {
                        'type': ['null', 'string'],
                        'description': "User's country code",
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the user was created',
                    },
                    'join_date': {
                        'type': ['null', 'string'],
                        'description': 'When the user joined',
                    },
                    'is_admin': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user is an admin',
                    },
                    'is_guest': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user is a guest',
                    },
                    'is_pending': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user is pending',
                    },
                    'is_view_only': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user is view-only',
                    },
                    'is_verified': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user is verified',
                    },
                    'location': {
                        'type': ['null', 'string'],
                        'description': "User's location",
                    },
                    'mobile_phone': {
                        'type': ['null', 'string'],
                        'description': "User's mobile phone number",
                    },
                    'phone': {
                        'type': ['null', 'string'],
                        'description': "User's phone number",
                    },
                    'photo_original': {
                        'type': ['null', 'string'],
                        'description': 'URL to original size photo',
                    },
                    'photo_small': {
                        'type': ['null', 'string'],
                        'description': 'URL to small photo',
                    },
                    'photo_thumb': {
                        'type': ['null', 'string'],
                        'description': 'URL to thumbnail photo',
                    },
                    'photo_thumb_small': {
                        'type': ['null', 'string'],
                        'description': 'URL to small thumbnail photo',
                    },
                    'photo_tiny': {
                        'type': ['null', 'string'],
                        'description': 'URL to tiny photo',
                    },
                    'time_zone_identifier': {
                        'type': ['null', 'string'],
                        'description': "User's timezone identifier",
                    },
                    'title': {
                        'type': ['null', 'string'],
                        'description': "User's job title",
                    },
                    'url': {
                        'type': ['null', 'string'],
                        'description': "User's Monday.com profile URL",
                    },
                    'utc_hours_diff': {
                        'type': ['null', 'integer'],
                        'description': "UTC hours difference for the user's timezone",
                    },
                },
                'x-airbyte-entity-name': 'users',
                'x-airbyte-stream-name': 'users',
            },
        ),
        EntityDefinition(
            name='boards',
            stream_name='boards',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:boards:list',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.LIST,
                    description='Returns all boards in the Monday.com account',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'boards': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com board object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique board identifier',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board name',
                                                },
                                                'board_kind': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board kind (public, private, share)',
                                                },
                                                'type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board type',
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board description',
                                                },
                                                'permissions': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board permissions',
                                                },
                                                'state': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board state (active, archived, deleted)',
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the board was last updated',
                                                },
                                                'columns': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board columns',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'archived': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'description': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'settings_str': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'title': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'width': {
                                                                'type': ['null', 'integer'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'groups': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board groups',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'archived': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'color': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'deleted': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'position': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'title': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'owners': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board owners',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'creator': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Board creator',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'tags': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board tags',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'top_group': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Top group on the board',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'views': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board views',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'settings_str': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'view_specific_data_str': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'workspace': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Workspace the board belongs to',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'kind': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'description': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                            'x-airbyte-entity-name': 'boards',
                                            'x-airbyte-stream-name': 'boards',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($page: Int, $limit: Int) {\n  boards(page: $page, limit: $limit) {\n    id\n    name\n    board_kind\n    type\n    description\n    permissions\n    state\n    updated_at\n    columns {\n      archived\n      description\n      id\n      settings_str\n      title\n      type\n      width\n    }\n    groups {\n      archived\n      color\n      deleted\n      id\n      position\n      title\n    }\n    owners {\n      id\n    }\n    creator {\n      id\n    }\n    subscribers {\n      id\n    }\n    tags {\n      id\n    }\n    top_group {\n      id\n    }\n    views {\n      id\n      name\n      settings_str\n      type\n      view_specific_data_str\n    }\n    workspace {\n      id\n      name\n      kind\n      description\n    }\n  }\n}\n',
                        'variables': {'page': '{{ page }}', 'limit': '{{ limit }}'},
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:boards:get',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.GET,
                    description='Returns a single board by ID',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'boards': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com board object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique board identifier',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board name',
                                                },
                                                'board_kind': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board kind (public, private, share)',
                                                },
                                                'type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board type',
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board description',
                                                },
                                                'permissions': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board permissions',
                                                },
                                                'state': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Board state (active, archived, deleted)',
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the board was last updated',
                                                },
                                                'columns': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board columns',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'archived': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'description': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'settings_str': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'title': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'width': {
                                                                'type': ['null', 'integer'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'groups': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board groups',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'archived': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'color': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'deleted': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'position': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'title': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'owners': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board owners',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'creator': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Board creator',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'tags': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board tags',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'top_group': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Top group on the board',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'views': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Board views',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'settings_str': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'view_specific_data_str': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'workspace': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Workspace the board belongs to',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'kind': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'description': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                            'x-airbyte-entity-name': 'boards',
                                            'x-airbyte-stream-name': 'boards',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($ids: [ID!]) {\n  boards(ids: $ids) {\n    id\n    name\n    board_kind\n    type\n    description\n    permissions\n    state\n    updated_at\n    columns {\n      archived\n      description\n      id\n      settings_str\n      title\n      type\n      width\n    }\n    groups {\n      archived\n      color\n      deleted\n      id\n      position\n      title\n    }\n    owners {\n      id\n    }\n    creator {\n      id\n    }\n    subscribers {\n      id\n    }\n    tags {\n      id\n    }\n    top_group {\n      id\n    }\n    views {\n      id\n      name\n      settings_str\n      type\n      view_specific_data_str\n    }\n    workspace {\n      id\n      name\n      kind\n      description\n    }\n  }\n}\n',
                        'variables': {'ids': '{{ id }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Monday.com board object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique board identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Board name',
                    },
                    'board_kind': {
                        'type': ['null', 'string'],
                        'description': 'Board kind (public, private, share)',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Board type',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Board description',
                    },
                    'permissions': {
                        'type': ['null', 'string'],
                        'description': 'Board permissions',
                    },
                    'state': {
                        'type': ['null', 'string'],
                        'description': 'Board state (active, archived, deleted)',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the board was last updated',
                    },
                    'columns': {
                        'type': ['null', 'array'],
                        'description': 'Board columns',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'archived': {
                                    'type': ['null', 'boolean'],
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                },
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'settings_str': {
                                    'type': ['null', 'string'],
                                },
                                'title': {
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'width': {
                                    'type': ['null', 'integer'],
                                },
                            },
                        },
                    },
                    'groups': {
                        'type': ['null', 'array'],
                        'description': 'Board groups',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'archived': {
                                    'type': ['null', 'boolean'],
                                },
                                'color': {
                                    'type': ['null', 'string'],
                                },
                                'deleted': {
                                    'type': ['null', 'boolean'],
                                },
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'position': {
                                    'type': ['null', 'string'],
                                },
                                'title': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'owners': {
                        'type': ['null', 'array'],
                        'description': 'Board owners',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'creator': {
                        'type': ['null', 'object'],
                        'description': 'Board creator',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'subscribers': {
                        'type': ['null', 'array'],
                        'description': 'Board subscribers',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'tags': {
                        'type': ['null', 'array'],
                        'description': 'Board tags',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'top_group': {
                        'type': ['null', 'object'],
                        'description': 'Top group on the board',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'views': {
                        'type': ['null', 'array'],
                        'description': 'Board views',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'settings_str': {
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'view_specific_data_str': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'workspace': {
                        'type': ['null', 'object'],
                        'description': 'Workspace the board belongs to',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                            'name': {
                                'type': ['null', 'string'],
                            },
                            'kind': {
                                'type': ['null', 'string'],
                            },
                            'description': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'boards',
                'x-airbyte-stream-name': 'boards',
            },
        ),
        EntityDefinition(
            name='items',
            stream_name='items',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:items:list',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.LIST,
                    description='Returns items from boards. Queries items through the boards endpoint using items_page for pagination.',
                    query_params=['board_id'],
                    query_params_schema={
                        'board_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'boards': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'items_page': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'items': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Monday.com item object',
                                                                'properties': {
                                                                    'id': {
                                                                        'type': ['null', 'string'],
                                                                        'description': 'Unique item identifier',
                                                                    },
                                                                    'name': {
                                                                        'type': ['null', 'string'],
                                                                        'description': 'Item name',
                                                                    },
                                                                    'created_at': {
                                                                        'type': ['null', 'string'],
                                                                        'description': 'When the item was created',
                                                                    },
                                                                    'creator_id': {
                                                                        'type': ['null', 'string'],
                                                                        'description': 'ID of the user who created the item',
                                                                    },
                                                                    'state': {
                                                                        'type': ['null', 'string'],
                                                                        'description': 'Item state (active, archived, deleted)',
                                                                    },
                                                                    'updated_at': {
                                                                        'type': ['null', 'string'],
                                                                        'description': 'When the item was last updated',
                                                                    },
                                                                    'board': {
                                                                        'type': ['null', 'object'],
                                                                        'description': 'Board the item belongs to',
                                                                        'properties': {
                                                                            'id': {
                                                                                'type': ['null', 'string'],
                                                                            },
                                                                            'name': {
                                                                                'type': ['null', 'string'],
                                                                            },
                                                                        },
                                                                    },
                                                                    'group': {
                                                                        'type': ['null', 'object'],
                                                                        'description': 'Group the item belongs to',
                                                                        'properties': {
                                                                            'id': {
                                                                                'type': ['null', 'string'],
                                                                            },
                                                                        },
                                                                    },
                                                                    'parent_item': {
                                                                        'type': ['null', 'object'],
                                                                        'description': 'Parent item (for subitems)',
                                                                        'properties': {
                                                                            'id': {
                                                                                'type': ['null', 'string'],
                                                                            },
                                                                        },
                                                                    },
                                                                    'column_values': {
                                                                        'type': ['null', 'array'],
                                                                        'description': 'Item column values',
                                                                        'items': {
                                                                            'type': ['null', 'object'],
                                                                            'properties': {
                                                                                'id': {
                                                                                    'type': ['null', 'string'],
                                                                                },
                                                                                'text': {
                                                                                    'type': ['null', 'string'],
                                                                                },
                                                                                'type': {
                                                                                    'type': ['null', 'string'],
                                                                                },
                                                                                'value': {
                                                                                    'type': ['null', 'string'],
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                    'subscribers': {
                                                                        'type': ['null', 'array'],
                                                                        'description': 'Item subscribers',
                                                                        'items': {
                                                                            'type': ['null', 'object'],
                                                                            'properties': {
                                                                                'id': {
                                                                                    'type': ['null', 'string'],
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                                'x-airbyte-entity-name': 'items',
                                                                'x-airbyte-stream-name': 'items',
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($boardId: [ID!], $limit: Int) {\n  boards(ids: $boardId) {\n    items_page(limit: $limit) {\n      items {\n        id\n        name\n        created_at\n        creator_id\n        state\n        updated_at\n        board {\n          id\n          name\n        }\n        group {\n          id\n        }\n        parent_item {\n          id\n        }\n        column_values {\n          id\n          text\n          type\n          value\n        }\n        subscribers {\n          id\n        }\n      }\n    }\n  }\n}\n',
                        'variables': {'boardId': '{{ board_id }}', 'limit': '{{ limit }}'},
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:items:get',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.GET,
                    description='Returns a single item by ID',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'items': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com item object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique item identifier',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Item name',
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the item was created',
                                                },
                                                'creator_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'ID of the user who created the item',
                                                },
                                                'state': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Item state (active, archived, deleted)',
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the item was last updated',
                                                },
                                                'board': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Board the item belongs to',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'group': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Group the item belongs to',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'parent_item': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Parent item (for subitems)',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'column_values': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Item column values',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'text': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'value': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Item subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'x-airbyte-entity-name': 'items',
                                            'x-airbyte-stream-name': 'items',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($ids: [ID!]) {\n  items(ids: $ids) {\n    id\n    name\n    created_at\n    creator_id\n    state\n    updated_at\n    board {\n      id\n      name\n    }\n    group {\n      id\n    }\n    parent_item {\n      id\n    }\n    column_values {\n      id\n      text\n      type\n      value\n    }\n    subscribers {\n      id\n    }\n  }\n}\n',
                        'variables': {'ids': '{{ id }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Monday.com item object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique item identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Item name',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the item was created',
                    },
                    'creator_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the user who created the item',
                    },
                    'state': {
                        'type': ['null', 'string'],
                        'description': 'Item state (active, archived, deleted)',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the item was last updated',
                    },
                    'board': {
                        'type': ['null', 'object'],
                        'description': 'Board the item belongs to',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                            'name': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'group': {
                        'type': ['null', 'object'],
                        'description': 'Group the item belongs to',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'parent_item': {
                        'type': ['null', 'object'],
                        'description': 'Parent item (for subitems)',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'column_values': {
                        'type': ['null', 'array'],
                        'description': 'Item column values',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'text': {
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'subscribers': {
                        'type': ['null', 'array'],
                        'description': 'Item subscribers',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'items',
                'x-airbyte-stream-name': 'items',
            },
        ),
        EntityDefinition(
            name='teams',
            stream_name='teams',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:teams:list',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.LIST,
                    description='Returns all teams in the Monday.com account',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'teams': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com team object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique team identifier',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Team name',
                                                },
                                                'picture_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Team picture URL',
                                                },
                                                'users': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Team members',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'x-airbyte-entity-name': 'teams',
                                            'x-airbyte-stream-name': 'teams',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={'type': 'graphql', 'query': 'query {\n  teams {\n    id\n    name\n    picture_url\n    users {\n      id\n    }\n  }\n}\n'},
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:teams:get',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.GET,
                    description='Returns a single team by ID',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'teams': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com team object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique team identifier',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Team name',
                                                },
                                                'picture_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Team picture URL',
                                                },
                                                'users': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Team members',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'x-airbyte-entity-name': 'teams',
                                            'x-airbyte-stream-name': 'teams',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($ids: [ID!]) {\n  teams(ids: $ids) {\n    id\n    name\n    picture_url\n    users {\n      id\n    }\n  }\n}\n',
                        'variables': {'ids': '{{ id }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Monday.com team object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique team identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Team name',
                    },
                    'picture_url': {
                        'type': ['null', 'string'],
                        'description': 'Team picture URL',
                    },
                    'users': {
                        'type': ['null', 'array'],
                        'description': 'Team members',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'teams',
                'x-airbyte-stream-name': 'teams',
            },
        ),
        EntityDefinition(
            name='tags',
            stream_name='tags',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:tags:list',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.LIST,
                    description='Returns all tags in the Monday.com account',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'tags': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com tag object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique tag identifier',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Tag name',
                                                },
                                                'color': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Tag color',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'tags',
                                            'x-airbyte-stream-name': 'tags',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={'type': 'graphql', 'query': 'query {\n  tags {\n    id\n    name\n    color\n  }\n}\n'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Monday.com tag object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique tag identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Tag name',
                    },
                    'color': {
                        'type': ['null', 'string'],
                        'description': 'Tag color',
                    },
                },
                'x-airbyte-entity-name': 'tags',
                'x-airbyte-stream-name': 'tags',
            },
        ),
        EntityDefinition(
            name='updates',
            stream_name='updates',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:updates:list',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.LIST,
                    description='Returns all updates (comments/posts) in the Monday.com account',
                    query_params=['page', 'limit'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'updates': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com update (comment/post) object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique update identifier',
                                                },
                                                'body': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Update body (HTML)',
                                                },
                                                'text_body': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Update body (plain text)',
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the update was created',
                                                },
                                                'creator_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'ID of the user who created the update',
                                                },
                                                'item_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'ID of the item this update belongs to',
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the update was last modified',
                                                },
                                                'replies': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Replies to this update',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'creator_id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'created_at': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'text_body': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'updated_at': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'body': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'assets': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Files attached to this update',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'url': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'url_thumbnail': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'public_url': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'file_extension': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'file_size': {
                                                                'type': ['null', 'integer'],
                                                            },
                                                            'created_at': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'original_geometry': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'uploaded_by': {
                                                                'type': ['null', 'object'],
                                                                'properties': {
                                                                    'id': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'x-airbyte-entity-name': 'updates',
                                            'x-airbyte-stream-name': 'updates',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($page: Int, $limit: Int) {\n  updates(page: $page, limit: $limit) {\n    id\n    body\n    text_body\n    created_at\n    creator_id\n    item_id\n    updated_at\n    replies {\n      id\n      creator_id\n      created_at\n      text_body\n      updated_at\n      body\n    }\n    assets {\n      id\n      name\n      url\n      url_thumbnail\n      public_url\n      file_extension\n      file_size\n      created_at\n      original_geometry\n      uploaded_by {\n        id\n      }\n    }\n  }\n}\n',
                        'variables': {'page': '{{ page }}', 'limit': '{{ limit }}'},
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:updates:get',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.GET,
                    description='Returns a single update by ID',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'updates': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com update (comment/post) object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique update identifier',
                                                },
                                                'body': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Update body (HTML)',
                                                },
                                                'text_body': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Update body (plain text)',
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the update was created',
                                                },
                                                'creator_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'ID of the user who created the update',
                                                },
                                                'item_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'ID of the item this update belongs to',
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the update was last modified',
                                                },
                                                'replies': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Replies to this update',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'creator_id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'created_at': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'text_body': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'updated_at': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'body': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'assets': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Files attached to this update',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'url': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'url_thumbnail': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'public_url': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'file_extension': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'file_size': {
                                                                'type': ['null', 'integer'],
                                                            },
                                                            'created_at': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'original_geometry': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'uploaded_by': {
                                                                'type': ['null', 'object'],
                                                                'properties': {
                                                                    'id': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'x-airbyte-entity-name': 'updates',
                                            'x-airbyte-stream-name': 'updates',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($ids: [ID!]) {\n  updates(ids: $ids) {\n    id\n    body\n    text_body\n    created_at\n    creator_id\n    item_id\n    updated_at\n    replies {\n      id\n      creator_id\n      created_at\n      text_body\n      updated_at\n      body\n    }\n    assets {\n      id\n      name\n      url\n      url_thumbnail\n      public_url\n      file_extension\n      file_size\n      created_at\n      original_geometry\n      uploaded_by {\n        id\n      }\n    }\n  }\n}\n',
                        'variables': {'ids': '{{ id }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Monday.com update (comment/post) object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique update identifier',
                    },
                    'body': {
                        'type': ['null', 'string'],
                        'description': 'Update body (HTML)',
                    },
                    'text_body': {
                        'type': ['null', 'string'],
                        'description': 'Update body (plain text)',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the update was created',
                    },
                    'creator_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the user who created the update',
                    },
                    'item_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the item this update belongs to',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the update was last modified',
                    },
                    'replies': {
                        'type': ['null', 'array'],
                        'description': 'Replies to this update',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'creator_id': {
                                    'type': ['null', 'string'],
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                },
                                'text_body': {
                                    'type': ['null', 'string'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                },
                                'body': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'assets': {
                        'type': ['null', 'array'],
                        'description': 'Files attached to this update',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'url': {
                                    'type': ['null', 'string'],
                                },
                                'url_thumbnail': {
                                    'type': ['null', 'string'],
                                },
                                'public_url': {
                                    'type': ['null', 'string'],
                                },
                                'file_extension': {
                                    'type': ['null', 'string'],
                                },
                                'file_size': {
                                    'type': ['null', 'integer'],
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                },
                                'original_geometry': {
                                    'type': ['null', 'string'],
                                },
                                'uploaded_by': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'updates',
                'x-airbyte-stream-name': 'updates',
            },
        ),
        EntityDefinition(
            name='workspaces',
            stream_name='workspaces',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:workspaces:list',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.LIST,
                    description='Returns all workspaces in the Monday.com account',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'workspaces': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com workspace object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique workspace identifier',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Workspace name',
                                                },
                                                'kind': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Workspace kind (open, closed)',
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Workspace description',
                                                },
                                                'state': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Workspace state',
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the workspace was created',
                                                },
                                                'account_product': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Account product info',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'kind': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'owners_subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Owner subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'settings': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Workspace settings',
                                                    'properties': {
                                                        'icon': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'color': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'image': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'team_owners_subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Team owner subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'teams_subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Team subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'users_subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'User subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'x-airbyte-entity-name': 'workspaces',
                                            'x-airbyte-stream-name': 'workspaces',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($page: Int, $limit: Int) {\n  workspaces(page: $page, limit: $limit) {\n    id\n    name\n    kind\n    description\n    state\n    created_at\n    account_product {\n      id\n      kind\n    }\n    owners_subscribers {\n      id\n    }\n    settings {\n      icon {\n        color\n        image\n      }\n    }\n    team_owners_subscribers {\n      id\n      name\n    }\n    teams_subscribers {\n      id\n      name\n    }\n    users_subscribers {\n      id\n    }\n  }\n}\n',
                        'variables': {'page': '{{ page }}', 'limit': '{{ limit }}'},
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:workspaces:get',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.GET,
                    description='Returns a single workspace by ID',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'workspaces': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Monday.com workspace object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique workspace identifier',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Workspace name',
                                                },
                                                'kind': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Workspace kind (open, closed)',
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Workspace description',
                                                },
                                                'state': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Workspace state',
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                    'description': 'When the workspace was created',
                                                },
                                                'account_product': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Account product info',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'kind': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'owners_subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Owner subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'settings': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Workspace settings',
                                                    'properties': {
                                                        'icon': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'color': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'image': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'team_owners_subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Team owner subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'teams_subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Team subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'users_subscribers': {
                                                    'type': ['null', 'array'],
                                                    'description': 'User subscribers',
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'x-airbyte-entity-name': 'workspaces',
                                            'x-airbyte-stream-name': 'workspaces',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($ids: [ID!]) {\n  workspaces(ids: $ids) {\n    id\n    name\n    kind\n    description\n    state\n    created_at\n    account_product {\n      id\n      kind\n    }\n    owners_subscribers {\n      id\n    }\n    settings {\n      icon {\n        color\n        image\n      }\n    }\n    team_owners_subscribers {\n      id\n      name\n    }\n    teams_subscribers {\n      id\n      name\n    }\n    users_subscribers {\n      id\n    }\n  }\n}\n',
                        'variables': {'ids': '{{ id }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Monday.com workspace object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique workspace identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Workspace name',
                    },
                    'kind': {
                        'type': ['null', 'string'],
                        'description': 'Workspace kind (open, closed)',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Workspace description',
                    },
                    'state': {
                        'type': ['null', 'string'],
                        'description': 'Workspace state',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the workspace was created',
                    },
                    'account_product': {
                        'type': ['null', 'object'],
                        'description': 'Account product info',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                            'kind': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'owners_subscribers': {
                        'type': ['null', 'array'],
                        'description': 'Owner subscribers',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'settings': {
                        'type': ['null', 'object'],
                        'description': 'Workspace settings',
                        'properties': {
                            'icon': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'color': {
                                        'type': ['null', 'string'],
                                    },
                                    'image': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                    },
                    'team_owners_subscribers': {
                        'type': ['null', 'array'],
                        'description': 'Team owner subscribers',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'teams_subscribers': {
                        'type': ['null', 'array'],
                        'description': 'Team subscribers',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'users_subscribers': {
                        'type': ['null', 'array'],
                        'description': 'User subscribers',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'workspaces',
                'x-airbyte-stream-name': 'workspaces',
            },
        ),
        EntityDefinition(
            name='activity_logs',
            stream_name='activity_logs',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:activity_logs:list',
                    path_override=PathOverrideConfig(
                        path='/v2',
                    ),
                    action=Action.LIST,
                    description='Returns activity logs from boards. Requires a board_id parameter.',
                    query_params=['board_id'],
                    query_params_schema={
                        'board_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'boards': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'activity_logs': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'Monday.com activity log entry',
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                                'description': 'Unique activity log identifier',
                                                            },
                                                            'event': {
                                                                'type': ['null', 'string'],
                                                                'description': 'Event type',
                                                            },
                                                            'data': {
                                                                'type': ['null', 'string'],
                                                                'description': 'Event data (JSON string)',
                                                            },
                                                            'entity': {
                                                                'type': ['null', 'string'],
                                                                'description': 'Entity type that was affected',
                                                            },
                                                            'created_at': {
                                                                'type': ['null', 'string'],
                                                                'description': 'When the activity occurred',
                                                            },
                                                            'user_id': {
                                                                'type': ['null', 'string'],
                                                                'description': 'ID of the user who performed the action',
                                                            },
                                                        },
                                                        'x-airbyte-entity-name': 'activity_logs',
                                                        'x-airbyte-stream-name': 'activity_logs',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($boardIds: [ID!]) {\n  boards(ids: $boardIds) {\n    activity_logs {\n      id\n      event\n      data\n      entity\n      created_at\n      user_id\n    }\n  }\n}\n',
                        'variables': {'boardIds': '{{ board_id }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Monday.com activity log entry',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique activity log identifier',
                    },
                    'event': {
                        'type': ['null', 'string'],
                        'description': 'Event type',
                    },
                    'data': {
                        'type': ['null', 'string'],
                        'description': 'Event data (JSON string)',
                    },
                    'entity': {
                        'type': ['null', 'string'],
                        'description': 'Entity type that was affected',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the activity occurred',
                    },
                    'user_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the user who performed the action',
                    },
                },
                'x-airbyte-entity-name': 'activity_logs',
                'x-airbyte-stream-name': 'activity_logs',
            },
        ),
    ],
    search_field_paths={
        'activity_logs': [
            'board_id',
            'created_at',
            'created_at_int',
            'data',
            'entity',
            'event',
            'id',
            'pulse_id',
            'user_id',
        ],
        'boards': [
            'board_kind',
            'columns',
            'columns[]',
            'communication',
            'creator',
            'creator.id',
            'description',
            'groups',
            'groups[]',
            'id',
            'name',
            'owners',
            'owners[]',
            'permissions',
            'state',
            'subscribers',
            'subscribers[]',
            'tags',
            'tags[]',
            'top_group',
            'top_group.id',
            'type',
            'updated_at',
            'updated_at_int',
            'updates',
            'updates[]',
            'views',
            'views[]',
            'workspace',
            'workspace.id',
            'workspace.name',
            'workspace.kind',
            'workspace.description',
        ],
        'items': [
            'assets',
            'assets[]',
            'board',
            'board.id',
            'board.name',
            'column_values',
            'column_values[]',
            'created_at',
            'creator_id',
            'group',
            'group.id',
            'id',
            'name',
            'parent_item',
            'parent_item.id',
            'state',
            'subscribers',
            'subscribers[]',
            'updated_at',
            'updated_at_int',
            'updates',
            'updates[]',
        ],
        'tags': ['color', 'id', 'name'],
        'teams': [
            'id',
            'name',
            'picture_url',
            'users',
            'users[]',
        ],
        'updates': [
            'assets',
            'assets[]',
            'body',
            'created_at',
            'creator_id',
            'id',
            'item_id',
            'replies',
            'replies[]',
            'text_body',
            'updated_at',
        ],
        'users': [
            'birthday',
            'country_code',
            'created_at',
            'email',
            'enabled',
            'id',
            'is_admin',
            'is_guest',
            'is_pending',
            'is_view_only',
            'is_verified',
            'join_date',
            'location',
            'mobile_phone',
            'name',
            'phone',
            'photo_original',
            'photo_small',
            'photo_thumb',
            'photo_thumb_small',
            'photo_tiny',
            'time_zone_identifier',
            'title',
            'url',
            'utc_hours_diff',
        ],
        'workspaces': [
            'account_product',
            'account_product.id',
            'account_product.kind',
            'created_at',
            'description',
            'id',
            'kind',
            'name',
            'owners_subscribers',
            'owners_subscribers[]',
            'settings',
            'settings.icon',
            'settings.icon.color',
            'settings.icon.image',
            'state',
            'team_owners_subscribers',
            'team_owners_subscribers[]',
            'teams_subscribers',
            'teams_subscribers[]',
            'users_subscribers',
            'users_subscribers[]',
        ],
    },
)