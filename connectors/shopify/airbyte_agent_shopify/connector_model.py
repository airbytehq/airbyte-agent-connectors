"""
Connector model for shopify.

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

ShopifyConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('9da77001-af33-4bcd-be46-6252bf9342b9'),
    name='shopify',
    version='0.1.3',
    base_url='https://{shop}.myshopify.com/admin/api/2025-01',
    auth=AuthConfig(
        type=AuthType.API_KEY,
        config={'header': 'X-Shopify-Access-Token', 'in': 'header'},
        user_config_spec=AirbyteAuthConfig(
            title='Access Token Authentication',
            type='object',
            required=['api_key', 'shop'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='Access Token',
                    description='Your Shopify Admin API access token',
                ),
                'shop': AuthConfigFieldSpec(
                    title='Shop Name',
                    description="Your Shopify store name (e.g., 'my-store' from my-store.myshopify.com)",
                ),
            },
            auth_mapping={'api_key': '${api_key}'},
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
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {'type': 'string', 'required': False},
                        'created_at_max': {'type': 'string', 'required': False},
                        'updated_at_min': {'type': 'string', 'required': False},
                        'updated_at_max': {'type': 'string', 'required': False},
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
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {'type': 'string', 'required': False},
                        'created_at_max': {'type': 'string', 'required': False},
                        'updated_at_min': {'type': 'string', 'required': False},
                        'updated_at_max': {'type': 'string', 'required': False},
                        'status': {
                            'type': 'string',
                            'required': False,
                            'default': 'any',
                        },
                        'financial_status': {'type': 'string', 'required': False},
                        'fulfillment_status': {'type': 'string', 'required': False},
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
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {'type': 'string', 'required': False},
                        'created_at_max': {'type': 'string', 'required': False},
                        'updated_at_min': {'type': 'string', 'required': False},
                        'updated_at_max': {'type': 'string', 'required': False},
                        'status': {'type': 'string', 'required': False},
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
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'products',
                                    'x-airbyte-stream-name': 'products',
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
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'products',
                                'x-airbyte-stream-name': 'products',
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
            },
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
            },
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
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {'type': 'string', 'required': False},
                        'created_at_max': {'type': 'string', 'required': False},
                        'updated_at_min': {'type': 'string', 'required': False},
                        'updated_at_max': {'type': 'string', 'required': False},
                        'status': {
                            'type': 'string',
                            'required': False,
                            'default': 'any',
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
            },
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
                        'ids': {'type': 'string', 'required': True},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
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
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {'type': 'string', 'required': False},
                        'created_at_max': {'type': 'string', 'required': False},
                        'updated_at_min': {'type': 'string', 'required': False},
                        'updated_at_max': {'type': 'string', 'required': False},
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
            },
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
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'title': {'type': 'string', 'required': False},
                        'product_id': {'type': 'integer', 'required': False},
                        'updated_at_min': {'type': 'string', 'required': False},
                        'updated_at_max': {'type': 'string', 'required': False},
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
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'title': {'type': 'string', 'required': False},
                        'product_id': {'type': 'integer', 'required': False},
                        'updated_at_min': {'type': 'string', 'required': False},
                        'updated_at_max': {'type': 'string', 'required': False},
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
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'status': {'type': 'string', 'required': False},
                        'updated_at_min': {'type': 'string', 'required': False},
                        'updated_at_max': {'type': 'string', 'required': False},
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
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'created_at_min': {'type': 'string', 'required': False},
                        'created_at_max': {'type': 'string', 'required': False},
                        'updated_at_min': {'type': 'string', 'required': False},
                        'updated_at_max': {'type': 'string', 'required': False},
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
            },
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
            },
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
            },
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
                        },
                        'since_id': {'type': 'integer', 'required': False},
                        'processed_at_min': {'type': 'string', 'required': False},
                        'processed_at_max': {'type': 'string', 'required': False},
                        'order': {'type': 'string', 'required': False},
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
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
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
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
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
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
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
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
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
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
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
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
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
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                ),
            },
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
                                },
                            },
                        },
                    },
                    record_extractor='$.metafields',
                    meta_extractor={'next_page_url': '@link.next'},
                    untested=True,
                ),
            },
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
            },
        ),
    ],
)