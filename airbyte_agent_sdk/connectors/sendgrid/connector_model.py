"""
Connector model for sendgrid.

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
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

SendgridConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('fbb5fbe2-16ad-4cf4-af7d-ff9d9c316c87'),
    name='sendgrid',
    version='1.0.3',
    base_url='https://api.sendgrid.com',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AuthConfigSpec(
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'SendGrid contacts with email and custom fields',
                                        'when_to_use': 'Looking up email contacts or subscriber information',
                                        'trigger_phrases': ['sendgrid contact', 'email contact'],
                                        'freshness': 'live',
                                        'example_questions': ['Find a contact in SendGrid'],
                                        'search_strategy': 'Search by email',
                                    },
                                },
                            },
                            'contact_count': {'type': 'integer', 'description': 'Total number of contacts'},
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
                    meta_extractor={'next': '$._metadata.next', 'contact_count': '$.contact_count'},
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
                        'x-airbyte-ai-hints': {
                            'summary': 'SendGrid contacts with email and custom fields',
                            'when_to_use': 'Looking up email contacts or subscriber information',
                            'trigger_phrases': ['sendgrid contact', 'email contact'],
                            'freshness': 'live',
                            'example_questions': ['Find a contact in SendGrid'],
                            'search_strategy': 'Search by email',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'SendGrid contacts with email and custom fields',
                    'when_to_use': 'Looking up email contacts or subscriber information',
                    'trigger_phrases': ['sendgrid contact', 'email contact'],
                    'freshness': 'live',
                    'example_questions': ['Find a contact in SendGrid'],
                    'search_strategy': 'Search by email',
                },
            },
            ai_hints={
                'summary': 'SendGrid contacts with email and custom fields',
                'when_to_use': 'Looking up email contacts or subscriber information',
                'trigger_phrases': ['sendgrid contact', 'email contact'],
                'freshness': 'live',
                'example_questions': ['Find a contact in SendGrid'],
                'search_strategy': 'Search by email',
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
                            'minimum': 1,
                            'maximum': 1000,
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Contact lists for organizing SendGrid recipients',
                                        'when_to_use': 'Questions about email lists or recipient management',
                                        'trigger_phrases': ['sendgrid list', 'email list', 'recipient list'],
                                        'freshness': 'live',
                                        'example_questions': ['What lists are in SendGrid?'],
                                        'search_strategy': 'Search by name',
                                    },
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Contact lists for organizing SendGrid recipients',
                            'when_to_use': 'Questions about email lists or recipient management',
                            'trigger_phrases': ['sendgrid list', 'email list', 'recipient list'],
                            'freshness': 'live',
                            'example_questions': ['What lists are in SendGrid?'],
                            'search_strategy': 'Search by name',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Contact lists for organizing SendGrid recipients',
                    'when_to_use': 'Questions about email lists or recipient management',
                    'trigger_phrases': ['sendgrid list', 'email list', 'recipient list'],
                    'freshness': 'live',
                    'example_questions': ['What lists are in SendGrid?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Contact lists for organizing SendGrid recipients',
                'when_to_use': 'Questions about email lists or recipient management',
                'trigger_phrases': ['sendgrid list', 'email list', 'recipient list'],
                'freshness': 'live',
                'example_questions': ['What lists are in SendGrid?'],
                'search_strategy': 'Search by name',
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Dynamic segments of contacts based on conditions',
                                        'when_to_use': 'Questions about contact segments or audience targeting',
                                        'trigger_phrases': ['sendgrid segment', 'contact segment'],
                                        'freshness': 'live',
                                        'example_questions': ['What segments are defined?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    no_pagination='The SendGrid /v3/marketing/segments/2.0 endpoint returns the full list of segments in a single response; the API does not expose pagination parameters.',
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Dynamic segments of contacts based on conditions',
                            'when_to_use': 'Questions about contact segments or audience targeting',
                            'trigger_phrases': ['sendgrid segment', 'contact segment'],
                            'freshness': 'live',
                            'example_questions': ['What segments are defined?'],
                            'search_strategy': 'Search by name',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Dynamic segments of contacts based on conditions',
                    'when_to_use': 'Questions about contact segments or audience targeting',
                    'trigger_phrases': ['sendgrid segment', 'contact segment'],
                    'freshness': 'live',
                    'example_questions': ['What segments are defined?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Dynamic segments of contacts based on conditions',
                'when_to_use': 'Questions about contact segments or audience targeting',
                'trigger_phrases': ['sendgrid segment', 'contact segment'],
                'freshness': 'live',
                'example_questions': ['What segments are defined?'],
                'search_strategy': 'Search by name',
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
                            'minimum': 1,
                            'maximum': 100,
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Legacy SendGrid email campaigns',
                                        'when_to_use': 'Questions about legacy campaign details',
                                        'trigger_phrases': ['sendgrid campaign', 'legacy campaign'],
                                        'freshness': 'live',
                                        'example_questions': ['Show SendGrid campaigns'],
                                        'search_strategy': 'Search by title',
                                    },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Legacy SendGrid email campaigns',
                    'when_to_use': 'Questions about legacy campaign details',
                    'trigger_phrases': ['sendgrid campaign', 'legacy campaign'],
                    'freshness': 'live',
                    'example_questions': ['Show SendGrid campaigns'],
                    'search_strategy': 'Search by title',
                },
            },
            ai_hints={
                'summary': 'Legacy SendGrid email campaigns',
                'when_to_use': 'Questions about legacy campaign details',
                'trigger_phrases': ['sendgrid campaign', 'legacy campaign'],
                'freshness': 'live',
                'example_questions': ['Show SendGrid campaigns'],
                'search_strategy': 'Search by title',
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
                            'minimum': 1,
                            'maximum': 100,
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Single Send email campaigns in SendGrid (modern API)',
                                        'when_to_use': 'Questions about email sends or campaign performance',
                                        'trigger_phrases': ['single send', 'email send', 'sendgrid email'],
                                        'freshness': 'live',
                                        'example_questions': ['Show recent email sends'],
                                        'search_strategy': 'Search by name or filter by status',
                                    },
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Single Send email campaigns in SendGrid (modern API)',
                            'when_to_use': 'Questions about email sends or campaign performance',
                            'trigger_phrases': ['single send', 'email send', 'sendgrid email'],
                            'freshness': 'live',
                            'example_questions': ['Show recent email sends'],
                            'search_strategy': 'Search by name or filter by status',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Single Send email campaigns in SendGrid (modern API)',
                    'when_to_use': 'Questions about email sends or campaign performance',
                    'trigger_phrases': ['single send', 'email send', 'sendgrid email'],
                    'freshness': 'live',
                    'example_questions': ['Show recent email sends'],
                    'search_strategy': 'Search by name or filter by status',
                },
            },
            ai_hints={
                'summary': 'Single Send email campaigns in SendGrid (modern API)',
                'when_to_use': 'Questions about email sends or campaign performance',
                'trigger_phrases': ['single send', 'email send', 'sendgrid email'],
                'freshness': 'live',
                'example_questions': ['Show recent email sends'],
                'search_strategy': 'Search by name or filter by status',
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
                            'minimum': 1,
                            'maximum': 200,
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Email templates for SendGrid campaigns and transactional emails',
                                        'when_to_use': 'Questions about available email templates',
                                        'trigger_phrases': ['sendgrid template', 'email template'],
                                        'freshness': 'live',
                                        'example_questions': ['What email templates are available?'],
                                        'search_strategy': 'Search by name',
                                    },
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
                    record_extractor='$.templates',
                    meta_extractor={'next': '$._metadata.next'},
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Email templates for SendGrid campaigns and transactional emails',
                            'when_to_use': 'Questions about available email templates',
                            'trigger_phrases': ['sendgrid template', 'email template'],
                            'freshness': 'live',
                            'example_questions': ['What email templates are available?'],
                            'search_strategy': 'Search by name',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Email templates for SendGrid campaigns and transactional emails',
                    'when_to_use': 'Questions about available email templates',
                    'trigger_phrases': ['sendgrid template', 'email template'],
                    'freshness': 'live',
                    'example_questions': ['What email templates are available?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Email templates for SendGrid campaigns and transactional emails',
                'when_to_use': 'Questions about available email templates',
                'trigger_phrases': ['sendgrid template', 'email template'],
                'freshness': 'live',
                'example_questions': ['What email templates are available?'],
                'search_strategy': 'Search by name',
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
                            'minimum': 1,
                            'maximum': 50,
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Performance statistics for Single Send campaigns',
                                        'when_to_use': 'Questions about email send performance or delivery metrics',
                                        'trigger_phrases': ['send stats', 'delivery stats', 'email performance'],
                                        'freshness': 'live',
                                        'example_questions': ['What were the stats for a send?'],
                                        'search_strategy': 'Filter by single send',
                                    },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Performance statistics for Single Send campaigns',
                    'when_to_use': 'Questions about email send performance or delivery metrics',
                    'trigger_phrases': ['send stats', 'delivery stats', 'email performance'],
                    'freshness': 'live',
                    'example_questions': ['What were the stats for a send?'],
                    'search_strategy': 'Filter by single send',
                },
            },
            ai_hints={
                'summary': 'Performance statistics for Single Send campaigns',
                'when_to_use': 'Questions about email send performance or delivery metrics',
                'trigger_phrases': ['send stats', 'delivery stats', 'email performance'],
                'freshness': 'live',
                'example_questions': ['What were the stats for a send?'],
                'search_strategy': 'Filter by single send',
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
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                            'minimum': 0,
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
                            'x-airbyte-ai-hints': {
                                'summary': 'Email bounce records from SendGrid deliveries',
                                'when_to_use': 'Questions about email bounces or delivery failures',
                                'trigger_phrases': ['bounce', 'email bounce', 'delivery failure'],
                                'freshness': 'live',
                                'example_questions': ['Show recent email bounces'],
                                'search_strategy': 'Search by email or filter by date',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
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
                'x-airbyte-ai-hints': {
                    'summary': 'Email bounce records from SendGrid deliveries',
                    'when_to_use': 'Questions about email bounces or delivery failures',
                    'trigger_phrases': ['bounce', 'email bounce', 'delivery failure'],
                    'freshness': 'live',
                    'example_questions': ['Show recent email bounces'],
                    'search_strategy': 'Search by email or filter by date',
                },
            },
            ai_hints={
                'summary': 'Email bounce records from SendGrid deliveries',
                'when_to_use': 'Questions about email bounces or delivery failures',
                'trigger_phrases': ['bounce', 'email bounce', 'delivery failure'],
                'freshness': 'live',
                'example_questions': ['Show recent email bounces'],
                'search_strategy': 'Search by email or filter by date',
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
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                            'minimum': 0,
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
                            'x-airbyte-ai-hints': {
                                'summary': 'Blocked email addresses that failed to deliver',
                                'when_to_use': 'Questions about blocked emails or delivery blocks',
                                'trigger_phrases': ['blocked email', 'delivery block'],
                                'freshness': 'live',
                                'example_questions': ['What emails are blocked?'],
                                'search_strategy': 'Search by email or filter by date',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
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
                'x-airbyte-ai-hints': {
                    'summary': 'Blocked email addresses that failed to deliver',
                    'when_to_use': 'Questions about blocked emails or delivery blocks',
                    'trigger_phrases': ['blocked email', 'delivery block'],
                    'freshness': 'live',
                    'example_questions': ['What emails are blocked?'],
                    'search_strategy': 'Search by email or filter by date',
                },
            },
            ai_hints={
                'summary': 'Blocked email addresses that failed to deliver',
                'when_to_use': 'Questions about blocked emails or delivery blocks',
                'trigger_phrases': ['blocked email', 'delivery block'],
                'freshness': 'live',
                'example_questions': ['What emails are blocked?'],
                'search_strategy': 'Search by email or filter by date',
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
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                            'minimum': 0,
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
                            'x-airbyte-ai-hints': {
                                'summary': 'Spam reports from recipients marking emails as spam',
                                'when_to_use': 'Questions about spam complaints or sender reputation',
                                'trigger_phrases': ['spam report', 'spam complaint', 'marked as spam'],
                                'freshness': 'live',
                                'example_questions': ['Show spam reports'],
                                'search_strategy': 'Search by email or filter by date',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
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
                'x-airbyte-ai-hints': {
                    'summary': 'Spam reports from recipients marking emails as spam',
                    'when_to_use': 'Questions about spam complaints or sender reputation',
                    'trigger_phrases': ['spam report', 'spam complaint', 'marked as spam'],
                    'freshness': 'live',
                    'example_questions': ['Show spam reports'],
                    'search_strategy': 'Search by email or filter by date',
                },
            },
            ai_hints={
                'summary': 'Spam reports from recipients marking emails as spam',
                'when_to_use': 'Questions about spam complaints or sender reputation',
                'trigger_phrases': ['spam report', 'spam complaint', 'marked as spam'],
                'freshness': 'live',
                'example_questions': ['Show spam reports'],
                'search_strategy': 'Search by email or filter by date',
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
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                            'minimum': 0,
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
                            'x-airbyte-ai-hints': {
                                'summary': 'Invalid email addresses that could not be delivered to',
                                'when_to_use': 'Questions about invalid email addresses or list hygiene',
                                'trigger_phrases': ['invalid email', 'bad email address'],
                                'freshness': 'live',
                                'example_questions': ['What emails are invalid?'],
                                'search_strategy': 'Search by email or filter by date',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
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
                'x-airbyte-ai-hints': {
                    'summary': 'Invalid email addresses that could not be delivered to',
                    'when_to_use': 'Questions about invalid email addresses or list hygiene',
                    'trigger_phrases': ['invalid email', 'bad email address'],
                    'freshness': 'live',
                    'example_questions': ['What emails are invalid?'],
                    'search_strategy': 'Search by email or filter by date',
                },
            },
            ai_hints={
                'summary': 'Invalid email addresses that could not be delivered to',
                'when_to_use': 'Questions about invalid email addresses or list hygiene',
                'trigger_phrases': ['invalid email', 'bad email address'],
                'freshness': 'live',
                'example_questions': ['What emails are invalid?'],
                'search_strategy': 'Search by email or filter by date',
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
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                            'minimum': 0,
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
                            'x-airbyte-ai-hints': {
                                'summary': 'Globally suppressed email addresses (unsubscribed from all)',
                                'when_to_use': 'Questions about global unsubscribes or suppression list',
                                'trigger_phrases': ['global suppression', 'global unsubscribe'],
                                'freshness': 'live',
                                'example_questions': ['Is an email globally suppressed?'],
                                'search_strategy': 'Search by email',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
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
                'x-airbyte-ai-hints': {
                    'summary': 'Globally suppressed email addresses (unsubscribed from all)',
                    'when_to_use': 'Questions about global unsubscribes or suppression list',
                    'trigger_phrases': ['global suppression', 'global unsubscribe'],
                    'freshness': 'live',
                    'example_questions': ['Is an email globally suppressed?'],
                    'search_strategy': 'Search by email',
                },
            },
            ai_hints={
                'summary': 'Globally suppressed email addresses (unsubscribed from all)',
                'when_to_use': 'Questions about global unsubscribes or suppression list',
                'trigger_phrases': ['global suppression', 'global unsubscribe'],
                'freshness': 'live',
                'example_questions': ['Is an email globally suppressed?'],
                'search_strategy': 'Search by email',
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
                            'x-airbyte-ai-hints': {
                                'summary': 'Suppression groups for managing email preferences',
                                'when_to_use': 'Questions about unsubscribe groups or preference management',
                                'trigger_phrases': ['suppression group', 'unsubscribe group', 'email preference'],
                                'freshness': 'static',
                                'example_questions': ['What suppression groups exist?'],
                                'search_strategy': 'List all suppression groups',
                            },
                        },
                    },
                    no_pagination='The SendGrid /v3/asm/groups endpoint returns the full list of suppression groups in a single response; the API does not expose pagination parameters.',
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Suppression groups for managing email preferences',
                            'when_to_use': 'Questions about unsubscribe groups or preference management',
                            'trigger_phrases': ['suppression group', 'unsubscribe group', 'email preference'],
                            'freshness': 'static',
                            'example_questions': ['What suppression groups exist?'],
                            'search_strategy': 'List all suppression groups',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Suppression groups for managing email preferences',
                    'when_to_use': 'Questions about unsubscribe groups or preference management',
                    'trigger_phrases': ['suppression group', 'unsubscribe group', 'email preference'],
                    'freshness': 'static',
                    'example_questions': ['What suppression groups exist?'],
                    'search_strategy': 'List all suppression groups',
                },
            },
            ai_hints={
                'summary': 'Suppression groups for managing email preferences',
                'when_to_use': 'Questions about unsubscribe groups or preference management',
                'trigger_phrases': ['suppression group', 'unsubscribe group', 'email preference'],
                'freshness': 'static',
                'example_questions': ['What suppression groups exist?'],
                'search_strategy': 'List all suppression groups',
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
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                            'minimum': 0,
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
                            'x-airbyte-ai-hints': {
                                'summary': 'Contacts suppressed within specific suppression groups',
                                'when_to_use': 'Questions about who has opted out of specific email groups',
                                'trigger_phrases': ['group member', 'suppressed contact'],
                                'freshness': 'live',
                                'example_questions': ['Who opted out of a specific email group?'],
                                'search_strategy': 'Filter by suppression group',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
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
                'x-airbyte-ai-hints': {
                    'summary': 'Contacts suppressed within specific suppression groups',
                    'when_to_use': 'Questions about who has opted out of specific email groups',
                    'trigger_phrases': ['group member', 'suppressed contact'],
                    'freshness': 'live',
                    'example_questions': ['Who opted out of a specific email group?'],
                    'search_strategy': 'Filter by suppression group',
                },
            },
            ai_hints={
                'summary': 'Contacts suppressed within specific suppression groups',
                'when_to_use': 'Questions about who has opted out of specific email groups',
                'trigger_phrases': ['group member', 'suppressed contact'],
                'freshness': 'live',
                'example_questions': ['Who opted out of a specific email group?'],
                'search_strategy': 'Filter by suppression group',
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='bounces',
                x_airbyte_name='bounces',
                fields=[
                    CacheFieldConfig(
                        name='created',
                        type=['null', 'integer'],
                        description='Unix timestamp when the bounce occurred',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='The email address that bounced',
                    ),
                    CacheFieldConfig(
                        name='reason',
                        type=['null', 'string'],
                        description='The reason for the bounce',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='The enhanced status code for the bounce',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='blocks',
                x_airbyte_name='blocks',
                fields=[
                    CacheFieldConfig(
                        name='created',
                        type=['null', 'integer'],
                        description='Unix timestamp when the block occurred',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='The blocked email address',
                    ),
                    CacheFieldConfig(
                        name='reason',
                        type=['null', 'string'],
                        description='The reason for the block',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='The status code for the block',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='campaigns',
                suggested=True,
                x_airbyte_name='campaigns',
                fields=[
                    CacheFieldConfig(
                        name='channels',
                        type=['null', 'array'],
                        description='Channels for this campaign',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the campaign was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique campaign identifier',
                    ),
                    CacheFieldConfig(
                        name='is_abtest',
                        type=['null', 'boolean'],
                        description='Whether this campaign is an A/B test',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Campaign name',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Campaign status',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the campaign was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='contacts',
                suggested=True,
                x_airbyte_name='contacts',
                fields=[
                    CacheFieldConfig(
                        name='address_line_1',
                        type=['null', 'string'],
                        description='Address line 1',
                    ),
                    CacheFieldConfig(
                        name='address_line_2',
                        type=['null', 'string'],
                        description='Address line 2',
                    ),
                    CacheFieldConfig(
                        name='alternate_emails',
                        type=['null', 'array'],
                        description='Alternate email addresses',
                    ),
                    CacheFieldConfig(
                        name='city',
                        type=['null', 'string'],
                        description='City',
                    ),
                    CacheFieldConfig(
                        name='contact_id',
                        type=['null', 'string'],
                        description='Unique contact identifier used by Airbyte',
                    ),
                    CacheFieldConfig(
                        name='country',
                        type=['null', 'string'],
                        description='Country',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the contact was created',
                    ),
                    CacheFieldConfig(
                        name='custom_fields',
                        type=['null', 'object'],
                        description='Custom field values',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='Contact email address',
                    ),
                    CacheFieldConfig(
                        name='facebook',
                        type=['null', 'string'],
                        description='Facebook ID',
                    ),
                    CacheFieldConfig(
                        name='first_name',
                        type=['null', 'string'],
                        description='Contact first name',
                    ),
                    CacheFieldConfig(
                        name='last_name',
                        type=['null', 'string'],
                        description='Contact last name',
                    ),
                    CacheFieldConfig(
                        name='line',
                        type=['null', 'string'],
                        description='LINE ID',
                    ),
                    CacheFieldConfig(
                        name='list_ids',
                        type=['null', 'array'],
                        description='IDs of lists the contact belongs to',
                    ),
                    CacheFieldConfig(
                        name='phone_number',
                        type=['null', 'string'],
                        description='Phone number',
                    ),
                    CacheFieldConfig(
                        name='postal_code',
                        type=['null', 'string'],
                        description='Postal code',
                    ),
                    CacheFieldConfig(
                        name='state_province_region',
                        type=['null', 'string'],
                        description='State, province, or region',
                    ),
                    CacheFieldConfig(
                        name='unique_name',
                        type=['null', 'string'],
                        description='Unique name for the contact',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the contact was last updated',
                    ),
                    CacheFieldConfig(
                        name='whatsapp',
                        type=['null', 'string'],
                        description='WhatsApp number',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='global_suppressions',
                x_airbyte_name='global_suppressions',
                fields=[
                    CacheFieldConfig(
                        name='created',
                        type=['null', 'integer'],
                        description='Unix timestamp when the global suppression was created',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='The globally suppressed email address',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='invalid_emails',
                x_airbyte_name='invalid_emails',
                fields=[
                    CacheFieldConfig(
                        name='created',
                        type=['null', 'integer'],
                        description='Unix timestamp when the invalid email was recorded',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='The invalid email address',
                    ),
                    CacheFieldConfig(
                        name='reason',
                        type=['null', 'string'],
                        description='The reason the email is invalid',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='lists',
                suggested=True,
                x_airbyte_name='lists',
                fields=[
                    CacheFieldConfig(
                        name='_metadata',
                        type=['null', 'object'],
                        description='Metadata about the list resource',
                        properties={
                            'self': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='contact_count',
                        type=['null', 'integer'],
                        description='Number of contacts in the list',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique list identifier',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the list',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='segments',
                suggested=True,
                x_airbyte_name='segments',
                fields=[
                    CacheFieldConfig(
                        name='contacts_count',
                        type=['null', 'integer'],
                        description='Number of contacts in the segment',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the segment was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique segment identifier',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Segment name',
                    ),
                    CacheFieldConfig(
                        name='next_sample_update',
                        type=['null', 'string'],
                        description='When the next sample update will occur',
                    ),
                    CacheFieldConfig(
                        name='parent_list_ids',
                        type=['null', 'array'],
                        description='IDs of parent lists',
                    ),
                    CacheFieldConfig(
                        name='query_version',
                        type=['null', 'string'],
                        description='Query version used',
                    ),
                    CacheFieldConfig(
                        name='sample_updated_at',
                        type=['null', 'string'],
                        description='When the sample was last updated',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'object'],
                        description='Segment status details',
                        properties={
                            'query_validation': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the segment was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='singlesend_stats',
                suggested=True,
                x_airbyte_name='singlesend_stats',
                fields=[
                    CacheFieldConfig(
                        name='ab_phase',
                        type=['null', 'string'],
                        description='The A/B test phase',
                    ),
                    CacheFieldConfig(
                        name='ab_variation',
                        type=['null', 'string'],
                        description='The A/B test variation',
                    ),
                    CacheFieldConfig(
                        name='aggregation',
                        type=['null', 'string'],
                        description='The aggregation type',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='The single send ID',
                    ),
                    CacheFieldConfig(
                        name='stats',
                        type=['null', 'object'],
                        description='Email statistics for the single send',
                        properties={
                            'bounce_drops': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'bounces': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'clicks': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'delivered': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'invalid_emails': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'opens': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'requests': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'spam_report_drops': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'spam_reports': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'unique_clicks': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'unique_opens': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'unsubscribes': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                        },
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='singlesends',
                suggested=True,
                x_airbyte_name='singlesends',
                fields=[
                    CacheFieldConfig(
                        name='categories',
                        type=['null', 'array'],
                        description='Categories associated with this single send',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the single send was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique single send identifier',
                    ),
                    CacheFieldConfig(
                        name='is_abtest',
                        type=['null', 'boolean'],
                        description='Whether this is an A/B test',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Single send name',
                    ),
                    CacheFieldConfig(
                        name='send_at',
                        type=['null', 'string'],
                        description='Scheduled send time',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Current status: draft, scheduled, or triggered',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the single send was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='suppression_group_members',
                x_airbyte_name='suppression_group_members',
                fields=[
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'integer'],
                        description='Unix timestamp when the suppression was created',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='The suppressed email address',
                    ),
                    CacheFieldConfig(
                        name='group_id',
                        type=['null', 'integer'],
                        description='ID of the suppression group',
                    ),
                    CacheFieldConfig(
                        name='group_name',
                        type=['null', 'string'],
                        description='Name of the suppression group',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='suppression_groups',
                x_airbyte_name='suppression_groups',
                fields=[
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Description of the suppression group',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique suppression group identifier',
                    ),
                    CacheFieldConfig(
                        name='is_default',
                        type=['null', 'boolean'],
                        description='Whether this is the default suppression group',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Suppression group name',
                    ),
                    CacheFieldConfig(
                        name='unsubscribes',
                        type=['null', 'integer'],
                        description='Number of unsubscribes in this group',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='templates',
                suggested=True,
                x_airbyte_name='templates',
                fields=[
                    CacheFieldConfig(
                        name='generation',
                        type=['null', 'string'],
                        description='Template generation (legacy or dynamic)',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique template identifier',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Template name',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the template was last updated',
                    ),
                    CacheFieldConfig(
                        name='versions',
                        type=['null', 'array'],
                        description='Template versions',
                    ),
                ],
            ),
        ],
        disable_compaction=True,
    ),
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
    example_questions=ExampleQuestions(
        direct=[
            'List all marketing contacts',
            'Get the details of a specific contact',
            'Show me all marketing lists',
            'List all transactional templates',
            'Show all single sends',
            'List all bounced emails',
            'Show all blocked email addresses',
            'List all spam reports',
            'Show all suppression groups',
        ],
        context_store_search=[
            'How many contacts are in each marketing list?',
            'Which single sends were scheduled in the last month?',
            'What are the most common bounce reasons?',
            'Show me contacts created in the last 7 days',
        ],
        search=[
            'How many contacts are in each marketing list?',
            'Which single sends were scheduled in the last month?',
            'What are the most common bounce reasons?',
            'Show me contacts created in the last 7 days',
        ],
        unsupported=[
            'Send an email',
            'Create a new contact',
            'Delete a bounce record',
            'Update a marketing list',
        ],
    ),
)