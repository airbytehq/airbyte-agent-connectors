"""
Connector model for klaviyo.

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

KlaviyoConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('95e8cffd-b8c4-4039-968e-d32fb4a69bde'),
    name='klaviyo',
    base_url='https://a.klaviyo.com/api',
    auth=AuthConfig(
        type=AuthType.API_KEY,
        config={'header': 'Authorization', 'in': 'header'},
        user_config_spec=AirbyteAuthConfig(
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Your Klaviyo private API key',
                ),
            },
            auth_mapping={'api_key': 'Klaviyo-API-Key ${api_key}'},
            replication_auth_key_mapping={'api_key': 'api_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='profiles',
            stream_name='profiles',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/profiles',
                    action=Action.LIST,
                    description='Returns a paginated list of profiles (contacts) in your Klaviyo account',
                    query_params=['page[size]', 'page[cursor]'],
                    query_params_schema={
                        'page[size]': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'page[cursor]': {'type': 'string', 'required': False},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of profiles',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Klaviyo profile representing a contact',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique profile identifier'},
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type (always "profile")',
                                        },
                                        'attributes': {
                                            'type': ['object', 'null'],
                                            'description': 'Profile attributes',
                                            'properties': {
                                                'email': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Email address',
                                                },
                                                'phone_number': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Phone number',
                                                },
                                                'external_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'External identifier',
                                                },
                                                'first_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'First name',
                                                },
                                                'last_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Last name',
                                                },
                                                'organization': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Organization name',
                                                },
                                                'title': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Job title',
                                                },
                                                'image': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Profile image URL',
                                                },
                                                'created': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Creation timestamp',
                                                },
                                                'updated': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Last update timestamp',
                                                },
                                                'location': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Location information',
                                                    'properties': {
                                                        'address1': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address2': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'region': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'zip': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'timezone': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'latitude': {
                                                            'type': ['number', 'null'],
                                                        },
                                                        'longitude': {
                                                            'type': ['number', 'null'],
                                                        },
                                                    },
                                                },
                                                'properties': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Custom properties',
                                                },
                                            },
                                        },
                                        'links': {
                                            'type': ['object', 'null'],
                                            'description': 'Related links',
                                            'properties': {
                                                'self': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'profiles',
                                    'x-airbyte-stream-name': 'profiles',
                                },
                            },
                            'links': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'self': {
                                        'type': ['string', 'null'],
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                    },
                                    'prev': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/profiles/{id}',
                    action=Action.GET,
                    description='Get a single profile by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A Klaviyo profile representing a contact',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique profile identifier'},
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Object type (always "profile")',
                                    },
                                    'attributes': {
                                        'type': ['object', 'null'],
                                        'description': 'Profile attributes',
                                        'properties': {
                                            'email': {
                                                'type': ['string', 'null'],
                                                'description': 'Email address',
                                            },
                                            'phone_number': {
                                                'type': ['string', 'null'],
                                                'description': 'Phone number',
                                            },
                                            'external_id': {
                                                'type': ['string', 'null'],
                                                'description': 'External identifier',
                                            },
                                            'first_name': {
                                                'type': ['string', 'null'],
                                                'description': 'First name',
                                            },
                                            'last_name': {
                                                'type': ['string', 'null'],
                                                'description': 'Last name',
                                            },
                                            'organization': {
                                                'type': ['string', 'null'],
                                                'description': 'Organization name',
                                            },
                                            'title': {
                                                'type': ['string', 'null'],
                                                'description': 'Job title',
                                            },
                                            'image': {
                                                'type': ['string', 'null'],
                                                'description': 'Profile image URL',
                                            },
                                            'created': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Creation timestamp',
                                            },
                                            'updated': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Last update timestamp',
                                            },
                                            'location': {
                                                'type': ['object', 'null'],
                                                'description': 'Location information',
                                                'properties': {
                                                    'address1': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'address2': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'city': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'country': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'region': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'zip': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'timezone': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'latitude': {
                                                        'type': ['number', 'null'],
                                                    },
                                                    'longitude': {
                                                        'type': ['number', 'null'],
                                                    },
                                                },
                                            },
                                            'properties': {
                                                'type': ['object', 'null'],
                                                'description': 'Custom properties',
                                            },
                                        },
                                    },
                                    'links': {
                                        'type': ['object', 'null'],
                                        'description': 'Related links',
                                        'properties': {
                                            'self': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'profiles',
                                'x-airbyte-stream-name': 'profiles',
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Klaviyo profile representing a contact',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique profile identifier'},
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Object type (always "profile")',
                    },
                    'attributes': {
                        'type': ['object', 'null'],
                        'description': 'Profile attributes',
                        'properties': {
                            'email': {
                                'type': ['string', 'null'],
                                'description': 'Email address',
                            },
                            'phone_number': {
                                'type': ['string', 'null'],
                                'description': 'Phone number',
                            },
                            'external_id': {
                                'type': ['string', 'null'],
                                'description': 'External identifier',
                            },
                            'first_name': {
                                'type': ['string', 'null'],
                                'description': 'First name',
                            },
                            'last_name': {
                                'type': ['string', 'null'],
                                'description': 'Last name',
                            },
                            'organization': {
                                'type': ['string', 'null'],
                                'description': 'Organization name',
                            },
                            'title': {
                                'type': ['string', 'null'],
                                'description': 'Job title',
                            },
                            'image': {
                                'type': ['string', 'null'],
                                'description': 'Profile image URL',
                            },
                            'created': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updated': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'location': {
                                'type': ['object', 'null'],
                                'description': 'Location information',
                                'properties': {
                                    'address1': {
                                        'type': ['string', 'null'],
                                    },
                                    'address2': {
                                        'type': ['string', 'null'],
                                    },
                                    'city': {
                                        'type': ['string', 'null'],
                                    },
                                    'country': {
                                        'type': ['string', 'null'],
                                    },
                                    'region': {
                                        'type': ['string', 'null'],
                                    },
                                    'zip': {
                                        'type': ['string', 'null'],
                                    },
                                    'timezone': {
                                        'type': ['string', 'null'],
                                    },
                                    'latitude': {
                                        'type': ['number', 'null'],
                                    },
                                    'longitude': {
                                        'type': ['number', 'null'],
                                    },
                                },
                            },
                            'properties': {
                                'type': ['object', 'null'],
                                'description': 'Custom properties',
                            },
                        },
                    },
                    'links': {
                        'type': ['object', 'null'],
                        'description': 'Related links',
                        'properties': {
                            'self': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'profiles',
                'x-airbyte-stream-name': 'profiles',
            },
        ),
        EntityDefinition(
            name='lists',
            stream_name='lists',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/lists',
                    action=Action.LIST,
                    description='Returns a paginated list of all lists in your Klaviyo account',
                    query_params=['page[size]', 'page[cursor]'],
                    query_params_schema={
                        'page[size]': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'page[cursor]': {'type': 'string', 'required': False},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of lists',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Klaviyo list for organizing profiles',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique list identifier'},
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type (always "list")',
                                        },
                                        'attributes': {
                                            'type': ['object', 'null'],
                                            'description': 'List attributes',
                                            'properties': {
                                                'name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'List name',
                                                },
                                                'created': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Creation timestamp',
                                                },
                                                'updated': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Last update timestamp',
                                                },
                                                'opt_in_process': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Opt-in process type',
                                                },
                                            },
                                        },
                                        'links': {
                                            'type': ['object', 'null'],
                                            'description': 'Related links',
                                            'properties': {
                                                'self': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'lists',
                                    'x-airbyte-stream-name': 'lists',
                                },
                            },
                            'links': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'self': {
                                        'type': ['string', 'null'],
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                    },
                                    'prev': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/lists/{id}',
                    action=Action.GET,
                    description='Get a single list by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A Klaviyo list for organizing profiles',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique list identifier'},
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Object type (always "list")',
                                    },
                                    'attributes': {
                                        'type': ['object', 'null'],
                                        'description': 'List attributes',
                                        'properties': {
                                            'name': {
                                                'type': ['string', 'null'],
                                                'description': 'List name',
                                            },
                                            'created': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Creation timestamp',
                                            },
                                            'updated': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Last update timestamp',
                                            },
                                            'opt_in_process': {
                                                'type': ['string', 'null'],
                                                'description': 'Opt-in process type',
                                            },
                                        },
                                    },
                                    'links': {
                                        'type': ['object', 'null'],
                                        'description': 'Related links',
                                        'properties': {
                                            'self': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'lists',
                                'x-airbyte-stream-name': 'lists',
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Klaviyo list for organizing profiles',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique list identifier'},
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Object type (always "list")',
                    },
                    'attributes': {
                        'type': ['object', 'null'],
                        'description': 'List attributes',
                        'properties': {
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'List name',
                            },
                            'created': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updated': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'opt_in_process': {
                                'type': ['string', 'null'],
                                'description': 'Opt-in process type',
                            },
                        },
                    },
                    'links': {
                        'type': ['object', 'null'],
                        'description': 'Related links',
                        'properties': {
                            'self': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'lists',
                'x-airbyte-stream-name': 'lists',
            },
        ),
        EntityDefinition(
            name='campaigns',
            stream_name='campaigns',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/campaigns',
                    action=Action.LIST,
                    description='Returns a paginated list of campaigns. A channel filter is required.',
                    query_params=['filter', 'page[size]', 'page[cursor]'],
                    query_params_schema={
                        'filter': {
                            'type': 'string',
                            'required': True,
                            'default': "equals(messages.channel,'email')",
                        },
                        'page[size]': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'page[cursor]': {'type': 'string', 'required': False},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of campaigns',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Klaviyo campaign',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type (always "campaign")',
                                        },
                                        'attributes': {
                                            'type': ['object', 'null'],
                                            'description': 'Campaign attributes',
                                            'properties': {
                                                'name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Campaign name',
                                                },
                                                'status': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Campaign status',
                                                },
                                                'archived': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether campaign is archived',
                                                },
                                                'audiences': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Target audiences',
                                                },
                                                'send_options': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Send options',
                                                },
                                                'tracking_options': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Tracking options',
                                                },
                                                'send_strategy': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Send strategy',
                                                },
                                                'created_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Creation timestamp',
                                                },
                                                'scheduled_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Scheduled send time',
                                                },
                                                'updated_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Last update timestamp',
                                                },
                                                'send_time': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Actual send time',
                                                },
                                            },
                                        },
                                        'links': {
                                            'type': ['object', 'null'],
                                            'description': 'Related links',
                                            'properties': {
                                                'self': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'campaigns',
                                    'x-airbyte-stream-name': 'campaigns',
                                },
                            },
                            'links': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'self': {
                                        'type': ['string', 'null'],
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                    },
                                    'prev': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/campaigns/{id}',
                    action=Action.GET,
                    description='Get a single campaign by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A Klaviyo campaign',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Object type (always "campaign")',
                                    },
                                    'attributes': {
                                        'type': ['object', 'null'],
                                        'description': 'Campaign attributes',
                                        'properties': {
                                            'name': {
                                                'type': ['string', 'null'],
                                                'description': 'Campaign name',
                                            },
                                            'status': {
                                                'type': ['string', 'null'],
                                                'description': 'Campaign status',
                                            },
                                            'archived': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether campaign is archived',
                                            },
                                            'audiences': {
                                                'type': ['object', 'null'],
                                                'description': 'Target audiences',
                                            },
                                            'send_options': {
                                                'type': ['object', 'null'],
                                                'description': 'Send options',
                                            },
                                            'tracking_options': {
                                                'type': ['object', 'null'],
                                                'description': 'Tracking options',
                                            },
                                            'send_strategy': {
                                                'type': ['object', 'null'],
                                                'description': 'Send strategy',
                                            },
                                            'created_at': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Creation timestamp',
                                            },
                                            'scheduled_at': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Scheduled send time',
                                            },
                                            'updated_at': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Last update timestamp',
                                            },
                                            'send_time': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Actual send time',
                                            },
                                        },
                                    },
                                    'links': {
                                        'type': ['object', 'null'],
                                        'description': 'Related links',
                                        'properties': {
                                            'self': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'campaigns',
                                'x-airbyte-stream-name': 'campaigns',
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Klaviyo campaign',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Object type (always "campaign")',
                    },
                    'attributes': {
                        'type': ['object', 'null'],
                        'description': 'Campaign attributes',
                        'properties': {
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Campaign name',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'Campaign status',
                            },
                            'archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether campaign is archived',
                            },
                            'audiences': {
                                'type': ['object', 'null'],
                                'description': 'Target audiences',
                            },
                            'send_options': {
                                'type': ['object', 'null'],
                                'description': 'Send options',
                            },
                            'tracking_options': {
                                'type': ['object', 'null'],
                                'description': 'Tracking options',
                            },
                            'send_strategy': {
                                'type': ['object', 'null'],
                                'description': 'Send strategy',
                            },
                            'created_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'scheduled_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Scheduled send time',
                            },
                            'updated_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'send_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Actual send time',
                            },
                        },
                    },
                    'links': {
                        'type': ['object', 'null'],
                        'description': 'Related links',
                        'properties': {
                            'self': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'campaigns',
                'x-airbyte-stream-name': 'campaigns',
            },
        ),
        EntityDefinition(
            name='events',
            stream_name='events',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/events',
                    action=Action.LIST,
                    description='Returns a paginated list of events (actions taken by profiles)',
                    query_params=['page[size]', 'page[cursor]', 'sort'],
                    query_params_schema={
                        'page[size]': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'page[cursor]': {'type': 'string', 'required': False},
                        'sort': {
                            'type': 'string',
                            'required': False,
                            'default': '-datetime',
                        },
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of events',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Klaviyo event representing an action taken by a profile',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique event identifier'},
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type (always "event")',
                                        },
                                        'attributes': {
                                            'type': ['object', 'null'],
                                            'description': 'Event attributes',
                                            'properties': {
                                                'timestamp': {
                                                    'oneOf': [
                                                        {'type': 'string', 'format': 'date-time'},
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Event timestamp (can be ISO string or Unix timestamp)',
                                                },
                                                'datetime': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Event datetime',
                                                },
                                                'uuid': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Event UUID',
                                                },
                                                'event_properties': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Custom event properties',
                                                },
                                            },
                                        },
                                        'relationships': {
                                            'type': ['object', 'null'],
                                            'description': 'Related resources',
                                            'properties': {
                                                'profile': {
                                                    'type': ['object', 'null'],
                                                    'properties': {
                                                        'data': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'type': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'id': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'metric': {
                                                    'type': ['object', 'null'],
                                                    'properties': {
                                                        'data': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'type': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'id': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'links': {
                                            'type': ['object', 'null'],
                                            'description': 'Related links',
                                            'properties': {
                                                'self': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'events',
                                    'x-airbyte-stream-name': 'events',
                                },
                            },
                            'links': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'self': {
                                        'type': ['string', 'null'],
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                    },
                                    'prev': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Klaviyo event representing an action taken by a profile',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique event identifier'},
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Object type (always "event")',
                    },
                    'attributes': {
                        'type': ['object', 'null'],
                        'description': 'Event attributes',
                        'properties': {
                            'timestamp': {
                                'oneOf': [
                                    {'type': 'string', 'format': 'date-time'},
                                    {'type': 'integer'},
                                    {'type': 'null'},
                                ],
                                'description': 'Event timestamp (can be ISO string or Unix timestamp)',
                            },
                            'datetime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Event datetime',
                            },
                            'uuid': {
                                'type': ['string', 'null'],
                                'description': 'Event UUID',
                            },
                            'event_properties': {
                                'type': ['object', 'null'],
                                'description': 'Custom event properties',
                            },
                        },
                    },
                    'relationships': {
                        'type': ['object', 'null'],
                        'description': 'Related resources',
                        'properties': {
                            'profile': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'data': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                            },
                                            'id': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                },
                            },
                            'metric': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'data': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'type': {
                                                'type': ['string', 'null'],
                                            },
                                            'id': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'links': {
                        'type': ['object', 'null'],
                        'description': 'Related links',
                        'properties': {
                            'self': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'events',
                'x-airbyte-stream-name': 'events',
            },
        ),
        EntityDefinition(
            name='metrics',
            stream_name='metrics',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/metrics',
                    action=Action.LIST,
                    description='Returns a paginated list of metrics (event types)',
                    query_params=['page[size]', 'page[cursor]'],
                    query_params_schema={
                        'page[size]': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'page[cursor]': {'type': 'string', 'required': False},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of metrics',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Klaviyo metric (event type)',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique metric identifier'},
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type (always "metric")',
                                        },
                                        'attributes': {
                                            'type': ['object', 'null'],
                                            'description': 'Metric attributes',
                                            'properties': {
                                                'name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Metric name',
                                                },
                                                'created': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Creation timestamp',
                                                },
                                                'updated': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Last update timestamp',
                                                },
                                                'integration': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Integration information',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'category': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'links': {
                                            'type': ['object', 'null'],
                                            'description': 'Related links',
                                            'properties': {
                                                'self': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'metrics',
                                    'x-airbyte-stream-name': 'metrics',
                                },
                            },
                            'links': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'self': {
                                        'type': ['string', 'null'],
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                    },
                                    'prev': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/metrics/{id}',
                    action=Action.GET,
                    description='Get a single metric by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A Klaviyo metric (event type)',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique metric identifier'},
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Object type (always "metric")',
                                    },
                                    'attributes': {
                                        'type': ['object', 'null'],
                                        'description': 'Metric attributes',
                                        'properties': {
                                            'name': {
                                                'type': ['string', 'null'],
                                                'description': 'Metric name',
                                            },
                                            'created': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Creation timestamp',
                                            },
                                            'updated': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Last update timestamp',
                                            },
                                            'integration': {
                                                'type': ['object', 'null'],
                                                'description': 'Integration information',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'category': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'links': {
                                        'type': ['object', 'null'],
                                        'description': 'Related links',
                                        'properties': {
                                            'self': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'metrics',
                                'x-airbyte-stream-name': 'metrics',
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Klaviyo metric (event type)',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique metric identifier'},
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Object type (always "metric")',
                    },
                    'attributes': {
                        'type': ['object', 'null'],
                        'description': 'Metric attributes',
                        'properties': {
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Metric name',
                            },
                            'created': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updated': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'integration': {
                                'type': ['object', 'null'],
                                'description': 'Integration information',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'category': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                        },
                    },
                    'links': {
                        'type': ['object', 'null'],
                        'description': 'Related links',
                        'properties': {
                            'self': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'metrics',
                'x-airbyte-stream-name': 'metrics',
            },
        ),
        EntityDefinition(
            name='flows',
            stream_name='flows',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/flows',
                    action=Action.LIST,
                    description='Returns a paginated list of flows (automated sequences)',
                    query_params=['page[size]', 'page[cursor]'],
                    query_params_schema={
                        'page[size]': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'page[cursor]': {'type': 'string', 'required': False},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of flows',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Klaviyo flow (automated sequence)',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique flow identifier'},
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type (always "flow")',
                                        },
                                        'attributes': {
                                            'type': ['object', 'null'],
                                            'description': 'Flow attributes',
                                            'properties': {
                                                'name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Flow name',
                                                },
                                                'status': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Flow status (draft, manual, live)',
                                                },
                                                'archived': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether flow is archived',
                                                },
                                                'created': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Creation timestamp',
                                                },
                                                'updated': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Last update timestamp',
                                                },
                                                'trigger_type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of trigger for the flow',
                                                },
                                            },
                                        },
                                        'links': {
                                            'type': ['object', 'null'],
                                            'description': 'Related links',
                                            'properties': {
                                                'self': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'flows',
                                    'x-airbyte-stream-name': 'flows',
                                },
                            },
                            'links': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'self': {
                                        'type': ['string', 'null'],
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                    },
                                    'prev': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/flows/{id}',
                    action=Action.GET,
                    description='Get a single flow by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A Klaviyo flow (automated sequence)',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique flow identifier'},
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Object type (always "flow")',
                                    },
                                    'attributes': {
                                        'type': ['object', 'null'],
                                        'description': 'Flow attributes',
                                        'properties': {
                                            'name': {
                                                'type': ['string', 'null'],
                                                'description': 'Flow name',
                                            },
                                            'status': {
                                                'type': ['string', 'null'],
                                                'description': 'Flow status (draft, manual, live)',
                                            },
                                            'archived': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether flow is archived',
                                            },
                                            'created': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Creation timestamp',
                                            },
                                            'updated': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Last update timestamp',
                                            },
                                            'trigger_type': {
                                                'type': ['string', 'null'],
                                                'description': 'Type of trigger for the flow',
                                            },
                                        },
                                    },
                                    'links': {
                                        'type': ['object', 'null'],
                                        'description': 'Related links',
                                        'properties': {
                                            'self': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'flows',
                                'x-airbyte-stream-name': 'flows',
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Klaviyo flow (automated sequence)',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique flow identifier'},
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Object type (always "flow")',
                    },
                    'attributes': {
                        'type': ['object', 'null'],
                        'description': 'Flow attributes',
                        'properties': {
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Flow name',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'Flow status (draft, manual, live)',
                            },
                            'archived': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether flow is archived',
                            },
                            'created': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updated': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'trigger_type': {
                                'type': ['string', 'null'],
                                'description': 'Type of trigger for the flow',
                            },
                        },
                    },
                    'links': {
                        'type': ['object', 'null'],
                        'description': 'Related links',
                        'properties': {
                            'self': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'flows',
                'x-airbyte-stream-name': 'flows',
            },
        ),
        EntityDefinition(
            name='email_templates',
            stream_name='email_templates',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/templates',
                    action=Action.LIST,
                    description='Returns a paginated list of email templates',
                    query_params=['page[size]', 'page[cursor]'],
                    query_params_schema={
                        'page[size]': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'page[cursor]': {'type': 'string', 'required': False},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of templates',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Klaviyo email template',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique template identifier'},
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type (always "template")',
                                        },
                                        'attributes': {
                                            'type': ['object', 'null'],
                                            'description': 'Template attributes',
                                            'properties': {
                                                'name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Template name',
                                                },
                                                'editor_type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Editor type used to create template',
                                                },
                                                'html': {
                                                    'type': ['string', 'null'],
                                                    'description': 'HTML content',
                                                },
                                                'text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Plain text content',
                                                },
                                                'created': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Creation timestamp',
                                                },
                                                'updated': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'Last update timestamp',
                                                },
                                            },
                                        },
                                        'links': {
                                            'type': ['object', 'null'],
                                            'description': 'Related links',
                                            'properties': {
                                                'self': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'email_templates',
                                    'x-airbyte-stream-name': 'email_templates',
                                },
                            },
                            'links': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'self': {
                                        'type': ['string', 'null'],
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                    },
                                    'prev': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/templates/{id}',
                    action=Action.GET,
                    description='Get a single email template by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['revision'],
                    header_params_schema={
                        'revision': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-10-15',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A Klaviyo email template',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique template identifier'},
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Object type (always "template")',
                                    },
                                    'attributes': {
                                        'type': ['object', 'null'],
                                        'description': 'Template attributes',
                                        'properties': {
                                            'name': {
                                                'type': ['string', 'null'],
                                                'description': 'Template name',
                                            },
                                            'editor_type': {
                                                'type': ['string', 'null'],
                                                'description': 'Editor type used to create template',
                                            },
                                            'html': {
                                                'type': ['string', 'null'],
                                                'description': 'HTML content',
                                            },
                                            'text': {
                                                'type': ['string', 'null'],
                                                'description': 'Plain text content',
                                            },
                                            'created': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Creation timestamp',
                                            },
                                            'updated': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Last update timestamp',
                                            },
                                        },
                                    },
                                    'links': {
                                        'type': ['object', 'null'],
                                        'description': 'Related links',
                                        'properties': {
                                            'self': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'email_templates',
                                'x-airbyte-stream-name': 'email_templates',
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Klaviyo email template',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique template identifier'},
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Object type (always "template")',
                    },
                    'attributes': {
                        'type': ['object', 'null'],
                        'description': 'Template attributes',
                        'properties': {
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Template name',
                            },
                            'editor_type': {
                                'type': ['string', 'null'],
                                'description': 'Editor type used to create template',
                            },
                            'html': {
                                'type': ['string', 'null'],
                                'description': 'HTML content',
                            },
                            'text': {
                                'type': ['string', 'null'],
                                'description': 'Plain text content',
                            },
                            'created': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updated': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                        },
                    },
                    'links': {
                        'type': ['object', 'null'],
                        'description': 'Related links',
                        'properties': {
                            'self': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'email_templates',
                'x-airbyte-stream-name': 'email_templates',
            },
        ),
    ],
    search_field_paths={
        'profiles': [
            'attributes',
            'attributes.anonymous_id',
            'attributes.created',
            'attributes.email',
            'attributes.external_id',
            'attributes.first_name',
            'attributes.image',
            'attributes.last_event_date',
            'attributes.last_name',
            'attributes.locale',
            'attributes.location',
            'attributes.location.address1',
            'attributes.location.address2',
            'attributes.location.city',
            'attributes.location.country',
            'attributes.location.ip',
            'attributes.location.latitude',
            'attributes.location.longitude',
            'attributes.location.region',
            'attributes.location.timezone',
            'attributes.location.zip',
            'attributes.organization',
            'attributes.phone_number',
            'attributes.predictive_analytics',
            'attributes.predictive_analytics.average_days_between_orders',
            'attributes.predictive_analytics.average_order_value',
            'attributes.predictive_analytics.churn_probability',
            'attributes.predictive_analytics.expected_date_of_next_order',
            'attributes.predictive_analytics.historic_clv',
            'attributes.predictive_analytics.historic_number_of_orders',
            'attributes.predictive_analytics.predicted_clv',
            'attributes.predictive_analytics.predicted_number_of_orders',
            'attributes.predictive_analytics.total_clv',
            'attributes.properties',
            'attributes.subscriptions',
            'attributes.subscriptions.email',
            'attributes.subscriptions.email.marketing',
            'attributes.subscriptions.email.marketing.can_receive_email_marketing',
            'attributes.subscriptions.email.marketing.consent',
            'attributes.subscriptions.email.marketing.consent_timestamp',
            'attributes.subscriptions.email.marketing.custom_method_detail',
            'attributes.subscriptions.email.marketing.double_optin',
            'attributes.subscriptions.email.marketing.last_updated',
            'attributes.subscriptions.email.marketing.list_suppressions',
            'attributes.subscriptions.email.marketing.list_suppressions[]',
            'attributes.subscriptions.email.marketing.method',
            'attributes.subscriptions.email.marketing.method_detail',
            'attributes.subscriptions.email.marketing.suppressions',
            'attributes.subscriptions.email.marketing.suppressions[]',
            'attributes.subscriptions.email.marketing.timestamp',
            'attributes.subscriptions.mobile_push',
            'attributes.subscriptions.mobile_push.marketing',
            'attributes.subscriptions.mobile_push.marketing.can_receive_sms_marketing',
            'attributes.subscriptions.mobile_push.marketing.consent',
            'attributes.subscriptions.mobile_push.marketing.consent_timestamp',
            'attributes.subscriptions.sms',
            'attributes.subscriptions.sms.marketing',
            'attributes.subscriptions.sms.marketing.can_receive_sms_marketing',
            'attributes.subscriptions.sms.marketing.consent',
            'attributes.subscriptions.sms.marketing.consent_timestamp',
            'attributes.subscriptions.sms.marketing.last_updated',
            'attributes.subscriptions.sms.marketing.method',
            'attributes.subscriptions.sms.marketing.method_detail',
            'attributes.subscriptions.sms.marketing.timestamp',
            'attributes.subscriptions.sms.transactional',
            'attributes.subscriptions.sms.transactional.can_receive_sms_marketing',
            'attributes.subscriptions.sms.transactional.consent',
            'attributes.subscriptions.sms.transactional.consent_timestamp',
            'attributes.subscriptions.sms.transactional.last_updated',
            'attributes.subscriptions.sms.transactional.method',
            'attributes.subscriptions.sms.transactional.method_detail',
            'attributes.subscriptions.sms.transactional.timestamp',
            'attributes.title',
            'attributes.updated',
            'id',
            'links',
            'links.self',
            'relationships',
            'relationships.lists',
            'relationships.lists.links',
            'relationships.lists.links.related',
            'relationships.lists.links.self',
            'relationships.segments',
            'relationships.segments.links',
            'relationships.segments.links.related',
            'relationships.segments.links.self',
            'segments',
            'type',
            'updated',
        ],
        'events': [
            'attributes',
            'attributes.datetime',
            'attributes.event_properties',
            'attributes.timestamp',
            'attributes.uuid',
            'datetime',
            'id',
            'links',
            'links.self',
            'relationships',
            'relationships.attributions',
            'relationships.attributions.data',
            'relationships.attributions.data[]',
            'relationships.attributions.links',
            'relationships.attributions.links.related',
            'relationships.attributions.links.self',
            'relationships.metric',
            'relationships.metric.data',
            'relationships.metric.data.type',
            'relationships.metric.data.id',
            'relationships.metric.links',
            'relationships.metric.links.related',
            'relationships.metric.links.self',
            'relationships.profile',
            'relationships.profile.data',
            'relationships.profile.data.type',
            'relationships.profile.data.id',
            'relationships.profile.links',
            'relationships.profile.links.related',
            'relationships.profile.links.self',
            'type',
        ],
        'email_templates': [
            'attributes',
            'attributes.company_id',
            'attributes.created',
            'attributes.editor_type',
            'attributes.html',
            'attributes.name',
            'attributes.text',
            'attributes.updated',
            'id',
            'links',
            'links.self',
            'type',
            'updated',
        ],
        'campaigns': [
            'attributes',
            'attributes.archived',
            'attributes.audiences',
            'attributes.audiences.excluded',
            'attributes.audiences.excluded[]',
            'attributes.audiences.included',
            'attributes.audiences.included[]',
            'attributes.channel',
            'attributes.created_at',
            'attributes.message',
            'attributes.name',
            'attributes.scheduled_at',
            'attributes.send_options',
            'attributes.send_options.ignore_unsubscribes',
            'attributes.send_options.use_smart_sending',
            'attributes.send_strategy',
            'attributes.send_strategy.method',
            'attributes.send_strategy.options_static',
            'attributes.send_strategy.options_static.datetime',
            'attributes.send_strategy.options_static.is_local',
            'attributes.send_strategy.options_static.send_past_recipients_immediately',
            'attributes.send_strategy.options_sto',
            'attributes.send_strategy.options_sto.date',
            'attributes.send_strategy.options_throttled',
            'attributes.send_strategy.options_throttled.datetime',
            'attributes.send_strategy.options_throttled.throttle_percentage',
            'attributes.send_time',
            'attributes.status',
            'attributes.tracking_options',
            'attributes.tracking_options.add_tracking_params',
            'attributes.tracking_options.is_add_utm',
            'attributes.tracking_options.is_tracking_clicks',
            'attributes.tracking_options.is_tracking_opens',
            'attributes.tracking_options.utm_params',
            'attributes.tracking_options.utm_params[]',
            'attributes.updated_at',
            'id',
            'links',
            'links.self',
            'relationships',
            'relationships.campaign-messages',
            'relationships.campaign-messages.data',
            'relationships.campaign-messages.data[]',
            'relationships.campaign-messages.links',
            'relationships.campaign-messages.links.related',
            'relationships.campaign-messages.links.self',
            'relationships.tags',
            'relationships.tags.data',
            'relationships.tags.data[]',
            'relationships.tags.links',
            'relationships.tags.links.related',
            'relationships.tags.links.self',
            'type',
            'updated_at',
        ],
        'flows': [
            'attributes',
            'attributes.archived',
            'attributes.created',
            'attributes.name',
            'attributes.status',
            'attributes.trigger_type',
            'attributes.updated',
            'id',
            'links',
            'links.self',
            'relationships',
            'relationships.flow-actions',
            'relationships.flow-actions.data',
            'relationships.flow-actions.data[]',
            'relationships.flow-actions.links',
            'relationships.flow-actions.links.related',
            'relationships.flow-actions.links.self',
            'relationships.tags',
            'relationships.tags.data',
            'relationships.tags.data[]',
            'relationships.tags.links',
            'relationships.tags.links.related',
            'relationships.tags.links.self',
            'type',
            'updated',
        ],
        'metrics': [
            'attributes',
            'attributes.created',
            'attributes.integration',
            'attributes.name',
            'attributes.updated',
            'id',
            'links',
            'links.self',
            'relationships',
            'relationships.flow-triggers',
            'relationships.flow-triggers.data',
            'relationships.flow-triggers.data.type',
            'relationships.flow-triggers.data.id',
            'relationships.flow-triggers.links',
            'relationships.flow-triggers.links.related',
            'relationships.flow-triggers.links.self',
            'type',
            'updated',
        ],
        'lists': [
            'attributes',
            'attributes.created',
            'attributes.name',
            'attributes.opt_in_process',
            'attributes.updated',
            'id',
            'links',
            'links.self',
            'relationships',
            'relationships.flow-triggers',
            'relationships.flow-triggers.data',
            'relationships.flow-triggers.data.type',
            'relationships.flow-triggers.data.id',
            'relationships.flow-triggers.links',
            'relationships.flow-triggers.links.related',
            'relationships.flow-triggers.links.self',
            'relationships.profiles',
            'relationships.profiles.links',
            'relationships.profiles.links.related',
            'relationships.profiles.links.self',
            'relationships.tags',
            'relationships.tags.data',
            'relationships.tags.data[]',
            'relationships.tags.links',
            'relationships.tags.links.related',
            'relationships.tags.links.self',
            'type',
            'updated',
        ],
    },
)