"""
Connector model for slack.

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
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
    ResponseErrorCheck,
)
from uuid import (
    UUID,
)

SlackConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('c2281cee-86f9-4a86-bb48-d23286b4c7bd'),
    name='slack',
    version='0.1.20',
    base_url='https://slack.com/api',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='bearerAuth',
                type=AuthType.BEARER,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AuthConfigSpec(
                    title='Token Authentication',
                    type='object',
                    required=['bot_key'],
                    properties={
                        'bot_key': AuthConfigFieldSpec(
                            title='Bot Key',
                            description='Your Slack Bot Key (xoxb-) or User Token (xoxp-)',
                        ),
                    },
                    auth_mapping={'token': '${bot_key}'},
                    replication_auth_key_mapping={'credentials.api_token': 'bot_key'},
                    replication_auth_key_constants={'credentials.option_title': 'API Token Credentials'},
                ),
            ),
            AuthOption(
                scheme_name='oauth2',
                type=AuthType.OAUTH2,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'refresh_url': 'https://slack.com/api/oauth.v2.access',
                },
                user_config_spec=AuthConfigSpec(
                    title='OAuth 2.0 Authentication',
                    type='object',
                    required=['access_token'],
                    properties={
                        'client_id': AuthConfigFieldSpec(
                            title='Client ID',
                            description="Your Slack App's Client ID",
                        ),
                        'client_secret': AuthConfigFieldSpec(
                            title='Client Secret',
                            description="Your Slack App's Client Secret",
                        ),
                        'access_token': AuthConfigFieldSpec(
                            title='Access Token',
                            description='OAuth access token (bot token from oauth.v2.access response)',
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
                    replication_auth_key_constants={'credentials.option_title': 'Default OAuth2.0 authorization'},
                ),
                untested=True,
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
                    path='/users.list',
                    action=Action.LIST,
                    description='Returns a list of all users in the Slack workspace',
                    query_params=['cursor', 'limit'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                            'minimum': 1,
                            'maximum': 1000,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing list of users',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'members': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Slack user object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique user identifier'},
                                        'team_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Team ID the user belongs to',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Username',
                                        },
                                        'deleted': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user has been deleted',
                                        },
                                        'color': {
                                            'type': ['string', 'null'],
                                            'description': 'User color for display',
                                        },
                                        'real_name': {
                                            'type': ['string', 'null'],
                                            'description': "User's real name",
                                        },
                                        'tz': {
                                            'type': ['string', 'null'],
                                            'description': 'Timezone identifier',
                                        },
                                        'tz_label': {
                                            'type': ['string', 'null'],
                                            'description': 'Timezone label',
                                        },
                                        'tz_offset': {
                                            'type': ['integer', 'null'],
                                            'description': 'Timezone offset in seconds',
                                        },
                                        'profile': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User profile information',
                                                    'properties': {
                                                        'title': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Job title',
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Phone number',
                                                        },
                                                        'skype': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Skype handle',
                                                        },
                                                        'real_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Real name',
                                                        },
                                                        'real_name_normalized': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Normalized real name',
                                                        },
                                                        'display_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Display name',
                                                        },
                                                        'display_name_normalized': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Normalized display name',
                                                        },
                                                        'status_text': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Status text',
                                                        },
                                                        'status_emoji': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Status emoji',
                                                        },
                                                        'status_expiration': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Status expiration timestamp',
                                                        },
                                                        'avatar_hash': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Avatar hash',
                                                        },
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'First name',
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Last name',
                                                        },
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Email address',
                                                        },
                                                        'image_24': {
                                                            'type': ['string', 'null'],
                                                            'description': '24px avatar URL',
                                                        },
                                                        'image_32': {
                                                            'type': ['string', 'null'],
                                                            'description': '32px avatar URL',
                                                        },
                                                        'image_48': {
                                                            'type': ['string', 'null'],
                                                            'description': '48px avatar URL',
                                                        },
                                                        'image_72': {
                                                            'type': ['string', 'null'],
                                                            'description': '72px avatar URL',
                                                        },
                                                        'image_192': {
                                                            'type': ['string', 'null'],
                                                            'description': '192px avatar URL',
                                                        },
                                                        'image_512': {
                                                            'type': ['string', 'null'],
                                                            'description': '512px avatar URL',
                                                        },
                                                        'team': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Team ID',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'User profile information',
                                        },
                                        'is_admin': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user is an admin',
                                        },
                                        'is_owner': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user is an owner',
                                        },
                                        'is_primary_owner': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user is the primary owner',
                                        },
                                        'is_restricted': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user is restricted',
                                        },
                                        'is_ultra_restricted': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user is ultra restricted',
                                        },
                                        'is_bot': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user is a bot',
                                        },
                                        'is_app_user': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user is an app user',
                                        },
                                        'updated': {
                                            'type': ['integer', 'null'],
                                            'description': 'Unix timestamp of last update',
                                        },
                                        'is_email_confirmed': {
                                            'type': ['boolean', 'null'],
                                            'description': "Whether the user's email is confirmed",
                                        },
                                        'who_can_share_contact_card': {
                                            'type': ['string', 'null'],
                                            'description': "Who can share the user's contact card",
                                        },
                                    },
                                    'x-airbyte-entity-name': 'users',
                                    'x-airbyte-stream-name': 'users',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Slack workspace members, their profiles, roles, and contact info',
                                        'when_to_use': 'Looking up a person in Slack by name, email, or role, or listing workspace members',
                                        'trigger_phrases': [
                                            'who is',
                                            'find user',
                                            'look up',
                                            'team members',
                                            'user list',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Who is John in Slack?', 'Find the Slack user with email alex@example.com', 'List all admins in the workspace'],
                                        'search_strategy': 'When searching for a user by name, match against all name-related fields: name (username), real_name, profile.display_name, profile.display_name_normalized, profile.real_name, profile.real_name_normalized, profile.first_name, profile.last_name, and profile.email. Use case-insensitive substring matching across all of these fields to maximize recall.',
                                    },
                                },
                            },
                            'cache_ts': {
                                'type': ['integer', 'null'],
                                'description': 'Cache timestamp',
                            },
                            'response_metadata': {
                                'type': 'object',
                                'description': 'Response metadata including pagination',
                                'properties': {
                                    'next_cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'Cursor for next page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.members',
                    meta_extractor={'next_cursor': '$.response_metadata.next_cursor'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/users.info',
                    action=Action.GET,
                    description='Get information about a single user by ID',
                    query_params=['user'],
                    query_params_schema={
                        'user': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing single user',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'user': {
                                'type': 'object',
                                'description': 'Slack user object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique user identifier'},
                                    'team_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Team ID the user belongs to',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Username',
                                    },
                                    'deleted': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the user has been deleted',
                                    },
                                    'color': {
                                        'type': ['string', 'null'],
                                        'description': 'User color for display',
                                    },
                                    'real_name': {
                                        'type': ['string', 'null'],
                                        'description': "User's real name",
                                    },
                                    'tz': {
                                        'type': ['string', 'null'],
                                        'description': 'Timezone identifier',
                                    },
                                    'tz_label': {
                                        'type': ['string', 'null'],
                                        'description': 'Timezone label',
                                    },
                                    'tz_offset': {
                                        'type': ['integer', 'null'],
                                        'description': 'Timezone offset in seconds',
                                    },
                                    'profile': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'User profile information',
                                                'properties': {
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Job title',
                                                    },
                                                    'phone': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Phone number',
                                                    },
                                                    'skype': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Skype handle',
                                                    },
                                                    'real_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Real name',
                                                    },
                                                    'real_name_normalized': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Normalized real name',
                                                    },
                                                    'display_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Display name',
                                                    },
                                                    'display_name_normalized': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Normalized display name',
                                                    },
                                                    'status_text': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Status text',
                                                    },
                                                    'status_emoji': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Status emoji',
                                                    },
                                                    'status_expiration': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Status expiration timestamp',
                                                    },
                                                    'avatar_hash': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Avatar hash',
                                                    },
                                                    'first_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'First name',
                                                    },
                                                    'last_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Last name',
                                                    },
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Email address',
                                                    },
                                                    'image_24': {
                                                        'type': ['string', 'null'],
                                                        'description': '24px avatar URL',
                                                    },
                                                    'image_32': {
                                                        'type': ['string', 'null'],
                                                        'description': '32px avatar URL',
                                                    },
                                                    'image_48': {
                                                        'type': ['string', 'null'],
                                                        'description': '48px avatar URL',
                                                    },
                                                    'image_72': {
                                                        'type': ['string', 'null'],
                                                        'description': '72px avatar URL',
                                                    },
                                                    'image_192': {
                                                        'type': ['string', 'null'],
                                                        'description': '192px avatar URL',
                                                    },
                                                    'image_512': {
                                                        'type': ['string', 'null'],
                                                        'description': '512px avatar URL',
                                                    },
                                                    'team': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Team ID',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'User profile information',
                                    },
                                    'is_admin': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the user is an admin',
                                    },
                                    'is_owner': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the user is an owner',
                                    },
                                    'is_primary_owner': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the user is the primary owner',
                                    },
                                    'is_restricted': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the user is restricted',
                                    },
                                    'is_ultra_restricted': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the user is ultra restricted',
                                    },
                                    'is_bot': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the user is a bot',
                                    },
                                    'is_app_user': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the user is an app user',
                                    },
                                    'updated': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of last update',
                                    },
                                    'is_email_confirmed': {
                                        'type': ['boolean', 'null'],
                                        'description': "Whether the user's email is confirmed",
                                    },
                                    'who_can_share_contact_card': {
                                        'type': ['string', 'null'],
                                        'description': "Who can share the user's contact card",
                                    },
                                },
                                'x-airbyte-entity-name': 'users',
                                'x-airbyte-stream-name': 'users',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Slack workspace members, their profiles, roles, and contact info',
                                    'when_to_use': 'Looking up a person in Slack by name, email, or role, or listing workspace members',
                                    'trigger_phrases': [
                                        'who is',
                                        'find user',
                                        'look up',
                                        'team members',
                                        'user list',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Who is John in Slack?', 'Find the Slack user with email alex@example.com', 'List all admins in the workspace'],
                                    'search_strategy': 'When searching for a user by name, match against all name-related fields: name (username), real_name, profile.display_name, profile.display_name_normalized, profile.real_name, profile.real_name_normalized, profile.first_name, profile.last_name, and profile.email. Use case-insensitive substring matching across all of these fields to maximize recall.',
                                },
                            },
                        },
                    },
                    record_extractor='$.user',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Slack user object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique user identifier'},
                    'team_id': {
                        'type': ['string', 'null'],
                        'description': 'Team ID the user belongs to',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Username',
                    },
                    'deleted': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user has been deleted',
                    },
                    'color': {
                        'type': ['string', 'null'],
                        'description': 'User color for display',
                    },
                    'real_name': {
                        'type': ['string', 'null'],
                        'description': "User's real name",
                    },
                    'tz': {
                        'type': ['string', 'null'],
                        'description': 'Timezone identifier',
                    },
                    'tz_label': {
                        'type': ['string', 'null'],
                        'description': 'Timezone label',
                    },
                    'tz_offset': {
                        'type': ['integer', 'null'],
                        'description': 'Timezone offset in seconds',
                    },
                    'profile': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/UserProfile'},
                            {'type': 'null'},
                        ],
                        'description': 'User profile information',
                    },
                    'is_admin': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is an admin',
                    },
                    'is_owner': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is an owner',
                    },
                    'is_primary_owner': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is the primary owner',
                    },
                    'is_restricted': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is restricted',
                    },
                    'is_ultra_restricted': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is ultra restricted',
                    },
                    'is_bot': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is a bot',
                    },
                    'is_app_user': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is an app user',
                    },
                    'updated': {
                        'type': ['integer', 'null'],
                        'description': 'Unix timestamp of last update',
                    },
                    'is_email_confirmed': {
                        'type': ['boolean', 'null'],
                        'description': "Whether the user's email is confirmed",
                    },
                    'who_can_share_contact_card': {
                        'type': ['string', 'null'],
                        'description': "Who can share the user's contact card",
                    },
                },
                'x-airbyte-entity-name': 'users',
                'x-airbyte-stream-name': 'users',
                'x-airbyte-ai-hints': {
                    'summary': 'Slack workspace members, their profiles, roles, and contact info',
                    'when_to_use': 'Looking up a person in Slack by name, email, or role, or listing workspace members',
                    'trigger_phrases': [
                        'who is',
                        'find user',
                        'look up',
                        'team members',
                        'user list',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Who is John in Slack?', 'Find the Slack user with email alex@example.com', 'List all admins in the workspace'],
                    'search_strategy': 'When searching for a user by name, match against all name-related fields: name (username), real_name, profile.display_name, profile.display_name_normalized, profile.real_name, profile.real_name_normalized, profile.first_name, profile.last_name, and profile.email. Use case-insensitive substring matching across all of these fields to maximize recall.',
                },
            },
            ai_hints={
                'summary': 'Slack workspace members, their profiles, roles, and contact info',
                'when_to_use': 'Looking up a person in Slack by name, email, or role, or listing workspace members',
                'trigger_phrases': [
                    'who is',
                    'find user',
                    'look up',
                    'team members',
                    'user list',
                ],
                'freshness': 'live',
                'example_questions': ['Who is John in Slack?', 'Find the Slack user with email alex@example.com', 'List all admins in the workspace'],
                'search_strategy': 'When searching for a user by name, match against all name-related fields: name (username), real_name, profile.display_name, profile.display_name_normalized, profile.real_name, profile.real_name_normalized, profile.first_name, profile.last_name, and profile.email. Use case-insensitive substring matching across all of these fields to maximize recall.',
            },
        ),
        EntityDefinition(
            name='channels',
            stream_name='channels',
            actions=[
                Action.LIST,
                Action.GET,
                Action.CREATE,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/conversations.list',
                    action=Action.LIST,
                    description='Returns a list of all channels in the Slack workspace',
                    query_params=[
                        'cursor',
                        'limit',
                        'types',
                        'exclude_archived',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                            'minimum': 1,
                            'maximum': 1000,
                        },
                        'types': {
                            'type': 'string',
                            'required': False,
                            'default': 'public_channel',
                        },
                        'exclude_archived': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing list of channels',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channels': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Slack channel object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique channel identifier'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Channel name',
                                        },
                                        'is_channel': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this is a channel',
                                        },
                                        'is_group': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this is a group',
                                        },
                                        'is_im': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this is a direct message',
                                        },
                                        'is_mpim': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this is a multi-party direct message',
                                        },
                                        'is_private': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the channel is private',
                                        },
                                        'created': {
                                            'type': ['integer', 'null'],
                                            'description': 'Unix timestamp of channel creation',
                                        },
                                        'is_archived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the channel is archived',
                                        },
                                        'is_general': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this is the general channel',
                                        },
                                        'unlinked': {
                                            'type': ['integer', 'null'],
                                            'description': 'Unlinked timestamp',
                                        },
                                        'name_normalized': {
                                            'type': ['string', 'null'],
                                            'description': 'Normalized channel name',
                                        },
                                        'is_shared': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the channel is shared',
                                        },
                                        'is_org_shared': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the channel is shared across the organization',
                                        },
                                        'is_pending_ext_shared': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether external sharing is pending',
                                        },
                                        'pending_shared': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'Pending shared teams',
                                        },
                                        'context_team_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Context team ID',
                                        },
                                        'updated': {
                                            'type': ['integer', 'null'],
                                            'description': 'Unix timestamp of last update',
                                        },
                                        'creator': {
                                            'type': ['string', 'null'],
                                            'description': 'User ID of the channel creator',
                                        },
                                        'is_ext_shared': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the channel is externally shared',
                                        },
                                        'shared_team_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'IDs of teams the channel is shared with',
                                        },
                                        'pending_connected_team_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'IDs of teams with pending connection',
                                        },
                                        'is_member': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the authenticated user is a member',
                                        },
                                        'topic': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Channel topic information',
                                                    'properties': {
                                                        'value': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Topic text',
                                                        },
                                                        'creator': {
                                                            'type': ['string', 'null'],
                                                            'description': 'User ID who set the topic',
                                                        },
                                                        'last_set': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Unix timestamp when topic was last set',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Channel topic',
                                        },
                                        'purpose': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Channel purpose information',
                                                    'properties': {
                                                        'value': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Purpose text',
                                                        },
                                                        'creator': {
                                                            'type': ['string', 'null'],
                                                            'description': 'User ID who set the purpose',
                                                        },
                                                        'last_set': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Unix timestamp when purpose was last set',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Channel purpose',
                                        },
                                        'previous_names': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'Previous channel names',
                                        },
                                        'num_members': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of members in the channel',
                                        },
                                        'parent_conversation': {
                                            'type': ['string', 'null'],
                                            'description': 'Parent conversation ID if this is a thread',
                                        },
                                        'properties': {
                                            'type': ['object', 'null'],
                                            'description': 'Additional channel properties',
                                        },
                                        'is_thread_only': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the channel is thread-only',
                                        },
                                        'is_read_only': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the channel is read-only',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'channels',
                                    'x-airbyte-stream-name': 'channels',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Slack channel metadata, names, and membership',
                                        'when_to_use': 'Looking up Slack channels by name or listing available channels',
                                        'trigger_phrases': ['which channel', 'find channel', 'channel list'],
                                        'freshness': 'live',
                                        'search_strategy': 'Search by channel name using fuzzy match.',
                                    },
                                },
                            },
                            'response_metadata': {
                                'type': 'object',
                                'description': 'Response metadata including pagination',
                                'properties': {
                                    'next_cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'Cursor for next page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.channels',
                    meta_extractor={'next_cursor': '$.response_metadata.next_cursor'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/conversations.info',
                    action=Action.GET,
                    description='Get information about a single channel by ID',
                    query_params=['channel'],
                    query_params_schema={
                        'channel': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing single channel',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channel': {
                                'type': 'object',
                                'description': 'Slack channel object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique channel identifier'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Channel name',
                                    },
                                    'is_channel': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a channel',
                                    },
                                    'is_group': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a group',
                                    },
                                    'is_im': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a direct message',
                                    },
                                    'is_mpim': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a multi-party direct message',
                                    },
                                    'is_private': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is private',
                                    },
                                    'created': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of channel creation',
                                    },
                                    'is_archived': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is archived',
                                    },
                                    'is_general': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is the general channel',
                                    },
                                    'unlinked': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unlinked timestamp',
                                    },
                                    'name_normalized': {
                                        'type': ['string', 'null'],
                                        'description': 'Normalized channel name',
                                    },
                                    'is_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared',
                                    },
                                    'is_org_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared across the organization',
                                    },
                                    'is_pending_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether external sharing is pending',
                                    },
                                    'pending_shared': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Pending shared teams',
                                    },
                                    'context_team_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Context team ID',
                                    },
                                    'updated': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of last update',
                                    },
                                    'creator': {
                                        'type': ['string', 'null'],
                                        'description': 'User ID of the channel creator',
                                    },
                                    'is_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is externally shared',
                                    },
                                    'shared_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams the channel is shared with',
                                    },
                                    'pending_connected_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams with pending connection',
                                    },
                                    'is_member': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the authenticated user is a member',
                                    },
                                    'topic': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel topic information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Topic text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the topic',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when topic was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel topic',
                                    },
                                    'purpose': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel purpose information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Purpose text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the purpose',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when purpose was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel purpose',
                                    },
                                    'previous_names': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Previous channel names',
                                    },
                                    'num_members': {
                                        'type': ['integer', 'null'],
                                        'description': 'Number of members in the channel',
                                    },
                                    'parent_conversation': {
                                        'type': ['string', 'null'],
                                        'description': 'Parent conversation ID if this is a thread',
                                    },
                                    'properties': {
                                        'type': ['object', 'null'],
                                        'description': 'Additional channel properties',
                                    },
                                    'is_thread_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is thread-only',
                                    },
                                    'is_read_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is read-only',
                                    },
                                },
                                'x-airbyte-entity-name': 'channels',
                                'x-airbyte-stream-name': 'channels',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Slack channel metadata, names, and membership',
                                    'when_to_use': 'Looking up Slack channels by name or listing available channels',
                                    'trigger_phrases': ['which channel', 'find channel', 'channel list'],
                                    'freshness': 'live',
                                    'search_strategy': 'Search by channel name using fuzzy match.',
                                },
                            },
                        },
                    },
                    record_extractor='$.channel',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/conversations.create',
                    action=Action.CREATE,
                    description='Creates a new public or private channel',
                    body_fields=['name', 'is_private'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a channel',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Channel name (lowercase, no spaces, max 80 chars)'},
                            'is_private': {'type': 'boolean', 'description': 'Create a private channel instead of public'},
                        },
                        'required': ['name'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from creating a channel',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channel': {
                                'type': 'object',
                                'description': 'Slack channel object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique channel identifier'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Channel name',
                                    },
                                    'is_channel': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a channel',
                                    },
                                    'is_group': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a group',
                                    },
                                    'is_im': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a direct message',
                                    },
                                    'is_mpim': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a multi-party direct message',
                                    },
                                    'is_private': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is private',
                                    },
                                    'created': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of channel creation',
                                    },
                                    'is_archived': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is archived',
                                    },
                                    'is_general': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is the general channel',
                                    },
                                    'unlinked': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unlinked timestamp',
                                    },
                                    'name_normalized': {
                                        'type': ['string', 'null'],
                                        'description': 'Normalized channel name',
                                    },
                                    'is_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared',
                                    },
                                    'is_org_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared across the organization',
                                    },
                                    'is_pending_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether external sharing is pending',
                                    },
                                    'pending_shared': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Pending shared teams',
                                    },
                                    'context_team_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Context team ID',
                                    },
                                    'updated': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of last update',
                                    },
                                    'creator': {
                                        'type': ['string', 'null'],
                                        'description': 'User ID of the channel creator',
                                    },
                                    'is_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is externally shared',
                                    },
                                    'shared_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams the channel is shared with',
                                    },
                                    'pending_connected_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams with pending connection',
                                    },
                                    'is_member': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the authenticated user is a member',
                                    },
                                    'topic': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel topic information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Topic text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the topic',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when topic was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel topic',
                                    },
                                    'purpose': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel purpose information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Purpose text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the purpose',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when purpose was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel purpose',
                                    },
                                    'previous_names': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Previous channel names',
                                    },
                                    'num_members': {
                                        'type': ['integer', 'null'],
                                        'description': 'Number of members in the channel',
                                    },
                                    'parent_conversation': {
                                        'type': ['string', 'null'],
                                        'description': 'Parent conversation ID if this is a thread',
                                    },
                                    'properties': {
                                        'type': ['object', 'null'],
                                        'description': 'Additional channel properties',
                                    },
                                    'is_thread_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is thread-only',
                                    },
                                    'is_read_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is read-only',
                                    },
                                },
                                'x-airbyte-entity-name': 'channels',
                                'x-airbyte-stream-name': 'channels',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Slack channel metadata, names, and membership',
                                    'when_to_use': 'Looking up Slack channels by name or listing available channels',
                                    'trigger_phrases': ['which channel', 'find channel', 'channel list'],
                                    'freshness': 'live',
                                    'search_strategy': 'Search by channel name using fuzzy match.',
                                },
                            },
                        },
                    },
                    record_extractor='$.channel',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='POST',
                    path='/conversations.rename',
                    action=Action.UPDATE,
                    description='Renames an existing channel',
                    body_fields=['channel', 'name'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for renaming a channel',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel ID to rename'},
                            'name': {'type': 'string', 'description': 'New channel name (lowercase, no spaces, max 80 chars)'},
                        },
                        'required': ['channel', 'name'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from renaming a channel',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channel': {
                                'type': 'object',
                                'description': 'Slack channel object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique channel identifier'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Channel name',
                                    },
                                    'is_channel': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a channel',
                                    },
                                    'is_group': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a group',
                                    },
                                    'is_im': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a direct message',
                                    },
                                    'is_mpim': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a multi-party direct message',
                                    },
                                    'is_private': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is private',
                                    },
                                    'created': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of channel creation',
                                    },
                                    'is_archived': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is archived',
                                    },
                                    'is_general': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is the general channel',
                                    },
                                    'unlinked': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unlinked timestamp',
                                    },
                                    'name_normalized': {
                                        'type': ['string', 'null'],
                                        'description': 'Normalized channel name',
                                    },
                                    'is_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared',
                                    },
                                    'is_org_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared across the organization',
                                    },
                                    'is_pending_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether external sharing is pending',
                                    },
                                    'pending_shared': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Pending shared teams',
                                    },
                                    'context_team_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Context team ID',
                                    },
                                    'updated': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of last update',
                                    },
                                    'creator': {
                                        'type': ['string', 'null'],
                                        'description': 'User ID of the channel creator',
                                    },
                                    'is_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is externally shared',
                                    },
                                    'shared_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams the channel is shared with',
                                    },
                                    'pending_connected_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams with pending connection',
                                    },
                                    'is_member': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the authenticated user is a member',
                                    },
                                    'topic': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel topic information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Topic text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the topic',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when topic was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel topic',
                                    },
                                    'purpose': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel purpose information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Purpose text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the purpose',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when purpose was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel purpose',
                                    },
                                    'previous_names': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Previous channel names',
                                    },
                                    'num_members': {
                                        'type': ['integer', 'null'],
                                        'description': 'Number of members in the channel',
                                    },
                                    'parent_conversation': {
                                        'type': ['string', 'null'],
                                        'description': 'Parent conversation ID if this is a thread',
                                    },
                                    'properties': {
                                        'type': ['object', 'null'],
                                        'description': 'Additional channel properties',
                                    },
                                    'is_thread_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is thread-only',
                                    },
                                    'is_read_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is read-only',
                                    },
                                },
                                'x-airbyte-entity-name': 'channels',
                                'x-airbyte-stream-name': 'channels',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Slack channel metadata, names, and membership',
                                    'when_to_use': 'Looking up Slack channels by name or listing available channels',
                                    'trigger_phrases': ['which channel', 'find channel', 'channel list'],
                                    'freshness': 'live',
                                    'search_strategy': 'Search by channel name using fuzzy match.',
                                },
                            },
                        },
                    },
                    record_extractor='$.channel',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Slack channel object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique channel identifier'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Channel name',
                    },
                    'is_channel': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this is a channel',
                    },
                    'is_group': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this is a group',
                    },
                    'is_im': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this is a direct message',
                    },
                    'is_mpim': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this is a multi-party direct message',
                    },
                    'is_private': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the channel is private',
                    },
                    'created': {
                        'type': ['integer', 'null'],
                        'description': 'Unix timestamp of channel creation',
                    },
                    'is_archived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the channel is archived',
                    },
                    'is_general': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this is the general channel',
                    },
                    'unlinked': {
                        'type': ['integer', 'null'],
                        'description': 'Unlinked timestamp',
                    },
                    'name_normalized': {
                        'type': ['string', 'null'],
                        'description': 'Normalized channel name',
                    },
                    'is_shared': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the channel is shared',
                    },
                    'is_org_shared': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the channel is shared across the organization',
                    },
                    'is_pending_ext_shared': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether external sharing is pending',
                    },
                    'pending_shared': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'Pending shared teams',
                    },
                    'context_team_id': {
                        'type': ['string', 'null'],
                        'description': 'Context team ID',
                    },
                    'updated': {
                        'type': ['integer', 'null'],
                        'description': 'Unix timestamp of last update',
                    },
                    'creator': {
                        'type': ['string', 'null'],
                        'description': 'User ID of the channel creator',
                    },
                    'is_ext_shared': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the channel is externally shared',
                    },
                    'shared_team_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'IDs of teams the channel is shared with',
                    },
                    'pending_connected_team_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'IDs of teams with pending connection',
                    },
                    'is_member': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the authenticated user is a member',
                    },
                    'topic': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ChannelTopic'},
                            {'type': 'null'},
                        ],
                        'description': 'Channel topic',
                    },
                    'purpose': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ChannelPurpose'},
                            {'type': 'null'},
                        ],
                        'description': 'Channel purpose',
                    },
                    'previous_names': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'Previous channel names',
                    },
                    'num_members': {
                        'type': ['integer', 'null'],
                        'description': 'Number of members in the channel',
                    },
                    'parent_conversation': {
                        'type': ['string', 'null'],
                        'description': 'Parent conversation ID if this is a thread',
                    },
                    'properties': {
                        'type': ['object', 'null'],
                        'description': 'Additional channel properties',
                    },
                    'is_thread_only': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the channel is thread-only',
                    },
                    'is_read_only': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the channel is read-only',
                    },
                },
                'x-airbyte-entity-name': 'channels',
                'x-airbyte-stream-name': 'channels',
                'x-airbyte-ai-hints': {
                    'summary': 'Slack channel metadata, names, and membership',
                    'when_to_use': 'Looking up Slack channels by name or listing available channels',
                    'trigger_phrases': ['which channel', 'find channel', 'channel list'],
                    'freshness': 'live',
                    'search_strategy': 'Search by channel name using fuzzy match.',
                },
            },
            ai_hints={
                'summary': 'Slack channel metadata, names, and membership',
                'when_to_use': 'Looking up Slack channels by name or listing available channels',
                'trigger_phrases': ['which channel', 'find channel', 'channel list'],
                'freshness': 'live',
                'search_strategy': 'Search by channel name using fuzzy match.',
            },
        ),
        EntityDefinition(
            name='channel_messages',
            stream_name='channel_messages',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/conversations.history',
                    action=Action.LIST,
                    description='Returns messages from a channel',
                    query_params=[
                        'channel',
                        'cursor',
                        'limit',
                        'oldest',
                        'latest',
                        'inclusive',
                    ],
                    query_params_schema={
                        'channel': {'type': 'string', 'required': True},
                        'cursor': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                            'minimum': 1,
                            'maximum': 1000,
                        },
                        'oldest': {'type': 'string', 'required': False},
                        'latest': {'type': 'string', 'required': False},
                        'inclusive': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing list of messages',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'messages': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Slack message object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Message type',
                                        },
                                        'subtype': {
                                            'type': ['string', 'null'],
                                            'description': 'Message subtype',
                                        },
                                        'ts': {'type': 'string', 'description': 'Message timestamp (unique identifier)'},
                                        'user': {
                                            'type': ['string', 'null'],
                                            'description': 'User ID who sent the message',
                                        },
                                        'text': {
                                            'type': ['string', 'null'],
                                            'description': 'Message text content',
                                        },
                                        'thread_ts': {
                                            'type': ['string', 'null'],
                                            'description': 'Thread parent timestamp',
                                        },
                                        'reply_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of replies in thread',
                                        },
                                        'reply_users_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of unique users who replied',
                                        },
                                        'latest_reply': {
                                            'type': ['string', 'null'],
                                            'description': 'Timestamp of latest reply',
                                        },
                                        'reply_users': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'User IDs who replied to the thread',
                                        },
                                        'is_locked': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the thread is locked',
                                        },
                                        'subscribed': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user is subscribed to the thread',
                                        },
                                        'reactions': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'Message reaction',
                                                'properties': {
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Reaction emoji name',
                                                    },
                                                    'users': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'string'},
                                                        'description': 'User IDs who reacted',
                                                    },
                                                    'count': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Number of reactions',
                                                    },
                                                },
                                            },
                                            'description': 'Reactions to the message',
                                        },
                                        'attachments': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'Message attachment',
                                                'properties': {
                                                    'id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Attachment ID',
                                                    },
                                                    'fallback': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Fallback text',
                                                    },
                                                    'color': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Attachment color',
                                                    },
                                                    'pretext': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Pretext',
                                                    },
                                                    'author_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Author name',
                                                    },
                                                    'author_link': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Author link',
                                                    },
                                                    'author_icon': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Author icon URL',
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Attachment title',
                                                    },
                                                    'title_link': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Title link',
                                                    },
                                                    'text': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Attachment text',
                                                    },
                                                    'fields': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                        'description': 'Attachment fields',
                                                    },
                                                    'image_url': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Image URL',
                                                    },
                                                    'thumb_url': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Thumbnail URL',
                                                    },
                                                    'footer': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Footer text',
                                                    },
                                                    'footer_icon': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Footer icon URL',
                                                    },
                                                    'ts': {
                                                        'type': ['string', 'integer', 'null'],
                                                        'description': 'Timestamp',
                                                    },
                                                },
                                            },
                                            'description': 'Message attachments',
                                        },
                                        'blocks': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                            'description': 'Block kit blocks',
                                        },
                                        'files': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'File object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'File ID',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'File name',
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                        'description': 'File title',
                                                    },
                                                    'mimetype': {
                                                        'type': ['string', 'null'],
                                                        'description': 'MIME type',
                                                    },
                                                    'filetype': {
                                                        'type': ['string', 'null'],
                                                        'description': 'File type',
                                                    },
                                                    'pretty_type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Human-readable file type',
                                                    },
                                                    'user': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who uploaded the file',
                                                    },
                                                    'size': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'File size in bytes',
                                                    },
                                                    'mode': {
                                                        'type': ['string', 'null'],
                                                        'description': 'File mode',
                                                    },
                                                    'is_external': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the file is external',
                                                    },
                                                    'external_type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'External file type',
                                                    },
                                                    'is_public': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the file is public',
                                                    },
                                                    'public_url_shared': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the public URL is shared',
                                                    },
                                                    'url_private': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Private URL',
                                                    },
                                                    'url_private_download': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Private download URL',
                                                    },
                                                    'permalink': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Permalink',
                                                    },
                                                    'permalink_public': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Public permalink',
                                                    },
                                                    'created': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp of creation',
                                                    },
                                                    'timestamp': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp',
                                                    },
                                                },
                                            },
                                            'description': 'Files attached to the message',
                                        },
                                        'edited': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Message edit information',
                                                    'properties': {
                                                        'user': {
                                                            'type': ['string', 'null'],
                                                            'description': 'User ID who edited the message',
                                                        },
                                                        'ts': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Edit timestamp',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Edit information',
                                        },
                                        'bot_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Bot ID if message was sent by a bot',
                                        },
                                        'bot_profile': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Bot profile information',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Bot ID',
                                                        },
                                                        'deleted': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the bot is deleted',
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Bot name',
                                                        },
                                                        'updated': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Unix timestamp of last update',
                                                        },
                                                        'app_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'App ID',
                                                        },
                                                        'team_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Team ID',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Bot profile information',
                                        },
                                        'app_id': {
                                            'type': ['string', 'null'],
                                            'description': 'App ID if message was sent by an app',
                                        },
                                        'team': {
                                            'type': ['string', 'null'],
                                            'description': 'Team ID',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'channel_messages',
                                    'x-airbyte-stream-name': 'channel_messages',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Recent Slack messages, channel activity, and conversations',
                                        'when_to_use': 'Questions about what someone said, recent channel activity, or Slack conversations',
                                        'trigger_phrases': [
                                            'latest in #',
                                            'what did [person] say',
                                            'updates in',
                                            'recent messages about',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ["What's the latest in #ext-marathon?", 'What did Alex say in the channel?'],
                                        'search_strategy': 'Use `channel_messages` for reading and searching existing Slack messages only. First find the channel using the `channels` entity search, then find messages using the `channel_messages` entity search filtered on channel_id for that channel. Example filter: {"eq": {"channel_id": "C123"}}. Do not use `channel_messages.create` to send a message. To post a new Slack message, use `messages.create` with channel and text.',
                                    },
                                },
                            },
                            'has_more': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether there are more messages',
                            },
                            'pin_count': {
                                'type': ['integer', 'null'],
                                'description': 'Number of pinned messages',
                            },
                            'response_metadata': {
                                'type': 'object',
                                'description': 'Response metadata including pagination',
                                'properties': {
                                    'next_cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'Cursor for next page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.messages',
                    meta_extractor={'next_cursor': '$.response_metadata.next_cursor', 'has_more': '$.has_more'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Slack message object',
                'properties': {
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Message type',
                    },
                    'subtype': {
                        'type': ['string', 'null'],
                        'description': 'Message subtype',
                    },
                    'ts': {'type': 'string', 'description': 'Message timestamp (unique identifier)'},
                    'user': {
                        'type': ['string', 'null'],
                        'description': 'User ID who sent the message',
                    },
                    'text': {
                        'type': ['string', 'null'],
                        'description': 'Message text content',
                    },
                    'thread_ts': {
                        'type': ['string', 'null'],
                        'description': 'Thread parent timestamp',
                    },
                    'reply_count': {
                        'type': ['integer', 'null'],
                        'description': 'Number of replies in thread',
                    },
                    'reply_users_count': {
                        'type': ['integer', 'null'],
                        'description': 'Number of unique users who replied',
                    },
                    'latest_reply': {
                        'type': ['string', 'null'],
                        'description': 'Timestamp of latest reply',
                    },
                    'reply_users': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'User IDs who replied to the thread',
                    },
                    'is_locked': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the thread is locked',
                    },
                    'subscribed': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is subscribed to the thread',
                    },
                    'reactions': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/Reaction'},
                        'description': 'Reactions to the message',
                    },
                    'attachments': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/Attachment'},
                        'description': 'Message attachments',
                    },
                    'blocks': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                        'description': 'Block kit blocks',
                    },
                    'files': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/File'},
                        'description': 'Files attached to the message',
                    },
                    'edited': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/EditedInfo'},
                            {'type': 'null'},
                        ],
                        'description': 'Edit information',
                    },
                    'bot_id': {
                        'type': ['string', 'null'],
                        'description': 'Bot ID if message was sent by a bot',
                    },
                    'bot_profile': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/BotProfile'},
                            {'type': 'null'},
                        ],
                        'description': 'Bot profile information',
                    },
                    'app_id': {
                        'type': ['string', 'null'],
                        'description': 'App ID if message was sent by an app',
                    },
                    'team': {
                        'type': ['string', 'null'],
                        'description': 'Team ID',
                    },
                },
                'x-airbyte-entity-name': 'channel_messages',
                'x-airbyte-stream-name': 'channel_messages',
                'x-airbyte-ai-hints': {
                    'summary': 'Recent Slack messages, channel activity, and conversations',
                    'when_to_use': 'Questions about what someone said, recent channel activity, or Slack conversations',
                    'trigger_phrases': [
                        'latest in #',
                        'what did [person] say',
                        'updates in',
                        'recent messages about',
                    ],
                    'freshness': 'live',
                    'example_questions': ["What's the latest in #ext-marathon?", 'What did Alex say in the channel?'],
                    'search_strategy': 'Use `channel_messages` for reading and searching existing Slack messages only. First find the channel using the `channels` entity search, then find messages using the `channel_messages` entity search filtered on channel_id for that channel. Example filter: {"eq": {"channel_id": "C123"}}. Do not use `channel_messages.create` to send a message. To post a new Slack message, use `messages.create` with channel and text.',
                },
            },
            ai_hints={
                'summary': 'Recent Slack messages, channel activity, and conversations',
                'when_to_use': 'Questions about what someone said, recent channel activity, or Slack conversations',
                'trigger_phrases': [
                    'latest in #',
                    'what did [person] say',
                    'updates in',
                    'recent messages about',
                ],
                'freshness': 'live',
                'example_questions': ["What's the latest in #ext-marathon?", 'What did Alex say in the channel?'],
                'search_strategy': 'Use `channel_messages` for reading and searching existing Slack messages only. First find the channel using the `channels` entity search, then find messages using the `channel_messages` entity search filtered on channel_id for that channel. Example filter: {"eq": {"channel_id": "C123"}}. Do not use `channel_messages.create` to send a message. To post a new Slack message, use `messages.create` with channel and text.',
            },
        ),
        EntityDefinition(
            name='threads',
            stream_name='threads',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/conversations.replies',
                    action=Action.LIST,
                    description='Returns messages in a thread (thread replies from conversations.replies endpoint)',
                    query_params=[
                        'channel',
                        'ts',
                        'cursor',
                        'limit',
                        'oldest',
                        'latest',
                        'inclusive',
                    ],
                    query_params_schema={
                        'channel': {'type': 'string', 'required': True},
                        'ts': {'type': 'string', 'required': False},
                        'cursor': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                            'minimum': 1,
                            'maximum': 1000,
                        },
                        'oldest': {'type': 'string', 'required': False},
                        'latest': {'type': 'string', 'required': False},
                        'inclusive': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing thread replies',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'messages': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Slack thread reply message object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Message type',
                                        },
                                        'subtype': {
                                            'type': ['string', 'null'],
                                            'description': 'Message subtype',
                                        },
                                        'ts': {'type': 'string', 'description': 'Message timestamp (unique identifier)'},
                                        'user': {
                                            'type': ['string', 'null'],
                                            'description': 'User ID who sent the message',
                                        },
                                        'text': {
                                            'type': ['string', 'null'],
                                            'description': 'Message text content',
                                        },
                                        'thread_ts': {
                                            'type': ['string', 'null'],
                                            'description': 'Thread parent timestamp',
                                        },
                                        'parent_user_id': {
                                            'type': ['string', 'null'],
                                            'description': 'User ID of the parent message author (present in thread replies)',
                                        },
                                        'reply_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of replies in thread',
                                        },
                                        'reply_users_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of unique users who replied',
                                        },
                                        'latest_reply': {
                                            'type': ['string', 'null'],
                                            'description': 'Timestamp of latest reply',
                                        },
                                        'reply_users': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'User IDs who replied to the thread',
                                        },
                                        'is_locked': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the thread is locked',
                                        },
                                        'subscribed': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user is subscribed to the thread',
                                        },
                                        'reactions': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'Message reaction',
                                                'properties': {
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Reaction emoji name',
                                                    },
                                                    'users': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'string'},
                                                        'description': 'User IDs who reacted',
                                                    },
                                                    'count': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Number of reactions',
                                                    },
                                                },
                                            },
                                            'description': 'Reactions to the message',
                                        },
                                        'attachments': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'Message attachment',
                                                'properties': {
                                                    'id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Attachment ID',
                                                    },
                                                    'fallback': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Fallback text',
                                                    },
                                                    'color': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Attachment color',
                                                    },
                                                    'pretext': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Pretext',
                                                    },
                                                    'author_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Author name',
                                                    },
                                                    'author_link': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Author link',
                                                    },
                                                    'author_icon': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Author icon URL',
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Attachment title',
                                                    },
                                                    'title_link': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Title link',
                                                    },
                                                    'text': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Attachment text',
                                                    },
                                                    'fields': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                        'description': 'Attachment fields',
                                                    },
                                                    'image_url': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Image URL',
                                                    },
                                                    'thumb_url': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Thumbnail URL',
                                                    },
                                                    'footer': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Footer text',
                                                    },
                                                    'footer_icon': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Footer icon URL',
                                                    },
                                                    'ts': {
                                                        'type': ['string', 'integer', 'null'],
                                                        'description': 'Timestamp',
                                                    },
                                                },
                                            },
                                            'description': 'Message attachments',
                                        },
                                        'blocks': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                            'description': 'Block kit blocks',
                                        },
                                        'files': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'File object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'File ID',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'File name',
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                        'description': 'File title',
                                                    },
                                                    'mimetype': {
                                                        'type': ['string', 'null'],
                                                        'description': 'MIME type',
                                                    },
                                                    'filetype': {
                                                        'type': ['string', 'null'],
                                                        'description': 'File type',
                                                    },
                                                    'pretty_type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Human-readable file type',
                                                    },
                                                    'user': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who uploaded the file',
                                                    },
                                                    'size': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'File size in bytes',
                                                    },
                                                    'mode': {
                                                        'type': ['string', 'null'],
                                                        'description': 'File mode',
                                                    },
                                                    'is_external': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the file is external',
                                                    },
                                                    'external_type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'External file type',
                                                    },
                                                    'is_public': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the file is public',
                                                    },
                                                    'public_url_shared': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the public URL is shared',
                                                    },
                                                    'url_private': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Private URL',
                                                    },
                                                    'url_private_download': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Private download URL',
                                                    },
                                                    'permalink': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Permalink',
                                                    },
                                                    'permalink_public': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Public permalink',
                                                    },
                                                    'created': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp of creation',
                                                    },
                                                    'timestamp': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp',
                                                    },
                                                },
                                            },
                                            'description': 'Files attached to the message',
                                        },
                                        'edited': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Message edit information',
                                                    'properties': {
                                                        'user': {
                                                            'type': ['string', 'null'],
                                                            'description': 'User ID who edited the message',
                                                        },
                                                        'ts': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Edit timestamp',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Edit information',
                                        },
                                        'bot_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Bot ID if message was sent by a bot',
                                        },
                                        'bot_profile': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Bot profile information',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Bot ID',
                                                        },
                                                        'deleted': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the bot is deleted',
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Bot name',
                                                        },
                                                        'updated': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Unix timestamp of last update',
                                                        },
                                                        'app_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'App ID',
                                                        },
                                                        'team_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Team ID',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Bot profile information',
                                        },
                                        'app_id': {
                                            'type': ['string', 'null'],
                                            'description': 'App ID if message was sent by an app',
                                        },
                                        'team': {
                                            'type': ['string', 'null'],
                                            'description': 'Team ID',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'threads',
                                    'x-airbyte-stream-name': 'threads',
                                },
                            },
                            'has_more': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether there are more replies',
                            },
                            'response_metadata': {
                                'type': 'object',
                                'description': 'Response metadata including pagination',
                                'properties': {
                                    'next_cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'Cursor for next page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.messages',
                    meta_extractor={'next_cursor': '$.response_metadata.next_cursor', 'has_more': '$.has_more'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Slack thread reply message object',
                'properties': {
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Message type',
                    },
                    'subtype': {
                        'type': ['string', 'null'],
                        'description': 'Message subtype',
                    },
                    'ts': {'type': 'string', 'description': 'Message timestamp (unique identifier)'},
                    'user': {
                        'type': ['string', 'null'],
                        'description': 'User ID who sent the message',
                    },
                    'text': {
                        'type': ['string', 'null'],
                        'description': 'Message text content',
                    },
                    'thread_ts': {
                        'type': ['string', 'null'],
                        'description': 'Thread parent timestamp',
                    },
                    'parent_user_id': {
                        'type': ['string', 'null'],
                        'description': 'User ID of the parent message author (present in thread replies)',
                    },
                    'reply_count': {
                        'type': ['integer', 'null'],
                        'description': 'Number of replies in thread',
                    },
                    'reply_users_count': {
                        'type': ['integer', 'null'],
                        'description': 'Number of unique users who replied',
                    },
                    'latest_reply': {
                        'type': ['string', 'null'],
                        'description': 'Timestamp of latest reply',
                    },
                    'reply_users': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'User IDs who replied to the thread',
                    },
                    'is_locked': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the thread is locked',
                    },
                    'subscribed': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is subscribed to the thread',
                    },
                    'reactions': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/Reaction'},
                        'description': 'Reactions to the message',
                    },
                    'attachments': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/Attachment'},
                        'description': 'Message attachments',
                    },
                    'blocks': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                        'description': 'Block kit blocks',
                    },
                    'files': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/File'},
                        'description': 'Files attached to the message',
                    },
                    'edited': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/EditedInfo'},
                            {'type': 'null'},
                        ],
                        'description': 'Edit information',
                    },
                    'bot_id': {
                        'type': ['string', 'null'],
                        'description': 'Bot ID if message was sent by a bot',
                    },
                    'bot_profile': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/BotProfile'},
                            {'type': 'null'},
                        ],
                        'description': 'Bot profile information',
                    },
                    'app_id': {
                        'type': ['string', 'null'],
                        'description': 'App ID if message was sent by an app',
                    },
                    'team': {
                        'type': ['string', 'null'],
                        'description': 'Team ID',
                    },
                },
                'x-airbyte-entity-name': 'threads',
                'x-airbyte-stream-name': 'threads',
            },
        ),
        EntityDefinition(
            name='messages',
            actions=[Action.CREATE, Action.UPDATE, Action.DELETE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/chat.postMessage',
                    action=Action.CREATE,
                    description='Posts a message to a public channel, private channel, or direct message conversation',
                    body_fields=[
                        'channel',
                        'text',
                        'thread_ts',
                        'reply_broadcast',
                        'unfurl_links',
                        'unfurl_media',
                    ],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a message',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel ID, private group ID, or user ID to send message to'},
                            'text': {'type': 'string', 'description': 'Message text content (supports mrkdwn formatting)'},
                            'thread_ts': {'type': 'string', 'description': 'Thread timestamp to reply to (for threaded messages)'},
                            'reply_broadcast': {'type': 'boolean', 'description': 'Also post reply to channel when replying to a thread'},
                            'unfurl_links': {'type': 'boolean', 'description': 'Enable unfurling of primarily text-based content'},
                            'unfurl_media': {'type': 'boolean', 'description': 'Enable unfurling of media content'},
                        },
                        'required': ['channel', 'text'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from creating a message',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channel': {
                                'type': ['string', 'null'],
                                'description': 'Channel ID where message was posted',
                            },
                            'ts': {
                                'type': ['string', 'null'],
                                'description': 'Message timestamp (unique identifier)',
                            },
                            'message': {
                                'type': 'object',
                                'description': 'A message object returned from create/update operations',
                                'properties': {
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Message type',
                                    },
                                    'subtype': {
                                        'type': ['string', 'null'],
                                        'description': 'Message subtype',
                                    },
                                    'text': {
                                        'type': ['string', 'null'],
                                        'description': 'Message text content',
                                    },
                                    'ts': {'type': 'string', 'description': 'Message timestamp (unique identifier)'},
                                    'user': {
                                        'type': ['string', 'null'],
                                        'description': 'User ID who sent the message',
                                    },
                                    'bot_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Bot ID if message was sent by a bot',
                                    },
                                    'app_id': {
                                        'type': ['string', 'null'],
                                        'description': 'App ID if message was sent by an app',
                                    },
                                    'team': {
                                        'type': ['string', 'null'],
                                        'description': 'Team ID',
                                    },
                                    'bot_profile': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Bot profile information',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Bot ID',
                                                    },
                                                    'deleted': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the bot is deleted',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Bot name',
                                                    },
                                                    'updated': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp of last update',
                                                    },
                                                    'app_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'App ID',
                                                    },
                                                    'team_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Team ID',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Bot profile information',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.message',
                    ai_hints={
                        'summary': 'Post or update Slack messages',
                        'when_to_use': 'When the user asks to send, post, announce, or reply with a new Slack message',
                        'trigger_phrases': [
                            'send a message',
                            'post in #',
                            'announce in channel',
                            'reply in Slack',
                        ],
                        'freshness': 'live',
                        'example_questions': ["Post 'Hello team' in a Slack channel", 'Send a message to a Slack channel'],
                        'search_strategy': 'Use messages.create to send a new Slack message. Required params: channel and text. Do not use channel_messages.create for writes.',
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='POST',
                    path='/chat.update',
                    action=Action.UPDATE,
                    description='Updates an existing message in a channel',
                    body_fields=['channel', 'ts', 'text'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating a message',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel ID containing the message'},
                            'ts': {'type': 'string', 'description': 'Timestamp of the message to update'},
                            'text': {'type': 'string', 'description': 'New message text content'},
                        },
                        'required': ['channel', 'ts', 'text'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from updating a message',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channel': {
                                'type': ['string', 'null'],
                                'description': 'Channel ID where message was updated',
                            },
                            'ts': {
                                'type': ['string', 'null'],
                                'description': 'Message timestamp',
                            },
                            'text': {
                                'type': ['string', 'null'],
                                'description': 'Updated message text',
                            },
                            'message': {
                                'type': 'object',
                                'description': 'A message object returned from create/update operations',
                                'properties': {
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Message type',
                                    },
                                    'subtype': {
                                        'type': ['string', 'null'],
                                        'description': 'Message subtype',
                                    },
                                    'text': {
                                        'type': ['string', 'null'],
                                        'description': 'Message text content',
                                    },
                                    'ts': {'type': 'string', 'description': 'Message timestamp (unique identifier)'},
                                    'user': {
                                        'type': ['string', 'null'],
                                        'description': 'User ID who sent the message',
                                    },
                                    'bot_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Bot ID if message was sent by a bot',
                                    },
                                    'app_id': {
                                        'type': ['string', 'null'],
                                        'description': 'App ID if message was sent by an app',
                                    },
                                    'team': {
                                        'type': ['string', 'null'],
                                        'description': 'Team ID',
                                    },
                                    'bot_profile': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Bot profile information',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Bot ID',
                                                    },
                                                    'deleted': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the bot is deleted',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Bot name',
                                                    },
                                                    'updated': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp of last update',
                                                    },
                                                    'app_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'App ID',
                                                    },
                                                    'team_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Team ID',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Bot profile information',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.message',
                    ai_hints={
                        'summary': 'Post or update Slack messages',
                        'when_to_use': 'When the user asks to edit, revise, or correct an existing Slack message',
                        'trigger_phrases': ['update a message', 'edit the Slack message', 'correct the Slack message'],
                        'freshness': 'live',
                        'example_questions': ["Update the Slack message to say 'Hello team'"],
                        'search_strategy': 'Use messages.update to edit an existing Slack message. Required params: channel, ts, and text.',
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='POST',
                    path='/chat.delete',
                    action=Action.DELETE,
                    description='Deletes a message from a channel. When used with a bot token, may only delete messages posted by that bot.',
                    body_fields=['channel', 'ts'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for deleting a message. Bot tokens can only delete messages posted by the bot.',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel ID containing the message to be deleted'},
                            'ts': {'type': 'string', 'description': 'Timestamp of the message to be deleted'},
                        },
                        'required': ['channel', 'ts'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from deleting a message',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channel': {
                                'type': ['string', 'null'],
                                'description': 'Channel ID where the message was deleted',
                            },
                            'ts': {
                                'type': ['string', 'null'],
                                'description': 'Timestamp of the deleted message',
                            },
                        },
                    },
                    record_extractor='$',
                    ai_hints={
                        'summary': 'Delete Slack messages',
                        'when_to_use': 'When the user wants to delete or remove a message the bot previously sent',
                        'trigger_phrases': ['delete message', 'remove message', 'unsend'],
                        'freshness': 'live',
                        'example_questions': ['Delete the last message the bot sent in a channel'],
                        'search_strategy': 'Use messages.delete to remove a message. Required params: channel and ts (timestamp of the message to delete). Bot tokens can only delete messages posted by the bot.',
                    },
                ),
            },
        ),
        EntityDefinition(
            name='channel_topics',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/conversations.setTopic',
                    action=Action.CREATE,
                    description='Sets the topic for a channel',
                    body_fields=['channel', 'topic'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for setting channel topic',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel ID to set topic for'},
                            'topic': {'type': 'string', 'description': 'New topic text (max 250 characters)'},
                        },
                        'required': ['channel', 'topic'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from setting channel topic',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channel': {
                                'type': 'object',
                                'description': 'Slack channel object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique channel identifier'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Channel name',
                                    },
                                    'is_channel': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a channel',
                                    },
                                    'is_group': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a group',
                                    },
                                    'is_im': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a direct message',
                                    },
                                    'is_mpim': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a multi-party direct message',
                                    },
                                    'is_private': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is private',
                                    },
                                    'created': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of channel creation',
                                    },
                                    'is_archived': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is archived',
                                    },
                                    'is_general': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is the general channel',
                                    },
                                    'unlinked': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unlinked timestamp',
                                    },
                                    'name_normalized': {
                                        'type': ['string', 'null'],
                                        'description': 'Normalized channel name',
                                    },
                                    'is_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared',
                                    },
                                    'is_org_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared across the organization',
                                    },
                                    'is_pending_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether external sharing is pending',
                                    },
                                    'pending_shared': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Pending shared teams',
                                    },
                                    'context_team_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Context team ID',
                                    },
                                    'updated': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of last update',
                                    },
                                    'creator': {
                                        'type': ['string', 'null'],
                                        'description': 'User ID of the channel creator',
                                    },
                                    'is_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is externally shared',
                                    },
                                    'shared_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams the channel is shared with',
                                    },
                                    'pending_connected_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams with pending connection',
                                    },
                                    'is_member': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the authenticated user is a member',
                                    },
                                    'topic': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel topic information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Topic text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the topic',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when topic was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel topic',
                                    },
                                    'purpose': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel purpose information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Purpose text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the purpose',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when purpose was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel purpose',
                                    },
                                    'previous_names': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Previous channel names',
                                    },
                                    'num_members': {
                                        'type': ['integer', 'null'],
                                        'description': 'Number of members in the channel',
                                    },
                                    'parent_conversation': {
                                        'type': ['string', 'null'],
                                        'description': 'Parent conversation ID if this is a thread',
                                    },
                                    'properties': {
                                        'type': ['object', 'null'],
                                        'description': 'Additional channel properties',
                                    },
                                    'is_thread_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is thread-only',
                                    },
                                    'is_read_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is read-only',
                                    },
                                },
                                'x-airbyte-entity-name': 'channels',
                                'x-airbyte-stream-name': 'channels',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Slack channel metadata, names, and membership',
                                    'when_to_use': 'Looking up Slack channels by name or listing available channels',
                                    'trigger_phrases': ['which channel', 'find channel', 'channel list'],
                                    'freshness': 'live',
                                    'search_strategy': 'Search by channel name using fuzzy match.',
                                },
                            },
                        },
                    },
                    record_extractor='$.channel',
                ),
            },
        ),
        EntityDefinition(
            name='channel_purposes',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/conversations.setPurpose',
                    action=Action.CREATE,
                    description='Sets the purpose for a channel',
                    body_fields=['channel', 'purpose'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for setting channel purpose',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel ID to set purpose for'},
                            'purpose': {'type': 'string', 'description': 'New purpose text (max 250 characters)'},
                        },
                        'required': ['channel', 'purpose'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from setting channel purpose',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channel': {
                                'type': 'object',
                                'description': 'Slack channel object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique channel identifier'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Channel name',
                                    },
                                    'is_channel': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a channel',
                                    },
                                    'is_group': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a group',
                                    },
                                    'is_im': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a direct message',
                                    },
                                    'is_mpim': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a multi-party direct message',
                                    },
                                    'is_private': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is private',
                                    },
                                    'created': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of channel creation',
                                    },
                                    'is_archived': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is archived',
                                    },
                                    'is_general': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is the general channel',
                                    },
                                    'unlinked': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unlinked timestamp',
                                    },
                                    'name_normalized': {
                                        'type': ['string', 'null'],
                                        'description': 'Normalized channel name',
                                    },
                                    'is_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared',
                                    },
                                    'is_org_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared across the organization',
                                    },
                                    'is_pending_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether external sharing is pending',
                                    },
                                    'pending_shared': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Pending shared teams',
                                    },
                                    'context_team_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Context team ID',
                                    },
                                    'updated': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of last update',
                                    },
                                    'creator': {
                                        'type': ['string', 'null'],
                                        'description': 'User ID of the channel creator',
                                    },
                                    'is_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is externally shared',
                                    },
                                    'shared_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams the channel is shared with',
                                    },
                                    'pending_connected_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams with pending connection',
                                    },
                                    'is_member': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the authenticated user is a member',
                                    },
                                    'topic': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel topic information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Topic text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the topic',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when topic was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel topic',
                                    },
                                    'purpose': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel purpose information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Purpose text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the purpose',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when purpose was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel purpose',
                                    },
                                    'previous_names': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Previous channel names',
                                    },
                                    'num_members': {
                                        'type': ['integer', 'null'],
                                        'description': 'Number of members in the channel',
                                    },
                                    'parent_conversation': {
                                        'type': ['string', 'null'],
                                        'description': 'Parent conversation ID if this is a thread',
                                    },
                                    'properties': {
                                        'type': ['object', 'null'],
                                        'description': 'Additional channel properties',
                                    },
                                    'is_thread_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is thread-only',
                                    },
                                    'is_read_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is read-only',
                                    },
                                },
                                'x-airbyte-entity-name': 'channels',
                                'x-airbyte-stream-name': 'channels',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Slack channel metadata, names, and membership',
                                    'when_to_use': 'Looking up Slack channels by name or listing available channels',
                                    'trigger_phrases': ['which channel', 'find channel', 'channel list'],
                                    'freshness': 'live',
                                    'search_strategy': 'Search by channel name using fuzzy match.',
                                },
                            },
                        },
                    },
                    record_extractor='$.channel',
                ),
            },
        ),
        EntityDefinition(
            name='channel_invites',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/conversations.invite',
                    action=Action.CREATE,
                    description='Invites one or more users to a public or private channel',
                    body_fields=['channel', 'users', 'force'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for inviting users to a channel',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'The ID of the public or private channel to invite user(s) to'},
                            'users': {'type': 'string', 'description': 'A comma separated list of user IDs. Up to 1000 users may be listed.'},
                            'force': {'type': 'boolean', 'description': 'When set to true and multiple user IDs are provided, continue inviting the valid ones while disregarding invalid IDs. Defaults to false.'},
                        },
                        'required': ['channel', 'users'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from inviting users to a channel',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channel': {
                                'type': 'object',
                                'description': 'Slack channel object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique channel identifier'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Channel name',
                                    },
                                    'is_channel': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a channel',
                                    },
                                    'is_group': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a group',
                                    },
                                    'is_im': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a direct message',
                                    },
                                    'is_mpim': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a multi-party direct message',
                                    },
                                    'is_private': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is private',
                                    },
                                    'created': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of channel creation',
                                    },
                                    'is_archived': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is archived',
                                    },
                                    'is_general': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is the general channel',
                                    },
                                    'unlinked': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unlinked timestamp',
                                    },
                                    'name_normalized': {
                                        'type': ['string', 'null'],
                                        'description': 'Normalized channel name',
                                    },
                                    'is_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared',
                                    },
                                    'is_org_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is shared across the organization',
                                    },
                                    'is_pending_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether external sharing is pending',
                                    },
                                    'pending_shared': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Pending shared teams',
                                    },
                                    'context_team_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Context team ID',
                                    },
                                    'updated': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of last update',
                                    },
                                    'creator': {
                                        'type': ['string', 'null'],
                                        'description': 'User ID of the channel creator',
                                    },
                                    'is_ext_shared': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is externally shared',
                                    },
                                    'shared_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams the channel is shared with',
                                    },
                                    'pending_connected_team_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'IDs of teams with pending connection',
                                    },
                                    'is_member': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the authenticated user is a member',
                                    },
                                    'topic': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel topic information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Topic text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the topic',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when topic was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel topic',
                                    },
                                    'purpose': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'Channel purpose information',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Purpose text',
                                                    },
                                                    'creator': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User ID who set the purpose',
                                                    },
                                                    'last_set': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Unix timestamp when purpose was last set',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Channel purpose',
                                    },
                                    'previous_names': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Previous channel names',
                                    },
                                    'num_members': {
                                        'type': ['integer', 'null'],
                                        'description': 'Number of members in the channel',
                                    },
                                    'parent_conversation': {
                                        'type': ['string', 'null'],
                                        'description': 'Parent conversation ID if this is a thread',
                                    },
                                    'properties': {
                                        'type': ['object', 'null'],
                                        'description': 'Additional channel properties',
                                    },
                                    'is_thread_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is thread-only',
                                    },
                                    'is_read_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the channel is read-only',
                                    },
                                },
                                'x-airbyte-entity-name': 'channels',
                                'x-airbyte-stream-name': 'channels',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Slack channel metadata, names, and membership',
                                    'when_to_use': 'Looking up Slack channels by name or listing available channels',
                                    'trigger_phrases': ['which channel', 'find channel', 'channel list'],
                                    'freshness': 'live',
                                    'search_strategy': 'Search by channel name using fuzzy match.',
                                },
                            },
                        },
                    },
                    record_extractor='$.channel',
                ),
            },
        ),
        EntityDefinition(
            name='reactions',
            actions=[Action.CREATE, Action.DELETE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/reactions.add',
                    action=Action.CREATE,
                    description='Adds a reaction (emoji) to a message',
                    body_fields=['channel', 'timestamp', 'name'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for adding a reaction',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel ID containing the message'},
                            'timestamp': {'type': 'string', 'description': 'Timestamp of the message to react to'},
                            'name': {'type': 'string', 'description': 'Reaction emoji name (without colons, e.g., "thumbsup")'},
                        },
                        'required': ['channel', 'timestamp', 'name'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from adding a reaction',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                        },
                    },
                    record_extractor='$',
                ),
                Action.DELETE: EndpointDefinition(
                    method='POST',
                    path='/reactions.remove',
                    action=Action.DELETE,
                    description='Removes a reaction (emoji) from a message',
                    body_fields=['channel', 'timestamp', 'name'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for removing a reaction from a message',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel ID containing the message'},
                            'timestamp': {'type': 'string', 'description': 'Timestamp of the message to remove reaction from'},
                            'name': {'type': 'string', 'description': 'Reaction emoji name to remove (without colons, e.g., "thumbsup")'},
                        },
                        'required': ['channel', 'timestamp', 'name'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from removing a reaction',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                        },
                    },
                    record_extractor='$',
                    ai_hints={
                        'summary': 'Remove reactions from Slack messages',
                        'when_to_use': 'When the user wants to remove a reaction (emoji) from a message',
                        'trigger_phrases': [
                            'remove reaction',
                            'unreact',
                            'remove emoji',
                            'take back reaction',
                        ],
                        'freshness': 'live',
                        'example_questions': ['Remove the :thumbsup: reaction from a message'],
                        'search_strategy': 'Use reactions.delete to remove a reaction from a message. Required params: channel, timestamp, and name (emoji name without colons).',
                    },
                ),
            },
        ),
        EntityDefinition(
            name='ephemeral_messages',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/chat.postEphemeral',
                    action=Action.CREATE,
                    description='Sends an ephemeral message to a user in a channel. Ephemeral messages are visible only to the target user and do not persist across sessions.',
                    body_fields=[
                        'channel',
                        'user',
                        'text',
                        'thread_ts',
                        'blocks',
                    ],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for sending an ephemeral message visible only to one user',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel, private group, or IM channel to send the ephemeral message to. Can be an encoded ID or a name.'},
                            'user': {'type': 'string', 'description': 'ID of the user who will receive the ephemeral message. The user should be in the channel specified by the channel argument.'},
                            'text': {'type': 'string', 'description': 'Message text content (supports mrkdwn formatting). How this field works depends on whether blocks are also provided.'},
                            'thread_ts': {'type': 'string', 'description': "Provide another message's ts value to post this ephemeral message in a thread. The thread must already be active."},
                            'blocks': {'type': 'string', 'description': 'A JSON-based array of structured blocks, presented as a URL-encoded string.'},
                        },
                        'required': ['channel', 'user', 'text'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from sending an ephemeral message',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'message_ts': {
                                'type': ['string', 'null'],
                                'description': 'Ephemeral message timestamp. Note this cannot be used with chat.update.',
                            },
                        },
                    },
                    record_extractor='$',
                    ai_hints={
                        'summary': 'Send ephemeral Slack messages visible only to one user',
                        'when_to_use': 'When the user wants to send a private/ephemeral message that only one person can see in a channel, or for agent check-ins that should not clutter the channel',
                        'trigger_phrases': [
                            'send ephemeral',
                            'private message in channel',
                            'whisper to user',
                            'send only to',
                        ],
                        'freshness': 'live',
                        'example_questions': ['Send an ephemeral message to a user in a channel', 'Whisper a reminder to a user in a channel'],
                        'search_strategy': 'Use ephemeral_messages.create to send a message visible only to a specific user in a channel. Required params: channel, user, and text.',
                    },
                ),
            },
        ),
        EntityDefinition(
            name='scheduled_messages',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/chat.scheduleMessage',
                    action=Action.CREATE,
                    description='Schedules a message for delivery to a channel at a specified time in the future. Messages can be scheduled up to 120 days in advance.',
                    body_fields=[
                        'channel',
                        'text',
                        'post_at',
                        'thread_ts',
                        'reply_broadcast',
                        'unfurl_links',
                        'unfurl_media',
                    ],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for scheduling a message for future delivery',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel, private group, or DM channel to send the scheduled message to. Can be an encoded ID or a name.'},
                            'text': {'type': 'string', 'description': 'Message text content (supports mrkdwn formatting). How this field works depends on whether blocks are also provided.'},
                            'post_at': {'type': 'integer', 'description': 'Unix timestamp representing the future time the message should post to Slack. Must be within 120 days.'},
                            'thread_ts': {'type': 'string', 'description': "Provide another message's ts value to make this message a reply. Avoid using a reply's ts value; use its parent instead."},
                            'reply_broadcast': {'type': 'boolean', 'description': 'Used in conjunction with thread_ts and indicates whether reply should be made visible to everyone in the channel. Defaults to false.'},
                            'unfurl_links': {'type': 'boolean', 'description': 'Pass true to enable unfurling of primarily text-based content.'},
                            'unfurl_media': {'type': 'boolean', 'description': 'Pass false to disable unfurling of media content.'},
                        },
                        'required': ['channel', 'text', 'post_at'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from scheduling a message',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'channel': {
                                'type': ['string', 'null'],
                                'description': 'Channel ID where the message will be posted',
                            },
                            'scheduled_message_id': {
                                'type': ['string', 'null'],
                                'description': 'ID of the scheduled message. Use with chat.deleteScheduledMessage to cancel.',
                            },
                            'post_at': {
                                'type': ['integer', 'null'],
                                'description': 'Unix timestamp when the message will be posted',
                            },
                            'message': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Content of a scheduled message',
                                        'properties': {
                                            'text': {
                                                'type': ['string', 'null'],
                                                'description': 'Message text content',
                                            },
                                            'username': {
                                                'type': ['string', 'null'],
                                                'description': 'Username that will post the message',
                                            },
                                            'bot_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Bot ID if scheduled by a bot',
                                            },
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Message type (e.g., "delayed_message")',
                                            },
                                            'subtype': {
                                                'type': ['string', 'null'],
                                                'description': 'Message subtype (e.g., "bot_message")',
                                            },
                                            'user': {
                                                'type': ['string', 'null'],
                                                'description': 'User ID who scheduled the message',
                                            },
                                            'team': {
                                                'type': ['string', 'null'],
                                                'description': 'Team ID of the workspace',
                                            },
                                            'app_id': {
                                                'type': ['string', 'null'],
                                                'description': 'App ID if scheduled by an app',
                                            },
                                            'bot_profile': {
                                                'type': ['object', 'null'],
                                                'description': 'Bot profile information if scheduled by a bot',
                                            },
                                            'blocks': {
                                                'type': ['array', 'null'],
                                                'description': 'Rich text block elements in the message',
                                                'items': {'type': 'object'},
                                            },
                                            'attachments': {
                                                'type': ['array', 'null'],
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Message attachment',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Attachment ID',
                                                        },
                                                        'fallback': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Fallback text',
                                                        },
                                                        'color': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Attachment color',
                                                        },
                                                        'pretext': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Pretext',
                                                        },
                                                        'author_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Author name',
                                                        },
                                                        'author_link': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Author link',
                                                        },
                                                        'author_icon': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Author icon URL',
                                                        },
                                                        'title': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Attachment title',
                                                        },
                                                        'title_link': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Title link',
                                                        },
                                                        'text': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Attachment text',
                                                        },
                                                        'fields': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'object'},
                                                            'description': 'Attachment fields',
                                                        },
                                                        'image_url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Image URL',
                                                        },
                                                        'thumb_url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Thumbnail URL',
                                                        },
                                                        'footer': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Footer text',
                                                        },
                                                        'footer_icon': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Footer icon URL',
                                                        },
                                                        'ts': {
                                                            'type': ['string', 'integer', 'null'],
                                                            'description': 'Timestamp',
                                                        },
                                                    },
                                                },
                                                'description': 'Message attachments',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The scheduled message content',
                            },
                        },
                    },
                    record_extractor='$',
                    ai_hints={
                        'summary': 'Schedule Slack messages for future delivery',
                        'when_to_use': 'When the user wants to schedule a message for later, set up reminders, or send end-of-day summaries at a specific time',
                        'trigger_phrases': [
                            'schedule a message',
                            'send later',
                            'post at',
                            'schedule for tomorrow',
                            'send a reminder at',
                        ],
                        'freshness': 'live',
                        'example_questions': ['Schedule a message in a channel for tomorrow at 9am', 'Send a reminder to a channel at 5pm today'],
                        'search_strategy': 'Use scheduled_messages.create to schedule a message for future delivery. Required params: channel, text, and post_at (Unix timestamp). Messages can be scheduled up to 120 days in advance.',
                    },
                ),
            },
        ),
        EntityDefinition(
            name='channel_archives',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/conversations.archive',
                    action=Action.CREATE,
                    description='Archives a conversation. Not all types of conversations can be archived.',
                    body_fields=['channel'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for archiving a channel',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'ID of the channel to archive'},
                        },
                        'required': ['channel'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from archiving a channel',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                        },
                    },
                    record_extractor='$',
                    ai_hints={
                        'summary': 'Archive Slack channels',
                        'when_to_use': 'When the user wants to archive a channel that is no longer active',
                        'trigger_phrases': ['archive channel', 'close channel', 'deactivate channel'],
                        'freshness': 'live',
                        'example_questions': ['Archive the #old-project channel'],
                        'search_strategy': 'Use channel_archives.create to archive a channel. Required param: channel (the channel ID to archive).',
                    },
                ),
            },
        ),
        EntityDefinition(
            name='channel_kicks',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/conversations.kick',
                    action=Action.CREATE,
                    description='Removes a user from a public or private channel',
                    body_fields=['channel', 'user'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for removing a user from a channel',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'ID of the channel to remove the user from'},
                            'user': {'type': 'string', 'description': 'User ID to be removed from the channel'},
                        },
                        'required': ['channel', 'user'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from removing a user from a channel',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'errors': {
                                'type': ['object', 'null'],
                                'description': 'Error details, empty object on success',
                            },
                        },
                    },
                    record_extractor='$',
                    ai_hints={
                        'summary': 'Remove users from Slack channels',
                        'when_to_use': 'When the user wants to remove or kick someone from a channel',
                        'trigger_phrases': ['remove user from channel', 'kick from channel', 'remove from channel'],
                        'freshness': 'live',
                        'example_questions': ['Remove a user from the #project channel'],
                        'search_strategy': 'Use channel_kicks.create to remove a user from a channel. Required params: channel and user (user ID to remove).',
                    },
                ),
            },
        ),
        EntityDefinition(
            name='pins',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/pins.add',
                    action=Action.CREATE,
                    description='Pins a message to a particular channel. Both channel and timestamp are required.',
                    body_fields=['channel', 'timestamp'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for pinning a message to a channel',
                        'properties': {
                            'channel': {'type': 'string', 'description': 'Channel ID to pin the message to'},
                            'timestamp': {'type': 'string', 'description': 'Timestamp of the message to pin'},
                        },
                        'required': ['channel', 'timestamp'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from pinning a message',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                        },
                    },
                    record_extractor='$',
                    ai_hints={
                        'summary': 'Pin messages to Slack channels',
                        'when_to_use': 'When the user wants to pin an important message to a channel for easy reference',
                        'trigger_phrases': ['pin message', 'pin to channel', 'pin this'],
                        'freshness': 'live',
                        'example_questions': ['Pin the latest message in a channel'],
                        'search_strategy': 'Use pins.create to pin a message to a channel. Required params: channel and timestamp (ts of the message to pin).',
                    },
                ),
            },
        ),
        EntityDefinition(
            name='bookmarks',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/bookmarks.add',
                    action=Action.CREATE,
                    description='Adds a bookmark (link) to a channel. Bookmarks appear in the channel header for easy access.',
                    body_fields=[
                        'channel_id',
                        'title',
                        'type',
                        'link',
                        'emoji',
                    ],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for adding a bookmark to a channel',
                        'properties': {
                            'channel_id': {'type': 'string', 'description': 'Channel ID to add the bookmark to'},
                            'title': {'type': 'string', 'description': 'Title for the bookmark'},
                            'type': {'type': 'string', 'description': 'Type of the bookmark (e.g., "link")'},
                            'link': {'type': 'string', 'description': 'URL to bookmark (required for link type). Must begin with http:// or https://.'},
                            'emoji': {'type': 'string', 'description': 'Emoji tag to apply to the bookmark (e.g., ":rocket:")'},
                        },
                        'required': ['channel_id', 'title', 'type'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from adding a bookmark',
                        'properties': {
                            'ok': {'type': 'boolean', 'description': 'Whether the request was successful'},
                            'bookmark': {
                                'type': 'object',
                                'description': 'A channel bookmark',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                        'description': 'Bookmark ID',
                                    },
                                    'channel_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Channel ID the bookmark belongs to',
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'Bookmark title',
                                    },
                                    'link': {
                                        'type': ['string', 'null'],
                                        'description': 'Bookmark URL',
                                    },
                                    'emoji': {
                                        'type': ['string', 'null'],
                                        'description': 'Emoji tag',
                                    },
                                    'icon_url': {
                                        'type': ['string', 'null'],
                                        'description': 'Icon URL (e.g., favicon)',
                                    },
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Bookmark type (e.g., "link")',
                                    },
                                    'entity_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Entity ID if bookmarking a message or file',
                                    },
                                    'date_created': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of bookmark creation',
                                    },
                                    'date_updated': {
                                        'type': ['integer', 'null'],
                                        'description': 'Unix timestamp of last update',
                                    },
                                    'rank': {
                                        'type': ['string', 'null'],
                                        'description': 'Sort rank',
                                    },
                                    'last_updated_by_user_id': {
                                        'type': ['string', 'null'],
                                        'description': 'User ID of last updater',
                                    },
                                    'last_updated_by_team_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Team ID of last updater',
                                    },
                                    'shortcut_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Shortcut ID if applicable',
                                    },
                                    'app_id': {
                                        'type': ['string', 'null'],
                                        'description': 'App ID if created by an app',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.bookmark',
                    ai_hints={
                        'summary': 'Add bookmarks to Slack channels',
                        'when_to_use': 'When the user wants to add a link or resource as a bookmark in a channel header',
                        'trigger_phrases': ['add bookmark', 'bookmark link', 'add link to channel'],
                        'freshness': 'live',
                        'example_questions': ['Add a bookmark to a channel with a link to our wiki'],
                        'search_strategy': 'Use bookmarks.create to add a bookmark to a channel. Required params: channel_id, title, and type. For links, also include the link URL.',
                    },
                ),
            },
        ),
    ],
    search_field_paths={
        'channel_members': ['channel_id', 'member_id'],
        'channels': [
            'context_team_id',
            'created',
            'creator',
            'id',
            'is_archived',
            'is_channel',
            'is_ext_shared',
            'is_general',
            'is_group',
            'is_im',
            'is_member',
            'is_mpim',
            'is_org_shared',
            'is_pending_ext_shared',
            'is_private',
            'is_read_only',
            'is_shared',
            'last_read',
            'locale',
            'name',
            'name_normalized',
            'num_members',
            'parent_conversation',
            'pending_connected_team_ids',
            'pending_connected_team_ids[]',
            'pending_shared',
            'pending_shared[]',
            'previous_names',
            'previous_names[]',
            'purpose',
            'purpose.creator',
            'purpose.last_set',
            'purpose.value',
            'shared_team_ids',
            'shared_team_ids[]',
            'topic',
            'topic.creator',
            'topic.last_set',
            'topic.value',
            'unlinked',
            'updated',
        ],
        'channel_messages': [
            'type',
            'subtype',
            'ts',
            'user',
            'text',
            'thread_ts',
            'reply_count',
            'reply_users_count',
            'latest_reply',
            'reply_users',
            'reply_users[]',
            'is_locked',
            'subscribed',
            'reactions',
            'reactions[]',
            'attachments',
            'attachments[]',
            'blocks',
            'blocks[]',
            'bot_id',
            'bot_profile',
            'team',
        ],
        'threads': [
            'type',
            'subtype',
            'ts',
            'user',
            'text',
            'thread_ts',
            'parent_user_id',
            'reply_count',
            'reply_users_count',
            'latest_reply',
            'reply_users',
            'reply_users[]',
            'is_locked',
            'subscribed',
            'blocks',
            'blocks[]',
            'bot_id',
            'team',
        ],
        'users': [
            'color',
            'deleted',
            'has_2fa',
            'id',
            'is_admin',
            'is_app_user',
            'is_bot',
            'is_email_confirmed',
            'is_forgotten',
            'is_invited_user',
            'is_owner',
            'is_primary_owner',
            'is_restricted',
            'is_ultra_restricted',
            'name',
            'profile',
            'profile.always_active',
            'profile.avatar_hash',
            'profile.display_name',
            'profile.display_name_normalized',
            'profile.email',
            'profile.fields',
            'profile.first_name',
            'profile.huddle_state',
            'profile.image_1024',
            'profile.image_192',
            'profile.image_24',
            'profile.image_32',
            'profile.image_48',
            'profile.image_512',
            'profile.image_72',
            'profile.image_original',
            'profile.last_name',
            'profile.phone',
            'profile.real_name',
            'profile.real_name_normalized',
            'profile.skype',
            'profile.status_emoji',
            'profile.status_emoji_display_info',
            'profile.status_emoji_display_info[]',
            'profile.status_expiration',
            'profile.status_text',
            'profile.status_text_canonical',
            'profile.team',
            'profile.title',
            'real_name',
            'team_id',
            'tz',
            'tz_label',
            'tz_offset',
            'updated',
            'who_can_share_contact_card',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all users in my Slack workspace',
            'Show me all public channels',
            'List members of a public channel',
            'Show me recent messages in a public channel',
            'Show me thread replies for a recent message',
            'List all channels I have access to',
            'Show me user details for a workspace member',
            'List channel members for a public channel',
            "Send a message to a channel saying 'Hello team!'",
            'Post a message in the general channel',
            'Update the most recent message in a channel',
            "Create a new public channel called 'project-updates'",
            "Create a private channel named 'team-internal'",
            "Rename a channel to 'new-channel-name'",
            "Set the topic for a channel to 'Daily standup notes'",
            'Update the purpose of a channel',
            'Add a thumbsup reaction to the latest message in a channel',
            'React with :rocket: to the latest message in a channel',
            "Reply to a recent thread with 'Thanks for the update!'",
            'Invite a user to a channel',
            'Add a team member to the #project-updates channel',
            'Send an ephemeral message to a user in a channel',
            'Whisper a private reminder to a user in #general',
            'Schedule a message in a channel for tomorrow at 9am',
            'Send a reminder to a channel at 5pm today',
            "Delete the bot's last message in a channel",
            'Remove the :thumbsup: reaction from a message',
            'Archive the #old-project channel',
            'Remove a user from the #team channel',
            'Pin the latest important message in a channel',
            'Add a bookmark link to a channel',
        ],
        context_store_search=['What messages were posted in channel {channel_id} last week?', 'Show me the conversation history for channel {channel_id}', 'Search for messages mentioning {keyword} in channel {channel_id}'],
        search=['What messages were posted in channel {channel_id} last week?', 'Show me the conversation history for channel {channel_id}', 'Search for messages mentioning {keyword} in channel {channel_id}'],
        unsupported=[
            'Delete channel {channel_id}',
            'Create a new user in the workspace',
            'Update user profile information',
            'Unarchive a channel',
        ],
    ),
    response_error_check=ResponseErrorCheck(
        field='ok',
        on_value=False,
        message_field='error',
    ),
)