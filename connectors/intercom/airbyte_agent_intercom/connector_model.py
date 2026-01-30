"""
Connector model for intercom.

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

IntercomConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('d8313939-3782-41b0-be29-b3ca20d8dd3a'),
    name='intercom',
    version='0.1.6',
    base_url='https://api.intercom.io',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
            title='Access Token Authentication',
            type='object',
            required=['access_token'],
            properties={
                'access_token': AuthConfigFieldSpec(
                    title='Access Token',
                    description='Your Intercom API Access Token',
                ),
            },
            auth_mapping={'token': '${access_token}'},
            replication_auth_key_mapping={'access_token': 'access_token'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='contacts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/contacts',
                    action=Action.LIST,
                    description='Returns a paginated list of contacts in the workspace',
                    query_params=['per_page', 'starting_after'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'starting_after': {'type': 'string', 'required': False},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of contacts',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of list',
                            },
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Contact object representing a user or lead',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of object (contact)',
                                        },
                                        'id': {'type': 'string', 'description': 'Unique contact identifier'},
                                        'workspace_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Workspace ID',
                                        },
                                        'external_id': {
                                            'type': ['string', 'null'],
                                            'description': 'External ID from your system',
                                        },
                                        'role': {
                                            'type': ['string', 'null'],
                                            'description': 'Role of the contact (user or lead)',
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                            'description': 'Email address',
                                        },
                                        'phone': {
                                            'type': ['string', 'null'],
                                            'description': 'Phone number',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Full name',
                                        },
                                        'avatar': {
                                            'type': ['string', 'null'],
                                            'description': 'Avatar URL',
                                        },
                                        'owner_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Owner admin ID',
                                        },
                                        'social_profiles': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Social profiles',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of list',
                                                        },
                                                        'data': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Social profile',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of social profile',
                                                                    },
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Social network name',
                                                                    },
                                                                    'url': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Profile URL',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'has_hard_bounced': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether email has hard bounced',
                                        },
                                        'marked_email_as_spam': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether contact marked email as spam',
                                        },
                                        'unsubscribed_from_emails': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether contact unsubscribed from emails',
                                        },
                                        'created_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                        'signed_up_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Sign up timestamp (Unix)',
                                        },
                                        'last_seen_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last seen timestamp (Unix)',
                                        },
                                        'last_replied_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last reply timestamp (Unix)',
                                        },
                                        'last_contacted_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last contacted timestamp (Unix)',
                                        },
                                        'last_email_opened_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last email opened timestamp (Unix)',
                                        },
                                        'last_email_clicked_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last email clicked timestamp (Unix)',
                                        },
                                        'language_override': {
                                            'type': ['string', 'null'],
                                            'description': 'Language override',
                                        },
                                        'browser': {
                                            'type': ['string', 'null'],
                                            'description': 'Browser used',
                                        },
                                        'browser_version': {
                                            'type': ['string', 'null'],
                                            'description': 'Browser version',
                                        },
                                        'browser_language': {
                                            'type': ['string', 'null'],
                                            'description': 'Browser language',
                                        },
                                        'os': {
                                            'type': ['string', 'null'],
                                            'description': 'Operating system',
                                        },
                                        'location': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Location information',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of location',
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Country',
                                                        },
                                                        'region': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Region/state',
                                                        },
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                            'description': 'City',
                                                        },
                                                        'country_code': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Country code',
                                                        },
                                                        'continent_code': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Continent code',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'android_app_name': {
                                            'type': ['string', 'null'],
                                            'description': 'Android app name',
                                        },
                                        'android_app_version': {
                                            'type': ['string', 'null'],
                                            'description': 'Android app version',
                                        },
                                        'android_device': {
                                            'type': ['string', 'null'],
                                            'description': 'Android device',
                                        },
                                        'android_os_version': {
                                            'type': ['string', 'null'],
                                            'description': 'Android OS version',
                                        },
                                        'android_sdk_version': {
                                            'type': ['string', 'null'],
                                            'description': 'Android SDK version',
                                        },
                                        'android_last_seen_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Android last seen timestamp',
                                        },
                                        'ios_app_name': {
                                            'type': ['string', 'null'],
                                            'description': 'iOS app name',
                                        },
                                        'ios_app_version': {
                                            'type': ['string', 'null'],
                                            'description': 'iOS app version',
                                        },
                                        'ios_device': {
                                            'type': ['string', 'null'],
                                            'description': 'iOS device',
                                        },
                                        'ios_os_version': {
                                            'type': ['string', 'null'],
                                            'description': 'iOS OS version',
                                        },
                                        'ios_sdk_version': {
                                            'type': ['string', 'null'],
                                            'description': 'iOS SDK version',
                                        },
                                        'ios_last_seen_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'iOS last seen timestamp',
                                        },
                                        'custom_attributes': {
                                            'type': ['object', 'null'],
                                            'description': 'Custom attributes',
                                            'additionalProperties': True,
                                        },
                                        'tags': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Tags associated with contact',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of list',
                                                        },
                                                        'data': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Tag reference',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of object',
                                                                    },
                                                                    'id': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Tag ID',
                                                                    },
                                                                    'url': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Tag URL',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'notes': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Notes associated with contact',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of list',
                                                        },
                                                        'data': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Note reference',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of object',
                                                                    },
                                                                    'id': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Note ID',
                                                                    },
                                                                    'url': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Note URL',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'companies': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Companies associated with contact',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of list',
                                                        },
                                                        'data': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Company reference',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of object',
                                                                    },
                                                                    'id': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Company ID',
                                                                    },
                                                                    'url': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Company URL',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                    },
                                    'x-airbyte-entity-name': 'contacts',
                                },
                            },
                            'total_count': {
                                'type': ['integer', 'null'],
                                'description': 'Total number of contacts',
                            },
                            'pages': {
                                'type': ['object', 'null'],
                                'description': 'Pagination metadata',
                                'properties': {
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Type of pagination',
                                    },
                                    'page': {
                                        'type': ['integer', 'null'],
                                        'description': 'Current page number',
                                    },
                                    'per_page': {
                                        'type': ['integer', 'null'],
                                        'description': 'Number of items per page',
                                    },
                                    'total_pages': {
                                        'type': ['integer', 'null'],
                                        'description': 'Total number of pages',
                                    },
                                    'next': {
                                        'type': ['object', 'null'],
                                        'description': 'Cursor for next page',
                                        'properties': {
                                            'page': {
                                                'type': ['integer', 'null'],
                                                'description': 'Next page number',
                                            },
                                            'starting_after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.pages.next.starting_after'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/contacts/{id}',
                    action=Action.GET,
                    description='Get a single contact by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Contact object representing a user or lead',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of object (contact)',
                            },
                            'id': {'type': 'string', 'description': 'Unique contact identifier'},
                            'workspace_id': {
                                'type': ['string', 'null'],
                                'description': 'Workspace ID',
                            },
                            'external_id': {
                                'type': ['string', 'null'],
                                'description': 'External ID from your system',
                            },
                            'role': {
                                'type': ['string', 'null'],
                                'description': 'Role of the contact (user or lead)',
                            },
                            'email': {
                                'type': ['string', 'null'],
                                'description': 'Email address',
                            },
                            'phone': {
                                'type': ['string', 'null'],
                                'description': 'Phone number',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Full name',
                            },
                            'avatar': {
                                'type': ['string', 'null'],
                                'description': 'Avatar URL',
                            },
                            'owner_id': {
                                'type': ['integer', 'null'],
                                'description': 'Owner admin ID',
                            },
                            'social_profiles': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Social profiles',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of list',
                                            },
                                            'data': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Social profile',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of social profile',
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Social network name',
                                                        },
                                                        'url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Profile URL',
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'has_hard_bounced': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether email has hard bounced',
                            },
                            'marked_email_as_spam': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether contact marked email as spam',
                            },
                            'unsubscribed_from_emails': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether contact unsubscribed from emails',
                            },
                            'created_at': {
                                'type': ['integer', 'null'],
                                'description': 'Creation timestamp (Unix)',
                            },
                            'updated_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last update timestamp (Unix)',
                            },
                            'signed_up_at': {
                                'type': ['integer', 'null'],
                                'description': 'Sign up timestamp (Unix)',
                            },
                            'last_seen_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last seen timestamp (Unix)',
                            },
                            'last_replied_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last reply timestamp (Unix)',
                            },
                            'last_contacted_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last contacted timestamp (Unix)',
                            },
                            'last_email_opened_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last email opened timestamp (Unix)',
                            },
                            'last_email_clicked_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last email clicked timestamp (Unix)',
                            },
                            'language_override': {
                                'type': ['string', 'null'],
                                'description': 'Language override',
                            },
                            'browser': {
                                'type': ['string', 'null'],
                                'description': 'Browser used',
                            },
                            'browser_version': {
                                'type': ['string', 'null'],
                                'description': 'Browser version',
                            },
                            'browser_language': {
                                'type': ['string', 'null'],
                                'description': 'Browser language',
                            },
                            'os': {
                                'type': ['string', 'null'],
                                'description': 'Operating system',
                            },
                            'location': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Location information',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of location',
                                            },
                                            'country': {
                                                'type': ['string', 'null'],
                                                'description': 'Country',
                                            },
                                            'region': {
                                                'type': ['string', 'null'],
                                                'description': 'Region/state',
                                            },
                                            'city': {
                                                'type': ['string', 'null'],
                                                'description': 'City',
                                            },
                                            'country_code': {
                                                'type': ['string', 'null'],
                                                'description': 'Country code',
                                            },
                                            'continent_code': {
                                                'type': ['string', 'null'],
                                                'description': 'Continent code',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'android_app_name': {
                                'type': ['string', 'null'],
                                'description': 'Android app name',
                            },
                            'android_app_version': {
                                'type': ['string', 'null'],
                                'description': 'Android app version',
                            },
                            'android_device': {
                                'type': ['string', 'null'],
                                'description': 'Android device',
                            },
                            'android_os_version': {
                                'type': ['string', 'null'],
                                'description': 'Android OS version',
                            },
                            'android_sdk_version': {
                                'type': ['string', 'null'],
                                'description': 'Android SDK version',
                            },
                            'android_last_seen_at': {
                                'type': ['integer', 'null'],
                                'description': 'Android last seen timestamp',
                            },
                            'ios_app_name': {
                                'type': ['string', 'null'],
                                'description': 'iOS app name',
                            },
                            'ios_app_version': {
                                'type': ['string', 'null'],
                                'description': 'iOS app version',
                            },
                            'ios_device': {
                                'type': ['string', 'null'],
                                'description': 'iOS device',
                            },
                            'ios_os_version': {
                                'type': ['string', 'null'],
                                'description': 'iOS OS version',
                            },
                            'ios_sdk_version': {
                                'type': ['string', 'null'],
                                'description': 'iOS SDK version',
                            },
                            'ios_last_seen_at': {
                                'type': ['integer', 'null'],
                                'description': 'iOS last seen timestamp',
                            },
                            'custom_attributes': {
                                'type': ['object', 'null'],
                                'description': 'Custom attributes',
                                'additionalProperties': True,
                            },
                            'tags': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Tags associated with contact',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of list',
                                            },
                                            'data': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Tag reference',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Tag ID',
                                                        },
                                                        'url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Tag URL',
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'notes': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Notes associated with contact',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of list',
                                            },
                                            'data': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Note reference',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Note ID',
                                                        },
                                                        'url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Note URL',
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'companies': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Companies associated with contact',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of list',
                                            },
                                            'data': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Company reference',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Company ID',
                                                        },
                                                        'url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Company URL',
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'x-airbyte-entity-name': 'contacts',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Contact object representing a user or lead',
                'properties': {
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Type of object (contact)',
                    },
                    'id': {'type': 'string', 'description': 'Unique contact identifier'},
                    'workspace_id': {
                        'type': ['string', 'null'],
                        'description': 'Workspace ID',
                    },
                    'external_id': {
                        'type': ['string', 'null'],
                        'description': 'External ID from your system',
                    },
                    'role': {
                        'type': ['string', 'null'],
                        'description': 'Role of the contact (user or lead)',
                    },
                    'email': {
                        'type': ['string', 'null'],
                        'description': 'Email address',
                    },
                    'phone': {
                        'type': ['string', 'null'],
                        'description': 'Phone number',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Full name',
                    },
                    'avatar': {
                        'type': ['string', 'null'],
                        'description': 'Avatar URL',
                    },
                    'owner_id': {
                        'type': ['integer', 'null'],
                        'description': 'Owner admin ID',
                    },
                    'social_profiles': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/SocialProfiles'},
                            {'type': 'null'},
                        ],
                    },
                    'has_hard_bounced': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether email has hard bounced',
                    },
                    'marked_email_as_spam': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether contact marked email as spam',
                    },
                    'unsubscribed_from_emails': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether contact unsubscribed from emails',
                    },
                    'created_at': {
                        'type': ['integer', 'null'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'signed_up_at': {
                        'type': ['integer', 'null'],
                        'description': 'Sign up timestamp (Unix)',
                    },
                    'last_seen_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last seen timestamp (Unix)',
                    },
                    'last_replied_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last reply timestamp (Unix)',
                    },
                    'last_contacted_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last contacted timestamp (Unix)',
                    },
                    'last_email_opened_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last email opened timestamp (Unix)',
                    },
                    'last_email_clicked_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last email clicked timestamp (Unix)',
                    },
                    'language_override': {
                        'type': ['string', 'null'],
                        'description': 'Language override',
                    },
                    'browser': {
                        'type': ['string', 'null'],
                        'description': 'Browser used',
                    },
                    'browser_version': {
                        'type': ['string', 'null'],
                        'description': 'Browser version',
                    },
                    'browser_language': {
                        'type': ['string', 'null'],
                        'description': 'Browser language',
                    },
                    'os': {
                        'type': ['string', 'null'],
                        'description': 'Operating system',
                    },
                    'location': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Location'},
                            {'type': 'null'},
                        ],
                    },
                    'android_app_name': {
                        'type': ['string', 'null'],
                        'description': 'Android app name',
                    },
                    'android_app_version': {
                        'type': ['string', 'null'],
                        'description': 'Android app version',
                    },
                    'android_device': {
                        'type': ['string', 'null'],
                        'description': 'Android device',
                    },
                    'android_os_version': {
                        'type': ['string', 'null'],
                        'description': 'Android OS version',
                    },
                    'android_sdk_version': {
                        'type': ['string', 'null'],
                        'description': 'Android SDK version',
                    },
                    'android_last_seen_at': {
                        'type': ['integer', 'null'],
                        'description': 'Android last seen timestamp',
                    },
                    'ios_app_name': {
                        'type': ['string', 'null'],
                        'description': 'iOS app name',
                    },
                    'ios_app_version': {
                        'type': ['string', 'null'],
                        'description': 'iOS app version',
                    },
                    'ios_device': {
                        'type': ['string', 'null'],
                        'description': 'iOS device',
                    },
                    'ios_os_version': {
                        'type': ['string', 'null'],
                        'description': 'iOS OS version',
                    },
                    'ios_sdk_version': {
                        'type': ['string', 'null'],
                        'description': 'iOS SDK version',
                    },
                    'ios_last_seen_at': {
                        'type': ['integer', 'null'],
                        'description': 'iOS last seen timestamp',
                    },
                    'custom_attributes': {
                        'type': ['object', 'null'],
                        'description': 'Custom attributes',
                        'additionalProperties': True,
                    },
                    'tags': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ContactTags'},
                            {'type': 'null'},
                        ],
                    },
                    'notes': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ContactNotes'},
                            {'type': 'null'},
                        ],
                    },
                    'companies': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ContactCompanies'},
                            {'type': 'null'},
                        ],
                    },
                },
                'x-airbyte-entity-name': 'contacts',
            },
        ),
        EntityDefinition(
            name='conversations',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/conversations',
                    action=Action.LIST,
                    description='Returns a paginated list of conversations',
                    query_params=['per_page', 'starting_after'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'starting_after': {'type': 'string', 'required': False},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of conversations',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of list',
                            },
                            'conversations': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Conversation object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of object (conversation)',
                                        },
                                        'id': {'type': 'string', 'description': 'Unique conversation identifier'},
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Conversation title',
                                        },
                                        'created_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                        'waiting_since': {
                                            'type': ['integer', 'null'],
                                            'description': 'Waiting since timestamp (Unix)',
                                        },
                                        'snoozed_until': {
                                            'type': ['integer', 'null'],
                                            'description': 'Snoozed until timestamp (Unix)',
                                        },
                                        'open': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether conversation is open',
                                        },
                                        'state': {
                                            'type': ['string', 'null'],
                                            'description': 'Conversation state (open, closed, snoozed)',
                                        },
                                        'read': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether conversation has been read',
                                        },
                                        'priority': {
                                            'type': ['string', 'null'],
                                            'description': 'Conversation priority',
                                        },
                                        'admin_assignee_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Assigned admin ID',
                                        },
                                        'team_assignee_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Assigned team ID',
                                        },
                                        'tags': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Tags on conversation',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of list',
                                                        },
                                                        'tags': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Tag object',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of object (tag)',
                                                                    },
                                                                    'id': {'type': 'string', 'description': 'Unique tag identifier'},
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Tag name',
                                                                    },
                                                                    'applied_at': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Applied timestamp (Unix)',
                                                                    },
                                                                    'applied_by': {
                                                                        'oneOf': [
                                                                            {
                                                                                'type': 'object',
                                                                                'description': 'Admin reference',
                                                                                'properties': {
                                                                                    'type': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Type of object',
                                                                                    },
                                                                                    'id': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Admin ID',
                                                                                    },
                                                                                },
                                                                            },
                                                                            {'type': 'null'},
                                                                        ],
                                                                    },
                                                                },
                                                                'x-airbyte-entity-name': 'tags',
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'conversation_rating': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Conversation rating',
                                                    'properties': {
                                                        'rating': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Rating value',
                                                        },
                                                        'remark': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Rating remark',
                                                        },
                                                        'created_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Rating timestamp',
                                                        },
                                                        'contact': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'Contact reference',
                                                                    'properties': {
                                                                        'type': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Type of object',
                                                                        },
                                                                        'id': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Contact ID',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'teammate': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'Admin reference',
                                                                    'properties': {
                                                                        'type': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Type of object',
                                                                        },
                                                                        'id': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Admin ID',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'source': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Conversation source',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Source type',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Source ID',
                                                        },
                                                        'delivered_as': {
                                                            'type': ['string', 'null'],
                                                            'description': 'How it was delivered',
                                                        },
                                                        'subject': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Subject line',
                                                        },
                                                        'body': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Message body',
                                                        },
                                                        'author': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'Message author',
                                                                    'properties': {
                                                                        'type': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Author type (admin, user, bot)',
                                                                        },
                                                                        'id': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Author ID',
                                                                        },
                                                                        'name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Author name',
                                                                        },
                                                                        'email': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Author email',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'attachments': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Message attachment',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Attachment type',
                                                                    },
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'File name',
                                                                    },
                                                                    'url': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'File URL',
                                                                    },
                                                                    'content_type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'MIME type',
                                                                    },
                                                                    'filesize': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'File size in bytes',
                                                                    },
                                                                    'width': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Image width',
                                                                    },
                                                                    'height': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Image height',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        'url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Source URL',
                                                        },
                                                        'redacted': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether content is redacted',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'contacts': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Contacts in conversation',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of list',
                                                        },
                                                        'contacts': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Contact reference',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of object',
                                                                    },
                                                                    'id': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Contact ID',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'teammates': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Teammates in conversation',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of list',
                                                        },
                                                        'admins': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Admin reference',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of object',
                                                                    },
                                                                    'id': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Admin ID',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'first_contact_reply': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'First contact reply info',
                                                    'properties': {
                                                        'created_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Reply timestamp',
                                                        },
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Reply type',
                                                        },
                                                        'url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Reply URL',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'sla_applied': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'SLA applied to conversation',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'sla_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'SLA name',
                                                        },
                                                        'sla_status': {
                                                            'type': ['string', 'null'],
                                                            'description': 'SLA status',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'statistics': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Conversation statistics',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'time_to_assignment': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Time to assignment in seconds',
                                                        },
                                                        'time_to_admin_reply': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Time to admin reply in seconds',
                                                        },
                                                        'time_to_first_close': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Time to first close in seconds',
                                                        },
                                                        'time_to_last_close': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Time to last close in seconds',
                                                        },
                                                        'median_time_to_reply': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Median time to reply in seconds',
                                                        },
                                                        'first_contact_reply_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'First contact reply timestamp',
                                                        },
                                                        'first_assignment_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'First assignment timestamp',
                                                        },
                                                        'first_admin_reply_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'First admin reply timestamp',
                                                        },
                                                        'first_close_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'First close timestamp',
                                                        },
                                                        'last_assignment_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Last assignment timestamp',
                                                        },
                                                        'last_assignment_admin_reply_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Last assignment admin reply timestamp',
                                                        },
                                                        'last_contact_reply_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Last contact reply timestamp',
                                                        },
                                                        'last_admin_reply_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Last admin reply timestamp',
                                                        },
                                                        'last_close_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Last close timestamp',
                                                        },
                                                        'last_closed_by_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'ID of admin who last closed',
                                                        },
                                                        'count_reopens': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Number of reopens',
                                                        },
                                                        'count_assignments': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Number of assignments',
                                                        },
                                                        'count_conversation_parts': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Number of conversation parts',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'conversation_parts': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Reference to conversation parts',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of list',
                                                        },
                                                        'conversation_parts': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Conversation part (message, note, action)',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of object',
                                                                    },
                                                                    'id': {'type': 'string', 'description': 'Unique part identifier'},
                                                                    'part_type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of part (comment, note, assignment, etc.)',
                                                                    },
                                                                    'body': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Part body content',
                                                                    },
                                                                    'created_at': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Creation timestamp (Unix)',
                                                                    },
                                                                    'updated_at': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Update timestamp (Unix)',
                                                                    },
                                                                    'notified_at': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Notification timestamp (Unix)',
                                                                    },
                                                                    'assigned_to': {
                                                                        'oneOf': [
                                                                            {
                                                                                'type': 'object',
                                                                                'description': 'Admin reference',
                                                                                'properties': {
                                                                                    'type': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Type of object',
                                                                                    },
                                                                                    'id': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Admin ID',
                                                                                    },
                                                                                },
                                                                            },
                                                                            {'type': 'null'},
                                                                        ],
                                                                    },
                                                                    'author': {
                                                                        'oneOf': [
                                                                            {
                                                                                'type': 'object',
                                                                                'description': 'Message author',
                                                                                'properties': {
                                                                                    'type': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Author type (admin, user, bot)',
                                                                                    },
                                                                                    'id': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Author ID',
                                                                                    },
                                                                                    'name': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Author name',
                                                                                    },
                                                                                    'email': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Author email',
                                                                                    },
                                                                                },
                                                                            },
                                                                            {'type': 'null'},
                                                                        ],
                                                                    },
                                                                    'attachments': {
                                                                        'type': 'array',
                                                                        'items': {
                                                                            'type': 'object',
                                                                            'description': 'Message attachment',
                                                                            'properties': {
                                                                                'type': {
                                                                                    'type': ['string', 'null'],
                                                                                    'description': 'Attachment type',
                                                                                },
                                                                                'name': {
                                                                                    'type': ['string', 'null'],
                                                                                    'description': 'File name',
                                                                                },
                                                                                'url': {
                                                                                    'type': ['string', 'null'],
                                                                                    'description': 'File URL',
                                                                                },
                                                                                'content_type': {
                                                                                    'type': ['string', 'null'],
                                                                                    'description': 'MIME type',
                                                                                },
                                                                                'filesize': {
                                                                                    'type': ['integer', 'null'],
                                                                                    'description': 'File size in bytes',
                                                                                },
                                                                                'width': {
                                                                                    'type': ['integer', 'null'],
                                                                                    'description': 'Image width',
                                                                                },
                                                                                'height': {
                                                                                    'type': ['integer', 'null'],
                                                                                    'description': 'Image height',
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                    'external_id': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'External ID',
                                                                    },
                                                                    'redacted': {
                                                                        'type': ['boolean', 'null'],
                                                                        'description': 'Whether content is redacted',
                                                                    },
                                                                },
                                                                'x-airbyte-entity-name': 'conversation_parts',
                                                            },
                                                        },
                                                        'total_count': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Total number of parts',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'custom_attributes': {
                                            'type': ['object', 'null'],
                                            'description': 'Custom attributes',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'x-airbyte-entity-name': 'conversations',
                                },
                            },
                            'total_count': {
                                'type': ['integer', 'null'],
                                'description': 'Total number of conversations',
                            },
                            'pages': {
                                'type': ['object', 'null'],
                                'description': 'Pagination metadata',
                                'properties': {
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Type of pagination',
                                    },
                                    'page': {
                                        'type': ['integer', 'null'],
                                        'description': 'Current page number',
                                    },
                                    'per_page': {
                                        'type': ['integer', 'null'],
                                        'description': 'Number of items per page',
                                    },
                                    'total_pages': {
                                        'type': ['integer', 'null'],
                                        'description': 'Total number of pages',
                                    },
                                    'next': {
                                        'type': ['object', 'null'],
                                        'description': 'Cursor for next page',
                                        'properties': {
                                            'page': {
                                                'type': ['integer', 'null'],
                                                'description': 'Next page number',
                                            },
                                            'starting_after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.conversations',
                    meta_extractor={'next_page': '$.pages.next.starting_after'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/conversations/{id}',
                    action=Action.GET,
                    description='Get a single conversation by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Conversation object',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of object (conversation)',
                            },
                            'id': {'type': 'string', 'description': 'Unique conversation identifier'},
                            'title': {
                                'type': ['string', 'null'],
                                'description': 'Conversation title',
                            },
                            'created_at': {
                                'type': ['integer', 'null'],
                                'description': 'Creation timestamp (Unix)',
                            },
                            'updated_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last update timestamp (Unix)',
                            },
                            'waiting_since': {
                                'type': ['integer', 'null'],
                                'description': 'Waiting since timestamp (Unix)',
                            },
                            'snoozed_until': {
                                'type': ['integer', 'null'],
                                'description': 'Snoozed until timestamp (Unix)',
                            },
                            'open': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether conversation is open',
                            },
                            'state': {
                                'type': ['string', 'null'],
                                'description': 'Conversation state (open, closed, snoozed)',
                            },
                            'read': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether conversation has been read',
                            },
                            'priority': {
                                'type': ['string', 'null'],
                                'description': 'Conversation priority',
                            },
                            'admin_assignee_id': {
                                'type': ['integer', 'null'],
                                'description': 'Assigned admin ID',
                            },
                            'team_assignee_id': {
                                'type': ['string', 'null'],
                                'description': 'Assigned team ID',
                            },
                            'tags': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Tags on conversation',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of list',
                                            },
                                            'tags': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Tag object',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object (tag)',
                                                        },
                                                        'id': {'type': 'string', 'description': 'Unique tag identifier'},
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Tag name',
                                                        },
                                                        'applied_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Applied timestamp (Unix)',
                                                        },
                                                        'applied_by': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'Admin reference',
                                                                    'properties': {
                                                                        'type': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Type of object',
                                                                        },
                                                                        'id': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Admin ID',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                    },
                                                    'x-airbyte-entity-name': 'tags',
                                                },
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'conversation_rating': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Conversation rating',
                                        'properties': {
                                            'rating': {
                                                'type': ['integer', 'null'],
                                                'description': 'Rating value',
                                            },
                                            'remark': {
                                                'type': ['string', 'null'],
                                                'description': 'Rating remark',
                                            },
                                            'created_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'Rating timestamp',
                                            },
                                            'contact': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'Contact reference',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of object',
                                                            },
                                                            'id': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Contact ID',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                            },
                                            'teammate': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'Admin reference',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Type of object',
                                                            },
                                                            'id': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Admin ID',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'source': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Conversation source',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Source type',
                                            },
                                            'id': {
                                                'type': ['string', 'null'],
                                                'description': 'Source ID',
                                            },
                                            'delivered_as': {
                                                'type': ['string', 'null'],
                                                'description': 'How it was delivered',
                                            },
                                            'subject': {
                                                'type': ['string', 'null'],
                                                'description': 'Subject line',
                                            },
                                            'body': {
                                                'type': ['string', 'null'],
                                                'description': 'Message body',
                                            },
                                            'author': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'Message author',
                                                        'properties': {
                                                            'type': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Author type (admin, user, bot)',
                                                            },
                                                            'id': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Author ID',
                                                            },
                                                            'name': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Author name',
                                                            },
                                                            'email': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Author email',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                            },
                                            'attachments': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Message attachment',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Attachment type',
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'File name',
                                                        },
                                                        'url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'File URL',
                                                        },
                                                        'content_type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'MIME type',
                                                        },
                                                        'filesize': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'File size in bytes',
                                                        },
                                                        'width': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Image width',
                                                        },
                                                        'height': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Image height',
                                                        },
                                                    },
                                                },
                                            },
                                            'url': {
                                                'type': ['string', 'null'],
                                                'description': 'Source URL',
                                            },
                                            'redacted': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether content is redacted',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'contacts': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Contacts in conversation',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of list',
                                            },
                                            'contacts': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Contact reference',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Contact ID',
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'teammates': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Teammates in conversation',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of list',
                                            },
                                            'admins': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Admin reference',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Admin ID',
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'first_contact_reply': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'First contact reply info',
                                        'properties': {
                                            'created_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'Reply timestamp',
                                            },
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Reply type',
                                            },
                                            'url': {
                                                'type': ['string', 'null'],
                                                'description': 'Reply URL',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'sla_applied': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'SLA applied to conversation',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of object',
                                            },
                                            'sla_name': {
                                                'type': ['string', 'null'],
                                                'description': 'SLA name',
                                            },
                                            'sla_status': {
                                                'type': ['string', 'null'],
                                                'description': 'SLA status',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'statistics': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Conversation statistics',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of object',
                                            },
                                            'time_to_assignment': {
                                                'type': ['integer', 'null'],
                                                'description': 'Time to assignment in seconds',
                                            },
                                            'time_to_admin_reply': {
                                                'type': ['integer', 'null'],
                                                'description': 'Time to admin reply in seconds',
                                            },
                                            'time_to_first_close': {
                                                'type': ['integer', 'null'],
                                                'description': 'Time to first close in seconds',
                                            },
                                            'time_to_last_close': {
                                                'type': ['integer', 'null'],
                                                'description': 'Time to last close in seconds',
                                            },
                                            'median_time_to_reply': {
                                                'type': ['integer', 'null'],
                                                'description': 'Median time to reply in seconds',
                                            },
                                            'first_contact_reply_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'First contact reply timestamp',
                                            },
                                            'first_assignment_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'First assignment timestamp',
                                            },
                                            'first_admin_reply_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'First admin reply timestamp',
                                            },
                                            'first_close_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'First close timestamp',
                                            },
                                            'last_assignment_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'Last assignment timestamp',
                                            },
                                            'last_assignment_admin_reply_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'Last assignment admin reply timestamp',
                                            },
                                            'last_contact_reply_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'Last contact reply timestamp',
                                            },
                                            'last_admin_reply_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'Last admin reply timestamp',
                                            },
                                            'last_close_at': {
                                                'type': ['integer', 'null'],
                                                'description': 'Last close timestamp',
                                            },
                                            'last_closed_by_id': {
                                                'type': ['string', 'null'],
                                                'description': 'ID of admin who last closed',
                                            },
                                            'count_reopens': {
                                                'type': ['integer', 'null'],
                                                'description': 'Number of reopens',
                                            },
                                            'count_assignments': {
                                                'type': ['integer', 'null'],
                                                'description': 'Number of assignments',
                                            },
                                            'count_conversation_parts': {
                                                'type': ['integer', 'null'],
                                                'description': 'Number of conversation parts',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'conversation_parts': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Reference to conversation parts',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of list',
                                            },
                                            'conversation_parts': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Conversation part (message, note, action)',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'id': {'type': 'string', 'description': 'Unique part identifier'},
                                                        'part_type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of part (comment, note, assignment, etc.)',
                                                        },
                                                        'body': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Part body content',
                                                        },
                                                        'created_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Creation timestamp (Unix)',
                                                        },
                                                        'updated_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Update timestamp (Unix)',
                                                        },
                                                        'notified_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Notification timestamp (Unix)',
                                                        },
                                                        'assigned_to': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'Admin reference',
                                                                    'properties': {
                                                                        'type': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Type of object',
                                                                        },
                                                                        'id': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Admin ID',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'author': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'Message author',
                                                                    'properties': {
                                                                        'type': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Author type (admin, user, bot)',
                                                                        },
                                                                        'id': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Author ID',
                                                                        },
                                                                        'name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Author name',
                                                                        },
                                                                        'email': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Author email',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'attachments': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Message attachment',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Attachment type',
                                                                    },
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'File name',
                                                                    },
                                                                    'url': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'File URL',
                                                                    },
                                                                    'content_type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'MIME type',
                                                                    },
                                                                    'filesize': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'File size in bytes',
                                                                    },
                                                                    'width': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Image width',
                                                                    },
                                                                    'height': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Image height',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        'external_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'External ID',
                                                        },
                                                        'redacted': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether content is redacted',
                                                        },
                                                    },
                                                    'x-airbyte-entity-name': 'conversation_parts',
                                                },
                                            },
                                            'total_count': {
                                                'type': ['integer', 'null'],
                                                'description': 'Total number of parts',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'custom_attributes': {
                                'type': ['object', 'null'],
                                'description': 'Custom attributes',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'conversations',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Conversation object',
                'properties': {
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Type of object (conversation)',
                    },
                    'id': {'type': 'string', 'description': 'Unique conversation identifier'},
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Conversation title',
                    },
                    'created_at': {
                        'type': ['integer', 'null'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'waiting_since': {
                        'type': ['integer', 'null'],
                        'description': 'Waiting since timestamp (Unix)',
                    },
                    'snoozed_until': {
                        'type': ['integer', 'null'],
                        'description': 'Snoozed until timestamp (Unix)',
                    },
                    'open': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether conversation is open',
                    },
                    'state': {
                        'type': ['string', 'null'],
                        'description': 'Conversation state (open, closed, snoozed)',
                    },
                    'read': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether conversation has been read',
                    },
                    'priority': {
                        'type': ['string', 'null'],
                        'description': 'Conversation priority',
                    },
                    'admin_assignee_id': {
                        'type': ['integer', 'null'],
                        'description': 'Assigned admin ID',
                    },
                    'team_assignee_id': {
                        'type': ['string', 'null'],
                        'description': 'Assigned team ID',
                    },
                    'tags': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ConversationTags'},
                            {'type': 'null'},
                        ],
                    },
                    'conversation_rating': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ConversationRating'},
                            {'type': 'null'},
                        ],
                    },
                    'source': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ConversationSource'},
                            {'type': 'null'},
                        ],
                    },
                    'contacts': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ConversationContacts'},
                            {'type': 'null'},
                        ],
                    },
                    'teammates': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ConversationTeammates'},
                            {'type': 'null'},
                        ],
                    },
                    'first_contact_reply': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/FirstContactReply'},
                            {'type': 'null'},
                        ],
                    },
                    'sla_applied': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/SlaApplied'},
                            {'type': 'null'},
                        ],
                    },
                    'statistics': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ConversationStatistics'},
                            {'type': 'null'},
                        ],
                    },
                    'conversation_parts': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ConversationPartsReference'},
                            {'type': 'null'},
                        ],
                    },
                    'custom_attributes': {
                        'type': ['object', 'null'],
                        'description': 'Custom attributes',
                        'additionalProperties': True,
                    },
                },
                'x-airbyte-entity-name': 'conversations',
            },
        ),
        EntityDefinition(
            name='companies',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/companies',
                    action=Action.LIST,
                    description='Returns a paginated list of companies',
                    query_params=['per_page', 'starting_after'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'starting_after': {'type': 'string', 'required': False},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of companies',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of list',
                            },
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Company object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of object (company)',
                                        },
                                        'id': {'type': 'string', 'description': 'Unique company identifier'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Company name',
                                        },
                                        'company_id': {
                                            'type': ['string', 'null'],
                                            'description': 'External company ID',
                                        },
                                        'plan': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Company plan',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plan ID',
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Plan name',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'size': {
                                            'type': ['integer', 'null'],
                                            'description': 'Company size',
                                        },
                                        'industry': {
                                            'type': ['string', 'null'],
                                            'description': 'Industry',
                                        },
                                        'website': {
                                            'type': ['string', 'null'],
                                            'description': 'Website URL',
                                        },
                                        'remote_created_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Remote creation timestamp',
                                        },
                                        'created_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                        'last_request_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last request timestamp (Unix)',
                                        },
                                        'session_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of sessions',
                                        },
                                        'monthly_spend': {
                                            'type': ['number', 'null'],
                                            'description': 'Monthly spend',
                                        },
                                        'user_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of users',
                                        },
                                        'tags': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Tags on company',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of list',
                                                        },
                                                        'tags': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Tag object',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of object (tag)',
                                                                    },
                                                                    'id': {'type': 'string', 'description': 'Unique tag identifier'},
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Tag name',
                                                                    },
                                                                    'applied_at': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Applied timestamp (Unix)',
                                                                    },
                                                                    'applied_by': {
                                                                        'oneOf': [
                                                                            {
                                                                                'type': 'object',
                                                                                'description': 'Admin reference',
                                                                                'properties': {
                                                                                    'type': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Type of object',
                                                                                    },
                                                                                    'id': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Admin ID',
                                                                                    },
                                                                                },
                                                                            },
                                                                            {'type': 'null'},
                                                                        ],
                                                                    },
                                                                },
                                                                'x-airbyte-entity-name': 'tags',
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'segments': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Segments for company',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of list',
                                                        },
                                                        'segments': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Segment object',
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Type of object (segment)',
                                                                    },
                                                                    'id': {'type': 'string', 'description': 'Unique segment identifier'},
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Segment name',
                                                                    },
                                                                    'created_at': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Creation timestamp (Unix)',
                                                                    },
                                                                    'updated_at': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Last update timestamp (Unix)',
                                                                    },
                                                                    'person_type': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Person type (user, lead, contact)',
                                                                    },
                                                                    'count': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Number of contacts in segment',
                                                                    },
                                                                },
                                                                'x-airbyte-entity-name': 'segments',
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'custom_attributes': {
                                            'type': ['object', 'null'],
                                            'description': 'Custom attributes',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'x-airbyte-entity-name': 'companies',
                                },
                            },
                            'total_count': {
                                'type': ['integer', 'null'],
                                'description': 'Total number of companies',
                            },
                            'pages': {
                                'type': ['object', 'null'],
                                'description': 'Pagination metadata',
                                'properties': {
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Type of pagination',
                                    },
                                    'page': {
                                        'type': ['integer', 'null'],
                                        'description': 'Current page number',
                                    },
                                    'per_page': {
                                        'type': ['integer', 'null'],
                                        'description': 'Number of items per page',
                                    },
                                    'total_pages': {
                                        'type': ['integer', 'null'],
                                        'description': 'Total number of pages',
                                    },
                                    'next': {
                                        'type': ['object', 'null'],
                                        'description': 'Cursor for next page',
                                        'properties': {
                                            'page': {
                                                'type': ['integer', 'null'],
                                                'description': 'Next page number',
                                            },
                                            'starting_after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.pages.next.starting_after'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/companies/{id}',
                    action=Action.GET,
                    description='Get a single company by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Company object',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of object (company)',
                            },
                            'id': {'type': 'string', 'description': 'Unique company identifier'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Company name',
                            },
                            'company_id': {
                                'type': ['string', 'null'],
                                'description': 'External company ID',
                            },
                            'plan': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Company plan',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of object',
                                            },
                                            'id': {
                                                'type': ['string', 'null'],
                                                'description': 'Plan ID',
                                            },
                                            'name': {
                                                'type': ['string', 'null'],
                                                'description': 'Plan name',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'size': {
                                'type': ['integer', 'null'],
                                'description': 'Company size',
                            },
                            'industry': {
                                'type': ['string', 'null'],
                                'description': 'Industry',
                            },
                            'website': {
                                'type': ['string', 'null'],
                                'description': 'Website URL',
                            },
                            'remote_created_at': {
                                'type': ['integer', 'null'],
                                'description': 'Remote creation timestamp',
                            },
                            'created_at': {
                                'type': ['integer', 'null'],
                                'description': 'Creation timestamp (Unix)',
                            },
                            'updated_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last update timestamp (Unix)',
                            },
                            'last_request_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last request timestamp (Unix)',
                            },
                            'session_count': {
                                'type': ['integer', 'null'],
                                'description': 'Number of sessions',
                            },
                            'monthly_spend': {
                                'type': ['number', 'null'],
                                'description': 'Monthly spend',
                            },
                            'user_count': {
                                'type': ['integer', 'null'],
                                'description': 'Number of users',
                            },
                            'tags': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Tags on company',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of list',
                                            },
                                            'tags': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Tag object',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object (tag)',
                                                        },
                                                        'id': {'type': 'string', 'description': 'Unique tag identifier'},
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Tag name',
                                                        },
                                                        'applied_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Applied timestamp (Unix)',
                                                        },
                                                        'applied_by': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'Admin reference',
                                                                    'properties': {
                                                                        'type': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Type of object',
                                                                        },
                                                                        'id': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Admin ID',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                    },
                                                    'x-airbyte-entity-name': 'tags',
                                                },
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'segments': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Segments for company',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of list',
                                            },
                                            'segments': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Segment object',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object (segment)',
                                                        },
                                                        'id': {'type': 'string', 'description': 'Unique segment identifier'},
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Segment name',
                                                        },
                                                        'created_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Creation timestamp (Unix)',
                                                        },
                                                        'updated_at': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Last update timestamp (Unix)',
                                                        },
                                                        'person_type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Person type (user, lead, contact)',
                                                        },
                                                        'count': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Number of contacts in segment',
                                                        },
                                                    },
                                                    'x-airbyte-entity-name': 'segments',
                                                },
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'custom_attributes': {
                                'type': ['object', 'null'],
                                'description': 'Custom attributes',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'companies',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Company object',
                'properties': {
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Type of object (company)',
                    },
                    'id': {'type': 'string', 'description': 'Unique company identifier'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Company name',
                    },
                    'company_id': {
                        'type': ['string', 'null'],
                        'description': 'External company ID',
                    },
                    'plan': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CompanyPlan'},
                            {'type': 'null'},
                        ],
                    },
                    'size': {
                        'type': ['integer', 'null'],
                        'description': 'Company size',
                    },
                    'industry': {
                        'type': ['string', 'null'],
                        'description': 'Industry',
                    },
                    'website': {
                        'type': ['string', 'null'],
                        'description': 'Website URL',
                    },
                    'remote_created_at': {
                        'type': ['integer', 'null'],
                        'description': 'Remote creation timestamp',
                    },
                    'created_at': {
                        'type': ['integer', 'null'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'last_request_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last request timestamp (Unix)',
                    },
                    'session_count': {
                        'type': ['integer', 'null'],
                        'description': 'Number of sessions',
                    },
                    'monthly_spend': {
                        'type': ['number', 'null'],
                        'description': 'Monthly spend',
                    },
                    'user_count': {
                        'type': ['integer', 'null'],
                        'description': 'Number of users',
                    },
                    'tags': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CompanyTags'},
                            {'type': 'null'},
                        ],
                    },
                    'segments': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CompanySegments'},
                            {'type': 'null'},
                        ],
                    },
                    'custom_attributes': {
                        'type': ['object', 'null'],
                        'description': 'Custom attributes',
                        'additionalProperties': True,
                    },
                },
                'x-airbyte-entity-name': 'companies',
            },
        ),
        EntityDefinition(
            name='teams',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/teams',
                    action=Action.LIST,
                    description='Returns a list of all teams in the workspace',
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'List of teams',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of list',
                            },
                            'teams': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Team object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of object (team)',
                                        },
                                        'id': {'type': 'string', 'description': 'Unique team identifier'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Team name',
                                        },
                                        'admin_ids': {
                                            'type': 'array',
                                            'items': {'type': 'integer'},
                                            'description': 'List of admin IDs in the team',
                                        },
                                        'admin_priority_level': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Admin priority level settings',
                                                    'properties': {
                                                        'primary_admin_ids': {
                                                            'type': 'array',
                                                            'items': {'type': 'integer'},
                                                            'description': 'Primary admin IDs',
                                                        },
                                                        'secondary_admin_ids': {
                                                            'type': 'array',
                                                            'items': {'type': 'integer'},
                                                            'description': 'Secondary admin IDs',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                    },
                                    'x-airbyte-entity-name': 'teams',
                                },
                            },
                        },
                    },
                    record_extractor='$.teams',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/teams/{id}',
                    action=Action.GET,
                    description='Get a single team by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Team object',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of object (team)',
                            },
                            'id': {'type': 'string', 'description': 'Unique team identifier'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Team name',
                            },
                            'admin_ids': {
                                'type': 'array',
                                'items': {'type': 'integer'},
                                'description': 'List of admin IDs in the team',
                            },
                            'admin_priority_level': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Admin priority level settings',
                                        'properties': {
                                            'primary_admin_ids': {
                                                'type': 'array',
                                                'items': {'type': 'integer'},
                                                'description': 'Primary admin IDs',
                                            },
                                            'secondary_admin_ids': {
                                                'type': 'array',
                                                'items': {'type': 'integer'},
                                                'description': 'Secondary admin IDs',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'x-airbyte-entity-name': 'teams',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Team object',
                'properties': {
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Type of object (team)',
                    },
                    'id': {'type': 'string', 'description': 'Unique team identifier'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Team name',
                    },
                    'admin_ids': {
                        'type': 'array',
                        'items': {'type': 'integer'},
                        'description': 'List of admin IDs in the team',
                    },
                    'admin_priority_level': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/AdminPriorityLevel'},
                            {'type': 'null'},
                        ],
                    },
                },
                'x-airbyte-entity-name': 'teams',
            },
        ),
        EntityDefinition(
            name='admins',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/admins',
                    action=Action.LIST,
                    description='Returns a list of all admins in the workspace',
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'List of admins',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of list',
                            },
                            'admins': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Admin object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of object (admin)',
                                        },
                                        'id': {'type': 'string', 'description': 'Unique admin identifier'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Admin name',
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                            'description': 'Admin email',
                                        },
                                        'email_verified': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether email is verified',
                                        },
                                        'job_title': {
                                            'type': ['string', 'null'],
                                            'description': 'Job title',
                                        },
                                        'away_mode_enabled': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether away mode is enabled',
                                        },
                                        'away_mode_reassign': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether to reassign when away',
                                        },
                                        'has_inbox_seat': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether admin has inbox seat',
                                        },
                                        'team_ids': {
                                            'type': 'array',
                                            'items': {'type': 'integer'},
                                            'description': 'List of team IDs',
                                        },
                                        'avatar': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Avatar image',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'image_url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Avatar image URL',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                    },
                                    'x-airbyte-entity-name': 'admins',
                                },
                            },
                        },
                    },
                    record_extractor='$.admins',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/admins/{id}',
                    action=Action.GET,
                    description='Get a single admin by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Admin object',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of object (admin)',
                            },
                            'id': {'type': 'string', 'description': 'Unique admin identifier'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Admin name',
                            },
                            'email': {
                                'type': ['string', 'null'],
                                'description': 'Admin email',
                            },
                            'email_verified': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether email is verified',
                            },
                            'job_title': {
                                'type': ['string', 'null'],
                                'description': 'Job title',
                            },
                            'away_mode_enabled': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether away mode is enabled',
                            },
                            'away_mode_reassign': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to reassign when away',
                            },
                            'has_inbox_seat': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether admin has inbox seat',
                            },
                            'team_ids': {
                                'type': 'array',
                                'items': {'type': 'integer'},
                                'description': 'List of team IDs',
                            },
                            'avatar': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Avatar image',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of object',
                                            },
                                            'image_url': {
                                                'type': ['string', 'null'],
                                                'description': 'Avatar image URL',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'x-airbyte-entity-name': 'admins',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Admin object',
                'properties': {
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Type of object (admin)',
                    },
                    'id': {'type': 'string', 'description': 'Unique admin identifier'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Admin name',
                    },
                    'email': {
                        'type': ['string', 'null'],
                        'description': 'Admin email',
                    },
                    'email_verified': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether email is verified',
                    },
                    'job_title': {
                        'type': ['string', 'null'],
                        'description': 'Job title',
                    },
                    'away_mode_enabled': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether away mode is enabled',
                    },
                    'away_mode_reassign': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether to reassign when away',
                    },
                    'has_inbox_seat': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether admin has inbox seat',
                    },
                    'team_ids': {
                        'type': 'array',
                        'items': {'type': 'integer'},
                        'description': 'List of team IDs',
                    },
                    'avatar': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Avatar'},
                            {'type': 'null'},
                        ],
                    },
                },
                'x-airbyte-entity-name': 'admins',
            },
        ),
        EntityDefinition(
            name='tags',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tags',
                    action=Action.LIST,
                    description='Returns a list of all tags in the workspace',
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'List of tags',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of list',
                            },
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Tag object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of object (tag)',
                                        },
                                        'id': {'type': 'string', 'description': 'Unique tag identifier'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Tag name',
                                        },
                                        'applied_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Applied timestamp (Unix)',
                                        },
                                        'applied_by': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Admin reference',
                                                    'properties': {
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Type of object',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Admin ID',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tags',
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/tags/{id}',
                    action=Action.GET,
                    description='Get a single tag by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Tag object',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of object (tag)',
                            },
                            'id': {'type': 'string', 'description': 'Unique tag identifier'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Tag name',
                            },
                            'applied_at': {
                                'type': ['integer', 'null'],
                                'description': 'Applied timestamp (Unix)',
                            },
                            'applied_by': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Admin reference',
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of object',
                                            },
                                            'id': {
                                                'type': ['string', 'null'],
                                                'description': 'Admin ID',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'x-airbyte-entity-name': 'tags',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Tag object',
                'properties': {
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Type of object (tag)',
                    },
                    'id': {'type': 'string', 'description': 'Unique tag identifier'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Tag name',
                    },
                    'applied_at': {
                        'type': ['integer', 'null'],
                        'description': 'Applied timestamp (Unix)',
                    },
                    'applied_by': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/AdminReference'},
                            {'type': 'null'},
                        ],
                    },
                },
                'x-airbyte-entity-name': 'tags',
            },
        ),
        EntityDefinition(
            name='segments',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/segments',
                    action=Action.LIST,
                    description='Returns a list of all segments in the workspace',
                    query_params=['include_count'],
                    query_params_schema={
                        'include_count': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'List of segments',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of list',
                            },
                            'segments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Segment object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of object (segment)',
                                        },
                                        'id': {'type': 'string', 'description': 'Unique segment identifier'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Segment name',
                                        },
                                        'created_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated_at': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                        'person_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Person type (user, lead, contact)',
                                        },
                                        'count': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of contacts in segment',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'segments',
                                },
                            },
                        },
                    },
                    record_extractor='$.segments',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/segments/{id}',
                    action=Action.GET,
                    description='Get a single segment by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Segment object',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of object (segment)',
                            },
                            'id': {'type': 'string', 'description': 'Unique segment identifier'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Segment name',
                            },
                            'created_at': {
                                'type': ['integer', 'null'],
                                'description': 'Creation timestamp (Unix)',
                            },
                            'updated_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last update timestamp (Unix)',
                            },
                            'person_type': {
                                'type': ['string', 'null'],
                                'description': 'Person type (user, lead, contact)',
                            },
                            'count': {
                                'type': ['integer', 'null'],
                                'description': 'Number of contacts in segment',
                            },
                        },
                        'x-airbyte-entity-name': 'segments',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Segment object',
                'properties': {
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Type of object (segment)',
                    },
                    'id': {'type': 'string', 'description': 'Unique segment identifier'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Segment name',
                    },
                    'created_at': {
                        'type': ['integer', 'null'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'person_type': {
                        'type': ['string', 'null'],
                        'description': 'Person type (user, lead, contact)',
                    },
                    'count': {
                        'type': ['integer', 'null'],
                        'description': 'Number of contacts in segment',
                    },
                },
                'x-airbyte-entity-name': 'segments',
            },
        ),
    ],
    search_field_paths={
        'companies': [
            'app_id',
            'company_id',
            'created_at',
            'custom_attributes',
            'id',
            'industry',
            'monthly_spend',
            'name',
            'plan',
            'plan.id',
            'plan.name',
            'plan.type',
            'remote_created_at',
            'segments',
            'segments.segments',
            'segments.segments[]',
            'segments.type',
            'session_count',
            'size',
            'tags',
            'tags.tags',
            'tags.tags[]',
            'tags.type',
            'type',
            'updated_at',
            'user_count',
            'website',
        ],
        'contacts': [
            'android_app_name',
            'android_app_version',
            'android_device',
            'android_last_seen_at',
            'android_os_version',
            'android_sdk_version',
            'avatar',
            'browser',
            'browser_language',
            'browser_version',
            'companies',
            'companies.data',
            'companies.data[]',
            'companies.has_more',
            'companies.total_count',
            'companies.type',
            'companies.url',
            'created_at',
            'custom_attributes',
            'email',
            'external_id',
            'has_hard_bounced',
            'id',
            'ios_app_name',
            'ios_app_version',
            'ios_device',
            'ios_last_seen_at',
            'ios_os_version',
            'ios_sdk_version',
            'language_override',
            'last_contacted_at',
            'last_email_clicked_at',
            'last_email_opened_at',
            'last_replied_at',
            'last_seen_at',
            'location',
            'location.city',
            'location.continent_code',
            'location.country',
            'location.country_code',
            'location.region',
            'location.type',
            'marked_email_as_spam',
            'name',
            'notes',
            'notes.data',
            'notes.data[]',
            'notes.has_more',
            'notes.total_count',
            'notes.type',
            'notes.url',
            'opted_in_subscription_types',
            'opted_in_subscription_types.data',
            'opted_in_subscription_types.data[]',
            'opted_in_subscription_types.has_more',
            'opted_in_subscription_types.total_count',
            'opted_in_subscription_types.type',
            'opted_in_subscription_types.url',
            'opted_out_subscription_types',
            'opted_out_subscription_types.data',
            'opted_out_subscription_types.data[]',
            'opted_out_subscription_types.has_more',
            'opted_out_subscription_types.total_count',
            'opted_out_subscription_types.type',
            'opted_out_subscription_types.url',
            'os',
            'owner_id',
            'phone',
            'referrer',
            'role',
            'signed_up_at',
            'sms_consent',
            'social_profiles',
            'social_profiles.data',
            'social_profiles.data[]',
            'social_profiles.type',
            'tags',
            'tags.data',
            'tags.data[]',
            'tags.has_more',
            'tags.total_count',
            'tags.type',
            'tags.url',
            'type',
            'unsubscribed_from_emails',
            'unsubscribed_from_sms',
            'updated_at',
            'utm_campaign',
            'utm_content',
            'utm_medium',
            'utm_source',
            'utm_term',
            'workspace_id',
        ],
        'conversation_parts': [
            'assigned_to',
            'attachments',
            'attachments[]',
            'author',
            'author.email',
            'author.id',
            'author.name',
            'author.type',
            'body',
            'conversation_created_at',
            'conversation_id',
            'conversation_total_parts',
            'conversation_updated_at',
            'created_at',
            'external_id',
            'id',
            'notified_at',
            'part_type',
            'redacted',
            'type',
            'updated_at',
        ],
        'conversations': [
            'admin_assignee_id',
            'ai_agent',
            'ai_agent.content_sources',
            'ai_agent.last_answer_type',
            'ai_agent.rating',
            'ai_agent.rating_remark',
            'ai_agent.resolution_state',
            'ai_agent.source_id',
            'ai_agent.source_title',
            'ai_agent.source_type',
            'ai_agent.triggered_at',
            'ai_agent_participated',
            'assignee',
            'assignee.email',
            'assignee.id',
            'assignee.name',
            'assignee.type',
            'contacts',
            'conversation_message',
            'conversation_message.attachments',
            'conversation_message.attachments[]',
            'conversation_message.author',
            'conversation_message.body',
            'conversation_message.delivered_as',
            'conversation_message.id',
            'conversation_message.subject',
            'conversation_message.type',
            'conversation_message.url',
            'conversation_rating',
            'conversation_rating.created_at',
            'conversation_rating.customer',
            'conversation_rating.rating',
            'conversation_rating.remark',
            'conversation_rating.teammate',
            'created_at',
            'custom_attributes',
            'customer_first_reply',
            'customer_first_reply.created_at',
            'customer_first_reply.type',
            'customer_first_reply.url',
            'customers',
            'customers[]',
            'first_contact_reply',
            'first_contact_reply.created_at',
            'first_contact_reply.type',
            'first_contact_reply.url',
            'id',
            'linked_objects',
            'linked_objects.data',
            'linked_objects.data[]',
            'linked_objects.has_more',
            'linked_objects.total_count',
            'linked_objects.type',
            'linked_objects.url',
            'open',
            'priority',
            'read',
            'redacted',
            'sent_at',
            'sla_applied',
            'sla_applied.sla_name',
            'sla_applied.sla_status',
            'snoozed_until',
            'source',
            'source.attachments',
            'source.attachments[]',
            'source.author',
            'source.body',
            'source.delivered_as',
            'source.id',
            'source.redacted',
            'source.subject',
            'source.type',
            'source.url',
            'state',
            'statistics',
            'statistics.count_assignments',
            'statistics.count_conversation_parts',
            'statistics.count_reopens',
            'statistics.first_admin_reply_at',
            'statistics.first_assignment_at',
            'statistics.first_close_at',
            'statistics.first_contact_reply_at',
            'statistics.last_admin_reply_at',
            'statistics.last_assignment_admin_reply_at',
            'statistics.last_assignment_at',
            'statistics.last_close_at',
            'statistics.last_closed_by_id',
            'statistics.last_contact_reply_at',
            'statistics.median_time_to_reply',
            'statistics.time_to_admin_reply',
            'statistics.time_to_assignment',
            'statistics.time_to_first_close',
            'statistics.time_to_last_close',
            'statistics.type',
            'tags',
            'team_assignee_id',
            'teammates',
            'teammates.admins',
            'teammates.admins[]',
            'teammates.type',
            'title',
            'topics',
            'topics.topics',
            'topics.topics[]',
            'topics.total_count',
            'topics.type',
            'type',
            'updated_at',
            'user',
            'user.id',
            'user.type',
            'waiting_since',
        ],
        'teams': [
            'admin_ids',
            'admin_ids[]',
            'id',
            'name',
            'type',
        ],
    },
)