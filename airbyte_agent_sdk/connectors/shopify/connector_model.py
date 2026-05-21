"""
Connector model for shopify.

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
    EntityRelationshipConfig,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

ShopifyConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('9da77001-af33-4bcd-be46-6252bf9342b9'),
    name='shopify',
    version='0.1.13',
    base_url='https://{shop}.myshopify.com/admin/api/2025-01',
    auth=AuthConfig(
        type=AuthType.API_KEY,
        config={'header': 'X-Shopify-Access-Token', 'in': 'header'},
        user_config_spec=AuthConfigSpec(
            title='Access Token Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='Access Token',
                    description='Your Shopify Admin API access token',
                ),
            },
            auth_mapping={'api_key': '${api_key}'},
            replication_auth_key_mapping={'credentials.api_password': 'api_key'},
            replication_auth_key_constants={'credentials.auth_method': 'api_password'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='customers',
            stream_name='customers',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/customers.json',
                    action=Action.LIST,
                    description='Returns a list of customers from the store',
                    query_params=[
                        'limit',
                        'since_id',
                        'created_at_min',
                        'created_at_max',
                        'updated_at_min',
                        'updated_at_max',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'created_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'customers': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Shopify customer',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique customer identifier'},
                                        'email': {
                                            'type': ['string', 'null'],
                                            'description': 'Customer email address',
                                        },
                                        'accepts_marketing': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the customer accepts marketing',
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the customer was created',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the customer was last updated',
                                        },
                                        'first_name': {
                                            'type': ['string', 'null'],
                                            'description': 'Customer first name',
                                        },
                                        'last_name': {
                                            'type': ['string', 'null'],
                                            'description': 'Customer last name',
                                        },
                                        'orders_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of orders',
                                        },
                                        'state': {
                                            'type': ['string', 'null'],
                                            'description': 'Customer state',
                                        },
                                        'total_spent': {
                                            'type': ['string', 'null'],
                                            'description': 'Total amount spent',
                                        },
                                        'last_order_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'ID of last order',
                                        },
                                        'note': {
                                            'type': ['string', 'null'],
                                            'description': 'Note about the customer',
                                        },
                                        'verified_email': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether email is verified',
                                        },
                                        'multipass_identifier': {
                                            'type': ['string', 'null'],
                                            'description': 'Multipass identifier',
                                        },
                                        'tax_exempt': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether customer is tax exempt',
                                        },
                                        'tags': {
                                            'type': ['string', 'null'],
                                            'description': 'Tags associated with customer',
                                        },
                                        'last_order_name': {
                                            'type': ['string', 'null'],
                                            'description': 'Name of last order',
                                        },
                                        'currency': {
                                            'type': ['string', 'null'],
                                            'description': 'Customer currency',
                                        },
                                        'phone': {
                                            'type': ['string', 'null'],
                                            'description': 'Customer phone number',
                                        },
                                        'addresses': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'A customer address',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Address ID'},
                                                    'customer_id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Customer ID',
                                                    },
                                                    'first_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'First name',
                                                    },
                                                    'last_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Last name',
                                                    },
                                                    'company': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Company name',
                                                    },
                                                    'address1': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Address line 1',
                                                    },
                                                    'address2': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Address line 2',
                                                    },
                                                    'city': {
                                                        'type': ['string', 'null'],
                                                        'description': 'City',
                                                    },
                                                    'province': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Province/State',
                                                    },
                                                    'country': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Country',
                                                    },
                                                    'zip': {
                                                        'type': ['string', 'null'],
                                                        'description': 'ZIP/Postal code',
                                                    },
                                                    'phone': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Phone number',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Full name',
                                                    },
                                                    'province_code': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Province code',
                                                    },
                                                    'country_code': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Country code',
                                                    },
                                                    'country_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Country name',
                                                    },
                                                    'default': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether this is the default address',
                                                    },
                                                },
                                                'required': ['id'],
                                            },
                                        },
                                        'accepts_marketing_updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When marketing acceptance was updated',
                                        },
                                        'marketing_opt_in_level': {
                                            'type': ['string', 'null'],
                                            'description': 'Marketing opt-in level',
                                        },
                                        'tax_exemptions': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                        },
                                        'email_marketing_consent': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'state': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'opt_in_level': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'consent_updated_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                        },
                                                        'consent_collected_from': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'sms_marketing_consent': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'state': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'opt_in_level': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'consent_updated_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                        },
                                                        'consent_collected_from': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                            'description': 'GraphQL API ID',
                                        },
                                        'default_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'A customer address',
                                                    'properties': {
                                                        'id': {'type': 'integer', 'description': 'Address ID'},
                                                        'customer_id': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Customer ID',
                                                        },
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'First name',
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Last name',
                                                        },
                                                        'company': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Company name',
                                                        },
                                                        'address1': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Address line 1',
                                                        },
                                                        'address2': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Address line 2',
                                                        },
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                            'description': 'City',
                                                        },
                                                        'province': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Province/State',
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Country',
                                                        },
                                                        'zip': {
                                                            'type': ['string', 'null'],
                                                            'description': 'ZIP/Postal code',
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Phone number',
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Full name',
                                                        },
                                                        'province_code': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Province code',
                                                        },
                                                        'country_code': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Country code',
                                                        },
                                                        'country_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Country name',
                                                        },
                                                        'default': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether this is the default address',
                                                        },
                                                    },
                                                    'required': ['id'],
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'customers',
                                    'x-airbyte-stream-name': 'customers',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Shopify customers with order history and contact information',
                                        'when_to_use': 'Looking up customer details or purchase history',
                                        'trigger_phrases': ['shopify customer', 'buyer', 'customer info'],
                                        'freshness': 'live',
                                        'example_questions': ['Find a customer in Shopify', 'Show customer order history'],
                                        'search_strategy': 'Search by email, name, or phone',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.customers',
                    meta_extractor={'next_page_url': '@link.next'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/customers/{customer_id}.json',
                    action=Action.GET,
                    description='Retrieves a single customer by ID',
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'customer': {
                                'type': 'object',
                                'description': 'A Shopify customer',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Unique customer identifier'},
                                    'email': {
                                        'type': ['string', 'null'],
                                        'description': 'Customer email address',
                                    },
                                    'accepts_marketing': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the customer accepts marketing',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'When the customer was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'When the customer was last updated',
                                    },
                                    'first_name': {
                                        'type': ['string', 'null'],
                                        'description': 'Customer first name',
                                    },
                                    'last_name': {
                                        'type': ['string', 'null'],
                                        'description': 'Customer last name',
                                    },
                                    'orders_count': {
                                        'type': ['integer', 'null'],
                                        'description': 'Number of orders',
                                    },
                                    'state': {
                                        'type': ['string', 'null'],
                                        'description': 'Customer state',
                                    },
                                    'total_spent': {
                                        'type': ['string', 'null'],
                                        'description': 'Total amount spent',
                                    },
                                    'last_order_id': {
                                        'type': ['integer', 'null'],
                                        'description': 'ID of last order',
                                    },
                                    'note': {
                                        'type': ['string', 'null'],
                                        'description': 'Note about the customer',
                                    },
                                    'verified_email': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether email is verified',
                                    },
                                    'multipass_identifier': {
                                        'type': ['string', 'null'],
                                        'description': 'Multipass identifier',
                                    },
                                    'tax_exempt': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether customer is tax exempt',
                                    },
                                    'tags': {
                                        'type': ['string', 'null'],
                                        'description': 'Tags associated with customer',
                                    },
                                    'last_order_name': {
                                        'type': ['string', 'null'],
                                        'description': 'Name of last order',
                                    },
                                    'currency': {
                                        'type': ['string', 'null'],
                                        'description': 'Customer currency',
                                    },
                                    'phone': {
                                        'type': ['string', 'null'],
                                        'description': 'Customer phone number',
                                    },
                                    'addresses': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A customer address',
                                            'properties': {
                                                'id': {'type': 'integer', 'description': 'Address ID'},
                                                'customer_id': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Customer ID',
                                                },
                                                'first_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'First name',
                                                },
                                                'last_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Last name',
                                                },
                                                'company': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Company name',
                                                },
                                                'address1': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Address line 1',
                                                },
                                                'address2': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Address line 2',
                                                },
                                                'city': {
                                                    'type': ['string', 'null'],
                                                    'description': 'City',
                                                },
                                                'province': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Province/State',
                                                },
                                                'country': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Country',
                                                },
                                                'zip': {
                                                    'type': ['string', 'null'],
                                                    'description': 'ZIP/Postal code',
                                                },
                                                'phone': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Phone number',
                                                },
                                                'name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Full name',
                                                },
                                                'province_code': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Province code',
                                                },
                                                'country_code': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Country code',
                                                },
                                                'country_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Country name',
                                                },
                                                'default': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether this is the default address',
                                                },
                                            },
                                            'required': ['id'],
                                        },
                                    },
                                    'accepts_marketing_updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'When marketing acceptance was updated',
                                    },
                                    'marketing_opt_in_level': {
                                        'type': ['string', 'null'],
                                        'description': 'Marketing opt-in level',
                                    },
                                    'tax_exemptions': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                    },
                                    'email_marketing_consent': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'state': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'opt_in_level': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'consent_updated_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'consent_collected_from': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'sms_marketing_consent': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'state': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'opt_in_level': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'consent_updated_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'consent_collected_from': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                        'description': 'GraphQL API ID',
                                    },
                                    'default_address': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'A customer address',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Address ID'},
                                                    'customer_id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Customer ID',
                                                    },
                                                    'first_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'First name',
                                                    },
                                                    'last_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Last name',
                                                    },
                                                    'company': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Company name',
                                                    },
                                                    'address1': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Address line 1',
                                                    },
                                                    'address2': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Address line 2',
                                                    },
                                                    'city': {
                                                        'type': ['string', 'null'],
                                                        'description': 'City',
                                                    },
                                                    'province': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Province/State',
                                                    },
                                                    'country': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Country',
                                                    },
                                                    'zip': {
                                                        'type': ['string', 'null'],
                                                        'description': 'ZIP/Postal code',
                                                    },
                                                    'phone': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Phone number',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Full name',
                                                    },
                                                    'province_code': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Province code',
                                                    },
                                                    'country_code': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Country code',
                                                    },
                                                    'country_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Country name',
                                                    },
                                                    'default': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether this is the default address',
                                                    },
                                                },
                                                'required': ['id'],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'customers',
                                'x-airbyte-stream-name': 'customers',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Shopify customers with order history and contact information',
                                    'when_to_use': 'Looking up customer details or purchase history',
                                    'trigger_phrases': ['shopify customer', 'buyer', 'customer info'],
                                    'freshness': 'live',
                                    'example_questions': ['Find a customer in Shopify', 'Show customer order history'],
                                    'search_strategy': 'Search by email, name, or phone',
                                },
                            },
                        },
                    },
                    record_extractor='$.customer',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Shopify customer',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique customer identifier'},
                    'email': {
                        'type': ['string', 'null'],
                        'description': 'Customer email address',
                    },
                    'accepts_marketing': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the customer accepts marketing',
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the customer was created',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the customer was last updated',
                    },
                    'first_name': {
                        'type': ['string', 'null'],
                        'description': 'Customer first name',
                    },
                    'last_name': {
                        'type': ['string', 'null'],
                        'description': 'Customer last name',
                    },
                    'orders_count': {
                        'type': ['integer', 'null'],
                        'description': 'Number of orders',
                    },
                    'state': {
                        'type': ['string', 'null'],
                        'description': 'Customer state',
                    },
                    'total_spent': {
                        'type': ['string', 'null'],
                        'description': 'Total amount spent',
                    },
                    'last_order_id': {
                        'type': ['integer', 'null'],
                        'description': 'ID of last order',
                    },
                    'note': {
                        'type': ['string', 'null'],
                        'description': 'Note about the customer',
                    },
                    'verified_email': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether email is verified',
                    },
                    'multipass_identifier': {
                        'type': ['string', 'null'],
                        'description': 'Multipass identifier',
                    },
                    'tax_exempt': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether customer is tax exempt',
                    },
                    'tags': {
                        'type': ['string', 'null'],
                        'description': 'Tags associated with customer',
                    },
                    'last_order_name': {
                        'type': ['string', 'null'],
                        'description': 'Name of last order',
                    },
                    'currency': {
                        'type': ['string', 'null'],
                        'description': 'Customer currency',
                    },
                    'phone': {
                        'type': ['string', 'null'],
                        'description': 'Customer phone number',
                    },
                    'addresses': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/CustomerAddress'},
                    },
                    'accepts_marketing_updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When marketing acceptance was updated',
                    },
                    'marketing_opt_in_level': {
                        'type': ['string', 'null'],
                        'description': 'Marketing opt-in level',
                    },
                    'tax_exemptions': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                    },
                    'email_marketing_consent': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MarketingConsent'},
                            {'type': 'null'},
                        ],
                    },
                    'sms_marketing_consent': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MarketingConsent'},
                            {'type': 'null'},
                        ],
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                        'description': 'GraphQL API ID',
                    },
                    'default_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CustomerAddress'},
                            {'type': 'null'},
                        ],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'customers',
                'x-airbyte-stream-name': 'customers',
                'x-airbyte-ai-hints': {
                    'summary': 'Shopify customers with order history and contact information',
                    'when_to_use': 'Looking up customer details or purchase history',
                    'trigger_phrases': ['shopify customer', 'buyer', 'customer info'],
                    'freshness': 'live',
                    'example_questions': ['Find a customer in Shopify', 'Show customer order history'],
                    'search_strategy': 'Search by email, name, or phone',
                },
            },
            ai_hints={
                'summary': 'Shopify customers with order history and contact information',
                'when_to_use': 'Looking up customer details or purchase history',
                'trigger_phrases': ['shopify customer', 'buyer', 'customer info'],
                'freshness': 'live',
                'example_questions': ['Find a customer in Shopify', 'Show customer order history'],
                'search_strategy': 'Search by email, name, or phone',
            },
        ),
        EntityDefinition(
            name='orders',
            stream_name='orders',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/orders.json',
                    action=Action.LIST,
                    description='Returns a list of orders from the store',
                    query_params=[
                        'limit',
                        'since_id',
                        'created_at_min',
                        'created_at_max',
                        'updated_at_min',
                        'updated_at_max',
                        'status',
                        'financial_status',
                        'fulfillment_status',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'created_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'status': {
                            'type': 'string',
                            'required': False,
                            'default': 'any',
                            'enum': [
                                'open',
                                'closed',
                                'cancelled',
                                'any',
                            ],
                        },
                        'financial_status': {
                            'type': 'string',
                            'required': False,
                            'enum': [
                                'authorized',
                                'pending',
                                'paid',
                                'partially_paid',
                                'refunded',
                                'voided',
                                'partially_refunded',
                                'any',
                                'unpaid',
                            ],
                        },
                        'fulfillment_status': {
                            'type': 'string',
                            'required': False,
                            'enum': [
                                'shipped',
                                'partial',
                                'unshipped',
                                'any',
                                'unfulfilled',
                            ],
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'orders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Shopify order',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique order identifier'},
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'app_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'browser_ip': {
                                            'type': ['string', 'null'],
                                        },
                                        'buyer_accepts_marketing': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'cancel_reason': {
                                            'type': ['string', 'null'],
                                        },
                                        'cancelled_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'cart_token': {
                                            'type': ['string', 'null'],
                                        },
                                        'checkout_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'checkout_token': {
                                            'type': ['string', 'null'],
                                        },
                                        'client_details': {
                                            'type': ['object', 'null'],
                                        },
                                        'closed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'company': {
                                            'type': ['object', 'null'],
                                        },
                                        'confirmation_number': {
                                            'type': ['string', 'null'],
                                        },
                                        'confirmed': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'contact_email': {
                                            'type': ['string', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'currency': {
                                            'type': ['string', 'null'],
                                        },
                                        'current_subtotal_price': {
                                            'type': ['string', 'null'],
                                        },
                                        'current_subtotal_price_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'current_total_additional_fees_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'current_total_discounts': {
                                            'type': ['string', 'null'],
                                        },
                                        'current_total_discounts_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'current_total_duties_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'current_total_price': {
                                            'type': ['string', 'null'],
                                        },
                                        'current_total_price_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'current_total_tax': {
                                            'type': ['string', 'null'],
                                        },
                                        'current_total_tax_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'customer': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'A Shopify customer',
                                                    'properties': {
                                                        'id': {'type': 'integer', 'description': 'Unique customer identifier'},
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer email address',
                                                        },
                                                        'accepts_marketing': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the customer accepts marketing',
                                                        },
                                                        'created_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When the customer was created',
                                                        },
                                                        'updated_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When the customer was last updated',
                                                        },
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer first name',
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer last name',
                                                        },
                                                        'orders_count': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Number of orders',
                                                        },
                                                        'state': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer state',
                                                        },
                                                        'total_spent': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Total amount spent',
                                                        },
                                                        'last_order_id': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'ID of last order',
                                                        },
                                                        'note': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Note about the customer',
                                                        },
                                                        'verified_email': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether email is verified',
                                                        },
                                                        'multipass_identifier': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Multipass identifier',
                                                        },
                                                        'tax_exempt': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether customer is tax exempt',
                                                        },
                                                        'tags': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Tags associated with customer',
                                                        },
                                                        'last_order_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Name of last order',
                                                        },
                                                        'currency': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer currency',
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer phone number',
                                                        },
                                                        'addresses': {
                                                            'type': ['array', 'null'],
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'A customer address',
                                                                'properties': {
                                                                    'id': {'type': 'integer', 'description': 'Address ID'},
                                                                    'customer_id': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Customer ID',
                                                                    },
                                                                    'first_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'First name',
                                                                    },
                                                                    'last_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Last name',
                                                                    },
                                                                    'company': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Company name',
                                                                    },
                                                                    'address1': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Address line 1',
                                                                    },
                                                                    'address2': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Address line 2',
                                                                    },
                                                                    'city': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'City',
                                                                    },
                                                                    'province': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Province/State',
                                                                    },
                                                                    'country': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country',
                                                                    },
                                                                    'zip': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'ZIP/Postal code',
                                                                    },
                                                                    'phone': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Phone number',
                                                                    },
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Full name',
                                                                    },
                                                                    'province_code': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Province code',
                                                                    },
                                                                    'country_code': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country code',
                                                                    },
                                                                    'country_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country name',
                                                                    },
                                                                    'default': {
                                                                        'type': ['boolean', 'null'],
                                                                        'description': 'Whether this is the default address',
                                                                    },
                                                                },
                                                                'required': ['id'],
                                                            },
                                                        },
                                                        'accepts_marketing_updated_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When marketing acceptance was updated',
                                                        },
                                                        'marketing_opt_in_level': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Marketing opt-in level',
                                                        },
                                                        'tax_exemptions': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'string'},
                                                        },
                                                        'email_marketing_consent': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'state': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'opt_in_level': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'consent_updated_at': {
                                                                            'type': ['string', 'null'],
                                                                            'format': 'date-time',
                                                                        },
                                                                        'consent_collected_from': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'sms_marketing_consent': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'state': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'opt_in_level': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'consent_updated_at': {
                                                                            'type': ['string', 'null'],
                                                                            'format': 'date-time',
                                                                        },
                                                                        'consent_collected_from': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'admin_graphql_api_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'GraphQL API ID',
                                                        },
                                                        'default_address': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'A customer address',
                                                                    'properties': {
                                                                        'id': {'type': 'integer', 'description': 'Address ID'},
                                                                        'customer_id': {
                                                                            'type': ['integer', 'null'],
                                                                            'description': 'Customer ID',
                                                                        },
                                                                        'first_name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'First name',
                                                                        },
                                                                        'last_name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Last name',
                                                                        },
                                                                        'company': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Company name',
                                                                        },
                                                                        'address1': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Address line 1',
                                                                        },
                                                                        'address2': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Address line 2',
                                                                        },
                                                                        'city': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'City',
                                                                        },
                                                                        'province': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Province/State',
                                                                        },
                                                                        'country': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Country',
                                                                        },
                                                                        'zip': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'ZIP/Postal code',
                                                                        },
                                                                        'phone': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Phone number',
                                                                        },
                                                                        'name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Full name',
                                                                        },
                                                                        'province_code': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Province code',
                                                                        },
                                                                        'country_code': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Country code',
                                                                        },
                                                                        'country_name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Country name',
                                                                        },
                                                                        'default': {
                                                                            'type': ['boolean', 'null'],
                                                                            'description': 'Whether this is the default address',
                                                                        },
                                                                    },
                                                                    'required': ['id'],
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                    },
                                                    'required': ['id'],
                                                    'x-airbyte-entity-name': 'customers',
                                                    'x-airbyte-stream-name': 'customers',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Shopify customers with order history and contact information',
                                                        'when_to_use': 'Looking up customer details or purchase history',
                                                        'trigger_phrases': ['shopify customer', 'buyer', 'customer info'],
                                                        'freshness': 'live',
                                                        'example_questions': ['Find a customer in Shopify', 'Show customer order history'],
                                                        'search_strategy': 'Search by email, name, or phone',
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'customer_locale': {
                                            'type': ['string', 'null'],
                                        },
                                        'device_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'discount_applications': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'discount_codes': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                        },
                                        'estimated_taxes': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'financial_status': {
                                            'type': ['string', 'null'],
                                        },
                                        'fulfillment_status': {
                                            'type': ['string', 'null'],
                                        },
                                        'fulfillments': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'A fulfillment',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Fulfillment ID'},
                                                    'order_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'status': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'created_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'service': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'updated_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'tracking_company': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'shipment_status': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'location_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'origin_address': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'line_items': {
                                                        'type': ['array', 'null'],
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'id': {'type': 'integer'},
                                                                'admin_graphql_api_id': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'attributed_staffs': {
                                                                    'type': ['array', 'null'],
                                                                    'items': {'type': 'object'},
                                                                },
                                                                'current_quantity': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'fulfillable_quantity': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'fulfillment_service': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'fulfillment_status': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'gift_card': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'grams': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'name': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'price': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'price_set': {
                                                                    'type': ['object', 'null'],
                                                                },
                                                                'product_exists': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'product_id': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'properties': {
                                                                    'type': ['array', 'null'],
                                                                    'items': {'type': 'object'},
                                                                },
                                                                'quantity': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'requires_shipping': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'sku': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'taxable': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'title': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'total_discount': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'total_discount_set': {
                                                                    'type': ['object', 'null'],
                                                                },
                                                                'variant_id': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'variant_inventory_management': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'variant_title': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'vendor': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'tax_lines': {
                                                                    'type': ['array', 'null'],
                                                                    'items': {'type': 'object'},
                                                                },
                                                                'duties': {
                                                                    'type': ['array', 'null'],
                                                                    'items': {'type': 'object'},
                                                                },
                                                                'discount_allocations': {
                                                                    'type': ['array', 'null'],
                                                                    'items': {'type': 'object'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                    'tracking_number': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'tracking_numbers': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'string'},
                                                    },
                                                    'tracking_url': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'tracking_urls': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'string'},
                                                    },
                                                    'receipt': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                                'required': ['id'],
                                                'x-airbyte-entity-name': 'fulfillments',
                                                'x-airbyte-stream-name': 'fulfillments',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Order fulfillments with tracking and shipping details',
                                                    'when_to_use': 'Questions about shipping status or fulfillment tracking',
                                                    'trigger_phrases': ['fulfillment', 'shipping status', 'tracking number'],
                                                    'freshness': 'live',
                                                    'example_questions': ['What is the shipping status of an order?'],
                                                    'search_strategy': 'Filter by order',
                                                },
                                            },
                                        },
                                        'gateway': {
                                            'type': ['string', 'null'],
                                        },
                                        'landing_site': {
                                            'type': ['string', 'null'],
                                        },
                                        'landing_site_ref': {
                                            'type': ['string', 'null'],
                                        },
                                        'line_items': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'integer'},
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'attributed_staffs': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'current_quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'fulfillable_quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'fulfillment_service': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'fulfillment_status': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'gift_card': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'grams': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'price': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'price_set': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'product_exists': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'product_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'properties': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'requires_shipping': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'sku': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'taxable': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'total_discount': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'total_discount_set': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'variant_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'variant_inventory_management': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'variant_title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'vendor': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'tax_lines': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'duties': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'discount_allocations': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                },
                                            },
                                        },
                                        'location_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'merchant_of_record_app_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'merchant_business_entity_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'duties_included': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'total_cash_rounding_payment_adjustment_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'total_cash_rounding_refund_adjustment_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'payment_terms': {
                                            'type': ['object', 'null'],
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'note': {
                                            'type': ['string', 'null'],
                                        },
                                        'note_attributes': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'number': {
                                            'type': ['integer', 'null'],
                                        },
                                        'order_number': {
                                            'type': ['integer', 'null'],
                                        },
                                        'order_status_url': {
                                            'type': ['string', 'null'],
                                        },
                                        'original_total_additional_fees_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'original_total_duties_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'payment_gateway_names': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                        },
                                        'phone': {
                                            'type': ['string', 'null'],
                                        },
                                        'po_number': {
                                            'type': ['string', 'null'],
                                        },
                                        'presentment_currency': {
                                            'type': ['string', 'null'],
                                        },
                                        'processed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'reference': {
                                            'type': ['string', 'null'],
                                        },
                                        'referring_site': {
                                            'type': ['string', 'null'],
                                        },
                                        'refunds': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'An order refund',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Refund ID'},
                                                    'order_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'created_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'note': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'user_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'processed_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'restock': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'duties': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'total_duties_set': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'return': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'refund_line_items': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'transactions': {
                                                        'type': ['array', 'null'],
                                                        'items': {
                                                            'type': 'object',
                                                            'description': 'An order transaction',
                                                            'properties': {
                                                                'id': {'type': 'integer', 'description': 'Transaction ID'},
                                                                'order_id': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'kind': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'gateway': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'status': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'message': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'created_at': {
                                                                    'type': ['string', 'null'],
                                                                    'format': 'date-time',
                                                                },
                                                                'test': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'authorization': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'location_id': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'user_id': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'parent_id': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'processed_at': {
                                                                    'type': ['string', 'null'],
                                                                    'format': 'date-time',
                                                                },
                                                                'device_id': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'error_code': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'source_name': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'receipt': {
                                                                    'type': ['object', 'null'],
                                                                },
                                                                'currency_exchange_adjustment': {
                                                                    'type': ['object', 'null'],
                                                                },
                                                                'amount': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'currency': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'payment_id': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'total_unsettled_set': {
                                                                    'type': ['object', 'null'],
                                                                },
                                                                'manual_payment_gateway': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'admin_graphql_api_id': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                            },
                                                            'required': ['id'],
                                                            'x-airbyte-entity-name': 'transactions',
                                                            'x-airbyte-stream-name': 'transactions',
                                                            'x-airbyte-ai-hints': {
                                                                'summary': 'Payment transactions on Shopify orders',
                                                                'when_to_use': 'Questions about payment processing or transaction details',
                                                                'trigger_phrases': ['shopify transaction', 'payment', 'charge'],
                                                                'freshness': 'live',
                                                                'example_questions': ['Show transactions for an order'],
                                                                'search_strategy': 'Filter by order',
                                                            },
                                                        },
                                                    },
                                                    'order_adjustments': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'refund_shipping_lines': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                },
                                                'required': ['id'],
                                                'x-airbyte-entity-name': 'order_refunds',
                                                'x-airbyte-stream-name': 'order_refunds',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Refunds processed for Shopify orders',
                                                    'when_to_use': 'Questions about refunds or return processing',
                                                    'trigger_phrases': ['refund', 'order refund', 'return'],
                                                    'freshness': 'live',
                                                    'example_questions': ['What refunds were processed for an order?'],
                                                    'search_strategy': 'Filter by order',
                                                },
                                            },
                                        },
                                        'shipping_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'An address in an order (shipping or billing) - does not have id field',
                                                    'properties': {
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'company': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address1': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address2': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'zip': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province_code': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country_code': {
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
                                                {'type': 'null'},
                                            ],
                                        },
                                        'shipping_lines': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'source_identifier': {
                                            'type': ['string', 'null'],
                                        },
                                        'source_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'source_url': {
                                            'type': ['string', 'null'],
                                        },
                                        'subtotal_price': {
                                            'type': ['string', 'null'],
                                        },
                                        'subtotal_price_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'tags': {
                                            'type': ['string', 'null'],
                                        },
                                        'tax_exempt': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'tax_lines': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'taxes_included': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'test': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'token': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_discounts': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_discounts_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'total_line_items_price': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_line_items_price_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'total_outstanding': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_price': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_price_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'total_shipping_price_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'total_tax': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_tax_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'total_tip_received': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_weight': {
                                            'type': ['integer', 'null'],
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'user_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'billing_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'An address in an order (shipping or billing) - does not have id field',
                                                    'properties': {
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'company': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address1': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address2': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'zip': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province_code': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country_code': {
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
                                                {'type': 'null'},
                                            ],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'orders',
                                    'x-airbyte-stream-name': 'orders',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Shopify orders with line items, payment, and fulfillment status',
                                        'when_to_use': 'Questions about orders, order status, or fulfillment',
                                        'trigger_phrases': [
                                            'shopify order',
                                            'order status',
                                            'fulfillment',
                                            'purchase',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Show recent Shopify orders', 'What is the status of an order?'],
                                        'search_strategy': 'Search by order number or filter by status, date, or customer',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.orders',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}.json',
                    action=Action.GET,
                    description='Retrieves a single order by ID',
                    path_params=['order_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'order': {
                                'type': 'object',
                                'description': 'A Shopify order',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Unique order identifier'},
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'app_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'browser_ip': {
                                        'type': ['string', 'null'],
                                    },
                                    'buyer_accepts_marketing': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'cancel_reason': {
                                        'type': ['string', 'null'],
                                    },
                                    'cancelled_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'cart_token': {
                                        'type': ['string', 'null'],
                                    },
                                    'checkout_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'checkout_token': {
                                        'type': ['string', 'null'],
                                    },
                                    'client_details': {
                                        'type': ['object', 'null'],
                                    },
                                    'closed_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'company': {
                                        'type': ['object', 'null'],
                                    },
                                    'confirmation_number': {
                                        'type': ['string', 'null'],
                                    },
                                    'confirmed': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'contact_email': {
                                        'type': ['string', 'null'],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'currency': {
                                        'type': ['string', 'null'],
                                    },
                                    'current_subtotal_price': {
                                        'type': ['string', 'null'],
                                    },
                                    'current_subtotal_price_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'current_total_additional_fees_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'current_total_discounts': {
                                        'type': ['string', 'null'],
                                    },
                                    'current_total_discounts_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'current_total_duties_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'current_total_price': {
                                        'type': ['string', 'null'],
                                    },
                                    'current_total_price_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'current_total_tax': {
                                        'type': ['string', 'null'],
                                    },
                                    'current_total_tax_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'customer': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'A Shopify customer',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Unique customer identifier'},
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer email address',
                                                    },
                                                    'accepts_marketing': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the customer accepts marketing',
                                                    },
                                                    'created_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When the customer was created',
                                                    },
                                                    'updated_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When the customer was last updated',
                                                    },
                                                    'first_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer first name',
                                                    },
                                                    'last_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer last name',
                                                    },
                                                    'orders_count': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Number of orders',
                                                    },
                                                    'state': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer state',
                                                    },
                                                    'total_spent': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Total amount spent',
                                                    },
                                                    'last_order_id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'ID of last order',
                                                    },
                                                    'note': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Note about the customer',
                                                    },
                                                    'verified_email': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether email is verified',
                                                    },
                                                    'multipass_identifier': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Multipass identifier',
                                                    },
                                                    'tax_exempt': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether customer is tax exempt',
                                                    },
                                                    'tags': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Tags associated with customer',
                                                    },
                                                    'last_order_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Name of last order',
                                                    },
                                                    'currency': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer currency',
                                                    },
                                                    'phone': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer phone number',
                                                    },
                                                    'addresses': {
                                                        'type': ['array', 'null'],
                                                        'items': {
                                                            'type': 'object',
                                                            'description': 'A customer address',
                                                            'properties': {
                                                                'id': {'type': 'integer', 'description': 'Address ID'},
                                                                'customer_id': {
                                                                    'type': ['integer', 'null'],
                                                                    'description': 'Customer ID',
                                                                },
                                                                'first_name': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'First name',
                                                                },
                                                                'last_name': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Last name',
                                                                },
                                                                'company': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Company name',
                                                                },
                                                                'address1': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Address line 1',
                                                                },
                                                                'address2': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Address line 2',
                                                                },
                                                                'city': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'City',
                                                                },
                                                                'province': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Province/State',
                                                                },
                                                                'country': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Country',
                                                                },
                                                                'zip': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'ZIP/Postal code',
                                                                },
                                                                'phone': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Phone number',
                                                                },
                                                                'name': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Full name',
                                                                },
                                                                'province_code': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Province code',
                                                                },
                                                                'country_code': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Country code',
                                                                },
                                                                'country_name': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Country name',
                                                                },
                                                                'default': {
                                                                    'type': ['boolean', 'null'],
                                                                    'description': 'Whether this is the default address',
                                                                },
                                                            },
                                                            'required': ['id'],
                                                        },
                                                    },
                                                    'accepts_marketing_updated_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When marketing acceptance was updated',
                                                    },
                                                    'marketing_opt_in_level': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Marketing opt-in level',
                                                    },
                                                    'tax_exemptions': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'string'},
                                                    },
                                                    'email_marketing_consent': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'state': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'opt_in_level': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'consent_updated_at': {
                                                                        'type': ['string', 'null'],
                                                                        'format': 'date-time',
                                                                    },
                                                                    'consent_collected_from': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                    'sms_marketing_consent': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'state': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'opt_in_level': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'consent_updated_at': {
                                                                        'type': ['string', 'null'],
                                                                        'format': 'date-time',
                                                                    },
                                                                    'consent_collected_from': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'GraphQL API ID',
                                                    },
                                                    'default_address': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'description': 'A customer address',
                                                                'properties': {
                                                                    'id': {'type': 'integer', 'description': 'Address ID'},
                                                                    'customer_id': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Customer ID',
                                                                    },
                                                                    'first_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'First name',
                                                                    },
                                                                    'last_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Last name',
                                                                    },
                                                                    'company': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Company name',
                                                                    },
                                                                    'address1': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Address line 1',
                                                                    },
                                                                    'address2': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Address line 2',
                                                                    },
                                                                    'city': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'City',
                                                                    },
                                                                    'province': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Province/State',
                                                                    },
                                                                    'country': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country',
                                                                    },
                                                                    'zip': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'ZIP/Postal code',
                                                                    },
                                                                    'phone': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Phone number',
                                                                    },
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Full name',
                                                                    },
                                                                    'province_code': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Province code',
                                                                    },
                                                                    'country_code': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country code',
                                                                    },
                                                                    'country_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country name',
                                                                    },
                                                                    'default': {
                                                                        'type': ['boolean', 'null'],
                                                                        'description': 'Whether this is the default address',
                                                                    },
                                                                },
                                                                'required': ['id'],
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                },
                                                'required': ['id'],
                                                'x-airbyte-entity-name': 'customers',
                                                'x-airbyte-stream-name': 'customers',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Shopify customers with order history and contact information',
                                                    'when_to_use': 'Looking up customer details or purchase history',
                                                    'trigger_phrases': ['shopify customer', 'buyer', 'customer info'],
                                                    'freshness': 'live',
                                                    'example_questions': ['Find a customer in Shopify', 'Show customer order history'],
                                                    'search_strategy': 'Search by email, name, or phone',
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'customer_locale': {
                                        'type': ['string', 'null'],
                                    },
                                    'device_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'discount_applications': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'discount_codes': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                    },
                                    'estimated_taxes': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'financial_status': {
                                        'type': ['string', 'null'],
                                    },
                                    'fulfillment_status': {
                                        'type': ['string', 'null'],
                                    },
                                    'fulfillments': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A fulfillment',
                                            'properties': {
                                                'id': {'type': 'integer', 'description': 'Fulfillment ID'},
                                                'order_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'status': {
                                                    'type': ['string', 'null'],
                                                },
                                                'created_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                },
                                                'service': {
                                                    'type': ['string', 'null'],
                                                },
                                                'updated_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                },
                                                'tracking_company': {
                                                    'type': ['string', 'null'],
                                                },
                                                'shipment_status': {
                                                    'type': ['string', 'null'],
                                                },
                                                'location_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'origin_address': {
                                                    'type': ['object', 'null'],
                                                },
                                                'line_items': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'id': {'type': 'integer'},
                                                            'admin_graphql_api_id': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'attributed_staffs': {
                                                                'type': ['array', 'null'],
                                                                'items': {'type': 'object'},
                                                            },
                                                            'current_quantity': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'fulfillable_quantity': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'fulfillment_service': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'fulfillment_status': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'gift_card': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'grams': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'name': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'price': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'price_set': {
                                                                'type': ['object', 'null'],
                                                            },
                                                            'product_exists': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'product_id': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'properties': {
                                                                'type': ['array', 'null'],
                                                                'items': {'type': 'object'},
                                                            },
                                                            'quantity': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'requires_shipping': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'sku': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'taxable': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'title': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'total_discount': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'total_discount_set': {
                                                                'type': ['object', 'null'],
                                                            },
                                                            'variant_id': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'variant_inventory_management': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'variant_title': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'vendor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'tax_lines': {
                                                                'type': ['array', 'null'],
                                                                'items': {'type': 'object'},
                                                            },
                                                            'duties': {
                                                                'type': ['array', 'null'],
                                                                'items': {'type': 'object'},
                                                            },
                                                            'discount_allocations': {
                                                                'type': ['array', 'null'],
                                                                'items': {'type': 'object'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'tracking_number': {
                                                    'type': ['string', 'null'],
                                                },
                                                'tracking_numbers': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'string'},
                                                },
                                                'tracking_url': {
                                                    'type': ['string', 'null'],
                                                },
                                                'tracking_urls': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'string'},
                                                },
                                                'receipt': {
                                                    'type': ['object', 'null'],
                                                },
                                                'name': {
                                                    'type': ['string', 'null'],
                                                },
                                                'admin_graphql_api_id': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'required': ['id'],
                                            'x-airbyte-entity-name': 'fulfillments',
                                            'x-airbyte-stream-name': 'fulfillments',
                                            'x-airbyte-ai-hints': {
                                                'summary': 'Order fulfillments with tracking and shipping details',
                                                'when_to_use': 'Questions about shipping status or fulfillment tracking',
                                                'trigger_phrases': ['fulfillment', 'shipping status', 'tracking number'],
                                                'freshness': 'live',
                                                'example_questions': ['What is the shipping status of an order?'],
                                                'search_strategy': 'Filter by order',
                                            },
                                        },
                                    },
                                    'gateway': {
                                        'type': ['string', 'null'],
                                    },
                                    'landing_site': {
                                        'type': ['string', 'null'],
                                    },
                                    'landing_site_ref': {
                                        'type': ['string', 'null'],
                                    },
                                    'line_items': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'integer'},
                                                'admin_graphql_api_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'attributed_staffs': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'current_quantity': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'fulfillable_quantity': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'fulfillment_service': {
                                                    'type': ['string', 'null'],
                                                },
                                                'fulfillment_status': {
                                                    'type': ['string', 'null'],
                                                },
                                                'gift_card': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'grams': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'name': {
                                                    'type': ['string', 'null'],
                                                },
                                                'price': {
                                                    'type': ['string', 'null'],
                                                },
                                                'price_set': {
                                                    'type': ['object', 'null'],
                                                },
                                                'product_exists': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'product_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'properties': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'quantity': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'requires_shipping': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'sku': {
                                                    'type': ['string', 'null'],
                                                },
                                                'taxable': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'title': {
                                                    'type': ['string', 'null'],
                                                },
                                                'total_discount': {
                                                    'type': ['string', 'null'],
                                                },
                                                'total_discount_set': {
                                                    'type': ['object', 'null'],
                                                },
                                                'variant_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'variant_inventory_management': {
                                                    'type': ['string', 'null'],
                                                },
                                                'variant_title': {
                                                    'type': ['string', 'null'],
                                                },
                                                'vendor': {
                                                    'type': ['string', 'null'],
                                                },
                                                'tax_lines': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'duties': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'discount_allocations': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                            },
                                        },
                                    },
                                    'location_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'merchant_of_record_app_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'merchant_business_entity_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'duties_included': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'total_cash_rounding_payment_adjustment_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'total_cash_rounding_refund_adjustment_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'payment_terms': {
                                        'type': ['object', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'note': {
                                        'type': ['string', 'null'],
                                    },
                                    'note_attributes': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'number': {
                                        'type': ['integer', 'null'],
                                    },
                                    'order_number': {
                                        'type': ['integer', 'null'],
                                    },
                                    'order_status_url': {
                                        'type': ['string', 'null'],
                                    },
                                    'original_total_additional_fees_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'original_total_duties_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'payment_gateway_names': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                    },
                                    'phone': {
                                        'type': ['string', 'null'],
                                    },
                                    'po_number': {
                                        'type': ['string', 'null'],
                                    },
                                    'presentment_currency': {
                                        'type': ['string', 'null'],
                                    },
                                    'processed_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'reference': {
                                        'type': ['string', 'null'],
                                    },
                                    'referring_site': {
                                        'type': ['string', 'null'],
                                    },
                                    'refunds': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'An order refund',
                                            'properties': {
                                                'id': {'type': 'integer', 'description': 'Refund ID'},
                                                'order_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'created_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                },
                                                'note': {
                                                    'type': ['string', 'null'],
                                                },
                                                'user_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'processed_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                },
                                                'restock': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'duties': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'total_duties_set': {
                                                    'type': ['object', 'null'],
                                                },
                                                'return': {
                                                    'type': ['object', 'null'],
                                                },
                                                'refund_line_items': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'transactions': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'An order transaction',
                                                        'properties': {
                                                            'id': {'type': 'integer', 'description': 'Transaction ID'},
                                                            'order_id': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'kind': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'gateway': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'status': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'message': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'created_at': {
                                                                'type': ['string', 'null'],
                                                                'format': 'date-time',
                                                            },
                                                            'test': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'authorization': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'location_id': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'user_id': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'parent_id': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'processed_at': {
                                                                'type': ['string', 'null'],
                                                                'format': 'date-time',
                                                            },
                                                            'device_id': {
                                                                'type': ['integer', 'null'],
                                                            },
                                                            'error_code': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'source_name': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'receipt': {
                                                                'type': ['object', 'null'],
                                                            },
                                                            'currency_exchange_adjustment': {
                                                                'type': ['object', 'null'],
                                                            },
                                                            'amount': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'currency': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'payment_id': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'total_unsettled_set': {
                                                                'type': ['object', 'null'],
                                                            },
                                                            'manual_payment_gateway': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'admin_graphql_api_id': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                        'required': ['id'],
                                                        'x-airbyte-entity-name': 'transactions',
                                                        'x-airbyte-stream-name': 'transactions',
                                                        'x-airbyte-ai-hints': {
                                                            'summary': 'Payment transactions on Shopify orders',
                                                            'when_to_use': 'Questions about payment processing or transaction details',
                                                            'trigger_phrases': ['shopify transaction', 'payment', 'charge'],
                                                            'freshness': 'live',
                                                            'example_questions': ['Show transactions for an order'],
                                                            'search_strategy': 'Filter by order',
                                                        },
                                                    },
                                                },
                                                'order_adjustments': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'admin_graphql_api_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'refund_shipping_lines': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                            },
                                            'required': ['id'],
                                            'x-airbyte-entity-name': 'order_refunds',
                                            'x-airbyte-stream-name': 'order_refunds',
                                            'x-airbyte-ai-hints': {
                                                'summary': 'Refunds processed for Shopify orders',
                                                'when_to_use': 'Questions about refunds or return processing',
                                                'trigger_phrases': ['refund', 'order refund', 'return'],
                                                'freshness': 'live',
                                                'example_questions': ['What refunds were processed for an order?'],
                                                'search_strategy': 'Filter by order',
                                            },
                                        },
                                    },
                                    'shipping_address': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'An address in an order (shipping or billing) - does not have id field',
                                                'properties': {
                                                    'first_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'last_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'company': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'address1': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'address2': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'city': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'province': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'country': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'zip': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'phone': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'province_code': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'country_code': {
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
                                            {'type': 'null'},
                                        ],
                                    },
                                    'shipping_lines': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'source_identifier': {
                                        'type': ['string', 'null'],
                                    },
                                    'source_name': {
                                        'type': ['string', 'null'],
                                    },
                                    'source_url': {
                                        'type': ['string', 'null'],
                                    },
                                    'subtotal_price': {
                                        'type': ['string', 'null'],
                                    },
                                    'subtotal_price_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'tags': {
                                        'type': ['string', 'null'],
                                    },
                                    'tax_exempt': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'tax_lines': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'taxes_included': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'test': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'token': {
                                        'type': ['string', 'null'],
                                    },
                                    'total_discounts': {
                                        'type': ['string', 'null'],
                                    },
                                    'total_discounts_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'total_line_items_price': {
                                        'type': ['string', 'null'],
                                    },
                                    'total_line_items_price_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'total_outstanding': {
                                        'type': ['string', 'null'],
                                    },
                                    'total_price': {
                                        'type': ['string', 'null'],
                                    },
                                    'total_price_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'total_shipping_price_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'total_tax': {
                                        'type': ['string', 'null'],
                                    },
                                    'total_tax_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'total_tip_received': {
                                        'type': ['string', 'null'],
                                    },
                                    'total_weight': {
                                        'type': ['integer', 'null'],
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'user_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'billing_address': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'An address in an order (shipping or billing) - does not have id field',
                                                'properties': {
                                                    'first_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'last_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'company': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'address1': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'address2': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'city': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'province': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'country': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'zip': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'phone': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'province_code': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'country_code': {
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
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'orders',
                                'x-airbyte-stream-name': 'orders',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Shopify orders with line items, payment, and fulfillment status',
                                    'when_to_use': 'Questions about orders, order status, or fulfillment',
                                    'trigger_phrases': [
                                        'shopify order',
                                        'order status',
                                        'fulfillment',
                                        'purchase',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Show recent Shopify orders', 'What is the status of an order?'],
                                    'search_strategy': 'Search by order number or filter by status, date, or customer',
                                },
                            },
                        },
                    },
                    record_extractor='$.order',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Shopify order',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique order identifier'},
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                    'app_id': {
                        'type': ['integer', 'null'],
                    },
                    'browser_ip': {
                        'type': ['string', 'null'],
                    },
                    'buyer_accepts_marketing': {
                        'type': ['boolean', 'null'],
                    },
                    'cancel_reason': {
                        'type': ['string', 'null'],
                    },
                    'cancelled_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'cart_token': {
                        'type': ['string', 'null'],
                    },
                    'checkout_id': {
                        'type': ['integer', 'null'],
                    },
                    'checkout_token': {
                        'type': ['string', 'null'],
                    },
                    'client_details': {
                        'type': ['object', 'null'],
                    },
                    'closed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'company': {
                        'type': ['object', 'null'],
                    },
                    'confirmation_number': {
                        'type': ['string', 'null'],
                    },
                    'confirmed': {
                        'type': ['boolean', 'null'],
                    },
                    'contact_email': {
                        'type': ['string', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'currency': {
                        'type': ['string', 'null'],
                    },
                    'current_subtotal_price': {
                        'type': ['string', 'null'],
                    },
                    'current_subtotal_price_set': {
                        'type': ['object', 'null'],
                    },
                    'current_total_additional_fees_set': {
                        'type': ['object', 'null'],
                    },
                    'current_total_discounts': {
                        'type': ['string', 'null'],
                    },
                    'current_total_discounts_set': {
                        'type': ['object', 'null'],
                    },
                    'current_total_duties_set': {
                        'type': ['object', 'null'],
                    },
                    'current_total_price': {
                        'type': ['string', 'null'],
                    },
                    'current_total_price_set': {
                        'type': ['object', 'null'],
                    },
                    'current_total_tax': {
                        'type': ['string', 'null'],
                    },
                    'current_total_tax_set': {
                        'type': ['object', 'null'],
                    },
                    'customer': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Customer'},
                            {'type': 'null'},
                        ],
                    },
                    'customer_locale': {
                        'type': ['string', 'null'],
                    },
                    'device_id': {
                        'type': ['integer', 'null'],
                    },
                    'discount_applications': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'discount_codes': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'email': {
                        'type': ['string', 'null'],
                    },
                    'estimated_taxes': {
                        'type': ['boolean', 'null'],
                    },
                    'financial_status': {
                        'type': ['string', 'null'],
                    },
                    'fulfillment_status': {
                        'type': ['string', 'null'],
                    },
                    'fulfillments': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/Fulfillment'},
                    },
                    'gateway': {
                        'type': ['string', 'null'],
                    },
                    'landing_site': {
                        'type': ['string', 'null'],
                    },
                    'landing_site_ref': {
                        'type': ['string', 'null'],
                    },
                    'line_items': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/LineItem'},
                    },
                    'location_id': {
                        'type': ['integer', 'null'],
                    },
                    'merchant_of_record_app_id': {
                        'type': ['integer', 'null'],
                    },
                    'merchant_business_entity_id': {
                        'type': ['string', 'null'],
                    },
                    'duties_included': {
                        'type': ['boolean', 'null'],
                    },
                    'total_cash_rounding_payment_adjustment_set': {
                        'type': ['object', 'null'],
                    },
                    'total_cash_rounding_refund_adjustment_set': {
                        'type': ['object', 'null'],
                    },
                    'payment_terms': {
                        'type': ['object', 'null'],
                    },
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'note': {
                        'type': ['string', 'null'],
                    },
                    'note_attributes': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'number': {
                        'type': ['integer', 'null'],
                    },
                    'order_number': {
                        'type': ['integer', 'null'],
                    },
                    'order_status_url': {
                        'type': ['string', 'null'],
                    },
                    'original_total_additional_fees_set': {
                        'type': ['object', 'null'],
                    },
                    'original_total_duties_set': {
                        'type': ['object', 'null'],
                    },
                    'payment_gateway_names': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                    },
                    'phone': {
                        'type': ['string', 'null'],
                    },
                    'po_number': {
                        'type': ['string', 'null'],
                    },
                    'presentment_currency': {
                        'type': ['string', 'null'],
                    },
                    'processed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'reference': {
                        'type': ['string', 'null'],
                    },
                    'referring_site': {
                        'type': ['string', 'null'],
                    },
                    'refunds': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/Refund'},
                    },
                    'shipping_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/OrderAddress'},
                            {'type': 'null'},
                        ],
                    },
                    'shipping_lines': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'source_identifier': {
                        'type': ['string', 'null'],
                    },
                    'source_name': {
                        'type': ['string', 'null'],
                    },
                    'source_url': {
                        'type': ['string', 'null'],
                    },
                    'subtotal_price': {
                        'type': ['string', 'null'],
                    },
                    'subtotal_price_set': {
                        'type': ['object', 'null'],
                    },
                    'tags': {
                        'type': ['string', 'null'],
                    },
                    'tax_exempt': {
                        'type': ['boolean', 'null'],
                    },
                    'tax_lines': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'taxes_included': {
                        'type': ['boolean', 'null'],
                    },
                    'test': {
                        'type': ['boolean', 'null'],
                    },
                    'token': {
                        'type': ['string', 'null'],
                    },
                    'total_discounts': {
                        'type': ['string', 'null'],
                    },
                    'total_discounts_set': {
                        'type': ['object', 'null'],
                    },
                    'total_line_items_price': {
                        'type': ['string', 'null'],
                    },
                    'total_line_items_price_set': {
                        'type': ['object', 'null'],
                    },
                    'total_outstanding': {
                        'type': ['string', 'null'],
                    },
                    'total_price': {
                        'type': ['string', 'null'],
                    },
                    'total_price_set': {
                        'type': ['object', 'null'],
                    },
                    'total_shipping_price_set': {
                        'type': ['object', 'null'],
                    },
                    'total_tax': {
                        'type': ['string', 'null'],
                    },
                    'total_tax_set': {
                        'type': ['object', 'null'],
                    },
                    'total_tip_received': {
                        'type': ['string', 'null'],
                    },
                    'total_weight': {
                        'type': ['integer', 'null'],
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'user_id': {
                        'type': ['integer', 'null'],
                    },
                    'billing_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/OrderAddress'},
                            {'type': 'null'},
                        ],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'orders',
                'x-airbyte-stream-name': 'orders',
                'x-airbyte-ai-hints': {
                    'summary': 'Shopify orders with line items, payment, and fulfillment status',
                    'when_to_use': 'Questions about orders, order status, or fulfillment',
                    'trigger_phrases': [
                        'shopify order',
                        'order status',
                        'fulfillment',
                        'purchase',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show recent Shopify orders', 'What is the status of an order?'],
                    'search_strategy': 'Search by order number or filter by status, date, or customer',
                },
            },
            ai_hints={
                'summary': 'Shopify orders with line items, payment, and fulfillment status',
                'when_to_use': 'Questions about orders, order status, or fulfillment',
                'trigger_phrases': [
                    'shopify order',
                    'order status',
                    'fulfillment',
                    'purchase',
                ],
                'freshness': 'live',
                'example_questions': ['Show recent Shopify orders', 'What is the status of an order?'],
                'search_strategy': 'Search by order number or filter by status, date, or customer',
            },
        ),
        EntityDefinition(
            name='products',
            stream_name='products',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/products.json',
                    action=Action.LIST,
                    description='Returns a list of products from the store',
                    query_params=[
                        'limit',
                        'since_id',
                        'created_at_min',
                        'created_at_max',
                        'updated_at_min',
                        'updated_at_max',
                        'status',
                        'product_type',
                        'vendor',
                        'collection_id',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'created_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'status': {
                            'type': 'string',
                            'required': False,
                            'enum': ['active', 'archived', 'draft'],
                        },
                        'product_type': {'type': 'string', 'required': False},
                        'vendor': {'type': 'string', 'required': False},
                        'collection_id': {'type': 'integer', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'products': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Shopify product',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique product identifier'},
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Product title',
                                        },
                                        'body_html': {
                                            'type': ['string', 'null'],
                                            'description': 'Product description in HTML',
                                        },
                                        'vendor': {
                                            'type': ['string', 'null'],
                                            'description': 'Product vendor',
                                        },
                                        'product_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Product type',
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the product was created',
                                        },
                                        'handle': {
                                            'type': ['string', 'null'],
                                            'description': 'Product handle for URL',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the product was last updated',
                                        },
                                        'published_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the product was published',
                                        },
                                        'template_suffix': {
                                            'type': ['string', 'null'],
                                            'description': 'Template suffix',
                                        },
                                        'published_scope': {
                                            'type': ['string', 'null'],
                                            'description': 'Published scope',
                                        },
                                        'tags': {
                                            'type': ['string', 'null'],
                                            'description': 'Product tags',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'Product status',
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                            'description': 'GraphQL API ID',
                                        },
                                        'variants': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'A product variant',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Variant ID'},
                                                    'product_id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Product ID',
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Variant title',
                                                    },
                                                    'price': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Variant price',
                                                    },
                                                    'sku': {
                                                        'type': ['string', 'null'],
                                                        'description': 'SKU',
                                                    },
                                                    'position': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Position',
                                                    },
                                                    'inventory_policy': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Inventory policy',
                                                    },
                                                    'compare_at_price': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Compare at price',
                                                    },
                                                    'fulfillment_service': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Fulfillment service',
                                                    },
                                                    'inventory_management': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Inventory management',
                                                    },
                                                    'option1': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Option 1 value',
                                                    },
                                                    'option2': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Option 2 value',
                                                    },
                                                    'option3': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Option 3 value',
                                                    },
                                                    'created_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When the variant was created',
                                                    },
                                                    'updated_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When the variant was last updated',
                                                    },
                                                    'taxable': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the variant is taxable',
                                                    },
                                                    'barcode': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Barcode',
                                                    },
                                                    'grams': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Weight in grams',
                                                    },
                                                    'image_id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Image ID',
                                                    },
                                                    'weight': {
                                                        'type': ['number', 'null'],
                                                        'description': 'Weight',
                                                    },
                                                    'weight_unit': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Weight unit',
                                                    },
                                                    'inventory_item_id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Inventory item ID',
                                                    },
                                                    'inventory_quantity': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Inventory quantity',
                                                    },
                                                    'old_inventory_quantity': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Old inventory quantity',
                                                    },
                                                    'requires_shipping': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether shipping is required',
                                                    },
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'GraphQL API ID',
                                                    },
                                                },
                                                'required': ['id'],
                                                'x-airbyte-entity-name': 'product_variants',
                                                'x-airbyte-stream-name': 'product_variants',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Product variants with size, color, SKU, and inventory details',
                                                    'when_to_use': 'Questions about product options, SKUs, or variant-level data',
                                                    'trigger_phrases': [
                                                        'product variant',
                                                        'SKU',
                                                        'size',
                                                        'color option',
                                                    ],
                                                    'freshness': 'live',
                                                    'example_questions': ['What variants does a product have?'],
                                                    'search_strategy': 'Filter by product',
                                                },
                                            },
                                        },
                                        'options': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'images': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'A product image',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Image ID'},
                                                    'product_id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Product ID',
                                                    },
                                                    'position': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Position',
                                                    },
                                                    'created_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When the image was created',
                                                    },
                                                    'updated_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When the image was last updated',
                                                    },
                                                    'alt': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Alt text',
                                                    },
                                                    'width': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Image width',
                                                    },
                                                    'height': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Image height',
                                                    },
                                                    'src': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Image source URL',
                                                    },
                                                    'variant_ids': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'integer'},
                                                    },
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'GraphQL API ID',
                                                    },
                                                },
                                                'required': ['id'],
                                                'x-airbyte-entity-name': 'product_images',
                                                'x-airbyte-stream-name': 'product_images',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Product images attached to Shopify products',
                                                    'when_to_use': 'Looking for product photos or image assets',
                                                    'trigger_phrases': ['product image', 'product photo'],
                                                    'freshness': 'live',
                                                    'example_questions': ['Show images for a product'],
                                                    'search_strategy': 'Filter by product',
                                                },
                                            },
                                        },
                                        'image': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'A product image',
                                                    'properties': {
                                                        'id': {'type': 'integer', 'description': 'Image ID'},
                                                        'product_id': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Product ID',
                                                        },
                                                        'position': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Position',
                                                        },
                                                        'created_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When the image was created',
                                                        },
                                                        'updated_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When the image was last updated',
                                                        },
                                                        'alt': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Alt text',
                                                        },
                                                        'width': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Image width',
                                                        },
                                                        'height': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Image height',
                                                        },
                                                        'src': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Image source URL',
                                                        },
                                                        'variant_ids': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'integer'},
                                                        },
                                                        'admin_graphql_api_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'GraphQL API ID',
                                                        },
                                                    },
                                                    'required': ['id'],
                                                    'x-airbyte-entity-name': 'product_images',
                                                    'x-airbyte-stream-name': 'product_images',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Product images attached to Shopify products',
                                                        'when_to_use': 'Looking for product photos or image assets',
                                                        'trigger_phrases': ['product image', 'product photo'],
                                                        'freshness': 'live',
                                                        'example_questions': ['Show images for a product'],
                                                        'search_strategy': 'Filter by product',
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'products',
                                    'x-airbyte-stream-name': 'products',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Shopify products with title, description, pricing, and inventory',
                                        'when_to_use': 'Questions about products, pricing, or product catalog',
                                        'trigger_phrases': [
                                            'shopify product',
                                            'product details',
                                            'pricing',
                                            'catalog',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['List Shopify products', 'What is the price of a product?'],
                                        'search_strategy': 'Search by title or filter by type, vendor, or status',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.products',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/products/{product_id}.json',
                    action=Action.GET,
                    description='Retrieves a single product by ID',
                    path_params=['product_id'],
                    path_params_schema={
                        'product_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'product': {
                                'type': 'object',
                                'description': 'A Shopify product',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Unique product identifier'},
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'Product title',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'Product description in HTML',
                                    },
                                    'vendor': {
                                        'type': ['string', 'null'],
                                        'description': 'Product vendor',
                                    },
                                    'product_type': {
                                        'type': ['string', 'null'],
                                        'description': 'Product type',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'When the product was created',
                                    },
                                    'handle': {
                                        'type': ['string', 'null'],
                                        'description': 'Product handle for URL',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'When the product was last updated',
                                    },
                                    'published_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'When the product was published',
                                    },
                                    'template_suffix': {
                                        'type': ['string', 'null'],
                                        'description': 'Template suffix',
                                    },
                                    'published_scope': {
                                        'type': ['string', 'null'],
                                        'description': 'Published scope',
                                    },
                                    'tags': {
                                        'type': ['string', 'null'],
                                        'description': 'Product tags',
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                        'description': 'Product status',
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                        'description': 'GraphQL API ID',
                                    },
                                    'variants': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A product variant',
                                            'properties': {
                                                'id': {'type': 'integer', 'description': 'Variant ID'},
                                                'product_id': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Product ID',
                                                },
                                                'title': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Variant title',
                                                },
                                                'price': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Variant price',
                                                },
                                                'sku': {
                                                    'type': ['string', 'null'],
                                                    'description': 'SKU',
                                                },
                                                'position': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Position',
                                                },
                                                'inventory_policy': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Inventory policy',
                                                },
                                                'compare_at_price': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Compare at price',
                                                },
                                                'fulfillment_service': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Fulfillment service',
                                                },
                                                'inventory_management': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Inventory management',
                                                },
                                                'option1': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Option 1 value',
                                                },
                                                'option2': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Option 2 value',
                                                },
                                                'option3': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Option 3 value',
                                                },
                                                'created_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'When the variant was created',
                                                },
                                                'updated_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'When the variant was last updated',
                                                },
                                                'taxable': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether the variant is taxable',
                                                },
                                                'barcode': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Barcode',
                                                },
                                                'grams': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Weight in grams',
                                                },
                                                'image_id': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Image ID',
                                                },
                                                'weight': {
                                                    'type': ['number', 'null'],
                                                    'description': 'Weight',
                                                },
                                                'weight_unit': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Weight unit',
                                                },
                                                'inventory_item_id': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Inventory item ID',
                                                },
                                                'inventory_quantity': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Inventory quantity',
                                                },
                                                'old_inventory_quantity': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Old inventory quantity',
                                                },
                                                'requires_shipping': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether shipping is required',
                                                },
                                                'admin_graphql_api_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'GraphQL API ID',
                                                },
                                            },
                                            'required': ['id'],
                                            'x-airbyte-entity-name': 'product_variants',
                                            'x-airbyte-stream-name': 'product_variants',
                                            'x-airbyte-ai-hints': {
                                                'summary': 'Product variants with size, color, SKU, and inventory details',
                                                'when_to_use': 'Questions about product options, SKUs, or variant-level data',
                                                'trigger_phrases': [
                                                    'product variant',
                                                    'SKU',
                                                    'size',
                                                    'color option',
                                                ],
                                                'freshness': 'live',
                                                'example_questions': ['What variants does a product have?'],
                                                'search_strategy': 'Filter by product',
                                            },
                                        },
                                    },
                                    'options': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'images': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'A product image',
                                            'properties': {
                                                'id': {'type': 'integer', 'description': 'Image ID'},
                                                'product_id': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Product ID',
                                                },
                                                'position': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Position',
                                                },
                                                'created_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'When the image was created',
                                                },
                                                'updated_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'When the image was last updated',
                                                },
                                                'alt': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Alt text',
                                                },
                                                'width': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Image width',
                                                },
                                                'height': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Image height',
                                                },
                                                'src': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Image source URL',
                                                },
                                                'variant_ids': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'integer'},
                                                },
                                                'admin_graphql_api_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'GraphQL API ID',
                                                },
                                            },
                                            'required': ['id'],
                                            'x-airbyte-entity-name': 'product_images',
                                            'x-airbyte-stream-name': 'product_images',
                                            'x-airbyte-ai-hints': {
                                                'summary': 'Product images attached to Shopify products',
                                                'when_to_use': 'Looking for product photos or image assets',
                                                'trigger_phrases': ['product image', 'product photo'],
                                                'freshness': 'live',
                                                'example_questions': ['Show images for a product'],
                                                'search_strategy': 'Filter by product',
                                            },
                                        },
                                    },
                                    'image': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'A product image',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Image ID'},
                                                    'product_id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Product ID',
                                                    },
                                                    'position': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Position',
                                                    },
                                                    'created_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When the image was created',
                                                    },
                                                    'updated_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When the image was last updated',
                                                    },
                                                    'alt': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Alt text',
                                                    },
                                                    'width': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Image width',
                                                    },
                                                    'height': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Image height',
                                                    },
                                                    'src': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Image source URL',
                                                    },
                                                    'variant_ids': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'integer'},
                                                    },
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'GraphQL API ID',
                                                    },
                                                },
                                                'required': ['id'],
                                                'x-airbyte-entity-name': 'product_images',
                                                'x-airbyte-stream-name': 'product_images',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Product images attached to Shopify products',
                                                    'when_to_use': 'Looking for product photos or image assets',
                                                    'trigger_phrases': ['product image', 'product photo'],
                                                    'freshness': 'live',
                                                    'example_questions': ['Show images for a product'],
                                                    'search_strategy': 'Filter by product',
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'products',
                                'x-airbyte-stream-name': 'products',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Shopify products with title, description, pricing, and inventory',
                                    'when_to_use': 'Questions about products, pricing, or product catalog',
                                    'trigger_phrases': [
                                        'shopify product',
                                        'product details',
                                        'pricing',
                                        'catalog',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['List Shopify products', 'What is the price of a product?'],
                                    'search_strategy': 'Search by title or filter by type, vendor, or status',
                                },
                            },
                        },
                    },
                    record_extractor='$.product',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Shopify product',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique product identifier'},
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Product title',
                    },
                    'body_html': {
                        'type': ['string', 'null'],
                        'description': 'Product description in HTML',
                    },
                    'vendor': {
                        'type': ['string', 'null'],
                        'description': 'Product vendor',
                    },
                    'product_type': {
                        'type': ['string', 'null'],
                        'description': 'Product type',
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the product was created',
                    },
                    'handle': {
                        'type': ['string', 'null'],
                        'description': 'Product handle for URL',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the product was last updated',
                    },
                    'published_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the product was published',
                    },
                    'template_suffix': {
                        'type': ['string', 'null'],
                        'description': 'Template suffix',
                    },
                    'published_scope': {
                        'type': ['string', 'null'],
                        'description': 'Published scope',
                    },
                    'tags': {
                        'type': ['string', 'null'],
                        'description': 'Product tags',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Product status',
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                        'description': 'GraphQL API ID',
                    },
                    'variants': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/ProductVariant'},
                    },
                    'options': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'images': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/ProductImage'},
                    },
                    'image': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ProductImage'},
                            {'type': 'null'},
                        ],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'products',
                'x-airbyte-stream-name': 'products',
                'x-airbyte-ai-hints': {
                    'summary': 'Shopify products with title, description, pricing, and inventory',
                    'when_to_use': 'Questions about products, pricing, or product catalog',
                    'trigger_phrases': [
                        'shopify product',
                        'product details',
                        'pricing',
                        'catalog',
                    ],
                    'freshness': 'live',
                    'example_questions': ['List Shopify products', 'What is the price of a product?'],
                    'search_strategy': 'Search by title or filter by type, vendor, or status',
                },
            },
            ai_hints={
                'summary': 'Shopify products with title, description, pricing, and inventory',
                'when_to_use': 'Questions about products, pricing, or product catalog',
                'trigger_phrases': [
                    'shopify product',
                    'product details',
                    'pricing',
                    'catalog',
                ],
                'freshness': 'live',
                'example_questions': ['List Shopify products', 'What is the price of a product?'],
                'search_strategy': 'Search by title or filter by type, vendor, or status',
            },
        ),
        EntityDefinition(
            name='product_variants',
            stream_name='product_variants',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/products/{product_id}/variants.json',
                    action=Action.LIST,
                    description='Returns a list of variants for a product',
                    query_params=['limit', 'since_id'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                    },
                    path_params=['product_id'],
                    path_params_schema={
                        'product_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'variants': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A product variant',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Variant ID'},
                                        'product_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Product ID',
                                        },
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Variant title',
                                        },
                                        'price': {
                                            'type': ['string', 'null'],
                                            'description': 'Variant price',
                                        },
                                        'sku': {
                                            'type': ['string', 'null'],
                                            'description': 'SKU',
                                        },
                                        'position': {
                                            'type': ['integer', 'null'],
                                            'description': 'Position',
                                        },
                                        'inventory_policy': {
                                            'type': ['string', 'null'],
                                            'description': 'Inventory policy',
                                        },
                                        'compare_at_price': {
                                            'type': ['string', 'null'],
                                            'description': 'Compare at price',
                                        },
                                        'fulfillment_service': {
                                            'type': ['string', 'null'],
                                            'description': 'Fulfillment service',
                                        },
                                        'inventory_management': {
                                            'type': ['string', 'null'],
                                            'description': 'Inventory management',
                                        },
                                        'option1': {
                                            'type': ['string', 'null'],
                                            'description': 'Option 1 value',
                                        },
                                        'option2': {
                                            'type': ['string', 'null'],
                                            'description': 'Option 2 value',
                                        },
                                        'option3': {
                                            'type': ['string', 'null'],
                                            'description': 'Option 3 value',
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the variant was created',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the variant was last updated',
                                        },
                                        'taxable': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the variant is taxable',
                                        },
                                        'barcode': {
                                            'type': ['string', 'null'],
                                            'description': 'Barcode',
                                        },
                                        'grams': {
                                            'type': ['integer', 'null'],
                                            'description': 'Weight in grams',
                                        },
                                        'image_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Image ID',
                                        },
                                        'weight': {
                                            'type': ['number', 'null'],
                                            'description': 'Weight',
                                        },
                                        'weight_unit': {
                                            'type': ['string', 'null'],
                                            'description': 'Weight unit',
                                        },
                                        'inventory_item_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Inventory item ID',
                                        },
                                        'inventory_quantity': {
                                            'type': ['integer', 'null'],
                                            'description': 'Inventory quantity',
                                        },
                                        'old_inventory_quantity': {
                                            'type': ['integer', 'null'],
                                            'description': 'Old inventory quantity',
                                        },
                                        'requires_shipping': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether shipping is required',
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                            'description': 'GraphQL API ID',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'product_variants',
                                    'x-airbyte-stream-name': 'product_variants',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Product variants with size, color, SKU, and inventory details',
                                        'when_to_use': 'Questions about product options, SKUs, or variant-level data',
                                        'trigger_phrases': [
                                            'product variant',
                                            'SKU',
                                            'size',
                                            'color option',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What variants does a product have?'],
                                        'search_strategy': 'Filter by product',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.variants',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/variants/{variant_id}.json',
                    action=Action.GET,
                    description='Retrieves a single product variant by ID',
                    path_params=['variant_id'],
                    path_params_schema={
                        'variant_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'variant': {
                                'type': 'object',
                                'description': 'A product variant',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Variant ID'},
                                    'product_id': {
                                        'type': ['integer', 'null'],
                                        'description': 'Product ID',
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'Variant title',
                                    },
                                    'price': {
                                        'type': ['string', 'null'],
                                        'description': 'Variant price',
                                    },
                                    'sku': {
                                        'type': ['string', 'null'],
                                        'description': 'SKU',
                                    },
                                    'position': {
                                        'type': ['integer', 'null'],
                                        'description': 'Position',
                                    },
                                    'inventory_policy': {
                                        'type': ['string', 'null'],
                                        'description': 'Inventory policy',
                                    },
                                    'compare_at_price': {
                                        'type': ['string', 'null'],
                                        'description': 'Compare at price',
                                    },
                                    'fulfillment_service': {
                                        'type': ['string', 'null'],
                                        'description': 'Fulfillment service',
                                    },
                                    'inventory_management': {
                                        'type': ['string', 'null'],
                                        'description': 'Inventory management',
                                    },
                                    'option1': {
                                        'type': ['string', 'null'],
                                        'description': 'Option 1 value',
                                    },
                                    'option2': {
                                        'type': ['string', 'null'],
                                        'description': 'Option 2 value',
                                    },
                                    'option3': {
                                        'type': ['string', 'null'],
                                        'description': 'Option 3 value',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'When the variant was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'When the variant was last updated',
                                    },
                                    'taxable': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the variant is taxable',
                                    },
                                    'barcode': {
                                        'type': ['string', 'null'],
                                        'description': 'Barcode',
                                    },
                                    'grams': {
                                        'type': ['integer', 'null'],
                                        'description': 'Weight in grams',
                                    },
                                    'image_id': {
                                        'type': ['integer', 'null'],
                                        'description': 'Image ID',
                                    },
                                    'weight': {
                                        'type': ['number', 'null'],
                                        'description': 'Weight',
                                    },
                                    'weight_unit': {
                                        'type': ['string', 'null'],
                                        'description': 'Weight unit',
                                    },
                                    'inventory_item_id': {
                                        'type': ['integer', 'null'],
                                        'description': 'Inventory item ID',
                                    },
                                    'inventory_quantity': {
                                        'type': ['integer', 'null'],
                                        'description': 'Inventory quantity',
                                    },
                                    'old_inventory_quantity': {
                                        'type': ['integer', 'null'],
                                        'description': 'Old inventory quantity',
                                    },
                                    'requires_shipping': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether shipping is required',
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                        'description': 'GraphQL API ID',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'product_variants',
                                'x-airbyte-stream-name': 'product_variants',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Product variants with size, color, SKU, and inventory details',
                                    'when_to_use': 'Questions about product options, SKUs, or variant-level data',
                                    'trigger_phrases': [
                                        'product variant',
                                        'SKU',
                                        'size',
                                        'color option',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What variants does a product have?'],
                                    'search_strategy': 'Filter by product',
                                },
                            },
                        },
                    },
                    record_extractor='$.variant',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A product variant',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Variant ID'},
                    'product_id': {
                        'type': ['integer', 'null'],
                        'description': 'Product ID',
                    },
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Variant title',
                    },
                    'price': {
                        'type': ['string', 'null'],
                        'description': 'Variant price',
                    },
                    'sku': {
                        'type': ['string', 'null'],
                        'description': 'SKU',
                    },
                    'position': {
                        'type': ['integer', 'null'],
                        'description': 'Position',
                    },
                    'inventory_policy': {
                        'type': ['string', 'null'],
                        'description': 'Inventory policy',
                    },
                    'compare_at_price': {
                        'type': ['string', 'null'],
                        'description': 'Compare at price',
                    },
                    'fulfillment_service': {
                        'type': ['string', 'null'],
                        'description': 'Fulfillment service',
                    },
                    'inventory_management': {
                        'type': ['string', 'null'],
                        'description': 'Inventory management',
                    },
                    'option1': {
                        'type': ['string', 'null'],
                        'description': 'Option 1 value',
                    },
                    'option2': {
                        'type': ['string', 'null'],
                        'description': 'Option 2 value',
                    },
                    'option3': {
                        'type': ['string', 'null'],
                        'description': 'Option 3 value',
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the variant was created',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the variant was last updated',
                    },
                    'taxable': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the variant is taxable',
                    },
                    'barcode': {
                        'type': ['string', 'null'],
                        'description': 'Barcode',
                    },
                    'grams': {
                        'type': ['integer', 'null'],
                        'description': 'Weight in grams',
                    },
                    'image_id': {
                        'type': ['integer', 'null'],
                        'description': 'Image ID',
                    },
                    'weight': {
                        'type': ['number', 'null'],
                        'description': 'Weight',
                    },
                    'weight_unit': {
                        'type': ['string', 'null'],
                        'description': 'Weight unit',
                    },
                    'inventory_item_id': {
                        'type': ['integer', 'null'],
                        'description': 'Inventory item ID',
                    },
                    'inventory_quantity': {
                        'type': ['integer', 'null'],
                        'description': 'Inventory quantity',
                    },
                    'old_inventory_quantity': {
                        'type': ['integer', 'null'],
                        'description': 'Old inventory quantity',
                    },
                    'requires_shipping': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether shipping is required',
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                        'description': 'GraphQL API ID',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'product_variants',
                'x-airbyte-stream-name': 'product_variants',
                'x-airbyte-ai-hints': {
                    'summary': 'Product variants with size, color, SKU, and inventory details',
                    'when_to_use': 'Questions about product options, SKUs, or variant-level data',
                    'trigger_phrases': [
                        'product variant',
                        'SKU',
                        'size',
                        'color option',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What variants does a product have?'],
                    'search_strategy': 'Filter by product',
                },
            },
            ai_hints={
                'summary': 'Product variants with size, color, SKU, and inventory details',
                'when_to_use': 'Questions about product options, SKUs, or variant-level data',
                'trigger_phrases': [
                    'product variant',
                    'SKU',
                    'size',
                    'color option',
                ],
                'freshness': 'live',
                'example_questions': ['What variants does a product have?'],
                'search_strategy': 'Filter by product',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='product_variants',
                    target_entity='products',
                    foreign_key='product_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='product_images',
            stream_name='product_images',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/products/{product_id}/images.json',
                    action=Action.LIST,
                    description='Returns a list of images for a product',
                    query_params=['since_id'],
                    query_params_schema={
                        'since_id': {'type': 'integer', 'required': False},
                    },
                    path_params=['product_id'],
                    path_params_schema={
                        'product_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'images': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A product image',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Image ID'},
                                        'product_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Product ID',
                                        },
                                        'position': {
                                            'type': ['integer', 'null'],
                                            'description': 'Position',
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the image was created',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the image was last updated',
                                        },
                                        'alt': {
                                            'type': ['string', 'null'],
                                            'description': 'Alt text',
                                        },
                                        'width': {
                                            'type': ['integer', 'null'],
                                            'description': 'Image width',
                                        },
                                        'height': {
                                            'type': ['integer', 'null'],
                                            'description': 'Image height',
                                        },
                                        'src': {
                                            'type': ['string', 'null'],
                                            'description': 'Image source URL',
                                        },
                                        'variant_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                            'description': 'GraphQL API ID',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'product_images',
                                    'x-airbyte-stream-name': 'product_images',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Product images attached to Shopify products',
                                        'when_to_use': 'Looking for product photos or image assets',
                                        'trigger_phrases': ['product image', 'product photo'],
                                        'freshness': 'live',
                                        'example_questions': ['Show images for a product'],
                                        'search_strategy': 'Filter by product',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.images',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/products/{product_id}/images/{image_id}.json',
                    action=Action.GET,
                    description='Retrieves a single product image by ID',
                    path_params=['product_id', 'image_id'],
                    path_params_schema={
                        'product_id': {'type': 'integer', 'required': True},
                        'image_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'image': {
                                'type': 'object',
                                'description': 'A product image',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Image ID'},
                                    'product_id': {
                                        'type': ['integer', 'null'],
                                        'description': 'Product ID',
                                    },
                                    'position': {
                                        'type': ['integer', 'null'],
                                        'description': 'Position',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'When the image was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'When the image was last updated',
                                    },
                                    'alt': {
                                        'type': ['string', 'null'],
                                        'description': 'Alt text',
                                    },
                                    'width': {
                                        'type': ['integer', 'null'],
                                        'description': 'Image width',
                                    },
                                    'height': {
                                        'type': ['integer', 'null'],
                                        'description': 'Image height',
                                    },
                                    'src': {
                                        'type': ['string', 'null'],
                                        'description': 'Image source URL',
                                    },
                                    'variant_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'integer'},
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                        'description': 'GraphQL API ID',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'product_images',
                                'x-airbyte-stream-name': 'product_images',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Product images attached to Shopify products',
                                    'when_to_use': 'Looking for product photos or image assets',
                                    'trigger_phrases': ['product image', 'product photo'],
                                    'freshness': 'live',
                                    'example_questions': ['Show images for a product'],
                                    'search_strategy': 'Filter by product',
                                },
                            },
                        },
                    },
                    record_extractor='$.image',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A product image',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Image ID'},
                    'product_id': {
                        'type': ['integer', 'null'],
                        'description': 'Product ID',
                    },
                    'position': {
                        'type': ['integer', 'null'],
                        'description': 'Position',
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the image was created',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the image was last updated',
                    },
                    'alt': {
                        'type': ['string', 'null'],
                        'description': 'Alt text',
                    },
                    'width': {
                        'type': ['integer', 'null'],
                        'description': 'Image width',
                    },
                    'height': {
                        'type': ['integer', 'null'],
                        'description': 'Image height',
                    },
                    'src': {
                        'type': ['string', 'null'],
                        'description': 'Image source URL',
                    },
                    'variant_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                        'description': 'GraphQL API ID',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'product_images',
                'x-airbyte-stream-name': 'product_images',
                'x-airbyte-ai-hints': {
                    'summary': 'Product images attached to Shopify products',
                    'when_to_use': 'Looking for product photos or image assets',
                    'trigger_phrases': ['product image', 'product photo'],
                    'freshness': 'live',
                    'example_questions': ['Show images for a product'],
                    'search_strategy': 'Filter by product',
                },
            },
            ai_hints={
                'summary': 'Product images attached to Shopify products',
                'when_to_use': 'Looking for product photos or image assets',
                'trigger_phrases': ['product image', 'product photo'],
                'freshness': 'live',
                'example_questions': ['Show images for a product'],
                'search_strategy': 'Filter by product',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='product_images',
                    target_entity='products',
                    foreign_key='product_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='abandoned_checkouts',
            stream_name='abandoned_checkouts',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/checkouts.json',
                    action=Action.LIST,
                    description='Returns a list of abandoned checkouts',
                    query_params=[
                        'limit',
                        'since_id',
                        'created_at_min',
                        'created_at_max',
                        'updated_at_min',
                        'updated_at_max',
                        'status',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'created_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'status': {
                            'type': 'string',
                            'required': False,
                            'default': 'any',
                            'enum': ['open', 'closed', 'any'],
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'checkouts': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An abandoned checkout',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Checkout ID'},
                                        'token': {
                                            'type': ['string', 'null'],
                                        },
                                        'cart_token': {
                                            'type': ['string', 'null'],
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                        },
                                        'gateway': {
                                            'type': ['string', 'null'],
                                        },
                                        'buyer_accepts_marketing': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'landing_site': {
                                            'type': ['string', 'null'],
                                        },
                                        'note': {
                                            'type': ['string', 'null'],
                                        },
                                        'note_attributes': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'referring_site': {
                                            'type': ['string', 'null'],
                                        },
                                        'shipping_lines': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'taxes_included': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'total_weight': {
                                            'type': ['integer', 'null'],
                                        },
                                        'currency': {
                                            'type': ['string', 'null'],
                                        },
                                        'completed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'closed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'user_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'location_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'source_identifier': {
                                            'type': ['string', 'null'],
                                        },
                                        'source_url': {
                                            'type': ['string', 'null'],
                                        },
                                        'device_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'phone': {
                                            'type': ['string', 'null'],
                                        },
                                        'customer_locale': {
                                            'type': ['string', 'null'],
                                        },
                                        'line_items': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'integer'},
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'attributed_staffs': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'current_quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'fulfillable_quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'fulfillment_service': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'fulfillment_status': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'gift_card': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'grams': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'price': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'price_set': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'product_exists': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'product_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'properties': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'requires_shipping': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'sku': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'taxable': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'total_discount': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'total_discount_set': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'variant_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'variant_inventory_management': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'variant_title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'vendor': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'tax_lines': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'duties': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'discount_allocations': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                },
                                            },
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'source': {
                                            'type': ['string', 'null'],
                                        },
                                        'abandoned_checkout_url': {
                                            'type': ['string', 'null'],
                                        },
                                        'discount_codes': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'tax_lines': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'source_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'presentment_currency': {
                                            'type': ['string', 'null'],
                                        },
                                        'buyer_accepts_sms_marketing': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'sms_marketing_phone': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_discounts': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_line_items_price': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_price': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_tax': {
                                            'type': ['string', 'null'],
                                        },
                                        'subtotal_price': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_duties': {
                                            'type': ['string', 'null'],
                                        },
                                        'billing_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'An address in an order (shipping or billing) - does not have id field',
                                                    'properties': {
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'company': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address1': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address2': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'zip': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province_code': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country_code': {
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
                                                {'type': 'null'},
                                            ],
                                        },
                                        'shipping_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'An address in an order (shipping or billing) - does not have id field',
                                                    'properties': {
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'company': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address1': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address2': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'zip': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province_code': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country_code': {
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
                                                {'type': 'null'},
                                            ],
                                        },
                                        'customer': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'A Shopify customer',
                                                    'properties': {
                                                        'id': {'type': 'integer', 'description': 'Unique customer identifier'},
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer email address',
                                                        },
                                                        'accepts_marketing': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the customer accepts marketing',
                                                        },
                                                        'created_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When the customer was created',
                                                        },
                                                        'updated_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When the customer was last updated',
                                                        },
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer first name',
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer last name',
                                                        },
                                                        'orders_count': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Number of orders',
                                                        },
                                                        'state': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer state',
                                                        },
                                                        'total_spent': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Total amount spent',
                                                        },
                                                        'last_order_id': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'ID of last order',
                                                        },
                                                        'note': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Note about the customer',
                                                        },
                                                        'verified_email': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether email is verified',
                                                        },
                                                        'multipass_identifier': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Multipass identifier',
                                                        },
                                                        'tax_exempt': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether customer is tax exempt',
                                                        },
                                                        'tags': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Tags associated with customer',
                                                        },
                                                        'last_order_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Name of last order',
                                                        },
                                                        'currency': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer currency',
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer phone number',
                                                        },
                                                        'addresses': {
                                                            'type': ['array', 'null'],
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'A customer address',
                                                                'properties': {
                                                                    'id': {'type': 'integer', 'description': 'Address ID'},
                                                                    'customer_id': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Customer ID',
                                                                    },
                                                                    'first_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'First name',
                                                                    },
                                                                    'last_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Last name',
                                                                    },
                                                                    'company': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Company name',
                                                                    },
                                                                    'address1': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Address line 1',
                                                                    },
                                                                    'address2': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Address line 2',
                                                                    },
                                                                    'city': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'City',
                                                                    },
                                                                    'province': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Province/State',
                                                                    },
                                                                    'country': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country',
                                                                    },
                                                                    'zip': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'ZIP/Postal code',
                                                                    },
                                                                    'phone': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Phone number',
                                                                    },
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Full name',
                                                                    },
                                                                    'province_code': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Province code',
                                                                    },
                                                                    'country_code': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country code',
                                                                    },
                                                                    'country_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country name',
                                                                    },
                                                                    'default': {
                                                                        'type': ['boolean', 'null'],
                                                                        'description': 'Whether this is the default address',
                                                                    },
                                                                },
                                                                'required': ['id'],
                                                            },
                                                        },
                                                        'accepts_marketing_updated_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When marketing acceptance was updated',
                                                        },
                                                        'marketing_opt_in_level': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Marketing opt-in level',
                                                        },
                                                        'tax_exemptions': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'string'},
                                                        },
                                                        'email_marketing_consent': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'state': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'opt_in_level': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'consent_updated_at': {
                                                                            'type': ['string', 'null'],
                                                                            'format': 'date-time',
                                                                        },
                                                                        'consent_collected_from': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'sms_marketing_consent': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'state': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'opt_in_level': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'consent_updated_at': {
                                                                            'type': ['string', 'null'],
                                                                            'format': 'date-time',
                                                                        },
                                                                        'consent_collected_from': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'admin_graphql_api_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'GraphQL API ID',
                                                        },
                                                        'default_address': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'A customer address',
                                                                    'properties': {
                                                                        'id': {'type': 'integer', 'description': 'Address ID'},
                                                                        'customer_id': {
                                                                            'type': ['integer', 'null'],
                                                                            'description': 'Customer ID',
                                                                        },
                                                                        'first_name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'First name',
                                                                        },
                                                                        'last_name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Last name',
                                                                        },
                                                                        'company': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Company name',
                                                                        },
                                                                        'address1': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Address line 1',
                                                                        },
                                                                        'address2': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Address line 2',
                                                                        },
                                                                        'city': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'City',
                                                                        },
                                                                        'province': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Province/State',
                                                                        },
                                                                        'country': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Country',
                                                                        },
                                                                        'zip': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'ZIP/Postal code',
                                                                        },
                                                                        'phone': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Phone number',
                                                                        },
                                                                        'name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Full name',
                                                                        },
                                                                        'province_code': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Province code',
                                                                        },
                                                                        'country_code': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Country code',
                                                                        },
                                                                        'country_name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Country name',
                                                                        },
                                                                        'default': {
                                                                            'type': ['boolean', 'null'],
                                                                            'description': 'Whether this is the default address',
                                                                        },
                                                                    },
                                                                    'required': ['id'],
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                    },
                                                    'required': ['id'],
                                                    'x-airbyte-entity-name': 'customers',
                                                    'x-airbyte-stream-name': 'customers',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Shopify customers with order history and contact information',
                                                        'when_to_use': 'Looking up customer details or purchase history',
                                                        'trigger_phrases': ['shopify customer', 'buyer', 'customer info'],
                                                        'freshness': 'live',
                                                        'example_questions': ['Find a customer in Shopify', 'Show customer order history'],
                                                        'search_strategy': 'Search by email, name, or phone',
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'abandoned_checkouts',
                                    'x-airbyte-stream-name': 'abandoned_checkouts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Abandoned checkout sessions with cart contents and customer info',
                                        'when_to_use': 'Questions about abandoned carts or checkout drop-off',
                                        'trigger_phrases': ['abandoned checkout', 'abandoned cart', 'cart recovery'],
                                        'freshness': 'live',
                                        'example_questions': ['Show abandoned checkouts', 'How many carts were abandoned?'],
                                        'search_strategy': 'Filter by date or customer',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.checkouts',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An abandoned checkout',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Checkout ID'},
                    'token': {
                        'type': ['string', 'null'],
                    },
                    'cart_token': {
                        'type': ['string', 'null'],
                    },
                    'email': {
                        'type': ['string', 'null'],
                    },
                    'gateway': {
                        'type': ['string', 'null'],
                    },
                    'buyer_accepts_marketing': {
                        'type': ['boolean', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'landing_site': {
                        'type': ['string', 'null'],
                    },
                    'note': {
                        'type': ['string', 'null'],
                    },
                    'note_attributes': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'referring_site': {
                        'type': ['string', 'null'],
                    },
                    'shipping_lines': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'taxes_included': {
                        'type': ['boolean', 'null'],
                    },
                    'total_weight': {
                        'type': ['integer', 'null'],
                    },
                    'currency': {
                        'type': ['string', 'null'],
                    },
                    'completed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'closed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'user_id': {
                        'type': ['integer', 'null'],
                    },
                    'location_id': {
                        'type': ['integer', 'null'],
                    },
                    'source_identifier': {
                        'type': ['string', 'null'],
                    },
                    'source_url': {
                        'type': ['string', 'null'],
                    },
                    'device_id': {
                        'type': ['integer', 'null'],
                    },
                    'phone': {
                        'type': ['string', 'null'],
                    },
                    'customer_locale': {
                        'type': ['string', 'null'],
                    },
                    'line_items': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/LineItem'},
                    },
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'source': {
                        'type': ['string', 'null'],
                    },
                    'abandoned_checkout_url': {
                        'type': ['string', 'null'],
                    },
                    'discount_codes': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'tax_lines': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'source_name': {
                        'type': ['string', 'null'],
                    },
                    'presentment_currency': {
                        'type': ['string', 'null'],
                    },
                    'buyer_accepts_sms_marketing': {
                        'type': ['boolean', 'null'],
                    },
                    'sms_marketing_phone': {
                        'type': ['string', 'null'],
                    },
                    'total_discounts': {
                        'type': ['string', 'null'],
                    },
                    'total_line_items_price': {
                        'type': ['string', 'null'],
                    },
                    'total_price': {
                        'type': ['string', 'null'],
                    },
                    'total_tax': {
                        'type': ['string', 'null'],
                    },
                    'subtotal_price': {
                        'type': ['string', 'null'],
                    },
                    'total_duties': {
                        'type': ['string', 'null'],
                    },
                    'billing_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/OrderAddress'},
                            {'type': 'null'},
                        ],
                    },
                    'shipping_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/OrderAddress'},
                            {'type': 'null'},
                        ],
                    },
                    'customer': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Customer'},
                            {'type': 'null'},
                        ],
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'abandoned_checkouts',
                'x-airbyte-stream-name': 'abandoned_checkouts',
                'x-airbyte-ai-hints': {
                    'summary': 'Abandoned checkout sessions with cart contents and customer info',
                    'when_to_use': 'Questions about abandoned carts or checkout drop-off',
                    'trigger_phrases': ['abandoned checkout', 'abandoned cart', 'cart recovery'],
                    'freshness': 'live',
                    'example_questions': ['Show abandoned checkouts', 'How many carts were abandoned?'],
                    'search_strategy': 'Filter by date or customer',
                },
            },
            ai_hints={
                'summary': 'Abandoned checkout sessions with cart contents and customer info',
                'when_to_use': 'Questions about abandoned carts or checkout drop-off',
                'trigger_phrases': ['abandoned checkout', 'abandoned cart', 'cart recovery'],
                'freshness': 'live',
                'example_questions': ['Show abandoned checkouts', 'How many carts were abandoned?'],
                'search_strategy': 'Filter by date or customer',
            },
        ),
        EntityDefinition(
            name='locations',
            stream_name='locations',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/locations.json',
                    action=Action.LIST,
                    description='Returns a list of locations for the store',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'locations': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A store location',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Location ID'},
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'address1': {
                                            'type': ['string', 'null'],
                                        },
                                        'address2': {
                                            'type': ['string', 'null'],
                                        },
                                        'city': {
                                            'type': ['string', 'null'],
                                        },
                                        'zip': {
                                            'type': ['string', 'null'],
                                        },
                                        'province': {
                                            'type': ['string', 'null'],
                                        },
                                        'country': {
                                            'type': ['string', 'null'],
                                        },
                                        'phone': {
                                            'type': ['string', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'country_code': {
                                            'type': ['string', 'null'],
                                        },
                                        'country_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'province_code': {
                                            'type': ['string', 'null'],
                                        },
                                        'legacy': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'active': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'localized_country_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'localized_province_name': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'locations',
                                    'x-airbyte-stream-name': 'locations',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Shopify store locations for inventory and fulfillment',
                                        'when_to_use': 'Questions about store or warehouse locations',
                                        'trigger_phrases': ['shopify location', 'warehouse', 'store location'],
                                        'freshness': 'static',
                                        'example_questions': ['What locations are configured in Shopify?'],
                                        'search_strategy': 'List all locations',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.locations',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/locations/{location_id}.json',
                    action=Action.GET,
                    description='Retrieves a single location by ID',
                    path_params=['location_id'],
                    path_params_schema={
                        'location_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'location': {
                                'type': 'object',
                                'description': 'A store location',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Location ID'},
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'address1': {
                                        'type': ['string', 'null'],
                                    },
                                    'address2': {
                                        'type': ['string', 'null'],
                                    },
                                    'city': {
                                        'type': ['string', 'null'],
                                    },
                                    'zip': {
                                        'type': ['string', 'null'],
                                    },
                                    'province': {
                                        'type': ['string', 'null'],
                                    },
                                    'country': {
                                        'type': ['string', 'null'],
                                    },
                                    'phone': {
                                        'type': ['string', 'null'],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'country_code': {
                                        'type': ['string', 'null'],
                                    },
                                    'country_name': {
                                        'type': ['string', 'null'],
                                    },
                                    'province_code': {
                                        'type': ['string', 'null'],
                                    },
                                    'legacy': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'active': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'localized_country_name': {
                                        'type': ['string', 'null'],
                                    },
                                    'localized_province_name': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'locations',
                                'x-airbyte-stream-name': 'locations',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Shopify store locations for inventory and fulfillment',
                                    'when_to_use': 'Questions about store or warehouse locations',
                                    'trigger_phrases': ['shopify location', 'warehouse', 'store location'],
                                    'freshness': 'static',
                                    'example_questions': ['What locations are configured in Shopify?'],
                                    'search_strategy': 'List all locations',
                                },
                            },
                        },
                    },
                    record_extractor='$.location',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A store location',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Location ID'},
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'address1': {
                        'type': ['string', 'null'],
                    },
                    'address2': {
                        'type': ['string', 'null'],
                    },
                    'city': {
                        'type': ['string', 'null'],
                    },
                    'zip': {
                        'type': ['string', 'null'],
                    },
                    'province': {
                        'type': ['string', 'null'],
                    },
                    'country': {
                        'type': ['string', 'null'],
                    },
                    'phone': {
                        'type': ['string', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'country_code': {
                        'type': ['string', 'null'],
                    },
                    'country_name': {
                        'type': ['string', 'null'],
                    },
                    'province_code': {
                        'type': ['string', 'null'],
                    },
                    'legacy': {
                        'type': ['boolean', 'null'],
                    },
                    'active': {
                        'type': ['boolean', 'null'],
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                    'localized_country_name': {
                        'type': ['string', 'null'],
                    },
                    'localized_province_name': {
                        'type': ['string', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'locations',
                'x-airbyte-stream-name': 'locations',
                'x-airbyte-ai-hints': {
                    'summary': 'Shopify store locations for inventory and fulfillment',
                    'when_to_use': 'Questions about store or warehouse locations',
                    'trigger_phrases': ['shopify location', 'warehouse', 'store location'],
                    'freshness': 'static',
                    'example_questions': ['What locations are configured in Shopify?'],
                    'search_strategy': 'List all locations',
                },
            },
            ai_hints={
                'summary': 'Shopify store locations for inventory and fulfillment',
                'when_to_use': 'Questions about store or warehouse locations',
                'trigger_phrases': ['shopify location', 'warehouse', 'store location'],
                'freshness': 'static',
                'example_questions': ['What locations are configured in Shopify?'],
                'search_strategy': 'List all locations',
            },
        ),
        EntityDefinition(
            name='inventory_levels',
            stream_name='inventory_levels',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/locations/{location_id}/inventory_levels.json',
                    action=Action.LIST,
                    description='Returns a list of inventory levels for a specific location',
                    query_params=['limit'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                    },
                    path_params=['location_id'],
                    path_params_schema={
                        'location_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'inventory_levels': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An inventory level',
                                    'properties': {
                                        'inventory_item_id': {'type': 'integer'},
                                        'location_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'available': {
                                            'type': ['integer', 'null'],
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'x-airbyte-entity-name': 'inventory_levels',
                                    'x-airbyte-stream-name': 'inventory_levels',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Inventory quantities at specific locations for variants',
                                        'when_to_use': 'Questions about stock levels or inventory availability',
                                        'trigger_phrases': ['inventory level', 'stock level', 'how many in stock'],
                                        'freshness': 'live',
                                        'example_questions': ['What is the stock level for a product?'],
                                        'search_strategy': 'Filter by location or inventory item',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.inventory_levels',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An inventory level',
                'properties': {
                    'inventory_item_id': {'type': 'integer'},
                    'location_id': {
                        'type': ['integer', 'null'],
                    },
                    'available': {
                        'type': ['integer', 'null'],
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                },
                'x-airbyte-entity-name': 'inventory_levels',
                'x-airbyte-stream-name': 'inventory_levels',
                'x-airbyte-ai-hints': {
                    'summary': 'Inventory quantities at specific locations for variants',
                    'when_to_use': 'Questions about stock levels or inventory availability',
                    'trigger_phrases': ['inventory level', 'stock level', 'how many in stock'],
                    'freshness': 'live',
                    'example_questions': ['What is the stock level for a product?'],
                    'search_strategy': 'Filter by location or inventory item',
                },
            },
            ai_hints={
                'summary': 'Inventory quantities at specific locations for variants',
                'when_to_use': 'Questions about stock levels or inventory availability',
                'trigger_phrases': ['inventory level', 'stock level', 'how many in stock'],
                'freshness': 'live',
                'example_questions': ['What is the stock level for a product?'],
                'search_strategy': 'Filter by location or inventory item',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='inventory_levels',
                    target_entity='locations',
                    foreign_key='location_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='inventory_items',
            stream_name='inventory_items',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/inventory_items.json',
                    action=Action.LIST,
                    description='Returns a list of inventory items',
                    query_params=['ids', 'limit'],
                    query_params_schema={
                        'ids': {
                            'type': 'string',
                            'required': True,
                            'default': '',
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'inventory_items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An inventory item',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Inventory item ID'},
                                        'sku': {
                                            'type': ['string', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'requires_shipping': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'cost': {
                                            'type': ['string', 'null'],
                                        },
                                        'country_code_of_origin': {
                                            'type': ['string', 'null'],
                                        },
                                        'province_code_of_origin': {
                                            'type': ['string', 'null'],
                                        },
                                        'harmonized_system_code': {
                                            'type': ['string', 'null'],
                                        },
                                        'tracked': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'country_harmonized_system_codes': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'inventory_items',
                                    'x-airbyte-stream-name': 'inventory_items',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Inventory items representing physical goods for tracking',
                                        'when_to_use': 'Questions about inventory item details or tracking configuration',
                                        'trigger_phrases': ['inventory item', 'tracked inventory'],
                                        'freshness': 'live',
                                        'example_questions': ['Show inventory item details'],
                                        'search_strategy': 'Filter by product variant',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.inventory_items',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/inventory_items/{inventory_item_id}.json',
                    action=Action.GET,
                    description='Retrieves a single inventory item by ID',
                    path_params=['inventory_item_id'],
                    path_params_schema={
                        'inventory_item_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'inventory_item': {
                                'type': 'object',
                                'description': 'An inventory item',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Inventory item ID'},
                                    'sku': {
                                        'type': ['string', 'null'],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'requires_shipping': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'cost': {
                                        'type': ['string', 'null'],
                                    },
                                    'country_code_of_origin': {
                                        'type': ['string', 'null'],
                                    },
                                    'province_code_of_origin': {
                                        'type': ['string', 'null'],
                                    },
                                    'harmonized_system_code': {
                                        'type': ['string', 'null'],
                                    },
                                    'tracked': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'country_harmonized_system_codes': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'inventory_items',
                                'x-airbyte-stream-name': 'inventory_items',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Inventory items representing physical goods for tracking',
                                    'when_to_use': 'Questions about inventory item details or tracking configuration',
                                    'trigger_phrases': ['inventory item', 'tracked inventory'],
                                    'freshness': 'live',
                                    'example_questions': ['Show inventory item details'],
                                    'search_strategy': 'Filter by product variant',
                                },
                            },
                        },
                    },
                    record_extractor='$.inventory_item',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An inventory item',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Inventory item ID'},
                    'sku': {
                        'type': ['string', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'requires_shipping': {
                        'type': ['boolean', 'null'],
                    },
                    'cost': {
                        'type': ['string', 'null'],
                    },
                    'country_code_of_origin': {
                        'type': ['string', 'null'],
                    },
                    'province_code_of_origin': {
                        'type': ['string', 'null'],
                    },
                    'harmonized_system_code': {
                        'type': ['string', 'null'],
                    },
                    'tracked': {
                        'type': ['boolean', 'null'],
                    },
                    'country_harmonized_system_codes': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'inventory_items',
                'x-airbyte-stream-name': 'inventory_items',
                'x-airbyte-ai-hints': {
                    'summary': 'Inventory items representing physical goods for tracking',
                    'when_to_use': 'Questions about inventory item details or tracking configuration',
                    'trigger_phrases': ['inventory item', 'tracked inventory'],
                    'freshness': 'live',
                    'example_questions': ['Show inventory item details'],
                    'search_strategy': 'Filter by product variant',
                },
            },
            ai_hints={
                'summary': 'Inventory items representing physical goods for tracking',
                'when_to_use': 'Questions about inventory item details or tracking configuration',
                'trigger_phrases': ['inventory item', 'tracked inventory'],
                'freshness': 'live',
                'example_questions': ['Show inventory item details'],
                'search_strategy': 'Filter by product variant',
            },
        ),
        EntityDefinition(
            name='shop',
            stream_name='shop',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/shop.json',
                    action=Action.GET,
                    description="Retrieves the shop's configuration",
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'shop': {
                                'type': 'object',
                                'description': 'Shop configuration',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Shop ID'},
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                    },
                                    'domain': {
                                        'type': ['string', 'null'],
                                    },
                                    'province': {
                                        'type': ['string', 'null'],
                                    },
                                    'country': {
                                        'type': ['string', 'null'],
                                    },
                                    'address1': {
                                        'type': ['string', 'null'],
                                    },
                                    'zip': {
                                        'type': ['string', 'null'],
                                    },
                                    'city': {
                                        'type': ['string', 'null'],
                                    },
                                    'source': {
                                        'type': ['string', 'null'],
                                    },
                                    'phone': {
                                        'type': ['string', 'null'],
                                    },
                                    'latitude': {
                                        'type': ['number', 'null'],
                                    },
                                    'longitude': {
                                        'type': ['number', 'null'],
                                    },
                                    'primary_locale': {
                                        'type': ['string', 'null'],
                                    },
                                    'address2': {
                                        'type': ['string', 'null'],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'country_code': {
                                        'type': ['string', 'null'],
                                    },
                                    'country_name': {
                                        'type': ['string', 'null'],
                                    },
                                    'currency': {
                                        'type': ['string', 'null'],
                                    },
                                    'customer_email': {
                                        'type': ['string', 'null'],
                                    },
                                    'timezone': {
                                        'type': ['string', 'null'],
                                    },
                                    'iana_timezone': {
                                        'type': ['string', 'null'],
                                    },
                                    'shop_owner': {
                                        'type': ['string', 'null'],
                                    },
                                    'money_format': {
                                        'type': ['string', 'null'],
                                    },
                                    'money_with_currency_format': {
                                        'type': ['string', 'null'],
                                    },
                                    'weight_unit': {
                                        'type': ['string', 'null'],
                                    },
                                    'province_code': {
                                        'type': ['string', 'null'],
                                    },
                                    'taxes_included': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'auto_configure_tax_inclusivity': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'tax_shipping': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'county_taxes': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'plan_display_name': {
                                        'type': ['string', 'null'],
                                    },
                                    'plan_name': {
                                        'type': ['string', 'null'],
                                    },
                                    'has_discounts': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'has_gift_cards': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'myshopify_domain': {
                                        'type': ['string', 'null'],
                                    },
                                    'google_apps_domain': {
                                        'type': ['string', 'null'],
                                    },
                                    'google_apps_login_enabled': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'money_in_emails_format': {
                                        'type': ['string', 'null'],
                                    },
                                    'money_with_currency_in_emails_format': {
                                        'type': ['string', 'null'],
                                    },
                                    'eligible_for_payments': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'requires_extra_payments_agreement': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'password_enabled': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'has_storefront': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'finances': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'primary_location_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'checkout_api_supported': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'multi_location_enabled': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'setup_required': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'pre_launch_enabled': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'enabled_presentment_currencies': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                    },
                                    'transactional_sms_disabled': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'marketing_sms_consent_enabled_at_checkout': {
                                        'type': ['boolean', 'null'],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'shop',
                                'x-airbyte-stream-name': 'shop',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Shopify store configuration and account details',
                                    'when_to_use': 'Questions about store settings or account information',
                                    'trigger_phrases': ['shopify shop', 'store settings', 'shop details'],
                                    'freshness': 'static',
                                    'example_questions': ['Show Shopify store details'],
                                    'search_strategy': 'Retrieve store info',
                                },
                            },
                        },
                    },
                    record_extractor='$.shop',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Shop configuration',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Shop ID'},
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'email': {
                        'type': ['string', 'null'],
                    },
                    'domain': {
                        'type': ['string', 'null'],
                    },
                    'province': {
                        'type': ['string', 'null'],
                    },
                    'country': {
                        'type': ['string', 'null'],
                    },
                    'address1': {
                        'type': ['string', 'null'],
                    },
                    'zip': {
                        'type': ['string', 'null'],
                    },
                    'city': {
                        'type': ['string', 'null'],
                    },
                    'source': {
                        'type': ['string', 'null'],
                    },
                    'phone': {
                        'type': ['string', 'null'],
                    },
                    'latitude': {
                        'type': ['number', 'null'],
                    },
                    'longitude': {
                        'type': ['number', 'null'],
                    },
                    'primary_locale': {
                        'type': ['string', 'null'],
                    },
                    'address2': {
                        'type': ['string', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'country_code': {
                        'type': ['string', 'null'],
                    },
                    'country_name': {
                        'type': ['string', 'null'],
                    },
                    'currency': {
                        'type': ['string', 'null'],
                    },
                    'customer_email': {
                        'type': ['string', 'null'],
                    },
                    'timezone': {
                        'type': ['string', 'null'],
                    },
                    'iana_timezone': {
                        'type': ['string', 'null'],
                    },
                    'shop_owner': {
                        'type': ['string', 'null'],
                    },
                    'money_format': {
                        'type': ['string', 'null'],
                    },
                    'money_with_currency_format': {
                        'type': ['string', 'null'],
                    },
                    'weight_unit': {
                        'type': ['string', 'null'],
                    },
                    'province_code': {
                        'type': ['string', 'null'],
                    },
                    'taxes_included': {
                        'type': ['boolean', 'null'],
                    },
                    'auto_configure_tax_inclusivity': {
                        'type': ['boolean', 'null'],
                    },
                    'tax_shipping': {
                        'type': ['boolean', 'null'],
                    },
                    'county_taxes': {
                        'type': ['boolean', 'null'],
                    },
                    'plan_display_name': {
                        'type': ['string', 'null'],
                    },
                    'plan_name': {
                        'type': ['string', 'null'],
                    },
                    'has_discounts': {
                        'type': ['boolean', 'null'],
                    },
                    'has_gift_cards': {
                        'type': ['boolean', 'null'],
                    },
                    'myshopify_domain': {
                        'type': ['string', 'null'],
                    },
                    'google_apps_domain': {
                        'type': ['string', 'null'],
                    },
                    'google_apps_login_enabled': {
                        'type': ['boolean', 'null'],
                    },
                    'money_in_emails_format': {
                        'type': ['string', 'null'],
                    },
                    'money_with_currency_in_emails_format': {
                        'type': ['string', 'null'],
                    },
                    'eligible_for_payments': {
                        'type': ['boolean', 'null'],
                    },
                    'requires_extra_payments_agreement': {
                        'type': ['boolean', 'null'],
                    },
                    'password_enabled': {
                        'type': ['boolean', 'null'],
                    },
                    'has_storefront': {
                        'type': ['boolean', 'null'],
                    },
                    'finances': {
                        'type': ['boolean', 'null'],
                    },
                    'primary_location_id': {
                        'type': ['integer', 'null'],
                    },
                    'checkout_api_supported': {
                        'type': ['boolean', 'null'],
                    },
                    'multi_location_enabled': {
                        'type': ['boolean', 'null'],
                    },
                    'setup_required': {
                        'type': ['boolean', 'null'],
                    },
                    'pre_launch_enabled': {
                        'type': ['boolean', 'null'],
                    },
                    'enabled_presentment_currencies': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                    },
                    'transactional_sms_disabled': {
                        'type': ['boolean', 'null'],
                    },
                    'marketing_sms_consent_enabled_at_checkout': {
                        'type': ['boolean', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'shop',
                'x-airbyte-stream-name': 'shop',
                'x-airbyte-ai-hints': {
                    'summary': 'Shopify store configuration and account details',
                    'when_to_use': 'Questions about store settings or account information',
                    'trigger_phrases': ['shopify shop', 'store settings', 'shop details'],
                    'freshness': 'static',
                    'example_questions': ['Show Shopify store details'],
                    'search_strategy': 'Retrieve store info',
                },
            },
            ai_hints={
                'summary': 'Shopify store configuration and account details',
                'when_to_use': 'Questions about store settings or account information',
                'trigger_phrases': ['shopify shop', 'store settings', 'shop details'],
                'freshness': 'static',
                'example_questions': ['Show Shopify store details'],
                'search_strategy': 'Retrieve store info',
            },
        ),
        EntityDefinition(
            name='price_rules',
            stream_name='price_rules',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/price_rules.json',
                    action=Action.LIST,
                    description='Returns a list of price rules',
                    query_params=[
                        'limit',
                        'since_id',
                        'created_at_min',
                        'created_at_max',
                        'updated_at_min',
                        'updated_at_max',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'created_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'price_rules': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A price rule',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Price rule ID'},
                                        'value_type': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': ['string', 'null'],
                                        },
                                        'customer_selection': {
                                            'type': ['string', 'null'],
                                        },
                                        'target_type': {
                                            'type': ['string', 'null'],
                                        },
                                        'target_selection': {
                                            'type': ['string', 'null'],
                                        },
                                        'allocation_method': {
                                            'type': ['string', 'null'],
                                        },
                                        'allocation_limit': {
                                            'type': ['integer', 'null'],
                                        },
                                        'once_per_customer': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'usage_limit': {
                                            'type': ['integer', 'null'],
                                        },
                                        'starts_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'ends_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'entitled_product_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'entitled_variant_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'entitled_collection_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'entitled_country_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'prerequisite_product_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'prerequisite_variant_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'prerequisite_collection_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'customer_segment_prerequisite_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'prerequisite_customer_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'prerequisite_subtotal_range': {
                                            'type': ['object', 'null'],
                                        },
                                        'prerequisite_quantity_range': {
                                            'type': ['object', 'null'],
                                        },
                                        'prerequisite_shipping_price_range': {
                                            'type': ['object', 'null'],
                                        },
                                        'prerequisite_to_entitlement_quantity_ratio': {
                                            'type': ['object', 'null'],
                                        },
                                        'prerequisite_to_entitlement_purchase': {
                                            'type': ['object', 'null'],
                                        },
                                        'title': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'price_rules',
                                    'x-airbyte-stream-name': 'price_rules',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Discount price rules for Shopify promotions',
                                        'when_to_use': 'Questions about discount rules or promotion configuration',
                                        'trigger_phrases': ['price rule', 'discount rule', 'promotion'],
                                        'freshness': 'live',
                                        'example_questions': ['What price rules are active?'],
                                        'search_strategy': 'List all price rules',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.price_rules',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/price_rules/{price_rule_id}.json',
                    action=Action.GET,
                    description='Retrieves a single price rule by ID',
                    path_params=['price_rule_id'],
                    path_params_schema={
                        'price_rule_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'price_rule': {
                                'type': 'object',
                                'description': 'A price rule',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Price rule ID'},
                                    'value_type': {
                                        'type': ['string', 'null'],
                                    },
                                    'value': {
                                        'type': ['string', 'null'],
                                    },
                                    'customer_selection': {
                                        'type': ['string', 'null'],
                                    },
                                    'target_type': {
                                        'type': ['string', 'null'],
                                    },
                                    'target_selection': {
                                        'type': ['string', 'null'],
                                    },
                                    'allocation_method': {
                                        'type': ['string', 'null'],
                                    },
                                    'allocation_limit': {
                                        'type': ['integer', 'null'],
                                    },
                                    'once_per_customer': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'usage_limit': {
                                        'type': ['integer', 'null'],
                                    },
                                    'starts_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'ends_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'entitled_product_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'integer'},
                                    },
                                    'entitled_variant_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'integer'},
                                    },
                                    'entitled_collection_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'integer'},
                                    },
                                    'entitled_country_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'integer'},
                                    },
                                    'prerequisite_product_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'integer'},
                                    },
                                    'prerequisite_variant_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'integer'},
                                    },
                                    'prerequisite_collection_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'integer'},
                                    },
                                    'customer_segment_prerequisite_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'integer'},
                                    },
                                    'prerequisite_customer_ids': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'integer'},
                                    },
                                    'prerequisite_subtotal_range': {
                                        'type': ['object', 'null'],
                                    },
                                    'prerequisite_quantity_range': {
                                        'type': ['object', 'null'],
                                    },
                                    'prerequisite_shipping_price_range': {
                                        'type': ['object', 'null'],
                                    },
                                    'prerequisite_to_entitlement_quantity_ratio': {
                                        'type': ['object', 'null'],
                                    },
                                    'prerequisite_to_entitlement_purchase': {
                                        'type': ['object', 'null'],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'price_rules',
                                'x-airbyte-stream-name': 'price_rules',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Discount price rules for Shopify promotions',
                                    'when_to_use': 'Questions about discount rules or promotion configuration',
                                    'trigger_phrases': ['price rule', 'discount rule', 'promotion'],
                                    'freshness': 'live',
                                    'example_questions': ['What price rules are active?'],
                                    'search_strategy': 'List all price rules',
                                },
                            },
                        },
                    },
                    record_extractor='$.price_rule',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A price rule',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Price rule ID'},
                    'value_type': {
                        'type': ['string', 'null'],
                    },
                    'value': {
                        'type': ['string', 'null'],
                    },
                    'customer_selection': {
                        'type': ['string', 'null'],
                    },
                    'target_type': {
                        'type': ['string', 'null'],
                    },
                    'target_selection': {
                        'type': ['string', 'null'],
                    },
                    'allocation_method': {
                        'type': ['string', 'null'],
                    },
                    'allocation_limit': {
                        'type': ['integer', 'null'],
                    },
                    'once_per_customer': {
                        'type': ['boolean', 'null'],
                    },
                    'usage_limit': {
                        'type': ['integer', 'null'],
                    },
                    'starts_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'ends_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'entitled_product_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'entitled_variant_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'entitled_collection_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'entitled_country_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'prerequisite_product_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'prerequisite_variant_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'prerequisite_collection_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'customer_segment_prerequisite_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'prerequisite_customer_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'prerequisite_subtotal_range': {
                        'type': ['object', 'null'],
                    },
                    'prerequisite_quantity_range': {
                        'type': ['object', 'null'],
                    },
                    'prerequisite_shipping_price_range': {
                        'type': ['object', 'null'],
                    },
                    'prerequisite_to_entitlement_quantity_ratio': {
                        'type': ['object', 'null'],
                    },
                    'prerequisite_to_entitlement_purchase': {
                        'type': ['object', 'null'],
                    },
                    'title': {
                        'type': ['string', 'null'],
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'price_rules',
                'x-airbyte-stream-name': 'price_rules',
                'x-airbyte-ai-hints': {
                    'summary': 'Discount price rules for Shopify promotions',
                    'when_to_use': 'Questions about discount rules or promotion configuration',
                    'trigger_phrases': ['price rule', 'discount rule', 'promotion'],
                    'freshness': 'live',
                    'example_questions': ['What price rules are active?'],
                    'search_strategy': 'List all price rules',
                },
            },
            ai_hints={
                'summary': 'Discount price rules for Shopify promotions',
                'when_to_use': 'Questions about discount rules or promotion configuration',
                'trigger_phrases': ['price rule', 'discount rule', 'promotion'],
                'freshness': 'live',
                'example_questions': ['What price rules are active?'],
                'search_strategy': 'List all price rules',
            },
        ),
        EntityDefinition(
            name='discount_codes',
            stream_name='discount_codes',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/price_rules/{price_rule_id}/discount_codes.json',
                    action=Action.LIST,
                    description='Returns a list of discount codes for a price rule',
                    query_params=['limit'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                    },
                    path_params=['price_rule_id'],
                    path_params_schema={
                        'price_rule_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'discount_codes': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A discount code',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Discount code ID'},
                                        'price_rule_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'code': {
                                            'type': ['string', 'null'],
                                        },
                                        'usage_count': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'discount_codes',
                                    'x-airbyte-stream-name': 'discount_codes',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Discount codes associated with Shopify price rules',
                                        'when_to_use': 'Questions about available discount codes',
                                        'trigger_phrases': ['discount code', 'promo code', 'coupon code'],
                                        'freshness': 'live',
                                        'example_questions': ['What discount codes are available?'],
                                        'search_strategy': 'Filter by price rule or search by code',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.discount_codes',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json',
                    action=Action.GET,
                    description='Retrieves a single discount code by ID',
                    path_params=['price_rule_id', 'discount_code_id'],
                    path_params_schema={
                        'price_rule_id': {'type': 'integer', 'required': True},
                        'discount_code_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'discount_code': {
                                'type': 'object',
                                'description': 'A discount code',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Discount code ID'},
                                    'price_rule_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'code': {
                                        'type': ['string', 'null'],
                                    },
                                    'usage_count': {
                                        'type': ['integer', 'null'],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'discount_codes',
                                'x-airbyte-stream-name': 'discount_codes',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Discount codes associated with Shopify price rules',
                                    'when_to_use': 'Questions about available discount codes',
                                    'trigger_phrases': ['discount code', 'promo code', 'coupon code'],
                                    'freshness': 'live',
                                    'example_questions': ['What discount codes are available?'],
                                    'search_strategy': 'Filter by price rule or search by code',
                                },
                            },
                        },
                    },
                    record_extractor='$.discount_code',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A discount code',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Discount code ID'},
                    'price_rule_id': {
                        'type': ['integer', 'null'],
                    },
                    'code': {
                        'type': ['string', 'null'],
                    },
                    'usage_count': {
                        'type': ['integer', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'discount_codes',
                'x-airbyte-stream-name': 'discount_codes',
                'x-airbyte-ai-hints': {
                    'summary': 'Discount codes associated with Shopify price rules',
                    'when_to_use': 'Questions about available discount codes',
                    'trigger_phrases': ['discount code', 'promo code', 'coupon code'],
                    'freshness': 'live',
                    'example_questions': ['What discount codes are available?'],
                    'search_strategy': 'Filter by price rule or search by code',
                },
            },
            ai_hints={
                'summary': 'Discount codes associated with Shopify price rules',
                'when_to_use': 'Questions about available discount codes',
                'trigger_phrases': ['discount code', 'promo code', 'coupon code'],
                'freshness': 'live',
                'example_questions': ['What discount codes are available?'],
                'search_strategy': 'Filter by price rule or search by code',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='discount_codes',
                    target_entity='price_rules',
                    foreign_key='price_rule_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='custom_collections',
            stream_name='custom_collections',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/custom_collections.json',
                    action=Action.LIST,
                    description='Returns a list of custom collections',
                    query_params=[
                        'limit',
                        'since_id',
                        'title',
                        'product_id',
                        'updated_at_min',
                        'updated_at_max',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'title': {'type': 'string', 'required': False},
                        'product_id': {'type': 'integer', 'required': False},
                        'updated_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'custom_collections': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A custom collection',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Collection ID'},
                                        'handle': {
                                            'type': ['string', 'null'],
                                        },
                                        'title': {
                                            'type': ['string', 'null'],
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'body_html': {
                                            'type': ['string', 'null'],
                                        },
                                        'published_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'sort_order': {
                                            'type': ['string', 'null'],
                                        },
                                        'template_suffix': {
                                            'type': ['string', 'null'],
                                        },
                                        'published_scope': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'image': {
                                            'type': ['object', 'null'],
                                        },
                                        'products_count': {
                                            'type': ['integer', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'custom_collections',
                                    'x-airbyte-stream-name': 'custom_collections',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Manually curated product collections in Shopify',
                                        'when_to_use': 'Questions about product collections or curated groupings',
                                        'trigger_phrases': ['custom collection', 'product collection'],
                                        'freshness': 'live',
                                        'example_questions': ['What custom collections exist?'],
                                        'search_strategy': 'Search by title',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.custom_collections',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/custom_collections/{collection_id}.json',
                    action=Action.GET,
                    description='Retrieves a single custom collection by ID',
                    path_params=['collection_id'],
                    path_params_schema={
                        'collection_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'custom_collection': {
                                'type': 'object',
                                'description': 'A custom collection',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Collection ID'},
                                    'handle': {
                                        'type': ['string', 'null'],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                    },
                                    'published_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'sort_order': {
                                        'type': ['string', 'null'],
                                    },
                                    'template_suffix': {
                                        'type': ['string', 'null'],
                                    },
                                    'published_scope': {
                                        'type': ['string', 'null'],
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'image': {
                                        'type': ['object', 'null'],
                                    },
                                    'products_count': {
                                        'type': ['integer', 'null'],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'custom_collections',
                                'x-airbyte-stream-name': 'custom_collections',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Manually curated product collections in Shopify',
                                    'when_to_use': 'Questions about product collections or curated groupings',
                                    'trigger_phrases': ['custom collection', 'product collection'],
                                    'freshness': 'live',
                                    'example_questions': ['What custom collections exist?'],
                                    'search_strategy': 'Search by title',
                                },
                            },
                        },
                    },
                    record_extractor='$.custom_collection',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A custom collection',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Collection ID'},
                    'handle': {
                        'type': ['string', 'null'],
                    },
                    'title': {
                        'type': ['string', 'null'],
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'body_html': {
                        'type': ['string', 'null'],
                    },
                    'published_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'sort_order': {
                        'type': ['string', 'null'],
                    },
                    'template_suffix': {
                        'type': ['string', 'null'],
                    },
                    'published_scope': {
                        'type': ['string', 'null'],
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                    'image': {
                        'type': ['object', 'null'],
                    },
                    'products_count': {
                        'type': ['integer', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'custom_collections',
                'x-airbyte-stream-name': 'custom_collections',
                'x-airbyte-ai-hints': {
                    'summary': 'Manually curated product collections in Shopify',
                    'when_to_use': 'Questions about product collections or curated groupings',
                    'trigger_phrases': ['custom collection', 'product collection'],
                    'freshness': 'live',
                    'example_questions': ['What custom collections exist?'],
                    'search_strategy': 'Search by title',
                },
            },
            ai_hints={
                'summary': 'Manually curated product collections in Shopify',
                'when_to_use': 'Questions about product collections or curated groupings',
                'trigger_phrases': ['custom collection', 'product collection'],
                'freshness': 'live',
                'example_questions': ['What custom collections exist?'],
                'search_strategy': 'Search by title',
            },
        ),
        EntityDefinition(
            name='smart_collections',
            stream_name='smart_collections',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/smart_collections.json',
                    action=Action.LIST,
                    description='Returns a list of smart collections',
                    query_params=[
                        'limit',
                        'since_id',
                        'title',
                        'product_id',
                        'updated_at_min',
                        'updated_at_max',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'title': {'type': 'string', 'required': False},
                        'product_id': {'type': 'integer', 'required': False},
                        'updated_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'smart_collections': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A smart collection',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Collection ID'},
                                        'handle': {
                                            'type': ['string', 'null'],
                                        },
                                        'title': {
                                            'type': ['string', 'null'],
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'body_html': {
                                            'type': ['string', 'null'],
                                        },
                                        'published_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'sort_order': {
                                            'type': ['string', 'null'],
                                        },
                                        'template_suffix': {
                                            'type': ['string', 'null'],
                                        },
                                        'disjunctive': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'rules': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'published_scope': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'image': {
                                            'type': ['object', 'null'],
                                        },
                                        'products_count': {
                                            'type': ['integer', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'smart_collections',
                                    'x-airbyte-stream-name': 'smart_collections',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Automated product collections based on rules in Shopify',
                                        'when_to_use': 'Questions about automated collections or rule-based groupings',
                                        'trigger_phrases': ['smart collection', 'automated collection'],
                                        'freshness': 'live',
                                        'example_questions': ['What smart collections exist?'],
                                        'search_strategy': 'Search by title',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.smart_collections',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/smart_collections/{collection_id}.json',
                    action=Action.GET,
                    description='Retrieves a single smart collection by ID',
                    path_params=['collection_id'],
                    path_params_schema={
                        'collection_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'smart_collection': {
                                'type': 'object',
                                'description': 'A smart collection',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Collection ID'},
                                    'handle': {
                                        'type': ['string', 'null'],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                    },
                                    'published_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'sort_order': {
                                        'type': ['string', 'null'],
                                    },
                                    'template_suffix': {
                                        'type': ['string', 'null'],
                                    },
                                    'disjunctive': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'rules': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'published_scope': {
                                        'type': ['string', 'null'],
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'image': {
                                        'type': ['object', 'null'],
                                    },
                                    'products_count': {
                                        'type': ['integer', 'null'],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'smart_collections',
                                'x-airbyte-stream-name': 'smart_collections',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Automated product collections based on rules in Shopify',
                                    'when_to_use': 'Questions about automated collections or rule-based groupings',
                                    'trigger_phrases': ['smart collection', 'automated collection'],
                                    'freshness': 'live',
                                    'example_questions': ['What smart collections exist?'],
                                    'search_strategy': 'Search by title',
                                },
                            },
                        },
                    },
                    record_extractor='$.smart_collection',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A smart collection',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Collection ID'},
                    'handle': {
                        'type': ['string', 'null'],
                    },
                    'title': {
                        'type': ['string', 'null'],
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'body_html': {
                        'type': ['string', 'null'],
                    },
                    'published_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'sort_order': {
                        'type': ['string', 'null'],
                    },
                    'template_suffix': {
                        'type': ['string', 'null'],
                    },
                    'disjunctive': {
                        'type': ['boolean', 'null'],
                    },
                    'rules': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'published_scope': {
                        'type': ['string', 'null'],
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                    'image': {
                        'type': ['object', 'null'],
                    },
                    'products_count': {
                        'type': ['integer', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'smart_collections',
                'x-airbyte-stream-name': 'smart_collections',
                'x-airbyte-ai-hints': {
                    'summary': 'Automated product collections based on rules in Shopify',
                    'when_to_use': 'Questions about automated collections or rule-based groupings',
                    'trigger_phrases': ['smart collection', 'automated collection'],
                    'freshness': 'live',
                    'example_questions': ['What smart collections exist?'],
                    'search_strategy': 'Search by title',
                },
            },
            ai_hints={
                'summary': 'Automated product collections based on rules in Shopify',
                'when_to_use': 'Questions about automated collections or rule-based groupings',
                'trigger_phrases': ['smart collection', 'automated collection'],
                'freshness': 'live',
                'example_questions': ['What smart collections exist?'],
                'search_strategy': 'Search by title',
            },
        ),
        EntityDefinition(
            name='collects',
            stream_name='collects',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/collects.json',
                    action=Action.LIST,
                    description='Returns a list of collects (links between products and collections)',
                    query_params=[
                        'limit',
                        'since_id',
                        'collection_id',
                        'product_id',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'collection_id': {'type': 'integer', 'required': False},
                        'product_id': {'type': 'integer', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'collects': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A collect (product-collection link)',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Collect ID'},
                                        'collection_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'product_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'position': {
                                            'type': ['integer', 'null'],
                                        },
                                        'sort_value': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'collects',
                                    'x-airbyte-stream-name': 'collects',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Links between products and collections in Shopify',
                                        'when_to_use': 'Questions about which products are in which collections',
                                        'trigger_phrases': ['product in collection', 'collection membership'],
                                        'freshness': 'live',
                                        'example_questions': ['What products are in a collection?'],
                                        'search_strategy': 'Filter by collection or product',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.collects',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/collects/{collect_id}.json',
                    action=Action.GET,
                    description='Retrieves a single collect by ID',
                    path_params=['collect_id'],
                    path_params_schema={
                        'collect_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'collect': {
                                'type': 'object',
                                'description': 'A collect (product-collection link)',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Collect ID'},
                                    'collection_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'product_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'position': {
                                        'type': ['integer', 'null'],
                                    },
                                    'sort_value': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'collects',
                                'x-airbyte-stream-name': 'collects',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Links between products and collections in Shopify',
                                    'when_to_use': 'Questions about which products are in which collections',
                                    'trigger_phrases': ['product in collection', 'collection membership'],
                                    'freshness': 'live',
                                    'example_questions': ['What products are in a collection?'],
                                    'search_strategy': 'Filter by collection or product',
                                },
                            },
                        },
                    },
                    record_extractor='$.collect',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A collect (product-collection link)',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Collect ID'},
                    'collection_id': {
                        'type': ['integer', 'null'],
                    },
                    'product_id': {
                        'type': ['integer', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'position': {
                        'type': ['integer', 'null'],
                    },
                    'sort_value': {
                        'type': ['string', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'collects',
                'x-airbyte-stream-name': 'collects',
                'x-airbyte-ai-hints': {
                    'summary': 'Links between products and collections in Shopify',
                    'when_to_use': 'Questions about which products are in which collections',
                    'trigger_phrases': ['product in collection', 'collection membership'],
                    'freshness': 'live',
                    'example_questions': ['What products are in a collection?'],
                    'search_strategy': 'Filter by collection or product',
                },
            },
            ai_hints={
                'summary': 'Links between products and collections in Shopify',
                'when_to_use': 'Questions about which products are in which collections',
                'trigger_phrases': ['product in collection', 'collection membership'],
                'freshness': 'live',
                'example_questions': ['What products are in a collection?'],
                'search_strategy': 'Filter by collection or product',
            },
        ),
        EntityDefinition(
            name='draft_orders',
            stream_name='draft_orders',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/draft_orders.json',
                    action=Action.LIST,
                    description='Returns a list of draft orders',
                    query_params=[
                        'limit',
                        'since_id',
                        'status',
                        'updated_at_min',
                        'updated_at_max',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'status': {
                            'type': 'string',
                            'required': False,
                            'enum': ['open', 'invoice_sent', 'completed'],
                        },
                        'updated_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'draft_orders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A draft order',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Draft order ID'},
                                        'note': {
                                            'type': ['string', 'null'],
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                        },
                                        'taxes_included': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'currency': {
                                            'type': ['string', 'null'],
                                        },
                                        'invoice_sent_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'tax_exempt': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'completed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                        },
                                        'line_items': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'integer'},
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'attributed_staffs': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'current_quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'fulfillable_quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'fulfillment_service': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'fulfillment_status': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'gift_card': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'grams': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'price': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'price_set': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'product_exists': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'product_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'properties': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'requires_shipping': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'sku': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'taxable': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'total_discount': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'total_discount_set': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'variant_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'variant_inventory_management': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'variant_title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'vendor': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'tax_lines': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'duties': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'discount_allocations': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                },
                                            },
                                        },
                                        'shipping_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'An address in an order (shipping or billing) - does not have id field',
                                                    'properties': {
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'company': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address1': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address2': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'zip': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province_code': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country_code': {
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
                                                {'type': 'null'},
                                            ],
                                        },
                                        'billing_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'An address in an order (shipping or billing) - does not have id field',
                                                    'properties': {
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'company': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address1': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'address2': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'zip': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'province_code': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country_code': {
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
                                                {'type': 'null'},
                                            ],
                                        },
                                        'invoice_url': {
                                            'type': ['string', 'null'],
                                        },
                                        'applied_discount': {
                                            'type': ['object', 'null'],
                                        },
                                        'order_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'shipping_line': {
                                            'type': ['object', 'null'],
                                        },
                                        'tax_lines': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'tags': {
                                            'type': ['string', 'null'],
                                        },
                                        'note_attributes': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'total_price': {
                                            'type': ['string', 'null'],
                                        },
                                        'subtotal_price': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_tax': {
                                            'type': ['string', 'null'],
                                        },
                                        'payment_terms': {
                                            'type': ['object', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'customer': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'A Shopify customer',
                                                    'properties': {
                                                        'id': {'type': 'integer', 'description': 'Unique customer identifier'},
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer email address',
                                                        },
                                                        'accepts_marketing': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the customer accepts marketing',
                                                        },
                                                        'created_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When the customer was created',
                                                        },
                                                        'updated_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When the customer was last updated',
                                                        },
                                                        'first_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer first name',
                                                        },
                                                        'last_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer last name',
                                                        },
                                                        'orders_count': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Number of orders',
                                                        },
                                                        'state': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer state',
                                                        },
                                                        'total_spent': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Total amount spent',
                                                        },
                                                        'last_order_id': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'ID of last order',
                                                        },
                                                        'note': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Note about the customer',
                                                        },
                                                        'verified_email': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether email is verified',
                                                        },
                                                        'multipass_identifier': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Multipass identifier',
                                                        },
                                                        'tax_exempt': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether customer is tax exempt',
                                                        },
                                                        'tags': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Tags associated with customer',
                                                        },
                                                        'last_order_name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Name of last order',
                                                        },
                                                        'currency': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer currency',
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Customer phone number',
                                                        },
                                                        'addresses': {
                                                            'type': ['array', 'null'],
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'A customer address',
                                                                'properties': {
                                                                    'id': {'type': 'integer', 'description': 'Address ID'},
                                                                    'customer_id': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Customer ID',
                                                                    },
                                                                    'first_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'First name',
                                                                    },
                                                                    'last_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Last name',
                                                                    },
                                                                    'company': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Company name',
                                                                    },
                                                                    'address1': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Address line 1',
                                                                    },
                                                                    'address2': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Address line 2',
                                                                    },
                                                                    'city': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'City',
                                                                    },
                                                                    'province': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Province/State',
                                                                    },
                                                                    'country': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country',
                                                                    },
                                                                    'zip': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'ZIP/Postal code',
                                                                    },
                                                                    'phone': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Phone number',
                                                                    },
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Full name',
                                                                    },
                                                                    'province_code': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Province code',
                                                                    },
                                                                    'country_code': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country code',
                                                                    },
                                                                    'country_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country name',
                                                                    },
                                                                    'default': {
                                                                        'type': ['boolean', 'null'],
                                                                        'description': 'Whether this is the default address',
                                                                    },
                                                                },
                                                                'required': ['id'],
                                                            },
                                                        },
                                                        'accepts_marketing_updated_at': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'When marketing acceptance was updated',
                                                        },
                                                        'marketing_opt_in_level': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Marketing opt-in level',
                                                        },
                                                        'tax_exemptions': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'string'},
                                                        },
                                                        'email_marketing_consent': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'state': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'opt_in_level': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'consent_updated_at': {
                                                                            'type': ['string', 'null'],
                                                                            'format': 'date-time',
                                                                        },
                                                                        'consent_collected_from': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'sms_marketing_consent': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'state': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'opt_in_level': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'consent_updated_at': {
                                                                            'type': ['string', 'null'],
                                                                            'format': 'date-time',
                                                                        },
                                                                        'consent_collected_from': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'admin_graphql_api_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'GraphQL API ID',
                                                        },
                                                        'default_address': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'A customer address',
                                                                    'properties': {
                                                                        'id': {'type': 'integer', 'description': 'Address ID'},
                                                                        'customer_id': {
                                                                            'type': ['integer', 'null'],
                                                                            'description': 'Customer ID',
                                                                        },
                                                                        'first_name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'First name',
                                                                        },
                                                                        'last_name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Last name',
                                                                        },
                                                                        'company': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Company name',
                                                                        },
                                                                        'address1': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Address line 1',
                                                                        },
                                                                        'address2': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Address line 2',
                                                                        },
                                                                        'city': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'City',
                                                                        },
                                                                        'province': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Province/State',
                                                                        },
                                                                        'country': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Country',
                                                                        },
                                                                        'zip': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'ZIP/Postal code',
                                                                        },
                                                                        'phone': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Phone number',
                                                                        },
                                                                        'name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Full name',
                                                                        },
                                                                        'province_code': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Province code',
                                                                        },
                                                                        'country_code': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Country code',
                                                                        },
                                                                        'country_name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Country name',
                                                                        },
                                                                        'default': {
                                                                            'type': ['boolean', 'null'],
                                                                            'description': 'Whether this is the default address',
                                                                        },
                                                                    },
                                                                    'required': ['id'],
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                    },
                                                    'required': ['id'],
                                                    'x-airbyte-entity-name': 'customers',
                                                    'x-airbyte-stream-name': 'customers',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Shopify customers with order history and contact information',
                                                        'when_to_use': 'Looking up customer details or purchase history',
                                                        'trigger_phrases': ['shopify customer', 'buyer', 'customer info'],
                                                        'freshness': 'live',
                                                        'example_questions': ['Find a customer in Shopify', 'Show customer order history'],
                                                        'search_strategy': 'Search by email, name, or phone',
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'allow_discount_codes_in_checkout?': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether discount codes can be applied at checkout',
                                        },
                                        'b2b?': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this is a B2B order',
                                        },
                                        'api_client_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'The ID of the API client that created the draft order',
                                        },
                                        'created_on_api_version_handle': {
                                            'type': ['string', 'null'],
                                            'description': 'The API version handle when the draft order was created',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'draft_orders',
                                    'x-airbyte-stream-name': 'draft_orders',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Draft orders created manually in Shopify admin',
                                        'when_to_use': 'Questions about draft orders or manually created orders',
                                        'trigger_phrases': ['draft order', 'manual order'],
                                        'freshness': 'live',
                                        'example_questions': ['Show draft orders'],
                                        'search_strategy': 'Filter by status or date',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.draft_orders',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/draft_orders/{draft_order_id}.json',
                    action=Action.GET,
                    description='Retrieves a single draft order by ID',
                    path_params=['draft_order_id'],
                    path_params_schema={
                        'draft_order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'draft_order': {
                                'type': 'object',
                                'description': 'A draft order',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Draft order ID'},
                                    'note': {
                                        'type': ['string', 'null'],
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                    },
                                    'taxes_included': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'currency': {
                                        'type': ['string', 'null'],
                                    },
                                    'invoice_sent_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'tax_exempt': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'completed_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                    },
                                    'line_items': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'integer'},
                                                'admin_graphql_api_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'attributed_staffs': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'current_quantity': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'fulfillable_quantity': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'fulfillment_service': {
                                                    'type': ['string', 'null'],
                                                },
                                                'fulfillment_status': {
                                                    'type': ['string', 'null'],
                                                },
                                                'gift_card': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'grams': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'name': {
                                                    'type': ['string', 'null'],
                                                },
                                                'price': {
                                                    'type': ['string', 'null'],
                                                },
                                                'price_set': {
                                                    'type': ['object', 'null'],
                                                },
                                                'product_exists': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'product_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'properties': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'quantity': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'requires_shipping': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'sku': {
                                                    'type': ['string', 'null'],
                                                },
                                                'taxable': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'title': {
                                                    'type': ['string', 'null'],
                                                },
                                                'total_discount': {
                                                    'type': ['string', 'null'],
                                                },
                                                'total_discount_set': {
                                                    'type': ['object', 'null'],
                                                },
                                                'variant_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'variant_inventory_management': {
                                                    'type': ['string', 'null'],
                                                },
                                                'variant_title': {
                                                    'type': ['string', 'null'],
                                                },
                                                'vendor': {
                                                    'type': ['string', 'null'],
                                                },
                                                'tax_lines': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'duties': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'discount_allocations': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                            },
                                        },
                                    },
                                    'shipping_address': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'An address in an order (shipping or billing) - does not have id field',
                                                'properties': {
                                                    'first_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'last_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'company': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'address1': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'address2': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'city': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'province': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'country': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'zip': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'phone': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'province_code': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'country_code': {
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
                                            {'type': 'null'},
                                        ],
                                    },
                                    'billing_address': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'An address in an order (shipping or billing) - does not have id field',
                                                'properties': {
                                                    'first_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'last_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'company': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'address1': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'address2': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'city': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'province': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'country': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'zip': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'phone': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'province_code': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'country_code': {
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
                                            {'type': 'null'},
                                        ],
                                    },
                                    'invoice_url': {
                                        'type': ['string', 'null'],
                                    },
                                    'applied_discount': {
                                        'type': ['object', 'null'],
                                    },
                                    'order_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'shipping_line': {
                                        'type': ['object', 'null'],
                                    },
                                    'tax_lines': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'tags': {
                                        'type': ['string', 'null'],
                                    },
                                    'note_attributes': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'total_price': {
                                        'type': ['string', 'null'],
                                    },
                                    'subtotal_price': {
                                        'type': ['string', 'null'],
                                    },
                                    'total_tax': {
                                        'type': ['string', 'null'],
                                    },
                                    'payment_terms': {
                                        'type': ['object', 'null'],
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'customer': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'description': 'A Shopify customer',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Unique customer identifier'},
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer email address',
                                                    },
                                                    'accepts_marketing': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the customer accepts marketing',
                                                    },
                                                    'created_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When the customer was created',
                                                    },
                                                    'updated_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When the customer was last updated',
                                                    },
                                                    'first_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer first name',
                                                    },
                                                    'last_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer last name',
                                                    },
                                                    'orders_count': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Number of orders',
                                                    },
                                                    'state': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer state',
                                                    },
                                                    'total_spent': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Total amount spent',
                                                    },
                                                    'last_order_id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'ID of last order',
                                                    },
                                                    'note': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Note about the customer',
                                                    },
                                                    'verified_email': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether email is verified',
                                                    },
                                                    'multipass_identifier': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Multipass identifier',
                                                    },
                                                    'tax_exempt': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether customer is tax exempt',
                                                    },
                                                    'tags': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Tags associated with customer',
                                                    },
                                                    'last_order_name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Name of last order',
                                                    },
                                                    'currency': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer currency',
                                                    },
                                                    'phone': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Customer phone number',
                                                    },
                                                    'addresses': {
                                                        'type': ['array', 'null'],
                                                        'items': {
                                                            'type': 'object',
                                                            'description': 'A customer address',
                                                            'properties': {
                                                                'id': {'type': 'integer', 'description': 'Address ID'},
                                                                'customer_id': {
                                                                    'type': ['integer', 'null'],
                                                                    'description': 'Customer ID',
                                                                },
                                                                'first_name': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'First name',
                                                                },
                                                                'last_name': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Last name',
                                                                },
                                                                'company': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Company name',
                                                                },
                                                                'address1': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Address line 1',
                                                                },
                                                                'address2': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Address line 2',
                                                                },
                                                                'city': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'City',
                                                                },
                                                                'province': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Province/State',
                                                                },
                                                                'country': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Country',
                                                                },
                                                                'zip': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'ZIP/Postal code',
                                                                },
                                                                'phone': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Phone number',
                                                                },
                                                                'name': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Full name',
                                                                },
                                                                'province_code': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Province code',
                                                                },
                                                                'country_code': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Country code',
                                                                },
                                                                'country_name': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Country name',
                                                                },
                                                                'default': {
                                                                    'type': ['boolean', 'null'],
                                                                    'description': 'Whether this is the default address',
                                                                },
                                                            },
                                                            'required': ['id'],
                                                        },
                                                    },
                                                    'accepts_marketing_updated_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'When marketing acceptance was updated',
                                                    },
                                                    'marketing_opt_in_level': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Marketing opt-in level',
                                                    },
                                                    'tax_exemptions': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'string'},
                                                    },
                                                    'email_marketing_consent': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'state': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'opt_in_level': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'consent_updated_at': {
                                                                        'type': ['string', 'null'],
                                                                        'format': 'date-time',
                                                                    },
                                                                    'consent_collected_from': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                    'sms_marketing_consent': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'state': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'opt_in_level': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'consent_updated_at': {
                                                                        'type': ['string', 'null'],
                                                                        'format': 'date-time',
                                                                    },
                                                                    'consent_collected_from': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'GraphQL API ID',
                                                    },
                                                    'default_address': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'description': 'A customer address',
                                                                'properties': {
                                                                    'id': {'type': 'integer', 'description': 'Address ID'},
                                                                    'customer_id': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'Customer ID',
                                                                    },
                                                                    'first_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'First name',
                                                                    },
                                                                    'last_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Last name',
                                                                    },
                                                                    'company': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Company name',
                                                                    },
                                                                    'address1': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Address line 1',
                                                                    },
                                                                    'address2': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Address line 2',
                                                                    },
                                                                    'city': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'City',
                                                                    },
                                                                    'province': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Province/State',
                                                                    },
                                                                    'country': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country',
                                                                    },
                                                                    'zip': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'ZIP/Postal code',
                                                                    },
                                                                    'phone': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Phone number',
                                                                    },
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Full name',
                                                                    },
                                                                    'province_code': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Province code',
                                                                    },
                                                                    'country_code': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country code',
                                                                    },
                                                                    'country_name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Country name',
                                                                    },
                                                                    'default': {
                                                                        'type': ['boolean', 'null'],
                                                                        'description': 'Whether this is the default address',
                                                                    },
                                                                },
                                                                'required': ['id'],
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                },
                                                'required': ['id'],
                                                'x-airbyte-entity-name': 'customers',
                                                'x-airbyte-stream-name': 'customers',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Shopify customers with order history and contact information',
                                                    'when_to_use': 'Looking up customer details or purchase history',
                                                    'trigger_phrases': ['shopify customer', 'buyer', 'customer info'],
                                                    'freshness': 'live',
                                                    'example_questions': ['Find a customer in Shopify', 'Show customer order history'],
                                                    'search_strategy': 'Search by email, name, or phone',
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'allow_discount_codes_in_checkout?': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether discount codes can be applied at checkout',
                                    },
                                    'b2b?': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is a B2B order',
                                    },
                                    'api_client_id': {
                                        'type': ['integer', 'null'],
                                        'description': 'The ID of the API client that created the draft order',
                                    },
                                    'created_on_api_version_handle': {
                                        'type': ['string', 'null'],
                                        'description': 'The API version handle when the draft order was created',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'draft_orders',
                                'x-airbyte-stream-name': 'draft_orders',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Draft orders created manually in Shopify admin',
                                    'when_to_use': 'Questions about draft orders or manually created orders',
                                    'trigger_phrases': ['draft order', 'manual order'],
                                    'freshness': 'live',
                                    'example_questions': ['Show draft orders'],
                                    'search_strategy': 'Filter by status or date',
                                },
                            },
                        },
                    },
                    record_extractor='$.draft_order',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A draft order',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Draft order ID'},
                    'note': {
                        'type': ['string', 'null'],
                    },
                    'email': {
                        'type': ['string', 'null'],
                    },
                    'taxes_included': {
                        'type': ['boolean', 'null'],
                    },
                    'currency': {
                        'type': ['string', 'null'],
                    },
                    'invoice_sent_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'tax_exempt': {
                        'type': ['boolean', 'null'],
                    },
                    'completed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'status': {
                        'type': ['string', 'null'],
                    },
                    'line_items': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/LineItem'},
                    },
                    'shipping_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/OrderAddress'},
                            {'type': 'null'},
                        ],
                    },
                    'billing_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/OrderAddress'},
                            {'type': 'null'},
                        ],
                    },
                    'invoice_url': {
                        'type': ['string', 'null'],
                    },
                    'applied_discount': {
                        'type': ['object', 'null'],
                    },
                    'order_id': {
                        'type': ['integer', 'null'],
                    },
                    'shipping_line': {
                        'type': ['object', 'null'],
                    },
                    'tax_lines': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'tags': {
                        'type': ['string', 'null'],
                    },
                    'note_attributes': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'total_price': {
                        'type': ['string', 'null'],
                    },
                    'subtotal_price': {
                        'type': ['string', 'null'],
                    },
                    'total_tax': {
                        'type': ['string', 'null'],
                    },
                    'payment_terms': {
                        'type': ['object', 'null'],
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                    'customer': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Customer'},
                            {'type': 'null'},
                        ],
                    },
                    'allow_discount_codes_in_checkout?': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether discount codes can be applied at checkout',
                    },
                    'b2b?': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this is a B2B order',
                    },
                    'api_client_id': {
                        'type': ['integer', 'null'],
                        'description': 'The ID of the API client that created the draft order',
                    },
                    'created_on_api_version_handle': {
                        'type': ['string', 'null'],
                        'description': 'The API version handle when the draft order was created',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'draft_orders',
                'x-airbyte-stream-name': 'draft_orders',
                'x-airbyte-ai-hints': {
                    'summary': 'Draft orders created manually in Shopify admin',
                    'when_to_use': 'Questions about draft orders or manually created orders',
                    'trigger_phrases': ['draft order', 'manual order'],
                    'freshness': 'live',
                    'example_questions': ['Show draft orders'],
                    'search_strategy': 'Filter by status or date',
                },
            },
            ai_hints={
                'summary': 'Draft orders created manually in Shopify admin',
                'when_to_use': 'Questions about draft orders or manually created orders',
                'trigger_phrases': ['draft order', 'manual order'],
                'freshness': 'live',
                'example_questions': ['Show draft orders'],
                'search_strategy': 'Filter by status or date',
            },
        ),
        EntityDefinition(
            name='fulfillments',
            stream_name='fulfillments',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/fulfillments.json',
                    action=Action.LIST,
                    description='Returns a list of fulfillments for an order',
                    query_params=[
                        'limit',
                        'since_id',
                        'created_at_min',
                        'created_at_max',
                        'updated_at_min',
                        'updated_at_max',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'created_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'updated_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                    },
                    path_params=['order_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'fulfillments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A fulfillment',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Fulfillment ID'},
                                        'order_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'service': {
                                            'type': ['string', 'null'],
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'tracking_company': {
                                            'type': ['string', 'null'],
                                        },
                                        'shipment_status': {
                                            'type': ['string', 'null'],
                                        },
                                        'location_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'origin_address': {
                                            'type': ['object', 'null'],
                                        },
                                        'line_items': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'integer'},
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'attributed_staffs': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'current_quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'fulfillable_quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'fulfillment_service': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'fulfillment_status': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'gift_card': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'grams': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'price': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'price_set': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'product_exists': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'product_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'properties': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'quantity': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'requires_shipping': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'sku': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'taxable': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'total_discount': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'total_discount_set': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'variant_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'variant_inventory_management': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'variant_title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'vendor': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'tax_lines': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'duties': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                    'discount_allocations': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'object'},
                                                    },
                                                },
                                            },
                                        },
                                        'tracking_number': {
                                            'type': ['string', 'null'],
                                        },
                                        'tracking_numbers': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                        },
                                        'tracking_url': {
                                            'type': ['string', 'null'],
                                        },
                                        'tracking_urls': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                        },
                                        'receipt': {
                                            'type': ['object', 'null'],
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'fulfillments',
                                    'x-airbyte-stream-name': 'fulfillments',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Order fulfillments with tracking and shipping details',
                                        'when_to_use': 'Questions about shipping status or fulfillment tracking',
                                        'trigger_phrases': ['fulfillment', 'shipping status', 'tracking number'],
                                        'freshness': 'live',
                                        'example_questions': ['What is the shipping status of an order?'],
                                        'search_strategy': 'Filter by order',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.fulfillments',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/fulfillments/{fulfillment_id}.json',
                    action=Action.GET,
                    description='Retrieves a single fulfillment by ID',
                    path_params=['order_id', 'fulfillment_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                        'fulfillment_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'fulfillment': {
                                'type': 'object',
                                'description': 'A fulfillment',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Fulfillment ID'},
                                    'order_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'service': {
                                        'type': ['string', 'null'],
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'tracking_company': {
                                        'type': ['string', 'null'],
                                    },
                                    'shipment_status': {
                                        'type': ['string', 'null'],
                                    },
                                    'location_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'origin_address': {
                                        'type': ['object', 'null'],
                                    },
                                    'line_items': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'integer'},
                                                'admin_graphql_api_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'attributed_staffs': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'current_quantity': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'fulfillable_quantity': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'fulfillment_service': {
                                                    'type': ['string', 'null'],
                                                },
                                                'fulfillment_status': {
                                                    'type': ['string', 'null'],
                                                },
                                                'gift_card': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'grams': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'name': {
                                                    'type': ['string', 'null'],
                                                },
                                                'price': {
                                                    'type': ['string', 'null'],
                                                },
                                                'price_set': {
                                                    'type': ['object', 'null'],
                                                },
                                                'product_exists': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'product_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'properties': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'quantity': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'requires_shipping': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'sku': {
                                                    'type': ['string', 'null'],
                                                },
                                                'taxable': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'title': {
                                                    'type': ['string', 'null'],
                                                },
                                                'total_discount': {
                                                    'type': ['string', 'null'],
                                                },
                                                'total_discount_set': {
                                                    'type': ['object', 'null'],
                                                },
                                                'variant_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'variant_inventory_management': {
                                                    'type': ['string', 'null'],
                                                },
                                                'variant_title': {
                                                    'type': ['string', 'null'],
                                                },
                                                'vendor': {
                                                    'type': ['string', 'null'],
                                                },
                                                'tax_lines': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'duties': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                                'discount_allocations': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                            },
                                        },
                                    },
                                    'tracking_number': {
                                        'type': ['string', 'null'],
                                    },
                                    'tracking_numbers': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                    },
                                    'tracking_url': {
                                        'type': ['string', 'null'],
                                    },
                                    'tracking_urls': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                    },
                                    'receipt': {
                                        'type': ['object', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'fulfillments',
                                'x-airbyte-stream-name': 'fulfillments',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Order fulfillments with tracking and shipping details',
                                    'when_to_use': 'Questions about shipping status or fulfillment tracking',
                                    'trigger_phrases': ['fulfillment', 'shipping status', 'tracking number'],
                                    'freshness': 'live',
                                    'example_questions': ['What is the shipping status of an order?'],
                                    'search_strategy': 'Filter by order',
                                },
                            },
                        },
                    },
                    record_extractor='$.fulfillment',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A fulfillment',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Fulfillment ID'},
                    'order_id': {
                        'type': ['integer', 'null'],
                    },
                    'status': {
                        'type': ['string', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'service': {
                        'type': ['string', 'null'],
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'tracking_company': {
                        'type': ['string', 'null'],
                    },
                    'shipment_status': {
                        'type': ['string', 'null'],
                    },
                    'location_id': {
                        'type': ['integer', 'null'],
                    },
                    'origin_address': {
                        'type': ['object', 'null'],
                    },
                    'line_items': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/LineItem'},
                    },
                    'tracking_number': {
                        'type': ['string', 'null'],
                    },
                    'tracking_numbers': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                    },
                    'tracking_url': {
                        'type': ['string', 'null'],
                    },
                    'tracking_urls': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                    },
                    'receipt': {
                        'type': ['object', 'null'],
                    },
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'fulfillments',
                'x-airbyte-stream-name': 'fulfillments',
                'x-airbyte-ai-hints': {
                    'summary': 'Order fulfillments with tracking and shipping details',
                    'when_to_use': 'Questions about shipping status or fulfillment tracking',
                    'trigger_phrases': ['fulfillment', 'shipping status', 'tracking number'],
                    'freshness': 'live',
                    'example_questions': ['What is the shipping status of an order?'],
                    'search_strategy': 'Filter by order',
                },
            },
            ai_hints={
                'summary': 'Order fulfillments with tracking and shipping details',
                'when_to_use': 'Questions about shipping status or fulfillment tracking',
                'trigger_phrases': ['fulfillment', 'shipping status', 'tracking number'],
                'freshness': 'live',
                'example_questions': ['What is the shipping status of an order?'],
                'search_strategy': 'Filter by order',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='fulfillments',
                    target_entity='orders',
                    foreign_key='order_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='order_refunds',
            stream_name='order_refunds',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/refunds.json',
                    action=Action.LIST,
                    description='Returns a list of refunds for an order',
                    query_params=['limit'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                    },
                    path_params=['order_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'refunds': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An order refund',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Refund ID'},
                                        'order_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'note': {
                                            'type': ['string', 'null'],
                                        },
                                        'user_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'processed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'restock': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'duties': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'total_duties_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'return': {
                                            'type': ['object', 'null'],
                                        },
                                        'refund_line_items': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'transactions': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'An order transaction',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Transaction ID'},
                                                    'order_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'kind': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'gateway': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'status': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'message': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'created_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'test': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'authorization': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'location_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'user_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'parent_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'processed_at': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'device_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'error_code': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'source_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'receipt': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'currency_exchange_adjustment': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'amount': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'currency': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'payment_id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'total_unsettled_set': {
                                                        'type': ['object', 'null'],
                                                    },
                                                    'manual_payment_gateway': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'admin_graphql_api_id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                                'required': ['id'],
                                                'x-airbyte-entity-name': 'transactions',
                                                'x-airbyte-stream-name': 'transactions',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Payment transactions on Shopify orders',
                                                    'when_to_use': 'Questions about payment processing or transaction details',
                                                    'trigger_phrases': ['shopify transaction', 'payment', 'charge'],
                                                    'freshness': 'live',
                                                    'example_questions': ['Show transactions for an order'],
                                                    'search_strategy': 'Filter by order',
                                                },
                                            },
                                        },
                                        'order_adjustments': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'refund_shipping_lines': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'order_refunds',
                                    'x-airbyte-stream-name': 'order_refunds',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Refunds processed for Shopify orders',
                                        'when_to_use': 'Questions about refunds or return processing',
                                        'trigger_phrases': ['refund', 'order refund', 'return'],
                                        'freshness': 'live',
                                        'example_questions': ['What refunds were processed for an order?'],
                                        'search_strategy': 'Filter by order',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.refunds',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/refunds/{refund_id}.json',
                    action=Action.GET,
                    description='Retrieves a single refund by ID',
                    path_params=['order_id', 'refund_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                        'refund_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'refund': {
                                'type': 'object',
                                'description': 'An order refund',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Refund ID'},
                                    'order_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'note': {
                                        'type': ['string', 'null'],
                                    },
                                    'user_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'processed_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'restock': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'duties': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'total_duties_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'return': {
                                        'type': ['object', 'null'],
                                    },
                                    'refund_line_items': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'transactions': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'description': 'An order transaction',
                                            'properties': {
                                                'id': {'type': 'integer', 'description': 'Transaction ID'},
                                                'order_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'kind': {
                                                    'type': ['string', 'null'],
                                                },
                                                'gateway': {
                                                    'type': ['string', 'null'],
                                                },
                                                'status': {
                                                    'type': ['string', 'null'],
                                                },
                                                'message': {
                                                    'type': ['string', 'null'],
                                                },
                                                'created_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                },
                                                'test': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'authorization': {
                                                    'type': ['string', 'null'],
                                                },
                                                'location_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'user_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'parent_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'processed_at': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                },
                                                'device_id': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'error_code': {
                                                    'type': ['string', 'null'],
                                                },
                                                'source_name': {
                                                    'type': ['string', 'null'],
                                                },
                                                'receipt': {
                                                    'type': ['object', 'null'],
                                                },
                                                'currency_exchange_adjustment': {
                                                    'type': ['object', 'null'],
                                                },
                                                'amount': {
                                                    'type': ['string', 'null'],
                                                },
                                                'currency': {
                                                    'type': ['string', 'null'],
                                                },
                                                'payment_id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'total_unsettled_set': {
                                                    'type': ['object', 'null'],
                                                },
                                                'manual_payment_gateway': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'admin_graphql_api_id': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                            'required': ['id'],
                                            'x-airbyte-entity-name': 'transactions',
                                            'x-airbyte-stream-name': 'transactions',
                                            'x-airbyte-ai-hints': {
                                                'summary': 'Payment transactions on Shopify orders',
                                                'when_to_use': 'Questions about payment processing or transaction details',
                                                'trigger_phrases': ['shopify transaction', 'payment', 'charge'],
                                                'freshness': 'live',
                                                'example_questions': ['Show transactions for an order'],
                                                'search_strategy': 'Filter by order',
                                            },
                                        },
                                    },
                                    'order_adjustments': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'refund_shipping_lines': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'order_refunds',
                                'x-airbyte-stream-name': 'order_refunds',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Refunds processed for Shopify orders',
                                    'when_to_use': 'Questions about refunds or return processing',
                                    'trigger_phrases': ['refund', 'order refund', 'return'],
                                    'freshness': 'live',
                                    'example_questions': ['What refunds were processed for an order?'],
                                    'search_strategy': 'Filter by order',
                                },
                            },
                        },
                    },
                    record_extractor='$.refund',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An order refund',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Refund ID'},
                    'order_id': {
                        'type': ['integer', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'note': {
                        'type': ['string', 'null'],
                    },
                    'user_id': {
                        'type': ['integer', 'null'],
                    },
                    'processed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'restock': {
                        'type': ['boolean', 'null'],
                    },
                    'duties': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'total_duties_set': {
                        'type': ['object', 'null'],
                    },
                    'return': {
                        'type': ['object', 'null'],
                    },
                    'refund_line_items': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'transactions': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/Transaction'},
                    },
                    'order_adjustments': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                    'refund_shipping_lines': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'order_refunds',
                'x-airbyte-stream-name': 'order_refunds',
                'x-airbyte-ai-hints': {
                    'summary': 'Refunds processed for Shopify orders',
                    'when_to_use': 'Questions about refunds or return processing',
                    'trigger_phrases': ['refund', 'order refund', 'return'],
                    'freshness': 'live',
                    'example_questions': ['What refunds were processed for an order?'],
                    'search_strategy': 'Filter by order',
                },
            },
            ai_hints={
                'summary': 'Refunds processed for Shopify orders',
                'when_to_use': 'Questions about refunds or return processing',
                'trigger_phrases': ['refund', 'order refund', 'return'],
                'freshness': 'live',
                'example_questions': ['What refunds were processed for an order?'],
                'search_strategy': 'Filter by order',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='order_refunds',
                    target_entity='orders',
                    foreign_key='order_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='transactions',
            stream_name='transactions',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/transactions.json',
                    action=Action.LIST,
                    description='Returns a list of transactions for an order',
                    query_params=['since_id'],
                    query_params_schema={
                        'since_id': {'type': 'integer', 'required': False},
                    },
                    path_params=['order_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'transactions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An order transaction',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Transaction ID'},
                                        'order_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'kind': {
                                            'type': ['string', 'null'],
                                        },
                                        'gateway': {
                                            'type': ['string', 'null'],
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                        },
                                        'message': {
                                            'type': ['string', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'test': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'authorization': {
                                            'type': ['string', 'null'],
                                        },
                                        'location_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'user_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'parent_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'processed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'device_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'error_code': {
                                            'type': ['string', 'null'],
                                        },
                                        'source_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'receipt': {
                                            'type': ['object', 'null'],
                                        },
                                        'currency_exchange_adjustment': {
                                            'type': ['object', 'null'],
                                        },
                                        'amount': {
                                            'type': ['string', 'null'],
                                        },
                                        'currency': {
                                            'type': ['string', 'null'],
                                        },
                                        'payment_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'total_unsettled_set': {
                                            'type': ['object', 'null'],
                                        },
                                        'manual_payment_gateway': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'transactions',
                                    'x-airbyte-stream-name': 'transactions',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Payment transactions on Shopify orders',
                                        'when_to_use': 'Questions about payment processing or transaction details',
                                        'trigger_phrases': ['shopify transaction', 'payment', 'charge'],
                                        'freshness': 'live',
                                        'example_questions': ['Show transactions for an order'],
                                        'search_strategy': 'Filter by order',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.transactions',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/transactions/{transaction_id}.json',
                    action=Action.GET,
                    description='Retrieves a single transaction by ID',
                    path_params=['order_id', 'transaction_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                        'transaction_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'transaction': {
                                'type': 'object',
                                'description': 'An order transaction',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Transaction ID'},
                                    'order_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'kind': {
                                        'type': ['string', 'null'],
                                    },
                                    'gateway': {
                                        'type': ['string', 'null'],
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                    },
                                    'message': {
                                        'type': ['string', 'null'],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'test': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'authorization': {
                                        'type': ['string', 'null'],
                                    },
                                    'location_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'user_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'parent_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'processed_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'device_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'error_code': {
                                        'type': ['string', 'null'],
                                    },
                                    'source_name': {
                                        'type': ['string', 'null'],
                                    },
                                    'receipt': {
                                        'type': ['object', 'null'],
                                    },
                                    'currency_exchange_adjustment': {
                                        'type': ['object', 'null'],
                                    },
                                    'amount': {
                                        'type': ['string', 'null'],
                                    },
                                    'currency': {
                                        'type': ['string', 'null'],
                                    },
                                    'payment_id': {
                                        'type': ['string', 'null'],
                                    },
                                    'total_unsettled_set': {
                                        'type': ['object', 'null'],
                                    },
                                    'manual_payment_gateway': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'transactions',
                                'x-airbyte-stream-name': 'transactions',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Payment transactions on Shopify orders',
                                    'when_to_use': 'Questions about payment processing or transaction details',
                                    'trigger_phrases': ['shopify transaction', 'payment', 'charge'],
                                    'freshness': 'live',
                                    'example_questions': ['Show transactions for an order'],
                                    'search_strategy': 'Filter by order',
                                },
                            },
                        },
                    },
                    record_extractor='$.transaction',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An order transaction',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Transaction ID'},
                    'order_id': {
                        'type': ['integer', 'null'],
                    },
                    'kind': {
                        'type': ['string', 'null'],
                    },
                    'gateway': {
                        'type': ['string', 'null'],
                    },
                    'status': {
                        'type': ['string', 'null'],
                    },
                    'message': {
                        'type': ['string', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'test': {
                        'type': ['boolean', 'null'],
                    },
                    'authorization': {
                        'type': ['string', 'null'],
                    },
                    'location_id': {
                        'type': ['integer', 'null'],
                    },
                    'user_id': {
                        'type': ['integer', 'null'],
                    },
                    'parent_id': {
                        'type': ['integer', 'null'],
                    },
                    'processed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'device_id': {
                        'type': ['integer', 'null'],
                    },
                    'error_code': {
                        'type': ['string', 'null'],
                    },
                    'source_name': {
                        'type': ['string', 'null'],
                    },
                    'receipt': {
                        'type': ['object', 'null'],
                    },
                    'currency_exchange_adjustment': {
                        'type': ['object', 'null'],
                    },
                    'amount': {
                        'type': ['string', 'null'],
                    },
                    'currency': {
                        'type': ['string', 'null'],
                    },
                    'payment_id': {
                        'type': ['string', 'null'],
                    },
                    'total_unsettled_set': {
                        'type': ['object', 'null'],
                    },
                    'manual_payment_gateway': {
                        'type': ['boolean', 'null'],
                    },
                    'admin_graphql_api_id': {
                        'type': ['string', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'transactions',
                'x-airbyte-stream-name': 'transactions',
                'x-airbyte-ai-hints': {
                    'summary': 'Payment transactions on Shopify orders',
                    'when_to_use': 'Questions about payment processing or transaction details',
                    'trigger_phrases': ['shopify transaction', 'payment', 'charge'],
                    'freshness': 'live',
                    'example_questions': ['Show transactions for an order'],
                    'search_strategy': 'Filter by order',
                },
            },
            ai_hints={
                'summary': 'Payment transactions on Shopify orders',
                'when_to_use': 'Questions about payment processing or transaction details',
                'trigger_phrases': ['shopify transaction', 'payment', 'charge'],
                'freshness': 'live',
                'example_questions': ['Show transactions for an order'],
                'search_strategy': 'Filter by order',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='transactions',
                    target_entity='orders',
                    foreign_key='order_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='tender_transactions',
            stream_name='tender_transactions',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tender_transactions.json',
                    action=Action.LIST,
                    description='Returns a list of tender transactions',
                    query_params=[
                        'limit',
                        'since_id',
                        'processed_at_min',
                        'processed_at_max',
                        'order',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'processed_at_min': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'processed_at_max': {
                            'type': 'string',
                            'required': False,
                            'format': 'date-time',
                        },
                        'order': {
                            'type': 'string',
                            'required': False,
                            'enum': ['processed_at ASC', 'processed_at DESC'],
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'tender_transactions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A tender transaction',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Tender transaction ID'},
                                        'order_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'amount': {
                                            'type': ['string', 'null'],
                                        },
                                        'currency': {
                                            'type': ['string', 'null'],
                                        },
                                        'user_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'test': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'processed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'remote_reference': {
                                            'type': ['string', 'null'],
                                        },
                                        'payment_details': {
                                            'type': ['object', 'null'],
                                        },
                                        'payment_method': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'tender_transactions',
                                    'x-airbyte-stream-name': 'tender_transactions',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Tender transactions recording payment method usage',
                                        'when_to_use': 'Questions about payment method usage or tender records',
                                        'trigger_phrases': ['tender transaction', 'payment method'],
                                        'freshness': 'live',
                                        'example_questions': ['Show recent tender transactions'],
                                        'search_strategy': 'Filter by date',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.tender_transactions',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A tender transaction',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Tender transaction ID'},
                    'order_id': {
                        'type': ['integer', 'null'],
                    },
                    'amount': {
                        'type': ['string', 'null'],
                    },
                    'currency': {
                        'type': ['string', 'null'],
                    },
                    'user_id': {
                        'type': ['integer', 'null'],
                    },
                    'test': {
                        'type': ['boolean', 'null'],
                    },
                    'processed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'remote_reference': {
                        'type': ['string', 'null'],
                    },
                    'payment_details': {
                        'type': ['object', 'null'],
                    },
                    'payment_method': {
                        'type': ['string', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'tender_transactions',
                'x-airbyte-stream-name': 'tender_transactions',
                'x-airbyte-ai-hints': {
                    'summary': 'Tender transactions recording payment method usage',
                    'when_to_use': 'Questions about payment method usage or tender records',
                    'trigger_phrases': ['tender transaction', 'payment method'],
                    'freshness': 'live',
                    'example_questions': ['Show recent tender transactions'],
                    'search_strategy': 'Filter by date',
                },
            },
            ai_hints={
                'summary': 'Tender transactions recording payment method usage',
                'when_to_use': 'Questions about payment method usage or tender records',
                'trigger_phrases': ['tender transaction', 'payment method'],
                'freshness': 'live',
                'example_questions': ['Show recent tender transactions'],
                'search_strategy': 'Filter by date',
            },
        ),
        EntityDefinition(
            name='countries',
            stream_name='countries',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/countries.json',
                    action=Action.LIST,
                    description='Returns a list of countries',
                    query_params=['since_id'],
                    query_params_schema={
                        'since_id': {'type': 'integer', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'countries': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A country',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Country ID'},
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'code': {
                                            'type': ['string', 'null'],
                                        },
                                        'tax_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'tax': {
                                            'type': ['number', 'null'],
                                        },
                                        'provinces': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'countries',
                                    'x-airbyte-stream-name': 'countries',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Countries configured for Shopify store shipping and taxes',
                                        'when_to_use': 'Questions about shipping zones or tax configuration by country',
                                        'trigger_phrases': ['shopify country', 'shipping country', 'tax region'],
                                        'freshness': 'static',
                                        'example_questions': ['What countries are configured for shipping?'],
                                        'search_strategy': 'List all countries',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.countries',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/countries/{country_id}.json',
                    action=Action.GET,
                    description='Retrieves a single country by ID',
                    path_params=['country_id'],
                    path_params_schema={
                        'country_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'country': {
                                'type': 'object',
                                'description': 'A country',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Country ID'},
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'code': {
                                        'type': ['string', 'null'],
                                    },
                                    'tax_name': {
                                        'type': ['string', 'null'],
                                    },
                                    'tax': {
                                        'type': ['number', 'null'],
                                    },
                                    'provinces': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'countries',
                                'x-airbyte-stream-name': 'countries',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Countries configured for Shopify store shipping and taxes',
                                    'when_to_use': 'Questions about shipping zones or tax configuration by country',
                                    'trigger_phrases': ['shopify country', 'shipping country', 'tax region'],
                                    'freshness': 'static',
                                    'example_questions': ['What countries are configured for shipping?'],
                                    'search_strategy': 'List all countries',
                                },
                            },
                        },
                    },
                    record_extractor='$.country',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A country',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Country ID'},
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'code': {
                        'type': ['string', 'null'],
                    },
                    'tax_name': {
                        'type': ['string', 'null'],
                    },
                    'tax': {
                        'type': ['number', 'null'],
                    },
                    'provinces': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'countries',
                'x-airbyte-stream-name': 'countries',
                'x-airbyte-ai-hints': {
                    'summary': 'Countries configured for Shopify store shipping and taxes',
                    'when_to_use': 'Questions about shipping zones or tax configuration by country',
                    'trigger_phrases': ['shopify country', 'shipping country', 'tax region'],
                    'freshness': 'static',
                    'example_questions': ['What countries are configured for shipping?'],
                    'search_strategy': 'List all countries',
                },
            },
            ai_hints={
                'summary': 'Countries configured for Shopify store shipping and taxes',
                'when_to_use': 'Questions about shipping zones or tax configuration by country',
                'trigger_phrases': ['shopify country', 'shipping country', 'tax region'],
                'freshness': 'static',
                'example_questions': ['What countries are configured for shipping?'],
                'search_strategy': 'List all countries',
            },
        ),
        EntityDefinition(
            name='metafield_shops',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/metafields.json',
                    action=Action.LIST,
                    description='Returns a list of metafields for the shop',
                    query_params=[
                        'limit',
                        'since_id',
                        'namespace',
                        'key',
                        'type',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'namespace': {'type': 'string', 'required': False},
                        'key': {'type': 'string', 'required': False},
                        'type': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'metafields': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A metafield',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Metafield ID'},
                                        'namespace': {
                                            'type': ['string', 'null'],
                                        },
                                        'key': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': [
                                                'string',
                                                'integer',
                                                'boolean',
                                                'null',
                                            ],
                                            'description': 'The metafield value (can be string, integer, or boolean depending on type)',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'owner_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'owner_resource': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'metafields',
                                    'x-airbyte-stream-name': 'metafields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom metafields storing additional data on Shopify resources',
                                        'when_to_use': 'Questions about custom metadata or extended fields on resources',
                                        'trigger_phrases': ['metafield', 'custom field', 'metadata'],
                                        'freshness': 'live',
                                        'example_questions': ['What metafields are on a product?'],
                                        'search_strategy': 'Filter by resource type and namespace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/metafields/{metafield_id}.json',
                    action=Action.GET,
                    description='Retrieves a single metafield by ID',
                    path_params=['metafield_id'],
                    path_params_schema={
                        'metafield_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'metafield': {
                                'type': 'object',
                                'description': 'A metafield',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Metafield ID'},
                                    'namespace': {
                                        'type': ['string', 'null'],
                                    },
                                    'key': {
                                        'type': ['string', 'null'],
                                    },
                                    'value': {
                                        'type': [
                                            'string',
                                            'integer',
                                            'boolean',
                                            'null',
                                        ],
                                        'description': 'The metafield value (can be string, integer, or boolean depending on type)',
                                    },
                                    'type': {
                                        'type': ['string', 'null'],
                                    },
                                    'description': {
                                        'type': ['string', 'null'],
                                    },
                                    'owner_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'owner_resource': {
                                        'type': ['string', 'null'],
                                    },
                                    'admin_graphql_api_id': {
                                        'type': ['string', 'null'],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'metafields',
                                'x-airbyte-stream-name': 'metafields',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Custom metafields storing additional data on Shopify resources',
                                    'when_to_use': 'Questions about custom metadata or extended fields on resources',
                                    'trigger_phrases': ['metafield', 'custom field', 'metadata'],
                                    'freshness': 'live',
                                    'example_questions': ['What metafields are on a product?'],
                                    'search_strategy': 'Filter by resource type and namespace',
                                },
                            },
                        },
                    },
                    record_extractor='$.metafield',
                ),
            },
        ),
        EntityDefinition(
            name='metafield_customers',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/customers/{customer_id}/metafields.json',
                    action=Action.LIST,
                    description='Returns a list of metafields for a customer',
                    query_params=[
                        'limit',
                        'since_id',
                        'namespace',
                        'key',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'namespace': {'type': 'string', 'required': False},
                        'key': {'type': 'string', 'required': False},
                    },
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'metafields': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A metafield',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Metafield ID'},
                                        'namespace': {
                                            'type': ['string', 'null'],
                                        },
                                        'key': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': [
                                                'string',
                                                'integer',
                                                'boolean',
                                                'null',
                                            ],
                                            'description': 'The metafield value (can be string, integer, or boolean depending on type)',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'owner_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'owner_resource': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'metafields',
                                    'x-airbyte-stream-name': 'metafields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom metafields storing additional data on Shopify resources',
                                        'when_to_use': 'Questions about custom metadata or extended fields on resources',
                                        'trigger_phrases': ['metafield', 'custom field', 'metadata'],
                                        'freshness': 'live',
                                        'example_questions': ['What metafields are on a product?'],
                                        'search_strategy': 'Filter by resource type and namespace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='metafield_customers',
                    target_entity='customers',
                    foreign_key='customer_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='metafield_products',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/products/{product_id}/metafields.json',
                    action=Action.LIST,
                    description='Returns a list of metafields for a product',
                    query_params=[
                        'limit',
                        'since_id',
                        'namespace',
                        'key',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'namespace': {'type': 'string', 'required': False},
                        'key': {'type': 'string', 'required': False},
                    },
                    path_params=['product_id'],
                    path_params_schema={
                        'product_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'metafields': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A metafield',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Metafield ID'},
                                        'namespace': {
                                            'type': ['string', 'null'],
                                        },
                                        'key': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': [
                                                'string',
                                                'integer',
                                                'boolean',
                                                'null',
                                            ],
                                            'description': 'The metafield value (can be string, integer, or boolean depending on type)',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'owner_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'owner_resource': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'metafields',
                                    'x-airbyte-stream-name': 'metafields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom metafields storing additional data on Shopify resources',
                                        'when_to_use': 'Questions about custom metadata or extended fields on resources',
                                        'trigger_phrases': ['metafield', 'custom field', 'metadata'],
                                        'freshness': 'live',
                                        'example_questions': ['What metafields are on a product?'],
                                        'search_strategy': 'Filter by resource type and namespace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='metafield_products',
                    target_entity='products',
                    foreign_key='product_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='metafield_orders',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/metafields.json',
                    action=Action.LIST,
                    description='Returns a list of metafields for an order',
                    query_params=[
                        'limit',
                        'since_id',
                        'namespace',
                        'key',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'namespace': {'type': 'string', 'required': False},
                        'key': {'type': 'string', 'required': False},
                    },
                    path_params=['order_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'metafields': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A metafield',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Metafield ID'},
                                        'namespace': {
                                            'type': ['string', 'null'],
                                        },
                                        'key': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': [
                                                'string',
                                                'integer',
                                                'boolean',
                                                'null',
                                            ],
                                            'description': 'The metafield value (can be string, integer, or boolean depending on type)',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'owner_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'owner_resource': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'metafields',
                                    'x-airbyte-stream-name': 'metafields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom metafields storing additional data on Shopify resources',
                                        'when_to_use': 'Questions about custom metadata or extended fields on resources',
                                        'trigger_phrases': ['metafield', 'custom field', 'metadata'],
                                        'freshness': 'live',
                                        'example_questions': ['What metafields are on a product?'],
                                        'search_strategy': 'Filter by resource type and namespace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='metafield_orders',
                    target_entity='orders',
                    foreign_key='order_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='metafield_draft_orders',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/draft_orders/{draft_order_id}/metafields.json',
                    action=Action.LIST,
                    description='Returns a list of metafields for a draft order',
                    query_params=[
                        'limit',
                        'since_id',
                        'namespace',
                        'key',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'namespace': {'type': 'string', 'required': False},
                        'key': {'type': 'string', 'required': False},
                    },
                    path_params=['draft_order_id'],
                    path_params_schema={
                        'draft_order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'metafields': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A metafield',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Metafield ID'},
                                        'namespace': {
                                            'type': ['string', 'null'],
                                        },
                                        'key': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': [
                                                'string',
                                                'integer',
                                                'boolean',
                                                'null',
                                            ],
                                            'description': 'The metafield value (can be string, integer, or boolean depending on type)',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'owner_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'owner_resource': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'metafields',
                                    'x-airbyte-stream-name': 'metafields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom metafields storing additional data on Shopify resources',
                                        'when_to_use': 'Questions about custom metadata or extended fields on resources',
                                        'trigger_phrases': ['metafield', 'custom field', 'metadata'],
                                        'freshness': 'live',
                                        'example_questions': ['What metafields are on a product?'],
                                        'search_strategy': 'Filter by resource type and namespace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='metafield_draft_orders',
                    target_entity='draft_orders',
                    foreign_key='draft_order_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='metafield_locations',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/locations/{location_id}/metafields.json',
                    action=Action.LIST,
                    description='Returns a list of metafields for a location',
                    query_params=[
                        'limit',
                        'since_id',
                        'namespace',
                        'key',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'namespace': {'type': 'string', 'required': False},
                        'key': {'type': 'string', 'required': False},
                    },
                    path_params=['location_id'],
                    path_params_schema={
                        'location_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'metafields': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A metafield',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Metafield ID'},
                                        'namespace': {
                                            'type': ['string', 'null'],
                                        },
                                        'key': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': [
                                                'string',
                                                'integer',
                                                'boolean',
                                                'null',
                                            ],
                                            'description': 'The metafield value (can be string, integer, or boolean depending on type)',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'owner_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'owner_resource': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'metafields',
                                    'x-airbyte-stream-name': 'metafields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom metafields storing additional data on Shopify resources',
                                        'when_to_use': 'Questions about custom metadata or extended fields on resources',
                                        'trigger_phrases': ['metafield', 'custom field', 'metadata'],
                                        'freshness': 'live',
                                        'example_questions': ['What metafields are on a product?'],
                                        'search_strategy': 'Filter by resource type and namespace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='metafield_locations',
                    target_entity='locations',
                    foreign_key='location_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='metafield_product_variants',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/variants/{variant_id}/metafields.json',
                    action=Action.LIST,
                    description='Returns a list of metafields for a product variant',
                    query_params=[
                        'limit',
                        'since_id',
                        'namespace',
                        'key',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'namespace': {'type': 'string', 'required': False},
                        'key': {'type': 'string', 'required': False},
                    },
                    path_params=['variant_id'],
                    path_params_schema={
                        'variant_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'metafields': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A metafield',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Metafield ID'},
                                        'namespace': {
                                            'type': ['string', 'null'],
                                        },
                                        'key': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': [
                                                'string',
                                                'integer',
                                                'boolean',
                                                'null',
                                            ],
                                            'description': 'The metafield value (can be string, integer, or boolean depending on type)',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'owner_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'owner_resource': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'metafields',
                                    'x-airbyte-stream-name': 'metafields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom metafields storing additional data on Shopify resources',
                                        'when_to_use': 'Questions about custom metadata or extended fields on resources',
                                        'trigger_phrases': ['metafield', 'custom field', 'metadata'],
                                        'freshness': 'live',
                                        'example_questions': ['What metafields are on a product?'],
                                        'search_strategy': 'Filter by resource type and namespace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='metafield_product_variants',
                    target_entity='product_variants',
                    foreign_key='variant_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='metafield_smart_collections',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/smart_collections/{collection_id}/metafields.json',
                    action=Action.LIST,
                    description='Returns a list of metafields for a smart collection',
                    query_params=[
                        'limit',
                        'since_id',
                        'namespace',
                        'key',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'namespace': {'type': 'string', 'required': False},
                        'key': {'type': 'string', 'required': False},
                    },
                    path_params=['collection_id'],
                    path_params_schema={
                        'collection_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'metafields': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A metafield',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Metafield ID'},
                                        'namespace': {
                                            'type': ['string', 'null'],
                                        },
                                        'key': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': [
                                                'string',
                                                'integer',
                                                'boolean',
                                                'null',
                                            ],
                                            'description': 'The metafield value (can be string, integer, or boolean depending on type)',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'owner_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'owner_resource': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'metafields',
                                    'x-airbyte-stream-name': 'metafields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom metafields storing additional data on Shopify resources',
                                        'when_to_use': 'Questions about custom metadata or extended fields on resources',
                                        'trigger_phrases': ['metafield', 'custom field', 'metadata'],
                                        'freshness': 'live',
                                        'example_questions': ['What metafields are on a product?'],
                                        'search_strategy': 'Filter by resource type and namespace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='metafield_smart_collections',
                    target_entity='smart_collections',
                    foreign_key='collection_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='metafield_product_images',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/products/{product_id}/images/{image_id}/metafields.json',
                    action=Action.LIST,
                    description='Returns a list of metafields for a product image',
                    query_params=[
                        'limit',
                        'since_id',
                        'namespace',
                        'key',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'namespace': {'type': 'string', 'required': False},
                        'key': {'type': 'string', 'required': False},
                    },
                    path_params=['product_id', 'image_id'],
                    path_params_schema={
                        'product_id': {'type': 'integer', 'required': True},
                        'image_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'metafields': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A metafield',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Metafield ID'},
                                        'namespace': {
                                            'type': ['string', 'null'],
                                        },
                                        'key': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': [
                                                'string',
                                                'integer',
                                                'boolean',
                                                'null',
                                            ],
                                            'description': 'The metafield value (can be string, integer, or boolean depending on type)',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'owner_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'owner_resource': {
                                            'type': ['string', 'null'],
                                        },
                                        'admin_graphql_api_id': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'metafields',
                                    'x-airbyte-stream-name': 'metafields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom metafields storing additional data on Shopify resources',
                                        'when_to_use': 'Questions about custom metadata or extended fields on resources',
                                        'trigger_phrases': ['metafield', 'custom field', 'metadata'],
                                        'freshness': 'live',
                                        'example_questions': ['What metafields are on a product?'],
                                        'search_strategy': 'Filter by resource type and namespace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                    untested=True,
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='metafield_product_images',
                    target_entity='products',
                    foreign_key='product_id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='metafield_product_images',
                    target_entity='product_images',
                    foreign_key='image_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='customer_address',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/customers/{customer_id}/addresses.json',
                    action=Action.LIST,
                    description='Returns a list of addresses for a customer',
                    query_params=['limit'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                    },
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'addresses': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A customer address',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Address ID'},
                                        'customer_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Customer ID',
                                        },
                                        'first_name': {
                                            'type': ['string', 'null'],
                                            'description': 'First name',
                                        },
                                        'last_name': {
                                            'type': ['string', 'null'],
                                            'description': 'Last name',
                                        },
                                        'company': {
                                            'type': ['string', 'null'],
                                            'description': 'Company name',
                                        },
                                        'address1': {
                                            'type': ['string', 'null'],
                                            'description': 'Address line 1',
                                        },
                                        'address2': {
                                            'type': ['string', 'null'],
                                            'description': 'Address line 2',
                                        },
                                        'city': {
                                            'type': ['string', 'null'],
                                            'description': 'City',
                                        },
                                        'province': {
                                            'type': ['string', 'null'],
                                            'description': 'Province/State',
                                        },
                                        'country': {
                                            'type': ['string', 'null'],
                                            'description': 'Country',
                                        },
                                        'zip': {
                                            'type': ['string', 'null'],
                                            'description': 'ZIP/Postal code',
                                        },
                                        'phone': {
                                            'type': ['string', 'null'],
                                            'description': 'Phone number',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Full name',
                                        },
                                        'province_code': {
                                            'type': ['string', 'null'],
                                            'description': 'Province code',
                                        },
                                        'country_code': {
                                            'type': ['string', 'null'],
                                            'description': 'Country code',
                                        },
                                        'country_name': {
                                            'type': ['string', 'null'],
                                            'description': 'Country name',
                                        },
                                        'default': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this is the default address',
                                        },
                                    },
                                    'required': ['id'],
                                },
                            },
                        },
                    },
                    record_extractor='$.addresses',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/customers/{customer_id}/addresses/{address_id}.json',
                    action=Action.GET,
                    description='Retrieves a single customer address by ID',
                    path_params=['customer_id', 'address_id'],
                    path_params_schema={
                        'customer_id': {'type': 'integer', 'required': True},
                        'address_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'customer_address': {
                                'type': 'object',
                                'description': 'A customer address',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Address ID'},
                                    'customer_id': {
                                        'type': ['integer', 'null'],
                                        'description': 'Customer ID',
                                    },
                                    'first_name': {
                                        'type': ['string', 'null'],
                                        'description': 'First name',
                                    },
                                    'last_name': {
                                        'type': ['string', 'null'],
                                        'description': 'Last name',
                                    },
                                    'company': {
                                        'type': ['string', 'null'],
                                        'description': 'Company name',
                                    },
                                    'address1': {
                                        'type': ['string', 'null'],
                                        'description': 'Address line 1',
                                    },
                                    'address2': {
                                        'type': ['string', 'null'],
                                        'description': 'Address line 2',
                                    },
                                    'city': {
                                        'type': ['string', 'null'],
                                        'description': 'City',
                                    },
                                    'province': {
                                        'type': ['string', 'null'],
                                        'description': 'Province/State',
                                    },
                                    'country': {
                                        'type': ['string', 'null'],
                                        'description': 'Country',
                                    },
                                    'zip': {
                                        'type': ['string', 'null'],
                                        'description': 'ZIP/Postal code',
                                    },
                                    'phone': {
                                        'type': ['string', 'null'],
                                        'description': 'Phone number',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Full name',
                                    },
                                    'province_code': {
                                        'type': ['string', 'null'],
                                        'description': 'Province code',
                                    },
                                    'country_code': {
                                        'type': ['string', 'null'],
                                        'description': 'Country code',
                                    },
                                    'country_name': {
                                        'type': ['string', 'null'],
                                        'description': 'Country name',
                                    },
                                    'default': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether this is the default address',
                                    },
                                },
                                'required': ['id'],
                            },
                        },
                    },
                    record_extractor='$.customer_address',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='customer_address',
                    target_entity='customers',
                    foreign_key='customer_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='fulfillment_orders',
            stream_name='fulfillment_orders',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/fulfillment_orders.json',
                    action=Action.LIST,
                    description='Returns a list of fulfillment orders for a specific order',
                    path_params=['order_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'fulfillment_orders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A fulfillment order',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Fulfillment order ID'},
                                        'shop_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'order_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'assigned_location_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'request_status': {
                                            'type': ['string', 'null'],
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                        },
                                        'supported_actions': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                        },
                                        'destination': {
                                            'type': ['object', 'null'],
                                        },
                                        'line_items': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'fulfill_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'fulfill_by': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'international_duties': {
                                            'type': ['object', 'null'],
                                        },
                                        'fulfillment_holds': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'delivery_method': {
                                            'type': ['object', 'null'],
                                        },
                                        'assigned_location': {
                                            'type': ['object', 'null'],
                                        },
                                        'merchant_requests': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'object'},
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'fulfillment_orders',
                                    'x-airbyte-stream-name': 'fulfillment_orders',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Fulfillment orders representing items to be shipped from a location',
                                        'when_to_use': 'Questions about pending fulfillment or items to ship',
                                        'trigger_phrases': ['fulfillment order', 'items to ship', 'pending fulfillment'],
                                        'freshness': 'live',
                                        'example_questions': ['What fulfillment orders are pending?'],
                                        'search_strategy': 'Filter by order or location',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.fulfillment_orders',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/fulfillment_orders/{fulfillment_order_id}.json',
                    action=Action.GET,
                    description='Retrieves a single fulfillment order by ID',
                    path_params=['fulfillment_order_id'],
                    path_params_schema={
                        'fulfillment_order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'fulfillment_order': {
                                'type': 'object',
                                'description': 'A fulfillment order',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Fulfillment order ID'},
                                    'shop_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'order_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'assigned_location_id': {
                                        'type': ['integer', 'null'],
                                    },
                                    'request_status': {
                                        'type': ['string', 'null'],
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                    },
                                    'supported_actions': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                    },
                                    'destination': {
                                        'type': ['object', 'null'],
                                    },
                                    'line_items': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'fulfill_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'fulfill_by': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'international_duties': {
                                        'type': ['object', 'null'],
                                    },
                                    'fulfillment_holds': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'delivery_method': {
                                        'type': ['object', 'null'],
                                    },
                                    'assigned_location': {
                                        'type': ['object', 'null'],
                                    },
                                    'merchant_requests': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'fulfillment_orders',
                                'x-airbyte-stream-name': 'fulfillment_orders',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Fulfillment orders representing items to be shipped from a location',
                                    'when_to_use': 'Questions about pending fulfillment or items to ship',
                                    'trigger_phrases': ['fulfillment order', 'items to ship', 'pending fulfillment'],
                                    'freshness': 'live',
                                    'example_questions': ['What fulfillment orders are pending?'],
                                    'search_strategy': 'Filter by order or location',
                                },
                            },
                        },
                    },
                    record_extractor='$.fulfillment_order',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A fulfillment order',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Fulfillment order ID'},
                    'shop_id': {
                        'type': ['integer', 'null'],
                    },
                    'order_id': {
                        'type': ['integer', 'null'],
                    },
                    'assigned_location_id': {
                        'type': ['integer', 'null'],
                    },
                    'request_status': {
                        'type': ['string', 'null'],
                    },
                    'status': {
                        'type': ['string', 'null'],
                    },
                    'supported_actions': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                    },
                    'destination': {
                        'type': ['object', 'null'],
                    },
                    'line_items': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'fulfill_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'fulfill_by': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'international_duties': {
                        'type': ['object', 'null'],
                    },
                    'fulfillment_holds': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'delivery_method': {
                        'type': ['object', 'null'],
                    },
                    'assigned_location': {
                        'type': ['object', 'null'],
                    },
                    'merchant_requests': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'fulfillment_orders',
                'x-airbyte-stream-name': 'fulfillment_orders',
                'x-airbyte-ai-hints': {
                    'summary': 'Fulfillment orders representing items to be shipped from a location',
                    'when_to_use': 'Questions about pending fulfillment or items to ship',
                    'trigger_phrases': ['fulfillment order', 'items to ship', 'pending fulfillment'],
                    'freshness': 'live',
                    'example_questions': ['What fulfillment orders are pending?'],
                    'search_strategy': 'Filter by order or location',
                },
            },
            ai_hints={
                'summary': 'Fulfillment orders representing items to be shipped from a location',
                'when_to_use': 'Questions about pending fulfillment or items to ship',
                'trigger_phrases': ['fulfillment order', 'items to ship', 'pending fulfillment'],
                'freshness': 'live',
                'example_questions': ['What fulfillment orders are pending?'],
                'search_strategy': 'Filter by order or location',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='fulfillment_orders',
                    target_entity='orders',
                    foreign_key='order_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='abandoned_checkouts',
                suggested=True,
                x_airbyte_name='abandoned_checkouts',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the abandoned checkout',
                    ),
                    CacheFieldConfig(
                        name='token',
                        type=['null', 'string'],
                        description='Unique token identifying the checkout',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='Email address provided for the checkout',
                    ),
                    CacheFieldConfig(
                        name='phone',
                        type=['null', 'string'],
                        description='Phone number provided for the checkout',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Shopify-assigned display name for the checkout (e.g. `#C12345`)',
                    ),
                    CacheFieldConfig(
                        name='currency',
                        type=['null', 'string'],
                        description='ISO 4217 currency code for the checkout totals',
                    ),
                    CacheFieldConfig(
                        name='total_price',
                        type=['null', 'string'],
                        description="Total price of the checkout in the shop's currency",
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the checkout was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the checkout was last updated',
                    ),
                    CacheFieldConfig(
                        name='completed_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the checkout was completed, if applicable',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='collects',
                x_airbyte_name='collects',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the collect',
                    ),
                    CacheFieldConfig(
                        name='collection_id',
                        type=['null', 'integer'],
                        description='Identifier of the collection the product belongs to',
                    ),
                    CacheFieldConfig(
                        name='product_id',
                        type=['null', 'integer'],
                        description='Identifier of the product in the collection',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'integer'],
                        description='Position of the product within the collection',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the collect was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the collect was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='countries',
                x_airbyte_name='countries',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the country tax row',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Human-readable country name',
                    ),
                    CacheFieldConfig(
                        name='code',
                        type=['null', 'string'],
                        description='ISO 3166-1 alpha-2 country code',
                    ),
                    CacheFieldConfig(
                        name='tax_name',
                        type=['null', 'string'],
                        description='Localized name of the tax applied in this country',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='custom_collections',
                x_airbyte_name='custom_collections',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the custom collection',
                    ),
                    CacheFieldConfig(
                        name='handle',
                        type=['null', 'string'],
                        description='URL-friendly handle for the custom collection',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Display title of the custom collection',
                    ),
                    CacheFieldConfig(
                        name='sort_order',
                        type=['null', 'string'],
                        description='How products are sorted within the collection (e.g. `best-selling`)',
                    ),
                    CacheFieldConfig(
                        name='published_scope',
                        type=['null', 'string'],
                        description='Publishing scope (`web` or `global`)',
                    ),
                    CacheFieldConfig(
                        name='published_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the collection was published',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the collection was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='customers',
                suggested=True,
                x_airbyte_name='customers',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the customer',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='Primary email address of the customer',
                    ),
                    CacheFieldConfig(
                        name='phone',
                        type=['null', 'string'],
                        description='Primary phone number of the customer',
                    ),
                    CacheFieldConfig(
                        name='first_name',
                        type=['null', 'string'],
                        description='First name of the customer',
                    ),
                    CacheFieldConfig(
                        name='last_name',
                        type=['null', 'string'],
                        description='Last name of the customer',
                    ),
                    CacheFieldConfig(
                        name='state',
                        type=['null', 'string'],
                        description='Account state (`disabled`, `invited`, `enabled`, `declined`)',
                    ),
                    CacheFieldConfig(
                        name='orders_count',
                        type=['null', 'integer'],
                        description='Number of orders placed by the customer',
                    ),
                    CacheFieldConfig(
                        name='total_spent',
                        type=['null', 'string'],
                        description='Total lifetime amount spent by the customer',
                    ),
                    CacheFieldConfig(
                        name='currency',
                        type=['null', 'string'],
                        description="ISO 4217 currency code for the customer's total spend",
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the customer record was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the customer record was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='discount_codes',
                suggested=True,
                x_airbyte_name='discount_codes',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the discount code',
                    ),
                    CacheFieldConfig(
                        name='price_rule_id',
                        type=['null', 'integer'],
                        description='Identifier of the parent price rule',
                    ),
                    CacheFieldConfig(
                        name='code',
                        type=['null', 'string'],
                        description='Discount code string shoppers enter at checkout',
                    ),
                    CacheFieldConfig(
                        name='usage_count',
                        type=['null', 'integer'],
                        description='Number of times the code has been redeemed',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the code was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the code was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='draft_orders',
                suggested=True,
                x_airbyte_name='draft_orders',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the draft order',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Shopify-assigned display name for the draft order (e.g. `#D12345`)',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='Email address associated with the draft order',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Status of the draft order (`open`, `invoice_sent`, `completed`)',
                    ),
                    CacheFieldConfig(
                        name='currency',
                        type=['null', 'string'],
                        description='ISO 4217 currency code for the draft order totals',
                    ),
                    CacheFieldConfig(
                        name='total_price',
                        type=['null', 'string'],
                        description='Total price of the draft order',
                    ),
                    CacheFieldConfig(
                        name='order_id',
                        type=['null', 'integer'],
                        description='Identifier of the completed order, if the draft has been completed',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the draft order was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the draft order was last updated',
                    ),
                    CacheFieldConfig(
                        name='completed_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the draft order was completed, if applicable',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='fulfillment_orders',
                x_airbyte_name='fulfillment_orders',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the fulfillment order',
                    ),
                    CacheFieldConfig(
                        name='order_id',
                        type=['null', 'integer'],
                        description='Identifier of the parent order',
                    ),
                    CacheFieldConfig(
                        name='shop_id',
                        type=['null', 'integer'],
                        description='Identifier of the shop that owns the fulfillment order',
                    ),
                    CacheFieldConfig(
                        name='assigned_location_id',
                        type=['null', 'integer'],
                        description='Identifier of the location assigned to fulfill the order',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Fulfillment order status (e.g. `open`, `in_progress`, `closed`)',
                    ),
                    CacheFieldConfig(
                        name='request_status',
                        type=['null', 'string'],
                        description='Status of the fulfillment request (e.g. `unsubmitted`, `submitted`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the fulfillment order was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the fulfillment order was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='fulfillments',
                suggested=True,
                x_airbyte_name='fulfillments',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the fulfillment',
                    ),
                    CacheFieldConfig(
                        name='order_id',
                        type=['null', 'integer'],
                        description='Identifier of the parent order',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Fulfillment status (e.g. `pending`, `open`, `success`, `cancelled`)',
                    ),
                    CacheFieldConfig(
                        name='shipment_status',
                        type=['null', 'string'],
                        description='Carrier shipment status (e.g. `delivered`, `in_transit`)',
                    ),
                    CacheFieldConfig(
                        name='tracking_company',
                        type=['null', 'string'],
                        description='Name of the shipping carrier',
                    ),
                    CacheFieldConfig(
                        name='tracking_number',
                        type=['null', 'string'],
                        description='Primary tracking number for the shipment',
                    ),
                    CacheFieldConfig(
                        name='location_id',
                        type=['null', 'integer'],
                        description='Identifier of the fulfilling location',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the fulfillment was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the fulfillment was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='inventory_items',
                suggested=True,
                x_airbyte_name='inventory_items',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the inventory item',
                    ),
                    CacheFieldConfig(
                        name='sku',
                        type=['null', 'string'],
                        description='Stock keeping unit associated with the inventory item',
                    ),
                    CacheFieldConfig(
                        name='tracked',
                        type=['null', 'boolean'],
                        description='Whether Shopify is tracking inventory for this item',
                    ),
                    CacheFieldConfig(
                        name='requires_shipping',
                        type=['null', 'boolean'],
                        description='Whether the item requires shipping',
                    ),
                    CacheFieldConfig(
                        name='country_code_of_origin',
                        type=['null', 'string'],
                        description="ISO country code of the item's country of origin",
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the inventory item was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the inventory item was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='inventory_levels',
                suggested=True,
                x_airbyte_name='inventory_levels',
                fields=[
                    CacheFieldConfig(
                        name='inventory_item_id',
                        type=['null', 'integer'],
                        description='Identifier of the inventory item',
                    ),
                    CacheFieldConfig(
                        name='location_id',
                        type=['null', 'integer'],
                        description='Identifier of the location holding the inventory',
                    ),
                    CacheFieldConfig(
                        name='available',
                        type=['null', 'integer'],
                        description='Number of units available at the location',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the inventory level was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='locations',
                x_airbyte_name='locations',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the location',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Display name of the location',
                    ),
                    CacheFieldConfig(
                        name='address1',
                        type=['null', 'string'],
                        description='Primary street address of the location',
                    ),
                    CacheFieldConfig(
                        name='city',
                        type=['null', 'string'],
                        description='City of the location',
                    ),
                    CacheFieldConfig(
                        name='province',
                        type=['null', 'string'],
                        description='Province, state, or region of the location',
                    ),
                    CacheFieldConfig(
                        name='country',
                        type=['null', 'string'],
                        description='Country name of the location',
                    ),
                    CacheFieldConfig(
                        name='country_code',
                        type=['null', 'string'],
                        description='ISO 3166-1 alpha-2 country code of the location',
                    ),
                    CacheFieldConfig(
                        name='phone',
                        type=['null', 'string'],
                        description='Phone number for the location',
                    ),
                    CacheFieldConfig(
                        name='active',
                        type=['null', 'boolean'],
                        description='Whether the location is currently active',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the location was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the location was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='metafield_customers',
                x_airbyte_name='metafield_customers',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the metafield',
                    ),
                    CacheFieldConfig(
                        name='namespace',
                        type=['null', 'string'],
                        description='Namespace group for the metafield',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['null', 'string'],
                        description='Key of the metafield within its namespace',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Serialized value stored in the metafield',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Shopify metafield type (e.g. `single_line_text_field`, `json`)',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Human-readable description of the metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_id',
                        type=['null', 'integer'],
                        description='Identifier of the resource that owns this metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_resource',
                        type=['null', 'string'],
                        description='Resource type that owns this metafield (e.g. `product`, `customer`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='metafield_draft_orders',
                x_airbyte_name='metafield_draft_orders',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the metafield',
                    ),
                    CacheFieldConfig(
                        name='namespace',
                        type=['null', 'string'],
                        description='Namespace group for the metafield',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['null', 'string'],
                        description='Key of the metafield within its namespace',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Serialized value stored in the metafield',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Shopify metafield type (e.g. `single_line_text_field`, `json`)',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Human-readable description of the metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_id',
                        type=['null', 'integer'],
                        description='Identifier of the resource that owns this metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_resource',
                        type=['null', 'string'],
                        description='Resource type that owns this metafield (e.g. `product`, `customer`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='metafield_locations',
                x_airbyte_name='metafield_locations',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the metafield',
                    ),
                    CacheFieldConfig(
                        name='namespace',
                        type=['null', 'string'],
                        description='Namespace group for the metafield',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['null', 'string'],
                        description='Key of the metafield within its namespace',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Serialized value stored in the metafield',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Shopify metafield type (e.g. `single_line_text_field`, `json`)',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Human-readable description of the metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_id',
                        type=['null', 'integer'],
                        description='Identifier of the resource that owns this metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_resource',
                        type=['null', 'string'],
                        description='Resource type that owns this metafield (e.g. `product`, `customer`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='metafield_orders',
                x_airbyte_name='metafield_orders',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the metafield',
                    ),
                    CacheFieldConfig(
                        name='namespace',
                        type=['null', 'string'],
                        description='Namespace group for the metafield',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['null', 'string'],
                        description='Key of the metafield within its namespace',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Serialized value stored in the metafield',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Shopify metafield type (e.g. `single_line_text_field`, `json`)',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Human-readable description of the metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_id',
                        type=['null', 'integer'],
                        description='Identifier of the resource that owns this metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_resource',
                        type=['null', 'string'],
                        description='Resource type that owns this metafield (e.g. `product`, `customer`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='metafield_product_images',
                x_airbyte_name='metafield_product_images',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the metafield',
                    ),
                    CacheFieldConfig(
                        name='namespace',
                        type=['null', 'string'],
                        description='Namespace group for the metafield',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['null', 'string'],
                        description='Key of the metafield within its namespace',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Serialized value stored in the metafield',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Shopify metafield type (e.g. `single_line_text_field`, `json`)',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Human-readable description of the metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_id',
                        type=['null', 'integer'],
                        description='Identifier of the resource that owns this metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_resource',
                        type=['null', 'string'],
                        description='Resource type that owns this metafield (e.g. `product`, `customer`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='metafield_product_variants',
                x_airbyte_name='metafield_product_variants',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the metafield',
                    ),
                    CacheFieldConfig(
                        name='namespace',
                        type=['null', 'string'],
                        description='Namespace group for the metafield',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['null', 'string'],
                        description='Key of the metafield within its namespace',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Serialized value stored in the metafield',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Shopify metafield type (e.g. `single_line_text_field`, `json`)',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Human-readable description of the metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_id',
                        type=['null', 'integer'],
                        description='Identifier of the resource that owns this metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_resource',
                        type=['null', 'string'],
                        description='Resource type that owns this metafield (e.g. `product`, `customer`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='metafield_products',
                x_airbyte_name='metafield_products',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the metafield',
                    ),
                    CacheFieldConfig(
                        name='namespace',
                        type=['null', 'string'],
                        description='Namespace group for the metafield',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['null', 'string'],
                        description='Key of the metafield within its namespace',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Serialized value stored in the metafield',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Shopify metafield type (e.g. `single_line_text_field`, `json`)',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Human-readable description of the metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_id',
                        type=['null', 'integer'],
                        description='Identifier of the resource that owns this metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_resource',
                        type=['null', 'string'],
                        description='Resource type that owns this metafield (e.g. `product`, `customer`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='metafield_shops',
                x_airbyte_name='metafield_shops',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the metafield',
                    ),
                    CacheFieldConfig(
                        name='namespace',
                        type=['null', 'string'],
                        description='Namespace group for the metafield',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['null', 'string'],
                        description='Key of the metafield within its namespace',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Serialized value stored in the metafield',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Shopify metafield type (e.g. `single_line_text_field`, `json`)',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Human-readable description of the metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_id',
                        type=['null', 'integer'],
                        description='Identifier of the resource that owns this metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_resource',
                        type=['null', 'string'],
                        description='Resource type that owns this metafield (e.g. `product`, `customer`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='metafield_smart_collections',
                x_airbyte_name='metafield_smart_collections',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the metafield',
                    ),
                    CacheFieldConfig(
                        name='namespace',
                        type=['null', 'string'],
                        description='Namespace group for the metafield',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['null', 'string'],
                        description='Key of the metafield within its namespace',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Serialized value stored in the metafield',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Shopify metafield type (e.g. `single_line_text_field`, `json`)',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Human-readable description of the metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_id',
                        type=['null', 'integer'],
                        description='Identifier of the resource that owns this metafield',
                    ),
                    CacheFieldConfig(
                        name='owner_resource',
                        type=['null', 'string'],
                        description='Resource type that owns this metafield (e.g. `product`, `customer`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the metafield was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='order_refunds',
                suggested=True,
                x_airbyte_name='order_refunds',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the refund',
                    ),
                    CacheFieldConfig(
                        name='order_id',
                        type=['null', 'integer'],
                        description='Identifier of the refunded order',
                    ),
                    CacheFieldConfig(
                        name='user_id',
                        type=['null', 'integer'],
                        description='Identifier of the staff user who processed the refund',
                    ),
                    CacheFieldConfig(
                        name='note',
                        type=['null', 'string'],
                        description='Merchant-provided note explaining the refund',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the refund was created',
                    ),
                    CacheFieldConfig(
                        name='processed_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the refund was processed',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='price_rules',
                x_airbyte_name='price_rules',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the price rule',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Administrative title of the price rule',
                    ),
                    CacheFieldConfig(
                        name='value_type',
                        type=['null', 'string'],
                        description='How the discount value is interpreted (`fixed_amount` or `percentage`)',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Discount value applied by the rule',
                    ),
                    CacheFieldConfig(
                        name='target_type',
                        type=['null', 'string'],
                        description='Type of target the rule applies to (`line_item` or `shipping_line`)',
                    ),
                    CacheFieldConfig(
                        name='target_selection',
                        type=['null', 'string'],
                        description='Which target items the rule applies to (`all` or `entitled`)',
                    ),
                    CacheFieldConfig(
                        name='allocation_method',
                        type=['null', 'string'],
                        description='How the discount is allocated (`each` or `across`)',
                    ),
                    CacheFieldConfig(
                        name='starts_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the rule starts being active',
                    ),
                    CacheFieldConfig(
                        name='ends_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the rule stops being active, if applicable',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the rule was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the rule was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='product_images',
                x_airbyte_name='product_images',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the product image',
                    ),
                    CacheFieldConfig(
                        name='product_id',
                        type=['null', 'integer'],
                        description='Identifier of the product the image belongs to',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'integer'],
                        description='Display position of the image within the product',
                    ),
                    CacheFieldConfig(
                        name='alt',
                        type=['null', 'string'],
                        description='Alt text for the image',
                    ),
                    CacheFieldConfig(
                        name='width',
                        type=['null', 'integer'],
                        description='Image width in pixels',
                    ),
                    CacheFieldConfig(
                        name='height',
                        type=['null', 'integer'],
                        description='Image height in pixels',
                    ),
                    CacheFieldConfig(
                        name='src',
                        type=['null', 'string'],
                        description='Public URL of the image',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the image was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the image was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='product_variants',
                suggested=True,
                x_airbyte_name='product_variants',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the product variant',
                    ),
                    CacheFieldConfig(
                        name='product_id',
                        type=['null', 'integer'],
                        description='Identifier of the parent product',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Display title of the variant',
                    ),
                    CacheFieldConfig(
                        name='sku',
                        type=['null', 'string'],
                        description='Stock keeping unit for the variant',
                    ),
                    CacheFieldConfig(
                        name='price',
                        type=['null', 'string'],
                        description="Price of the variant in the shop's currency",
                    ),
                    CacheFieldConfig(
                        name='compare_at_price',
                        type=['null', 'string'],
                        description='Original (compare-at) price of the variant, if set',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'integer'],
                        description='Display position of the variant within the product',
                    ),
                    CacheFieldConfig(
                        name='inventory_policy',
                        type=['null', 'string'],
                        description='Behaviour when out of stock (`deny` or `continue`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the variant was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the variant was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='shop',
                x_airbyte_name='shop',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the shop',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Display name of the shop',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='Primary contact email for the shop',
                    ),
                    CacheFieldConfig(
                        name='domain',
                        type=['null', 'string'],
                        description='Custom domain configured for the shop, if any',
                    ),
                    CacheFieldConfig(
                        name='myshopify_domain',
                        type=['null', 'string'],
                        description='Canonical `*.myshopify.com` domain for the shop',
                    ),
                    CacheFieldConfig(
                        name='country_code',
                        type=['null', 'string'],
                        description='ISO 3166-1 alpha-2 country code of the shop',
                    ),
                    CacheFieldConfig(
                        name='currency',
                        type=['null', 'string'],
                        description='ISO 4217 currency code used by the shop',
                    ),
                    CacheFieldConfig(
                        name='timezone',
                        type=['null', 'string'],
                        description='Timezone configured for the shop (e.g. `(GMT-05:00) Eastern Time`)',
                    ),
                    CacheFieldConfig(
                        name='plan_name',
                        type=['null', 'string'],
                        description='Shopify plan identifier (e.g. `shopify_plus`, `basic`)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the shop was created',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the shop was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='smart_collections',
                x_airbyte_name='smart_collections',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the smart collection',
                    ),
                    CacheFieldConfig(
                        name='handle',
                        type=['null', 'string'],
                        description='URL-friendly handle for the smart collection',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Display title of the smart collection',
                    ),
                    CacheFieldConfig(
                        name='sort_order',
                        type=['null', 'string'],
                        description='How products are sorted within the collection',
                    ),
                    CacheFieldConfig(
                        name='published_scope',
                        type=['null', 'string'],
                        description='Publishing scope (`web` or `global`)',
                    ),
                    CacheFieldConfig(
                        name='published_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the collection was published',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the collection was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='tender_transactions',
                x_airbyte_name='tender_transactions',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the tender transaction',
                    ),
                    CacheFieldConfig(
                        name='order_id',
                        type=['null', 'integer'],
                        description='Identifier of the order the transaction belongs to',
                    ),
                    CacheFieldConfig(
                        name='user_id',
                        type=['null', 'integer'],
                        description='Identifier of the staff user who processed the transaction',
                    ),
                    CacheFieldConfig(
                        name='amount',
                        type=['null', 'string'],
                        description="Amount of the transaction in the shop's currency",
                    ),
                    CacheFieldConfig(
                        name='currency',
                        type=['null', 'string'],
                        description='ISO 4217 currency code for the transaction amount',
                    ),
                    CacheFieldConfig(
                        name='payment_method',
                        type=['null', 'string'],
                        description='Payment method used (e.g. `credit_card`, `paypal`)',
                    ),
                    CacheFieldConfig(
                        name='test',
                        type=['null', 'boolean'],
                        description='Whether the transaction was a test transaction',
                    ),
                    CacheFieldConfig(
                        name='processed_at',
                        type=['null', 'string'],
                        description='ISO 8601 timestamp when the transaction was processed',
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'abandoned_checkouts': [
            'id',
            'token',
            'email',
            'phone',
            'name',
            'currency',
            'total_price',
            'created_at',
            'updated_at',
            'completed_at',
        ],
        'collects': [
            'id',
            'collection_id',
            'product_id',
            'position',
            'created_at',
            'updated_at',
        ],
        'countries': [
            'id',
            'name',
            'code',
            'tax_name',
        ],
        'custom_collections': [
            'id',
            'handle',
            'title',
            'sort_order',
            'published_scope',
            'published_at',
            'updated_at',
        ],
        'customers': [
            'id',
            'email',
            'phone',
            'first_name',
            'last_name',
            'state',
            'orders_count',
            'total_spent',
            'currency',
            'created_at',
            'updated_at',
        ],
        'discount_codes': [
            'id',
            'price_rule_id',
            'code',
            'usage_count',
            'created_at',
            'updated_at',
        ],
        'draft_orders': [
            'id',
            'name',
            'email',
            'status',
            'currency',
            'total_price',
            'order_id',
            'created_at',
            'updated_at',
            'completed_at',
        ],
        'fulfillment_orders': [
            'id',
            'order_id',
            'shop_id',
            'assigned_location_id',
            'status',
            'request_status',
            'created_at',
            'updated_at',
        ],
        'fulfillments': [
            'id',
            'order_id',
            'status',
            'shipment_status',
            'tracking_company',
            'tracking_number',
            'location_id',
            'created_at',
            'updated_at',
        ],
        'inventory_items': [
            'id',
            'sku',
            'tracked',
            'requires_shipping',
            'country_code_of_origin',
            'created_at',
            'updated_at',
        ],
        'inventory_levels': [
            'inventory_item_id',
            'location_id',
            'available',
            'updated_at',
        ],
        'locations': [
            'id',
            'name',
            'address1',
            'city',
            'province',
            'country',
            'country_code',
            'phone',
            'active',
            'created_at',
            'updated_at',
        ],
        'metafield_customers': [
            'id',
            'namespace',
            'key',
            'value',
            'type',
            'description',
            'owner_id',
            'owner_resource',
            'created_at',
            'updated_at',
        ],
        'metafield_draft_orders': [
            'id',
            'namespace',
            'key',
            'value',
            'type',
            'description',
            'owner_id',
            'owner_resource',
            'created_at',
            'updated_at',
        ],
        'metafield_locations': [
            'id',
            'namespace',
            'key',
            'value',
            'type',
            'description',
            'owner_id',
            'owner_resource',
            'created_at',
            'updated_at',
        ],
        'metafield_orders': [
            'id',
            'namespace',
            'key',
            'value',
            'type',
            'description',
            'owner_id',
            'owner_resource',
            'created_at',
            'updated_at',
        ],
        'metafield_product_images': [
            'id',
            'namespace',
            'key',
            'value',
            'type',
            'description',
            'owner_id',
            'owner_resource',
            'created_at',
            'updated_at',
        ],
        'metafield_product_variants': [
            'id',
            'namespace',
            'key',
            'value',
            'type',
            'description',
            'owner_id',
            'owner_resource',
            'created_at',
            'updated_at',
        ],
        'metafield_products': [
            'id',
            'namespace',
            'key',
            'value',
            'type',
            'description',
            'owner_id',
            'owner_resource',
            'created_at',
            'updated_at',
        ],
        'metafield_shops': [
            'id',
            'namespace',
            'key',
            'value',
            'type',
            'description',
            'owner_id',
            'owner_resource',
            'created_at',
            'updated_at',
        ],
        'metafield_smart_collections': [
            'id',
            'namespace',
            'key',
            'value',
            'type',
            'description',
            'owner_id',
            'owner_resource',
            'created_at',
            'updated_at',
        ],
        'order_refunds': [
            'id',
            'order_id',
            'user_id',
            'note',
            'created_at',
            'processed_at',
        ],
        'price_rules': [
            'id',
            'title',
            'value_type',
            'value',
            'target_type',
            'target_selection',
            'allocation_method',
            'starts_at',
            'ends_at',
            'created_at',
            'updated_at',
        ],
        'product_images': [
            'id',
            'product_id',
            'position',
            'alt',
            'width',
            'height',
            'src',
            'created_at',
            'updated_at',
        ],
        'product_variants': [
            'id',
            'product_id',
            'title',
            'sku',
            'price',
            'compare_at_price',
            'position',
            'inventory_policy',
            'created_at',
            'updated_at',
        ],
        'shop': [
            'id',
            'name',
            'email',
            'domain',
            'myshopify_domain',
            'country_code',
            'currency',
            'timezone',
            'plan_name',
            'created_at',
            'updated_at',
        ],
        'smart_collections': [
            'id',
            'handle',
            'title',
            'sort_order',
            'published_scope',
            'published_at',
            'updated_at',
        ],
        'tender_transactions': [
            'id',
            'order_id',
            'user_id',
            'amount',
            'currency',
            'payment_method',
            'test',
            'processed_at',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all customers in my Shopify store',
            'Show me details for a recent customer',
            'What products do I have in my store?',
            'List all locations for my store',
            'Show me inventory levels for a recent location',
            'Show me all draft orders',
            'List all custom collections in my store',
            'Show me details for a recent order',
            'Show me product variants for a recent product',
        ],
        context_store_search=['Show me orders from the last 30 days', 'Show me abandoned checkouts from this week', 'What price rules are currently active?'],
        search=['Show me orders from the last 30 days', 'Show me abandoned checkouts from this week', 'What price rules are currently active?'],
        unsupported=[
            'Create a new customer in Shopify',
            'Update product pricing',
            'Delete an order',
            'Process a refund',
            'Send shipping notification to customer',
            'Create a new discount code',
        ],
    ),
    server_variable_defaults={'shop': 'my-store'},
)