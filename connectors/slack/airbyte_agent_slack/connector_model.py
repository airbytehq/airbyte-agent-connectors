"""
Connector model for slack.

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
from uuid import (
    UUID,
)

SlackConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('c2281cee-86f9-4a86-bb48-d23286b4c7bd'),
    name='slack',
    version='0.1.11',
    base_url='https://slack.com/api',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='bearerAuth',
                type=AuthType.BEARER,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AirbyteAuthConfig(
                    title='Token Authentication',
                    type='object',
                    required=['api_token'],
                    properties={
                        'api_token': AuthConfigFieldSpec(
                            title='API Token',
                            description='Your Slack Bot Token (xoxb-) or User Token (xoxp-)',
                        ),
                    },
                    auth_mapping={'token': '${api_token}'},
                    replication_auth_key_mapping={'credentials.api_token': 'api_token'},
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
                user_config_spec=AirbyteAuthConfig(
                    title='OAuth 2.0 Authentication',
                    type='object',
                    required=['client_id', 'client_secret', 'access_token'],
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
            actions=[Action.CREATE, Action.UPDATE],
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
                            },
                        },
                    },
                    record_extractor='$.channel',
                ),
            },
        ),
        EntityDefinition(
            name='reactions',
            actions=[Action.CREATE],
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
)