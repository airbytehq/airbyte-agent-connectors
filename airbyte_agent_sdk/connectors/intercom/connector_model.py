"""
Connector model for intercom.

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
    EntityRelationshipConfig,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

IntercomConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('d8313939-3782-41b0-be29-b3ca20d8dd3a'),
    name='intercom',
    version='0.1.10',
    base_url='https://api.intercom.io',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AuthConfigSpec(
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
            stream_name='contacts',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
                Action.DELETE,
            ],
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
                            'minimum': 1,
                            'maximum': 150,
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
                                    'x-airbyte-stream-name': 'contacts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Intercom contacts (users and leads) with profile and activity data',
                                        'when_to_use': 'Looking up customer or lead information in Intercom',
                                        'trigger_phrases': [
                                            'intercom contact',
                                            'customer',
                                            'lead',
                                            'user profile',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Find a contact in Intercom', 'Look up a customer by email'],
                                        'search_strategy': 'Search by email, name, or external ID',
                                    },
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
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/contacts',
                    action=Action.CREATE,
                    description='Create a new contact (user or lead)',
                    body_fields=[
                        'role',
                        'external_id',
                        'email',
                        'phone',
                        'name',
                        'avatar',
                        'signed_up_at',
                        'last_seen_at',
                        'owner_id',
                        'unsubscribed_from_emails',
                        'custom_attributes',
                    ],
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'role': {'type': 'string', 'description': 'The role of the contact (user or lead)'},
                            'external_id': {'type': 'string', 'description': 'A unique identifier for the contact from your system'},
                            'email': {'type': 'string', 'description': "The contact's email address"},
                            'phone': {'type': 'string', 'description': "The contact's phone number"},
                            'name': {'type': 'string', 'description': "The contact's full name"},
                            'avatar': {'type': 'string', 'description': "An image URL for the contact's avatar"},
                            'signed_up_at': {'type': 'integer', 'description': 'Sign up timestamp (Unix)'},
                            'last_seen_at': {'type': 'integer', 'description': 'Last seen timestamp (Unix)'},
                            'owner_id': {'type': 'integer', 'description': 'The ID of the admin assigned as owner'},
                            'unsubscribed_from_emails': {'type': 'boolean', 'description': 'Whether the contact is unsubscribed from emails'},
                            'custom_attributes': {
                                'type': 'object',
                                'description': 'Custom attributes for the contact',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['role'],
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
                        'x-airbyte-stream-name': 'contacts',
                        'x-airbyte-ai-hints': {
                            'summary': 'Intercom contacts (users and leads) with profile and activity data',
                            'when_to_use': 'Looking up customer or lead information in Intercom',
                            'trigger_phrases': [
                                'intercom contact',
                                'customer',
                                'lead',
                                'user profile',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find a contact in Intercom', 'Look up a customer by email'],
                            'search_strategy': 'Search by email, name, or external ID',
                        },
                    },
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
                        'x-airbyte-stream-name': 'contacts',
                        'x-airbyte-ai-hints': {
                            'summary': 'Intercom contacts (users and leads) with profile and activity data',
                            'when_to_use': 'Looking up customer or lead information in Intercom',
                            'trigger_phrases': [
                                'intercom contact',
                                'customer',
                                'lead',
                                'user profile',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find a contact in Intercom', 'Look up a customer by email'],
                            'search_strategy': 'Search by email, name, or external ID',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/contacts/{id}',
                    action=Action.UPDATE,
                    description='Update an existing contact by ID',
                    body_fields=[
                        'role',
                        'external_id',
                        'email',
                        'phone',
                        'name',
                        'avatar',
                        'signed_up_at',
                        'last_seen_at',
                        'owner_id',
                        'unsubscribed_from_emails',
                        'custom_attributes',
                    ],
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
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'role': {'type': 'string', 'description': 'The role of the contact (user or lead)'},
                            'external_id': {'type': 'string', 'description': 'A unique identifier for the contact from your system'},
                            'email': {'type': 'string', 'description': "The contact's email address"},
                            'phone': {'type': 'string', 'description': "The contact's phone number"},
                            'name': {'type': 'string', 'description': "The contact's full name"},
                            'avatar': {'type': 'string', 'description': "An image URL for the contact's avatar"},
                            'signed_up_at': {'type': 'integer', 'description': 'Sign up timestamp (Unix)'},
                            'last_seen_at': {'type': 'integer', 'description': 'Last seen timestamp (Unix)'},
                            'owner_id': {'type': 'integer', 'description': 'The ID of the admin assigned as owner'},
                            'unsubscribed_from_emails': {'type': 'boolean', 'description': 'Whether the contact is unsubscribed from emails'},
                            'custom_attributes': {
                                'type': 'object',
                                'description': 'Custom attributes for the contact',
                                'additionalProperties': True,
                            },
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
                        'x-airbyte-stream-name': 'contacts',
                        'x-airbyte-ai-hints': {
                            'summary': 'Intercom contacts (users and leads) with profile and activity data',
                            'when_to_use': 'Looking up customer or lead information in Intercom',
                            'trigger_phrases': [
                                'intercom contact',
                                'customer',
                                'lead',
                                'user profile',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find a contact in Intercom', 'Look up a customer by email'],
                            'search_strategy': 'Search by email, name, or external ID',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/contacts/{id}',
                    action=Action.DELETE,
                    description='Permanently delete a contact by ID',
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
                        'description': 'Response from deleting a contact',
                        'properties': {
                            'type': {'type': 'string', 'description': 'Type of object (contact)'},
                            'id': {'type': 'string', 'description': 'The ID of the deleted contact'},
                            'external_id': {
                                'type': ['string', 'null'],
                                'description': 'External ID of the deleted contact',
                            },
                            'deleted': {'type': 'boolean', 'description': 'Whether the contact was successfully deleted'},
                        },
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
                'x-airbyte-stream-name': 'contacts',
                'x-airbyte-ai-hints': {
                    'summary': 'Intercom contacts (users and leads) with profile and activity data',
                    'when_to_use': 'Looking up customer or lead information in Intercom',
                    'trigger_phrases': [
                        'intercom contact',
                        'customer',
                        'lead',
                        'user profile',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Find a contact in Intercom', 'Look up a customer by email'],
                    'search_strategy': 'Search by email, name, or external ID',
                },
            },
            ai_hints={
                'summary': 'Intercom contacts (users and leads) with profile and activity data',
                'when_to_use': 'Looking up customer or lead information in Intercom',
                'trigger_phrases': [
                    'intercom contact',
                    'customer',
                    'lead',
                    'user profile',
                ],
                'freshness': 'live',
                'example_questions': ['Find a contact in Intercom', 'Look up a customer by email'],
                'search_strategy': 'Search by email, name, or external ID',
            },
        ),
        EntityDefinition(
            name='conversations',
            stream_name='conversations',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
                Action.DELETE,
            ],
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
                            'minimum': 1,
                            'maximum': 150,
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
                                                                'x-airbyte-stream-name': 'tags',
                                                                'x-airbyte-ai-hints': {
                                                                    'summary': 'Tags for categorizing contacts, companies, and conversations',
                                                                    'when_to_use': 'Questions about available tags or contact categorization',
                                                                    'trigger_phrases': ['intercom tag', 'contact tag'],
                                                                    'freshness': 'live',
                                                                    'example_questions': ['What tags exist in Intercom?'],
                                                                    'search_strategy': 'Search by name',
                                                                },
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
                                                                'x-airbyte-stream-name': 'conversation_parts',
                                                                'x-airbyte-ai-hints': {
                                                                    'summary': 'Individual messages within Intercom conversations',
                                                                    'when_to_use': 'Looking at specific messages in a conversation thread',
                                                                    'trigger_phrases': ['conversation part', 'message', 'reply'],
                                                                    'freshness': 'live',
                                                                    'example_questions': ['Show messages in a conversation'],
                                                                    'search_strategy': 'Filter by conversation',
                                                                },
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
                                    'x-airbyte-stream-name': 'conversations',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Intercom conversations (chat threads) with customers',
                                        'when_to_use': 'Questions about customer conversations or support chat history',
                                        'trigger_phrases': [
                                            'intercom conversation',
                                            'chat',
                                            'customer message',
                                            'support thread',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Show open Intercom conversations', 'Find chats with a customer'],
                                        'search_strategy': 'Search by contact or filter by status and assignee',
                                    },
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
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/conversations',
                    action=Action.CREATE,
                    description='Create a new conversation initiated by a contact (user or lead)',
                    body_fields=[
                        'from',
                        'body',
                        'subject',
                        'attachment_urls',
                        'created_at',
                    ],
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'from': {
                                'type': 'object',
                                'description': 'The contact (user or lead) initiating the conversation',
                                'required': ['type', 'id'],
                                'properties': {
                                    'type': {
                                        'type': 'string',
                                        'description': 'The type of the contact (lead, user, or contact)',
                                        'enum': ['lead', 'user', 'contact'],
                                    },
                                    'id': {'type': 'string', 'description': 'The identifier for the contact as given by Intercom (a 24 character UUID)'},
                                },
                            },
                            'body': {'type': 'string', 'description': 'The content of the initial message in the conversation'},
                            'subject': {'type': 'string', 'description': 'The subject line of the conversation (optional)'},
                            'attachment_urls': {
                                'type': 'array',
                                'description': 'A list of URLs of attached files (max 10)',
                                'items': {'type': 'string'},
                            },
                            'created_at': {'type': 'integer', 'description': 'Optional timestamp for the conversation creation (Unix)'},
                        },
                        'required': ['from', 'body'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Message object returned when creating a conversation',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of object',
                            },
                            'id': {'type': 'string', 'description': 'Unique message identifier'},
                            'created_at': {
                                'type': ['integer', 'null'],
                                'description': 'Creation timestamp (Unix)',
                            },
                            'subject': {
                                'type': ['string', 'null'],
                                'description': 'Subject of the message',
                            },
                            'body': {
                                'type': ['string', 'null'],
                                'description': 'Body of the message',
                            },
                            'message_type': {
                                'type': ['string', 'null'],
                                'description': 'Type of message (email, inapp, facebook, twitter)',
                            },
                            'conversation_id': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the conversation created',
                            },
                        },
                    },
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
                                                    'x-airbyte-stream-name': 'tags',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Tags for categorizing contacts, companies, and conversations',
                                                        'when_to_use': 'Questions about available tags or contact categorization',
                                                        'trigger_phrases': ['intercom tag', 'contact tag'],
                                                        'freshness': 'live',
                                                        'example_questions': ['What tags exist in Intercom?'],
                                                        'search_strategy': 'Search by name',
                                                    },
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
                                                    'x-airbyte-stream-name': 'conversation_parts',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Individual messages within Intercom conversations',
                                                        'when_to_use': 'Looking at specific messages in a conversation thread',
                                                        'trigger_phrases': ['conversation part', 'message', 'reply'],
                                                        'freshness': 'live',
                                                        'example_questions': ['Show messages in a conversation'],
                                                        'search_strategy': 'Filter by conversation',
                                                    },
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
                        'x-airbyte-stream-name': 'conversations',
                        'x-airbyte-ai-hints': {
                            'summary': 'Intercom conversations (chat threads) with customers',
                            'when_to_use': 'Questions about customer conversations or support chat history',
                            'trigger_phrases': [
                                'intercom conversation',
                                'chat',
                                'customer message',
                                'support thread',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Show open Intercom conversations', 'Find chats with a customer'],
                            'search_strategy': 'Search by contact or filter by status and assignee',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/conversations/{id}',
                    action=Action.UPDATE,
                    description='Update conversation attributes such as custom_attributes or read status',
                    body_fields=['read', 'custom_attributes'],
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
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'read': {'type': 'boolean', 'description': 'Mark the conversation as read or unread'},
                            'custom_attributes': {
                                'type': 'object',
                                'description': 'Custom attributes to set on the conversation',
                                'additionalProperties': True,
                            },
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
                                                    'x-airbyte-stream-name': 'tags',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Tags for categorizing contacts, companies, and conversations',
                                                        'when_to_use': 'Questions about available tags or contact categorization',
                                                        'trigger_phrases': ['intercom tag', 'contact tag'],
                                                        'freshness': 'live',
                                                        'example_questions': ['What tags exist in Intercom?'],
                                                        'search_strategy': 'Search by name',
                                                    },
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
                                                    'x-airbyte-stream-name': 'conversation_parts',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Individual messages within Intercom conversations',
                                                        'when_to_use': 'Looking at specific messages in a conversation thread',
                                                        'trigger_phrases': ['conversation part', 'message', 'reply'],
                                                        'freshness': 'live',
                                                        'example_questions': ['Show messages in a conversation'],
                                                        'search_strategy': 'Filter by conversation',
                                                    },
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
                        'x-airbyte-stream-name': 'conversations',
                        'x-airbyte-ai-hints': {
                            'summary': 'Intercom conversations (chat threads) with customers',
                            'when_to_use': 'Questions about customer conversations or support chat history',
                            'trigger_phrases': [
                                'intercom conversation',
                                'chat',
                                'customer message',
                                'support thread',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Show open Intercom conversations', 'Find chats with a customer'],
                            'search_strategy': 'Search by contact or filter by status and assignee',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/conversations/{id}',
                    action=Action.DELETE,
                    description='Permanently delete a conversation by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.14',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from deleting a conversation',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The ID of the deleted conversation'},
                            'object': {'type': 'string', 'description': 'Type of object (conversation)'},
                            'deleted': {'type': 'boolean', 'description': 'Whether the conversation was successfully deleted'},
                        },
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
                'x-airbyte-stream-name': 'conversations',
                'x-airbyte-ai-hints': {
                    'summary': 'Intercom conversations (chat threads) with customers',
                    'when_to_use': 'Questions about customer conversations or support chat history',
                    'trigger_phrases': [
                        'intercom conversation',
                        'chat',
                        'customer message',
                        'support thread',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show open Intercom conversations', 'Find chats with a customer'],
                    'search_strategy': 'Search by contact or filter by status and assignee',
                },
            },
            ai_hints={
                'summary': 'Intercom conversations (chat threads) with customers',
                'when_to_use': 'Questions about customer conversations or support chat history',
                'trigger_phrases': [
                    'intercom conversation',
                    'chat',
                    'customer message',
                    'support thread',
                ],
                'freshness': 'live',
                'example_questions': ['Show open Intercom conversations', 'Find chats with a customer'],
                'search_strategy': 'Search by contact or filter by status and assignee',
            },
        ),
        EntityDefinition(
            name='companies',
            stream_name='companies',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
                Action.DELETE,
            ],
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
                            'minimum': 1,
                            'maximum': 150,
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
                                        'app_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID of the application associated with the company',
                                        },
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
                                                                'x-airbyte-stream-name': 'tags',
                                                                'x-airbyte-ai-hints': {
                                                                    'summary': 'Tags for categorizing contacts, companies, and conversations',
                                                                    'when_to_use': 'Questions about available tags or contact categorization',
                                                                    'trigger_phrases': ['intercom tag', 'contact tag'],
                                                                    'freshness': 'live',
                                                                    'example_questions': ['What tags exist in Intercom?'],
                                                                    'search_strategy': 'Search by name',
                                                                },
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
                                                                'x-airbyte-stream-name': 'segments',
                                                                'x-airbyte-ai-hints': {
                                                                    'summary': 'Dynamic segments of contacts based on filter criteria',
                                                                    'when_to_use': 'Questions about user segments or customer groups',
                                                                    'trigger_phrases': ['intercom segment', 'user segment', 'customer group'],
                                                                    'freshness': 'live',
                                                                    'example_questions': ['What segments are defined in Intercom?'],
                                                                    'search_strategy': 'Search by name',
                                                                },
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
                                    'x-airbyte-stream-name': 'companies',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Companies associated with Intercom contacts',
                                        'when_to_use': 'Looking up company details or grouping contacts by company',
                                        'trigger_phrases': ['intercom company', 'company details'],
                                        'freshness': 'live',
                                        'example_questions': ['Show companies in Intercom'],
                                        'search_strategy': 'Search by name or company ID',
                                    },
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
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/companies',
                    action=Action.CREATE,
                    description='Create a new company or update an existing one by company_id',
                    body_fields=[
                        'company_id',
                        'name',
                        'plan',
                        'monthly_spend',
                        'size',
                        'website',
                        'industry',
                        'custom_attributes',
                    ],
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'company_id': {'type': 'string', 'description': 'A unique identifier for the company from your system'},
                            'name': {'type': 'string', 'description': 'The name of the company'},
                            'plan': {'type': 'string', 'description': 'The name of the plan the company is on'},
                            'monthly_spend': {'type': 'number', 'description': 'The monthly spend of the company'},
                            'size': {'type': 'integer', 'description': 'The number of employees in the company'},
                            'website': {'type': 'string', 'description': 'The URL of the company website'},
                            'industry': {'type': 'string', 'description': 'The industry the company operates in'},
                            'custom_attributes': {
                                'type': 'object',
                                'description': 'Custom attributes for the company',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['company_id'],
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
                            'app_id': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the application associated with the company',
                            },
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
                                                    'x-airbyte-stream-name': 'tags',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Tags for categorizing contacts, companies, and conversations',
                                                        'when_to_use': 'Questions about available tags or contact categorization',
                                                        'trigger_phrases': ['intercom tag', 'contact tag'],
                                                        'freshness': 'live',
                                                        'example_questions': ['What tags exist in Intercom?'],
                                                        'search_strategy': 'Search by name',
                                                    },
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
                                                    'x-airbyte-stream-name': 'segments',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Dynamic segments of contacts based on filter criteria',
                                                        'when_to_use': 'Questions about user segments or customer groups',
                                                        'trigger_phrases': ['intercom segment', 'user segment', 'customer group'],
                                                        'freshness': 'live',
                                                        'example_questions': ['What segments are defined in Intercom?'],
                                                        'search_strategy': 'Search by name',
                                                    },
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
                        'x-airbyte-stream-name': 'companies',
                        'x-airbyte-ai-hints': {
                            'summary': 'Companies associated with Intercom contacts',
                            'when_to_use': 'Looking up company details or grouping contacts by company',
                            'trigger_phrases': ['intercom company', 'company details'],
                            'freshness': 'live',
                            'example_questions': ['Show companies in Intercom'],
                            'search_strategy': 'Search by name or company ID',
                        },
                    },
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
                            'app_id': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the application associated with the company',
                            },
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
                                                    'x-airbyte-stream-name': 'tags',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Tags for categorizing contacts, companies, and conversations',
                                                        'when_to_use': 'Questions about available tags or contact categorization',
                                                        'trigger_phrases': ['intercom tag', 'contact tag'],
                                                        'freshness': 'live',
                                                        'example_questions': ['What tags exist in Intercom?'],
                                                        'search_strategy': 'Search by name',
                                                    },
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
                                                    'x-airbyte-stream-name': 'segments',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Dynamic segments of contacts based on filter criteria',
                                                        'when_to_use': 'Questions about user segments or customer groups',
                                                        'trigger_phrases': ['intercom segment', 'user segment', 'customer group'],
                                                        'freshness': 'live',
                                                        'example_questions': ['What segments are defined in Intercom?'],
                                                        'search_strategy': 'Search by name',
                                                    },
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
                        'x-airbyte-stream-name': 'companies',
                        'x-airbyte-ai-hints': {
                            'summary': 'Companies associated with Intercom contacts',
                            'when_to_use': 'Looking up company details or grouping contacts by company',
                            'trigger_phrases': ['intercom company', 'company details'],
                            'freshness': 'live',
                            'example_questions': ['Show companies in Intercom'],
                            'search_strategy': 'Search by name or company ID',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/companies/{id}',
                    action=Action.UPDATE,
                    description='Update an existing company by ID',
                    body_fields=[
                        'name',
                        'plan',
                        'monthly_spend',
                        'size',
                        'website',
                        'industry',
                        'custom_attributes',
                    ],
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
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the company'},
                            'plan': {'type': 'string', 'description': 'The name of the plan the company is on'},
                            'monthly_spend': {'type': 'number', 'description': 'The monthly spend of the company'},
                            'size': {'type': 'integer', 'description': 'The number of employees in the company'},
                            'website': {'type': 'string', 'description': 'The URL of the company website'},
                            'industry': {'type': 'string', 'description': 'The industry the company operates in'},
                            'custom_attributes': {
                                'type': 'object',
                                'description': 'Custom attributes for the company',
                                'additionalProperties': True,
                            },
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
                            'app_id': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the application associated with the company',
                            },
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
                                                    'x-airbyte-stream-name': 'tags',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Tags for categorizing contacts, companies, and conversations',
                                                        'when_to_use': 'Questions about available tags or contact categorization',
                                                        'trigger_phrases': ['intercom tag', 'contact tag'],
                                                        'freshness': 'live',
                                                        'example_questions': ['What tags exist in Intercom?'],
                                                        'search_strategy': 'Search by name',
                                                    },
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
                                                    'x-airbyte-stream-name': 'segments',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Dynamic segments of contacts based on filter criteria',
                                                        'when_to_use': 'Questions about user segments or customer groups',
                                                        'trigger_phrases': ['intercom segment', 'user segment', 'customer group'],
                                                        'freshness': 'live',
                                                        'example_questions': ['What segments are defined in Intercom?'],
                                                        'search_strategy': 'Search by name',
                                                    },
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
                        'x-airbyte-stream-name': 'companies',
                        'x-airbyte-ai-hints': {
                            'summary': 'Companies associated with Intercom contacts',
                            'when_to_use': 'Looking up company details or grouping contacts by company',
                            'trigger_phrases': ['intercom company', 'company details'],
                            'freshness': 'live',
                            'example_questions': ['Show companies in Intercom'],
                            'search_strategy': 'Search by name or company ID',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/companies/{id}',
                    action=Action.DELETE,
                    description='Permanently delete a company by ID',
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
                        'description': 'Response from deleting a company',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The ID of the deleted company'},
                            'object': {'type': 'string', 'description': 'Type of object (company)'},
                            'deleted': {'type': 'boolean', 'description': 'Whether the company was successfully deleted'},
                        },
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
                    'app_id': {
                        'type': ['string', 'null'],
                        'description': 'The ID of the application associated with the company',
                    },
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
                'x-airbyte-stream-name': 'companies',
                'x-airbyte-ai-hints': {
                    'summary': 'Companies associated with Intercom contacts',
                    'when_to_use': 'Looking up company details or grouping contacts by company',
                    'trigger_phrases': ['intercom company', 'company details'],
                    'freshness': 'live',
                    'example_questions': ['Show companies in Intercom'],
                    'search_strategy': 'Search by name or company ID',
                },
            },
            ai_hints={
                'summary': 'Companies associated with Intercom contacts',
                'when_to_use': 'Looking up company details or grouping contacts by company',
                'trigger_phrases': ['intercom company', 'company details'],
                'freshness': 'live',
                'example_questions': ['Show companies in Intercom'],
                'search_strategy': 'Search by name or company ID',
            },
        ),
        EntityDefinition(
            name='teams',
            stream_name='teams',
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
                                    'x-airbyte-stream-name': 'teams',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Support teams in Intercom for conversation routing',
                                        'when_to_use': 'Questions about team structure or conversation assignment',
                                        'trigger_phrases': ['intercom team', 'support team'],
                                        'freshness': 'static',
                                        'example_questions': ['What teams are in Intercom?'],
                                        'search_strategy': 'List all teams',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.teams',
                    no_pagination='The Intercom /teams endpoint returns the full set of configured teams as a team.list response in a single call; no pages/starting_after pagination is exposed.',
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
                        'x-airbyte-stream-name': 'teams',
                        'x-airbyte-ai-hints': {
                            'summary': 'Support teams in Intercom for conversation routing',
                            'when_to_use': 'Questions about team structure or conversation assignment',
                            'trigger_phrases': ['intercom team', 'support team'],
                            'freshness': 'static',
                            'example_questions': ['What teams are in Intercom?'],
                            'search_strategy': 'List all teams',
                        },
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
                'x-airbyte-stream-name': 'teams',
                'x-airbyte-ai-hints': {
                    'summary': 'Support teams in Intercom for conversation routing',
                    'when_to_use': 'Questions about team structure or conversation assignment',
                    'trigger_phrases': ['intercom team', 'support team'],
                    'freshness': 'static',
                    'example_questions': ['What teams are in Intercom?'],
                    'search_strategy': 'List all teams',
                },
            },
            ai_hints={
                'summary': 'Support teams in Intercom for conversation routing',
                'when_to_use': 'Questions about team structure or conversation assignment',
                'trigger_phrases': ['intercom team', 'support team'],
                'freshness': 'static',
                'example_questions': ['What teams are in Intercom?'],
                'search_strategy': 'List all teams',
            },
        ),
        EntityDefinition(
            name='admins',
            stream_name='admins',
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
                                    'x-airbyte-stream-name': 'admins',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Intercom admin users (agents and operators)',
                                        'when_to_use': 'Looking up support agent details',
                                        'trigger_phrases': ['intercom admin', 'support agent', 'operator'],
                                        'freshness': 'live',
                                        'example_questions': ['Who are the Intercom admins?'],
                                        'search_strategy': 'Search by name or email',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.admins',
                    no_pagination='The Intercom /admins endpoint returns the full set of workspace admins as an admin.list response in a single call; no pages/starting_after pagination is exposed.',
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
                        'x-airbyte-stream-name': 'admins',
                        'x-airbyte-ai-hints': {
                            'summary': 'Intercom admin users (agents and operators)',
                            'when_to_use': 'Looking up support agent details',
                            'trigger_phrases': ['intercom admin', 'support agent', 'operator'],
                            'freshness': 'live',
                            'example_questions': ['Who are the Intercom admins?'],
                            'search_strategy': 'Search by name or email',
                        },
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
                'x-airbyte-stream-name': 'admins',
                'x-airbyte-ai-hints': {
                    'summary': 'Intercom admin users (agents and operators)',
                    'when_to_use': 'Looking up support agent details',
                    'trigger_phrases': ['intercom admin', 'support agent', 'operator'],
                    'freshness': 'live',
                    'example_questions': ['Who are the Intercom admins?'],
                    'search_strategy': 'Search by name or email',
                },
            },
            ai_hints={
                'summary': 'Intercom admin users (agents and operators)',
                'when_to_use': 'Looking up support agent details',
                'trigger_phrases': ['intercom admin', 'support agent', 'operator'],
                'freshness': 'live',
                'example_questions': ['Who are the Intercom admins?'],
                'search_strategy': 'Search by name or email',
            },
        ),
        EntityDefinition(
            name='tags',
            stream_name='tags',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.DELETE,
            ],
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
                                    'x-airbyte-stream-name': 'tags',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Tags for categorizing contacts, companies, and conversations',
                                        'when_to_use': 'Questions about available tags or contact categorization',
                                        'trigger_phrases': ['intercom tag', 'contact tag'],
                                        'freshness': 'live',
                                        'example_questions': ['What tags exist in Intercom?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    no_pagination='The Intercom /tags endpoint returns the full set of workspace tags as a tag.list response in a single call; no pages/starting_after pagination is exposed.',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/tags',
                    action=Action.CREATE,
                    description='Create a new tag or update an existing one',
                    body_fields=['name'],
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the tag'},
                        },
                        'required': ['name'],
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
                        'x-airbyte-stream-name': 'tags',
                        'x-airbyte-ai-hints': {
                            'summary': 'Tags for categorizing contacts, companies, and conversations',
                            'when_to_use': 'Questions about available tags or contact categorization',
                            'trigger_phrases': ['intercom tag', 'contact tag'],
                            'freshness': 'live',
                            'example_questions': ['What tags exist in Intercom?'],
                            'search_strategy': 'Search by name',
                        },
                    },
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
                        'x-airbyte-stream-name': 'tags',
                        'x-airbyte-ai-hints': {
                            'summary': 'Tags for categorizing contacts, companies, and conversations',
                            'when_to_use': 'Questions about available tags or contact categorization',
                            'trigger_phrases': ['intercom tag', 'contact tag'],
                            'freshness': 'live',
                            'example_questions': ['What tags exist in Intercom?'],
                            'search_strategy': 'Search by name',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/tags/{id}',
                    action=Action.DELETE,
                    description='Permanently delete a tag by ID. This removes the tag from all contacts, companies, and conversations.',
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
                    response_schema={'type': 'object', 'description': 'Response from deleting a tag (Intercom returns an empty body)'},
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
                'x-airbyte-stream-name': 'tags',
                'x-airbyte-ai-hints': {
                    'summary': 'Tags for categorizing contacts, companies, and conversations',
                    'when_to_use': 'Questions about available tags or contact categorization',
                    'trigger_phrases': ['intercom tag', 'contact tag'],
                    'freshness': 'live',
                    'example_questions': ['What tags exist in Intercom?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Tags for categorizing contacts, companies, and conversations',
                'when_to_use': 'Questions about available tags or contact categorization',
                'trigger_phrases': ['intercom tag', 'contact tag'],
                'freshness': 'live',
                'example_questions': ['What tags exist in Intercom?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='notes',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/contacts/{contact_id}/notes',
                    action=Action.CREATE,
                    description='Create a note on an existing contact',
                    body_fields=['body', 'admin_id'],
                    path_params=['contact_id'],
                    path_params_schema={
                        'contact_id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': '2.11',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'body': {'type': 'string', 'description': 'The body of the note in HTML format'},
                            'admin_id': {'type': 'string', 'description': 'The ID of the admin creating the note'},
                        },
                        'required': ['body'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Note object on a contact',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Type of object (note)',
                            },
                            'id': {'type': 'string', 'description': 'Unique note identifier'},
                            'created_at': {
                                'type': ['integer', 'null'],
                                'description': 'Creation timestamp (Unix)',
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
                            'body': {
                                'type': ['string', 'null'],
                                'description': 'The body of the note',
                            },
                        },
                        'x-airbyte-entity-name': 'notes',
                        'x-airbyte-ai-hints': {
                            'summary': 'Internal notes on Intercom contacts',
                            'when_to_use': 'Looking for internal notes or context about a customer',
                            'trigger_phrases': ['intercom note', 'contact note', 'internal note'],
                            'freshness': 'live',
                            'example_questions': ['What notes are on a contact?'],
                            'search_strategy': 'Filter by contact',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Note object on a contact',
                'properties': {
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Type of object (note)',
                    },
                    'id': {'type': 'string', 'description': 'Unique note identifier'},
                    'created_at': {
                        'type': ['integer', 'null'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'contact': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ContactReference'},
                            {'type': 'null'},
                        ],
                    },
                    'author': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Author'},
                            {'type': 'null'},
                        ],
                    },
                    'body': {
                        'type': ['string', 'null'],
                        'description': 'The body of the note',
                    },
                },
                'x-airbyte-entity-name': 'notes',
                'x-airbyte-ai-hints': {
                    'summary': 'Internal notes on Intercom contacts',
                    'when_to_use': 'Looking for internal notes or context about a customer',
                    'trigger_phrases': ['intercom note', 'contact note', 'internal note'],
                    'freshness': 'live',
                    'example_questions': ['What notes are on a contact?'],
                    'search_strategy': 'Filter by contact',
                },
            },
            ai_hints={
                'summary': 'Internal notes on Intercom contacts',
                'when_to_use': 'Looking for internal notes or context about a customer',
                'trigger_phrases': ['intercom note', 'contact note', 'internal note'],
                'freshness': 'live',
                'example_questions': ['What notes are on a contact?'],
                'search_strategy': 'Filter by contact',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='notes',
                    target_entity='contacts',
                    foreign_key='contact_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='segments',
            stream_name='segments',
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
                                    'x-airbyte-stream-name': 'segments',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Dynamic segments of contacts based on filter criteria',
                                        'when_to_use': 'Questions about user segments or customer groups',
                                        'trigger_phrases': ['intercom segment', 'user segment', 'customer group'],
                                        'freshness': 'live',
                                        'example_questions': ['What segments are defined in Intercom?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.segments',
                    no_pagination='The Intercom /segments endpoint returns the full set of workspace segments as a segment.list response in a single call; no pages/starting_after pagination is exposed.',
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
                        'x-airbyte-stream-name': 'segments',
                        'x-airbyte-ai-hints': {
                            'summary': 'Dynamic segments of contacts based on filter criteria',
                            'when_to_use': 'Questions about user segments or customer groups',
                            'trigger_phrases': ['intercom segment', 'user segment', 'customer group'],
                            'freshness': 'live',
                            'example_questions': ['What segments are defined in Intercom?'],
                            'search_strategy': 'Search by name',
                        },
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
                'x-airbyte-stream-name': 'segments',
                'x-airbyte-ai-hints': {
                    'summary': 'Dynamic segments of contacts based on filter criteria',
                    'when_to_use': 'Questions about user segments or customer groups',
                    'trigger_phrases': ['intercom segment', 'user segment', 'customer group'],
                    'freshness': 'live',
                    'example_questions': ['What segments are defined in Intercom?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Dynamic segments of contacts based on filter criteria',
                'when_to_use': 'Questions about user segments or customer groups',
                'trigger_phrases': ['intercom segment', 'user segment', 'customer group'],
                'freshness': 'live',
                'example_questions': ['What segments are defined in Intercom?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='internal_articles',
            actions=[Action.CREATE, Action.UPDATE, Action.DELETE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/internal_articles',
                    action=Action.CREATE,
                    description='Create a new internal article in the workspace',
                    body_fields=[
                        'title',
                        'body',
                        'owner_id',
                        'author_id',
                    ],
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': 'Unstable',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the article'},
                            'body': {'type': 'string', 'description': 'The content of the article in HTML'},
                            'owner_id': {'type': 'integer', 'description': 'The ID of the owner of the article'},
                            'author_id': {'type': 'integer', 'description': 'The ID of the author of the article'},
                        },
                        'required': ['title', 'owner_id', 'author_id'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Internal article object',
                        'properties': {
                            'id': {
                                'type': ['integer', 'string'],
                                'description': 'The unique identifier for the article',
                            },
                            'title': {
                                'type': ['string', 'null'],
                                'description': 'The title of the article',
                            },
                            'body': {
                                'type': ['string', 'null'],
                                'description': 'The body of the article in HTML',
                            },
                            'owner_id': {
                                'type': ['integer', 'null'],
                                'description': 'The ID of the owner of the article',
                            },
                            'author_id': {
                                'type': ['integer', 'null'],
                                'description': 'The ID of the author of the article',
                            },
                            'created_at': {
                                'type': ['integer', 'null'],
                                'description': 'Creation timestamp (Unix)',
                            },
                            'updated_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last update timestamp (Unix)',
                            },
                            'locale': {
                                'type': ['string', 'null'],
                                'description': 'The default locale of the article',
                            },
                        },
                        'x-airbyte-entity-name': 'internal_articles',
                        'x-airbyte-ai-hints': {
                            'summary': 'Internal help center articles for the support team',
                            'when_to_use': 'Looking for internal knowledge base content',
                            'trigger_phrases': ['help article', 'knowledge base', 'internal article'],
                            'freshness': 'live',
                            'example_questions': ['Find an internal help article about a topic'],
                            'search_strategy': 'Search by title or content',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/internal_articles/{id}',
                    action=Action.UPDATE,
                    description='Update an existing internal article by ID',
                    body_fields=[
                        'title',
                        'body',
                        'author_id',
                        'owner_id',
                    ],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': 'Unstable',
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the article'},
                            'body': {'type': 'string', 'description': 'The content of the article in HTML'},
                            'author_id': {'type': 'integer', 'description': 'The ID of the author of the article'},
                            'owner_id': {'type': 'integer', 'description': 'The ID of the owner of the article'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Internal article object',
                        'properties': {
                            'id': {
                                'type': ['integer', 'string'],
                                'description': 'The unique identifier for the article',
                            },
                            'title': {
                                'type': ['string', 'null'],
                                'description': 'The title of the article',
                            },
                            'body': {
                                'type': ['string', 'null'],
                                'description': 'The body of the article in HTML',
                            },
                            'owner_id': {
                                'type': ['integer', 'null'],
                                'description': 'The ID of the owner of the article',
                            },
                            'author_id': {
                                'type': ['integer', 'null'],
                                'description': 'The ID of the author of the article',
                            },
                            'created_at': {
                                'type': ['integer', 'null'],
                                'description': 'Creation timestamp (Unix)',
                            },
                            'updated_at': {
                                'type': ['integer', 'null'],
                                'description': 'Last update timestamp (Unix)',
                            },
                            'locale': {
                                'type': ['string', 'null'],
                                'description': 'The default locale of the article',
                            },
                        },
                        'x-airbyte-entity-name': 'internal_articles',
                        'x-airbyte-ai-hints': {
                            'summary': 'Internal help center articles for the support team',
                            'when_to_use': 'Looking for internal knowledge base content',
                            'trigger_phrases': ['help article', 'knowledge base', 'internal article'],
                            'freshness': 'live',
                            'example_questions': ['Find an internal help article about a topic'],
                            'search_strategy': 'Search by title or content',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/internal_articles/{id}',
                    action=Action.DELETE,
                    description='Permanently delete an internal article by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['Intercom-Version'],
                    header_params_schema={
                        'Intercom-Version': {
                            'type': 'string',
                            'required': False,
                            'default': 'Unstable',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from deleting an internal article',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The ID of the deleted internal article'},
                            'object': {'type': 'string', 'description': 'Type of object (internal_article)'},
                            'deleted': {'type': 'boolean', 'description': 'Whether the internal article was successfully deleted'},
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Internal article object',
                'properties': {
                    'id': {
                        'type': ['integer', 'string'],
                        'description': 'The unique identifier for the article',
                    },
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'The title of the article',
                    },
                    'body': {
                        'type': ['string', 'null'],
                        'description': 'The body of the article in HTML',
                    },
                    'owner_id': {
                        'type': ['integer', 'null'],
                        'description': 'The ID of the owner of the article',
                    },
                    'author_id': {
                        'type': ['integer', 'null'],
                        'description': 'The ID of the author of the article',
                    },
                    'created_at': {
                        'type': ['integer', 'null'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated_at': {
                        'type': ['integer', 'null'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'locale': {
                        'type': ['string', 'null'],
                        'description': 'The default locale of the article',
                    },
                },
                'x-airbyte-entity-name': 'internal_articles',
                'x-airbyte-ai-hints': {
                    'summary': 'Internal help center articles for the support team',
                    'when_to_use': 'Looking for internal knowledge base content',
                    'trigger_phrases': ['help article', 'knowledge base', 'internal article'],
                    'freshness': 'live',
                    'example_questions': ['Find an internal help article about a topic'],
                    'search_strategy': 'Search by title or content',
                },
            },
            ai_hints={
                'summary': 'Internal help center articles for the support team',
                'when_to_use': 'Looking for internal knowledge base content',
                'trigger_phrases': ['help article', 'knowledge base', 'internal article'],
                'freshness': 'live',
                'example_questions': ['Find an internal help article about a topic'],
                'search_strategy': 'Search by title or content',
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='companies',
                suggested=True,
                x_airbyte_name='companies',
                fields=[
                    CacheFieldConfig(
                        name='app_id',
                        type=['null', 'string'],
                        description='The ID of the application associated with the company',
                    ),
                    CacheFieldConfig(
                        name='company_id',
                        type=['null', 'string'],
                        description='The unique identifier of the company',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'integer'],
                        description='The date and time when the company was created',
                    ),
                    CacheFieldConfig(
                        name='custom_attributes',
                        type=['null', 'object'],
                        description='Custom attributes specific to the company',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='The ID of the company',
                    ),
                    CacheFieldConfig(
                        name='industry',
                        type=['null', 'string'],
                        description='The industry in which the company operates',
                    ),
                    CacheFieldConfig(
                        name='monthly_spend',
                        type=['null', 'number'],
                        description='The monthly spend of the company',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='The name of the company',
                    ),
                    CacheFieldConfig(
                        name='plan',
                        type=['null', 'object'],
                        description="Details of the company's subscription plan",
                        properties={
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='remote_created_at',
                        type=['null', 'integer'],
                        description='The remote date and time when the company was created',
                    ),
                    CacheFieldConfig(
                        name='segments',
                        type=['null', 'object'],
                        description='Segments associated with the company',
                        properties={
                            'segments': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='session_count',
                        type=['null', 'integer'],
                        description='The number of sessions related to the company',
                    ),
                    CacheFieldConfig(
                        name='size',
                        type=['null', 'integer'],
                        description='The size of the company',
                    ),
                    CacheFieldConfig(
                        name='tags',
                        type=['null', 'object'],
                        description='Tags associated with the company',
                        properties={
                            'tags': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='The type of the company',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'integer'],
                        description='The date and time when the company was last updated',
                    ),
                    CacheFieldConfig(
                        name='user_count',
                        type=['null', 'integer'],
                        description='The number of users associated with the company',
                    ),
                    CacheFieldConfig(
                        name='website',
                        type=['null', 'string'],
                        description='The website of the company',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='contacts',
                suggested=True,
                x_airbyte_name='contacts',
                fields=[
                    CacheFieldConfig(
                        name='android_app_name',
                        type=['null', 'string'],
                        description='The name of the Android app associated with the contact.',
                    ),
                    CacheFieldConfig(
                        name='android_app_version',
                        type=['null', 'string'],
                        description='The version of the Android app associated with the contact.',
                    ),
                    CacheFieldConfig(
                        name='android_device',
                        type=['null', 'string'],
                        description='The device used by the contact for Android.',
                    ),
                    CacheFieldConfig(
                        name='android_last_seen_at',
                        type=['null', 'string'],
                        description='The date and time when the contact was last seen on Android.',
                    ),
                    CacheFieldConfig(
                        name='android_os_version',
                        type=['null', 'string'],
                        description='The operating system version of the Android device.',
                    ),
                    CacheFieldConfig(
                        name='android_sdk_version',
                        type=['null', 'string'],
                        description='The SDK version of the Android device.',
                    ),
                    CacheFieldConfig(
                        name='avatar',
                        type=['null', 'string'],
                        description="URL pointing to the contact's avatar image.",
                    ),
                    CacheFieldConfig(
                        name='browser',
                        type=['null', 'string'],
                        description='The browser used by the contact.',
                    ),
                    CacheFieldConfig(
                        name='browser_language',
                        type=['null', 'string'],
                        description="The language preference set in the contact's browser.",
                    ),
                    CacheFieldConfig(
                        name='browser_version',
                        type=['null', 'string'],
                        description='The version of the browser used by the contact.',
                    ),
                    CacheFieldConfig(
                        name='companies',
                        type=['null', 'object'],
                        description='Companies associated with the contact.',
                        properties={
                            'data': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'has_more': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'total_count': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'url': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'integer'],
                        description='The date and time when the contact was created.',
                    ),
                    CacheFieldConfig(
                        name='custom_attributes',
                        type=['null', 'object'],
                        description='Custom attributes defined for the contact.',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='The email address of the contact.',
                    ),
                    CacheFieldConfig(
                        name='external_id',
                        type=['null', 'string'],
                        description='External identifier for the contact.',
                    ),
                    CacheFieldConfig(
                        name='has_hard_bounced',
                        type=['null', 'boolean'],
                        description='Flag indicating if the contact has hard bounced.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='The unique identifier of the contact.',
                    ),
                    CacheFieldConfig(
                        name='ios_app_name',
                        type=['null', 'string'],
                        description='The name of the iOS app associated with the contact.',
                    ),
                    CacheFieldConfig(
                        name='ios_app_version',
                        type=['null', 'string'],
                        description='The version of the iOS app associated with the contact.',
                    ),
                    CacheFieldConfig(
                        name='ios_device',
                        type=['null', 'string'],
                        description='The device used by the contact for iOS.',
                    ),
                    CacheFieldConfig(
                        name='ios_last_seen_at',
                        type=['null', 'integer'],
                        description='The date and time when the contact was last seen on iOS.',
                    ),
                    CacheFieldConfig(
                        name='ios_os_version',
                        type=['null', 'string'],
                        description='The operating system version of the iOS device.',
                    ),
                    CacheFieldConfig(
                        name='ios_sdk_version',
                        type=['null', 'string'],
                        description='The SDK version of the iOS device.',
                    ),
                    CacheFieldConfig(
                        name='language_override',
                        type=['null', 'string'],
                        description='Language override set for the contact.',
                    ),
                    CacheFieldConfig(
                        name='last_contacted_at',
                        type=['null', 'integer'],
                        description='The date and time when the contact was last contacted.',
                    ),
                    CacheFieldConfig(
                        name='last_email_clicked_at',
                        type=['null', 'integer'],
                        description='The date and time when the contact last clicked an email.',
                    ),
                    CacheFieldConfig(
                        name='last_email_opened_at',
                        type=['null', 'integer'],
                        description='The date and time when the contact last opened an email.',
                    ),
                    CacheFieldConfig(
                        name='last_replied_at',
                        type=['null', 'integer'],
                        description='The date and time when the contact last replied.',
                    ),
                    CacheFieldConfig(
                        name='last_seen_at',
                        type=['null', 'integer'],
                        description='The date and time when the contact was last seen overall.',
                    ),
                    CacheFieldConfig(
                        name='location',
                        type=['null', 'object'],
                        description='Location details of the contact.',
                        properties={
                            'city': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'continent_code': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'country': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'country_code': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'region': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='marked_email_as_spam',
                        type=['null', 'boolean'],
                        description="Flag indicating if the contact's email was marked as spam.",
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='The name of the contact.',
                    ),
                    CacheFieldConfig(
                        name='notes',
                        type=['null', 'object'],
                        description='Notes associated with the contact.',
                        properties={
                            'data': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'has_more': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'total_count': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'url': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='opted_in_subscription_types',
                        type=['null', 'object'],
                        description='Subscription types the contact opted into.',
                        properties={
                            'data': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'has_more': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'total_count': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'url': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='opted_out_subscription_types',
                        type=['null', 'object'],
                        description='Subscription types the contact opted out from.',
                        properties={
                            'data': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'has_more': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'total_count': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'url': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='os',
                        type=['null', 'string'],
                        description="Operating system of the contact's device.",
                    ),
                    CacheFieldConfig(
                        name='owner_id',
                        type=['null', 'integer'],
                        description="The unique identifier of the contact's owner.",
                    ),
                    CacheFieldConfig(
                        name='phone',
                        type=['null', 'string'],
                        description='The phone number of the contact.',
                    ),
                    CacheFieldConfig(
                        name='referrer',
                        type=['null', 'string'],
                        description='Referrer information related to the contact.',
                    ),
                    CacheFieldConfig(
                        name='role',
                        type=['null', 'string'],
                        description='Role or position of the contact.',
                    ),
                    CacheFieldConfig(
                        name='signed_up_at',
                        type=['null', 'integer'],
                        description='The date and time when the contact signed up.',
                    ),
                    CacheFieldConfig(
                        name='sms_consent',
                        type=['null', 'boolean'],
                        description='Consent status for SMS communication.',
                    ),
                    CacheFieldConfig(
                        name='social_profiles',
                        type=['null', 'object'],
                        description='Social profiles associated with the contact.',
                        properties={
                            'data': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='tags',
                        type=['null', 'object'],
                        description='Tags associated with the contact.',
                        properties={
                            'data': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'has_more': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'total_count': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'url': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Type of contact.',
                    ),
                    CacheFieldConfig(
                        name='unsubscribed_from_emails',
                        type=['null', 'boolean'],
                        description='Flag indicating if the contact unsubscribed from emails.',
                    ),
                    CacheFieldConfig(
                        name='unsubscribed_from_sms',
                        type=['null', 'boolean'],
                        description='Flag indicating if the contact unsubscribed from SMS.',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'integer'],
                        description='The date and time when the contact was last updated.',
                    ),
                    CacheFieldConfig(
                        name='utm_campaign',
                        type=['null', 'string'],
                        description='Campaign data from UTM parameters.',
                    ),
                    CacheFieldConfig(
                        name='utm_content',
                        type=['null', 'string'],
                        description='Content data from UTM parameters.',
                    ),
                    CacheFieldConfig(
                        name='utm_medium',
                        type=['null', 'string'],
                        description='Medium data from UTM parameters.',
                    ),
                    CacheFieldConfig(
                        name='utm_source',
                        type=['null', 'string'],
                        description='Source data from UTM parameters.',
                    ),
                    CacheFieldConfig(
                        name='utm_term',
                        type=['null', 'string'],
                        description='Term data from UTM parameters.',
                    ),
                    CacheFieldConfig(
                        name='workspace_id',
                        type=['null', 'string'],
                        description='The unique identifier of the workspace associated with the contact.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='conversation_parts',
                x_airbyte_name='conversation_parts',
                fields=[
                    CacheFieldConfig(
                        name='assigned_to',
                        type=['object', 'string', 'null'],
                        description='The user or team member who is assigned to handle this conversation part.',
                    ),
                    CacheFieldConfig(
                        name='attachments',
                        type=['null', 'array'],
                        description='Represents the attachments associated with the conversation part.',
                    ),
                    CacheFieldConfig(
                        name='author',
                        type=['null', 'object'],
                        description='Represents the author of the conversation part.',
                        properties={
                            'email': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='body',
                        type=['null', 'string'],
                        description='The main content or message body of the conversation part.',
                    ),
                    CacheFieldConfig(
                        name='conversation_created_at',
                        type=['null', 'integer'],
                        description='The date and time when the conversation was created.',
                    ),
                    CacheFieldConfig(
                        name='conversation_id',
                        type=['null', 'integer'],
                        description='The unique identifier of the conversation.',
                    ),
                    CacheFieldConfig(
                        name='conversation_total_parts',
                        type=['null', 'integer'],
                        description='The total number of parts in the conversation.',
                    ),
                    CacheFieldConfig(
                        name='conversation_updated_at',
                        type=['null', 'integer'],
                        description='The date and time when the conversation was last updated.',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'integer'],
                        description='The date and time when the conversation part was created.',
                    ),
                    CacheFieldConfig(
                        name='external_id',
                        type=['null', 'string'],
                        description='An external identifier associated with the conversation part.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='The unique identifier of the conversation part.',
                    ),
                    CacheFieldConfig(
                        name='notified_at',
                        type=['null', 'integer'],
                        description='The date and time when the conversation part was last notified.',
                    ),
                    CacheFieldConfig(
                        name='part_type',
                        type=['null', 'string'],
                        description='The type or category of the conversation part.',
                    ),
                    CacheFieldConfig(
                        name='redacted',
                        type=['null', 'boolean'],
                        description='Indicates if the conversation part has been redacted or censored.',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='The type of conversation part, such as message or note.',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'integer'],
                        description='The date and time when the conversation part was last updated.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='conversations',
                suggested=True,
                x_airbyte_name='conversations',
                fields=[
                    CacheFieldConfig(
                        name='admin_assignee_id',
                        type=['null', 'integer'],
                        description='The ID of the administrator assigned to the conversation',
                    ),
                    CacheFieldConfig(
                        name='ai_agent',
                        type=['null', 'object'],
                        description='Data related to AI Agent involvement in the conversation',
                        properties={
                            'content_sources': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                            'last_answer_type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'rating': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'rating_remark': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'resolution_state': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'source_id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'source_title': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'source_type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'triggered_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='ai_agent_participated',
                        type=['null', 'boolean'],
                        description='Indicates whether AI Agent participated in the conversation',
                    ),
                    CacheFieldConfig(
                        name='assignee',
                        type=['null', 'object'],
                        description='The assigned user responsible for the conversation.',
                        properties={
                            'email': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='contacts',
                        type=['null', 'object'],
                        description='List of contacts involved in the conversation.',
                    ),
                    CacheFieldConfig(
                        name='conversation_message',
                        type=['null', 'object'],
                        description='The main message content of the conversation.',
                        properties={
                            'attachments': CacheFieldProperty(
                                type=['array', 'null'],
                            ),
                            'author': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                            'body': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'delivered_as': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'subject': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'url': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='conversation_rating',
                        type=['null', 'object'],
                        description='Ratings given to the conversation by the customer and teammate.',
                        properties={
                            'created_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'customer': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                            'rating': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'remark': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'teammate': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'integer'],
                        description='The timestamp when the conversation was created',
                    ),
                    CacheFieldConfig(
                        name='custom_attributes',
                        type=['null', 'object'],
                        description='Custom attributes associated with the conversation',
                    ),
                    CacheFieldConfig(
                        name='customer_first_reply',
                        type=['null', 'object'],
                        description='Timestamp indicating when the customer first replied.',
                        properties={
                            'created_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'url': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='customers',
                        type=['array', 'null'],
                        description='List of customers involved in the conversation',
                    ),
                    CacheFieldConfig(
                        name='first_contact_reply',
                        type=['null', 'object'],
                        description='Timestamp indicating when the first contact replied.',
                        properties={
                            'created_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'url': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='The unique ID of the conversation',
                    ),
                    CacheFieldConfig(
                        name='linked_objects',
                        type=['null', 'object'],
                        description='Linked objects associated with the conversation',
                        properties={
                            'data': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'has_more': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'total_count': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'url': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='open',
                        type=['null', 'boolean'],
                        description='Indicates if the conversation is open or closed',
                    ),
                    CacheFieldConfig(
                        name='priority',
                        type=['null', 'string'],
                        description='The priority level of the conversation',
                    ),
                    CacheFieldConfig(
                        name='read',
                        type=['null', 'boolean'],
                        description='Indicates if the conversation has been read',
                    ),
                    CacheFieldConfig(
                        name='redacted',
                        type=['null', 'boolean'],
                        description='Indicates if the conversation is redacted',
                    ),
                    CacheFieldConfig(
                        name='sent_at',
                        type=['null', 'integer'],
                        description='The timestamp when the conversation was sent',
                    ),
                    CacheFieldConfig(
                        name='sla_applied',
                        type=['null', 'object'],
                        description='Service Level Agreement details applied to the conversation.',
                        properties={
                            'sla_name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'sla_status': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='snoozed_until',
                        type=['null', 'integer'],
                        description='Timestamp until the conversation is snoozed',
                    ),
                    CacheFieldConfig(
                        name='source',
                        type=['null', 'object'],
                        description='Source details of the conversation.',
                        properties={
                            'attachments': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'author': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                            'body': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'delivered_as': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'redacted': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'subject': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'url': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='state',
                        type=['null', 'string'],
                        description='The state of the conversation (e.g., new, in progress)',
                    ),
                    CacheFieldConfig(
                        name='statistics',
                        type=['null', 'object'],
                        description='Statistics related to the conversation.',
                        properties={
                            'count_assignments': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'count_conversation_parts': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'count_reopens': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'first_admin_reply_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'first_assignment_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'first_close_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'first_contact_reply_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'last_admin_reply_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'last_assignment_admin_reply_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'last_assignment_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'last_close_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'last_closed_by_id': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'last_contact_reply_at': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'median_time_to_reply': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'time_to_admin_reply': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'time_to_assignment': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'time_to_first_close': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'time_to_last_close': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='tags',
                        type=['null', 'object'],
                        description='Tags applied to the conversation.',
                    ),
                    CacheFieldConfig(
                        name='team_assignee_id',
                        type=['null', 'integer'],
                        description='The ID of the team assigned to the conversation',
                    ),
                    CacheFieldConfig(
                        name='teammates',
                        type=['null', 'object'],
                        description='List of teammates involved in the conversation.',
                        properties={
                            'admins': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='The title of the conversation',
                    ),
                    CacheFieldConfig(
                        name='topics',
                        type=['null', 'object'],
                        description='Topics associated with the conversation.',
                        properties={
                            'topics': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'total_count': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='The type of the conversation',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'integer'],
                        description='The timestamp when the conversation was last updated',
                    ),
                    CacheFieldConfig(
                        name='user',
                        type=['null', 'object'],
                        description='The user related to the conversation.',
                        properties={
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='waiting_since',
                        type=['null', 'integer'],
                        description='Timestamp since waiting for a response',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='teams',
                suggested=True,
                x_airbyte_name='teams',
                fields=[
                    CacheFieldConfig(
                        name='admin_ids',
                        type=['array', 'null'],
                        description='Array of user IDs representing the admins of the team.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the team.',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the team.',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description="Type of team (e.g., 'internal', 'external').",
                    ),
                ],
            ),
        ],
        disable_compaction=True,
    ),
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
    example_questions=ExampleQuestions(
        direct=[
            'List all contacts in my Intercom workspace',
            'List all companies in Intercom',
            'What teams are configured in my workspace?',
            'Show me all admins in my Intercom account',
            'List all tags used in Intercom',
            'Show me all customer segments',
            'Show me details for a recent contact',
            'Show me details for a recent company',
            'Show me details for a recent conversation',
            "Create a new lead contact named 'Jane Smith' with email jane@example.com",
            "Create an internal article titled 'Onboarding Guide' with instructions for new team members",
            "Create a company named 'Acme Corp' with company_id 'acme-001'",
            "Create a tag named 'VIP Customer'",
        ],
        context_store_search=[
            "Create a conversation from contact {id} saying 'I need help with my account'",
            "Update the name of contact {id} to 'John Updated'",
            "Add a note to contact {id} saying 'Followed up on support request'",
            'Show me conversations from the last week',
            'List conversations assigned to team {team_id}',
            'Show me open conversations',
            'Delete contact {id}',
            'Delete company {id}',
            'Delete tag {id}',
            'Delete conversation {id}',
            'Delete internal article {id}',
            'Update conversation {id} to mark it as read',
            'Update internal article {id} with a new title',
        ],
        search=[
            "Create a conversation from contact {id} saying 'I need help with my account'",
            "Update the name of contact {id} to 'John Updated'",
            "Add a note to contact {id} saying 'Followed up on support request'",
            'Show me conversations from the last week',
            'List conversations assigned to team {team_id}',
            'Show me open conversations',
            'Delete contact {id}',
            'Delete company {id}',
            'Delete tag {id}',
            'Delete conversation {id}',
            'Delete internal article {id}',
            'Update conversation {id} to mark it as read',
            'Update internal article {id} with a new title',
        ],
        unsupported=['Send a message to a customer', 'Assign a conversation to an admin'],
    ),
)