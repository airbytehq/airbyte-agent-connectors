"""
Connector model for harvest.

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

HarvestConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('fe2b4084-3386-4d3b-9ad6-308f61a6f1e6'),
    name='harvest',
    version='1.0.2',
    base_url='https://api.harvestapp.com/v2',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='oauth2',
                type=AuthType.OAUTH2,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'refresh_url': 'https://id.getharvest.com/api/v2/oauth2/token',
                    'additional_headers': {'Harvest-Account-Id': '{{ account_id }}'},
                },
                user_config_spec=AirbyteAuthConfig(
                    title='OAuth 2.0',
                    type='object',
                    required=[
                        'client_id',
                        'client_secret',
                        'refresh_token',
                        'account_id',
                    ],
                    properties={
                        'client_id': AuthConfigFieldSpec(
                            title='Client ID',
                        ),
                        'client_secret': AuthConfigFieldSpec(
                            title='Client Secret',
                        ),
                        'refresh_token': AuthConfigFieldSpec(
                            title='Refresh Token',
                            description='Your Harvest OAuth2 refresh token',
                        ),
                        'account_id': AuthConfigFieldSpec(
                            title='Account ID',
                            description='Your Harvest account ID',
                        ),
                    },
                    auth_mapping={
                        'client_id': '${client_id}',
                        'client_secret': '${client_secret}',
                        'refresh_token': '${refresh_token}',
                    },
                    replication_auth_key_mapping={
                        'credentials.refresh_token': 'refresh_token',
                        'credentials.client_id': 'client_id',
                        'credentials.client_secret': 'client_secret',
                        'account_id': 'account_id',
                    },
                    additional_headers={'Harvest-Account-Id': '{{ account_id }}'},
                    replication_auth_key_constants={'credentials.auth_type': 'Client'},
                ),
                untested=True,
            ),
            AuthOption(
                scheme_name='bearer',
                type=AuthType.BEARER,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'additional_headers': {'Harvest-Account-Id': '{{ account_id }}'},
                },
                user_config_spec=AirbyteAuthConfig(
                    title='Personal Access Token',
                    type='object',
                    required=['token', 'account_id'],
                    properties={
                        'token': AuthConfigFieldSpec(
                            title='Personal Access Token',
                            description='Your Harvest personal access token',
                        ),
                        'account_id': AuthConfigFieldSpec(
                            title='Account ID',
                            description='Your Harvest account ID',
                        ),
                    },
                    auth_mapping={'token': '${token}'},
                    replication_auth_key_mapping={'credentials.api_token': 'token', 'account_id': 'account_id'},
                    additional_headers={'Harvest-Account-Id': '{{ account_id }}'},
                    replication_auth_key_constants={'credentials.auth_type': 'Token'},
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
                    path='/users',
                    action=Action.LIST,
                    description='Returns a paginated list of users in the Harvest account',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of users',
                        'properties': {
                            'users': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest user',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique user ID'},
                                        'first_name': {
                                            'type': ['null', 'string'],
                                            'description': 'First name of the user',
                                        },
                                        'last_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Last name of the user',
                                        },
                                        'email': {
                                            'type': ['null', 'string'],
                                            'description': 'Email address of the user',
                                        },
                                        'telephone': {
                                            'type': ['null', 'string'],
                                            'description': 'Telephone number of the user',
                                        },
                                        'timezone': {
                                            'type': ['null', 'string'],
                                            'description': 'Timezone of the user',
                                        },
                                        'has_access_to_all_future_projects': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the user has access to all future projects',
                                        },
                                        'is_contractor': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the user is a contractor',
                                        },
                                        'is_active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the user is active',
                                        },
                                        'weekly_capacity': {
                                            'type': ['null', 'integer'],
                                            'description': 'Weekly capacity in seconds',
                                        },
                                        'default_hourly_rate': {
                                            'type': ['null', 'number'],
                                            'description': 'Default hourly rate for the user',
                                        },
                                        'cost_rate': {
                                            'type': ['null', 'number'],
                                            'description': 'Cost rate for the user',
                                        },
                                        'roles': {
                                            'type': ['null', 'array'],
                                            'description': 'Roles assigned to the user',
                                            'items': {'type': 'string'},
                                        },
                                        'access_roles': {
                                            'type': ['null', 'array'],
                                            'description': 'Access roles assigned to the user',
                                            'items': {'type': 'string'},
                                        },
                                        'avatar_url': {
                                            'type': ['null', 'string'],
                                            'description': "URL to the user's avatar image",
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the user was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the user was last updated',
                                        },
                                        'employee_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Employee ID of the user',
                                        },
                                        'calendar_integration_enabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether calendar integration is enabled for the user',
                                        },
                                        'calendar_integration_source': {
                                            'type': ['null', 'string'],
                                            'description': 'Source of calendar integration',
                                        },
                                        'can_create_projects': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the user can create projects',
                                        },
                                        'permissions_claims': {
                                            'type': ['null', 'array'],
                                            'description': 'List of permission claims for the user',
                                            'items': {'type': 'string'},
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'users',
                                    'x-airbyte-stream-name': 'users',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.users',
                    meta_extractor={'next_link': '$.links.next'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/users/{id}',
                    action=Action.GET,
                    description='Get a single user by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest user',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique user ID'},
                            'first_name': {
                                'type': ['null', 'string'],
                                'description': 'First name of the user',
                            },
                            'last_name': {
                                'type': ['null', 'string'],
                                'description': 'Last name of the user',
                            },
                            'email': {
                                'type': ['null', 'string'],
                                'description': 'Email address of the user',
                            },
                            'telephone': {
                                'type': ['null', 'string'],
                                'description': 'Telephone number of the user',
                            },
                            'timezone': {
                                'type': ['null', 'string'],
                                'description': 'Timezone of the user',
                            },
                            'has_access_to_all_future_projects': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the user has access to all future projects',
                            },
                            'is_contractor': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the user is a contractor',
                            },
                            'is_active': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the user is active',
                            },
                            'weekly_capacity': {
                                'type': ['null', 'integer'],
                                'description': 'Weekly capacity in seconds',
                            },
                            'default_hourly_rate': {
                                'type': ['null', 'number'],
                                'description': 'Default hourly rate for the user',
                            },
                            'cost_rate': {
                                'type': ['null', 'number'],
                                'description': 'Cost rate for the user',
                            },
                            'roles': {
                                'type': ['null', 'array'],
                                'description': 'Roles assigned to the user',
                                'items': {'type': 'string'},
                            },
                            'access_roles': {
                                'type': ['null', 'array'],
                                'description': 'Access roles assigned to the user',
                                'items': {'type': 'string'},
                            },
                            'avatar_url': {
                                'type': ['null', 'string'],
                                'description': "URL to the user's avatar image",
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the user was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the user was last updated',
                            },
                            'employee_id': {
                                'type': ['null', 'string'],
                                'description': 'Employee ID of the user',
                            },
                            'calendar_integration_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether calendar integration is enabled for the user',
                            },
                            'calendar_integration_source': {
                                'type': ['null', 'string'],
                                'description': 'Source of calendar integration',
                            },
                            'can_create_projects': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the user can create projects',
                            },
                            'permissions_claims': {
                                'type': ['null', 'array'],
                                'description': 'List of permission claims for the user',
                                'items': {'type': 'string'},
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'users',
                        'x-airbyte-stream-name': 'users',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest user',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique user ID'},
                    'first_name': {
                        'type': ['null', 'string'],
                        'description': 'First name of the user',
                    },
                    'last_name': {
                        'type': ['null', 'string'],
                        'description': 'Last name of the user',
                    },
                    'email': {
                        'type': ['null', 'string'],
                        'description': 'Email address of the user',
                    },
                    'telephone': {
                        'type': ['null', 'string'],
                        'description': 'Telephone number of the user',
                    },
                    'timezone': {
                        'type': ['null', 'string'],
                        'description': 'Timezone of the user',
                    },
                    'has_access_to_all_future_projects': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user has access to all future projects',
                    },
                    'is_contractor': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user is a contractor',
                    },
                    'is_active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user is active',
                    },
                    'weekly_capacity': {
                        'type': ['null', 'integer'],
                        'description': 'Weekly capacity in seconds',
                    },
                    'default_hourly_rate': {
                        'type': ['null', 'number'],
                        'description': 'Default hourly rate for the user',
                    },
                    'cost_rate': {
                        'type': ['null', 'number'],
                        'description': 'Cost rate for the user',
                    },
                    'roles': {
                        'type': ['null', 'array'],
                        'description': 'Roles assigned to the user',
                        'items': {'type': 'string'},
                    },
                    'access_roles': {
                        'type': ['null', 'array'],
                        'description': 'Access roles assigned to the user',
                        'items': {'type': 'string'},
                    },
                    'avatar_url': {
                        'type': ['null', 'string'],
                        'description': "URL to the user's avatar image",
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the user was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the user was last updated',
                    },
                    'employee_id': {
                        'type': ['null', 'string'],
                        'description': 'Employee ID of the user',
                    },
                    'calendar_integration_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether calendar integration is enabled for the user',
                    },
                    'calendar_integration_source': {
                        'type': ['null', 'string'],
                        'description': 'Source of calendar integration',
                    },
                    'can_create_projects': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user can create projects',
                    },
                    'permissions_claims': {
                        'type': ['null', 'array'],
                        'description': 'List of permission claims for the user',
                        'items': {'type': 'string'},
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'users',
                'x-airbyte-stream-name': 'users',
            },
        ),
        EntityDefinition(
            name='clients',
            stream_name='clients',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/clients',
                    action=Action.LIST,
                    description='Returns a paginated list of clients',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of clients',
                        'properties': {
                            'clients': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest client',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique client ID'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the client',
                                        },
                                        'is_active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the client is active',
                                        },
                                        'address': {
                                            'type': ['null', 'string'],
                                            'description': 'Address of the client',
                                        },
                                        'statement_key': {
                                            'type': ['null', 'string'],
                                            'description': 'Statement key for the client',
                                        },
                                        'currency': {
                                            'type': ['null', 'string'],
                                            'description': 'Currency code for the client',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the client was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the client was last updated',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'clients',
                                    'x-airbyte-stream-name': 'clients',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.clients',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/clients/{id}',
                    action=Action.GET,
                    description='Get a single client by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest client',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique client ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the client',
                            },
                            'is_active': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the client is active',
                            },
                            'address': {
                                'type': ['null', 'string'],
                                'description': 'Address of the client',
                            },
                            'statement_key': {
                                'type': ['null', 'string'],
                                'description': 'Statement key for the client',
                            },
                            'currency': {
                                'type': ['null', 'string'],
                                'description': 'Currency code for the client',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the client was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the client was last updated',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'clients',
                        'x-airbyte-stream-name': 'clients',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest client',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique client ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the client',
                    },
                    'is_active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the client is active',
                    },
                    'address': {
                        'type': ['null', 'string'],
                        'description': 'Address of the client',
                    },
                    'statement_key': {
                        'type': ['null', 'string'],
                        'description': 'Statement key for the client',
                    },
                    'currency': {
                        'type': ['null', 'string'],
                        'description': 'Currency code for the client',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the client was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the client was last updated',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'clients',
                'x-airbyte-stream-name': 'clients',
            },
        ),
        EntityDefinition(
            name='contacts',
            stream_name='contacts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/contacts',
                    action=Action.LIST,
                    description='Returns a paginated list of contacts',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of contacts',
                        'properties': {
                            'contacts': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest contact associated with a client',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique contact ID'},
                                        'title': {
                                            'type': ['null', 'string'],
                                            'description': 'Title of the contact',
                                        },
                                        'first_name': {
                                            'type': ['null', 'string'],
                                            'description': 'First name of the contact',
                                        },
                                        'last_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Last name of the contact',
                                        },
                                        'email': {
                                            'type': ['null', 'string'],
                                            'description': 'Email address of the contact',
                                        },
                                        'phone_office': {
                                            'type': ['null', 'string'],
                                            'description': 'Office phone number',
                                        },
                                        'phone_mobile': {
                                            'type': ['null', 'string'],
                                            'description': 'Mobile phone number',
                                        },
                                        'fax': {
                                            'type': ['null', 'string'],
                                            'description': 'Fax number',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the contact was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the contact was last updated',
                                        },
                                        'client': {
                                            'type': ['null', 'object'],
                                            'description': 'The client associated with this contact',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Client ID',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Client name',
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'contacts',
                                    'x-airbyte-stream-name': 'contacts',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.contacts',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/contacts/{id}',
                    action=Action.GET,
                    description='Get a single contact by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest contact associated with a client',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique contact ID'},
                            'title': {
                                'type': ['null', 'string'],
                                'description': 'Title of the contact',
                            },
                            'first_name': {
                                'type': ['null', 'string'],
                                'description': 'First name of the contact',
                            },
                            'last_name': {
                                'type': ['null', 'string'],
                                'description': 'Last name of the contact',
                            },
                            'email': {
                                'type': ['null', 'string'],
                                'description': 'Email address of the contact',
                            },
                            'phone_office': {
                                'type': ['null', 'string'],
                                'description': 'Office phone number',
                            },
                            'phone_mobile': {
                                'type': ['null', 'string'],
                                'description': 'Mobile phone number',
                            },
                            'fax': {
                                'type': ['null', 'string'],
                                'description': 'Fax number',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the contact was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the contact was last updated',
                            },
                            'client': {
                                'type': ['null', 'object'],
                                'description': 'The client associated with this contact',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Client ID',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Client name',
                                    },
                                },
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'contacts',
                        'x-airbyte-stream-name': 'contacts',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest contact associated with a client',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique contact ID'},
                    'title': {
                        'type': ['null', 'string'],
                        'description': 'Title of the contact',
                    },
                    'first_name': {
                        'type': ['null', 'string'],
                        'description': 'First name of the contact',
                    },
                    'last_name': {
                        'type': ['null', 'string'],
                        'description': 'Last name of the contact',
                    },
                    'email': {
                        'type': ['null', 'string'],
                        'description': 'Email address of the contact',
                    },
                    'phone_office': {
                        'type': ['null', 'string'],
                        'description': 'Office phone number',
                    },
                    'phone_mobile': {
                        'type': ['null', 'string'],
                        'description': 'Mobile phone number',
                    },
                    'fax': {
                        'type': ['null', 'string'],
                        'description': 'Fax number',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the contact was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the contact was last updated',
                    },
                    'client': {
                        'type': ['null', 'object'],
                        'description': 'The client associated with this contact',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Client ID',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Client name',
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'contacts',
                'x-airbyte-stream-name': 'contacts',
            },
        ),
        EntityDefinition(
            name='company',
            stream_name='company',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/company',
                    action=Action.GET,
                    description='Returns the company information for the authenticated account',
                    response_schema={
                        'type': 'object',
                        'description': 'The Harvest company/account information',
                        'properties': {
                            'base_uri': {
                                'type': ['null', 'string'],
                                'description': 'Base URI for the Harvest account',
                            },
                            'full_domain': {
                                'type': ['null', 'string'],
                                'description': 'Full domain of the Harvest account',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the company',
                            },
                            'is_active': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the company account is active',
                            },
                            'week_start_day': {
                                'type': ['null', 'string'],
                                'description': "Day of the week the company's work week starts",
                            },
                            'wants_timestamp_timers': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether timestamp timers are enabled',
                            },
                            'time_format': {
                                'type': ['null', 'string'],
                                'description': 'Time format used by the company',
                            },
                            'date_format': {
                                'type': ['null', 'string'],
                                'description': 'Date format used by the company',
                            },
                            'plan_type': {
                                'type': ['null', 'string'],
                                'description': 'The Harvest plan type',
                            },
                            'clock': {
                                'type': ['null', 'string'],
                                'description': 'Clock format (12h or 24h)',
                            },
                            'currency_code_display': {
                                'type': ['null', 'string'],
                                'description': 'Currency code display format',
                            },
                            'currency_symbol_display': {
                                'type': ['null', 'string'],
                                'description': 'Currency symbol display format',
                            },
                            'decimal_symbol': {
                                'type': ['null', 'string'],
                                'description': 'Decimal symbol used for numbers',
                            },
                            'thousands_separator': {
                                'type': ['null', 'string'],
                                'description': 'Thousands separator used for numbers',
                            },
                            'color_scheme': {
                                'type': ['null', 'string'],
                                'description': 'Color scheme of the Harvest account',
                            },
                            'weekly_capacity': {
                                'type': ['null', 'integer'],
                                'description': 'Weekly capacity in seconds',
                            },
                            'expense_feature': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the expense feature is enabled',
                            },
                            'invoice_feature': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the invoice feature is enabled',
                            },
                            'estimate_feature': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the estimate feature is enabled',
                            },
                            'approval_feature': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the approval feature is enabled',
                            },
                            'team_feature': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the team feature is enabled',
                            },
                            'currency': {
                                'type': ['null', 'string'],
                                'description': 'Currency used by the company',
                            },
                            'saml_sign_in_required': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether SAML sign-in is required',
                            },
                            'day_entry_notes_required': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether day entry notes are required',
                            },
                        },
                        'x-airbyte-entity-name': 'company',
                        'x-airbyte-stream-name': 'company',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'The Harvest company/account information',
                'properties': {
                    'base_uri': {
                        'type': ['null', 'string'],
                        'description': 'Base URI for the Harvest account',
                    },
                    'full_domain': {
                        'type': ['null', 'string'],
                        'description': 'Full domain of the Harvest account',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the company',
                    },
                    'is_active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the company account is active',
                    },
                    'week_start_day': {
                        'type': ['null', 'string'],
                        'description': "Day of the week the company's work week starts",
                    },
                    'wants_timestamp_timers': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether timestamp timers are enabled',
                    },
                    'time_format': {
                        'type': ['null', 'string'],
                        'description': 'Time format used by the company',
                    },
                    'date_format': {
                        'type': ['null', 'string'],
                        'description': 'Date format used by the company',
                    },
                    'plan_type': {
                        'type': ['null', 'string'],
                        'description': 'The Harvest plan type',
                    },
                    'clock': {
                        'type': ['null', 'string'],
                        'description': 'Clock format (12h or 24h)',
                    },
                    'currency_code_display': {
                        'type': ['null', 'string'],
                        'description': 'Currency code display format',
                    },
                    'currency_symbol_display': {
                        'type': ['null', 'string'],
                        'description': 'Currency symbol display format',
                    },
                    'decimal_symbol': {
                        'type': ['null', 'string'],
                        'description': 'Decimal symbol used for numbers',
                    },
                    'thousands_separator': {
                        'type': ['null', 'string'],
                        'description': 'Thousands separator used for numbers',
                    },
                    'color_scheme': {
                        'type': ['null', 'string'],
                        'description': 'Color scheme of the Harvest account',
                    },
                    'weekly_capacity': {
                        'type': ['null', 'integer'],
                        'description': 'Weekly capacity in seconds',
                    },
                    'expense_feature': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the expense feature is enabled',
                    },
                    'invoice_feature': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the invoice feature is enabled',
                    },
                    'estimate_feature': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the estimate feature is enabled',
                    },
                    'approval_feature': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the approval feature is enabled',
                    },
                    'team_feature': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the team feature is enabled',
                    },
                    'currency': {
                        'type': ['null', 'string'],
                        'description': 'Currency used by the company',
                    },
                    'saml_sign_in_required': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether SAML sign-in is required',
                    },
                    'day_entry_notes_required': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether day entry notes are required',
                    },
                },
                'x-airbyte-entity-name': 'company',
                'x-airbyte-stream-name': 'company',
            },
        ),
        EntityDefinition(
            name='projects',
            stream_name='projects',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects',
                    action=Action.LIST,
                    description='Returns a paginated list of projects',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of projects',
                        'properties': {
                            'projects': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest project',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique project ID'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the project',
                                        },
                                        'code': {
                                            'type': ['null', 'string'],
                                            'description': 'Project code',
                                        },
                                        'is_active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the project is active',
                                        },
                                        'is_billable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the project is billable',
                                        },
                                        'is_fixed_fee': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the project is a fixed fee project',
                                        },
                                        'bill_by': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing method for the project',
                                        },
                                        'hourly_rate': {
                                            'type': ['null', 'number'],
                                            'description': 'Hourly rate for the project',
                                        },
                                        'budget_by': {
                                            'type': ['null', 'string'],
                                            'description': 'Budget method for the project',
                                        },
                                        'budget_is_monthly': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the budget resets monthly',
                                        },
                                        'budget': {
                                            'type': ['null', 'number'],
                                            'description': 'Budget amount for the project',
                                        },
                                        'cost_budget': {
                                            'type': ['null', 'number'],
                                            'description': 'Cost budget for the project',
                                        },
                                        'cost_budget_include_expenses': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the cost budget includes expenses',
                                        },
                                        'notify_when_over_budget': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to notify when over budget',
                                        },
                                        'over_budget_notification_percentage': {
                                            'type': ['null', 'number'],
                                            'description': 'Percentage at which over-budget notification triggers',
                                        },
                                        'over_budget_notification_date': {
                                            'type': ['null', 'string'],
                                            'description': 'Date of the last over-budget notification',
                                        },
                                        'show_budget_to_all': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to show the budget to all users',
                                        },
                                        'fee': {
                                            'type': ['null', 'number'],
                                            'description': 'Fixed fee amount for the project',
                                        },
                                        'notes': {
                                            'type': ['null', 'string'],
                                            'description': 'Notes about the project',
                                        },
                                        'starts_on': {
                                            'type': ['null', 'string'],
                                            'description': 'Start date of the project',
                                        },
                                        'ends_on': {
                                            'type': ['null', 'string'],
                                            'description': 'End date of the project',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the project was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the project was last updated',
                                        },
                                        'client': {
                                            'type': ['null', 'object'],
                                            'description': 'The client associated with the project',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Client ID',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Client name',
                                                },
                                                'currency': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Client currency',
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'projects',
                                    'x-airbyte-stream-name': 'projects',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.projects',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{id}',
                    action=Action.GET,
                    description='Get a single project by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest project',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique project ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the project',
                            },
                            'code': {
                                'type': ['null', 'string'],
                                'description': 'Project code',
                            },
                            'is_active': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the project is active',
                            },
                            'is_billable': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the project is billable',
                            },
                            'is_fixed_fee': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the project is a fixed fee project',
                            },
                            'bill_by': {
                                'type': ['null', 'string'],
                                'description': 'Billing method for the project',
                            },
                            'hourly_rate': {
                                'type': ['null', 'number'],
                                'description': 'Hourly rate for the project',
                            },
                            'budget_by': {
                                'type': ['null', 'string'],
                                'description': 'Budget method for the project',
                            },
                            'budget_is_monthly': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the budget resets monthly',
                            },
                            'budget': {
                                'type': ['null', 'number'],
                                'description': 'Budget amount for the project',
                            },
                            'cost_budget': {
                                'type': ['null', 'number'],
                                'description': 'Cost budget for the project',
                            },
                            'cost_budget_include_expenses': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the cost budget includes expenses',
                            },
                            'notify_when_over_budget': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether to notify when over budget',
                            },
                            'over_budget_notification_percentage': {
                                'type': ['null', 'number'],
                                'description': 'Percentage at which over-budget notification triggers',
                            },
                            'over_budget_notification_date': {
                                'type': ['null', 'string'],
                                'description': 'Date of the last over-budget notification',
                            },
                            'show_budget_to_all': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether to show the budget to all users',
                            },
                            'fee': {
                                'type': ['null', 'number'],
                                'description': 'Fixed fee amount for the project',
                            },
                            'notes': {
                                'type': ['null', 'string'],
                                'description': 'Notes about the project',
                            },
                            'starts_on': {
                                'type': ['null', 'string'],
                                'description': 'Start date of the project',
                            },
                            'ends_on': {
                                'type': ['null', 'string'],
                                'description': 'End date of the project',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the project was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the project was last updated',
                            },
                            'client': {
                                'type': ['null', 'object'],
                                'description': 'The client associated with the project',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Client ID',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Client name',
                                    },
                                    'currency': {
                                        'type': ['null', 'string'],
                                        'description': 'Client currency',
                                    },
                                },
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'projects',
                        'x-airbyte-stream-name': 'projects',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest project',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique project ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the project',
                    },
                    'code': {
                        'type': ['null', 'string'],
                        'description': 'Project code',
                    },
                    'is_active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the project is active',
                    },
                    'is_billable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the project is billable',
                    },
                    'is_fixed_fee': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the project is a fixed fee project',
                    },
                    'bill_by': {
                        'type': ['null', 'string'],
                        'description': 'Billing method for the project',
                    },
                    'hourly_rate': {
                        'type': ['null', 'number'],
                        'description': 'Hourly rate for the project',
                    },
                    'budget_by': {
                        'type': ['null', 'string'],
                        'description': 'Budget method for the project',
                    },
                    'budget_is_monthly': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the budget resets monthly',
                    },
                    'budget': {
                        'type': ['null', 'number'],
                        'description': 'Budget amount for the project',
                    },
                    'cost_budget': {
                        'type': ['null', 'number'],
                        'description': 'Cost budget for the project',
                    },
                    'cost_budget_include_expenses': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the cost budget includes expenses',
                    },
                    'notify_when_over_budget': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to notify when over budget',
                    },
                    'over_budget_notification_percentage': {
                        'type': ['null', 'number'],
                        'description': 'Percentage at which over-budget notification triggers',
                    },
                    'over_budget_notification_date': {
                        'type': ['null', 'string'],
                        'description': 'Date of the last over-budget notification',
                    },
                    'show_budget_to_all': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to show the budget to all users',
                    },
                    'fee': {
                        'type': ['null', 'number'],
                        'description': 'Fixed fee amount for the project',
                    },
                    'notes': {
                        'type': ['null', 'string'],
                        'description': 'Notes about the project',
                    },
                    'starts_on': {
                        'type': ['null', 'string'],
                        'description': 'Start date of the project',
                    },
                    'ends_on': {
                        'type': ['null', 'string'],
                        'description': 'End date of the project',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the project was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the project was last updated',
                    },
                    'client': {
                        'type': ['null', 'object'],
                        'description': 'The client associated with the project',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Client ID',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Client name',
                            },
                            'currency': {
                                'type': ['null', 'string'],
                                'description': 'Client currency',
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'projects',
                'x-airbyte-stream-name': 'projects',
            },
        ),
        EntityDefinition(
            name='tasks',
            stream_name='tasks',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tasks',
                    action=Action.LIST,
                    description='Returns a paginated list of tasks',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks',
                        'properties': {
                            'tasks': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest task',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique task ID'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the task',
                                        },
                                        'billable_by_default': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the task is billable by default',
                                        },
                                        'default_hourly_rate': {
                                            'type': ['null', 'number'],
                                            'description': 'Default hourly rate for the task',
                                        },
                                        'is_default': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the task is a default task',
                                        },
                                        'is_active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the task is active',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the task was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the task was last updated',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'tasks',
                                    'x-airbyte-stream-name': 'tasks',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.tasks',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/tasks/{id}',
                    action=Action.GET,
                    description='Get a single task by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest task',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique task ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the task',
                            },
                            'billable_by_default': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the task is billable by default',
                            },
                            'default_hourly_rate': {
                                'type': ['null', 'number'],
                                'description': 'Default hourly rate for the task',
                            },
                            'is_default': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the task is a default task',
                            },
                            'is_active': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the task is active',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the task was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the task was last updated',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'tasks',
                        'x-airbyte-stream-name': 'tasks',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest task',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique task ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the task',
                    },
                    'billable_by_default': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the task is billable by default',
                    },
                    'default_hourly_rate': {
                        'type': ['null', 'number'],
                        'description': 'Default hourly rate for the task',
                    },
                    'is_default': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the task is a default task',
                    },
                    'is_active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the task is active',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the task was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the task was last updated',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'tasks',
                'x-airbyte-stream-name': 'tasks',
            },
        ),
        EntityDefinition(
            name='time_entries',
            stream_name='time_entries',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/time_entries',
                    action=Action.LIST,
                    description='Returns a paginated list of time entries',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of time entries',
                        'properties': {
                            'time_entries': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest time entry',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique time entry ID'},
                                        'spent_date': {
                                            'type': ['null', 'string'],
                                            'description': 'Date the time was spent',
                                        },
                                        'hours': {
                                            'type': ['null', 'number'],
                                            'description': 'Total hours tracked',
                                        },
                                        'hours_without_timer': {
                                            'type': ['null', 'number'],
                                            'description': 'Hours tracked without a timer',
                                        },
                                        'rounded_hours': {
                                            'type': ['null', 'number'],
                                            'description': 'Rounded hours',
                                        },
                                        'notes': {
                                            'type': ['null', 'string'],
                                            'description': 'Notes for the time entry',
                                        },
                                        'is_locked': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the time entry is locked',
                                        },
                                        'locked_reason': {
                                            'type': ['null', 'string'],
                                            'description': 'Reason the time entry is locked',
                                        },
                                        'is_closed': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the time entry is closed',
                                        },
                                        'is_billed': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the time entry has been billed',
                                        },
                                        'timer_started_at': {
                                            'type': ['null', 'string'],
                                            'description': 'Timestamp when the timer was started',
                                        },
                                        'started_time': {
                                            'type': ['null', 'string'],
                                            'description': 'Start time of the time entry',
                                        },
                                        'ended_time': {
                                            'type': ['null', 'string'],
                                            'description': 'End time of the time entry',
                                        },
                                        'is_running': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the timer is currently running',
                                        },
                                        'billable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the time entry is billable',
                                        },
                                        'budgeted': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the time entry is budgeted',
                                        },
                                        'billable_rate': {
                                            'type': ['null', 'number'],
                                            'description': 'Billable rate for the time entry',
                                        },
                                        'cost_rate': {
                                            'type': ['null', 'number'],
                                            'description': 'Cost rate for the time entry',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the time entry was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the time entry was last updated',
                                        },
                                        'approval_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Approval status of the time entry',
                                        },
                                        'is_explicitly_locked': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the time entry is explicitly locked',
                                        },
                                        'user': {
                                            'type': ['null', 'object'],
                                            'description': 'The user associated with the time entry',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'User ID',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'User name',
                                                },
                                            },
                                        },
                                        'client': {
                                            'type': ['null', 'object'],
                                            'description': 'The client associated with the time entry',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Client ID',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Client name',
                                                },
                                            },
                                        },
                                        'project': {
                                            'type': ['null', 'object'],
                                            'description': 'The project associated with the time entry',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Project ID',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Project name',
                                                },
                                            },
                                        },
                                        'task': {
                                            'type': ['null', 'object'],
                                            'description': 'The task associated with the time entry',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Task ID',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Task name',
                                                },
                                            },
                                        },
                                        'user_assignment': {
                                            'type': ['null', 'object'],
                                            'description': 'The user assignment associated with the time entry',
                                        },
                                        'task_assignment': {
                                            'type': ['null', 'object'],
                                            'description': 'The task assignment associated with the time entry',
                                        },
                                        'external_reference': {
                                            'type': ['null', 'object'],
                                            'description': 'External reference for the time entry',
                                        },
                                        'invoice': {
                                            'type': ['null', 'object'],
                                            'description': 'The invoice associated with the time entry',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Invoice ID',
                                                },
                                                'number': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Invoice number',
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'time_entries',
                                    'x-airbyte-stream-name': 'time_entries',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.time_entries',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/time_entries/{id}',
                    action=Action.GET,
                    description='Get a single time entry by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest time entry',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique time entry ID'},
                            'spent_date': {
                                'type': ['null', 'string'],
                                'description': 'Date the time was spent',
                            },
                            'hours': {
                                'type': ['null', 'number'],
                                'description': 'Total hours tracked',
                            },
                            'hours_without_timer': {
                                'type': ['null', 'number'],
                                'description': 'Hours tracked without a timer',
                            },
                            'rounded_hours': {
                                'type': ['null', 'number'],
                                'description': 'Rounded hours',
                            },
                            'notes': {
                                'type': ['null', 'string'],
                                'description': 'Notes for the time entry',
                            },
                            'is_locked': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the time entry is locked',
                            },
                            'locked_reason': {
                                'type': ['null', 'string'],
                                'description': 'Reason the time entry is locked',
                            },
                            'is_closed': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the time entry is closed',
                            },
                            'is_billed': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the time entry has been billed',
                            },
                            'timer_started_at': {
                                'type': ['null', 'string'],
                                'description': 'Timestamp when the timer was started',
                            },
                            'started_time': {
                                'type': ['null', 'string'],
                                'description': 'Start time of the time entry',
                            },
                            'ended_time': {
                                'type': ['null', 'string'],
                                'description': 'End time of the time entry',
                            },
                            'is_running': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the timer is currently running',
                            },
                            'billable': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the time entry is billable',
                            },
                            'budgeted': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the time entry is budgeted',
                            },
                            'billable_rate': {
                                'type': ['null', 'number'],
                                'description': 'Billable rate for the time entry',
                            },
                            'cost_rate': {
                                'type': ['null', 'number'],
                                'description': 'Cost rate for the time entry',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the time entry was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the time entry was last updated',
                            },
                            'approval_status': {
                                'type': ['null', 'string'],
                                'description': 'Approval status of the time entry',
                            },
                            'is_explicitly_locked': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the time entry is explicitly locked',
                            },
                            'user': {
                                'type': ['null', 'object'],
                                'description': 'The user associated with the time entry',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'User ID',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'User name',
                                    },
                                },
                            },
                            'client': {
                                'type': ['null', 'object'],
                                'description': 'The client associated with the time entry',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Client ID',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Client name',
                                    },
                                },
                            },
                            'project': {
                                'type': ['null', 'object'],
                                'description': 'The project associated with the time entry',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Project ID',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Project name',
                                    },
                                },
                            },
                            'task': {
                                'type': ['null', 'object'],
                                'description': 'The task associated with the time entry',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Task ID',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Task name',
                                    },
                                },
                            },
                            'user_assignment': {
                                'type': ['null', 'object'],
                                'description': 'The user assignment associated with the time entry',
                            },
                            'task_assignment': {
                                'type': ['null', 'object'],
                                'description': 'The task assignment associated with the time entry',
                            },
                            'external_reference': {
                                'type': ['null', 'object'],
                                'description': 'External reference for the time entry',
                            },
                            'invoice': {
                                'type': ['null', 'object'],
                                'description': 'The invoice associated with the time entry',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Invoice ID',
                                    },
                                    'number': {
                                        'type': ['null', 'string'],
                                        'description': 'Invoice number',
                                    },
                                },
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'time_entries',
                        'x-airbyte-stream-name': 'time_entries',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest time entry',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique time entry ID'},
                    'spent_date': {
                        'type': ['null', 'string'],
                        'description': 'Date the time was spent',
                    },
                    'hours': {
                        'type': ['null', 'number'],
                        'description': 'Total hours tracked',
                    },
                    'hours_without_timer': {
                        'type': ['null', 'number'],
                        'description': 'Hours tracked without a timer',
                    },
                    'rounded_hours': {
                        'type': ['null', 'number'],
                        'description': 'Rounded hours',
                    },
                    'notes': {
                        'type': ['null', 'string'],
                        'description': 'Notes for the time entry',
                    },
                    'is_locked': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the time entry is locked',
                    },
                    'locked_reason': {
                        'type': ['null', 'string'],
                        'description': 'Reason the time entry is locked',
                    },
                    'is_closed': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the time entry is closed',
                    },
                    'is_billed': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the time entry has been billed',
                    },
                    'timer_started_at': {
                        'type': ['null', 'string'],
                        'description': 'Timestamp when the timer was started',
                    },
                    'started_time': {
                        'type': ['null', 'string'],
                        'description': 'Start time of the time entry',
                    },
                    'ended_time': {
                        'type': ['null', 'string'],
                        'description': 'End time of the time entry',
                    },
                    'is_running': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the timer is currently running',
                    },
                    'billable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the time entry is billable',
                    },
                    'budgeted': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the time entry is budgeted',
                    },
                    'billable_rate': {
                        'type': ['null', 'number'],
                        'description': 'Billable rate for the time entry',
                    },
                    'cost_rate': {
                        'type': ['null', 'number'],
                        'description': 'Cost rate for the time entry',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the time entry was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the time entry was last updated',
                    },
                    'approval_status': {
                        'type': ['null', 'string'],
                        'description': 'Approval status of the time entry',
                    },
                    'is_explicitly_locked': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the time entry is explicitly locked',
                    },
                    'user': {
                        'type': ['null', 'object'],
                        'description': 'The user associated with the time entry',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'User ID',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'User name',
                            },
                        },
                    },
                    'client': {
                        'type': ['null', 'object'],
                        'description': 'The client associated with the time entry',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Client ID',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Client name',
                            },
                        },
                    },
                    'project': {
                        'type': ['null', 'object'],
                        'description': 'The project associated with the time entry',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Project ID',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Project name',
                            },
                        },
                    },
                    'task': {
                        'type': ['null', 'object'],
                        'description': 'The task associated with the time entry',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Task ID',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Task name',
                            },
                        },
                    },
                    'user_assignment': {
                        'type': ['null', 'object'],
                        'description': 'The user assignment associated with the time entry',
                    },
                    'task_assignment': {
                        'type': ['null', 'object'],
                        'description': 'The task assignment associated with the time entry',
                    },
                    'external_reference': {
                        'type': ['null', 'object'],
                        'description': 'External reference for the time entry',
                    },
                    'invoice': {
                        'type': ['null', 'object'],
                        'description': 'The invoice associated with the time entry',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Invoice ID',
                            },
                            'number': {
                                'type': ['null', 'string'],
                                'description': 'Invoice number',
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'time_entries',
                'x-airbyte-stream-name': 'time_entries',
            },
        ),
        EntityDefinition(
            name='invoices',
            stream_name='invoices',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/invoices',
                    action=Action.LIST,
                    description='Returns a paginated list of invoices',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of invoices',
                        'properties': {
                            'invoices': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest invoice',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique invoice ID'},
                                        'client_key': {
                                            'type': ['null', 'string'],
                                            'description': 'Client key for the invoice',
                                        },
                                        'number': {
                                            'type': ['null', 'string'],
                                            'description': 'Invoice number',
                                        },
                                        'purchase_order': {
                                            'type': ['null', 'string'],
                                            'description': 'Purchase order number',
                                        },
                                        'amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Total amount of the invoice',
                                        },
                                        'due_amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Amount due on the invoice',
                                        },
                                        'tax': {
                                            'type': ['null', 'number'],
                                            'description': 'Tax percentage',
                                        },
                                        'tax_amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Tax amount',
                                        },
                                        'tax2': {
                                            'type': ['null', 'number'],
                                            'description': 'Second tax percentage',
                                        },
                                        'tax2_amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Second tax amount',
                                        },
                                        'discount': {
                                            'type': ['null', 'number'],
                                            'description': 'Discount percentage',
                                        },
                                        'discount_amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Discount amount',
                                        },
                                        'subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Subject of the invoice',
                                        },
                                        'notes': {
                                            'type': ['null', 'string'],
                                            'description': 'Notes on the invoice',
                                        },
                                        'currency': {
                                            'type': ['null', 'string'],
                                            'description': 'Currency code for the invoice',
                                        },
                                        'state': {
                                            'type': ['null', 'string'],
                                            'description': 'State of the invoice (draft, open, paid, closed)',
                                        },
                                        'period_start': {
                                            'type': ['null', 'string'],
                                            'description': 'Start of the invoice period',
                                        },
                                        'period_end': {
                                            'type': ['null', 'string'],
                                            'description': 'End of the invoice period',
                                        },
                                        'issue_date': {
                                            'type': ['null', 'string'],
                                            'description': 'Date the invoice was issued',
                                        },
                                        'due_date': {
                                            'type': ['null', 'string'],
                                            'description': 'Date the invoice is due',
                                        },
                                        'payment_term': {
                                            'type': ['null', 'string'],
                                            'description': 'Payment term for the invoice',
                                        },
                                        'payment_options': {
                                            'type': ['null', 'array'],
                                            'description': 'Available payment options',
                                            'items': {'type': 'string'},
                                        },
                                        'sent_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the invoice was sent',
                                        },
                                        'paid_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the invoice was paid',
                                        },
                                        'paid_date': {
                                            'type': ['null', 'string'],
                                            'description': 'Date the invoice was paid',
                                        },
                                        'closed_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the invoice was closed',
                                        },
                                        'recurring_invoice_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'ID of the recurring invoice',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the invoice was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the invoice was last updated',
                                        },
                                        'client': {
                                            'type': ['null', 'object'],
                                            'description': 'The client associated with the invoice',
                                        },
                                        'estimate': {
                                            'type': ['null', 'object'],
                                            'description': 'The estimate associated with the invoice',
                                        },
                                        'retainer': {
                                            'type': ['null', 'object'],
                                            'description': 'The retainer associated with the invoice',
                                        },
                                        'creator': {
                                            'type': ['null', 'object'],
                                            'description': 'The creator of the invoice',
                                        },
                                        'line_items': {
                                            'type': ['null', 'array'],
                                            'description': 'Line items on the invoice',
                                            'items': {'type': 'object'},
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'invoices',
                                    'x-airbyte-stream-name': 'invoices',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.invoices',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/invoices/{id}',
                    action=Action.GET,
                    description='Get a single invoice by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest invoice',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique invoice ID'},
                            'client_key': {
                                'type': ['null', 'string'],
                                'description': 'Client key for the invoice',
                            },
                            'number': {
                                'type': ['null', 'string'],
                                'description': 'Invoice number',
                            },
                            'purchase_order': {
                                'type': ['null', 'string'],
                                'description': 'Purchase order number',
                            },
                            'amount': {
                                'type': ['null', 'number'],
                                'description': 'Total amount of the invoice',
                            },
                            'due_amount': {
                                'type': ['null', 'number'],
                                'description': 'Amount due on the invoice',
                            },
                            'tax': {
                                'type': ['null', 'number'],
                                'description': 'Tax percentage',
                            },
                            'tax_amount': {
                                'type': ['null', 'number'],
                                'description': 'Tax amount',
                            },
                            'tax2': {
                                'type': ['null', 'number'],
                                'description': 'Second tax percentage',
                            },
                            'tax2_amount': {
                                'type': ['null', 'number'],
                                'description': 'Second tax amount',
                            },
                            'discount': {
                                'type': ['null', 'number'],
                                'description': 'Discount percentage',
                            },
                            'discount_amount': {
                                'type': ['null', 'number'],
                                'description': 'Discount amount',
                            },
                            'subject': {
                                'type': ['null', 'string'],
                                'description': 'Subject of the invoice',
                            },
                            'notes': {
                                'type': ['null', 'string'],
                                'description': 'Notes on the invoice',
                            },
                            'currency': {
                                'type': ['null', 'string'],
                                'description': 'Currency code for the invoice',
                            },
                            'state': {
                                'type': ['null', 'string'],
                                'description': 'State of the invoice (draft, open, paid, closed)',
                            },
                            'period_start': {
                                'type': ['null', 'string'],
                                'description': 'Start of the invoice period',
                            },
                            'period_end': {
                                'type': ['null', 'string'],
                                'description': 'End of the invoice period',
                            },
                            'issue_date': {
                                'type': ['null', 'string'],
                                'description': 'Date the invoice was issued',
                            },
                            'due_date': {
                                'type': ['null', 'string'],
                                'description': 'Date the invoice is due',
                            },
                            'payment_term': {
                                'type': ['null', 'string'],
                                'description': 'Payment term for the invoice',
                            },
                            'payment_options': {
                                'type': ['null', 'array'],
                                'description': 'Available payment options',
                                'items': {'type': 'string'},
                            },
                            'sent_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the invoice was sent',
                            },
                            'paid_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the invoice was paid',
                            },
                            'paid_date': {
                                'type': ['null', 'string'],
                                'description': 'Date the invoice was paid',
                            },
                            'closed_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the invoice was closed',
                            },
                            'recurring_invoice_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the recurring invoice',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the invoice was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the invoice was last updated',
                            },
                            'client': {
                                'type': ['null', 'object'],
                                'description': 'The client associated with the invoice',
                            },
                            'estimate': {
                                'type': ['null', 'object'],
                                'description': 'The estimate associated with the invoice',
                            },
                            'retainer': {
                                'type': ['null', 'object'],
                                'description': 'The retainer associated with the invoice',
                            },
                            'creator': {
                                'type': ['null', 'object'],
                                'description': 'The creator of the invoice',
                            },
                            'line_items': {
                                'type': ['null', 'array'],
                                'description': 'Line items on the invoice',
                                'items': {'type': 'object'},
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'invoices',
                        'x-airbyte-stream-name': 'invoices',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest invoice',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique invoice ID'},
                    'client_key': {
                        'type': ['null', 'string'],
                        'description': 'Client key for the invoice',
                    },
                    'number': {
                        'type': ['null', 'string'],
                        'description': 'Invoice number',
                    },
                    'purchase_order': {
                        'type': ['null', 'string'],
                        'description': 'Purchase order number',
                    },
                    'amount': {
                        'type': ['null', 'number'],
                        'description': 'Total amount of the invoice',
                    },
                    'due_amount': {
                        'type': ['null', 'number'],
                        'description': 'Amount due on the invoice',
                    },
                    'tax': {
                        'type': ['null', 'number'],
                        'description': 'Tax percentage',
                    },
                    'tax_amount': {
                        'type': ['null', 'number'],
                        'description': 'Tax amount',
                    },
                    'tax2': {
                        'type': ['null', 'number'],
                        'description': 'Second tax percentage',
                    },
                    'tax2_amount': {
                        'type': ['null', 'number'],
                        'description': 'Second tax amount',
                    },
                    'discount': {
                        'type': ['null', 'number'],
                        'description': 'Discount percentage',
                    },
                    'discount_amount': {
                        'type': ['null', 'number'],
                        'description': 'Discount amount',
                    },
                    'subject': {
                        'type': ['null', 'string'],
                        'description': 'Subject of the invoice',
                    },
                    'notes': {
                        'type': ['null', 'string'],
                        'description': 'Notes on the invoice',
                    },
                    'currency': {
                        'type': ['null', 'string'],
                        'description': 'Currency code for the invoice',
                    },
                    'state': {
                        'type': ['null', 'string'],
                        'description': 'State of the invoice (draft, open, paid, closed)',
                    },
                    'period_start': {
                        'type': ['null', 'string'],
                        'description': 'Start of the invoice period',
                    },
                    'period_end': {
                        'type': ['null', 'string'],
                        'description': 'End of the invoice period',
                    },
                    'issue_date': {
                        'type': ['null', 'string'],
                        'description': 'Date the invoice was issued',
                    },
                    'due_date': {
                        'type': ['null', 'string'],
                        'description': 'Date the invoice is due',
                    },
                    'payment_term': {
                        'type': ['null', 'string'],
                        'description': 'Payment term for the invoice',
                    },
                    'payment_options': {
                        'type': ['null', 'array'],
                        'description': 'Available payment options',
                        'items': {'type': 'string'},
                    },
                    'sent_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the invoice was sent',
                    },
                    'paid_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the invoice was paid',
                    },
                    'paid_date': {
                        'type': ['null', 'string'],
                        'description': 'Date the invoice was paid',
                    },
                    'closed_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the invoice was closed',
                    },
                    'recurring_invoice_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the recurring invoice',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the invoice was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the invoice was last updated',
                    },
                    'client': {
                        'type': ['null', 'object'],
                        'description': 'The client associated with the invoice',
                    },
                    'estimate': {
                        'type': ['null', 'object'],
                        'description': 'The estimate associated with the invoice',
                    },
                    'retainer': {
                        'type': ['null', 'object'],
                        'description': 'The retainer associated with the invoice',
                    },
                    'creator': {
                        'type': ['null', 'object'],
                        'description': 'The creator of the invoice',
                    },
                    'line_items': {
                        'type': ['null', 'array'],
                        'description': 'Line items on the invoice',
                        'items': {'type': 'object'},
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'invoices',
                'x-airbyte-stream-name': 'invoices',
            },
        ),
        EntityDefinition(
            name='invoice_item_categories',
            stream_name='invoice_item_categories',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/invoice_item_categories',
                    action=Action.LIST,
                    description='Returns a paginated list of invoice item categories',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of invoice item categories',
                        'properties': {
                            'invoice_item_categories': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest invoice item category',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique invoice item category ID'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the category',
                                        },
                                        'use_as_service': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the category is used as a service',
                                        },
                                        'use_as_expense': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the category is used as an expense',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the category was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the category was last updated',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'invoice_item_categories',
                                    'x-airbyte-stream-name': 'invoice_item_categories',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.invoice_item_categories',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/invoice_item_categories/{id}',
                    action=Action.GET,
                    description='Get a single invoice item category by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest invoice item category',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique invoice item category ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the category',
                            },
                            'use_as_service': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the category is used as a service',
                            },
                            'use_as_expense': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the category is used as an expense',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the category was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the category was last updated',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'invoice_item_categories',
                        'x-airbyte-stream-name': 'invoice_item_categories',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest invoice item category',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique invoice item category ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the category',
                    },
                    'use_as_service': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the category is used as a service',
                    },
                    'use_as_expense': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the category is used as an expense',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the category was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the category was last updated',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'invoice_item_categories',
                'x-airbyte-stream-name': 'invoice_item_categories',
            },
        ),
        EntityDefinition(
            name='estimates',
            stream_name='estimates',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/estimates',
                    action=Action.LIST,
                    description='Returns a paginated list of estimates',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of estimates',
                        'properties': {
                            'estimates': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest estimate',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique estimate ID'},
                                        'client_key': {
                                            'type': ['null', 'string'],
                                            'description': 'Client key for the estimate',
                                        },
                                        'number': {
                                            'type': ['null', 'string'],
                                            'description': 'Estimate number',
                                        },
                                        'purchase_order': {
                                            'type': ['null', 'string'],
                                            'description': 'Purchase order number',
                                        },
                                        'amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Total amount of the estimate',
                                        },
                                        'tax': {
                                            'type': ['null', 'number'],
                                            'description': 'Tax percentage',
                                        },
                                        'tax_amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Tax amount',
                                        },
                                        'tax2': {
                                            'type': ['null', 'number'],
                                            'description': 'Second tax percentage',
                                        },
                                        'tax2_amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Second tax amount',
                                        },
                                        'discount': {
                                            'type': ['null', 'number'],
                                            'description': 'Discount percentage',
                                        },
                                        'discount_amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Discount amount',
                                        },
                                        'subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Subject of the estimate',
                                        },
                                        'notes': {
                                            'type': ['null', 'string'],
                                            'description': 'Notes on the estimate',
                                        },
                                        'currency': {
                                            'type': ['null', 'string'],
                                            'description': 'Currency code for the estimate',
                                        },
                                        'state': {
                                            'type': ['null', 'string'],
                                            'description': 'State of the estimate (draft, sent, accepted, declined)',
                                        },
                                        'issue_date': {
                                            'type': ['null', 'string'],
                                            'description': 'Date the estimate was issued',
                                        },
                                        'sent_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the estimate was sent',
                                        },
                                        'accepted_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the estimate was accepted',
                                        },
                                        'declined_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the estimate was declined',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the estimate was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the estimate was last updated',
                                        },
                                        'client': {
                                            'type': ['null', 'object'],
                                            'description': 'The client associated with the estimate',
                                        },
                                        'creator': {
                                            'type': ['null', 'object'],
                                            'description': 'The creator of the estimate',
                                        },
                                        'line_items': {
                                            'type': ['null', 'array'],
                                            'description': 'Line items on the estimate',
                                            'items': {'type': 'object'},
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'estimates',
                                    'x-airbyte-stream-name': 'estimates',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.estimates',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/estimates/{id}',
                    action=Action.GET,
                    description='Get a single estimate by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest estimate',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique estimate ID'},
                            'client_key': {
                                'type': ['null', 'string'],
                                'description': 'Client key for the estimate',
                            },
                            'number': {
                                'type': ['null', 'string'],
                                'description': 'Estimate number',
                            },
                            'purchase_order': {
                                'type': ['null', 'string'],
                                'description': 'Purchase order number',
                            },
                            'amount': {
                                'type': ['null', 'number'],
                                'description': 'Total amount of the estimate',
                            },
                            'tax': {
                                'type': ['null', 'number'],
                                'description': 'Tax percentage',
                            },
                            'tax_amount': {
                                'type': ['null', 'number'],
                                'description': 'Tax amount',
                            },
                            'tax2': {
                                'type': ['null', 'number'],
                                'description': 'Second tax percentage',
                            },
                            'tax2_amount': {
                                'type': ['null', 'number'],
                                'description': 'Second tax amount',
                            },
                            'discount': {
                                'type': ['null', 'number'],
                                'description': 'Discount percentage',
                            },
                            'discount_amount': {
                                'type': ['null', 'number'],
                                'description': 'Discount amount',
                            },
                            'subject': {
                                'type': ['null', 'string'],
                                'description': 'Subject of the estimate',
                            },
                            'notes': {
                                'type': ['null', 'string'],
                                'description': 'Notes on the estimate',
                            },
                            'currency': {
                                'type': ['null', 'string'],
                                'description': 'Currency code for the estimate',
                            },
                            'state': {
                                'type': ['null', 'string'],
                                'description': 'State of the estimate (draft, sent, accepted, declined)',
                            },
                            'issue_date': {
                                'type': ['null', 'string'],
                                'description': 'Date the estimate was issued',
                            },
                            'sent_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the estimate was sent',
                            },
                            'accepted_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the estimate was accepted',
                            },
                            'declined_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the estimate was declined',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the estimate was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the estimate was last updated',
                            },
                            'client': {
                                'type': ['null', 'object'],
                                'description': 'The client associated with the estimate',
                            },
                            'creator': {
                                'type': ['null', 'object'],
                                'description': 'The creator of the estimate',
                            },
                            'line_items': {
                                'type': ['null', 'array'],
                                'description': 'Line items on the estimate',
                                'items': {'type': 'object'},
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'estimates',
                        'x-airbyte-stream-name': 'estimates',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest estimate',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique estimate ID'},
                    'client_key': {
                        'type': ['null', 'string'],
                        'description': 'Client key for the estimate',
                    },
                    'number': {
                        'type': ['null', 'string'],
                        'description': 'Estimate number',
                    },
                    'purchase_order': {
                        'type': ['null', 'string'],
                        'description': 'Purchase order number',
                    },
                    'amount': {
                        'type': ['null', 'number'],
                        'description': 'Total amount of the estimate',
                    },
                    'tax': {
                        'type': ['null', 'number'],
                        'description': 'Tax percentage',
                    },
                    'tax_amount': {
                        'type': ['null', 'number'],
                        'description': 'Tax amount',
                    },
                    'tax2': {
                        'type': ['null', 'number'],
                        'description': 'Second tax percentage',
                    },
                    'tax2_amount': {
                        'type': ['null', 'number'],
                        'description': 'Second tax amount',
                    },
                    'discount': {
                        'type': ['null', 'number'],
                        'description': 'Discount percentage',
                    },
                    'discount_amount': {
                        'type': ['null', 'number'],
                        'description': 'Discount amount',
                    },
                    'subject': {
                        'type': ['null', 'string'],
                        'description': 'Subject of the estimate',
                    },
                    'notes': {
                        'type': ['null', 'string'],
                        'description': 'Notes on the estimate',
                    },
                    'currency': {
                        'type': ['null', 'string'],
                        'description': 'Currency code for the estimate',
                    },
                    'state': {
                        'type': ['null', 'string'],
                        'description': 'State of the estimate (draft, sent, accepted, declined)',
                    },
                    'issue_date': {
                        'type': ['null', 'string'],
                        'description': 'Date the estimate was issued',
                    },
                    'sent_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the estimate was sent',
                    },
                    'accepted_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the estimate was accepted',
                    },
                    'declined_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the estimate was declined',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the estimate was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the estimate was last updated',
                    },
                    'client': {
                        'type': ['null', 'object'],
                        'description': 'The client associated with the estimate',
                    },
                    'creator': {
                        'type': ['null', 'object'],
                        'description': 'The creator of the estimate',
                    },
                    'line_items': {
                        'type': ['null', 'array'],
                        'description': 'Line items on the estimate',
                        'items': {'type': 'object'},
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'estimates',
                'x-airbyte-stream-name': 'estimates',
            },
        ),
        EntityDefinition(
            name='estimate_item_categories',
            stream_name='estimate_item_categories',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/estimate_item_categories',
                    action=Action.LIST,
                    description='Returns a paginated list of estimate item categories',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of estimate item categories',
                        'properties': {
                            'estimate_item_categories': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest estimate item category',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique estimate item category ID'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the category',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the category was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the category was last updated',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'estimate_item_categories',
                                    'x-airbyte-stream-name': 'estimate_item_categories',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.estimate_item_categories',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/estimate_item_categories/{id}',
                    action=Action.GET,
                    description='Get a single estimate item category by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest estimate item category',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique estimate item category ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the category',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the category was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the category was last updated',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'estimate_item_categories',
                        'x-airbyte-stream-name': 'estimate_item_categories',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest estimate item category',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique estimate item category ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the category',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the category was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the category was last updated',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'estimate_item_categories',
                'x-airbyte-stream-name': 'estimate_item_categories',
            },
        ),
        EntityDefinition(
            name='expenses',
            stream_name='expenses',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/expenses',
                    action=Action.LIST,
                    description='Returns a paginated list of expenses',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of expenses',
                        'properties': {
                            'expenses': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest expense',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique expense ID'},
                                        'notes': {
                                            'type': ['null', 'string'],
                                            'description': 'Notes about the expense',
                                        },
                                        'total_cost': {
                                            'type': ['null', 'number'],
                                            'description': 'Total cost of the expense',
                                        },
                                        'units': {
                                            'type': ['null', 'number'],
                                            'description': 'Number of units',
                                        },
                                        'is_closed': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the expense is closed',
                                        },
                                        'is_locked': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the expense is locked',
                                        },
                                        'is_billed': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the expense has been billed',
                                        },
                                        'locked_reason': {
                                            'type': ['null', 'string'],
                                            'description': 'Reason the expense is locked',
                                        },
                                        'spent_date': {
                                            'type': ['null', 'string'],
                                            'description': 'Date the expense was incurred',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the expense was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the expense was last updated',
                                        },
                                        'billable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the expense is billable',
                                        },
                                        'approval_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Approval status of the expense',
                                        },
                                        'is_explicitly_locked': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the expense is explicitly locked',
                                        },
                                        'receipt': {
                                            'type': ['null', 'object'],
                                            'description': 'Receipt attached to the expense',
                                        },
                                        'user': {
                                            'type': ['null', 'object'],
                                            'description': 'The user who created the expense',
                                        },
                                        'user_assignment': {
                                            'type': ['null', 'object'],
                                            'description': 'The user assignment associated with the expense',
                                        },
                                        'project': {
                                            'type': ['null', 'object'],
                                            'description': 'The project associated with the expense',
                                        },
                                        'expense_category': {
                                            'type': ['null', 'object'],
                                            'description': 'The expense category',
                                        },
                                        'client': {
                                            'type': ['null', 'object'],
                                            'description': 'The client associated with the expense',
                                        },
                                        'invoice': {
                                            'type': ['null', 'object'],
                                            'description': 'The invoice associated with the expense',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'expenses',
                                    'x-airbyte-stream-name': 'expenses',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.expenses',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/expenses/{id}',
                    action=Action.GET,
                    description='Get a single expense by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest expense',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique expense ID'},
                            'notes': {
                                'type': ['null', 'string'],
                                'description': 'Notes about the expense',
                            },
                            'total_cost': {
                                'type': ['null', 'number'],
                                'description': 'Total cost of the expense',
                            },
                            'units': {
                                'type': ['null', 'number'],
                                'description': 'Number of units',
                            },
                            'is_closed': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the expense is closed',
                            },
                            'is_locked': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the expense is locked',
                            },
                            'is_billed': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the expense has been billed',
                            },
                            'locked_reason': {
                                'type': ['null', 'string'],
                                'description': 'Reason the expense is locked',
                            },
                            'spent_date': {
                                'type': ['null', 'string'],
                                'description': 'Date the expense was incurred',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the expense was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the expense was last updated',
                            },
                            'billable': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the expense is billable',
                            },
                            'approval_status': {
                                'type': ['null', 'string'],
                                'description': 'Approval status of the expense',
                            },
                            'is_explicitly_locked': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the expense is explicitly locked',
                            },
                            'receipt': {
                                'type': ['null', 'object'],
                                'description': 'Receipt attached to the expense',
                            },
                            'user': {
                                'type': ['null', 'object'],
                                'description': 'The user who created the expense',
                            },
                            'user_assignment': {
                                'type': ['null', 'object'],
                                'description': 'The user assignment associated with the expense',
                            },
                            'project': {
                                'type': ['null', 'object'],
                                'description': 'The project associated with the expense',
                            },
                            'expense_category': {
                                'type': ['null', 'object'],
                                'description': 'The expense category',
                            },
                            'client': {
                                'type': ['null', 'object'],
                                'description': 'The client associated with the expense',
                            },
                            'invoice': {
                                'type': ['null', 'object'],
                                'description': 'The invoice associated with the expense',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'expenses',
                        'x-airbyte-stream-name': 'expenses',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest expense',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique expense ID'},
                    'notes': {
                        'type': ['null', 'string'],
                        'description': 'Notes about the expense',
                    },
                    'total_cost': {
                        'type': ['null', 'number'],
                        'description': 'Total cost of the expense',
                    },
                    'units': {
                        'type': ['null', 'number'],
                        'description': 'Number of units',
                    },
                    'is_closed': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the expense is closed',
                    },
                    'is_locked': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the expense is locked',
                    },
                    'is_billed': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the expense has been billed',
                    },
                    'locked_reason': {
                        'type': ['null', 'string'],
                        'description': 'Reason the expense is locked',
                    },
                    'spent_date': {
                        'type': ['null', 'string'],
                        'description': 'Date the expense was incurred',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the expense was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the expense was last updated',
                    },
                    'billable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the expense is billable',
                    },
                    'approval_status': {
                        'type': ['null', 'string'],
                        'description': 'Approval status of the expense',
                    },
                    'is_explicitly_locked': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the expense is explicitly locked',
                    },
                    'receipt': {
                        'type': ['null', 'object'],
                        'description': 'Receipt attached to the expense',
                    },
                    'user': {
                        'type': ['null', 'object'],
                        'description': 'The user who created the expense',
                    },
                    'user_assignment': {
                        'type': ['null', 'object'],
                        'description': 'The user assignment associated with the expense',
                    },
                    'project': {
                        'type': ['null', 'object'],
                        'description': 'The project associated with the expense',
                    },
                    'expense_category': {
                        'type': ['null', 'object'],
                        'description': 'The expense category',
                    },
                    'client': {
                        'type': ['null', 'object'],
                        'description': 'The client associated with the expense',
                    },
                    'invoice': {
                        'type': ['null', 'object'],
                        'description': 'The invoice associated with the expense',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'expenses',
                'x-airbyte-stream-name': 'expenses',
            },
        ),
        EntityDefinition(
            name='expense_categories',
            stream_name='expense_categories',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/expense_categories',
                    action=Action.LIST,
                    description='Returns a paginated list of expense categories',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of expense categories',
                        'properties': {
                            'expense_categories': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest expense category',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique expense category ID'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the expense category',
                                        },
                                        'unit_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Unit name for the expense category',
                                        },
                                        'unit_price': {
                                            'type': ['null', 'number'],
                                            'description': 'Unit price for the expense category',
                                        },
                                        'is_active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the expense category is active',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the expense category was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the expense category was last updated',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'expense_categories',
                                    'x-airbyte-stream-name': 'expense_categories',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.expense_categories',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/expense_categories/{id}',
                    action=Action.GET,
                    description='Get a single expense category by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest expense category',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique expense category ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the expense category',
                            },
                            'unit_name': {
                                'type': ['null', 'string'],
                                'description': 'Unit name for the expense category',
                            },
                            'unit_price': {
                                'type': ['null', 'number'],
                                'description': 'Unit price for the expense category',
                            },
                            'is_active': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the expense category is active',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the expense category was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the expense category was last updated',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'expense_categories',
                        'x-airbyte-stream-name': 'expense_categories',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest expense category',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique expense category ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the expense category',
                    },
                    'unit_name': {
                        'type': ['null', 'string'],
                        'description': 'Unit name for the expense category',
                    },
                    'unit_price': {
                        'type': ['null', 'number'],
                        'description': 'Unit price for the expense category',
                    },
                    'is_active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the expense category is active',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the expense category was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the expense category was last updated',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'expense_categories',
                'x-airbyte-stream-name': 'expense_categories',
            },
        ),
        EntityDefinition(
            name='roles',
            stream_name='roles',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/roles',
                    action=Action.LIST,
                    description='Returns a paginated list of roles',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of roles',
                        'properties': {
                            'roles': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest role',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique role ID'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the role',
                                        },
                                        'user_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'IDs of users assigned to this role',
                                            'items': {'type': 'integer'},
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the role was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the role was last updated',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'roles',
                                    'x-airbyte-stream-name': 'roles',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.roles',
                    meta_extractor={'next_link': '$.links.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/roles/{id}',
                    action=Action.GET,
                    description='Get a single role by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Harvest role',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique role ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the role',
                            },
                            'user_ids': {
                                'type': ['null', 'array'],
                                'description': 'IDs of users assigned to this role',
                                'items': {'type': 'integer'},
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the role was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the role was last updated',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'roles',
                        'x-airbyte-stream-name': 'roles',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest role',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique role ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the role',
                    },
                    'user_ids': {
                        'type': ['null', 'array'],
                        'description': 'IDs of users assigned to this role',
                        'items': {'type': 'integer'},
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the role was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the role was last updated',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'roles',
                'x-airbyte-stream-name': 'roles',
            },
        ),
        EntityDefinition(
            name='user_assignments',
            stream_name='user_assignments',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/user_assignments',
                    action=Action.LIST,
                    description='Returns a paginated list of user assignments across all projects',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of user assignments',
                        'properties': {
                            'user_assignments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest user assignment linking a user to a project',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique user assignment ID'},
                                        'is_project_manager': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the user is the project manager',
                                        },
                                        'is_active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the assignment is active',
                                        },
                                        'budget': {
                                            'type': ['null', 'number'],
                                            'description': 'Budget for the user assignment',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the assignment was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the assignment was last updated',
                                        },
                                        'hourly_rate': {
                                            'type': ['null', 'number'],
                                            'description': 'Hourly rate for the assignment',
                                        },
                                        'use_default_rates': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the assignment uses default rates',
                                        },
                                        'project': {
                                            'type': ['null', 'object'],
                                            'description': 'The project associated with the assignment',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Project ID',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Project name',
                                                },
                                                'code': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Project code',
                                                },
                                            },
                                        },
                                        'user': {
                                            'type': ['null', 'object'],
                                            'description': 'The user associated with the assignment',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'User ID',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'User name',
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'user_assignments',
                                    'x-airbyte-stream-name': 'user_assignments',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.user_assignments',
                    meta_extractor={'next_link': '$.links.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest user assignment linking a user to a project',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique user assignment ID'},
                    'is_project_manager': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user is the project manager',
                    },
                    'is_active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the assignment is active',
                    },
                    'budget': {
                        'type': ['null', 'number'],
                        'description': 'Budget for the user assignment',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the assignment was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the assignment was last updated',
                    },
                    'hourly_rate': {
                        'type': ['null', 'number'],
                        'description': 'Hourly rate for the assignment',
                    },
                    'use_default_rates': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the assignment uses default rates',
                    },
                    'project': {
                        'type': ['null', 'object'],
                        'description': 'The project associated with the assignment',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Project ID',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Project name',
                            },
                            'code': {
                                'type': ['null', 'string'],
                                'description': 'Project code',
                            },
                        },
                    },
                    'user': {
                        'type': ['null', 'object'],
                        'description': 'The user associated with the assignment',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'User ID',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'User name',
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'user_assignments',
                'x-airbyte-stream-name': 'user_assignments',
            },
        ),
        EntityDefinition(
            name='task_assignments',
            stream_name='task_assignments',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/task_assignments',
                    action=Action.LIST,
                    description='Returns a paginated list of task assignments across all projects',
                    query_params=['per_page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of task assignments',
                        'properties': {
                            'task_assignments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Harvest task assignment linking a task to a project',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique task assignment ID'},
                                        'billable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the task assignment is billable',
                                        },
                                        'is_active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the assignment is active',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the assignment was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the assignment was last updated',
                                        },
                                        'hourly_rate': {
                                            'type': ['null', 'number'],
                                            'description': 'Hourly rate for the assignment',
                                        },
                                        'budget': {
                                            'type': ['null', 'number'],
                                            'description': 'Budget for the task assignment',
                                        },
                                        'project': {
                                            'type': ['null', 'object'],
                                            'description': 'The project associated with the assignment',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Project ID',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Project name',
                                                },
                                                'code': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Project code',
                                                },
                                            },
                                        },
                                        'task': {
                                            'type': ['null', 'object'],
                                            'description': 'The task associated with the assignment',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Task ID',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Task name',
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'task_assignments',
                                    'x-airbyte-stream-name': 'task_assignments',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.task_assignments',
                    meta_extractor={'next_link': '$.links.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Harvest task assignment linking a task to a project',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique task assignment ID'},
                    'billable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the task assignment is billable',
                    },
                    'is_active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the assignment is active',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the assignment was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the assignment was last updated',
                    },
                    'hourly_rate': {
                        'type': ['null', 'number'],
                        'description': 'Hourly rate for the assignment',
                    },
                    'budget': {
                        'type': ['null', 'number'],
                        'description': 'Budget for the task assignment',
                    },
                    'project': {
                        'type': ['null', 'object'],
                        'description': 'The project associated with the assignment',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Project ID',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Project name',
                            },
                            'code': {
                                'type': ['null', 'string'],
                                'description': 'Project code',
                            },
                        },
                    },
                    'task': {
                        'type': ['null', 'object'],
                        'description': 'The task associated with the assignment',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Task ID',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Task name',
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'task_assignments',
                'x-airbyte-stream-name': 'task_assignments',
            },
        ),
        EntityDefinition(
            name='time_projects',
            stream_name='time_projects',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/reports/time/projects',
                    action=Action.LIST,
                    description='Returns time report data grouped by project for a given date range',
                    query_params=['from', 'to', 'per_page'],
                    query_params_schema={
                        'from': {
                            'type': 'string',
                            'required': True,
                            'default': '20200101',
                        },
                        'to': {
                            'type': 'string',
                            'required': True,
                            'default': '21000101',
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of time report entries by project',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A time report entry grouped by project',
                                    'properties': {
                                        'project_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique identifier for the project',
                                        },
                                        'project_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the project',
                                        },
                                        'client_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique identifier for the client associated with this project',
                                        },
                                        'client_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the client associated with this project',
                                        },
                                        'total_hours': {
                                            'type': ['null', 'number'],
                                            'description': 'Total number of hours spent on this project',
                                        },
                                        'billable_hours': {
                                            'type': ['null', 'number'],
                                            'description': 'Number of billable hours spent on this project',
                                        },
                                        'currency': {
                                            'type': ['null', 'string'],
                                            'description': 'Currency code for the billable amount',
                                        },
                                        'billable_amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Total billable amount for this project',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'time_projects',
                                    'x-airbyte-stream-name': 'time_projects',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_link': '$.links.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A time report entry grouped by project',
                'properties': {
                    'project_id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the project',
                    },
                    'project_name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the project',
                    },
                    'client_id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the client associated with this project',
                    },
                    'client_name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the client associated with this project',
                    },
                    'total_hours': {
                        'type': ['null', 'number'],
                        'description': 'Total number of hours spent on this project',
                    },
                    'billable_hours': {
                        'type': ['null', 'number'],
                        'description': 'Number of billable hours spent on this project',
                    },
                    'currency': {
                        'type': ['null', 'string'],
                        'description': 'Currency code for the billable amount',
                    },
                    'billable_amount': {
                        'type': ['null', 'number'],
                        'description': 'Total billable amount for this project',
                    },
                },
                'x-airbyte-entity-name': 'time_projects',
                'x-airbyte-stream-name': 'time_projects',
            },
        ),
        EntityDefinition(
            name='time_tasks',
            stream_name='time_tasks',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/reports/time/tasks',
                    action=Action.LIST,
                    description='Returns time report data grouped by task for a given date range',
                    query_params=['from', 'to', 'per_page'],
                    query_params_schema={
                        'from': {
                            'type': 'string',
                            'required': True,
                            'default': '20200101',
                        },
                        'to': {
                            'type': 'string',
                            'required': True,
                            'default': '21000101',
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of time report entries by task',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A time report entry grouped by task',
                                    'properties': {
                                        'task_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique identifier for the task',
                                        },
                                        'task_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the task',
                                        },
                                        'total_hours': {
                                            'type': ['null', 'number'],
                                            'description': 'Total number of hours spent on this task',
                                        },
                                        'billable_hours': {
                                            'type': ['null', 'number'],
                                            'description': 'Number of billable hours spent on this task',
                                        },
                                        'currency': {
                                            'type': ['null', 'string'],
                                            'description': 'Currency code for the billable amount',
                                        },
                                        'billable_amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Total billable amount for this task',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'time_tasks',
                                    'x-airbyte-stream-name': 'time_tasks',
                                },
                            },
                            'per_page': {'type': 'integer', 'description': 'Number of records per page'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages'},
                            'total_entries': {'type': 'integer', 'description': 'Total number of entries'},
                            'page': {'type': 'integer', 'description': 'Current page number'},
                            'next_page': {
                                'type': ['null', 'integer'],
                                'description': 'The next page number',
                            },
                            'previous_page': {
                                'type': ['null', 'integer'],
                                'description': 'The previous page number',
                            },
                            'links': {
                                'type': 'object',
                                'description': 'Pagination links for navigating result pages',
                                'properties': {
                                    'first': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the first page of results',
                                    },
                                    'previous': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the previous page of results',
                                    },
                                    'next': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the next page of results',
                                    },
                                    'last': {
                                        'type': ['null', 'string'],
                                        'description': 'URL to the last page of results',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_link': '$.links.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A time report entry grouped by task',
                'properties': {
                    'task_id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the task',
                    },
                    'task_name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the task',
                    },
                    'total_hours': {
                        'type': ['null', 'number'],
                        'description': 'Total number of hours spent on this task',
                    },
                    'billable_hours': {
                        'type': ['null', 'number'],
                        'description': 'Number of billable hours spent on this task',
                    },
                    'currency': {
                        'type': ['null', 'string'],
                        'description': 'Currency code for the billable amount',
                    },
                    'billable_amount': {
                        'type': ['null', 'number'],
                        'description': 'Total billable amount for this task',
                    },
                },
                'x-airbyte-entity-name': 'time_tasks',
                'x-airbyte-stream-name': 'time_tasks',
            },
        ),
    ],
    search_field_paths={
        'clients': [
            'address',
            'created_at',
            'currency',
            'id',
            'is_active',
            'name',
            'updated_at',
        ],
        'company': [
            'base_uri',
            'currency',
            'full_domain',
            'is_active',
            'name',
            'plan_type',
            'weekly_capacity',
        ],
        'contacts': [
            'client',
            'created_at',
            'email',
            'first_name',
            'id',
            'last_name',
            'title',
            'updated_at',
        ],
        'estimate_item_categories': [
            'created_at',
            'id',
            'name',
            'updated_at',
        ],
        'estimates': [
            'amount',
            'client',
            'created_at',
            'currency',
            'id',
            'issue_date',
            'number',
            'state',
            'subject',
            'updated_at',
        ],
        'expense_categories': [
            'created_at',
            'id',
            'is_active',
            'name',
            'unit_name',
            'unit_price',
            'updated_at',
        ],
        'expenses': [
            'billable',
            'client',
            'created_at',
            'expense_category',
            'id',
            'is_billed',
            'notes',
            'project',
            'spent_date',
            'total_cost',
            'updated_at',
            'user',
        ],
        'invoice_item_categories': [
            'created_at',
            'id',
            'name',
            'updated_at',
            'use_as_expense',
            'use_as_service',
        ],
        'invoices': [
            'amount',
            'client',
            'created_at',
            'currency',
            'due_amount',
            'due_date',
            'id',
            'issue_date',
            'number',
            'state',
            'subject',
            'updated_at',
        ],
        'projects': [
            'budget',
            'client',
            'code',
            'created_at',
            'hourly_rate',
            'id',
            'is_active',
            'is_billable',
            'name',
            'starts_on',
            'updated_at',
        ],
        'roles': [
            'created_at',
            'id',
            'name',
            'updated_at',
            'user_ids',
            'user_ids[]',
        ],
        'task_assignments': [
            'billable',
            'created_at',
            'hourly_rate',
            'id',
            'is_active',
            'project',
            'task',
            'updated_at',
        ],
        'tasks': [
            'billable_by_default',
            'created_at',
            'default_hourly_rate',
            'id',
            'is_active',
            'name',
            'updated_at',
        ],
        'time_entries': [
            'billable',
            'client',
            'created_at',
            'hours',
            'id',
            'is_billed',
            'notes',
            'project',
            'spent_date',
            'task',
            'updated_at',
            'user',
        ],
        'time_projects': [
            'billable_amount',
            'billable_hours',
            'client_id',
            'client_name',
            'currency',
            'project_id',
            'project_name',
            'total_hours',
        ],
        'time_tasks': [
            'billable_amount',
            'billable_hours',
            'currency',
            'task_id',
            'task_name',
            'total_hours',
        ],
        'user_assignments': [
            'budget',
            'created_at',
            'hourly_rate',
            'id',
            'is_active',
            'is_project_manager',
            'project',
            'updated_at',
            'user',
        ],
        'users': [
            'avatar_url',
            'cost_rate',
            'created_at',
            'default_hourly_rate',
            'email',
            'first_name',
            'id',
            'is_active',
            'is_contractor',
            'last_name',
            'roles',
            'roles[]',
            'telephone',
            'timezone',
            'updated_at',
            'weekly_capacity',
        ],
    },
)