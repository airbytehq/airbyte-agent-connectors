"""
Connector model for sendgrid.

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

SendgridConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('fbb5fbe2-16ad-4cf4-af7d-ff9d9c316c87'),
    name='sendgrid',
    version='1.0.2',
    base_url='https://api.sendgrid.com',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
            title='API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Your SendGrid API key (generated at https://app.sendgrid.com/settings/api_keys)',
                ),
            },
            auth_mapping={'token': '${api_key}'},
            replication_auth_key_mapping={'api_key': 'api_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='contacts',
            stream_name='contacts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/marketing/contacts',
                    action=Action.LIST,
                    description='Returns a sample of contacts. Use the export endpoint for full lists.',
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing a list of contacts',
                        'properties': {
                            'result': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A SendGrid marketing contact',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique contact identifier'},
                                        'email': {
                                            'type': ['null', 'string'],
                                            'description': 'Contact email address',
                                        },
                                        'first_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Contact first name',
                                        },
                                        'last_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Contact last name',
                                        },
                                        'unique_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique name for the contact',
                                        },
                                        'alternate_emails': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'Alternate email addresses',
                                        },
                                        'address_line_1': {
                                            'type': ['null', 'string'],
                                            'description': 'Address line 1',
                                        },
                                        'address_line_2': {
                                            'type': ['null', 'string'],
                                            'description': 'Address line 2',
                                        },
                                        'city': {
                                            'type': ['null', 'string'],
                                            'description': 'City',
                                        },
                                        'state_province_region': {
                                            'type': ['null', 'string'],
                                            'description': 'State, province, or region',
                                        },
                                        'country': {
                                            'type': ['null', 'string'],
                                            'description': 'Country',
                                        },
                                        'postal_code': {
                                            'type': ['null', 'string'],
                                            'description': 'Postal code',
                                        },
                                        'phone_number': {
                                            'type': ['null', 'string'],
                                            'description': 'Phone number',
                                        },
                                        'whatsapp': {
                                            'type': ['null', 'string'],
                                            'description': 'WhatsApp number',
                                        },
                                        'line': {
                                            'type': ['null', 'string'],
                                            'description': 'LINE ID',
                                        },
                                        'facebook': {
                                            'type': ['null', 'string'],
                                            'description': 'Facebook ID',
                                        },
                                        'list_ids': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'IDs of lists the contact belongs to',
                                        },
                                        'segment_ids': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'IDs of segments the contact belongs to',
                                        },
                                        'custom_fields': {
                                            'type': ['null', 'object'],
                                            'description': 'Custom field values',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the contact was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the contact was last updated',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'contacts',
                                    'x-airbyte-stream-name': 'contacts',
                                },
                            },
                            'contact_count': {'type': 'integer', 'description': 'Total number of contacts'},
                        },
                    },
                    record_extractor='$.result',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v3/marketing/contacts/{id}',
                    action=Action.GET,
                    description='Returns the full details and all fields for the specified contact.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A SendGrid marketing contact',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique contact identifier'},
                            'email': {
                                'type': ['null', 'string'],
                                'description': 'Contact email address',
                            },
                            'first_name': {
                                'type': ['null', 'string'],
                                'description': 'Contact first name',
                            },
                            'last_name': {
                                'type': ['null', 'string'],
                                'description': 'Contact last name',
                            },
                            'unique_name': {
                                'type': ['null', 'string'],
                                'description': 'Unique name for the contact',
                            },
                            'alternate_emails': {
                                'type': ['null', 'array'],
                                'items': {'type': 'string'},
                                'description': 'Alternate email addresses',
                            },
                            'address_line_1': {
                                'type': ['null', 'string'],
                                'description': 'Address line 1',
                            },
                            'address_line_2': {
                                'type': ['null', 'string'],
                                'description': 'Address line 2',
                            },
                            'city': {
                                'type': ['null', 'string'],
                                'description': 'City',
                            },
                            'state_province_region': {
                                'type': ['null', 'string'],
                                'description': 'State, province, or region',
                            },
                            'country': {
                                'type': ['null', 'string'],
                                'description': 'Country',
                            },
                            'postal_code': {
                                'type': ['null', 'string'],
                                'description': 'Postal code',
                            },
                            'phone_number': {
                                'type': ['null', 'string'],
                                'description': 'Phone number',
                            },
                            'whatsapp': {
                                'type': ['null', 'string'],
                                'description': 'WhatsApp number',
                            },
                            'line': {
                                'type': ['null', 'string'],
                                'description': 'LINE ID',
                            },
                            'facebook': {
                                'type': ['null', 'string'],
                                'description': 'Facebook ID',
                            },
                            'list_ids': {
                                'type': ['null', 'array'],
                                'items': {'type': 'string'},
                                'description': 'IDs of lists the contact belongs to',
                            },
                            'segment_ids': {
                                'type': ['null', 'array'],
                                'items': {'type': 'string'},
                                'description': 'IDs of segments the contact belongs to',
                            },
                            'custom_fields': {
                                'type': ['null', 'object'],
                                'description': 'Custom field values',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the contact was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the contact was last updated',
                            },
                        },
                        'x-airbyte-entity-name': 'contacts',
                        'x-airbyte-stream-name': 'contacts',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A SendGrid marketing contact',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique contact identifier'},
                    'email': {
                        'type': ['null', 'string'],
                        'description': 'Contact email address',
                    },
                    'first_name': {
                        'type': ['null', 'string'],
                        'description': 'Contact first name',
                    },
                    'last_name': {
                        'type': ['null', 'string'],
                        'description': 'Contact last name',
                    },
                    'unique_name': {
                        'type': ['null', 'string'],
                        'description': 'Unique name for the contact',
                    },
                    'alternate_emails': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'Alternate email addresses',
                    },
                    'address_line_1': {
                        'type': ['null', 'string'],
                        'description': 'Address line 1',
                    },
                    'address_line_2': {
                        'type': ['null', 'string'],
                        'description': 'Address line 2',
                    },
                    'city': {
                        'type': ['null', 'string'],
                        'description': 'City',
                    },
                    'state_province_region': {
                        'type': ['null', 'string'],
                        'description': 'State, province, or region',
                    },
                    'country': {
                        'type': ['null', 'string'],
                        'description': 'Country',
                    },
                    'postal_code': {
                        'type': ['null', 'string'],
                        'description': 'Postal code',
                    },
                    'phone_number': {
                        'type': ['null', 'string'],
                        'description': 'Phone number',
                    },
                    'whatsapp': {
                        'type': ['null', 'string'],
                        'description': 'WhatsApp number',
                    },
                    'line': {
                        'type': ['null', 'string'],
                        'description': 'LINE ID',
                    },
                    'facebook': {
                        'type': ['null', 'string'],
                        'description': 'Facebook ID',
                    },
                    'list_ids': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'IDs of lists the contact belongs to',
                    },
                    'segment_ids': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'IDs of segments the contact belongs to',
                    },
                    'custom_fields': {
                        'type': ['null', 'object'],
                        'description': 'Custom field values',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the contact was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the contact was last updated',
                    },
                },
                'x-airbyte-entity-name': 'contacts',
                'x-airbyte-stream-name': 'contacts',
            },
        ),
        EntityDefinition(
            name='lists',
            stream_name='lists',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/marketing/lists',
                    action=Action.LIST,
                    description='Returns all marketing contact lists.',
                    query_params=['page_size'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing a list of marketing lists',
                        'properties': {
                            'result': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A SendGrid marketing list',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique list identifier'},
                                        'name': {'type': 'string', 'description': 'Name of the list'},
                                        'contact_count': {'type': 'integer', 'description': 'Number of contacts in the list'},
                                        '_metadata': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'self': {'type': 'string'},
                                            },
                                            'description': 'Metadata about the list resource',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'lists',
                                    'x-airbyte-stream-name': 'lists',
                                },
                            },
                            '_metadata': {
                                'type': 'object',
                                'properties': {
                                    'next': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.result',
                    meta_extractor={'next': '$._metadata.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v3/marketing/lists/{id}',
                    action=Action.GET,
                    description='Returns a specific marketing list by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A SendGrid marketing list',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique list identifier'},
                            'name': {'type': 'string', 'description': 'Name of the list'},
                            'contact_count': {'type': 'integer', 'description': 'Number of contacts in the list'},
                            '_metadata': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'self': {'type': 'string'},
                                },
                                'description': 'Metadata about the list resource',
                            },
                        },
                        'x-airbyte-entity-name': 'lists',
                        'x-airbyte-stream-name': 'lists',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A SendGrid marketing list',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique list identifier'},
                    'name': {'type': 'string', 'description': 'Name of the list'},
                    'contact_count': {'type': 'integer', 'description': 'Number of contacts in the list'},
                    '_metadata': {
                        'type': ['null', 'object'],
                        'properties': {
                            'self': {'type': 'string'},
                        },
                        'description': 'Metadata about the list resource',
                    },
                },
                'x-airbyte-entity-name': 'lists',
                'x-airbyte-stream-name': 'lists',
            },
        ),
        EntityDefinition(
            name='segments',
            stream_name='segments',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/marketing/segments/2.0',
                    action=Action.LIST,
                    description='Returns all segments (v2).',
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing a list of segments',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A SendGrid marketing segment',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique segment identifier'},
                                        'name': {'type': 'string', 'description': 'Segment name'},
                                        'contacts_count': {'type': 'integer', 'description': 'Number of contacts in the segment'},
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the segment was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the segment was last updated',
                                        },
                                        'sample_updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the sample was last updated',
                                        },
                                        'next_sample_update': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the next sample update will occur',
                                        },
                                        'parent_list_ids': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': ['null', 'string'],
                                            },
                                            'description': 'IDs of parent lists',
                                        },
                                        'query_version': {'type': 'string', 'description': 'Query version used'},
                                        'status': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'query_validation': {'type': 'string'},
                                            },
                                            'description': 'Segment status details',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'segments',
                                    'x-airbyte-stream-name': 'segments',
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v3/marketing/segments/2.0/{segment_id}',
                    action=Action.GET,
                    description='Returns a specific segment by ID.',
                    path_params=['segment_id'],
                    path_params_schema={
                        'segment_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A SendGrid marketing segment',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique segment identifier'},
                            'name': {'type': 'string', 'description': 'Segment name'},
                            'contacts_count': {'type': 'integer', 'description': 'Number of contacts in the segment'},
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the segment was created',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the segment was last updated',
                            },
                            'sample_updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the sample was last updated',
                            },
                            'next_sample_update': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the next sample update will occur',
                            },
                            'parent_list_ids': {
                                'type': ['null', 'array'],
                                'items': {
                                    'type': ['null', 'string'],
                                },
                                'description': 'IDs of parent lists',
                            },
                            'query_version': {'type': 'string', 'description': 'Query version used'},
                            'status': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'query_validation': {'type': 'string'},
                                },
                                'description': 'Segment status details',
                            },
                        },
                        'x-airbyte-entity-name': 'segments',
                        'x-airbyte-stream-name': 'segments',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A SendGrid marketing segment',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique segment identifier'},
                    'name': {'type': 'string', 'description': 'Segment name'},
                    'contacts_count': {'type': 'integer', 'description': 'Number of contacts in the segment'},
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the segment was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the segment was last updated',
                    },
                    'sample_updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the sample was last updated',
                    },
                    'next_sample_update': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the next sample update will occur',
                    },
                    'parent_list_ids': {
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'string'],
                        },
                        'description': 'IDs of parent lists',
                    },
                    'query_version': {'type': 'string', 'description': 'Query version used'},
                    'status': {
                        'type': ['null', 'object'],
                        'properties': {
                            'query_validation': {'type': 'string'},
                        },
                        'description': 'Segment status details',
                    },
                },
                'x-airbyte-entity-name': 'segments',
                'x-airbyte-stream-name': 'segments',
            },
        ),
        EntityDefinition(
            name='campaigns',
            stream_name='campaigns',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/marketing/campaigns',
                    action=Action.LIST,
                    description='Returns all marketing campaigns.',
                    query_params=['page_size'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing a list of campaigns',
                        'properties': {
                            'result': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A SendGrid marketing campaign',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                                        'name': {'type': 'string', 'description': 'Campaign name'},
                                        'status': {'type': 'string', 'description': 'Campaign status'},
                                        'channels': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'Channels for this campaign',
                                        },
                                        'is_abtest': {'type': 'boolean', 'description': 'Whether this campaign is an A/B test'},
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the campaign was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the campaign was last updated',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'campaigns',
                                    'x-airbyte-stream-name': 'campaigns',
                                },
                            },
                            '_metadata': {
                                'type': 'object',
                                'properties': {
                                    'next': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.result',
                    meta_extractor={'next': '$._metadata.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A SendGrid marketing campaign',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                    'name': {'type': 'string', 'description': 'Campaign name'},
                    'status': {'type': 'string', 'description': 'Campaign status'},
                    'channels': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'Channels for this campaign',
                    },
                    'is_abtest': {'type': 'boolean', 'description': 'Whether this campaign is an A/B test'},
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the campaign was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the campaign was last updated',
                    },
                },
                'x-airbyte-entity-name': 'campaigns',
                'x-airbyte-stream-name': 'campaigns',
            },
        ),
        EntityDefinition(
            name='singlesends',
            stream_name='singlesends',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/marketing/singlesends',
                    action=Action.LIST,
                    description='Returns all single sends.',
                    query_params=['page_size'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing a list of single sends',
                        'properties': {
                            'result': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A SendGrid single send',
                                    'properties': {
                                        'id': {
                                            'type': 'string',
                                            'format': 'uuid',
                                            'description': 'Unique single send identifier',
                                        },
                                        'name': {'type': 'string', 'description': 'Single send name'},
                                        'status': {'type': 'string', 'description': 'Current status: draft, scheduled, or triggered'},
                                        'categories': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'Categories associated with this single send',
                                        },
                                        'send_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Scheduled send time',
                                        },
                                        'send_to': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'list_ids': {
                                                    'type': ['null', 'array'],
                                                    'items': {'type': 'string'},
                                                },
                                                'segment_ids': {
                                                    'type': ['null', 'array'],
                                                    'items': {'type': 'string'},
                                                },
                                                'all': {'type': 'boolean'},
                                            },
                                            'description': 'Recipients configuration',
                                        },
                                        'email_config': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'subject': {
                                                    'type': ['null', 'string'],
                                                },
                                                'html_content': {
                                                    'type': ['null', 'string'],
                                                },
                                                'plain_content': {
                                                    'type': ['null', 'string'],
                                                },
                                                'generate_plain_content': {'type': 'boolean'},
                                                'design_id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'editor': {
                                                    'type': ['null', 'string'],
                                                },
                                                'suppression_group_id': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'custom_unsubscribe_url': {
                                                    'type': ['null', 'string'],
                                                },
                                                'sender_id': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'ip_pool': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                            'description': 'Email configuration details',
                                        },
                                        'is_abtest': {'type': 'boolean', 'description': 'Whether this is an A/B test'},
                                        'created_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the single send was created',
                                        },
                                        'updated_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the single send was last updated',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'singlesends',
                                    'x-airbyte-stream-name': 'singlesends',
                                },
                            },
                            '_metadata': {
                                'type': 'object',
                                'properties': {
                                    'next': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.result',
                    meta_extractor={'next': '$._metadata.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v3/marketing/singlesends/{id}',
                    action=Action.GET,
                    description='Returns details about one single send.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A SendGrid single send',
                        'properties': {
                            'id': {
                                'type': 'string',
                                'format': 'uuid',
                                'description': 'Unique single send identifier',
                            },
                            'name': {'type': 'string', 'description': 'Single send name'},
                            'status': {'type': 'string', 'description': 'Current status: draft, scheduled, or triggered'},
                            'categories': {
                                'type': ['null', 'array'],
                                'items': {'type': 'string'},
                                'description': 'Categories associated with this single send',
                            },
                            'send_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Scheduled send time',
                            },
                            'send_to': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'list_ids': {
                                        'type': ['null', 'array'],
                                        'items': {'type': 'string'},
                                    },
                                    'segment_ids': {
                                        'type': ['null', 'array'],
                                        'items': {'type': 'string'},
                                    },
                                    'all': {'type': 'boolean'},
                                },
                                'description': 'Recipients configuration',
                            },
                            'email_config': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'subject': {
                                        'type': ['null', 'string'],
                                    },
                                    'html_content': {
                                        'type': ['null', 'string'],
                                    },
                                    'plain_content': {
                                        'type': ['null', 'string'],
                                    },
                                    'generate_plain_content': {'type': 'boolean'},
                                    'design_id': {
                                        'type': ['null', 'string'],
                                    },
                                    'editor': {
                                        'type': ['null', 'string'],
                                    },
                                    'suppression_group_id': {
                                        'type': ['null', 'integer'],
                                    },
                                    'custom_unsubscribe_url': {
                                        'type': ['null', 'string'],
                                    },
                                    'sender_id': {
                                        'type': ['null', 'integer'],
                                    },
                                    'ip_pool': {
                                        'type': ['null', 'string'],
                                    },
                                },
                                'description': 'Email configuration details',
                            },
                            'is_abtest': {'type': 'boolean', 'description': 'Whether this is an A/B test'},
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the single send was created',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the single send was last updated',
                            },
                        },
                        'x-airbyte-entity-name': 'singlesends',
                        'x-airbyte-stream-name': 'singlesends',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A SendGrid single send',
                'properties': {
                    'id': {
                        'type': 'string',
                        'format': 'uuid',
                        'description': 'Unique single send identifier',
                    },
                    'name': {'type': 'string', 'description': 'Single send name'},
                    'status': {'type': 'string', 'description': 'Current status: draft, scheduled, or triggered'},
                    'categories': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'Categories associated with this single send',
                    },
                    'send_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Scheduled send time',
                    },
                    'send_to': {
                        'type': ['null', 'object'],
                        'properties': {
                            'list_ids': {
                                'type': ['null', 'array'],
                                'items': {'type': 'string'},
                            },
                            'segment_ids': {
                                'type': ['null', 'array'],
                                'items': {'type': 'string'},
                            },
                            'all': {'type': 'boolean'},
                        },
                        'description': 'Recipients configuration',
                    },
                    'email_config': {
                        'type': ['null', 'object'],
                        'properties': {
                            'subject': {
                                'type': ['null', 'string'],
                            },
                            'html_content': {
                                'type': ['null', 'string'],
                            },
                            'plain_content': {
                                'type': ['null', 'string'],
                            },
                            'generate_plain_content': {'type': 'boolean'},
                            'design_id': {
                                'type': ['null', 'string'],
                            },
                            'editor': {
                                'type': ['null', 'string'],
                            },
                            'suppression_group_id': {
                                'type': ['null', 'integer'],
                            },
                            'custom_unsubscribe_url': {
                                'type': ['null', 'string'],
                            },
                            'sender_id': {
                                'type': ['null', 'integer'],
                            },
                            'ip_pool': {
                                'type': ['null', 'string'],
                            },
                        },
                        'description': 'Email configuration details',
                    },
                    'is_abtest': {'type': 'boolean', 'description': 'Whether this is an A/B test'},
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the single send was created',
                    },
                    'updated_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the single send was last updated',
                    },
                },
                'x-airbyte-entity-name': 'singlesends',
                'x-airbyte-stream-name': 'singlesends',
            },
        ),
        EntityDefinition(
            name='templates',
            stream_name='templates',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/templates',
                    action=Action.LIST,
                    description='Returns paged transactional templates (legacy and dynamic).',
                    query_params=['generations', 'page_size'],
                    query_params_schema={
                        'generations': {
                            'type': 'string',
                            'required': False,
                            'default': 'legacy,dynamic',
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing a list of templates',
                        'properties': {
                            'templates': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A SendGrid transactional template',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique template identifier'},
                                        'name': {'type': 'string', 'description': 'Template name'},
                                        'generation': {'type': 'string', 'description': 'Template generation (legacy or dynamic)'},
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the template was last updated',
                                        },
                                        'versions': {
                                            'type': ['null', 'array'],
                                            'description': 'Template versions',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'templates',
                                    'x-airbyte-stream-name': 'templates',
                                },
                            },
                        },
                    },
                    record_extractor='$.templates',
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v3/templates/{template_id}',
                    action=Action.GET,
                    description='Returns a single transactional template.',
                    path_params=['template_id'],
                    path_params_schema={
                        'template_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A SendGrid transactional template',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique template identifier'},
                            'name': {'type': 'string', 'description': 'Template name'},
                            'generation': {'type': 'string', 'description': 'Template generation (legacy or dynamic)'},
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the template was last updated',
                            },
                            'versions': {
                                'type': ['null', 'array'],
                                'description': 'Template versions',
                            },
                        },
                        'x-airbyte-entity-name': 'templates',
                        'x-airbyte-stream-name': 'templates',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A SendGrid transactional template',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique template identifier'},
                    'name': {'type': 'string', 'description': 'Template name'},
                    'generation': {'type': 'string', 'description': 'Template generation (legacy or dynamic)'},
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the template was last updated',
                    },
                    'versions': {
                        'type': ['null', 'array'],
                        'description': 'Template versions',
                    },
                },
                'x-airbyte-entity-name': 'templates',
                'x-airbyte-stream-name': 'templates',
            },
        ),
        EntityDefinition(
            name='singlesend_stats',
            stream_name='singlesend_stats',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/marketing/stats/singlesends',
                    action=Action.LIST,
                    description='Returns stats for all single sends.',
                    query_params=['page_size'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing a list of single send stats',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Stats for a single send',
                                    'properties': {
                                        'id': {
                                            'type': 'string',
                                            'format': 'uuid',
                                            'description': 'The single send ID',
                                        },
                                        'ab_phase': {
                                            'type': ['null', 'string'],
                                            'description': 'The A/B test phase',
                                        },
                                        'ab_variation': {
                                            'type': ['null', 'string'],
                                            'description': 'The A/B test variation',
                                        },
                                        'aggregation': {
                                            'type': ['null', 'string'],
                                            'description': 'The aggregation type',
                                        },
                                        'stats': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'bounce_drops': {'type': 'integer'},
                                                'bounces': {'type': 'integer'},
                                                'clicks': {'type': 'integer'},
                                                'delivered': {'type': 'integer'},
                                                'invalid_emails': {'type': 'integer'},
                                                'opens': {'type': 'integer'},
                                                'requests': {'type': 'integer'},
                                                'spam_report_drops': {'type': 'integer'},
                                                'spam_reports': {'type': 'integer'},
                                                'unique_clicks': {'type': 'integer'},
                                                'unique_opens': {'type': 'integer'},
                                                'unsubscribes': {'type': 'integer'},
                                            },
                                            'description': 'Email statistics for the single send',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'singlesend_stats',
                                    'x-airbyte-stream-name': 'singlesend_stats',
                                },
                            },
                            '_metadata': {
                                'type': 'object',
                                'properties': {
                                    'next': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next': '$._metadata.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Stats for a single send',
                'properties': {
                    'id': {
                        'type': 'string',
                        'format': 'uuid',
                        'description': 'The single send ID',
                    },
                    'ab_phase': {
                        'type': ['null', 'string'],
                        'description': 'The A/B test phase',
                    },
                    'ab_variation': {
                        'type': ['null', 'string'],
                        'description': 'The A/B test variation',
                    },
                    'aggregation': {
                        'type': ['null', 'string'],
                        'description': 'The aggregation type',
                    },
                    'stats': {
                        'type': ['null', 'object'],
                        'properties': {
                            'bounce_drops': {'type': 'integer'},
                            'bounces': {'type': 'integer'},
                            'clicks': {'type': 'integer'},
                            'delivered': {'type': 'integer'},
                            'invalid_emails': {'type': 'integer'},
                            'opens': {'type': 'integer'},
                            'requests': {'type': 'integer'},
                            'spam_report_drops': {'type': 'integer'},
                            'spam_reports': {'type': 'integer'},
                            'unique_clicks': {'type': 'integer'},
                            'unique_opens': {'type': 'integer'},
                            'unsubscribes': {'type': 'integer'},
                        },
                        'description': 'Email statistics for the single send',
                    },
                },
                'x-airbyte-entity-name': 'singlesend_stats',
                'x-airbyte-stream-name': 'singlesend_stats',
            },
        ),
        EntityDefinition(
            name='bounces',
            stream_name='bounces',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/suppression/bounces',
                    action=Action.LIST,
                    description='Returns all bounced email records.',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A bounced email record',
                            'properties': {
                                'created': {'type': 'integer', 'description': 'Unix timestamp when the bounce occurred'},
                                'email': {'type': 'string', 'description': 'The email address that bounced'},
                                'reason': {'type': 'string', 'description': 'The reason for the bounce'},
                                'status': {'type': 'string', 'description': 'The enhanced status code for the bounce'},
                            },
                            'x-airbyte-entity-name': 'bounces',
                            'x-airbyte-stream-name': 'bounces',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A bounced email record',
                'properties': {
                    'created': {'type': 'integer', 'description': 'Unix timestamp when the bounce occurred'},
                    'email': {'type': 'string', 'description': 'The email address that bounced'},
                    'reason': {'type': 'string', 'description': 'The reason for the bounce'},
                    'status': {'type': 'string', 'description': 'The enhanced status code for the bounce'},
                },
                'x-airbyte-entity-name': 'bounces',
                'x-airbyte-stream-name': 'bounces',
            },
        ),
        EntityDefinition(
            name='blocks',
            stream_name='blocks',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/suppression/blocks',
                    action=Action.LIST,
                    description='Returns all blocked email records.',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A blocked email record',
                            'properties': {
                                'created': {'type': 'integer', 'description': 'Unix timestamp when the block occurred'},
                                'email': {'type': 'string', 'description': 'The blocked email address'},
                                'reason': {'type': 'string', 'description': 'The reason for the block'},
                                'status': {'type': 'string', 'description': 'The status code for the block'},
                            },
                            'x-airbyte-entity-name': 'blocks',
                            'x-airbyte-stream-name': 'blocks',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A blocked email record',
                'properties': {
                    'created': {'type': 'integer', 'description': 'Unix timestamp when the block occurred'},
                    'email': {'type': 'string', 'description': 'The blocked email address'},
                    'reason': {'type': 'string', 'description': 'The reason for the block'},
                    'status': {'type': 'string', 'description': 'The status code for the block'},
                },
                'x-airbyte-entity-name': 'blocks',
                'x-airbyte-stream-name': 'blocks',
            },
        ),
        EntityDefinition(
            name='spam_reports',
            stream_name='spam_reports',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/suppression/spam_reports',
                    action=Action.LIST,
                    description='Returns all spam report records.',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A spam report record',
                            'properties': {
                                'created': {'type': 'integer', 'description': 'Unix timestamp when the spam report was received'},
                                'email': {'type': 'string', 'description': 'The email address that reported spam'},
                                'ip': {'type': 'string', 'description': 'The IP address from which the email was sent'},
                            },
                            'x-airbyte-entity-name': 'spam_reports',
                            'x-airbyte-stream-name': 'spam_reports',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A spam report record',
                'properties': {
                    'created': {'type': 'integer', 'description': 'Unix timestamp when the spam report was received'},
                    'email': {'type': 'string', 'description': 'The email address that reported spam'},
                    'ip': {'type': 'string', 'description': 'The IP address from which the email was sent'},
                },
                'x-airbyte-entity-name': 'spam_reports',
                'x-airbyte-stream-name': 'spam_reports',
            },
        ),
        EntityDefinition(
            name='invalid_emails',
            stream_name='invalid_emails',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/suppression/invalid_emails',
                    action=Action.LIST,
                    description='Returns all invalid email records.',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'An invalid email record',
                            'properties': {
                                'created': {'type': 'integer', 'description': 'Unix timestamp when the invalid email was recorded'},
                                'email': {'type': 'string', 'description': 'The invalid email address'},
                                'reason': {'type': 'string', 'description': 'The reason the email is invalid'},
                            },
                            'x-airbyte-entity-name': 'invalid_emails',
                            'x-airbyte-stream-name': 'invalid_emails',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An invalid email record',
                'properties': {
                    'created': {'type': 'integer', 'description': 'Unix timestamp when the invalid email was recorded'},
                    'email': {'type': 'string', 'description': 'The invalid email address'},
                    'reason': {'type': 'string', 'description': 'The reason the email is invalid'},
                },
                'x-airbyte-entity-name': 'invalid_emails',
                'x-airbyte-stream-name': 'invalid_emails',
            },
        ),
        EntityDefinition(
            name='global_suppressions',
            stream_name='global_suppressions',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/suppression/unsubscribes',
                    action=Action.LIST,
                    description='Returns all globally unsubscribed email addresses.',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A globally suppressed email address',
                            'properties': {
                                'created': {'type': 'integer', 'description': 'Unix timestamp when the global suppression was created'},
                                'email': {'type': 'string', 'description': 'The globally suppressed email address'},
                            },
                            'x-airbyte-entity-name': 'global_suppressions',
                            'x-airbyte-stream-name': 'global_suppressions',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A globally suppressed email address',
                'properties': {
                    'created': {'type': 'integer', 'description': 'Unix timestamp when the global suppression was created'},
                    'email': {'type': 'string', 'description': 'The globally suppressed email address'},
                },
                'x-airbyte-entity-name': 'global_suppressions',
                'x-airbyte-stream-name': 'global_suppressions',
            },
        ),
        EntityDefinition(
            name='suppression_groups',
            stream_name='suppression_groups',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/asm/groups',
                    action=Action.LIST,
                    description='Returns all suppression (unsubscribe) groups.',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A suppression (unsubscribe) group',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique suppression group identifier'},
                                'name': {'type': 'string', 'description': 'Suppression group name'},
                                'description': {'type': 'string', 'description': 'Description of the suppression group'},
                                'is_default': {'type': 'boolean', 'description': 'Whether this is the default suppression group'},
                                'unsubscribes': {'type': 'integer', 'description': 'Number of unsubscribes in this group'},
                            },
                            'x-airbyte-entity-name': 'suppression_groups',
                            'x-airbyte-stream-name': 'suppression_groups',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v3/asm/groups/{group_id}',
                    action=Action.GET,
                    description='Returns information about a single suppression group.',
                    path_params=['group_id'],
                    path_params_schema={
                        'group_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A suppression (unsubscribe) group',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique suppression group identifier'},
                            'name': {'type': 'string', 'description': 'Suppression group name'},
                            'description': {'type': 'string', 'description': 'Description of the suppression group'},
                            'is_default': {'type': 'boolean', 'description': 'Whether this is the default suppression group'},
                            'unsubscribes': {'type': 'integer', 'description': 'Number of unsubscribes in this group'},
                        },
                        'x-airbyte-entity-name': 'suppression_groups',
                        'x-airbyte-stream-name': 'suppression_groups',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A suppression (unsubscribe) group',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique suppression group identifier'},
                    'name': {'type': 'string', 'description': 'Suppression group name'},
                    'description': {'type': 'string', 'description': 'Description of the suppression group'},
                    'is_default': {'type': 'boolean', 'description': 'Whether this is the default suppression group'},
                    'unsubscribes': {'type': 'integer', 'description': 'Number of unsubscribes in this group'},
                },
                'x-airbyte-entity-name': 'suppression_groups',
                'x-airbyte-stream-name': 'suppression_groups',
            },
        ),
        EntityDefinition(
            name='suppression_group_members',
            stream_name='suppression_group_members',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/asm/suppressions',
                    action=Action.LIST,
                    description='Returns all suppressions across all groups.',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A member of a suppression group',
                            'properties': {
                                'email': {'type': 'string', 'description': 'The suppressed email address'},
                                'group_id': {'type': 'integer', 'description': 'ID of the suppression group'},
                                'group_name': {'type': 'string', 'description': 'Name of the suppression group'},
                                'created_at': {'type': 'integer', 'description': 'Unix timestamp when the suppression was created'},
                            },
                            'x-airbyte-entity-name': 'suppression_group_members',
                            'x-airbyte-stream-name': 'suppression_group_members',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A member of a suppression group',
                'properties': {
                    'email': {'type': 'string', 'description': 'The suppressed email address'},
                    'group_id': {'type': 'integer', 'description': 'ID of the suppression group'},
                    'group_name': {'type': 'string', 'description': 'Name of the suppression group'},
                    'created_at': {'type': 'integer', 'description': 'Unix timestamp when the suppression was created'},
                },
                'x-airbyte-entity-name': 'suppression_group_members',
                'x-airbyte-stream-name': 'suppression_group_members',
            },
        ),
    ],
    search_field_paths={
        'bounces': [
            'created',
            'email',
            'reason',
            'status',
        ],
        'blocks': [
            'created',
            'email',
            'reason',
            'status',
        ],
        'campaigns': [
            'channels',
            'channels[]',
            'created_at',
            'id',
            'is_abtest',
            'name',
            'status',
            'updated_at',
        ],
        'contacts': [
            'address_line_1',
            'address_line_2',
            'alternate_emails',
            'alternate_emails[]',
            'city',
            'contact_id',
            'country',
            'created_at',
            'custom_fields',
            'email',
            'facebook',
            'first_name',
            'last_name',
            'line',
            'list_ids',
            'list_ids[]',
            'phone_number',
            'postal_code',
            'state_province_region',
            'unique_name',
            'updated_at',
            'whatsapp',
        ],
        'global_suppressions': ['created', 'email'],
        'invalid_emails': ['created', 'email', 'reason'],
        'lists': [
            '_metadata',
            '_metadata.self',
            'contact_count',
            'id',
            'name',
        ],
        'segments': [
            'contacts_count',
            'created_at',
            'id',
            'name',
            'next_sample_update',
            'parent_list_ids',
            'parent_list_ids[]',
            'query_version',
            'sample_updated_at',
            'status',
            'status.query_validation',
            'updated_at',
        ],
        'singlesend_stats': [
            'ab_phase',
            'ab_variation',
            'aggregation',
            'id',
            'stats',
            'stats.bounce_drops',
            'stats.bounces',
            'stats.clicks',
            'stats.delivered',
            'stats.invalid_emails',
            'stats.opens',
            'stats.requests',
            'stats.spam_report_drops',
            'stats.spam_reports',
            'stats.unique_clicks',
            'stats.unique_opens',
            'stats.unsubscribes',
        ],
        'singlesends': [
            'categories',
            'categories[]',
            'created_at',
            'id',
            'is_abtest',
            'name',
            'send_at',
            'status',
            'updated_at',
        ],
        'stats_automations': [
            'aggregation',
            'id',
            'stats',
            'stats.bounce_drops',
            'stats.bounces',
            'stats.clicks',
            'stats.delivered',
            'stats.invalid_emails',
            'stats.opens',
            'stats.requests',
            'stats.spam_report_drops',
            'stats.spam_reports',
            'stats.unique_clicks',
            'stats.unique_opens',
            'stats.unsubscribes',
            'step_id',
        ],
        'suppression_group_members': [
            'created_at',
            'email',
            'group_id',
            'group_name',
        ],
        'suppression_groups': [
            'description',
            'id',
            'is_default',
            'name',
            'unsubscribes',
        ],
        'templates': [
            'generation',
            'id',
            'name',
            'updated_at',
            'versions',
            'versions[]',
        ],
    },
)