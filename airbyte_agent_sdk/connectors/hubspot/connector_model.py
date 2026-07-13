"""
Connector model for hubspot.

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
from uuid import (
    UUID,
)

HubspotConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('36c891d9-4bd9-43ac-bad2-10e12756272c'),
    name='hubspot',
    version='0.1.20',
    base_url='https://api.hubapi.com',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='oauth2',
                type=AuthType.OAUTH2,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'refresh_url': 'https://api.hubapi.com/oauth/v1/token',
                    'auth_style': 'body',
                    'body_format': 'form',
                },
                user_config_spec=AuthConfigSpec(
                    title='OAuth2',
                    type='object',
                    required=['refresh_token'],
                    properties={
                        'client_id': AuthConfigFieldSpec(
                            title='Client ID',
                            description='Your HubSpot OAuth2 Client ID',
                        ),
                        'client_secret': AuthConfigFieldSpec(
                            title='Client Secret',
                            description='Your HubSpot OAuth2 Client Secret',
                        ),
                        'refresh_token': AuthConfigFieldSpec(
                            title='Refresh Token',
                            description='Your HubSpot OAuth2 Refresh Token',
                        ),
                        'access_token': AuthConfigFieldSpec(
                            title='Access Token',
                            description='Your HubSpot OAuth2 Access Token (optional if refresh_token is provided)',
                        ),
                    },
                    auth_mapping={
                        'client_id': '${client_id}',
                        'client_secret': '${client_secret}',
                        'refresh_token': '${refresh_token}',
                        'access_token': '${access_token}',
                    },
                    replication_auth_key_mapping={
                        'credentials.client_id': 'client_id',
                        'credentials.client_secret': 'client_secret',
                        'credentials.refresh_token': 'refresh_token',
                    },
                    replication_auth_key_constants={'credentials.credentials_title': 'OAuth Credentials'},
                ),
            ),
            AuthOption(
                scheme_name='hubspotPrivateApp',
                type=AuthType.BEARER,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AuthConfigSpec(
                    title='Private App',
                    type='object',
                    required=['private_app_token'],
                    properties={
                        'private_app_token': AuthConfigFieldSpec(
                            title='Private App Token',
                            description='Access token from a HubSpot Private App',
                        ),
                    },
                    auth_mapping={'token': '${private_app_token}'},
                    replication_auth_key_mapping={'credentials.access_token': 'private_app_token'},
                    replication_auth_key_constants={'credentials.credentials_title': 'Private App Credentials'},
                ),
            ),
        ],
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
                Action.API_SEARCH,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/contacts',
                    action=Action.LIST,
                    description='Returns a paginated list of contacts',
                    query_params=[
                        'limit',
                        'after',
                        'associations',
                        'properties',
                        'propertiesWithHistory',
                        'archived',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of contacts',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot contact object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique contact identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Contact properties',
                                            'properties': {
                                                'createdate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'email': {
                                                    'type': ['string', 'null'],
                                                },
                                                'firstname': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'lastname': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the contact is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the contact was archived',
                                        },
                                        'propertiesWithHistory': {
                                            'type': ['object', 'null'],
                                            'description': 'Properties with historical values',
                                            'additionalProperties': True,
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                        'objectWriteTraceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Trace identifier for write operations',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL to view contact in HubSpot',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'contacts',
                                    'x-airbyte-stream-name': 'contacts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'HubSpot contacts with email, name, and engagement history',
                                        'when_to_use': 'Looking up contact information, leads, or people in the CRM',
                                        'trigger_phrases': [
                                            'hubspot contact',
                                            'lead',
                                            'customer contact',
                                            'who is',
                                            'contact info',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Find a contact in HubSpot', 'Show contact details for an email'],
                                        'search_strategy': 'Search by email or name across properties for best results',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                    preferred_for_check=True,
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/contacts',
                    action=Action.CREATE,
                    description='Create a new contact in HubSpot CRM with the provided properties.',
                    body_fields=['properties'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new contact',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Contact properties to set',
                                'required': ['email'],
                                'properties': {
                                    'email': {'type': 'string', 'description': 'Contact email address (required, used as unique identifier)'},
                                    'firstname': {'type': 'string', 'description': 'Contact first name'},
                                    'lastname': {'type': 'string', 'description': 'Contact last name'},
                                    'phone': {'type': 'string', 'description': 'Contact phone number'},
                                    'company': {'type': 'string', 'description': 'Company name associated with the contact'},
                                    'website': {'type': 'string', 'description': 'Contact website URL'},
                                    'lifecyclestage': {'type': 'string', 'description': 'Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)'},
                                    'jobtitle': {'type': 'string', 'description': 'Contact job title'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this contact'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot contact object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique contact identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Contact properties',
                                'properties': {
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                    },
                                    'firstname': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'lastname': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the contact is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the contact was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view contact in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'contacts',
                        'x-airbyte-stream-name': 'contacts',
                        'x-airbyte-ai-hints': {
                            'summary': 'HubSpot contacts with email, name, and engagement history',
                            'when_to_use': 'Looking up contact information, leads, or people in the CRM',
                            'trigger_phrases': [
                                'hubspot contact',
                                'lead',
                                'customer contact',
                                'who is',
                                'contact info',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find a contact in HubSpot', 'Show contact details for an email'],
                            'search_strategy': 'Search by email or name across properties for best results',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/contacts/{contactId}',
                    action=Action.GET,
                    description='Get a single contact by ID',
                    query_params=[
                        'properties',
                        'propertiesWithHistory',
                        'associations',
                        'idProperty',
                        'archived',
                    ],
                    query_params_schema={
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'idProperty': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['contactId'],
                    path_params_schema={
                        'contactId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot contact object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique contact identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Contact properties',
                                'properties': {
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                    },
                                    'firstname': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'lastname': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the contact is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the contact was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view contact in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'contacts',
                        'x-airbyte-stream-name': 'contacts',
                        'x-airbyte-ai-hints': {
                            'summary': 'HubSpot contacts with email, name, and engagement history',
                            'when_to_use': 'Looking up contact information, leads, or people in the CRM',
                            'trigger_phrases': [
                                'hubspot contact',
                                'lead',
                                'customer contact',
                                'who is',
                                'contact info',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find a contact in HubSpot', 'Show contact details for an email'],
                            'search_strategy': 'Search by email or name across properties for best results',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/crm/v3/objects/contacts/{contactId}',
                    action=Action.UPDATE,
                    description="Update an existing contact's properties by ID. Only the specified properties will be updated.",
                    body_fields=['properties'],
                    path_params=['contactId'],
                    path_params_schema={
                        'contactId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing contact. Only provided properties will be updated.',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Contact properties to update',
                                'properties': {
                                    'email': {'type': 'string', 'description': 'Contact email address'},
                                    'firstname': {'type': 'string', 'description': 'Contact first name'},
                                    'lastname': {'type': 'string', 'description': 'Contact last name'},
                                    'phone': {'type': 'string', 'description': 'Contact phone number'},
                                    'company': {'type': 'string', 'description': 'Company name associated with the contact'},
                                    'website': {'type': 'string', 'description': 'Contact website URL'},
                                    'lifecyclestage': {'type': 'string', 'description': 'Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)'},
                                    'jobtitle': {'type': 'string', 'description': 'Contact job title'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this contact'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot contact object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique contact identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Contact properties',
                                'properties': {
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                    },
                                    'firstname': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'lastname': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the contact is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the contact was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view contact in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'contacts',
                        'x-airbyte-stream-name': 'contacts',
                        'x-airbyte-ai-hints': {
                            'summary': 'HubSpot contacts with email, name, and engagement history',
                            'when_to_use': 'Looking up contact information, leads, or people in the CRM',
                            'trigger_phrases': [
                                'hubspot contact',
                                'lead',
                                'customer contact',
                                'who is',
                                'contact info',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find a contact in HubSpot', 'Show contact details for an email'],
                            'search_strategy': 'Search by email or name across properties for best results',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/contacts/search',
                    action=Action.API_SEARCH,
                    description='Search for contacts by filtering on properties, searching through associations, and sorting results.',
                    body_fields=[
                        'filterGroups',
                        'properties',
                        'limit',
                        'after',
                        'sorts',
                        'query',
                    ],
                    request_body_defaults={'limit': 25},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filterGroups': {
                                'type': 'array',
                                'description': 'Up to 6 groups of filters defining additional query criteria.',
                                'required': True,
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'filters': {
                                            'type': 'array',
                                            'required': True,
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'operator': {
                                                        'type': 'string',
                                                        'enum': [
                                                            'BETWEEN',
                                                            'CONTAINS_TOKEN',
                                                            'EQ',
                                                            'GT',
                                                            'GTE',
                                                            'HAS_PROPERTY',
                                                            'IN',
                                                            'LT',
                                                            'LTE',
                                                            'NEQ',
                                                            'NOT_CONTAINS_TOKEN',
                                                            'NOT_HAS_PROPERTY',
                                                            'NOT_IN',
                                                        ],
                                                        'required': True,
                                                    },
                                                    'propertyName': {
                                                        'type': 'string',
                                                        'description': 'The name of the property to apply the filter on.',
                                                        'required': True,
                                                    },
                                                    'value': {'type': 'string', 'description': 'The value to match against the property.'},
                                                    'values': {
                                                        'type': 'array',
                                                        'description': 'The values to match against the property.',
                                                        'items': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'properties': {
                                'type': 'array',
                                'description': 'A list of property names to include in the response.',
                                'required': True,
                                'items': {'type': 'string'},
                            },
                            'limit': {
                                'type': 'integer',
                                'description': 'Maximum number of results to return',
                                'required': True,
                                'minimum': 1,
                                'maximum': 200,
                                'default': 25,
                            },
                            'after': {'type': 'string', 'description': 'A paging cursor token for retrieving subsequent pages.'},
                            'sorts': {
                                'type': 'array',
                                'description': 'Sort criteria',
                                'required': True,
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'propertyName': {'type': 'string'},
                                        'direction': {
                                            'type': 'string',
                                            'enum': ['ASCENDING', 'DESCENDING'],
                                        },
                                    },
                                },
                            },
                            'query': {'type': 'string', 'description': 'The search query string, up to 3000 characters.'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of contacts',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot contact object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique contact identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Contact properties',
                                            'properties': {
                                                'createdate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'email': {
                                                    'type': ['string', 'null'],
                                                },
                                                'firstname': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'lastname': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the contact is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the contact was archived',
                                        },
                                        'propertiesWithHistory': {
                                            'type': ['object', 'null'],
                                            'description': 'Properties with historical values',
                                            'additionalProperties': True,
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                        'objectWriteTraceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Trace identifier for write operations',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL to view contact in HubSpot',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'contacts',
                                    'x-airbyte-stream-name': 'contacts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'HubSpot contacts with email, name, and engagement history',
                                        'when_to_use': 'Looking up contact information, leads, or people in the CRM',
                                        'trigger_phrases': [
                                            'hubspot contact',
                                            'lead',
                                            'customer contact',
                                            'who is',
                                            'contact info',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Find a contact in HubSpot', 'Show contact details for an email'],
                                        'search_strategy': 'Search by email or name across properties for best results',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={
                        'total': '$.total',
                        'next_cursor': '$.paging.next.after',
                        'next_link': '$.paging.next.link',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'HubSpot contact object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique contact identifier'},
                    'properties': {
                        'type': 'object',
                        'description': 'Contact properties',
                        'properties': {
                            'createdate': {
                                'type': ['string', 'null'],
                            },
                            'email': {
                                'type': ['string', 'null'],
                            },
                            'firstname': {
                                'type': ['string', 'null'],
                            },
                            'hs_object_id': {
                                'type': ['string', 'null'],
                            },
                            'lastmodifieddate': {
                                'type': ['string', 'null'],
                            },
                            'lastname': {
                                'type': ['string', 'null'],
                            },
                        },
                        'additionalProperties': True,
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the contact is archived'},
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the contact was archived',
                    },
                    'propertiesWithHistory': {
                        'type': ['object', 'null'],
                        'description': 'Properties with historical values',
                        'additionalProperties': True,
                    },
                    'associations': {
                        'type': ['object', 'null'],
                        'description': 'Relationships with other CRM objects',
                        'additionalProperties': True,
                    },
                    'objectWriteTraceId': {
                        'type': ['string', 'null'],
                        'description': 'Trace identifier for write operations',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'URL to view contact in HubSpot',
                    },
                },
                'x-airbyte-entity-name': 'contacts',
                'x-airbyte-stream-name': 'contacts',
                'x-airbyte-ai-hints': {
                    'summary': 'HubSpot contacts with email, name, and engagement history',
                    'when_to_use': 'Looking up contact information, leads, or people in the CRM',
                    'trigger_phrases': [
                        'hubspot contact',
                        'lead',
                        'customer contact',
                        'who is',
                        'contact info',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Find a contact in HubSpot', 'Show contact details for an email'],
                    'search_strategy': 'Search by email or name across properties for best results',
                },
            },
            ai_hints={
                'summary': 'HubSpot contacts with email, name, and engagement history',
                'when_to_use': 'Looking up contact information, leads, or people in the CRM',
                'trigger_phrases': [
                    'hubspot contact',
                    'lead',
                    'customer contact',
                    'who is',
                    'contact info',
                ],
                'freshness': 'live',
                'example_questions': ['Find a contact in HubSpot', 'Show contact details for an email'],
                'search_strategy': 'Search by email or name across properties for best results',
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
                Action.API_SEARCH,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/companies',
                    action=Action.LIST,
                    description='Retrieve all companies, using query parameters to control the information that gets returned.',
                    query_params=[
                        'limit',
                        'after',
                        'associations',
                        'properties',
                        'propertiesWithHistory',
                        'archived',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of companies',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot company object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique company identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Company properties',
                                            'properties': {
                                                'createdate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'domain': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'name': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the company is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the company was archived',
                                        },
                                        'propertiesWithHistory': {
                                            'type': ['object', 'null'],
                                            'description': 'Properties with historical values',
                                            'additionalProperties': True,
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                        'objectWriteTraceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Trace identifier for write operations',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL to view company in HubSpot',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'companies',
                                    'x-airbyte-stream-name': 'companies',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Companies in HubSpot CRM with industry, size, and revenue data',
                                        'when_to_use': 'Looking up company information or account details',
                                        'trigger_phrases': [
                                            'hubspot company',
                                            'account',
                                            'company details',
                                            'which company',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Find a company in HubSpot', 'Show company details'],
                                        'search_strategy': 'Search by name or domain',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/companies',
                    action=Action.CREATE,
                    description='Create a new company in HubSpot CRM with the provided properties.',
                    body_fields=['properties'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new company',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Company properties to set',
                                'required': ['name'],
                                'properties': {
                                    'name': {'type': 'string', 'description': 'Company name (required)'},
                                    'domain': {'type': 'string', 'description': 'Company domain name (e.g., example.com)'},
                                    'description': {'type': 'string', 'description': 'Company description'},
                                    'phone': {'type': 'string', 'description': 'Company phone number'},
                                    'industry': {'type': 'string', 'description': 'Company industry (e.g., COMPUTER_SOFTWARE, INFORMATION_TECHNOLOGY_AND_SERVICES, INTERNET, FINANCIAL_SERVICES, MARKETING_AND_ADVERTISING, EDUCATION_MANAGEMENT)'},
                                    'city': {'type': 'string', 'description': 'Company city'},
                                    'state': {'type': 'string', 'description': 'Company state/region'},
                                    'country': {'type': 'string', 'description': 'Company country'},
                                    'zip': {'type': 'string', 'description': 'Company postal/zip code'},
                                    'numberofemployees': {'type': 'string', 'description': 'Number of employees'},
                                    'annualrevenue': {'type': 'string', 'description': 'Annual revenue'},
                                    'lifecyclestage': {'type': 'string', 'description': 'Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this company'},
                                    'website': {'type': 'string', 'description': 'Company website URL'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot company object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique company identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Company properties',
                                'properties': {
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'domain': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the company is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the company was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view company in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'companies',
                        'x-airbyte-stream-name': 'companies',
                        'x-airbyte-ai-hints': {
                            'summary': 'Companies in HubSpot CRM with industry, size, and revenue data',
                            'when_to_use': 'Looking up company information or account details',
                            'trigger_phrases': [
                                'hubspot company',
                                'account',
                                'company details',
                                'which company',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find a company in HubSpot', 'Show company details'],
                            'search_strategy': 'Search by name or domain',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/companies/{companyId}',
                    action=Action.GET,
                    description='Get a single company by ID',
                    query_params=[
                        'properties',
                        'propertiesWithHistory',
                        'associations',
                        'idProperty',
                        'archived',
                    ],
                    query_params_schema={
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'idProperty': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['companyId'],
                    path_params_schema={
                        'companyId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot company object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique company identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Company properties',
                                'properties': {
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'domain': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the company is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the company was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view company in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'companies',
                        'x-airbyte-stream-name': 'companies',
                        'x-airbyte-ai-hints': {
                            'summary': 'Companies in HubSpot CRM with industry, size, and revenue data',
                            'when_to_use': 'Looking up company information or account details',
                            'trigger_phrases': [
                                'hubspot company',
                                'account',
                                'company details',
                                'which company',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find a company in HubSpot', 'Show company details'],
                            'search_strategy': 'Search by name or domain',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/crm/v3/objects/companies/{companyId}',
                    action=Action.UPDATE,
                    description="Update an existing company's properties by ID. Only the specified properties will be updated.",
                    body_fields=['properties'],
                    path_params=['companyId'],
                    path_params_schema={
                        'companyId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing company. Only provided properties will be updated.',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Company properties to update',
                                'properties': {
                                    'name': {'type': 'string', 'description': 'Company name'},
                                    'domain': {'type': 'string', 'description': 'Company domain name (e.g., example.com)'},
                                    'description': {'type': 'string', 'description': 'Company description'},
                                    'phone': {'type': 'string', 'description': 'Company phone number'},
                                    'industry': {'type': 'string', 'description': 'Company industry (e.g., COMPUTER_SOFTWARE, INFORMATION_TECHNOLOGY_AND_SERVICES, INTERNET, FINANCIAL_SERVICES, MARKETING_AND_ADVERTISING, EDUCATION_MANAGEMENT)'},
                                    'city': {'type': 'string', 'description': 'Company city'},
                                    'state': {'type': 'string', 'description': 'Company state/region'},
                                    'country': {'type': 'string', 'description': 'Company country'},
                                    'zip': {'type': 'string', 'description': 'Company postal/zip code'},
                                    'numberofemployees': {'type': 'string', 'description': 'Number of employees'},
                                    'annualrevenue': {'type': 'string', 'description': 'Annual revenue'},
                                    'lifecyclestage': {'type': 'string', 'description': 'Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this company'},
                                    'website': {'type': 'string', 'description': 'Company website URL'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot company object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique company identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Company properties',
                                'properties': {
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'domain': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the company is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the company was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view company in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'companies',
                        'x-airbyte-stream-name': 'companies',
                        'x-airbyte-ai-hints': {
                            'summary': 'Companies in HubSpot CRM with industry, size, and revenue data',
                            'when_to_use': 'Looking up company information or account details',
                            'trigger_phrases': [
                                'hubspot company',
                                'account',
                                'company details',
                                'which company',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find a company in HubSpot', 'Show company details'],
                            'search_strategy': 'Search by name or domain',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/companies/search',
                    action=Action.API_SEARCH,
                    description='Search for companies by filtering on properties, searching through associations, and sorting results.',
                    body_fields=[
                        'filterGroups',
                        'properties',
                        'limit',
                        'after',
                        'sorts',
                        'query',
                    ],
                    request_body_defaults={'limit': 25},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filterGroups': {
                                'type': 'array',
                                'description': 'Up to 6 groups of filters defining additional query criteria.',
                                'required': True,
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'filters': {
                                            'type': 'array',
                                            'required': True,
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'operator': {
                                                        'type': 'string',
                                                        'enum': [
                                                            'BETWEEN',
                                                            'CONTAINS_TOKEN',
                                                            'EQ',
                                                            'GT',
                                                            'GTE',
                                                            'HAS_PROPERTY',
                                                            'IN',
                                                            'LT',
                                                            'LTE',
                                                            'NEQ',
                                                            'NOT_CONTAINS_TOKEN',
                                                            'NOT_HAS_PROPERTY',
                                                            'NOT_IN',
                                                        ],
                                                        'required': True,
                                                    },
                                                    'propertyName': {
                                                        'type': 'string',
                                                        'description': 'The name of the property to apply the filter on.',
                                                        'required': True,
                                                    },
                                                    'value': {'type': 'string', 'description': 'The value to match against the property.'},
                                                    'values': {
                                                        'type': 'array',
                                                        'description': 'The values to match against the property.',
                                                        'items': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'properties': {
                                'type': 'array',
                                'description': 'A list of property names to include in the response.',
                                'required': True,
                                'items': {'type': 'string'},
                            },
                            'limit': {
                                'type': 'integer',
                                'description': 'Maximum number of results to return',
                                'required': True,
                                'minimum': 1,
                                'maximum': 200,
                                'default': 25,
                            },
                            'after': {'type': 'string', 'description': 'A paging cursor token for retrieving subsequent pages.'},
                            'sorts': {
                                'type': 'array',
                                'description': 'Sort criteria',
                                'required': True,
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'propertyName': {'type': 'string'},
                                        'direction': {
                                            'type': 'string',
                                            'enum': ['ASCENDING', 'DESCENDING'],
                                        },
                                    },
                                },
                            },
                            'query': {'type': 'string', 'description': 'The search query string, up to 3000 characters.'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of companies',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot company object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique company identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Company properties',
                                            'properties': {
                                                'createdate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'domain': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'name': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the company is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the company was archived',
                                        },
                                        'propertiesWithHistory': {
                                            'type': ['object', 'null'],
                                            'description': 'Properties with historical values',
                                            'additionalProperties': True,
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                        'objectWriteTraceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Trace identifier for write operations',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL to view company in HubSpot',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'companies',
                                    'x-airbyte-stream-name': 'companies',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Companies in HubSpot CRM with industry, size, and revenue data',
                                        'when_to_use': 'Looking up company information or account details',
                                        'trigger_phrases': [
                                            'hubspot company',
                                            'account',
                                            'company details',
                                            'which company',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Find a company in HubSpot', 'Show company details'],
                                        'search_strategy': 'Search by name or domain',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={
                        'total': '$.total',
                        'next_cursor': '$.paging.next.after',
                        'next_link': '$.paging.next.link',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'HubSpot company object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique company identifier'},
                    'properties': {
                        'type': 'object',
                        'description': 'Company properties',
                        'properties': {
                            'createdate': {
                                'type': ['string', 'null'],
                            },
                            'domain': {
                                'type': ['string', 'null'],
                            },
                            'hs_lastmodifieddate': {
                                'type': ['string', 'null'],
                            },
                            'hs_object_id': {
                                'type': ['string', 'null'],
                            },
                            'name': {
                                'type': ['string', 'null'],
                            },
                        },
                        'additionalProperties': True,
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the company is archived'},
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the company was archived',
                    },
                    'propertiesWithHistory': {
                        'type': ['object', 'null'],
                        'description': 'Properties with historical values',
                        'additionalProperties': True,
                    },
                    'associations': {
                        'type': ['object', 'null'],
                        'description': 'Relationships with other CRM objects',
                        'additionalProperties': True,
                    },
                    'objectWriteTraceId': {
                        'type': ['string', 'null'],
                        'description': 'Trace identifier for write operations',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'URL to view company in HubSpot',
                    },
                },
                'x-airbyte-entity-name': 'companies',
                'x-airbyte-stream-name': 'companies',
                'x-airbyte-ai-hints': {
                    'summary': 'Companies in HubSpot CRM with industry, size, and revenue data',
                    'when_to_use': 'Looking up company information or account details',
                    'trigger_phrases': [
                        'hubspot company',
                        'account',
                        'company details',
                        'which company',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Find a company in HubSpot', 'Show company details'],
                    'search_strategy': 'Search by name or domain',
                },
            },
            ai_hints={
                'summary': 'Companies in HubSpot CRM with industry, size, and revenue data',
                'when_to_use': 'Looking up company information or account details',
                'trigger_phrases': [
                    'hubspot company',
                    'account',
                    'company details',
                    'which company',
                ],
                'freshness': 'live',
                'example_questions': ['Find a company in HubSpot', 'Show company details'],
                'search_strategy': 'Search by name or domain',
            },
        ),
        EntityDefinition(
            name='deals',
            stream_name='deals',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
                Action.API_SEARCH,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/deals',
                    action=Action.LIST,
                    description='Returns a paginated list of deals',
                    query_params=[
                        'limit',
                        'after',
                        'associations',
                        'properties',
                        'propertiesWithHistory',
                        'archived',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of deals',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot deal object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique deal identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Deal properties',
                                            'properties': {
                                                'amount': {
                                                    'type': ['string', 'null'],
                                                },
                                                'closedate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'createdate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'dealname': {
                                                    'type': ['string', 'null'],
                                                },
                                                'dealstage': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'pipeline': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the deal is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the deal was archived',
                                        },
                                        'propertiesWithHistory': {
                                            'type': ['object', 'null'],
                                            'description': 'Properties with historical values',
                                            'additionalProperties': True,
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                        'objectWriteTraceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Trace identifier for write operations',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL to view deal in HubSpot',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'deals',
                                    'x-airbyte-stream-name': 'deals',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Sales deals with stage, amount, close date, and owner',
                                        'when_to_use': 'Questions about sales pipeline, deal status, revenue, or forecasts',
                                        'trigger_phrases': [
                                            'deal',
                                            'sales pipeline',
                                            'deal stage',
                                            'revenue forecast',
                                            'close date',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What deals are in the pipeline?', 'Show deals closing this month'],
                                        'search_strategy': 'Search by name or filter by stage, owner, or close date',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/deals',
                    action=Action.CREATE,
                    description='Create a new deal in HubSpot CRM with the provided properties.',
                    body_fields=['properties'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new deal',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Deal properties to set',
                                'required': ['dealname'],
                                'properties': {
                                    'dealname': {'type': 'string', 'description': 'Deal name (required)'},
                                    'amount': {'type': 'string', 'description': 'Deal amount'},
                                    'dealstage': {'type': 'string', 'description': 'Deal stage ID (e.g., appointmentscheduled, qualifiedtobuy, presentationscheduled, decisionmakerboughtin, contractsent, closedwon, closedlost)'},
                                    'pipeline': {'type': 'string', 'description': 'Deal pipeline ID (defaults to the default pipeline)'},
                                    'closedate': {'type': 'string', 'description': 'Expected close date (ISO 8601 format, e.g., 2024-12-31T00:00:00.000Z)'},
                                    'dealtype': {'type': 'string', 'description': 'Deal type (e.g., newbusiness, existingbusiness)'},
                                    'description': {'type': 'string', 'description': 'Deal description'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this deal'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot deal object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique deal identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Deal properties',
                                'properties': {
                                    'amount': {
                                        'type': ['string', 'null'],
                                    },
                                    'closedate': {
                                        'type': ['string', 'null'],
                                    },
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'dealname': {
                                        'type': ['string', 'null'],
                                    },
                                    'dealstage': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'pipeline': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the deal is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the deal was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view deal in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'deals',
                        'x-airbyte-stream-name': 'deals',
                        'x-airbyte-ai-hints': {
                            'summary': 'Sales deals with stage, amount, close date, and owner',
                            'when_to_use': 'Questions about sales pipeline, deal status, revenue, or forecasts',
                            'trigger_phrases': [
                                'deal',
                                'sales pipeline',
                                'deal stage',
                                'revenue forecast',
                                'close date',
                            ],
                            'freshness': 'live',
                            'example_questions': ['What deals are in the pipeline?', 'Show deals closing this month'],
                            'search_strategy': 'Search by name or filter by stage, owner, or close date',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/deals/{dealId}',
                    action=Action.GET,
                    description='Get a single deal by ID',
                    query_params=[
                        'properties',
                        'propertiesWithHistory',
                        'associations',
                        'idProperty',
                        'archived',
                    ],
                    query_params_schema={
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'idProperty': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['dealId'],
                    path_params_schema={
                        'dealId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot deal object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique deal identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Deal properties',
                                'properties': {
                                    'amount': {
                                        'type': ['string', 'null'],
                                    },
                                    'closedate': {
                                        'type': ['string', 'null'],
                                    },
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'dealname': {
                                        'type': ['string', 'null'],
                                    },
                                    'dealstage': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'pipeline': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the deal is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the deal was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view deal in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'deals',
                        'x-airbyte-stream-name': 'deals',
                        'x-airbyte-ai-hints': {
                            'summary': 'Sales deals with stage, amount, close date, and owner',
                            'when_to_use': 'Questions about sales pipeline, deal status, revenue, or forecasts',
                            'trigger_phrases': [
                                'deal',
                                'sales pipeline',
                                'deal stage',
                                'revenue forecast',
                                'close date',
                            ],
                            'freshness': 'live',
                            'example_questions': ['What deals are in the pipeline?', 'Show deals closing this month'],
                            'search_strategy': 'Search by name or filter by stage, owner, or close date',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/crm/v3/objects/deals/{dealId}',
                    action=Action.UPDATE,
                    description="Update an existing deal's properties by ID. Only the specified properties will be updated.",
                    body_fields=['properties'],
                    path_params=['dealId'],
                    path_params_schema={
                        'dealId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing deal. Only provided properties will be updated.',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Deal properties to update',
                                'properties': {
                                    'dealname': {'type': 'string', 'description': 'Deal name'},
                                    'amount': {'type': 'string', 'description': 'Deal amount'},
                                    'dealstage': {'type': 'string', 'description': 'Deal stage ID (e.g., appointmentscheduled, qualifiedtobuy, presentationscheduled, decisionmakerboughtin, contractsent, closedwon, closedlost)'},
                                    'pipeline': {'type': 'string', 'description': 'Deal pipeline ID'},
                                    'closedate': {'type': 'string', 'description': 'Expected close date (ISO 8601 format, e.g., 2024-12-31T00:00:00.000Z)'},
                                    'dealtype': {'type': 'string', 'description': 'Deal type (e.g., newbusiness, existingbusiness)'},
                                    'description': {'type': 'string', 'description': 'Deal description'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this deal'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot deal object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique deal identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Deal properties',
                                'properties': {
                                    'amount': {
                                        'type': ['string', 'null'],
                                    },
                                    'closedate': {
                                        'type': ['string', 'null'],
                                    },
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'dealname': {
                                        'type': ['string', 'null'],
                                    },
                                    'dealstage': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'pipeline': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the deal is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the deal was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view deal in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'deals',
                        'x-airbyte-stream-name': 'deals',
                        'x-airbyte-ai-hints': {
                            'summary': 'Sales deals with stage, amount, close date, and owner',
                            'when_to_use': 'Questions about sales pipeline, deal status, revenue, or forecasts',
                            'trigger_phrases': [
                                'deal',
                                'sales pipeline',
                                'deal stage',
                                'revenue forecast',
                                'close date',
                            ],
                            'freshness': 'live',
                            'example_questions': ['What deals are in the pipeline?', 'Show deals closing this month'],
                            'search_strategy': 'Search by name or filter by stage, owner, or close date',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/deals/search',
                    action=Action.API_SEARCH,
                    description='Search deals with filters and sorting',
                    body_fields=[
                        'filterGroups',
                        'properties',
                        'limit',
                        'after',
                        'sorts',
                        'query',
                    ],
                    request_body_defaults={'limit': 25},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filterGroups': {
                                'type': 'array',
                                'description': 'Up to 6 groups of filters defining additional query criteria.',
                                'required': True,
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'filters': {
                                            'type': 'array',
                                            'required': True,
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'operator': {
                                                        'type': 'string',
                                                        'enum': [
                                                            'BETWEEN',
                                                            'CONTAINS_TOKEN',
                                                            'EQ',
                                                            'GT',
                                                            'GTE',
                                                            'HAS_PROPERTY',
                                                            'IN',
                                                            'LT',
                                                            'LTE',
                                                            'NEQ',
                                                            'NOT_CONTAINS_TOKEN',
                                                            'NOT_HAS_PROPERTY',
                                                            'NOT_IN',
                                                        ],
                                                        'required': True,
                                                    },
                                                    'propertyName': {
                                                        'type': 'string',
                                                        'description': 'The name of the property to apply the filter on.',
                                                        'required': True,
                                                    },
                                                    'value': {'type': 'string', 'description': 'The value to match against the property.'},
                                                    'values': {
                                                        'type': 'array',
                                                        'description': 'The values to match against the property.',
                                                        'items': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'properties': {
                                'type': 'array',
                                'description': 'A list of property names to include in the response.',
                                'required': True,
                                'items': {'type': 'string'},
                            },
                            'limit': {
                                'type': 'integer',
                                'description': 'Maximum number of results to return',
                                'required': True,
                                'minimum': 1,
                                'maximum': 200,
                                'default': 25,
                            },
                            'after': {'type': 'string', 'description': 'A paging cursor token for retrieving subsequent pages.'},
                            'sorts': {
                                'type': 'array',
                                'description': 'Sort criteria',
                                'required': True,
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'propertyName': {'type': 'string'},
                                        'direction': {
                                            'type': 'string',
                                            'enum': ['ASCENDING', 'DESCENDING'],
                                        },
                                    },
                                },
                            },
                            'query': {'type': 'string', 'description': 'The search query string, up to 3000 characters.'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of deals',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot deal object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique deal identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Deal properties',
                                            'properties': {
                                                'amount': {
                                                    'type': ['string', 'null'],
                                                },
                                                'closedate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'createdate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'dealname': {
                                                    'type': ['string', 'null'],
                                                },
                                                'dealstage': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'pipeline': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the deal is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the deal was archived',
                                        },
                                        'propertiesWithHistory': {
                                            'type': ['object', 'null'],
                                            'description': 'Properties with historical values',
                                            'additionalProperties': True,
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                        'objectWriteTraceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Trace identifier for write operations',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL to view deal in HubSpot',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'deals',
                                    'x-airbyte-stream-name': 'deals',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Sales deals with stage, amount, close date, and owner',
                                        'when_to_use': 'Questions about sales pipeline, deal status, revenue, or forecasts',
                                        'trigger_phrases': [
                                            'deal',
                                            'sales pipeline',
                                            'deal stage',
                                            'revenue forecast',
                                            'close date',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What deals are in the pipeline?', 'Show deals closing this month'],
                                        'search_strategy': 'Search by name or filter by stage, owner, or close date',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={
                        'total': '$.total',
                        'next_cursor': '$.paging.next.after',
                        'next_link': '$.paging.next.link',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'HubSpot deal object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique deal identifier'},
                    'properties': {
                        'type': 'object',
                        'description': 'Deal properties',
                        'properties': {
                            'amount': {
                                'type': ['string', 'null'],
                            },
                            'closedate': {
                                'type': ['string', 'null'],
                            },
                            'createdate': {
                                'type': ['string', 'null'],
                            },
                            'dealname': {
                                'type': ['string', 'null'],
                            },
                            'dealstage': {
                                'type': ['string', 'null'],
                            },
                            'hs_lastmodifieddate': {
                                'type': ['string', 'null'],
                            },
                            'hs_object_id': {
                                'type': ['string', 'null'],
                            },
                            'pipeline': {
                                'type': ['string', 'null'],
                            },
                        },
                        'additionalProperties': True,
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the deal is archived'},
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the deal was archived',
                    },
                    'propertiesWithHistory': {
                        'type': ['object', 'null'],
                        'description': 'Properties with historical values',
                        'additionalProperties': True,
                    },
                    'associations': {
                        'type': ['object', 'null'],
                        'description': 'Relationships with other CRM objects',
                        'additionalProperties': True,
                    },
                    'objectWriteTraceId': {
                        'type': ['string', 'null'],
                        'description': 'Trace identifier for write operations',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'URL to view deal in HubSpot',
                    },
                },
                'x-airbyte-entity-name': 'deals',
                'x-airbyte-stream-name': 'deals',
                'x-airbyte-ai-hints': {
                    'summary': 'Sales deals with stage, amount, close date, and owner',
                    'when_to_use': 'Questions about sales pipeline, deal status, revenue, or forecasts',
                    'trigger_phrases': [
                        'deal',
                        'sales pipeline',
                        'deal stage',
                        'revenue forecast',
                        'close date',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What deals are in the pipeline?', 'Show deals closing this month'],
                    'search_strategy': 'Search by name or filter by stage, owner, or close date',
                },
            },
            ai_hints={
                'summary': 'Sales deals with stage, amount, close date, and owner',
                'when_to_use': 'Questions about sales pipeline, deal status, revenue, or forecasts',
                'trigger_phrases': [
                    'deal',
                    'sales pipeline',
                    'deal stage',
                    'revenue forecast',
                    'close date',
                ],
                'freshness': 'live',
                'example_questions': ['What deals are in the pipeline?', 'Show deals closing this month'],
                'search_strategy': 'Search by name or filter by stage, owner, or close date',
            },
        ),
        EntityDefinition(
            name='tickets',
            stream_name='tickets',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
                Action.API_SEARCH,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/tickets',
                    action=Action.LIST,
                    description='Returns a paginated list of tickets',
                    query_params=[
                        'limit',
                        'after',
                        'associations',
                        'properties',
                        'propertiesWithHistory',
                        'archived',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tickets',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot ticket object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique ticket identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Ticket properties',
                                            'properties': {
                                                'content': {
                                                    'type': ['string', 'null'],
                                                },
                                                'createdate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_pipeline': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_pipeline_stage': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_ticket_category': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_ticket_priority': {
                                                    'type': ['string', 'null'],
                                                },
                                                'subject': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the ticket is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the ticket was archived',
                                        },
                                        'propertiesWithHistory': {
                                            'type': ['object', 'null'],
                                            'description': 'Properties with historical values',
                                            'additionalProperties': True,
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                        'objectWriteTraceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Trace identifier for write operations',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL to view ticket in HubSpot',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tickets',
                                    'x-airbyte-stream-name': 'tickets',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Support tickets tracking customer issues and requests',
                                        'when_to_use': 'Finding support tickets or customer service issues',
                                        'trigger_phrases': ['hubspot ticket', 'support ticket', 'customer issue'],
                                        'freshness': 'live',
                                        'example_questions': ['Show open HubSpot tickets', 'Find support tickets for a company'],
                                        'search_strategy': 'Search by subject or filter by status, priority, or assignee',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/tickets',
                    action=Action.CREATE,
                    description='Create a new support ticket in HubSpot CRM with the provided properties.',
                    body_fields=['properties'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new support ticket',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Ticket properties to set',
                                'required': ['subject', 'hs_pipeline', 'hs_pipeline_stage'],
                                'properties': {
                                    'subject': {'type': 'string', 'description': 'Ticket subject line (required)'},
                                    'content': {'type': 'string', 'description': 'Ticket description/content'},
                                    'hs_pipeline': {'type': 'string', 'description': "Ticket pipeline ID (required, use '0' for default pipeline)"},
                                    'hs_pipeline_stage': {'type': 'string', 'description': "Pipeline stage ID (required, e.g., '1' for New in the default pipeline)"},
                                    'hs_ticket_priority': {'type': 'string', 'description': 'Ticket priority (e.g., LOW, MEDIUM, HIGH)'},
                                    'hs_ticket_category': {'type': 'string', 'description': 'Ticket category'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this ticket'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot ticket object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique ticket identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Ticket properties',
                                'properties': {
                                    'content': {
                                        'type': ['string', 'null'],
                                    },
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_pipeline': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_pipeline_stage': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_ticket_category': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_ticket_priority': {
                                        'type': ['string', 'null'],
                                    },
                                    'subject': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the ticket is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the ticket was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view ticket in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'tickets',
                        'x-airbyte-stream-name': 'tickets',
                        'x-airbyte-ai-hints': {
                            'summary': 'Support tickets tracking customer issues and requests',
                            'when_to_use': 'Finding support tickets or customer service issues',
                            'trigger_phrases': ['hubspot ticket', 'support ticket', 'customer issue'],
                            'freshness': 'live',
                            'example_questions': ['Show open HubSpot tickets', 'Find support tickets for a company'],
                            'search_strategy': 'Search by subject or filter by status, priority, or assignee',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/tickets/{ticketId}',
                    action=Action.GET,
                    description='Get a single ticket by ID',
                    query_params=[
                        'properties',
                        'propertiesWithHistory',
                        'associations',
                        'idProperty',
                        'archived',
                    ],
                    query_params_schema={
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'idProperty': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['ticketId'],
                    path_params_schema={
                        'ticketId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot ticket object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique ticket identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Ticket properties',
                                'properties': {
                                    'content': {
                                        'type': ['string', 'null'],
                                    },
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_pipeline': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_pipeline_stage': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_ticket_category': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_ticket_priority': {
                                        'type': ['string', 'null'],
                                    },
                                    'subject': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the ticket is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the ticket was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view ticket in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'tickets',
                        'x-airbyte-stream-name': 'tickets',
                        'x-airbyte-ai-hints': {
                            'summary': 'Support tickets tracking customer issues and requests',
                            'when_to_use': 'Finding support tickets or customer service issues',
                            'trigger_phrases': ['hubspot ticket', 'support ticket', 'customer issue'],
                            'freshness': 'live',
                            'example_questions': ['Show open HubSpot tickets', 'Find support tickets for a company'],
                            'search_strategy': 'Search by subject or filter by status, priority, or assignee',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/crm/v3/objects/tickets/{ticketId}',
                    action=Action.UPDATE,
                    description="Update an existing ticket's properties by ID. Only the specified properties will be updated.",
                    body_fields=['properties'],
                    path_params=['ticketId'],
                    path_params_schema={
                        'ticketId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing ticket. Only provided properties will be updated.',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Ticket properties to update',
                                'properties': {
                                    'subject': {'type': 'string', 'description': 'Ticket subject line'},
                                    'content': {'type': 'string', 'description': 'Ticket description/content'},
                                    'hs_pipeline': {'type': 'string', 'description': 'Ticket pipeline ID'},
                                    'hs_pipeline_stage': {'type': 'string', 'description': 'Pipeline stage ID'},
                                    'hs_ticket_priority': {'type': 'string', 'description': 'Ticket priority (e.g., LOW, MEDIUM, HIGH)'},
                                    'hs_ticket_category': {'type': 'string', 'description': 'Ticket category'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this ticket'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot ticket object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique ticket identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Ticket properties',
                                'properties': {
                                    'content': {
                                        'type': ['string', 'null'],
                                    },
                                    'createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_pipeline': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_pipeline_stage': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_ticket_category': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_ticket_priority': {
                                        'type': ['string', 'null'],
                                    },
                                    'subject': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the ticket is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the ticket was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view ticket in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'tickets',
                        'x-airbyte-stream-name': 'tickets',
                        'x-airbyte-ai-hints': {
                            'summary': 'Support tickets tracking customer issues and requests',
                            'when_to_use': 'Finding support tickets or customer service issues',
                            'trigger_phrases': ['hubspot ticket', 'support ticket', 'customer issue'],
                            'freshness': 'live',
                            'example_questions': ['Show open HubSpot tickets', 'Find support tickets for a company'],
                            'search_strategy': 'Search by subject or filter by status, priority, or assignee',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/tickets/search',
                    action=Action.API_SEARCH,
                    description='Search for tickets by filtering on properties, searching through associations, and sorting results.',
                    body_fields=[
                        'filterGroups',
                        'properties',
                        'limit',
                        'after',
                        'sorts',
                        'query',
                    ],
                    request_body_defaults={'limit': 25},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filterGroups': {
                                'type': 'array',
                                'description': 'Up to 6 groups of filters defining additional query criteria.',
                                'required': True,
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'filters': {
                                            'type': 'array',
                                            'required': True,
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'operator': {
                                                        'type': 'string',
                                                        'enum': [
                                                            'BETWEEN',
                                                            'CONTAINS_TOKEN',
                                                            'EQ',
                                                            'GT',
                                                            'GTE',
                                                            'HAS_PROPERTY',
                                                            'IN',
                                                            'LT',
                                                            'LTE',
                                                            'NEQ',
                                                            'NOT_CONTAINS_TOKEN',
                                                            'NOT_HAS_PROPERTY',
                                                            'NOT_IN',
                                                        ],
                                                        'required': True,
                                                    },
                                                    'propertyName': {
                                                        'type': 'string',
                                                        'description': 'The name of the property to apply the filter on.',
                                                        'required': True,
                                                    },
                                                    'value': {'type': 'string', 'description': 'The value to match against the property.'},
                                                    'values': {
                                                        'type': 'array',
                                                        'description': 'The values to match against the property.',
                                                        'items': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'properties': {
                                'type': 'array',
                                'description': 'A list of property names to include in the response.',
                                'required': True,
                                'items': {'type': 'string'},
                            },
                            'limit': {
                                'type': 'integer',
                                'description': 'Maximum number of results to return',
                                'required': True,
                                'minimum': 1,
                                'maximum': 200,
                                'default': 25,
                            },
                            'after': {'type': 'string', 'description': 'A paging cursor token for retrieving subsequent pages.'},
                            'sorts': {
                                'type': 'array',
                                'description': 'Sort criteria',
                                'required': True,
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'propertyName': {'type': 'string'},
                                        'direction': {
                                            'type': 'string',
                                            'enum': ['ASCENDING', 'DESCENDING'],
                                        },
                                    },
                                },
                            },
                            'query': {'type': 'string', 'description': 'The search query string, up to 3000 characters.'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tickets',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot ticket object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique ticket identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Ticket properties',
                                            'properties': {
                                                'content': {
                                                    'type': ['string', 'null'],
                                                },
                                                'createdate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_pipeline': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_pipeline_stage': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_ticket_category': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_ticket_priority': {
                                                    'type': ['string', 'null'],
                                                },
                                                'subject': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the ticket is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the ticket was archived',
                                        },
                                        'propertiesWithHistory': {
                                            'type': ['object', 'null'],
                                            'description': 'Properties with historical values',
                                            'additionalProperties': True,
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                        'objectWriteTraceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Trace identifier for write operations',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL to view ticket in HubSpot',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tickets',
                                    'x-airbyte-stream-name': 'tickets',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Support tickets tracking customer issues and requests',
                                        'when_to_use': 'Finding support tickets or customer service issues',
                                        'trigger_phrases': ['hubspot ticket', 'support ticket', 'customer issue'],
                                        'freshness': 'live',
                                        'example_questions': ['Show open HubSpot tickets', 'Find support tickets for a company'],
                                        'search_strategy': 'Search by subject or filter by status, priority, or assignee',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={
                        'total': '$.total',
                        'next_cursor': '$.paging.next.after',
                        'next_link': '$.paging.next.link',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'HubSpot ticket object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique ticket identifier'},
                    'properties': {
                        'type': 'object',
                        'description': 'Ticket properties',
                        'properties': {
                            'content': {
                                'type': ['string', 'null'],
                            },
                            'createdate': {
                                'type': ['string', 'null'],
                            },
                            'hs_lastmodifieddate': {
                                'type': ['string', 'null'],
                            },
                            'hs_object_id': {
                                'type': ['string', 'null'],
                            },
                            'hs_pipeline': {
                                'type': ['string', 'null'],
                            },
                            'hs_pipeline_stage': {
                                'type': ['string', 'null'],
                            },
                            'hs_ticket_category': {
                                'type': ['string', 'null'],
                            },
                            'hs_ticket_priority': {
                                'type': ['string', 'null'],
                            },
                            'subject': {
                                'type': ['string', 'null'],
                            },
                        },
                        'additionalProperties': True,
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the ticket is archived'},
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the ticket was archived',
                    },
                    'propertiesWithHistory': {
                        'type': ['object', 'null'],
                        'description': 'Properties with historical values',
                        'additionalProperties': True,
                    },
                    'associations': {
                        'type': ['object', 'null'],
                        'description': 'Relationships with other CRM objects',
                        'additionalProperties': True,
                    },
                    'objectWriteTraceId': {
                        'type': ['string', 'null'],
                        'description': 'Trace identifier for write operations',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'URL to view ticket in HubSpot',
                    },
                },
                'x-airbyte-entity-name': 'tickets',
                'x-airbyte-stream-name': 'tickets',
                'x-airbyte-ai-hints': {
                    'summary': 'Support tickets tracking customer issues and requests',
                    'when_to_use': 'Finding support tickets or customer service issues',
                    'trigger_phrases': ['hubspot ticket', 'support ticket', 'customer issue'],
                    'freshness': 'live',
                    'example_questions': ['Show open HubSpot tickets', 'Find support tickets for a company'],
                    'search_strategy': 'Search by subject or filter by status, priority, or assignee',
                },
            },
            ai_hints={
                'summary': 'Support tickets tracking customer issues and requests',
                'when_to_use': 'Finding support tickets or customer service issues',
                'trigger_phrases': ['hubspot ticket', 'support ticket', 'customer issue'],
                'freshness': 'live',
                'example_questions': ['Show open HubSpot tickets', 'Find support tickets for a company'],
                'search_strategy': 'Search by subject or filter by status, priority, or assignee',
            },
        ),
        EntityDefinition(
            name='notes',
            stream_name='engagements_notes',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.DELETE,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/notes',
                    action=Action.LIST,
                    description='Returns a paginated list of notes',
                    query_params=[
                        'limit',
                        'after',
                        'associations',
                        'properties',
                        'propertiesWithHistory',
                        'archived',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of notes',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot note/engagement object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique note identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Note properties',
                                            'properties': {
                                                'hs_note_body': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The body content of the note (supports HTML)',
                                                },
                                                'hs_timestamp': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Timestamp when the note activity occurred',
                                                },
                                                'hubspot_owner_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'ID of the note owner',
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'HubSpot object ID',
                                                },
                                                'hs_createdate': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Date the note was created',
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Last modified date',
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the note is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the note was archived',
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'x-airbyte-entity-name': 'notes',
                                    'x-airbyte-stream-name': 'engagements_notes',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Notes attached to CRM records (contacts, companies, deals, tickets)',
                                        'when_to_use': 'Listing, viewing, adding, updating, or deleting notes on CRM records',
                                        'trigger_phrases': [
                                            'add note',
                                            'create note',
                                            'write note',
                                            'note to contact',
                                            'note on deal',
                                            'list notes',
                                            'get note',
                                            'delete note',
                                            'remove note',
                                        ],
                                        'freshness': 'live',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/notes',
                    action=Action.CREATE,
                    description='Create a new note in HubSpot CRM. Notes can be associated with contacts,\ncompanies, deals, or tickets by using the associations parameter.\nThe hs_timestamp property sets when the note activity occurred.\n',
                    body_fields=['properties', 'associations'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new note',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Note properties to set',
                                'required': ['hs_note_body', 'hs_timestamp'],
                                'properties': {
                                    'hs_note_body': {'type': 'string', 'description': 'The body content of the note (supports HTML)'},
                                    'hs_timestamp': {'type': 'string', 'description': 'Required. Timestamp when the note activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one.'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this note'},
                                },
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': 'array',
                                'description': 'Associate the note with other CRM records (contacts, companies, deals, tickets)',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'to': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'ID of the record to associate with'},
                                            },
                                        },
                                        'types': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'associationCategory': {'type': 'string', 'description': 'Association category (e.g., HUBSPOT_DEFINED)'},
                                                    'associationTypeId': {'type': 'integer', 'description': 'Association type ID (e.g., 202 for note-to-contact, 190 for note-to-company, 214 for note-to-deal, 18 for note-to-ticket)'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot note/engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique note identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Note properties',
                                'properties': {
                                    'hs_note_body': {
                                        'type': ['string', 'null'],
                                        'description': 'The body content of the note (supports HTML)',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the note activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the note owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the note was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the note is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the note was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'notes',
                        'x-airbyte-stream-name': 'engagements_notes',
                        'x-airbyte-ai-hints': {
                            'summary': 'Notes attached to CRM records (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, adding, updating, or deleting notes on CRM records',
                            'trigger_phrases': [
                                'add note',
                                'create note',
                                'write note',
                                'note to contact',
                                'note on deal',
                                'list notes',
                                'get note',
                                'delete note',
                                'remove note',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/notes/{noteId}',
                    action=Action.GET,
                    description='Get a single note by ID',
                    query_params=[
                        'properties',
                        'propertiesWithHistory',
                        'associations',
                        'idProperty',
                        'archived',
                    ],
                    query_params_schema={
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'idProperty': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['noteId'],
                    path_params_schema={
                        'noteId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot note/engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique note identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Note properties',
                                'properties': {
                                    'hs_note_body': {
                                        'type': ['string', 'null'],
                                        'description': 'The body content of the note (supports HTML)',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the note activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the note owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the note was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the note is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the note was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'notes',
                        'x-airbyte-stream-name': 'engagements_notes',
                        'x-airbyte-ai-hints': {
                            'summary': 'Notes attached to CRM records (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, adding, updating, or deleting notes on CRM records',
                            'trigger_phrases': [
                                'add note',
                                'create note',
                                'write note',
                                'note to contact',
                                'note on deal',
                                'list notes',
                                'get note',
                                'delete note',
                                'remove note',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/crm/v3/objects/notes/{noteId}',
                    action=Action.DELETE,
                    description='Archive a note by ID. This is a soft delete — the note is moved to the\nrecycle bin and can be restored for approximately 90 days. No public\nhard-delete endpoint exists.\n',
                    path_params=['noteId'],
                    path_params_schema={
                        'noteId': {'type': 'string', 'required': True},
                    },
                    no_content_response=True,
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/crm/v3/objects/notes/{noteId}',
                    action=Action.UPDATE,
                    description="Update an existing note's properties by ID.",
                    body_fields=['properties'],
                    path_params=['noteId'],
                    path_params_schema={
                        'noteId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing note. Only provided properties will be updated.',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Note properties to update',
                                'properties': {
                                    'hs_note_body': {'type': 'string', 'description': 'The body content of the note (supports HTML)'},
                                    'hs_timestamp': {'type': 'string', 'description': 'Timestamp when the note activity occurred'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this note'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot note/engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique note identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Note properties',
                                'properties': {
                                    'hs_note_body': {
                                        'type': ['string', 'null'],
                                        'description': 'The body content of the note (supports HTML)',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the note activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the note owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the note was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the note is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the note was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'notes',
                        'x-airbyte-stream-name': 'engagements_notes',
                        'x-airbyte-ai-hints': {
                            'summary': 'Notes attached to CRM records (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, adding, updating, or deleting notes on CRM records',
                            'trigger_phrases': [
                                'add note',
                                'create note',
                                'write note',
                                'note to contact',
                                'note on deal',
                                'list notes',
                                'get note',
                                'delete note',
                                'remove note',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'HubSpot note/engagement object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique note identifier'},
                    'properties': {
                        'type': 'object',
                        'description': 'Note properties',
                        'properties': {
                            'hs_note_body': {
                                'type': ['string', 'null'],
                                'description': 'The body content of the note (supports HTML)',
                            },
                            'hs_timestamp': {
                                'type': ['string', 'null'],
                                'description': 'Timestamp when the note activity occurred',
                            },
                            'hubspot_owner_id': {
                                'type': ['string', 'null'],
                                'description': 'ID of the note owner',
                            },
                            'hs_object_id': {
                                'type': ['string', 'null'],
                                'description': 'HubSpot object ID',
                            },
                            'hs_createdate': {
                                'type': ['string', 'null'],
                                'description': 'Date the note was created',
                            },
                            'hs_lastmodifieddate': {
                                'type': ['string', 'null'],
                                'description': 'Last modified date',
                            },
                        },
                        'additionalProperties': True,
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the note is archived'},
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the note was archived',
                    },
                    'associations': {
                        'type': ['object', 'null'],
                        'description': 'Relationships with other CRM objects',
                        'additionalProperties': True,
                    },
                },
                'x-airbyte-entity-name': 'notes',
                'x-airbyte-stream-name': 'engagements_notes',
                'x-airbyte-ai-hints': {
                    'summary': 'Notes attached to CRM records (contacts, companies, deals, tickets)',
                    'when_to_use': 'Listing, viewing, adding, updating, or deleting notes on CRM records',
                    'trigger_phrases': [
                        'add note',
                        'create note',
                        'write note',
                        'note to contact',
                        'note on deal',
                        'list notes',
                        'get note',
                        'delete note',
                        'remove note',
                    ],
                    'freshness': 'live',
                },
            },
            ai_hints={
                'summary': 'Notes attached to CRM records (contacts, companies, deals, tickets)',
                'when_to_use': 'Listing, viewing, adding, updating, or deleting notes on CRM records',
                'trigger_phrases': [
                    'add note',
                    'create note',
                    'write note',
                    'note to contact',
                    'note on deal',
                    'list notes',
                    'get note',
                    'delete note',
                    'remove note',
                ],
                'freshness': 'live',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='notes',
                    target_entity='contacts',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='notes',
                    target_entity='companies',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='notes',
                    target_entity='deals',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='notes',
                    target_entity='tickets',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
            ],
        ),
        EntityDefinition(
            name='calls',
            stream_name='engagements_calls',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.DELETE,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/calls',
                    action=Action.LIST,
                    description='Returns a paginated list of calls',
                    query_params=[
                        'limit',
                        'after',
                        'associations',
                        'properties',
                        'propertiesWithHistory',
                        'archived',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of calls',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot call engagement object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique call identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Call properties',
                                            'properties': {
                                                'hs_call_body': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Description or notes about the call',
                                                },
                                                'hs_call_direction': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Direction of the call (INBOUND or OUTBOUND)',
                                                },
                                                'hs_call_disposition': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The outcome of the call (e.g., connected, no answer, busy, left voicemail)',
                                                },
                                                'hs_call_duration': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Duration of the call in milliseconds',
                                                },
                                                'hs_call_from_number': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Phone number the call was made from',
                                                },
                                                'hs_call_to_number': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Phone number the call was made to',
                                                },
                                                'hs_call_status': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER, FAILED, CANCELED, CONNECTING, RINGING, IN_PROGRESS)',
                                                },
                                                'hs_call_title': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Title or subject of the call',
                                                },
                                                'hs_timestamp': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Timestamp when the call activity occurred',
                                                },
                                                'hubspot_owner_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'ID of the call owner',
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'HubSpot object ID',
                                                },
                                                'hs_createdate': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Date the call was created',
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Last modified date',
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the call is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the call was archived',
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'x-airbyte-entity-name': 'calls',
                                    'x-airbyte-stream-name': 'engagements_calls',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Call engagements logged in the CRM (contacts, companies, deals, tickets)',
                                        'when_to_use': 'Listing, viewing, logging, updating, or deleting call records on CRM objects',
                                        'trigger_phrases': [
                                            'log call',
                                            'create call',
                                            'record call',
                                            'call to contact',
                                            'call on deal',
                                            'list calls',
                                            'get call',
                                            'delete call',
                                            'remove call',
                                        ],
                                        'freshness': 'live',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/calls',
                    action=Action.CREATE,
                    description='Create a new call engagement in HubSpot CRM. Calls can be associated with contacts,\ncompanies, deals, or tickets by using the associations parameter.\nThe hs_timestamp property sets when the call activity occurred.\n',
                    body_fields=['properties', 'associations'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new call',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Call properties to set',
                                'required': ['hs_timestamp'],
                                'properties': {
                                    'hs_call_body': {'type': 'string', 'description': 'Description or notes about the call'},
                                    'hs_call_direction': {'type': 'string', 'description': 'Direction of the call (INBOUND or OUTBOUND)'},
                                    'hs_call_disposition': {'type': 'string', 'description': 'The outcome of the call (e.g., connected, no answer, busy, left voicemail)'},
                                    'hs_call_duration': {'type': 'string', 'description': 'Duration of the call in milliseconds'},
                                    'hs_call_from_number': {'type': 'string', 'description': 'Phone number the call was made from'},
                                    'hs_call_to_number': {'type': 'string', 'description': 'Phone number the call was made to'},
                                    'hs_call_status': {'type': 'string', 'description': 'Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER, FAILED, CANCELED)'},
                                    'hs_call_title': {'type': 'string', 'description': 'Title or subject of the call'},
                                    'hs_timestamp': {'type': 'string', 'description': 'Required. Timestamp when the call activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one.'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this call'},
                                },
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': 'array',
                                'description': 'Associate the call with other CRM records (contacts, companies, deals, tickets)',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'to': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'ID of the record to associate with'},
                                            },
                                        },
                                        'types': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'associationCategory': {'type': 'string', 'description': 'Association category (e.g., HUBSPOT_DEFINED)'},
                                                    'associationTypeId': {'type': 'integer', 'description': 'Association type ID (e.g., 194 for call-to-contact, 182 for call-to-company, 206 for call-to-deal, 220 for call-to-ticket)'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot call engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique call identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Call properties',
                                'properties': {
                                    'hs_call_body': {
                                        'type': ['string', 'null'],
                                        'description': 'Description or notes about the call',
                                    },
                                    'hs_call_direction': {
                                        'type': ['string', 'null'],
                                        'description': 'Direction of the call (INBOUND or OUTBOUND)',
                                    },
                                    'hs_call_disposition': {
                                        'type': ['string', 'null'],
                                        'description': 'The outcome of the call (e.g., connected, no answer, busy, left voicemail)',
                                    },
                                    'hs_call_duration': {
                                        'type': ['string', 'null'],
                                        'description': 'Duration of the call in milliseconds',
                                    },
                                    'hs_call_from_number': {
                                        'type': ['string', 'null'],
                                        'description': 'Phone number the call was made from',
                                    },
                                    'hs_call_to_number': {
                                        'type': ['string', 'null'],
                                        'description': 'Phone number the call was made to',
                                    },
                                    'hs_call_status': {
                                        'type': ['string', 'null'],
                                        'description': 'Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER, FAILED, CANCELED, CONNECTING, RINGING, IN_PROGRESS)',
                                    },
                                    'hs_call_title': {
                                        'type': ['string', 'null'],
                                        'description': 'Title or subject of the call',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the call activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the call owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the call was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the call is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the call was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'calls',
                        'x-airbyte-stream-name': 'engagements_calls',
                        'x-airbyte-ai-hints': {
                            'summary': 'Call engagements logged in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, logging, updating, or deleting call records on CRM objects',
                            'trigger_phrases': [
                                'log call',
                                'create call',
                                'record call',
                                'call to contact',
                                'call on deal',
                                'list calls',
                                'get call',
                                'delete call',
                                'remove call',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/calls/{callId}',
                    action=Action.GET,
                    description='Get a single call by ID',
                    query_params=[
                        'properties',
                        'propertiesWithHistory',
                        'associations',
                        'idProperty',
                        'archived',
                    ],
                    query_params_schema={
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'idProperty': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['callId'],
                    path_params_schema={
                        'callId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot call engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique call identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Call properties',
                                'properties': {
                                    'hs_call_body': {
                                        'type': ['string', 'null'],
                                        'description': 'Description or notes about the call',
                                    },
                                    'hs_call_direction': {
                                        'type': ['string', 'null'],
                                        'description': 'Direction of the call (INBOUND or OUTBOUND)',
                                    },
                                    'hs_call_disposition': {
                                        'type': ['string', 'null'],
                                        'description': 'The outcome of the call (e.g., connected, no answer, busy, left voicemail)',
                                    },
                                    'hs_call_duration': {
                                        'type': ['string', 'null'],
                                        'description': 'Duration of the call in milliseconds',
                                    },
                                    'hs_call_from_number': {
                                        'type': ['string', 'null'],
                                        'description': 'Phone number the call was made from',
                                    },
                                    'hs_call_to_number': {
                                        'type': ['string', 'null'],
                                        'description': 'Phone number the call was made to',
                                    },
                                    'hs_call_status': {
                                        'type': ['string', 'null'],
                                        'description': 'Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER, FAILED, CANCELED, CONNECTING, RINGING, IN_PROGRESS)',
                                    },
                                    'hs_call_title': {
                                        'type': ['string', 'null'],
                                        'description': 'Title or subject of the call',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the call activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the call owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the call was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the call is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the call was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'calls',
                        'x-airbyte-stream-name': 'engagements_calls',
                        'x-airbyte-ai-hints': {
                            'summary': 'Call engagements logged in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, logging, updating, or deleting call records on CRM objects',
                            'trigger_phrases': [
                                'log call',
                                'create call',
                                'record call',
                                'call to contact',
                                'call on deal',
                                'list calls',
                                'get call',
                                'delete call',
                                'remove call',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/crm/v3/objects/calls/{callId}',
                    action=Action.DELETE,
                    description='Archive a call by ID. This is a soft delete — the call is moved to the\nrecycle bin and can be restored for approximately 90 days. No public\nhard-delete endpoint exists.\n',
                    path_params=['callId'],
                    path_params_schema={
                        'callId': {'type': 'string', 'required': True},
                    },
                    no_content_response=True,
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/crm/v3/objects/calls/{callId}',
                    action=Action.UPDATE,
                    description="Update an existing call's properties by ID.",
                    body_fields=['properties'],
                    path_params=['callId'],
                    path_params_schema={
                        'callId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing call. Only provided properties will be updated.',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Call properties to update',
                                'properties': {
                                    'hs_call_body': {'type': 'string', 'description': 'Description or notes about the call'},
                                    'hs_call_direction': {'type': 'string', 'description': 'Direction of the call (INBOUND or OUTBOUND)'},
                                    'hs_call_disposition': {'type': 'string', 'description': 'The outcome of the call'},
                                    'hs_call_duration': {'type': 'string', 'description': 'Duration of the call in milliseconds'},
                                    'hs_call_from_number': {'type': 'string', 'description': 'Phone number the call was made from'},
                                    'hs_call_to_number': {'type': 'string', 'description': 'Phone number the call was made to'},
                                    'hs_call_status': {'type': 'string', 'description': 'Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)'},
                                    'hs_call_title': {'type': 'string', 'description': 'Title or subject of the call'},
                                    'hs_timestamp': {'type': 'string', 'description': 'Timestamp when the call activity occurred'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this call'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot call engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique call identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Call properties',
                                'properties': {
                                    'hs_call_body': {
                                        'type': ['string', 'null'],
                                        'description': 'Description or notes about the call',
                                    },
                                    'hs_call_direction': {
                                        'type': ['string', 'null'],
                                        'description': 'Direction of the call (INBOUND or OUTBOUND)',
                                    },
                                    'hs_call_disposition': {
                                        'type': ['string', 'null'],
                                        'description': 'The outcome of the call (e.g., connected, no answer, busy, left voicemail)',
                                    },
                                    'hs_call_duration': {
                                        'type': ['string', 'null'],
                                        'description': 'Duration of the call in milliseconds',
                                    },
                                    'hs_call_from_number': {
                                        'type': ['string', 'null'],
                                        'description': 'Phone number the call was made from',
                                    },
                                    'hs_call_to_number': {
                                        'type': ['string', 'null'],
                                        'description': 'Phone number the call was made to',
                                    },
                                    'hs_call_status': {
                                        'type': ['string', 'null'],
                                        'description': 'Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER, FAILED, CANCELED, CONNECTING, RINGING, IN_PROGRESS)',
                                    },
                                    'hs_call_title': {
                                        'type': ['string', 'null'],
                                        'description': 'Title or subject of the call',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the call activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the call owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the call was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the call is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the call was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'calls',
                        'x-airbyte-stream-name': 'engagements_calls',
                        'x-airbyte-ai-hints': {
                            'summary': 'Call engagements logged in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, logging, updating, or deleting call records on CRM objects',
                            'trigger_phrases': [
                                'log call',
                                'create call',
                                'record call',
                                'call to contact',
                                'call on deal',
                                'list calls',
                                'get call',
                                'delete call',
                                'remove call',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'HubSpot call engagement object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique call identifier'},
                    'properties': {
                        'type': 'object',
                        'description': 'Call properties',
                        'properties': {
                            'hs_call_body': {
                                'type': ['string', 'null'],
                                'description': 'Description or notes about the call',
                            },
                            'hs_call_direction': {
                                'type': ['string', 'null'],
                                'description': 'Direction of the call (INBOUND or OUTBOUND)',
                            },
                            'hs_call_disposition': {
                                'type': ['string', 'null'],
                                'description': 'The outcome of the call (e.g., connected, no answer, busy, left voicemail)',
                            },
                            'hs_call_duration': {
                                'type': ['string', 'null'],
                                'description': 'Duration of the call in milliseconds',
                            },
                            'hs_call_from_number': {
                                'type': ['string', 'null'],
                                'description': 'Phone number the call was made from',
                            },
                            'hs_call_to_number': {
                                'type': ['string', 'null'],
                                'description': 'Phone number the call was made to',
                            },
                            'hs_call_status': {
                                'type': ['string', 'null'],
                                'description': 'Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER, FAILED, CANCELED, CONNECTING, RINGING, IN_PROGRESS)',
                            },
                            'hs_call_title': {
                                'type': ['string', 'null'],
                                'description': 'Title or subject of the call',
                            },
                            'hs_timestamp': {
                                'type': ['string', 'null'],
                                'description': 'Timestamp when the call activity occurred',
                            },
                            'hubspot_owner_id': {
                                'type': ['string', 'null'],
                                'description': 'ID of the call owner',
                            },
                            'hs_object_id': {
                                'type': ['string', 'null'],
                                'description': 'HubSpot object ID',
                            },
                            'hs_createdate': {
                                'type': ['string', 'null'],
                                'description': 'Date the call was created',
                            },
                            'hs_lastmodifieddate': {
                                'type': ['string', 'null'],
                                'description': 'Last modified date',
                            },
                        },
                        'additionalProperties': True,
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the call is archived'},
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the call was archived',
                    },
                    'associations': {
                        'type': ['object', 'null'],
                        'description': 'Relationships with other CRM objects',
                        'additionalProperties': True,
                    },
                },
                'x-airbyte-entity-name': 'calls',
                'x-airbyte-stream-name': 'engagements_calls',
                'x-airbyte-ai-hints': {
                    'summary': 'Call engagements logged in the CRM (contacts, companies, deals, tickets)',
                    'when_to_use': 'Listing, viewing, logging, updating, or deleting call records on CRM objects',
                    'trigger_phrases': [
                        'log call',
                        'create call',
                        'record call',
                        'call to contact',
                        'call on deal',
                        'list calls',
                        'get call',
                        'delete call',
                        'remove call',
                    ],
                    'freshness': 'live',
                },
            },
            ai_hints={
                'summary': 'Call engagements logged in the CRM (contacts, companies, deals, tickets)',
                'when_to_use': 'Listing, viewing, logging, updating, or deleting call records on CRM objects',
                'trigger_phrases': [
                    'log call',
                    'create call',
                    'record call',
                    'call to contact',
                    'call on deal',
                    'list calls',
                    'get call',
                    'delete call',
                    'remove call',
                ],
                'freshness': 'live',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='calls',
                    target_entity='contacts',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='calls',
                    target_entity='companies',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='calls',
                    target_entity='deals',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='calls',
                    target_entity='tickets',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
            ],
        ),
        EntityDefinition(
            name='emails',
            stream_name='engagements_emails',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.DELETE,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/emails',
                    action=Action.LIST,
                    description='Returns a paginated list of emails',
                    query_params=[
                        'limit',
                        'after',
                        'associations',
                        'properties',
                        'propertiesWithHistory',
                        'archived',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of emails',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot email engagement object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique email identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Email properties',
                                            'properties': {
                                                'hs_email_subject': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Subject line of the email',
                                                },
                                                'hs_email_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text body of the email',
                                                },
                                                'hs_email_html': {
                                                    'type': ['string', 'null'],
                                                    'description': 'HTML body of the email',
                                                },
                                                'hs_email_direction': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)',
                                                },
                                                'hs_email_status': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Status of the email (e.g., BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)',
                                                },
                                                'hs_email_sender_email': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Sender email address',
                                                },
                                                'hs_email_to_email': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Recipient email address(es)',
                                                },
                                                'hs_timestamp': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Timestamp when the email activity occurred',
                                                },
                                                'hubspot_owner_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'ID of the email owner',
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'HubSpot object ID',
                                                },
                                                'hs_createdate': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Date the email was created',
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Last modified date',
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the email is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the email was archived',
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'x-airbyte-entity-name': 'emails',
                                    'x-airbyte-stream-name': 'engagements_emails',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Email engagements logged in the CRM (contacts, companies, deals, tickets)',
                                        'when_to_use': 'Listing, viewing, logging, updating, or deleting email records on CRM objects',
                                        'trigger_phrases': [
                                            'log email',
                                            'create email',
                                            'record email',
                                            'email to contact',
                                            'email on deal',
                                            'list emails',
                                            'get email',
                                            'delete email',
                                            'remove email',
                                        ],
                                        'freshness': 'live',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/emails',
                    action=Action.CREATE,
                    description='Create a new email engagement in HubSpot CRM. Emails can be associated with contacts,\ncompanies, deals, or tickets by using the associations parameter.\nThe hs_timestamp property sets when the email activity occurred.\n',
                    body_fields=['properties', 'associations'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new email',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Email properties to set',
                                'required': ['hs_timestamp', 'hs_email_direction'],
                                'properties': {
                                    'hs_email_subject': {'type': 'string', 'description': 'Subject line of the email'},
                                    'hs_email_text': {'type': 'string', 'description': 'Plain text body of the email'},
                                    'hs_email_html': {'type': 'string', 'description': 'HTML body of the email'},
                                    'hs_email_direction': {'type': 'string', 'description': 'Required. Direction of the email (EMAIL for sent, INCOMING_EMAIL for received, FORWARDED_EMAIL for forwarded)'},
                                    'hs_email_status': {'type': 'string', 'description': 'Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)'},
                                    'hs_email_sender_email': {'type': 'string', 'description': 'Sender email address'},
                                    'hs_email_to_email': {'type': 'string', 'description': 'Recipient email address(es)'},
                                    'hs_timestamp': {'type': 'string', 'description': 'Required. Timestamp when the email activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one.'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this email'},
                                },
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': 'array',
                                'description': 'Associate the email with other CRM records (contacts, companies, deals, tickets)',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'to': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'ID of the record to associate with'},
                                            },
                                        },
                                        'types': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'associationCategory': {'type': 'string', 'description': 'Association category (e.g., HUBSPOT_DEFINED)'},
                                                    'associationTypeId': {'type': 'integer', 'description': 'Association type ID (e.g., 198 for email-to-contact, 186 for email-to-company, 210 for email-to-deal, 224 for email-to-ticket)'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot email engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique email identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Email properties',
                                'properties': {
                                    'hs_email_subject': {
                                        'type': ['string', 'null'],
                                        'description': 'Subject line of the email',
                                    },
                                    'hs_email_text': {
                                        'type': ['string', 'null'],
                                        'description': 'Plain text body of the email',
                                    },
                                    'hs_email_html': {
                                        'type': ['string', 'null'],
                                        'description': 'HTML body of the email',
                                    },
                                    'hs_email_direction': {
                                        'type': ['string', 'null'],
                                        'description': 'Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)',
                                    },
                                    'hs_email_status': {
                                        'type': ['string', 'null'],
                                        'description': 'Status of the email (e.g., BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)',
                                    },
                                    'hs_email_sender_email': {
                                        'type': ['string', 'null'],
                                        'description': 'Sender email address',
                                    },
                                    'hs_email_to_email': {
                                        'type': ['string', 'null'],
                                        'description': 'Recipient email address(es)',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the email activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the email owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the email was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the email is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the email was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'emails',
                        'x-airbyte-stream-name': 'engagements_emails',
                        'x-airbyte-ai-hints': {
                            'summary': 'Email engagements logged in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, logging, updating, or deleting email records on CRM objects',
                            'trigger_phrases': [
                                'log email',
                                'create email',
                                'record email',
                                'email to contact',
                                'email on deal',
                                'list emails',
                                'get email',
                                'delete email',
                                'remove email',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/emails/{emailId}',
                    action=Action.GET,
                    description='Get a single email by ID',
                    query_params=[
                        'properties',
                        'propertiesWithHistory',
                        'associations',
                        'idProperty',
                        'archived',
                    ],
                    query_params_schema={
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'idProperty': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['emailId'],
                    path_params_schema={
                        'emailId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot email engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique email identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Email properties',
                                'properties': {
                                    'hs_email_subject': {
                                        'type': ['string', 'null'],
                                        'description': 'Subject line of the email',
                                    },
                                    'hs_email_text': {
                                        'type': ['string', 'null'],
                                        'description': 'Plain text body of the email',
                                    },
                                    'hs_email_html': {
                                        'type': ['string', 'null'],
                                        'description': 'HTML body of the email',
                                    },
                                    'hs_email_direction': {
                                        'type': ['string', 'null'],
                                        'description': 'Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)',
                                    },
                                    'hs_email_status': {
                                        'type': ['string', 'null'],
                                        'description': 'Status of the email (e.g., BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)',
                                    },
                                    'hs_email_sender_email': {
                                        'type': ['string', 'null'],
                                        'description': 'Sender email address',
                                    },
                                    'hs_email_to_email': {
                                        'type': ['string', 'null'],
                                        'description': 'Recipient email address(es)',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the email activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the email owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the email was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the email is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the email was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'emails',
                        'x-airbyte-stream-name': 'engagements_emails',
                        'x-airbyte-ai-hints': {
                            'summary': 'Email engagements logged in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, logging, updating, or deleting email records on CRM objects',
                            'trigger_phrases': [
                                'log email',
                                'create email',
                                'record email',
                                'email to contact',
                                'email on deal',
                                'list emails',
                                'get email',
                                'delete email',
                                'remove email',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/crm/v3/objects/emails/{emailId}',
                    action=Action.DELETE,
                    description='Archive an email by ID. This is a soft delete — the email is moved to the\nrecycle bin and can be restored for approximately 90 days. No public\nhard-delete endpoint exists.\n',
                    path_params=['emailId'],
                    path_params_schema={
                        'emailId': {'type': 'string', 'required': True},
                    },
                    no_content_response=True,
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/crm/v3/objects/emails/{emailId}',
                    action=Action.UPDATE,
                    description="Update an existing email's properties by ID.",
                    body_fields=['properties'],
                    path_params=['emailId'],
                    path_params_schema={
                        'emailId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing email. Only provided properties will be updated.',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Email properties to update',
                                'properties': {
                                    'hs_email_subject': {'type': 'string', 'description': 'Subject line of the email'},
                                    'hs_email_text': {'type': 'string', 'description': 'Plain text body of the email'},
                                    'hs_email_html': {'type': 'string', 'description': 'HTML body of the email'},
                                    'hs_email_direction': {'type': 'string', 'description': 'Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)'},
                                    'hs_email_status': {'type': 'string', 'description': 'Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)'},
                                    'hs_timestamp': {'type': 'string', 'description': 'Timestamp when the email activity occurred'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this email'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot email engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique email identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Email properties',
                                'properties': {
                                    'hs_email_subject': {
                                        'type': ['string', 'null'],
                                        'description': 'Subject line of the email',
                                    },
                                    'hs_email_text': {
                                        'type': ['string', 'null'],
                                        'description': 'Plain text body of the email',
                                    },
                                    'hs_email_html': {
                                        'type': ['string', 'null'],
                                        'description': 'HTML body of the email',
                                    },
                                    'hs_email_direction': {
                                        'type': ['string', 'null'],
                                        'description': 'Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)',
                                    },
                                    'hs_email_status': {
                                        'type': ['string', 'null'],
                                        'description': 'Status of the email (e.g., BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)',
                                    },
                                    'hs_email_sender_email': {
                                        'type': ['string', 'null'],
                                        'description': 'Sender email address',
                                    },
                                    'hs_email_to_email': {
                                        'type': ['string', 'null'],
                                        'description': 'Recipient email address(es)',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the email activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the email owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the email was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the email is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the email was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'emails',
                        'x-airbyte-stream-name': 'engagements_emails',
                        'x-airbyte-ai-hints': {
                            'summary': 'Email engagements logged in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, logging, updating, or deleting email records on CRM objects',
                            'trigger_phrases': [
                                'log email',
                                'create email',
                                'record email',
                                'email to contact',
                                'email on deal',
                                'list emails',
                                'get email',
                                'delete email',
                                'remove email',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'HubSpot email engagement object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique email identifier'},
                    'properties': {
                        'type': 'object',
                        'description': 'Email properties',
                        'properties': {
                            'hs_email_subject': {
                                'type': ['string', 'null'],
                                'description': 'Subject line of the email',
                            },
                            'hs_email_text': {
                                'type': ['string', 'null'],
                                'description': 'Plain text body of the email',
                            },
                            'hs_email_html': {
                                'type': ['string', 'null'],
                                'description': 'HTML body of the email',
                            },
                            'hs_email_direction': {
                                'type': ['string', 'null'],
                                'description': 'Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)',
                            },
                            'hs_email_status': {
                                'type': ['string', 'null'],
                                'description': 'Status of the email (e.g., BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)',
                            },
                            'hs_email_sender_email': {
                                'type': ['string', 'null'],
                                'description': 'Sender email address',
                            },
                            'hs_email_to_email': {
                                'type': ['string', 'null'],
                                'description': 'Recipient email address(es)',
                            },
                            'hs_timestamp': {
                                'type': ['string', 'null'],
                                'description': 'Timestamp when the email activity occurred',
                            },
                            'hubspot_owner_id': {
                                'type': ['string', 'null'],
                                'description': 'ID of the email owner',
                            },
                            'hs_object_id': {
                                'type': ['string', 'null'],
                                'description': 'HubSpot object ID',
                            },
                            'hs_createdate': {
                                'type': ['string', 'null'],
                                'description': 'Date the email was created',
                            },
                            'hs_lastmodifieddate': {
                                'type': ['string', 'null'],
                                'description': 'Last modified date',
                            },
                        },
                        'additionalProperties': True,
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the email is archived'},
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the email was archived',
                    },
                    'associations': {
                        'type': ['object', 'null'],
                        'description': 'Relationships with other CRM objects',
                        'additionalProperties': True,
                    },
                },
                'x-airbyte-entity-name': 'emails',
                'x-airbyte-stream-name': 'engagements_emails',
                'x-airbyte-ai-hints': {
                    'summary': 'Email engagements logged in the CRM (contacts, companies, deals, tickets)',
                    'when_to_use': 'Listing, viewing, logging, updating, or deleting email records on CRM objects',
                    'trigger_phrases': [
                        'log email',
                        'create email',
                        'record email',
                        'email to contact',
                        'email on deal',
                        'list emails',
                        'get email',
                        'delete email',
                        'remove email',
                    ],
                    'freshness': 'live',
                },
            },
            ai_hints={
                'summary': 'Email engagements logged in the CRM (contacts, companies, deals, tickets)',
                'when_to_use': 'Listing, viewing, logging, updating, or deleting email records on CRM objects',
                'trigger_phrases': [
                    'log email',
                    'create email',
                    'record email',
                    'email to contact',
                    'email on deal',
                    'list emails',
                    'get email',
                    'delete email',
                    'remove email',
                ],
                'freshness': 'live',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='emails',
                    target_entity='contacts',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='emails',
                    target_entity='companies',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='emails',
                    target_entity='deals',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='emails',
                    target_entity='tickets',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
            ],
        ),
        EntityDefinition(
            name='meetings',
            stream_name='engagements_meetings',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.DELETE,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/meetings',
                    action=Action.LIST,
                    description='Returns a paginated list of meetings',
                    query_params=[
                        'limit',
                        'after',
                        'associations',
                        'properties',
                        'propertiesWithHistory',
                        'archived',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of meetings',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot meeting engagement object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique meeting identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Meeting properties',
                                            'properties': {
                                                'hs_meeting_title': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Title of the meeting',
                                                },
                                                'hs_meeting_body': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Description or notes about the meeting',
                                                },
                                                'hs_meeting_start_time': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Start time of the meeting (ISO 8601 format)',
                                                },
                                                'hs_meeting_end_time': {
                                                    'type': ['string', 'null'],
                                                    'description': 'End time of the meeting (ISO 8601 format)',
                                                },
                                                'hs_meeting_location': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Location of the meeting',
                                                },
                                                'hs_meeting_outcome': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)',
                                                },
                                                'hs_internal_meeting_notes': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Internal notes about the meeting',
                                                },
                                                'hs_timestamp': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Timestamp when the meeting activity occurred',
                                                },
                                                'hubspot_owner_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'ID of the meeting owner',
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'HubSpot object ID',
                                                },
                                                'hs_createdate': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Date the meeting was created',
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Last modified date',
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the meeting is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the meeting was archived',
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'x-airbyte-entity-name': 'meetings',
                                    'x-airbyte-stream-name': 'engagements_meetings',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Meeting engagements logged in the CRM (contacts, companies, deals, tickets)',
                                        'when_to_use': 'Listing, viewing, scheduling, updating, or deleting meeting records on CRM objects',
                                        'trigger_phrases': [
                                            'log meeting',
                                            'create meeting',
                                            'schedule meeting',
                                            'meeting with contact',
                                            'meeting on deal',
                                            'list meetings',
                                            'get meeting',
                                            'delete meeting',
                                            'remove meeting',
                                        ],
                                        'freshness': 'live',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/meetings',
                    action=Action.CREATE,
                    description='Create a new meeting engagement in HubSpot CRM. Meetings can be associated with contacts,\ncompanies, deals, or tickets by using the associations parameter.\nThe hs_timestamp property sets when the meeting activity occurred.\n',
                    body_fields=['properties', 'associations'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new meeting',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Meeting properties to set',
                                'required': ['hs_timestamp', 'hs_meeting_title'],
                                'properties': {
                                    'hs_meeting_title': {'type': 'string', 'description': 'Required. Title of the meeting'},
                                    'hs_meeting_body': {'type': 'string', 'description': 'Description or notes about the meeting (supports HTML)'},
                                    'hs_meeting_start_time': {'type': 'string', 'description': 'Start time of the meeting (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z)'},
                                    'hs_meeting_end_time': {'type': 'string', 'description': 'End time of the meeting (ISO 8601 format, e.g. 2025-01-15T11:30:00.000Z)'},
                                    'hs_meeting_location': {'type': 'string', 'description': 'Location of the meeting'},
                                    'hs_meeting_outcome': {'type': 'string', 'description': 'Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)'},
                                    'hs_internal_meeting_notes': {'type': 'string', 'description': 'Internal notes about the meeting'},
                                    'hs_timestamp': {'type': 'string', 'description': 'Required. Timestamp when the meeting activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one.'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this meeting'},
                                },
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': 'array',
                                'description': 'Associate the meeting with other CRM records (contacts, companies, deals, tickets)',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'to': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'ID of the record to associate with'},
                                            },
                                        },
                                        'types': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'associationCategory': {'type': 'string', 'description': 'Association category (e.g., HUBSPOT_DEFINED)'},
                                                    'associationTypeId': {'type': 'integer', 'description': 'Association type ID (e.g., 200 for meeting-to-contact, 188 for meeting-to-company, 212 for meeting-to-deal, 226 for meeting-to-ticket)'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot meeting engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique meeting identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Meeting properties',
                                'properties': {
                                    'hs_meeting_title': {
                                        'type': ['string', 'null'],
                                        'description': 'Title of the meeting',
                                    },
                                    'hs_meeting_body': {
                                        'type': ['string', 'null'],
                                        'description': 'Description or notes about the meeting',
                                    },
                                    'hs_meeting_start_time': {
                                        'type': ['string', 'null'],
                                        'description': 'Start time of the meeting (ISO 8601 format)',
                                    },
                                    'hs_meeting_end_time': {
                                        'type': ['string', 'null'],
                                        'description': 'End time of the meeting (ISO 8601 format)',
                                    },
                                    'hs_meeting_location': {
                                        'type': ['string', 'null'],
                                        'description': 'Location of the meeting',
                                    },
                                    'hs_meeting_outcome': {
                                        'type': ['string', 'null'],
                                        'description': 'Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)',
                                    },
                                    'hs_internal_meeting_notes': {
                                        'type': ['string', 'null'],
                                        'description': 'Internal notes about the meeting',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the meeting activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the meeting owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the meeting was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the meeting is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the meeting was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'meetings',
                        'x-airbyte-stream-name': 'engagements_meetings',
                        'x-airbyte-ai-hints': {
                            'summary': 'Meeting engagements logged in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, scheduling, updating, or deleting meeting records on CRM objects',
                            'trigger_phrases': [
                                'log meeting',
                                'create meeting',
                                'schedule meeting',
                                'meeting with contact',
                                'meeting on deal',
                                'list meetings',
                                'get meeting',
                                'delete meeting',
                                'remove meeting',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/meetings/{meetingId}',
                    action=Action.GET,
                    description='Get a single meeting by ID',
                    query_params=[
                        'properties',
                        'propertiesWithHistory',
                        'associations',
                        'idProperty',
                        'archived',
                    ],
                    query_params_schema={
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'idProperty': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['meetingId'],
                    path_params_schema={
                        'meetingId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot meeting engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique meeting identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Meeting properties',
                                'properties': {
                                    'hs_meeting_title': {
                                        'type': ['string', 'null'],
                                        'description': 'Title of the meeting',
                                    },
                                    'hs_meeting_body': {
                                        'type': ['string', 'null'],
                                        'description': 'Description or notes about the meeting',
                                    },
                                    'hs_meeting_start_time': {
                                        'type': ['string', 'null'],
                                        'description': 'Start time of the meeting (ISO 8601 format)',
                                    },
                                    'hs_meeting_end_time': {
                                        'type': ['string', 'null'],
                                        'description': 'End time of the meeting (ISO 8601 format)',
                                    },
                                    'hs_meeting_location': {
                                        'type': ['string', 'null'],
                                        'description': 'Location of the meeting',
                                    },
                                    'hs_meeting_outcome': {
                                        'type': ['string', 'null'],
                                        'description': 'Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)',
                                    },
                                    'hs_internal_meeting_notes': {
                                        'type': ['string', 'null'],
                                        'description': 'Internal notes about the meeting',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the meeting activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the meeting owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the meeting was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the meeting is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the meeting was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'meetings',
                        'x-airbyte-stream-name': 'engagements_meetings',
                        'x-airbyte-ai-hints': {
                            'summary': 'Meeting engagements logged in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, scheduling, updating, or deleting meeting records on CRM objects',
                            'trigger_phrases': [
                                'log meeting',
                                'create meeting',
                                'schedule meeting',
                                'meeting with contact',
                                'meeting on deal',
                                'list meetings',
                                'get meeting',
                                'delete meeting',
                                'remove meeting',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/crm/v3/objects/meetings/{meetingId}',
                    action=Action.DELETE,
                    description='Archive a meeting by ID. This is a soft delete — the meeting is moved to the\nrecycle bin and can be restored for approximately 90 days. No public\nhard-delete endpoint exists.\n',
                    path_params=['meetingId'],
                    path_params_schema={
                        'meetingId': {'type': 'string', 'required': True},
                    },
                    no_content_response=True,
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/crm/v3/objects/meetings/{meetingId}',
                    action=Action.UPDATE,
                    description="Update an existing meeting's properties by ID.",
                    body_fields=['properties'],
                    path_params=['meetingId'],
                    path_params_schema={
                        'meetingId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing meeting. Only provided properties will be updated.',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Meeting properties to update',
                                'properties': {
                                    'hs_meeting_title': {'type': 'string', 'description': 'Title of the meeting'},
                                    'hs_meeting_body': {'type': 'string', 'description': 'Description or notes about the meeting (supports HTML)'},
                                    'hs_meeting_start_time': {'type': 'string', 'description': 'Start time of the meeting (ISO 8601 format)'},
                                    'hs_meeting_end_time': {'type': 'string', 'description': 'End time of the meeting (ISO 8601 format)'},
                                    'hs_meeting_location': {'type': 'string', 'description': 'Location of the meeting'},
                                    'hs_meeting_outcome': {'type': 'string', 'description': 'Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)'},
                                    'hs_internal_meeting_notes': {'type': 'string', 'description': 'Internal notes about the meeting'},
                                    'hs_timestamp': {'type': 'string', 'description': 'Timestamp when the meeting activity occurred'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this meeting'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot meeting engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique meeting identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Meeting properties',
                                'properties': {
                                    'hs_meeting_title': {
                                        'type': ['string', 'null'],
                                        'description': 'Title of the meeting',
                                    },
                                    'hs_meeting_body': {
                                        'type': ['string', 'null'],
                                        'description': 'Description or notes about the meeting',
                                    },
                                    'hs_meeting_start_time': {
                                        'type': ['string', 'null'],
                                        'description': 'Start time of the meeting (ISO 8601 format)',
                                    },
                                    'hs_meeting_end_time': {
                                        'type': ['string', 'null'],
                                        'description': 'End time of the meeting (ISO 8601 format)',
                                    },
                                    'hs_meeting_location': {
                                        'type': ['string', 'null'],
                                        'description': 'Location of the meeting',
                                    },
                                    'hs_meeting_outcome': {
                                        'type': ['string', 'null'],
                                        'description': 'Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)',
                                    },
                                    'hs_internal_meeting_notes': {
                                        'type': ['string', 'null'],
                                        'description': 'Internal notes about the meeting',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the meeting activity occurred',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the meeting owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the meeting was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the meeting is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the meeting was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'meetings',
                        'x-airbyte-stream-name': 'engagements_meetings',
                        'x-airbyte-ai-hints': {
                            'summary': 'Meeting engagements logged in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, scheduling, updating, or deleting meeting records on CRM objects',
                            'trigger_phrases': [
                                'log meeting',
                                'create meeting',
                                'schedule meeting',
                                'meeting with contact',
                                'meeting on deal',
                                'list meetings',
                                'get meeting',
                                'delete meeting',
                                'remove meeting',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'HubSpot meeting engagement object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique meeting identifier'},
                    'properties': {
                        'type': 'object',
                        'description': 'Meeting properties',
                        'properties': {
                            'hs_meeting_title': {
                                'type': ['string', 'null'],
                                'description': 'Title of the meeting',
                            },
                            'hs_meeting_body': {
                                'type': ['string', 'null'],
                                'description': 'Description or notes about the meeting',
                            },
                            'hs_meeting_start_time': {
                                'type': ['string', 'null'],
                                'description': 'Start time of the meeting (ISO 8601 format)',
                            },
                            'hs_meeting_end_time': {
                                'type': ['string', 'null'],
                                'description': 'End time of the meeting (ISO 8601 format)',
                            },
                            'hs_meeting_location': {
                                'type': ['string', 'null'],
                                'description': 'Location of the meeting',
                            },
                            'hs_meeting_outcome': {
                                'type': ['string', 'null'],
                                'description': 'Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)',
                            },
                            'hs_internal_meeting_notes': {
                                'type': ['string', 'null'],
                                'description': 'Internal notes about the meeting',
                            },
                            'hs_timestamp': {
                                'type': ['string', 'null'],
                                'description': 'Timestamp when the meeting activity occurred',
                            },
                            'hubspot_owner_id': {
                                'type': ['string', 'null'],
                                'description': 'ID of the meeting owner',
                            },
                            'hs_object_id': {
                                'type': ['string', 'null'],
                                'description': 'HubSpot object ID',
                            },
                            'hs_createdate': {
                                'type': ['string', 'null'],
                                'description': 'Date the meeting was created',
                            },
                            'hs_lastmodifieddate': {
                                'type': ['string', 'null'],
                                'description': 'Last modified date',
                            },
                        },
                        'additionalProperties': True,
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the meeting is archived'},
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the meeting was archived',
                    },
                    'associations': {
                        'type': ['object', 'null'],
                        'description': 'Relationships with other CRM objects',
                        'additionalProperties': True,
                    },
                },
                'x-airbyte-entity-name': 'meetings',
                'x-airbyte-stream-name': 'engagements_meetings',
                'x-airbyte-ai-hints': {
                    'summary': 'Meeting engagements logged in the CRM (contacts, companies, deals, tickets)',
                    'when_to_use': 'Listing, viewing, scheduling, updating, or deleting meeting records on CRM objects',
                    'trigger_phrases': [
                        'log meeting',
                        'create meeting',
                        'schedule meeting',
                        'meeting with contact',
                        'meeting on deal',
                        'list meetings',
                        'get meeting',
                        'delete meeting',
                        'remove meeting',
                    ],
                    'freshness': 'live',
                },
            },
            ai_hints={
                'summary': 'Meeting engagements logged in the CRM (contacts, companies, deals, tickets)',
                'when_to_use': 'Listing, viewing, scheduling, updating, or deleting meeting records on CRM objects',
                'trigger_phrases': [
                    'log meeting',
                    'create meeting',
                    'schedule meeting',
                    'meeting with contact',
                    'meeting on deal',
                    'list meetings',
                    'get meeting',
                    'delete meeting',
                    'remove meeting',
                ],
                'freshness': 'live',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='meetings',
                    target_entity='contacts',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='meetings',
                    target_entity='companies',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='meetings',
                    target_entity='deals',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='meetings',
                    target_entity='tickets',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
            ],
        ),
        EntityDefinition(
            name='tasks',
            stream_name='engagements_tasks',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.DELETE,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/tasks',
                    action=Action.LIST,
                    description='Returns a paginated list of tasks',
                    query_params=[
                        'limit',
                        'after',
                        'associations',
                        'properties',
                        'propertiesWithHistory',
                        'archived',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'HubSpot task engagement object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique task identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Task properties',
                                            'properties': {
                                                'hs_task_body': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Description or notes for the task (supports HTML)',
                                                },
                                                'hs_task_subject': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Subject or title of the task',
                                                },
                                                'hs_task_status': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Status of the task (e.g., NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)',
                                                },
                                                'hs_task_priority': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Priority of the task (e.g., LOW, MEDIUM, HIGH)',
                                                },
                                                'hs_task_type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of the task (e.g., TODO, CALL, EMAIL)',
                                                },
                                                'hs_task_reminders': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Reminder timestamp for the task (epoch milliseconds)',
                                                },
                                                'hs_timestamp': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Timestamp when the task activity occurred (due date)',
                                                },
                                                'hubspot_owner_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'ID of the task owner',
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'HubSpot object ID',
                                                },
                                                'hs_createdate': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Date the task was created',
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Last modified date',
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the task is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the task was archived',
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                    'x-airbyte-stream-name': 'engagements_tasks',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Task engagements in the CRM (contacts, companies, deals, tickets)',
                                        'when_to_use': 'Listing, viewing, creating, updating, or deleting task records on CRM objects',
                                        'trigger_phrases': [
                                            'create task',
                                            'add task',
                                            'assign task',
                                            'task for contact',
                                            'task on deal',
                                            'list tasks',
                                            'get task',
                                            'delete task',
                                            'remove task',
                                            'to-do',
                                        ],
                                        'freshness': 'live',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                            'total': {'type': 'integer', 'description': 'Total number of results (search only)'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/crm/v3/objects/tasks',
                    action=Action.CREATE,
                    description='Create a new task in HubSpot CRM. Tasks can be associated with contacts,\ncompanies, deals, or tickets by using the associations parameter.\nThe hs_timestamp property sets when the task activity occurred.\n',
                    body_fields=['properties', 'associations'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new task',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Task properties to set',
                                'required': ['hs_timestamp', 'hs_task_subject'],
                                'properties': {
                                    'hs_task_body': {'type': 'string', 'description': 'Description or notes for the task (supports HTML)'},
                                    'hs_task_subject': {'type': 'string', 'description': 'Required. Subject or title of the task'},
                                    'hs_task_status': {'type': 'string', 'description': 'Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED). Defaults to NOT_STARTED.'},
                                    'hs_task_priority': {'type': 'string', 'description': 'Priority of the task (LOW, MEDIUM, HIGH)'},
                                    'hs_task_type': {'type': 'string', 'description': 'Type of the task (TODO, CALL, EMAIL). Defaults to TODO.'},
                                    'hs_task_reminders': {'type': 'string', 'description': 'Reminder timestamp for the task (epoch milliseconds)'},
                                    'hs_timestamp': {'type': 'string', 'description': 'Required. Due date / timestamp for the task (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one.'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this task'},
                                },
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': 'array',
                                'description': 'Associate the task with other CRM records (contacts, companies, deals, tickets)',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'to': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'ID of the record to associate with'},
                                            },
                                        },
                                        'types': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'associationCategory': {'type': 'string', 'description': 'Association category (e.g., HUBSPOT_DEFINED)'},
                                                    'associationTypeId': {'type': 'integer', 'description': 'Association type ID (e.g., 204 for task-to-contact, 192 for task-to-company, 216 for task-to-deal, 228 for task-to-ticket)'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot task engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique task identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Task properties',
                                'properties': {
                                    'hs_task_body': {
                                        'type': ['string', 'null'],
                                        'description': 'Description or notes for the task (supports HTML)',
                                    },
                                    'hs_task_subject': {
                                        'type': ['string', 'null'],
                                        'description': 'Subject or title of the task',
                                    },
                                    'hs_task_status': {
                                        'type': ['string', 'null'],
                                        'description': 'Status of the task (e.g., NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)',
                                    },
                                    'hs_task_priority': {
                                        'type': ['string', 'null'],
                                        'description': 'Priority of the task (e.g., LOW, MEDIUM, HIGH)',
                                    },
                                    'hs_task_type': {
                                        'type': ['string', 'null'],
                                        'description': 'Type of the task (e.g., TODO, CALL, EMAIL)',
                                    },
                                    'hs_task_reminders': {
                                        'type': ['string', 'null'],
                                        'description': 'Reminder timestamp for the task (epoch milliseconds)',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the task activity occurred (due date)',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the task owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the task was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the task is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the task was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'tasks',
                        'x-airbyte-stream-name': 'engagements_tasks',
                        'x-airbyte-ai-hints': {
                            'summary': 'Task engagements in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, creating, updating, or deleting task records on CRM objects',
                            'trigger_phrases': [
                                'create task',
                                'add task',
                                'assign task',
                                'task for contact',
                                'task on deal',
                                'list tasks',
                                'get task',
                                'delete task',
                                'remove task',
                                'to-do',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/tasks/{taskId}',
                    action=Action.GET,
                    description='Get a single task by ID',
                    query_params=[
                        'properties',
                        'propertiesWithHistory',
                        'associations',
                        'idProperty',
                        'archived',
                    ],
                    query_params_schema={
                        'properties': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'idProperty': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['taskId'],
                    path_params_schema={
                        'taskId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot task engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique task identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Task properties',
                                'properties': {
                                    'hs_task_body': {
                                        'type': ['string', 'null'],
                                        'description': 'Description or notes for the task (supports HTML)',
                                    },
                                    'hs_task_subject': {
                                        'type': ['string', 'null'],
                                        'description': 'Subject or title of the task',
                                    },
                                    'hs_task_status': {
                                        'type': ['string', 'null'],
                                        'description': 'Status of the task (e.g., NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)',
                                    },
                                    'hs_task_priority': {
                                        'type': ['string', 'null'],
                                        'description': 'Priority of the task (e.g., LOW, MEDIUM, HIGH)',
                                    },
                                    'hs_task_type': {
                                        'type': ['string', 'null'],
                                        'description': 'Type of the task (e.g., TODO, CALL, EMAIL)',
                                    },
                                    'hs_task_reminders': {
                                        'type': ['string', 'null'],
                                        'description': 'Reminder timestamp for the task (epoch milliseconds)',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the task activity occurred (due date)',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the task owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the task was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the task is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the task was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'tasks',
                        'x-airbyte-stream-name': 'engagements_tasks',
                        'x-airbyte-ai-hints': {
                            'summary': 'Task engagements in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, creating, updating, or deleting task records on CRM objects',
                            'trigger_phrases': [
                                'create task',
                                'add task',
                                'assign task',
                                'task for contact',
                                'task on deal',
                                'list tasks',
                                'get task',
                                'delete task',
                                'remove task',
                                'to-do',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/crm/v3/objects/tasks/{taskId}',
                    action=Action.DELETE,
                    description='Archive a task by ID. This is a soft delete — the task is moved to the\nrecycle bin and can be restored for approximately 90 days. No public\nhard-delete endpoint exists.\n',
                    path_params=['taskId'],
                    path_params_schema={
                        'taskId': {'type': 'string', 'required': True},
                    },
                    no_content_response=True,
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/crm/v3/objects/tasks/{taskId}',
                    action=Action.UPDATE,
                    description="Update an existing task's properties by ID.",
                    body_fields=['properties'],
                    path_params=['taskId'],
                    path_params_schema={
                        'taskId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing task. Only provided properties will be updated.',
                        'properties': {
                            'properties': {
                                'type': 'object',
                                'description': 'Task properties to update',
                                'properties': {
                                    'hs_task_body': {'type': 'string', 'description': 'Description or notes for the task (supports HTML)'},
                                    'hs_task_subject': {'type': 'string', 'description': 'Subject or title of the task'},
                                    'hs_task_status': {'type': 'string', 'description': 'Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)'},
                                    'hs_task_priority': {'type': 'string', 'description': 'Priority of the task (LOW, MEDIUM, HIGH)'},
                                    'hs_task_type': {'type': 'string', 'description': 'Type of the task (TODO, CALL, EMAIL)'},
                                    'hs_task_reminders': {'type': 'string', 'description': 'Reminder timestamp for the task (epoch milliseconds)'},
                                    'hs_timestamp': {'type': 'string', 'description': 'Due date / timestamp for the task'},
                                    'hubspot_owner_id': {'type': 'string', 'description': 'ID of the HubSpot owner to assign to this task'},
                                },
                                'additionalProperties': True,
                            },
                        },
                        'required': ['properties'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'HubSpot task engagement object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique task identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Task properties',
                                'properties': {
                                    'hs_task_body': {
                                        'type': ['string', 'null'],
                                        'description': 'Description or notes for the task (supports HTML)',
                                    },
                                    'hs_task_subject': {
                                        'type': ['string', 'null'],
                                        'description': 'Subject or title of the task',
                                    },
                                    'hs_task_status': {
                                        'type': ['string', 'null'],
                                        'description': 'Status of the task (e.g., NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)',
                                    },
                                    'hs_task_priority': {
                                        'type': ['string', 'null'],
                                        'description': 'Priority of the task (e.g., LOW, MEDIUM, HIGH)',
                                    },
                                    'hs_task_type': {
                                        'type': ['string', 'null'],
                                        'description': 'Type of the task (e.g., TODO, CALL, EMAIL)',
                                    },
                                    'hs_task_reminders': {
                                        'type': ['string', 'null'],
                                        'description': 'Reminder timestamp for the task (epoch milliseconds)',
                                    },
                                    'hs_timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'Timestamp when the task activity occurred (due date)',
                                    },
                                    'hubspot_owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'ID of the task owner',
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                        'description': 'HubSpot object ID',
                                    },
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the task was created',
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                        'description': 'Last modified date',
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the task is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the task was archived',
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                        },
                        'x-airbyte-entity-name': 'tasks',
                        'x-airbyte-stream-name': 'engagements_tasks',
                        'x-airbyte-ai-hints': {
                            'summary': 'Task engagements in the CRM (contacts, companies, deals, tickets)',
                            'when_to_use': 'Listing, viewing, creating, updating, or deleting task records on CRM objects',
                            'trigger_phrases': [
                                'create task',
                                'add task',
                                'assign task',
                                'task for contact',
                                'task on deal',
                                'list tasks',
                                'get task',
                                'delete task',
                                'remove task',
                                'to-do',
                            ],
                            'freshness': 'live',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'HubSpot task engagement object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique task identifier'},
                    'properties': {
                        'type': 'object',
                        'description': 'Task properties',
                        'properties': {
                            'hs_task_body': {
                                'type': ['string', 'null'],
                                'description': 'Description or notes for the task (supports HTML)',
                            },
                            'hs_task_subject': {
                                'type': ['string', 'null'],
                                'description': 'Subject or title of the task',
                            },
                            'hs_task_status': {
                                'type': ['string', 'null'],
                                'description': 'Status of the task (e.g., NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)',
                            },
                            'hs_task_priority': {
                                'type': ['string', 'null'],
                                'description': 'Priority of the task (e.g., LOW, MEDIUM, HIGH)',
                            },
                            'hs_task_type': {
                                'type': ['string', 'null'],
                                'description': 'Type of the task (e.g., TODO, CALL, EMAIL)',
                            },
                            'hs_task_reminders': {
                                'type': ['string', 'null'],
                                'description': 'Reminder timestamp for the task (epoch milliseconds)',
                            },
                            'hs_timestamp': {
                                'type': ['string', 'null'],
                                'description': 'Timestamp when the task activity occurred (due date)',
                            },
                            'hubspot_owner_id': {
                                'type': ['string', 'null'],
                                'description': 'ID of the task owner',
                            },
                            'hs_object_id': {
                                'type': ['string', 'null'],
                                'description': 'HubSpot object ID',
                            },
                            'hs_createdate': {
                                'type': ['string', 'null'],
                                'description': 'Date the task was created',
                            },
                            'hs_lastmodifieddate': {
                                'type': ['string', 'null'],
                                'description': 'Last modified date',
                            },
                        },
                        'additionalProperties': True,
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the task is archived'},
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the task was archived',
                    },
                    'associations': {
                        'type': ['object', 'null'],
                        'description': 'Relationships with other CRM objects',
                        'additionalProperties': True,
                    },
                },
                'x-airbyte-entity-name': 'tasks',
                'x-airbyte-stream-name': 'engagements_tasks',
                'x-airbyte-ai-hints': {
                    'summary': 'Task engagements in the CRM (contacts, companies, deals, tickets)',
                    'when_to_use': 'Listing, viewing, creating, updating, or deleting task records on CRM objects',
                    'trigger_phrases': [
                        'create task',
                        'add task',
                        'assign task',
                        'task for contact',
                        'task on deal',
                        'list tasks',
                        'get task',
                        'delete task',
                        'remove task',
                        'to-do',
                    ],
                    'freshness': 'live',
                },
            },
            ai_hints={
                'summary': 'Task engagements in the CRM (contacts, companies, deals, tickets)',
                'when_to_use': 'Listing, viewing, creating, updating, or deleting task records on CRM objects',
                'trigger_phrases': [
                    'create task',
                    'add task',
                    'assign task',
                    'task for contact',
                    'task on deal',
                    'list tasks',
                    'get task',
                    'delete task',
                    'remove task',
                    'to-do',
                ],
                'freshness': 'live',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='tasks',
                    target_entity='contacts',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='tasks',
                    target_entity='companies',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='tasks',
                    target_entity='deals',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
                EntityRelationshipConfig(
                    source_entity='tasks',
                    target_entity='tickets',
                    foreign_key='associations',
                    cardinality='many_to_many',
                ),
            ],
        ),
        EntityDefinition(
            name='schemas',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm-object-schemas/v3/schemas',
                    action=Action.LIST,
                    description='Returns all custom object schemas to discover available custom objects',
                    query_params=['archived'],
                    query_params_schema={
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'List of custom object schemas',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Custom object schema definition',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Schema ID'},
                                        'name': {'type': 'string', 'description': 'Schema name'},
                                        'labels': {
                                            'type': 'object',
                                            'description': 'Display labels',
                                            'properties': {
                                                'singular': {'type': 'string'},
                                                'plural': {'type': 'string'},
                                            },
                                        },
                                        'objectTypeId': {'type': 'string', 'description': 'Object type identifier'},
                                        'fullyQualifiedName': {'type': 'string', 'description': 'Fully qualified name (p{portal_id}_{object_name})'},
                                        'requiredProperties': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                        },
                                        'searchableProperties': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                        },
                                        'primaryDisplayProperty': {'type': 'string'},
                                        'secondaryDisplayProperties': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'allowsSensitiveProperties': {'type': 'boolean'},
                                        'archived': {'type': 'boolean'},
                                        'restorable': {'type': 'boolean'},
                                        'metaType': {'type': 'string'},
                                        'createdByUserId': {'type': 'integer'},
                                        'updatedByUserId': {'type': 'integer'},
                                        'properties': {
                                            'type': 'array',
                                            'description': 'Schema properties',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {'type': 'string'},
                                                    'label': {'type': 'string'},
                                                    'type': {'type': 'string'},
                                                    'fieldType': {'type': 'string'},
                                                    'description': {'type': 'string'},
                                                    'groupName': {'type': 'string'},
                                                    'displayOrder': {'type': 'integer'},
                                                    'calculated': {'type': 'boolean'},
                                                    'externalOptions': {'type': 'boolean'},
                                                    'archived': {'type': 'boolean'},
                                                    'hasUniqueValue': {'type': 'boolean'},
                                                    'hidden': {'type': 'boolean'},
                                                    'formField': {'type': 'boolean'},
                                                    'dataSensitivity': {'type': 'string'},
                                                    'hubspotDefined': {'type': 'boolean'},
                                                    'updatedAt': {'type': 'string'},
                                                    'createdAt': {'type': 'string'},
                                                    'options': {'type': 'array'},
                                                    'createdUserId': {'type': 'string'},
                                                    'updatedUserId': {'type': 'string'},
                                                    'showCurrencySymbol': {'type': 'boolean'},
                                                    'modificationMetadata': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'archivable': {'type': 'boolean'},
                                                            'readOnlyDefinition': {'type': 'boolean'},
                                                            'readOnlyValue': {'type': 'boolean'},
                                                            'readOnlyOptions': {'type': 'boolean'},
                                                        },
                                                        'additionalProperties': True,
                                                    },
                                                },
                                                'additionalProperties': True,
                                            },
                                        },
                                        'associations': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'fromObjectTypeId': {'type': 'string'},
                                                    'toObjectTypeId': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'cardinality': {'type': 'string'},
                                                    'id': {'type': 'string'},
                                                    'inverseCardinality': {'type': 'string'},
                                                    'hasUserEnforcedMaxToObjectIds': {'type': 'boolean'},
                                                    'hasUserEnforcedMaxFromObjectIds': {'type': 'boolean'},
                                                    'maxToObjectIds': {'type': 'integer'},
                                                    'maxFromObjectIds': {'type': 'integer'},
                                                    'createdAt': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'updatedAt': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                                'additionalProperties': True,
                                            },
                                        },
                                        'createdAt': {'type': 'string', 'format': 'date-time'},
                                        'updatedAt': {'type': 'string', 'format': 'date-time'},
                                    },
                                    'x-airbyte-entity-name': 'schemas',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom object schema definitions in HubSpot',
                                        'when_to_use': 'Looking up custom object structures or schema definitions',
                                        'trigger_phrases': ['custom object schema', 'object definition', 'hubspot schema'],
                                        'freshness': 'static',
                                        'example_questions': ['What custom objects are defined in HubSpot?'],
                                        'search_strategy': 'List all schema definitions',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    no_pagination='HubSpot GET /crm-object-schemas/v3/schemas returns all custom object schemas defined on the portal in a single response; unlike the paged CRM object endpoints this discovery endpoint exposes no paging.next cursor or after token.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm-object-schemas/v3/schemas/{objectType}',
                    action=Action.GET,
                    description='Get the schema for a specific custom object type',
                    path_params=['objectType'],
                    path_params_schema={
                        'objectType': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Custom object schema definition',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Schema ID'},
                            'name': {'type': 'string', 'description': 'Schema name'},
                            'labels': {
                                'type': 'object',
                                'description': 'Display labels',
                                'properties': {
                                    'singular': {'type': 'string'},
                                    'plural': {'type': 'string'},
                                },
                            },
                            'objectTypeId': {'type': 'string', 'description': 'Object type identifier'},
                            'fullyQualifiedName': {'type': 'string', 'description': 'Fully qualified name (p{portal_id}_{object_name})'},
                            'requiredProperties': {
                                'type': 'array',
                                'items': {'type': 'string'},
                            },
                            'searchableProperties': {
                                'type': 'array',
                                'items': {'type': 'string'},
                            },
                            'primaryDisplayProperty': {'type': 'string'},
                            'secondaryDisplayProperties': {
                                'type': 'array',
                                'items': {'type': 'string'},
                            },
                            'description': {
                                'type': ['string', 'null'],
                            },
                            'allowsSensitiveProperties': {'type': 'boolean'},
                            'archived': {'type': 'boolean'},
                            'restorable': {'type': 'boolean'},
                            'metaType': {'type': 'string'},
                            'createdByUserId': {'type': 'integer'},
                            'updatedByUserId': {'type': 'integer'},
                            'properties': {
                                'type': 'array',
                                'description': 'Schema properties',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                        'label': {'type': 'string'},
                                        'type': {'type': 'string'},
                                        'fieldType': {'type': 'string'},
                                        'description': {'type': 'string'},
                                        'groupName': {'type': 'string'},
                                        'displayOrder': {'type': 'integer'},
                                        'calculated': {'type': 'boolean'},
                                        'externalOptions': {'type': 'boolean'},
                                        'archived': {'type': 'boolean'},
                                        'hasUniqueValue': {'type': 'boolean'},
                                        'hidden': {'type': 'boolean'},
                                        'formField': {'type': 'boolean'},
                                        'dataSensitivity': {'type': 'string'},
                                        'hubspotDefined': {'type': 'boolean'},
                                        'updatedAt': {'type': 'string'},
                                        'createdAt': {'type': 'string'},
                                        'options': {'type': 'array'},
                                        'createdUserId': {'type': 'string'},
                                        'updatedUserId': {'type': 'string'},
                                        'showCurrencySymbol': {'type': 'boolean'},
                                        'modificationMetadata': {
                                            'type': 'object',
                                            'properties': {
                                                'archivable': {'type': 'boolean'},
                                                'readOnlyDefinition': {'type': 'boolean'},
                                                'readOnlyValue': {'type': 'boolean'},
                                                'readOnlyOptions': {'type': 'boolean'},
                                            },
                                            'additionalProperties': True,
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                            'associations': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'fromObjectTypeId': {'type': 'string'},
                                        'toObjectTypeId': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'cardinality': {'type': 'string'},
                                        'id': {'type': 'string'},
                                        'inverseCardinality': {'type': 'string'},
                                        'hasUserEnforcedMaxToObjectIds': {'type': 'boolean'},
                                        'hasUserEnforcedMaxFromObjectIds': {'type': 'boolean'},
                                        'maxToObjectIds': {'type': 'integer'},
                                        'maxFromObjectIds': {'type': 'integer'},
                                        'createdAt': {
                                            'type': ['string', 'null'],
                                        },
                                        'updatedAt': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                            'createdAt': {'type': 'string', 'format': 'date-time'},
                            'updatedAt': {'type': 'string', 'format': 'date-time'},
                        },
                        'x-airbyte-entity-name': 'schemas',
                        'x-airbyte-ai-hints': {
                            'summary': 'Custom object schema definitions in HubSpot',
                            'when_to_use': 'Looking up custom object structures or schema definitions',
                            'trigger_phrases': ['custom object schema', 'object definition', 'hubspot schema'],
                            'freshness': 'static',
                            'example_questions': ['What custom objects are defined in HubSpot?'],
                            'search_strategy': 'List all schema definitions',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Custom object schema definition',
                'properties': {
                    'id': {'type': 'string', 'description': 'Schema ID'},
                    'name': {'type': 'string', 'description': 'Schema name'},
                    'labels': {
                        'type': 'object',
                        'description': 'Display labels',
                        'properties': {
                            'singular': {'type': 'string'},
                            'plural': {'type': 'string'},
                        },
                    },
                    'objectTypeId': {'type': 'string', 'description': 'Object type identifier'},
                    'fullyQualifiedName': {'type': 'string', 'description': 'Fully qualified name (p{portal_id}_{object_name})'},
                    'requiredProperties': {
                        'type': 'array',
                        'items': {'type': 'string'},
                    },
                    'searchableProperties': {
                        'type': 'array',
                        'items': {'type': 'string'},
                    },
                    'primaryDisplayProperty': {'type': 'string'},
                    'secondaryDisplayProperties': {
                        'type': 'array',
                        'items': {'type': 'string'},
                    },
                    'description': {
                        'type': ['string', 'null'],
                    },
                    'allowsSensitiveProperties': {'type': 'boolean'},
                    'archived': {'type': 'boolean'},
                    'restorable': {'type': 'boolean'},
                    'metaType': {'type': 'string'},
                    'createdByUserId': {'type': 'integer'},
                    'updatedByUserId': {'type': 'integer'},
                    'properties': {
                        'type': 'array',
                        'description': 'Schema properties',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'name': {'type': 'string'},
                                'label': {'type': 'string'},
                                'type': {'type': 'string'},
                                'fieldType': {'type': 'string'},
                                'description': {'type': 'string'},
                                'groupName': {'type': 'string'},
                                'displayOrder': {'type': 'integer'},
                                'calculated': {'type': 'boolean'},
                                'externalOptions': {'type': 'boolean'},
                                'archived': {'type': 'boolean'},
                                'hasUniqueValue': {'type': 'boolean'},
                                'hidden': {'type': 'boolean'},
                                'formField': {'type': 'boolean'},
                                'dataSensitivity': {'type': 'string'},
                                'hubspotDefined': {'type': 'boolean'},
                                'updatedAt': {'type': 'string'},
                                'createdAt': {'type': 'string'},
                                'options': {'type': 'array'},
                                'createdUserId': {'type': 'string'},
                                'updatedUserId': {'type': 'string'},
                                'showCurrencySymbol': {'type': 'boolean'},
                                'modificationMetadata': {
                                    'type': 'object',
                                    'properties': {
                                        'archivable': {'type': 'boolean'},
                                        'readOnlyDefinition': {'type': 'boolean'},
                                        'readOnlyValue': {'type': 'boolean'},
                                        'readOnlyOptions': {'type': 'boolean'},
                                    },
                                    'additionalProperties': True,
                                },
                            },
                            'additionalProperties': True,
                        },
                    },
                    'associations': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'fromObjectTypeId': {'type': 'string'},
                                'toObjectTypeId': {'type': 'string'},
                                'name': {'type': 'string'},
                                'cardinality': {'type': 'string'},
                                'id': {'type': 'string'},
                                'inverseCardinality': {'type': 'string'},
                                'hasUserEnforcedMaxToObjectIds': {'type': 'boolean'},
                                'hasUserEnforcedMaxFromObjectIds': {'type': 'boolean'},
                                'maxToObjectIds': {'type': 'integer'},
                                'maxFromObjectIds': {'type': 'integer'},
                                'createdAt': {
                                    'type': ['string', 'null'],
                                },
                                'updatedAt': {
                                    'type': ['string', 'null'],
                                },
                            },
                            'additionalProperties': True,
                        },
                    },
                    'createdAt': {'type': 'string', 'format': 'date-time'},
                    'updatedAt': {'type': 'string', 'format': 'date-time'},
                },
                'x-airbyte-entity-name': 'schemas',
                'x-airbyte-ai-hints': {
                    'summary': 'Custom object schema definitions in HubSpot',
                    'when_to_use': 'Looking up custom object structures or schema definitions',
                    'trigger_phrases': ['custom object schema', 'object definition', 'hubspot schema'],
                    'freshness': 'static',
                    'example_questions': ['What custom objects are defined in HubSpot?'],
                    'search_strategy': 'List all schema definitions',
                },
            },
            ai_hints={
                'summary': 'Custom object schema definitions in HubSpot',
                'when_to_use': 'Looking up custom object structures or schema definitions',
                'trigger_phrases': ['custom object schema', 'object definition', 'hubspot schema'],
                'freshness': 'static',
                'example_questions': ['What custom objects are defined in HubSpot?'],
                'search_strategy': 'List all schema definitions',
            },
        ),
        EntityDefinition(
            name='objects',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/{objectType}',
                    action=Action.LIST,
                    description='Read a page of objects. Control what is returned via the properties query param.',
                    query_params=[
                        'limit',
                        'after',
                        'properties',
                        'archived',
                        'associations',
                        'propertiesWithHistory',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'archived': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                        'associations': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                    },
                    path_params=['objectType'],
                    path_params_schema={
                        'objectType': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of generic CRM objects',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Generic HubSpot CRM object (for custom objects)',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique object identifier'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Object properties',
                                            'properties': {
                                                'hs_createdate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_lastmodifieddate': {
                                                    'type': ['string', 'null'],
                                                },
                                                'hs_object_id': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'additionalProperties': True,
                                        },
                                        'createdAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the object is archived'},
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the object was archived',
                                        },
                                        'propertiesWithHistory': {
                                            'type': ['object', 'null'],
                                            'description': 'Properties with historical values',
                                            'additionalProperties': True,
                                        },
                                        'associations': {
                                            'type': ['object', 'null'],
                                            'description': 'Relationships with other CRM objects',
                                            'additionalProperties': True,
                                        },
                                        'objectWriteTraceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Trace identifier for write operations',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL to view object in HubSpot',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'objects',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom CRM objects defined in HubSpot',
                                        'when_to_use': 'Querying custom objects or non-standard CRM entities',
                                        'trigger_phrases': ['custom object', 'hubspot object', 'CRM object'],
                                        'freshness': 'live',
                                        'example_questions': ['Show custom objects in HubSpot'],
                                        'search_strategy': 'Filter by object type',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Cursor for next page'},
                                            'link': {'type': 'string', 'description': 'URL for next page'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v3/objects/{objectType}/{objectId}',
                    action=Action.GET,
                    description='Read an Object identified by {objectId}. {objectId} refers to the internal object ID by default, or optionally any unique property value as specified by the idProperty query param. Control what is returned via the properties query param.',
                    query_params=[
                        'properties',
                        'archived',
                        'associations',
                        'idProperty',
                        'propertiesWithHistory',
                    ],
                    query_params_schema={
                        'properties': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                        'associations': {'type': 'string', 'required': False},
                        'idProperty': {'type': 'string', 'required': False},
                        'propertiesWithHistory': {'type': 'string', 'required': False},
                    },
                    path_params=['objectType', 'objectId'],
                    path_params_schema={
                        'objectType': {'type': 'string', 'required': True},
                        'objectId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Generic HubSpot CRM object (for custom objects)',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique object identifier'},
                            'properties': {
                                'type': 'object',
                                'description': 'Object properties',
                                'properties': {
                                    'hs_createdate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_lastmodifieddate': {
                                        'type': ['string', 'null'],
                                    },
                                    'hs_object_id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'additionalProperties': True,
                            },
                            'createdAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updatedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the object is archived'},
                            'archivedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the object was archived',
                            },
                            'propertiesWithHistory': {
                                'type': ['object', 'null'],
                                'description': 'Properties with historical values',
                                'additionalProperties': True,
                            },
                            'associations': {
                                'type': ['object', 'null'],
                                'description': 'Relationships with other CRM objects',
                                'additionalProperties': True,
                            },
                            'objectWriteTraceId': {
                                'type': ['string', 'null'],
                                'description': 'Trace identifier for write operations',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL to view object in HubSpot',
                            },
                        },
                        'x-airbyte-entity-name': 'objects',
                        'x-airbyte-ai-hints': {
                            'summary': 'Custom CRM objects defined in HubSpot',
                            'when_to_use': 'Querying custom objects or non-standard CRM entities',
                            'trigger_phrases': ['custom object', 'hubspot object', 'CRM object'],
                            'freshness': 'live',
                            'example_questions': ['Show custom objects in HubSpot'],
                            'search_strategy': 'Filter by object type',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Generic HubSpot CRM object (for custom objects)',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique object identifier'},
                    'properties': {
                        'type': 'object',
                        'description': 'Object properties',
                        'properties': {
                            'hs_createdate': {
                                'type': ['string', 'null'],
                            },
                            'hs_lastmodifieddate': {
                                'type': ['string', 'null'],
                            },
                            'hs_object_id': {
                                'type': ['string', 'null'],
                            },
                        },
                        'additionalProperties': True,
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the object is archived'},
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the object was archived',
                    },
                    'propertiesWithHistory': {
                        'type': ['object', 'null'],
                        'description': 'Properties with historical values',
                        'additionalProperties': True,
                    },
                    'associations': {
                        'type': ['object', 'null'],
                        'description': 'Relationships with other CRM objects',
                        'additionalProperties': True,
                    },
                    'objectWriteTraceId': {
                        'type': ['string', 'null'],
                        'description': 'Trace identifier for write operations',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'URL to view object in HubSpot',
                    },
                },
                'x-airbyte-entity-name': 'objects',
                'x-airbyte-ai-hints': {
                    'summary': 'Custom CRM objects defined in HubSpot',
                    'when_to_use': 'Querying custom objects or non-standard CRM entities',
                    'trigger_phrases': ['custom object', 'hubspot object', 'CRM object'],
                    'freshness': 'live',
                    'example_questions': ['Show custom objects in HubSpot'],
                    'search_strategy': 'Filter by object type',
                },
            },
            ai_hints={
                'summary': 'Custom CRM objects defined in HubSpot',
                'when_to_use': 'Querying custom objects or non-standard CRM entities',
                'trigger_phrases': ['custom object', 'hubspot object', 'CRM object'],
                'freshness': 'live',
                'example_questions': ['Show custom objects in HubSpot'],
                'search_strategy': 'Filter by object type',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='objects',
                    target_entity='schemas',
                    foreign_key='objectType',
                    target_key='fullyQualifiedName',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='associations',
            actions=[Action.LIST, Action.CREATE, Action.DELETE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v4/objects/{fromObjectType}/{fromObjectId}/associations/{toObjectType}',
                    action=Action.LIST,
                    description='Retrieve all associations between a specific CRM record and a target object type using\nthe v4 associations API. Returns up to 500 associations per call. Use the `after` cursor\nfor pagination when there are more results. For example, retrieve all companies associated\nwith a contact, or all deals associated with a company.\n',
                    query_params=['after', 'limit'],
                    query_params_schema={
                        'after': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                        },
                    },
                    path_params=['fromObjectType', 'fromObjectId', 'toObjectType'],
                    path_params_schema={
                        'fromObjectType': {'type': 'string', 'required': True},
                        'fromObjectId': {'type': 'string', 'required': True},
                        'toObjectType': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of associations for a CRM record',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'description': 'List of associated objects with their association type details',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'toObjectId': {
                                            'type': ['string', 'integer'],
                                            'description': 'ID of the associated target record',
                                        },
                                        'associationTypes': {
                                            'type': 'array',
                                            'description': 'List of association types linking the two records',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'category': {
                                                        'type': 'string',
                                                        'description': 'Category of the association (HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED)',
                                                        'enum': ['HUBSPOT_DEFINED', 'USER_DEFINED', 'INTEGRATOR_DEFINED'],
                                                    },
                                                    'typeId': {'type': 'integer', 'description': 'Numeric identifier for the association type'},
                                                    'label': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Human-readable label for the association type (e.g., "Primary Company")',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'description': 'Pagination information for retrieving additional results',
                                'properties': {
                                    'next': {
                                        'type': 'object',
                                        'description': 'Cursor for the next page of results',
                                        'properties': {
                                            'after': {'type': 'string', 'description': 'Paging cursor token for retrieving the next page'},
                                            'link': {'type': 'string', 'description': 'URL for retrieving the next page of results'},
                                        },
                                        'context': {
                                            'type': 'object',
                                            'description': 'Additional error context',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'associations',
                    },
                    meta_extractor={'next_cursor': '$.paging.next.after', 'next_link': '$.paging.next.link'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='PUT',
                    path='/crm/v4/objects/{fromObjectType}/{fromObjectId}/associations/{toObjectType}/{toObjectId}',
                    action=Action.CREATE,
                    description='Create a labeled association between two CRM records using the v4 associations API.\nLabeled associations carry an association type ID and category that describe the relationship\n(e.g., "Primary Company", "Billing Contact"). This is idempotent — calling it again with the same\nIDs and label has no effect. Use the association type ID and category from the HubSpot association\ndefinitions for the relevant object pair. Common association type IDs include:\n- Contact to Company: 279 (HUBSPOT_DEFINED) for default, 1 (HUBSPOT_DEFINED) for Primary\n- Company to Contact: 280 (HUBSPOT_DEFINED) for default, 2 (HUBSPOT_DEFINED) for Primary\n- Contact to Deal: 4 (HUBSPOT_DEFINED) for default\n- Deal to Contact: 3 (HUBSPOT_DEFINED) for default\n- Deal to Company: 341 (HUBSPOT_DEFINED) for default, 5 (HUBSPOT_DEFINED) for Primary\n- Company to Deal: 342 (HUBSPOT_DEFINED) for default, 6 (HUBSPOT_DEFINED) for Primary\n- Contact to Ticket: 15 (HUBSPOT_DEFINED) for default\n- Ticket to Contact: 16 (HUBSPOT_DEFINED) for default\n- Ticket to Company: 339 (HUBSPOT_DEFINED) for default, 26 (HUBSPOT_DEFINED) for Primary\n- Company to Ticket: 340 (HUBSPOT_DEFINED) for default, 25 (HUBSPOT_DEFINED) for Primary\n',
                    body_fields=['associationCategory', 'associationTypeId'],
                    body_is_array=True,
                    path_params=[
                        'fromObjectType',
                        'fromObjectId',
                        'toObjectType',
                        'toObjectId',
                    ],
                    path_params_schema={
                        'fromObjectType': {'type': 'string', 'required': True},
                        'fromObjectId': {'type': 'string', 'required': True},
                        'toObjectType': {'type': 'string', 'required': True},
                        'toObjectId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'array',
                        'description': 'Array of association type specifications. Each item defines a labeled association type\nto apply between the two records. Multiple labels can be set in a single call.\n',
                        'items': {
                            'type': 'object',
                            'required': ['associationCategory', 'associationTypeId'],
                            'properties': {
                                'associationCategory': {
                                    'type': 'string',
                                    'description': 'Category of the association type. Use HUBSPOT_DEFINED for standard HubSpot association\ntypes (e.g., primary company, default contact-to-deal) or USER_DEFINED for custom\nassociation labels created in your HubSpot portal.\n',
                                    'enum': ['HUBSPOT_DEFINED', 'USER_DEFINED'],
                                },
                                'associationTypeId': {'type': 'integer', 'description': 'Numeric identifier for the association type. Common IDs include:\n279 = Contact to Company (default), 280 = Company to Contact (default),\n4 = Contact to Deal (default), 3 = Deal to Contact (default),\n341 = Deal to Company (default), 342 = Company to Deal (default),\n1 = Contact to Primary Company, 2 = Company to Primary Contact,\n5 = Deal to Primary Company, 6 = Primary Company to Deal,\n15 = Contact to Ticket (default), 16 = Ticket to Contact (default),\n339 = Ticket to Company (default), 340 = Company to Ticket (default),\n26 = Ticket to Primary Company, 25 = Primary Company to Ticket.\nUse the association definitions API to discover additional type IDs.\n'},
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Result of creating an association between two CRM records',
                        'properties': {
                            'status': {'type': 'string', 'description': 'Status of the association operation (e.g., COMPLETE)'},
                            'results': {
                                'type': 'array',
                                'description': 'List of created associations',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'from': {
                                            'type': 'object',
                                            'description': 'The source record of the association',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'ID of the source record'},
                                            },
                                        },
                                        'to': {
                                            'type': 'object',
                                            'description': 'The target record of the association',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'ID of the target record'},
                                            },
                                        },
                                        'associationSpec': {
                                            'type': 'object',
                                            'description': 'Details about the association type',
                                            'properties': {
                                                'associationCategory': {
                                                    'type': 'string',
                                                    'description': 'Category of the association (HUBSPOT_DEFINED or USER_DEFINED)',
                                                    'enum': ['HUBSPOT_DEFINED', 'USER_DEFINED'],
                                                },
                                                'associationTypeId': {'type': 'integer', 'description': 'Numeric ID of the association type'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                            'startedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Timestamp when the operation started',
                            },
                            'completedAt': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Timestamp when the operation completed',
                            },
                            'requestedAt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Timestamp when the operation was requested',
                            },
                        },
                        'x-airbyte-entity-name': 'associations',
                        'x-airbyte-ai-hints': {
                            'summary': 'CRM record associations linking contacts, companies, deals, and tickets',
                            'when_to_use': 'Linking or relating two CRM records, such as associating a contact with a company or a deal with a contact',
                            'trigger_phrases': [
                                'associate',
                                'link records',
                                'connect contact to company',
                                'relate deal to contact',
                                'association',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Associate a contact with a deal', 'Link a company to a ticket'],
                            'search_strategy': 'Specify the from and to object types and record IDs',
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/crm/v4/objects/{fromObjectType}/{fromObjectId}/associations/{toObjectType}/{toObjectId}',
                    action=Action.DELETE,
                    description='Delete all associations between two specific CRM records using the v4 associations API.\nThis removes every association (both default and labeled) between the two specified records.\nThis operation is irreversible — deleted associations must be recreated manually.\n',
                    path_params=[
                        'fromObjectType',
                        'fromObjectId',
                        'toObjectType',
                        'toObjectId',
                    ],
                    path_params_schema={
                        'fromObjectType': {'type': 'string', 'required': True},
                        'fromObjectId': {'type': 'string', 'required': True},
                        'toObjectType': {'type': 'string', 'required': True},
                        'toObjectId': {'type': 'string', 'required': True},
                    },
                    no_content_response=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Result of creating an association between two CRM records',
                'properties': {
                    'status': {'type': 'string', 'description': 'Status of the association operation (e.g., COMPLETE)'},
                    'results': {
                        'type': 'array',
                        'description': 'List of created associations',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'from': {
                                    'type': 'object',
                                    'description': 'The source record of the association',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'ID of the source record'},
                                    },
                                },
                                'to': {
                                    'type': 'object',
                                    'description': 'The target record of the association',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'ID of the target record'},
                                    },
                                },
                                'associationSpec': {
                                    'type': 'object',
                                    'description': 'Details about the association type',
                                    'properties': {
                                        'associationCategory': {
                                            'type': 'string',
                                            'description': 'Category of the association (HUBSPOT_DEFINED or USER_DEFINED)',
                                            'enum': ['HUBSPOT_DEFINED', 'USER_DEFINED'],
                                        },
                                        'associationTypeId': {'type': 'integer', 'description': 'Numeric ID of the association type'},
                                    },
                                },
                            },
                            'additionalProperties': True,
                        },
                    },
                    'startedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Timestamp when the operation started',
                    },
                    'completedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Timestamp when the operation completed',
                    },
                    'requestedAt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Timestamp when the operation was requested',
                    },
                },
                'x-airbyte-entity-name': 'associations',
                'x-airbyte-ai-hints': {
                    'summary': 'CRM record associations linking contacts, companies, deals, and tickets',
                    'when_to_use': 'Linking or relating two CRM records, such as associating a contact with a company or a deal with a contact',
                    'trigger_phrases': [
                        'associate',
                        'link records',
                        'connect contact to company',
                        'relate deal to contact',
                        'association',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Associate a contact with a deal', 'Link a company to a ticket'],
                    'search_strategy': 'Specify the from and to object types and record IDs',
                },
            },
            ai_hints={
                'summary': 'CRM record associations linking contacts, companies, deals, and tickets',
                'when_to_use': 'Linking or relating two CRM records, such as associating a contact with a company or a deal with a contact',
                'trigger_phrases': [
                    'associate',
                    'link records',
                    'connect contact to company',
                    'relate deal to contact',
                    'association',
                ],
                'freshness': 'live',
                'example_questions': ['Associate a contact with a deal', 'Link a company to a ticket'],
                'search_strategy': 'Specify the from and to object types and record IDs',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='associations',
                    target_entity='contacts',
                    foreign_key='fromObjectId',
                    cardinality='many_to_one',
                    description='Associations can link from contacts to other CRM objects',
                ),
                EntityRelationshipConfig(
                    source_entity='associations',
                    target_entity='companies',
                    foreign_key='toObjectId',
                    cardinality='many_to_one',
                    description='Associations can link to companies from other CRM objects',
                ),
                EntityRelationshipConfig(
                    source_entity='associations',
                    target_entity='deals',
                    foreign_key='fromObjectId',
                    cardinality='many_to_one',
                    description='Associations can link from deals to other CRM objects',
                ),
                EntityRelationshipConfig(
                    source_entity='associations',
                    target_entity='tickets',
                    foreign_key='fromObjectId',
                    cardinality='many_to_one',
                    description='Associations can link from tickets to other CRM objects',
                ),
                EntityRelationshipConfig(
                    source_entity='associations',
                    target_entity='schemas',
                    foreign_key='fromObjectType',
                    target_key='fullyQualifiedName',
                    cardinality='many_to_one',
                    description='Association source object type resolves to a CRM object schema',
                ),
                EntityRelationshipConfig(
                    source_entity='associations',
                    target_entity='schemas',
                    foreign_key='toObjectType',
                    target_key='fullyQualifiedName',
                    cardinality='many_to_one',
                    description='Association target object type resolves to a CRM object schema',
                ),
            ],
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
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates whether the company has been deleted and moved to the recycling bin',
                    ),
                    CacheFieldConfig(
                        name='contacts',
                        type=['null', 'array'],
                        description='Associated contact records linked to this company',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the company record was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the company record',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['object'],
                        description='Object containing all property values for the company',
                    ),
                    CacheFieldConfig(
                        name='properties.createdate',
                        x_airbyte_name='properties_createdate',
                        type=['null', 'string'],
                        description='Date the company was created',
                    ),
                    CacheFieldConfig(
                        name='properties.domain',
                        x_airbyte_name='properties_domain',
                        type=['null', 'string'],
                        description='Company domain name',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_lastmodifieddate',
                        x_airbyte_name='properties_hs_lastmodifieddate',
                        type=['null', 'string'],
                        description='Last modified date of the company',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_object_id',
                        x_airbyte_name='properties_hs_object_id',
                        type=['null', 'string'],
                        description='HubSpot object ID',
                    ),
                    CacheFieldConfig(
                        name='properties.hubspot_owner_id',
                        x_airbyte_name='properties_hubspot_owner_id',
                        type=['null', 'string'],
                        description='ID of the HubSpot owner assigned to this company',
                    ),
                    CacheFieldConfig(
                        name='properties.name',
                        x_airbyte_name='properties_name',
                        type=['null', 'string'],
                        description='Company name',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['null', 'string'],
                        description='Timestamp when the company record was last modified',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='contacts',
                suggested=True,
                x_airbyte_name='contacts',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Boolean flag indicating whether the contact has been archived or deleted',
                    ),
                    CacheFieldConfig(
                        name='companies',
                        type=['null', 'array'],
                        description='Associated company records linked to this contact',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp indicating when the contact was first created in the system',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the contact record',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['object'],
                        description='Key-value object storing all contact properties and their values.',
                    ),
                    CacheFieldConfig(
                        name='properties.associatedcompanyid',
                        x_airbyte_name='properties_associatedcompanyid',
                        type=['null', 'string'],
                        description='ID of the associated company',
                    ),
                    CacheFieldConfig(
                        name='properties.createdate',
                        x_airbyte_name='properties_createdate',
                        type=['null', 'string'],
                        description='Date the contact was created',
                    ),
                    CacheFieldConfig(
                        name='properties.email',
                        x_airbyte_name='properties_email',
                        type=['null', 'string'],
                        description='Contact email address',
                    ),
                    CacheFieldConfig(
                        name='properties.firstname',
                        x_airbyte_name='properties_firstname',
                        type=['null', 'string'],
                        description='Contact first name',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_object_id',
                        x_airbyte_name='properties_hs_object_id',
                        type=['null', 'string'],
                        description='HubSpot object ID',
                    ),
                    CacheFieldConfig(
                        name='properties.hubspot_owner_id',
                        x_airbyte_name='properties_hubspot_owner_id',
                        type=['null', 'string'],
                        description='ID of the HubSpot owner assigned to this contact',
                    ),
                    CacheFieldConfig(
                        name='properties.lastmodifieddate',
                        x_airbyte_name='properties_lastmodifieddate',
                        type=['null', 'string'],
                        description='Last modified date of the contact',
                    ),
                    CacheFieldConfig(
                        name='properties.lastname',
                        x_airbyte_name='properties_lastname',
                        type=['null', 'string'],
                        description='Contact last name',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['null', 'string'],
                        description='Timestamp indicating when the contact record was last modified',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='deals',
                suggested=True,
                x_airbyte_name='deals',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates whether the deal has been deleted and moved to the recycling bin',
                    ),
                    CacheFieldConfig(
                        name='companies',
                        type=['null', 'array'],
                        description='Collection of company records associated with the deal',
                    ),
                    CacheFieldConfig(
                        name='contacts',
                        type=['null', 'array'],
                        description='Collection of contact records associated with the deal',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the deal record was originally created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the deal record',
                    ),
                    CacheFieldConfig(
                        name='line_items',
                        type=['null', 'array'],
                        description='Collection of product line items associated with the deal',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['object'],
                        description='Key-value object containing all deal properties and custom fields',
                    ),
                    CacheFieldConfig(
                        name='properties.amount',
                        x_airbyte_name='properties_amount',
                        type=['null', 'string'],
                        description='Deal amount',
                    ),
                    CacheFieldConfig(
                        name='properties.closedate',
                        x_airbyte_name='properties_closedate',
                        type=['null', 'string'],
                        description='Expected close date of the deal',
                    ),
                    CacheFieldConfig(
                        name='properties.createdate',
                        x_airbyte_name='properties_createdate',
                        type=['null', 'string'],
                        description='Date the deal was created',
                    ),
                    CacheFieldConfig(
                        name='properties.dealname',
                        x_airbyte_name='properties_dealname',
                        type=['null', 'string'],
                        description='Deal name',
                    ),
                    CacheFieldConfig(
                        name='properties.dealstage',
                        x_airbyte_name='properties_dealstage',
                        type=['null', 'string'],
                        description='Current deal stage',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_lastmodifieddate',
                        x_airbyte_name='properties_hs_lastmodifieddate',
                        type=['null', 'string'],
                        description='Last modified date of the deal',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_object_id',
                        x_airbyte_name='properties_hs_object_id',
                        type=['null', 'string'],
                        description='HubSpot object ID',
                    ),
                    CacheFieldConfig(
                        name='properties.hubspot_owner_id',
                        x_airbyte_name='properties_hubspot_owner_id',
                        type=['null', 'string'],
                        description='ID of the HubSpot owner assigned to this deal',
                    ),
                    CacheFieldConfig(
                        name='properties.pipeline',
                        x_airbyte_name='properties_pipeline',
                        type=['null', 'string'],
                        description='Deal pipeline',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['null', 'string'],
                        description='Timestamp when the deal record was last modified',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='tickets',
                suggested=True,
                x_airbyte_name='tickets',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates whether the ticket has been deleted and moved to the recycling bin',
                    ),
                    CacheFieldConfig(
                        name='companies',
                        type=['null', 'array'],
                        description='Collection of company records associated with the ticket',
                    ),
                    CacheFieldConfig(
                        name='contacts',
                        type=['null', 'array'],
                        description='Collection of contact records associated with the ticket',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the ticket record was originally created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the ticket record',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['object'],
                        description='Object containing all property values for the ticket',
                    ),
                    CacheFieldConfig(
                        name='properties.content',
                        x_airbyte_name='properties_content',
                        type=['null', 'string'],
                        description='Ticket content/description',
                    ),
                    CacheFieldConfig(
                        name='properties.createdate',
                        x_airbyte_name='properties_createdate',
                        type=['null', 'string'],
                        description='Date the ticket was created',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_lastmodifieddate',
                        x_airbyte_name='properties_hs_lastmodifieddate',
                        type=['null', 'string'],
                        description='Last modified date of the ticket',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_object_id',
                        x_airbyte_name='properties_hs_object_id',
                        type=['null', 'string'],
                        description='HubSpot object ID',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_pipeline',
                        x_airbyte_name='properties_hs_pipeline',
                        type=['null', 'string'],
                        description='Ticket pipeline',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_pipeline_stage',
                        x_airbyte_name='properties_hs_pipeline_stage',
                        type=['null', 'string'],
                        description='Current pipeline stage of the ticket',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_ticket_category',
                        x_airbyte_name='properties_hs_ticket_category',
                        type=['null', 'string'],
                        description='Ticket category',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_ticket_priority',
                        x_airbyte_name='properties_hs_ticket_priority',
                        type=['null', 'string'],
                        description='Ticket priority level',
                    ),
                    CacheFieldConfig(
                        name='properties.subject',
                        x_airbyte_name='properties_subject',
                        type=['null', 'string'],
                        description='Ticket subject line',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['null', 'string'],
                        description='Timestamp when the ticket record was last modified',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='notes',
                x_airbyte_name='engagements_notes',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates whether the note has been archived',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the note was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the note record',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['object'],
                        description='Object containing all property values for the note',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_createdate',
                        x_airbyte_name='properties_hs_createdate',
                        type=['null', 'string'],
                        description='Date the note was created',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_lastmodifieddate',
                        x_airbyte_name='properties_hs_lastmodifieddate',
                        type=['null', 'string'],
                        description='Last modified date of the note',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_note_body',
                        x_airbyte_name='properties_hs_note_body',
                        type=['null', 'string'],
                        description='The body content of the note (supports HTML)',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_object_id',
                        x_airbyte_name='properties_hs_object_id',
                        type=['null', 'string'],
                        description='HubSpot object ID',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_timestamp',
                        x_airbyte_name='properties_hs_timestamp',
                        type=['null', 'string'],
                        description='Timestamp when the note activity occurred',
                    ),
                    CacheFieldConfig(
                        name='properties.hubspot_owner_id',
                        x_airbyte_name='properties_hubspot_owner_id',
                        type=['null', 'string'],
                        description='ID of the note owner',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['null', 'string'],
                        description='Timestamp when the note record was last modified',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='calls',
                x_airbyte_name='engagements_calls',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates whether the call has been archived',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the call was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the call record',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['object'],
                        description='Object containing all property values for the call',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_call_body',
                        x_airbyte_name='properties_hs_call_body',
                        type=['null', 'string'],
                        description='Description or notes about the call',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_call_direction',
                        x_airbyte_name='properties_hs_call_direction',
                        type=['null', 'string'],
                        description='Direction of the call (INBOUND or OUTBOUND)',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_call_duration',
                        x_airbyte_name='properties_hs_call_duration',
                        type=['null', 'string'],
                        description='Duration of the call in milliseconds',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_call_status',
                        x_airbyte_name='properties_hs_call_status',
                        type=['null', 'string'],
                        description='Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_call_title',
                        x_airbyte_name='properties_hs_call_title',
                        type=['null', 'string'],
                        description='Title or subject of the call',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_createdate',
                        x_airbyte_name='properties_hs_createdate',
                        type=['null', 'string'],
                        description='Date the call was created',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_lastmodifieddate',
                        x_airbyte_name='properties_hs_lastmodifieddate',
                        type=['null', 'string'],
                        description='Last modified date of the call',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_object_id',
                        x_airbyte_name='properties_hs_object_id',
                        type=['null', 'string'],
                        description='HubSpot object ID',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_timestamp',
                        x_airbyte_name='properties_hs_timestamp',
                        type=['null', 'string'],
                        description='Timestamp when the call activity occurred',
                    ),
                    CacheFieldConfig(
                        name='properties.hubspot_owner_id',
                        x_airbyte_name='properties_hubspot_owner_id',
                        type=['null', 'string'],
                        description='ID of the call owner',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['null', 'string'],
                        description='Timestamp when the call record was last modified',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='emails',
                x_airbyte_name='engagements_emails',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates whether the email has been archived',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the email was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the email record',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['object'],
                        description='Object containing all property values for the email',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_createdate',
                        x_airbyte_name='properties_hs_createdate',
                        type=['null', 'string'],
                        description='Date the email was created',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_email_direction',
                        x_airbyte_name='properties_hs_email_direction',
                        type=['null', 'string'],
                        description='Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_email_status',
                        x_airbyte_name='properties_hs_email_status',
                        type=['null', 'string'],
                        description='Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_email_subject',
                        x_airbyte_name='properties_hs_email_subject',
                        type=['null', 'string'],
                        description='Subject line of the email',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_email_text',
                        x_airbyte_name='properties_hs_email_text',
                        type=['null', 'string'],
                        description='Plain text body of the email',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_lastmodifieddate',
                        x_airbyte_name='properties_hs_lastmodifieddate',
                        type=['null', 'string'],
                        description='Last modified date of the email',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_object_id',
                        x_airbyte_name='properties_hs_object_id',
                        type=['null', 'string'],
                        description='HubSpot object ID',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_timestamp',
                        x_airbyte_name='properties_hs_timestamp',
                        type=['null', 'string'],
                        description='Timestamp when the email activity occurred',
                    ),
                    CacheFieldConfig(
                        name='properties.hubspot_owner_id',
                        x_airbyte_name='properties_hubspot_owner_id',
                        type=['null', 'string'],
                        description='ID of the email owner',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['null', 'string'],
                        description='Timestamp when the email record was last modified',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='meetings',
                x_airbyte_name='engagements_meetings',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates whether the meeting has been archived',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the meeting was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the meeting record',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['object'],
                        description='Object containing all property values for the meeting',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_createdate',
                        x_airbyte_name='properties_hs_createdate',
                        type=['null', 'string'],
                        description='Date the meeting was created',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_lastmodifieddate',
                        x_airbyte_name='properties_hs_lastmodifieddate',
                        type=['null', 'string'],
                        description='Last modified date of the meeting',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_meeting_body',
                        x_airbyte_name='properties_hs_meeting_body',
                        type=['null', 'string'],
                        description='Description or notes about the meeting',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_meeting_end_time',
                        x_airbyte_name='properties_hs_meeting_end_time',
                        type=['null', 'string'],
                        description='End time of the meeting',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_meeting_location',
                        x_airbyte_name='properties_hs_meeting_location',
                        type=['null', 'string'],
                        description='Location of the meeting',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_meeting_outcome',
                        x_airbyte_name='properties_hs_meeting_outcome',
                        type=['null', 'string'],
                        description='Outcome of the meeting (e.g., SCHEDULED, COMPLETED, NO_SHOW, CANCELED)',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_meeting_start_time',
                        x_airbyte_name='properties_hs_meeting_start_time',
                        type=['null', 'string'],
                        description='Start time of the meeting',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_meeting_title',
                        x_airbyte_name='properties_hs_meeting_title',
                        type=['null', 'string'],
                        description='Title of the meeting',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_object_id',
                        x_airbyte_name='properties_hs_object_id',
                        type=['null', 'string'],
                        description='HubSpot object ID',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_timestamp',
                        x_airbyte_name='properties_hs_timestamp',
                        type=['null', 'string'],
                        description='Timestamp when the meeting activity occurred',
                    ),
                    CacheFieldConfig(
                        name='properties.hubspot_owner_id',
                        x_airbyte_name='properties_hubspot_owner_id',
                        type=['null', 'string'],
                        description='ID of the meeting owner',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['null', 'string'],
                        description='Timestamp when the meeting record was last modified',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='tasks',
                x_airbyte_name='engagements_tasks',
                fields=[
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates whether the task has been archived',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the task was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the task record',
                    ),
                    CacheFieldConfig(
                        name='properties',
                        type=['object'],
                        description='Object containing all property values for the task',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_createdate',
                        x_airbyte_name='properties_hs_createdate',
                        type=['null', 'string'],
                        description='Date the task was created',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_lastmodifieddate',
                        x_airbyte_name='properties_hs_lastmodifieddate',
                        type=['null', 'string'],
                        description='Last modified date of the task',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_object_id',
                        x_airbyte_name='properties_hs_object_id',
                        type=['null', 'string'],
                        description='HubSpot object ID',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_task_body',
                        x_airbyte_name='properties_hs_task_body',
                        type=['null', 'string'],
                        description='Description or notes for the task',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_task_priority',
                        x_airbyte_name='properties_hs_task_priority',
                        type=['null', 'string'],
                        description='Priority of the task (LOW, MEDIUM, HIGH)',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_task_status',
                        x_airbyte_name='properties_hs_task_status',
                        type=['null', 'string'],
                        description='Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_task_subject',
                        x_airbyte_name='properties_hs_task_subject',
                        type=['null', 'string'],
                        description='Subject or title of the task',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_task_type',
                        x_airbyte_name='properties_hs_task_type',
                        type=['null', 'string'],
                        description='Type of the task (TODO, CALL, EMAIL)',
                    ),
                    CacheFieldConfig(
                        name='properties.hs_timestamp',
                        x_airbyte_name='properties_hs_timestamp',
                        type=['null', 'string'],
                        description='Due date / timestamp for the task',
                    ),
                    CacheFieldConfig(
                        name='properties.hubspot_owner_id',
                        x_airbyte_name='properties_hubspot_owner_id',
                        type=['null', 'string'],
                        description='ID of the task owner',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['null', 'string'],
                        description='Timestamp when the task record was last modified',
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'companies': [
            'archived',
            'contacts',
            'contacts[]',
            'createdAt',
            'id',
            'properties',
            'properties.createdate',
            'properties.domain',
            'properties.hs_lastmodifieddate',
            'properties.hs_object_id',
            'properties.hubspot_owner_id',
            'properties.name',
            'updatedAt',
        ],
        'contacts': [
            'archived',
            'companies',
            'companies[]',
            'createdAt',
            'id',
            'properties',
            'properties.associatedcompanyid',
            'properties.createdate',
            'properties.email',
            'properties.firstname',
            'properties.hs_object_id',
            'properties.hubspot_owner_id',
            'properties.lastmodifieddate',
            'properties.lastname',
            'updatedAt',
        ],
        'deals': [
            'archived',
            'companies',
            'companies[]',
            'contacts',
            'contacts[]',
            'createdAt',
            'id',
            'line_items',
            'line_items[]',
            'properties',
            'properties.amount',
            'properties.closedate',
            'properties.createdate',
            'properties.dealname',
            'properties.dealstage',
            'properties.hs_lastmodifieddate',
            'properties.hs_object_id',
            'properties.hubspot_owner_id',
            'properties.pipeline',
            'updatedAt',
        ],
        'tickets': [
            'archived',
            'companies',
            'companies[]',
            'contacts',
            'contacts[]',
            'createdAt',
            'id',
            'properties',
            'properties.content',
            'properties.createdate',
            'properties.hs_lastmodifieddate',
            'properties.hs_object_id',
            'properties.hs_pipeline',
            'properties.hs_pipeline_stage',
            'properties.hs_ticket_category',
            'properties.hs_ticket_priority',
            'properties.subject',
            'updatedAt',
        ],
        'notes': [
            'archived',
            'createdAt',
            'id',
            'properties',
            'properties.hs_createdate',
            'properties.hs_lastmodifieddate',
            'properties.hs_note_body',
            'properties.hs_object_id',
            'properties.hs_timestamp',
            'properties.hubspot_owner_id',
            'updatedAt',
        ],
        'calls': [
            'archived',
            'createdAt',
            'id',
            'properties',
            'properties.hs_call_body',
            'properties.hs_call_direction',
            'properties.hs_call_duration',
            'properties.hs_call_status',
            'properties.hs_call_title',
            'properties.hs_createdate',
            'properties.hs_lastmodifieddate',
            'properties.hs_object_id',
            'properties.hs_timestamp',
            'properties.hubspot_owner_id',
            'updatedAt',
        ],
        'emails': [
            'archived',
            'createdAt',
            'id',
            'properties',
            'properties.hs_createdate',
            'properties.hs_email_direction',
            'properties.hs_email_status',
            'properties.hs_email_subject',
            'properties.hs_email_text',
            'properties.hs_lastmodifieddate',
            'properties.hs_object_id',
            'properties.hs_timestamp',
            'properties.hubspot_owner_id',
            'updatedAt',
        ],
        'meetings': [
            'archived',
            'createdAt',
            'id',
            'properties',
            'properties.hs_createdate',
            'properties.hs_lastmodifieddate',
            'properties.hs_meeting_body',
            'properties.hs_meeting_end_time',
            'properties.hs_meeting_location',
            'properties.hs_meeting_outcome',
            'properties.hs_meeting_start_time',
            'properties.hs_meeting_title',
            'properties.hs_object_id',
            'properties.hs_timestamp',
            'properties.hubspot_owner_id',
            'updatedAt',
        ],
        'tasks': [
            'archived',
            'createdAt',
            'id',
            'properties',
            'properties.hs_createdate',
            'properties.hs_lastmodifieddate',
            'properties.hs_object_id',
            'properties.hs_task_body',
            'properties.hs_task_priority',
            'properties.hs_task_status',
            'properties.hs_task_subject',
            'properties.hs_task_type',
            'properties.hs_timestamp',
            'properties.hubspot_owner_id',
            'updatedAt',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List recent deals',
            'List recent tickets',
            'List companies in my CRM',
            'List contacts in my CRM',
            'Create a new contact with email john@example.com and name John Smith',
            "Create a new deal called 'Enterprise License' with amount 50000",
            "Update the deal stage to 'closedwon' for a specific deal",
            "Create a new company called 'Acme Corp' with domain acme.com",
            "Create a support ticket with subject 'Login issue' and priority HIGH",
            'Update the contact email for a specific contact',
            'Associate contact 123 with deal 456',
            'Link a contact to a company in HubSpot',
            'Set contact 123 as the Primary contact for company 456',
            'List all associations for contact 123 to companies',
            'Remove an association between a contact and a deal',
            "Add a note to contact 12345 saying 'Discussed pricing options'",
            'List recent notes in my CRM',
            'Get the details of a specific note',
            'Delete a note from HubSpot',
            'Log a call with contact 12345 about pricing discussion',
            'List recent calls in my CRM',
            'Create an email record for outreach to a contact',
            'List recent emails in my CRM',
            'Schedule a meeting with a contact for next Tuesday',
            'List recent meetings in my CRM',
            'Create a follow-up task for a deal',
            'List tasks in my CRM',
        ],
        context_store_search=[
            'Show me all deals from Acme Corp this quarter',
            'What are the top 5 most valuable deals in my pipeline right now?',
            'Search for contacts in the marketing department at HubSpot',
            "Give me an overview of my sales team's deals in the last 30 days",
            'Identify the most active companies in our CRM this month',
            'Compare the number of deals closed by different sales representatives',
            'Find all tickets related to a specific product issue and summarize their status',
        ],
        search=[
            'Show me all deals from Acme Corp this quarter',
            'What are the top 5 most valuable deals in my pipeline right now?',
            'Search for contacts in the marketing department at HubSpot',
            "Give me an overview of my sales team's deals in the last 30 days",
            'Identify the most active companies in our CRM this month',
            'Compare the number of deals closed by different sales representatives',
            'Find all tickets related to a specific product issue and summarize their status',
        ],
        unsupported=['Delete a contact from HubSpot', 'Delete a deal record'],
    ),
)