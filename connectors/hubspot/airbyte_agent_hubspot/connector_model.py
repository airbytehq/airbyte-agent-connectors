"""
Connector model for hubspot.

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

HubspotConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('36c891d9-4bd9-43ac-bad2-10e12756272c'),
    name='hubspot',
    version='0.1.9',
    base_url='https://api.hubapi.com',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://api.hubapi.com/oauth/v1/token',
            'auth_style': 'body',
            'body_format': 'form',
        },
        user_config_spec=AirbyteAuthConfig(
            title='OAuth2 Authentication',
            type='object',
            required=['client_id', 'client_secret', 'refresh_token'],
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
    entities=[
        EntityDefinition(
            name='contacts',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
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
            },
        ),
        EntityDefinition(
            name='companies',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
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
            },
        ),
        EntityDefinition(
            name='deals',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
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
            },
        ),
        EntityDefinition(
            name='tickets',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
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
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
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
            },
        ),
    ],
    search_field_paths={
        'companies': [
            'archived',
            'contacts',
            'contacts[]',
            'createdAt',
            'id',
            'properties',
            'updatedAt',
        ],
        'contacts': [
            'archived',
            'companies',
            'companies[]',
            'createdAt',
            'id',
            'properties',
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
            'updatedAt',
        ],
    },
)