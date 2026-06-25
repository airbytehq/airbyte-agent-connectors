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
    version='0.1.19',
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
                                    'industry': {'type': 'string', 'description': 'Company industry'},
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
                                    'industry': {'type': 'string', 'description': 'Company industry'},
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
        unsupported=[
            'Delete a contact from HubSpot',
            'Delete a deal record',
            'Schedule a follow-up task for this deal',
            'Send an email to all contacts in the sales pipeline',
        ],
    ),
)