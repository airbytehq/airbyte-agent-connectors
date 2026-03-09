"""
Connector model for zendesk-talk.

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

ZendeskTalkConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('c8630570-086d-4a40-99ae-ea5b18673071'),
    name='zendesk-talk',
    base_url='https://{subdomain}.zendesk.com/api/v2/channels/voice',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='zendeskOAuth',
                type=AuthType.OAUTH2,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'refresh_url': 'https://{{subdomain}}.zendesk.com/oauth/tokens',
                },
                user_config_spec=AirbyteAuthConfig(
                    title='OAuth 2.0',
                    description='Zendesk OAuth 2.0 authentication',
                    type='object',
                    required=['access_token'],
                    properties={
                        'access_token': AuthConfigFieldSpec(
                            title='Access Token',
                            description='OAuth 2.0 access token',
                        ),
                        'refresh_token': AuthConfigFieldSpec(
                            title='Refresh Token',
                            description='OAuth 2.0 refresh token (optional)',
                        ),
                        'client_id': AuthConfigFieldSpec(
                            title='Client ID',
                            description='OAuth client ID',
                        ),
                        'client_secret': AuthConfigFieldSpec(
                            title='Client Secret',
                            description='OAuth client secret',
                        ),
                    },
                    auth_mapping={
                        'access_token': '${access_token}',
                        'refresh_token': '${refresh_token}',
                        'client_id': '${client_id}',
                        'client_secret': '${client_secret}',
                    },
                    replication_auth_key_mapping={
                        'credentials.access_token': 'access_token',
                        'credentials.refresh_token': 'refresh_token',
                        'credentials.client_id': 'client_id',
                        'credentials.client_secret': 'client_secret',
                    },
                    replication_auth_key_constants={'credentials.auth_type': 'oauth2_refresh'},
                ),
                untested=True,
            ),
            AuthOption(
                scheme_name='zendeskAPIToken',
                type=AuthType.BASIC,
                user_config_spec=AirbyteAuthConfig(
                    title='API Token',
                    description='Authenticate using email and API token',
                    type='object',
                    required=['email', 'api_token'],
                    properties={
                        'email': AuthConfigFieldSpec(
                            title='Email Address',
                            description='Your Zendesk account email address',
                            format='email',
                        ),
                        'api_token': AuthConfigFieldSpec(
                            title='API Token',
                            description='Your Zendesk API token from Admin Center',
                        ),
                    },
                    auth_mapping={'username': '${email}/token', 'password': '${api_token}'},
                    replication_auth_key_mapping={'credentials.email': 'email', 'credentials.api_token': 'api_token'},
                    replication_auth_key_constants={'credentials.auth_type': 'api_token'},
                ),
            ),
        ],
    ),
    entities=[
        EntityDefinition(
            name='phone_numbers',
            stream_name='phone_numbers',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/phone_numbers',
                    action=Action.LIST,
                    description='Returns a list of all phone numbers in the Zendesk Talk account',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'phone_numbers': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique phone number identifier',
                                        },
                                        'brand_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'ID of brand associated with the phone number',
                                        },
                                        'call_recording_consent': {
                                            'type': ['null', 'string'],
                                            'description': 'What call recording consent is set to',
                                        },
                                        'capabilities': {
                                            'type': ['null', 'object'],
                                            'description': 'Phone number capabilities (sms, mms, voice)',
                                            'properties': {
                                                'sms': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'mms': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'voice': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'emergency_address': {
                                                    'type': ['null', 'boolean'],
                                                },
                                            },
                                        },
                                        'categorised_greetings': {
                                            'type': ['null', 'object'],
                                            'description': 'Greeting category IDs and names',
                                        },
                                        'categorised_greetings_with_sub_settings': {
                                            'type': ['null', 'object'],
                                            'description': 'Greeting categories with associated settings',
                                        },
                                        'country_code': {
                                            'type': ['null', 'string'],
                                            'description': 'ISO country code for the number',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'Date and time the phone number was created',
                                        },
                                        'default_greeting_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'Names of default system greetings',
                                            'items': {'type': 'string'},
                                        },
                                        'default_group_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Default group ID',
                                        },
                                        'display_number': {
                                            'type': ['null', 'string'],
                                            'description': 'Formatted phone number',
                                        },
                                        'external': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is an external caller ID number',
                                        },
                                        'failover_number': {
                                            'type': ['null', 'string'],
                                            'description': 'Failover number associated with the phone number',
                                        },
                                        'greeting_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'Custom greeting IDs associated with the phone number',
                                            'items': {'type': 'integer'},
                                        },
                                        'group_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'Array of associated group IDs',
                                            'items': {'type': 'integer'},
                                        },
                                        'ivr_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'ID of IVR associated with the phone number',
                                        },
                                        'line_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Type of line (phone or digital)',
                                        },
                                        'location': {
                                            'type': ['null', 'string'],
                                            'description': 'Geographical location of the number',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Nickname if set, otherwise the display number',
                                        },
                                        'nickname': {
                                            'type': ['null', 'string'],
                                            'description': 'Nickname of the phone number',
                                        },
                                        'number': {
                                            'type': ['null', 'string'],
                                            'description': 'Phone number digits',
                                        },
                                        'outbound_enabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether outbound calls are enabled',
                                        },
                                        'priority': {
                                            'type': ['null', 'integer'],
                                            'description': 'Priority level of the phone number',
                                        },
                                        'recorded': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether calls are recorded',
                                        },
                                        'schedule_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'ID of schedule associated with the phone number',
                                        },
                                        'sms_enabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether SMS is enabled',
                                        },
                                        'sms_group_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Group associated with SMS',
                                        },
                                        'token': {
                                            'type': ['null', 'string'],
                                            'description': 'Generated token unique for the phone number',
                                        },
                                        'toll_free': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the number is toll-free',
                                        },
                                        'transcription': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether voicemail transcription is enabled',
                                        },
                                        'voice_enabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether voice is enabled',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'phone_numbers',
                                    'x-airbyte-stream-name': 'phone_numbers',
                                },
                            },
                            'next_page': {
                                'type': ['null', 'string'],
                                'description': 'URL for the next page of results',
                            },
                            'previous_page': {
                                'type': ['null', 'string'],
                                'description': 'URL for the previous page of results',
                            },
                            'count': {
                                'type': ['null', 'integer'],
                                'description': 'Total count of phone numbers',
                            },
                        },
                    },
                    record_extractor='$.phone_numbers',
                    meta_extractor={'next_page': '$.next_page'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/phone_numbers/{phone_number_id}',
                    action=Action.GET,
                    description='Retrieves a single phone number by ID',
                    path_params=['phone_number_id'],
                    path_params_schema={
                        'phone_number_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'phone_number': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique phone number identifier',
                                    },
                                    'brand_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'ID of brand associated with the phone number',
                                    },
                                    'call_recording_consent': {
                                        'type': ['null', 'string'],
                                        'description': 'What call recording consent is set to',
                                    },
                                    'capabilities': {
                                        'type': ['null', 'object'],
                                        'description': 'Phone number capabilities (sms, mms, voice)',
                                        'properties': {
                                            'sms': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'mms': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'voice': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'emergency_address': {
                                                'type': ['null', 'boolean'],
                                            },
                                        },
                                    },
                                    'categorised_greetings': {
                                        'type': ['null', 'object'],
                                        'description': 'Greeting category IDs and names',
                                    },
                                    'categorised_greetings_with_sub_settings': {
                                        'type': ['null', 'object'],
                                        'description': 'Greeting categories with associated settings',
                                    },
                                    'country_code': {
                                        'type': ['null', 'string'],
                                        'description': 'ISO country code for the number',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'description': 'Date and time the phone number was created',
                                    },
                                    'default_greeting_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'Names of default system greetings',
                                        'items': {'type': 'string'},
                                    },
                                    'default_group_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Default group ID',
                                    },
                                    'display_number': {
                                        'type': ['null', 'string'],
                                        'description': 'Formatted phone number',
                                    },
                                    'external': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether this is an external caller ID number',
                                    },
                                    'failover_number': {
                                        'type': ['null', 'string'],
                                        'description': 'Failover number associated with the phone number',
                                    },
                                    'greeting_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'Custom greeting IDs associated with the phone number',
                                        'items': {'type': 'integer'},
                                    },
                                    'group_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'Array of associated group IDs',
                                        'items': {'type': 'integer'},
                                    },
                                    'ivr_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'ID of IVR associated with the phone number',
                                    },
                                    'line_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Type of line (phone or digital)',
                                    },
                                    'location': {
                                        'type': ['null', 'string'],
                                        'description': 'Geographical location of the number',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Nickname if set, otherwise the display number',
                                    },
                                    'nickname': {
                                        'type': ['null', 'string'],
                                        'description': 'Nickname of the phone number',
                                    },
                                    'number': {
                                        'type': ['null', 'string'],
                                        'description': 'Phone number digits',
                                    },
                                    'outbound_enabled': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether outbound calls are enabled',
                                    },
                                    'priority': {
                                        'type': ['null', 'integer'],
                                        'description': 'Priority level of the phone number',
                                    },
                                    'recorded': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether calls are recorded',
                                    },
                                    'schedule_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'ID of schedule associated with the phone number',
                                    },
                                    'sms_enabled': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether SMS is enabled',
                                    },
                                    'sms_group_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Group associated with SMS',
                                    },
                                    'token': {
                                        'type': ['null', 'string'],
                                        'description': 'Generated token unique for the phone number',
                                    },
                                    'toll_free': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the number is toll-free',
                                    },
                                    'transcription': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether voicemail transcription is enabled',
                                    },
                                    'voice_enabled': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether voice is enabled',
                                    },
                                },
                                'x-airbyte-entity-name': 'phone_numbers',
                                'x-airbyte-stream-name': 'phone_numbers',
                            },
                        },
                    },
                    record_extractor='$.phone_number',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique phone number identifier',
                    },
                    'brand_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of brand associated with the phone number',
                    },
                    'call_recording_consent': {
                        'type': ['null', 'string'],
                        'description': 'What call recording consent is set to',
                    },
                    'capabilities': {
                        'type': ['null', 'object'],
                        'description': 'Phone number capabilities (sms, mms, voice)',
                        'properties': {
                            'sms': {
                                'type': ['null', 'boolean'],
                            },
                            'mms': {
                                'type': ['null', 'boolean'],
                            },
                            'voice': {
                                'type': ['null', 'boolean'],
                            },
                            'emergency_address': {
                                'type': ['null', 'boolean'],
                            },
                        },
                    },
                    'categorised_greetings': {
                        'type': ['null', 'object'],
                        'description': 'Greeting category IDs and names',
                    },
                    'categorised_greetings_with_sub_settings': {
                        'type': ['null', 'object'],
                        'description': 'Greeting categories with associated settings',
                    },
                    'country_code': {
                        'type': ['null', 'string'],
                        'description': 'ISO country code for the number',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'Date and time the phone number was created',
                    },
                    'default_greeting_ids': {
                        'type': ['null', 'array'],
                        'description': 'Names of default system greetings',
                        'items': {'type': 'string'},
                    },
                    'default_group_id': {
                        'type': ['null', 'integer'],
                        'description': 'Default group ID',
                    },
                    'display_number': {
                        'type': ['null', 'string'],
                        'description': 'Formatted phone number',
                    },
                    'external': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is an external caller ID number',
                    },
                    'failover_number': {
                        'type': ['null', 'string'],
                        'description': 'Failover number associated with the phone number',
                    },
                    'greeting_ids': {
                        'type': ['null', 'array'],
                        'description': 'Custom greeting IDs associated with the phone number',
                        'items': {'type': 'integer'},
                    },
                    'group_ids': {
                        'type': ['null', 'array'],
                        'description': 'Array of associated group IDs',
                        'items': {'type': 'integer'},
                    },
                    'ivr_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of IVR associated with the phone number',
                    },
                    'line_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of line (phone or digital)',
                    },
                    'location': {
                        'type': ['null', 'string'],
                        'description': 'Geographical location of the number',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Nickname if set, otherwise the display number',
                    },
                    'nickname': {
                        'type': ['null', 'string'],
                        'description': 'Nickname of the phone number',
                    },
                    'number': {
                        'type': ['null', 'string'],
                        'description': 'Phone number digits',
                    },
                    'outbound_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether outbound calls are enabled',
                    },
                    'priority': {
                        'type': ['null', 'integer'],
                        'description': 'Priority level of the phone number',
                    },
                    'recorded': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether calls are recorded',
                    },
                    'schedule_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of schedule associated with the phone number',
                    },
                    'sms_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether SMS is enabled',
                    },
                    'sms_group_id': {
                        'type': ['null', 'integer'],
                        'description': 'Group associated with SMS',
                    },
                    'token': {
                        'type': ['null', 'string'],
                        'description': 'Generated token unique for the phone number',
                    },
                    'toll_free': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the number is toll-free',
                    },
                    'transcription': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether voicemail transcription is enabled',
                    },
                    'voice_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether voice is enabled',
                    },
                },
                'x-airbyte-entity-name': 'phone_numbers',
                'x-airbyte-stream-name': 'phone_numbers',
            },
        ),
        EntityDefinition(
            name='addresses',
            stream_name='addresses',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/addresses',
                    action=Action.LIST,
                    description='Returns a list of all addresses in the Zendesk Talk account',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'addresses': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique address identifier',
                                        },
                                        'city': {
                                            'type': ['null', 'string'],
                                            'description': 'City of the address',
                                        },
                                        'country_code': {
                                            'type': ['null', 'string'],
                                            'description': 'ISO country code',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the address',
                                        },
                                        'provider_reference': {
                                            'type': ['null', 'string'],
                                            'description': 'Provider reference of the address',
                                        },
                                        'province': {
                                            'type': ['null', 'string'],
                                            'description': 'Province of the address',
                                        },
                                        'state': {
                                            'type': ['null', 'string'],
                                            'description': 'State of the address',
                                        },
                                        'street': {
                                            'type': ['null', 'string'],
                                            'description': 'Street of the address',
                                        },
                                        'zip': {
                                            'type': ['null', 'string'],
                                            'description': 'Zip code of the address',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'addresses',
                                    'x-airbyte-stream-name': 'addresses',
                                },
                            },
                            'next_page': {
                                'type': ['null', 'string'],
                            },
                            'previous_page': {
                                'type': ['null', 'string'],
                            },
                            'count': {
                                'type': ['null', 'integer'],
                            },
                        },
                    },
                    record_extractor='$.addresses',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/addresses/{address_id}',
                    action=Action.GET,
                    description='Retrieves a single address by ID',
                    path_params=['address_id'],
                    path_params_schema={
                        'address_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'address': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique address identifier',
                                    },
                                    'city': {
                                        'type': ['null', 'string'],
                                        'description': 'City of the address',
                                    },
                                    'country_code': {
                                        'type': ['null', 'string'],
                                        'description': 'ISO country code',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the address',
                                    },
                                    'provider_reference': {
                                        'type': ['null', 'string'],
                                        'description': 'Provider reference of the address',
                                    },
                                    'province': {
                                        'type': ['null', 'string'],
                                        'description': 'Province of the address',
                                    },
                                    'state': {
                                        'type': ['null', 'string'],
                                        'description': 'State of the address',
                                    },
                                    'street': {
                                        'type': ['null', 'string'],
                                        'description': 'Street of the address',
                                    },
                                    'zip': {
                                        'type': ['null', 'string'],
                                        'description': 'Zip code of the address',
                                    },
                                },
                                'x-airbyte-entity-name': 'addresses',
                                'x-airbyte-stream-name': 'addresses',
                            },
                        },
                    },
                    record_extractor='$.address',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique address identifier',
                    },
                    'city': {
                        'type': ['null', 'string'],
                        'description': 'City of the address',
                    },
                    'country_code': {
                        'type': ['null', 'string'],
                        'description': 'ISO country code',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the address',
                    },
                    'provider_reference': {
                        'type': ['null', 'string'],
                        'description': 'Provider reference of the address',
                    },
                    'province': {
                        'type': ['null', 'string'],
                        'description': 'Province of the address',
                    },
                    'state': {
                        'type': ['null', 'string'],
                        'description': 'State of the address',
                    },
                    'street': {
                        'type': ['null', 'string'],
                        'description': 'Street of the address',
                    },
                    'zip': {
                        'type': ['null', 'string'],
                        'description': 'Zip code of the address',
                    },
                },
                'x-airbyte-entity-name': 'addresses',
                'x-airbyte-stream-name': 'addresses',
            },
        ),
        EntityDefinition(
            name='greetings',
            stream_name='greetings',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/greetings',
                    action=Action.LIST,
                    description='Returns a list of all greetings in the Zendesk Talk account',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'greetings': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Greeting ID',
                                        },
                                        'active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the greeting is associated with phone numbers',
                                        },
                                        'audio_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Audio file name',
                                        },
                                        'audio_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Path to the greeting sound file',
                                        },
                                        'category_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'ID of the greeting category',
                                        },
                                        'default': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is a system default greeting',
                                        },
                                        'default_lang': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the greeting has a default language',
                                        },
                                        'has_sub_settings': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Sub-settings for categorized greetings',
                                        },
                                        'ivr_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'IDs of IVRs associated with the greeting',
                                            'items': {
                                                'type': ['string', 'integer'],
                                            },
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the greeting',
                                        },
                                        'pending': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the greeting is pending',
                                        },
                                        'phone_number_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'IDs of phone numbers associated with the greeting',
                                            'items': {
                                                'type': ['integer', 'string'],
                                            },
                                        },
                                        'upload_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Upload ID associated with the greeting',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'greetings',
                                    'x-airbyte-stream-name': 'greetings',
                                },
                            },
                            'next_page': {
                                'type': ['null', 'string'],
                            },
                            'previous_page': {
                                'type': ['null', 'string'],
                            },
                            'count': {
                                'type': ['null', 'integer'],
                            },
                        },
                    },
                    record_extractor='$.greetings',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/greetings/{greeting_id}',
                    action=Action.GET,
                    description='Retrieves a single greeting by ID',
                    path_params=['greeting_id'],
                    path_params_schema={
                        'greeting_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'greeting': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'string'],
                                        'description': 'Greeting ID',
                                    },
                                    'active': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the greeting is associated with phone numbers',
                                    },
                                    'audio_name': {
                                        'type': ['null', 'string'],
                                        'description': 'Audio file name',
                                    },
                                    'audio_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Path to the greeting sound file',
                                    },
                                    'category_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'ID of the greeting category',
                                    },
                                    'default': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether this is a system default greeting',
                                    },
                                    'default_lang': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the greeting has a default language',
                                    },
                                    'has_sub_settings': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Sub-settings for categorized greetings',
                                    },
                                    'ivr_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'IDs of IVRs associated with the greeting',
                                        'items': {
                                            'type': ['string', 'integer'],
                                        },
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the greeting',
                                    },
                                    'pending': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the greeting is pending',
                                    },
                                    'phone_number_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'IDs of phone numbers associated with the greeting',
                                        'items': {
                                            'type': ['integer', 'string'],
                                        },
                                    },
                                    'upload_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Upload ID associated with the greeting',
                                    },
                                },
                                'x-airbyte-entity-name': 'greetings',
                                'x-airbyte-stream-name': 'greetings',
                            },
                        },
                    },
                    record_extractor='$.greeting',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Greeting ID',
                    },
                    'active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the greeting is associated with phone numbers',
                    },
                    'audio_name': {
                        'type': ['null', 'string'],
                        'description': 'Audio file name',
                    },
                    'audio_url': {
                        'type': ['null', 'string'],
                        'description': 'Path to the greeting sound file',
                    },
                    'category_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the greeting category',
                    },
                    'default': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is a system default greeting',
                    },
                    'default_lang': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the greeting has a default language',
                    },
                    'has_sub_settings': {
                        'type': ['null', 'boolean'],
                        'description': 'Sub-settings for categorized greetings',
                    },
                    'ivr_ids': {
                        'type': ['null', 'array'],
                        'description': 'IDs of IVRs associated with the greeting',
                        'items': {
                            'type': ['string', 'integer'],
                        },
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the greeting',
                    },
                    'pending': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the greeting is pending',
                    },
                    'phone_number_ids': {
                        'type': ['null', 'array'],
                        'description': 'IDs of phone numbers associated with the greeting',
                        'items': {
                            'type': ['integer', 'string'],
                        },
                    },
                    'upload_id': {
                        'type': ['null', 'integer'],
                        'description': 'Upload ID associated with the greeting',
                    },
                },
                'x-airbyte-entity-name': 'greetings',
                'x-airbyte-stream-name': 'greetings',
            },
        ),
        EntityDefinition(
            name='greeting_categories',
            stream_name='greeting_categories',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/greeting_categories',
                    action=Action.LIST,
                    description='Returns a list of all greeting categories',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'greeting_categories': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Greeting category ID',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the greeting category',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'greeting_categories',
                                    'x-airbyte-stream-name': 'greeting_categories',
                                },
                            },
                            'next_page': {
                                'type': ['null', 'string'],
                            },
                            'previous_page': {
                                'type': ['null', 'string'],
                            },
                            'count': {
                                'type': ['null', 'integer'],
                            },
                        },
                    },
                    record_extractor='$.greeting_categories',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/greeting_categories/{greeting_category_id}',
                    action=Action.GET,
                    description='Retrieves a single greeting category by ID',
                    path_params=['greeting_category_id'],
                    path_params_schema={
                        'greeting_category_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'greeting_category': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Greeting category ID',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the greeting category',
                                    },
                                },
                                'x-airbyte-entity-name': 'greeting_categories',
                                'x-airbyte-stream-name': 'greeting_categories',
                            },
                        },
                    },
                    record_extractor='$.greeting_category',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Greeting category ID',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the greeting category',
                    },
                },
                'x-airbyte-entity-name': 'greeting_categories',
                'x-airbyte-stream-name': 'greeting_categories',
            },
        ),
        EntityDefinition(
            name='ivrs',
            stream_name='ivrs',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ivr',
                    action=Action.LIST,
                    description='Returns a list of all IVR configurations',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'ivrs': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'IVR ID',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the IVR',
                                        },
                                        'phone_number_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'IDs of phone numbers configured with this IVR',
                                            'items': {
                                                'type': ['string', 'integer'],
                                            },
                                        },
                                        'phone_number_names': {
                                            'type': ['null', 'array'],
                                            'description': 'Names of phone numbers configured with this IVR',
                                            'items': {
                                                'type': ['string', 'integer'],
                                            },
                                        },
                                        'menus': {
                                            'type': ['null', 'array'],
                                            'description': 'List of IVR menus',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'name': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'default': {
                                                        'type': ['null', 'boolean'],
                                                    },
                                                    'greeting_id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'routes': {
                                                        'type': ['null', 'array'],
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'id': {
                                                                    'type': ['null', 'integer'],
                                                                },
                                                                'action': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'greeting': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'keypress': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'option_text': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'options': {
                                                                    'type': ['null', 'object'],
                                                                },
                                                                'overflow_options': {
                                                                    'type': ['null', 'array'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'ivrs',
                                    'x-airbyte-stream-name': 'ivrs',
                                },
                            },
                            'next_page': {
                                'type': ['null', 'string'],
                            },
                            'previous_page': {
                                'type': ['null', 'string'],
                            },
                            'count': {
                                'type': ['null', 'integer'],
                            },
                        },
                    },
                    record_extractor='$.ivrs',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/ivr/{ivr_id}',
                    action=Action.GET,
                    description='Retrieves a single IVR configuration by ID',
                    path_params=['ivr_id'],
                    path_params_schema={
                        'ivr_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'ivr': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'IVR ID',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the IVR',
                                    },
                                    'phone_number_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'IDs of phone numbers configured with this IVR',
                                        'items': {
                                            'type': ['string', 'integer'],
                                        },
                                    },
                                    'phone_number_names': {
                                        'type': ['null', 'array'],
                                        'description': 'Names of phone numbers configured with this IVR',
                                        'items': {
                                            'type': ['string', 'integer'],
                                        },
                                    },
                                    'menus': {
                                        'type': ['null', 'array'],
                                        'description': 'List of IVR menus',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                },
                                                'default': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'greeting_id': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'routes': {
                                                    'type': ['null', 'array'],
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'integer'],
                                                            },
                                                            'action': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'greeting': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'keypress': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'option_text': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'options': {
                                                                'type': ['null', 'object'],
                                                            },
                                                            'overflow_options': {
                                                                'type': ['null', 'array'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'x-airbyte-entity-name': 'ivrs',
                                'x-airbyte-stream-name': 'ivrs',
                            },
                        },
                    },
                    record_extractor='$.ivr',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'IVR ID',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the IVR',
                    },
                    'phone_number_ids': {
                        'type': ['null', 'array'],
                        'description': 'IDs of phone numbers configured with this IVR',
                        'items': {
                            'type': ['string', 'integer'],
                        },
                    },
                    'phone_number_names': {
                        'type': ['null', 'array'],
                        'description': 'Names of phone numbers configured with this IVR',
                        'items': {
                            'type': ['string', 'integer'],
                        },
                    },
                    'menus': {
                        'type': ['null', 'array'],
                        'description': 'List of IVR menus',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'default': {
                                    'type': ['null', 'boolean'],
                                },
                                'greeting_id': {
                                    'type': ['null', 'integer'],
                                },
                                'routes': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'action': {
                                                'type': ['null', 'string'],
                                            },
                                            'greeting': {
                                                'type': ['null', 'string'],
                                            },
                                            'keypress': {
                                                'type': ['null', 'string'],
                                            },
                                            'option_text': {
                                                'type': ['null', 'string'],
                                            },
                                            'options': {
                                                'type': ['null', 'object'],
                                            },
                                            'overflow_options': {
                                                'type': ['null', 'array'],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'ivrs',
                'x-airbyte-stream-name': 'ivrs',
            },
        ),
        EntityDefinition(
            name='agents_activity',
            stream_name='agents_activity',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/stats/agents_activity',
                    action=Action.LIST,
                    description='Returns activity statistics for all agents for the current day',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'agents_activity': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'agent_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Agent ID',
                                        },
                                        'agent_state': {
                                            'type': ['null', 'string'],
                                            'description': 'Agent state: online, offline, away, or transfers_only',
                                        },
                                        'available_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total time agent was available to answer calls',
                                        },
                                        'avatar_url': {
                                            'type': ['null', 'string'],
                                            'description': 'URL to agent avatar',
                                        },
                                        'away_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total time agent was set to away',
                                        },
                                        'call_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Agent call status: on_call, wrap_up, or null',
                                        },
                                        'calls_accepted': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total calls accepted',
                                        },
                                        'calls_denied': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total calls denied',
                                        },
                                        'calls_missed': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total calls missed',
                                        },
                                        'forwarding_number': {
                                            'type': ['null', 'string'],
                                            'description': 'Forwarding number set by the agent',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Agent name',
                                        },
                                        'online_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total online time',
                                        },
                                        'total_call_duration': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total call duration',
                                        },
                                        'total_talk_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total talk time (excludes hold)',
                                        },
                                        'total_wrap_up_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total wrap-up time',
                                        },
                                        'transfers_only_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total time in transfers-only mode',
                                        },
                                        'via': {
                                            'type': ['null', 'string'],
                                            'description': 'Channel the agent is registered on',
                                        },
                                        'accepted_third_party_conferences': {
                                            'type': ['null', 'integer'],
                                            'description': 'Accepted third party conferences',
                                        },
                                        'accepted_transfers': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total transfers accepted',
                                        },
                                        'average_hold_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Average hold time per call',
                                        },
                                        'average_talk_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Average talk time per call',
                                        },
                                        'average_wrap_up_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Average wrap-up time per call',
                                        },
                                        'calls_put_on_hold': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total calls placed on hold',
                                        },
                                        'started_third_party_conferences': {
                                            'type': ['null', 'integer'],
                                            'description': 'Started third party conferences',
                                        },
                                        'started_transfers': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total transfers started',
                                        },
                                        'total_hold_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total hold time across all calls',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'agents_activity',
                                    'x-airbyte-stream-name': 'agents_activity',
                                },
                            },
                            'next_page': {
                                'type': ['null', 'string'],
                            },
                            'previous_page': {
                                'type': ['null', 'string'],
                            },
                            'count': {
                                'type': ['null', 'integer'],
                            },
                        },
                    },
                    record_extractor='$.agents_activity',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'agent_id': {
                        'type': ['null', 'integer'],
                        'description': 'Agent ID',
                    },
                    'agent_state': {
                        'type': ['null', 'string'],
                        'description': 'Agent state: online, offline, away, or transfers_only',
                    },
                    'available_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total time agent was available to answer calls',
                    },
                    'avatar_url': {
                        'type': ['null', 'string'],
                        'description': 'URL to agent avatar',
                    },
                    'away_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total time agent was set to away',
                    },
                    'call_status': {
                        'type': ['null', 'string'],
                        'description': 'Agent call status: on_call, wrap_up, or null',
                    },
                    'calls_accepted': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls accepted',
                    },
                    'calls_denied': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls denied',
                    },
                    'calls_missed': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls missed',
                    },
                    'forwarding_number': {
                        'type': ['null', 'string'],
                        'description': 'Forwarding number set by the agent',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Agent name',
                    },
                    'online_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total online time',
                    },
                    'total_call_duration': {
                        'type': ['null', 'integer'],
                        'description': 'Total call duration',
                    },
                    'total_talk_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total talk time (excludes hold)',
                    },
                    'total_wrap_up_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total wrap-up time',
                    },
                    'transfers_only_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total time in transfers-only mode',
                    },
                    'via': {
                        'type': ['null', 'string'],
                        'description': 'Channel the agent is registered on',
                    },
                    'accepted_third_party_conferences': {
                        'type': ['null', 'integer'],
                        'description': 'Accepted third party conferences',
                    },
                    'accepted_transfers': {
                        'type': ['null', 'integer'],
                        'description': 'Total transfers accepted',
                    },
                    'average_hold_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average hold time per call',
                    },
                    'average_talk_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average talk time per call',
                    },
                    'average_wrap_up_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average wrap-up time per call',
                    },
                    'calls_put_on_hold': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls placed on hold',
                    },
                    'started_third_party_conferences': {
                        'type': ['null', 'integer'],
                        'description': 'Started third party conferences',
                    },
                    'started_transfers': {
                        'type': ['null', 'integer'],
                        'description': 'Total transfers started',
                    },
                    'total_hold_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total hold time across all calls',
                    },
                },
                'x-airbyte-entity-name': 'agents_activity',
                'x-airbyte-stream-name': 'agents_activity',
            },
        ),
        EntityDefinition(
            name='agents_overview',
            stream_name='agents_overview',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/stats/agents_overview',
                    action=Action.LIST,
                    description='Returns overview statistics for all agents for the current day',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'agents_overview': {
                                'type': 'object',
                                'properties': {
                                    'average_calls_accepted': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average calls accepted',
                                    },
                                    'average_calls_denied': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average calls denied',
                                    },
                                    'average_calls_missed': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average calls missed',
                                    },
                                    'average_wrap_up_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average wrap-up time',
                                    },
                                    'total_calls_accepted': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total calls accepted',
                                    },
                                    'total_calls_denied': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total calls denied',
                                    },
                                    'total_calls_missed': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total calls missed',
                                    },
                                    'total_talk_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total talk time',
                                    },
                                    'total_wrap_up_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total wrap-up time',
                                    },
                                    'average_accepted_transfers': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average accepted transfers',
                                    },
                                    'average_available_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average available time',
                                    },
                                    'average_away_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average away time',
                                    },
                                    'average_calls_put_on_hold': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average calls put on hold',
                                    },
                                    'average_hold_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average hold time',
                                    },
                                    'average_online_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average online time',
                                    },
                                    'average_started_transfers': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average started transfers',
                                    },
                                    'average_talk_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average talk time',
                                    },
                                    'average_transfers_only_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average transfers-only time',
                                    },
                                    'current_timestamp': {
                                        'type': ['null', 'integer'],
                                        'description': 'Current timestamp',
                                    },
                                    'total_accepted_transfers': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total accepted transfers',
                                    },
                                    'total_calls_put_on_hold': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total calls put on hold',
                                    },
                                    'total_hold_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total hold time',
                                    },
                                    'total_started_transfers': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total started transfers',
                                    },
                                },
                                'x-airbyte-entity-name': 'agents_overview',
                                'x-airbyte-stream-name': 'agents_overview',
                            },
                        },
                    },
                    record_extractor='$.agents_overview',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'average_calls_accepted': {
                        'type': ['null', 'integer'],
                        'description': 'Average calls accepted',
                    },
                    'average_calls_denied': {
                        'type': ['null', 'integer'],
                        'description': 'Average calls denied',
                    },
                    'average_calls_missed': {
                        'type': ['null', 'integer'],
                        'description': 'Average calls missed',
                    },
                    'average_wrap_up_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average wrap-up time',
                    },
                    'total_calls_accepted': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls accepted',
                    },
                    'total_calls_denied': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls denied',
                    },
                    'total_calls_missed': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls missed',
                    },
                    'total_talk_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total talk time',
                    },
                    'total_wrap_up_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total wrap-up time',
                    },
                    'average_accepted_transfers': {
                        'type': ['null', 'integer'],
                        'description': 'Average accepted transfers',
                    },
                    'average_available_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average available time',
                    },
                    'average_away_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average away time',
                    },
                    'average_calls_put_on_hold': {
                        'type': ['null', 'integer'],
                        'description': 'Average calls put on hold',
                    },
                    'average_hold_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average hold time',
                    },
                    'average_online_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average online time',
                    },
                    'average_started_transfers': {
                        'type': ['null', 'integer'],
                        'description': 'Average started transfers',
                    },
                    'average_talk_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average talk time',
                    },
                    'average_transfers_only_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average transfers-only time',
                    },
                    'current_timestamp': {
                        'type': ['null', 'integer'],
                        'description': 'Current timestamp',
                    },
                    'total_accepted_transfers': {
                        'type': ['null', 'integer'],
                        'description': 'Total accepted transfers',
                    },
                    'total_calls_put_on_hold': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls put on hold',
                    },
                    'total_hold_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total hold time',
                    },
                    'total_started_transfers': {
                        'type': ['null', 'integer'],
                        'description': 'Total started transfers',
                    },
                },
                'x-airbyte-entity-name': 'agents_overview',
                'x-airbyte-stream-name': 'agents_overview',
            },
        ),
        EntityDefinition(
            name='account_overview',
            stream_name='account_overview',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/stats/account_overview',
                    action=Action.LIST,
                    description='Returns overview statistics for the account for the current day',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'account_overview': {
                                'type': 'object',
                                'properties': {
                                    'average_call_duration': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average call duration',
                                    },
                                    'average_callback_wait_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average callback wait time',
                                    },
                                    'average_hold_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average hold time per call',
                                    },
                                    'average_queue_wait_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average queue wait time',
                                    },
                                    'average_time_to_answer': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average time to answer',
                                    },
                                    'average_wrap_up_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average wrap-up time',
                                    },
                                    'current_timestamp': {
                                        'type': ['null', 'integer'],
                                        'description': 'Current timestamp',
                                    },
                                    'max_calls_waiting': {
                                        'type': ['null', 'integer'],
                                        'description': 'Max calls waiting in queue',
                                    },
                                    'max_queue_wait_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Max queue wait time',
                                    },
                                    'total_call_duration': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total call duration',
                                    },
                                    'total_callback_calls': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total callback calls',
                                    },
                                    'total_calls': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total calls',
                                    },
                                    'total_calls_abandoned_in_queue': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total calls abandoned in queue',
                                    },
                                    'total_calls_outside_business_hours': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total calls outside business hours',
                                    },
                                    'total_calls_with_exceeded_queue_wait_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total calls exceeding max queue wait time',
                                    },
                                    'total_calls_with_requested_voicemail': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total calls requesting voicemail',
                                    },
                                    'total_embeddable_callback_calls': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total embeddable callback calls',
                                    },
                                    'total_hold_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total hold time',
                                    },
                                    'total_inbound_calls': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total inbound calls',
                                    },
                                    'total_outbound_calls': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total outbound calls',
                                    },
                                    'total_textback_requests': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total textback requests',
                                    },
                                    'total_voicemails': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total voicemails',
                                    },
                                    'total_wrap_up_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total wrap-up time',
                                    },
                                },
                                'x-airbyte-entity-name': 'account_overview',
                                'x-airbyte-stream-name': 'account_overview',
                            },
                        },
                    },
                    record_extractor='$.account_overview',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'average_call_duration': {
                        'type': ['null', 'integer'],
                        'description': 'Average call duration',
                    },
                    'average_callback_wait_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average callback wait time',
                    },
                    'average_hold_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average hold time per call',
                    },
                    'average_queue_wait_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average queue wait time',
                    },
                    'average_time_to_answer': {
                        'type': ['null', 'integer'],
                        'description': 'Average time to answer',
                    },
                    'average_wrap_up_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average wrap-up time',
                    },
                    'current_timestamp': {
                        'type': ['null', 'integer'],
                        'description': 'Current timestamp',
                    },
                    'max_calls_waiting': {
                        'type': ['null', 'integer'],
                        'description': 'Max calls waiting in queue',
                    },
                    'max_queue_wait_time': {
                        'type': ['null', 'integer'],
                        'description': 'Max queue wait time',
                    },
                    'total_call_duration': {
                        'type': ['null', 'integer'],
                        'description': 'Total call duration',
                    },
                    'total_callback_calls': {
                        'type': ['null', 'integer'],
                        'description': 'Total callback calls',
                    },
                    'total_calls': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls',
                    },
                    'total_calls_abandoned_in_queue': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls abandoned in queue',
                    },
                    'total_calls_outside_business_hours': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls outside business hours',
                    },
                    'total_calls_with_exceeded_queue_wait_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls exceeding max queue wait time',
                    },
                    'total_calls_with_requested_voicemail': {
                        'type': ['null', 'integer'],
                        'description': 'Total calls requesting voicemail',
                    },
                    'total_embeddable_callback_calls': {
                        'type': ['null', 'integer'],
                        'description': 'Total embeddable callback calls',
                    },
                    'total_hold_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total hold time',
                    },
                    'total_inbound_calls': {
                        'type': ['null', 'integer'],
                        'description': 'Total inbound calls',
                    },
                    'total_outbound_calls': {
                        'type': ['null', 'integer'],
                        'description': 'Total outbound calls',
                    },
                    'total_textback_requests': {
                        'type': ['null', 'integer'],
                        'description': 'Total textback requests',
                    },
                    'total_voicemails': {
                        'type': ['null', 'integer'],
                        'description': 'Total voicemails',
                    },
                    'total_wrap_up_time': {
                        'type': ['null', 'integer'],
                        'description': 'Total wrap-up time',
                    },
                },
                'x-airbyte-entity-name': 'account_overview',
                'x-airbyte-stream-name': 'account_overview',
            },
        ),
        EntityDefinition(
            name='current_queue_activity',
            stream_name='current_queue_activity',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/stats/current_queue_activity',
                    action=Action.LIST,
                    description='Returns current queue activity statistics',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'current_queue_activity': {
                                'type': 'object',
                                'properties': {
                                    'agents_online': {
                                        'type': ['null', 'integer'],
                                        'description': 'Current number of agents online',
                                    },
                                    'average_wait_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Average wait time for callers in queue (seconds)',
                                    },
                                    'callbacks_waiting': {
                                        'type': ['null', 'integer'],
                                        'description': 'Number of callers in callback queue',
                                    },
                                    'calls_waiting': {
                                        'type': ['null', 'integer'],
                                        'description': 'Number of callers waiting in queue',
                                    },
                                    'current_timestamp': {
                                        'type': ['null', 'integer'],
                                        'description': 'Current timestamp',
                                    },
                                    'embeddable_callbacks_waiting': {
                                        'type': ['null', 'integer'],
                                        'description': 'Number of Web Widget callback requests waiting',
                                    },
                                    'longest_wait_time': {
                                        'type': ['null', 'integer'],
                                        'description': 'Longest wait time for any caller (seconds)',
                                    },
                                    'ai_agent_calls': {
                                        'type': ['null', 'integer'],
                                        'description': 'Current number of calls with AI agents',
                                    },
                                },
                                'x-airbyte-entity-name': 'current_queue_activity',
                                'x-airbyte-stream-name': 'current_queue_activity',
                            },
                        },
                    },
                    record_extractor='$.current_queue_activity',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'agents_online': {
                        'type': ['null', 'integer'],
                        'description': 'Current number of agents online',
                    },
                    'average_wait_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average wait time for callers in queue (seconds)',
                    },
                    'callbacks_waiting': {
                        'type': ['null', 'integer'],
                        'description': 'Number of callers in callback queue',
                    },
                    'calls_waiting': {
                        'type': ['null', 'integer'],
                        'description': 'Number of callers waiting in queue',
                    },
                    'current_timestamp': {
                        'type': ['null', 'integer'],
                        'description': 'Current timestamp',
                    },
                    'embeddable_callbacks_waiting': {
                        'type': ['null', 'integer'],
                        'description': 'Number of Web Widget callback requests waiting',
                    },
                    'longest_wait_time': {
                        'type': ['null', 'integer'],
                        'description': 'Longest wait time for any caller (seconds)',
                    },
                    'ai_agent_calls': {
                        'type': ['null', 'integer'],
                        'description': 'Current number of calls with AI agents',
                    },
                },
                'x-airbyte-entity-name': 'current_queue_activity',
                'x-airbyte-stream-name': 'current_queue_activity',
            },
        ),
        EntityDefinition(
            name='calls',
            stream_name='calls',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/stats/incremental/calls',
                    action=Action.LIST,
                    description='Returns incremental call data. Requires a start_time parameter (Unix epoch timestamp).',
                    query_params=['start_time'],
                    query_params_schema={
                        'start_time': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'calls': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Call ID',
                                        },
                                        'agent_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Agent ID',
                                        },
                                        'call_charge': {
                                            'type': ['null', 'string'],
                                            'description': 'Call charge amount',
                                        },
                                        'call_group_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Call group ID',
                                        },
                                        'call_recording_consent': {
                                            'type': ['null', 'string'],
                                            'description': 'Call recording consent status',
                                        },
                                        'call_recording_consent_action': {
                                            'type': ['null', 'string'],
                                            'description': 'Recording consent action',
                                        },
                                        'call_recording_consent_keypress': {
                                            'type': ['null', 'string'],
                                            'description': 'Recording consent keypress',
                                        },
                                        'callback': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this was a callback',
                                        },
                                        'callback_source': {
                                            'type': ['null', 'string'],
                                            'description': 'Source of the callback',
                                        },
                                        'completion_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Call completion status',
                                        },
                                        'consultation_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Consultation time',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'Creation timestamp',
                                        },
                                        'customer_requested_voicemail': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether customer requested voicemail',
                                        },
                                        'default_group': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether default group was used',
                                        },
                                        'direction': {
                                            'type': ['null', 'string'],
                                            'description': 'Call direction (inbound/outbound)',
                                        },
                                        'duration': {
                                            'type': ['null', 'integer'],
                                            'description': 'Call duration in seconds',
                                        },
                                        'exceeded_queue_time': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether queue time was exceeded',
                                        },
                                        'exceeded_queue_wait_time': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether max queue wait time was exceeded',
                                        },
                                        'hold_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Hold time in seconds',
                                        },
                                        'ivr_action': {
                                            'type': ['null', 'string'],
                                            'description': 'IVR action taken',
                                        },
                                        'ivr_destination_group_name': {
                                            'type': ['null', 'string'],
                                            'description': 'IVR destination group name',
                                        },
                                        'ivr_hops': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of IVR hops',
                                        },
                                        'ivr_routed_to': {
                                            'type': ['null', 'string'],
                                            'description': 'Where IVR routed the call',
                                        },
                                        'ivr_time_spent': {
                                            'type': ['null', 'integer'],
                                            'description': 'Time spent in IVR',
                                        },
                                        'minutes_billed': {
                                            'type': ['null', 'integer'],
                                            'description': 'Minutes billed',
                                        },
                                        'not_recording_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Time not recording',
                                        },
                                        'outside_business_hours': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether call was outside business hours',
                                        },
                                        'overflowed': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether call overflowed',
                                        },
                                        'overflowed_to': {
                                            'type': ['null', 'string'],
                                            'description': 'Where call overflowed to',
                                        },
                                        'phone_number': {
                                            'type': ['null', 'string'],
                                            'description': 'Phone number used',
                                        },
                                        'phone_number_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Phone number ID',
                                        },
                                        'quality_issues': {
                                            'type': ['null', 'array'],
                                            'description': 'Quality issues detected',
                                            'items': {'type': 'string'},
                                        },
                                        'recording_control_interactions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Recording control interactions count',
                                        },
                                        'recording_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Recording time',
                                        },
                                        'talk_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Talk time in seconds',
                                        },
                                        'ticket_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Associated ticket ID',
                                        },
                                        'time_to_answer': {
                                            'type': ['null', 'integer'],
                                            'description': 'Time to answer in seconds',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'Last update timestamp',
                                        },
                                        'voicemail': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether it was a voicemail',
                                        },
                                        'wait_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Wait time in seconds',
                                        },
                                        'wrap_up_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Wrap-up time in seconds',
                                        },
                                        'customer_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Customer ID',
                                        },
                                        'line': {
                                            'type': ['null', 'string'],
                                            'description': 'Line name',
                                        },
                                        'line_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Line ID',
                                        },
                                        'line_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Line type (phone or digital)',
                                        },
                                        'call_channel': {
                                            'type': ['null', 'string'],
                                            'description': 'Channel of the call',
                                        },
                                        'post_call_transcription_created': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether a post-call transcription was created',
                                        },
                                        'post_call_summary_created': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether a post-call summary was created',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'calls',
                                    'x-airbyte-stream-name': 'calls',
                                },
                            },
                            'next_page': {
                                'type': ['null', 'string'],
                            },
                            'count': {
                                'type': ['null', 'integer'],
                            },
                            'end_time': {
                                'type': ['null', 'integer'],
                                'description': 'End time of the incremental export window (Unix epoch)',
                            },
                        },
                    },
                    record_extractor='$.calls',
                    meta_extractor={'next_page': '$.next_page', 'count': '$.count'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Call ID',
                    },
                    'agent_id': {
                        'type': ['null', 'integer'],
                        'description': 'Agent ID',
                    },
                    'call_charge': {
                        'type': ['null', 'string'],
                        'description': 'Call charge amount',
                    },
                    'call_group_id': {
                        'type': ['null', 'integer'],
                        'description': 'Call group ID',
                    },
                    'call_recording_consent': {
                        'type': ['null', 'string'],
                        'description': 'Call recording consent status',
                    },
                    'call_recording_consent_action': {
                        'type': ['null', 'string'],
                        'description': 'Recording consent action',
                    },
                    'call_recording_consent_keypress': {
                        'type': ['null', 'string'],
                        'description': 'Recording consent keypress',
                    },
                    'callback': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this was a callback',
                    },
                    'callback_source': {
                        'type': ['null', 'string'],
                        'description': 'Source of the callback',
                    },
                    'completion_status': {
                        'type': ['null', 'string'],
                        'description': 'Call completion status',
                    },
                    'consultation_time': {
                        'type': ['null', 'integer'],
                        'description': 'Consultation time',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'Creation timestamp',
                    },
                    'customer_requested_voicemail': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether customer requested voicemail',
                    },
                    'default_group': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether default group was used',
                    },
                    'direction': {
                        'type': ['null', 'string'],
                        'description': 'Call direction (inbound/outbound)',
                    },
                    'duration': {
                        'type': ['null', 'integer'],
                        'description': 'Call duration in seconds',
                    },
                    'exceeded_queue_time': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether queue time was exceeded',
                    },
                    'exceeded_queue_wait_time': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether max queue wait time was exceeded',
                    },
                    'hold_time': {
                        'type': ['null', 'integer'],
                        'description': 'Hold time in seconds',
                    },
                    'ivr_action': {
                        'type': ['null', 'string'],
                        'description': 'IVR action taken',
                    },
                    'ivr_destination_group_name': {
                        'type': ['null', 'string'],
                        'description': 'IVR destination group name',
                    },
                    'ivr_hops': {
                        'type': ['null', 'integer'],
                        'description': 'Number of IVR hops',
                    },
                    'ivr_routed_to': {
                        'type': ['null', 'string'],
                        'description': 'Where IVR routed the call',
                    },
                    'ivr_time_spent': {
                        'type': ['null', 'integer'],
                        'description': 'Time spent in IVR',
                    },
                    'minutes_billed': {
                        'type': ['null', 'integer'],
                        'description': 'Minutes billed',
                    },
                    'not_recording_time': {
                        'type': ['null', 'integer'],
                        'description': 'Time not recording',
                    },
                    'outside_business_hours': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether call was outside business hours',
                    },
                    'overflowed': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether call overflowed',
                    },
                    'overflowed_to': {
                        'type': ['null', 'string'],
                        'description': 'Where call overflowed to',
                    },
                    'phone_number': {
                        'type': ['null', 'string'],
                        'description': 'Phone number used',
                    },
                    'phone_number_id': {
                        'type': ['null', 'integer'],
                        'description': 'Phone number ID',
                    },
                    'quality_issues': {
                        'type': ['null', 'array'],
                        'description': 'Quality issues detected',
                        'items': {'type': 'string'},
                    },
                    'recording_control_interactions': {
                        'type': ['null', 'integer'],
                        'description': 'Recording control interactions count',
                    },
                    'recording_time': {
                        'type': ['null', 'integer'],
                        'description': 'Recording time',
                    },
                    'talk_time': {
                        'type': ['null', 'integer'],
                        'description': 'Talk time in seconds',
                    },
                    'ticket_id': {
                        'type': ['null', 'integer'],
                        'description': 'Associated ticket ID',
                    },
                    'time_to_answer': {
                        'type': ['null', 'integer'],
                        'description': 'Time to answer in seconds',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'Last update timestamp',
                    },
                    'voicemail': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether it was a voicemail',
                    },
                    'wait_time': {
                        'type': ['null', 'integer'],
                        'description': 'Wait time in seconds',
                    },
                    'wrap_up_time': {
                        'type': ['null', 'integer'],
                        'description': 'Wrap-up time in seconds',
                    },
                    'customer_id': {
                        'type': ['null', 'integer'],
                        'description': 'Customer ID',
                    },
                    'line': {
                        'type': ['null', 'string'],
                        'description': 'Line name',
                    },
                    'line_id': {
                        'type': ['null', 'integer'],
                        'description': 'Line ID',
                    },
                    'line_type': {
                        'type': ['null', 'string'],
                        'description': 'Line type (phone or digital)',
                    },
                    'call_channel': {
                        'type': ['null', 'string'],
                        'description': 'Channel of the call',
                    },
                    'post_call_transcription_created': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether a post-call transcription was created',
                    },
                    'post_call_summary_created': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether a post-call summary was created',
                    },
                },
                'x-airbyte-entity-name': 'calls',
                'x-airbyte-stream-name': 'calls',
            },
        ),
        EntityDefinition(
            name='call_legs',
            stream_name='call_legs',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/stats/incremental/legs',
                    action=Action.LIST,
                    description='Returns incremental call leg data. Requires a start_time parameter (Unix epoch timestamp).',
                    query_params=['start_time'],
                    query_params_schema={
                        'start_time': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'legs': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Call leg ID',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Type of call leg',
                                        },
                                        'agent_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Agent ID',
                                        },
                                        'available_via': {
                                            'type': ['null', 'string'],
                                            'description': 'Channel agent was available through',
                                        },
                                        'call_charge': {
                                            'type': ['null', 'string'],
                                            'description': 'Call charge amount',
                                        },
                                        'call_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Associated call ID',
                                        },
                                        'completion_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Completion status',
                                        },
                                        'conference_from': {
                                            'type': ['null', 'integer'],
                                            'description': 'Conference from time',
                                        },
                                        'conference_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Conference duration',
                                        },
                                        'conference_to': {
                                            'type': ['null', 'integer'],
                                            'description': 'Conference to time',
                                        },
                                        'consultation_from': {
                                            'type': ['null', 'integer'],
                                            'description': 'Consultation from time',
                                        },
                                        'consultation_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Consultation duration',
                                        },
                                        'consultation_to': {
                                            'type': ['null', 'integer'],
                                            'description': 'Consultation to time',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'Creation timestamp',
                                        },
                                        'duration': {
                                            'type': ['null', 'integer'],
                                            'description': 'Duration in seconds',
                                        },
                                        'forwarded_to': {
                                            'type': ['null', 'string'],
                                            'description': 'Number forwarded to',
                                        },
                                        'hold_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Hold time in seconds',
                                        },
                                        'minutes_billed': {
                                            'type': ['null', 'integer'],
                                            'description': 'Minutes billed',
                                        },
                                        'quality_issues': {
                                            'type': ['null', 'array'],
                                            'description': 'Quality issues detected',
                                            'items': {'type': 'string'},
                                        },
                                        'talk_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Talk time in seconds',
                                        },
                                        'transferred_from': {
                                            'type': ['null', 'integer'],
                                            'description': 'Transferred from agent ID',
                                        },
                                        'transferred_to': {
                                            'type': ['null', 'integer'],
                                            'description': 'Transferred to agent ID',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'Last update timestamp',
                                        },
                                        'user_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'User ID',
                                        },
                                        'wrap_up_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Wrap-up time in seconds',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'call_legs',
                                    'x-airbyte-stream-name': 'call_legs',
                                },
                            },
                            'next_page': {
                                'type': ['null', 'string'],
                            },
                            'count': {
                                'type': ['null', 'integer'],
                            },
                            'end_time': {
                                'type': ['null', 'integer'],
                                'description': 'End time of the incremental export window (Unix epoch)',
                            },
                        },
                    },
                    record_extractor='$.legs',
                    meta_extractor={'next_page': '$.next_page', 'count': '$.count'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Call leg ID',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Type of call leg',
                    },
                    'agent_id': {
                        'type': ['null', 'integer'],
                        'description': 'Agent ID',
                    },
                    'available_via': {
                        'type': ['null', 'string'],
                        'description': 'Channel agent was available through',
                    },
                    'call_charge': {
                        'type': ['null', 'string'],
                        'description': 'Call charge amount',
                    },
                    'call_id': {
                        'type': ['null', 'integer'],
                        'description': 'Associated call ID',
                    },
                    'completion_status': {
                        'type': ['null', 'string'],
                        'description': 'Completion status',
                    },
                    'conference_from': {
                        'type': ['null', 'integer'],
                        'description': 'Conference from time',
                    },
                    'conference_time': {
                        'type': ['null', 'integer'],
                        'description': 'Conference duration',
                    },
                    'conference_to': {
                        'type': ['null', 'integer'],
                        'description': 'Conference to time',
                    },
                    'consultation_from': {
                        'type': ['null', 'integer'],
                        'description': 'Consultation from time',
                    },
                    'consultation_time': {
                        'type': ['null', 'integer'],
                        'description': 'Consultation duration',
                    },
                    'consultation_to': {
                        'type': ['null', 'integer'],
                        'description': 'Consultation to time',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'Creation timestamp',
                    },
                    'duration': {
                        'type': ['null', 'integer'],
                        'description': 'Duration in seconds',
                    },
                    'forwarded_to': {
                        'type': ['null', 'string'],
                        'description': 'Number forwarded to',
                    },
                    'hold_time': {
                        'type': ['null', 'integer'],
                        'description': 'Hold time in seconds',
                    },
                    'minutes_billed': {
                        'type': ['null', 'integer'],
                        'description': 'Minutes billed',
                    },
                    'quality_issues': {
                        'type': ['null', 'array'],
                        'description': 'Quality issues detected',
                        'items': {'type': 'string'},
                    },
                    'talk_time': {
                        'type': ['null', 'integer'],
                        'description': 'Talk time in seconds',
                    },
                    'transferred_from': {
                        'type': ['null', 'integer'],
                        'description': 'Transferred from agent ID',
                    },
                    'transferred_to': {
                        'type': ['null', 'integer'],
                        'description': 'Transferred to agent ID',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'Last update timestamp',
                    },
                    'user_id': {
                        'type': ['null', 'integer'],
                        'description': 'User ID',
                    },
                    'wrap_up_time': {
                        'type': ['null', 'integer'],
                        'description': 'Wrap-up time in seconds',
                    },
                },
                'x-airbyte-entity-name': 'call_legs',
                'x-airbyte-stream-name': 'call_legs',
            },
        ),
    ],
    search_field_paths={
        'addresses': [
            'city',
            'country_code',
            'id',
            'name',
            'provider_reference',
            'province',
            'state',
            'street',
            'zip',
        ],
        'agents_activity': [
            'accepted_third_party_conferences',
            'accepted_transfers',
            'agent_id',
            'agent_state',
            'available_time',
            'avatar_url',
            'average_hold_time',
            'average_talk_time',
            'average_wrap_up_time',
            'away_time',
            'call_status',
            'calls_accepted',
            'calls_denied',
            'calls_missed',
            'calls_put_on_hold',
            'forwarding_number',
            'name',
            'online_time',
            'started_third_party_conferences',
            'started_transfers',
            'total_call_duration',
            'total_hold_time',
            'total_talk_time',
            'total_wrap_up_time',
            'transfers_only_time',
            'via',
        ],
        'agents_overview': [
            'average_accepted_transfers',
            'average_available_time',
            'average_away_time',
            'average_calls_accepted',
            'average_calls_denied',
            'average_calls_missed',
            'average_calls_put_on_hold',
            'average_hold_time',
            'average_online_time',
            'average_started_transfers',
            'average_talk_time',
            'average_transfers_only_time',
            'average_wrap_up_time',
            'current_timestamp',
            'total_accepted_transfers',
            'total_calls_accepted',
            'total_calls_denied',
            'total_calls_missed',
            'total_calls_put_on_hold',
            'total_hold_time',
            'total_started_transfers',
            'total_talk_time',
            'total_wrap_up_time',
        ],
        'greeting_categories': ['id', 'name'],
        'greetings': [
            'active',
            'audio_name',
            'audio_url',
            'category_id',
            'default',
            'default_lang',
            'has_sub_settings',
            'id',
            'ivr_ids',
            'ivr_ids[]',
            'name',
            'pending',
            'phone_number_ids',
            'phone_number_ids[]',
            'upload_id',
        ],
        'phone_numbers': [
            'call_recording_consent',
            'capabilities',
            'capabilities.emergency_address',
            'capabilities.mms',
            'capabilities.sms',
            'capabilities.voice',
            'categorised_greetings',
            'categorised_greetings_with_sub_settings',
            'country_code',
            'created_at',
            'default_greeting_ids',
            'default_greeting_ids[]',
            'default_group_id',
            'display_number',
            'external',
            'failover_number',
            'greeting_ids',
            'greeting_ids[]',
            'group_ids',
            'group_ids[]',
            'id',
            'ivr_id',
            'line_type',
            'location',
            'name',
            'nickname',
            'number',
            'outbound_enabled',
            'priority',
            'recorded',
            'schedule_id',
            'sms_enabled',
            'sms_group_id',
            'token',
            'toll_free',
            'transcription',
            'voice_enabled',
        ],
        'call_legs': [
            'agent_id',
            'available_via',
            'call_charge',
            'call_id',
            'completion_status',
            'conference_from',
            'conference_time',
            'conference_to',
            'consultation_from',
            'consultation_time',
            'consultation_to',
            'created_at',
            'duration',
            'forwarded_to',
            'hold_time',
            'id',
            'minutes_billed',
            'quality_issues',
            'quality_issues[]',
            'talk_time',
            'transferred_from',
            'transferred_to',
            'type',
            'updated_at',
            'user_id',
            'wrap_up_time',
        ],
        'calls': [
            'agent_id',
            'call_charge',
            'call_group_id',
            'call_recording_consent',
            'call_recording_consent_action',
            'call_recording_consent_keypress',
            'callback',
            'callback_source',
            'completion_status',
            'consultation_time',
            'created_at',
            'customer_requested_voicemail',
            'default_group',
            'direction',
            'duration',
            'exceeded_queue_time',
            'exceeded_queue_wait_time',
            'hold_time',
            'id',
            'ivr_action',
            'ivr_destination_group_name',
            'ivr_hops',
            'ivr_routed_to',
            'ivr_time_spent',
            'minutes_billed',
            'not_recording_time',
            'outside_business_hours',
            'overflowed',
            'overflowed_to',
            'phone_number',
            'phone_number_id',
            'quality_issues',
            'quality_issues[]',
            'recording_control_interactions',
            'recording_time',
            'talk_time',
            'ticket_id',
            'time_to_answer',
            'updated_at',
            'voicemail',
            'wait_time',
            'wrap_up_time',
        ],
        'current_queue_activity': [
            'agents_online',
            'average_wait_time',
            'callbacks_waiting',
            'calls_waiting',
            'current_timestamp',
            'embeddable_callbacks_waiting',
            'longest_wait_time',
        ],
        'account_overview': [
            'average_call_duration',
            'average_callback_wait_time',
            'average_hold_time',
            'average_queue_wait_time',
            'average_time_to_answer',
            'average_wrap_up_time',
            'current_timestamp',
            'max_calls_waiting',
            'max_queue_wait_time',
            'total_call_duration',
            'total_callback_calls',
            'total_calls',
            'total_calls_abandoned_in_queue',
            'total_calls_outside_business_hours',
            'total_calls_with_exceeded_queue_wait_time',
            'total_calls_with_requested_voicemail',
            'total_embeddable_callback_calls',
            'total_hold_time',
            'total_inbound_calls',
            'total_outbound_calls',
            'total_textback_requests',
            'total_voicemails',
            'total_wrap_up_time',
        ],
        'ivrs': [
            'id',
            'menus',
            'menus[]',
            'name',
            'phone_number_ids',
            'phone_number_ids[]',
            'phone_number_names',
            'phone_number_names[]',
        ],
        'ivr_menus': [
            'default',
            'greeting_id',
            'id',
            'ivr_id',
            'name',
        ],
        'ivr_routes': [
            'action',
            'greeting',
            'id',
            'ivr_id',
            'ivr_menu_id',
            'keypress',
            'option_text',
            'options',
            'overflow_options',
            'overflow_options[]',
        ],
    },
    server_variable_defaults={'subdomain': 'your-subdomain'},
)