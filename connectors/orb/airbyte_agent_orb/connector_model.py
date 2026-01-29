"""
Connector model for orb.

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

OrbConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('7f0455fb-4518-4ec0-b7a3-d808bf8081cc'),
    name='orb',
    version='0.1.1',
    base_url='https://api.billwithorb.com/v1',
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
                    description='Your Orb API key',
                ),
            },
            auth_mapping={'token': '${api_key}'},
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
                    path='/customers',
                    action=Action.LIST,
                    description='Returns a paginated list of customers',
                    query_params=['limit', 'cursor'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of customers',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Customer object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The unique identifier of the customer'},
                                        'external_customer_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID of the customer in an external system',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the customer',
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                            'description': 'The email address of the customer',
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the customer was created',
                                        },
                                        'payment_provider': {
                                            'type': ['string', 'null'],
                                            'description': 'The payment provider used by the customer',
                                        },
                                        'payment_provider_id': {
                                            'type': ['string', 'null'],
                                            'description': "The ID of the customer in the payment provider's system",
                                        },
                                        'timezone': {
                                            'type': ['string', 'null'],
                                            'description': 'The timezone setting of the customer',
                                        },
                                        'shipping_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Address object',
                                                    'properties': {
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The city of the address',
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The country of the address',
                                                        },
                                                        'line1': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The first line of the address',
                                                        },
                                                        'line2': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The second line of the address',
                                                        },
                                                        'postal_code': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The postal code of the address',
                                                        },
                                                        'state': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The state or region of the address',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The shipping address of the customer',
                                        },
                                        'billing_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Address object',
                                                    'properties': {
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The city of the address',
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The country of the address',
                                                        },
                                                        'line1': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The first line of the address',
                                                        },
                                                        'line2': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The second line of the address',
                                                        },
                                                        'postal_code': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The postal code of the address',
                                                        },
                                                        'state': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The state or region of the address',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The billing address of the customer',
                                        },
                                        'balance': {
                                            'type': ['string', 'null'],
                                            'description': 'The current balance of the customer',
                                        },
                                        'currency': {
                                            'type': ['string', 'null'],
                                            'description': 'The currency of the customer',
                                        },
                                        'tax_id': {
                                            'type': ['object', 'null'],
                                            'description': 'Tax identification information',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The type of tax ID',
                                                },
                                                'value': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The value of the tax ID',
                                                },
                                                'country': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The country of the tax ID',
                                                },
                                            },
                                        },
                                        'auto_collection': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether auto collection is enabled',
                                        },
                                        'metadata': {
                                            'type': ['object', 'null'],
                                            'description': 'Additional metadata for the customer',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'customers',
                                    'x-airbyte-stream-name': 'customers',
                                },
                            },
                            'pagination_metadata': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'has_more': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether there are more results',
                                    },
                                    'next_cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'Cursor for the next page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination_metadata.next_cursor'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/customers/{customer_id}',
                    action=Action.GET,
                    description='Get a single customer by ID',
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Customer object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The unique identifier of the customer'},
                            'external_customer_id': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the customer in an external system',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the customer',
                            },
                            'email': {
                                'type': ['string', 'null'],
                                'description': 'The email address of the customer',
                            },
                            'created_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when the customer was created',
                            },
                            'payment_provider': {
                                'type': ['string', 'null'],
                                'description': 'The payment provider used by the customer',
                            },
                            'payment_provider_id': {
                                'type': ['string', 'null'],
                                'description': "The ID of the customer in the payment provider's system",
                            },
                            'timezone': {
                                'type': ['string', 'null'],
                                'description': 'The timezone setting of the customer',
                            },
                            'shipping_address': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Address object',
                                        'properties': {
                                            'city': {
                                                'type': ['string', 'null'],
                                                'description': 'The city of the address',
                                            },
                                            'country': {
                                                'type': ['string', 'null'],
                                                'description': 'The country of the address',
                                            },
                                            'line1': {
                                                'type': ['string', 'null'],
                                                'description': 'The first line of the address',
                                            },
                                            'line2': {
                                                'type': ['string', 'null'],
                                                'description': 'The second line of the address',
                                            },
                                            'postal_code': {
                                                'type': ['string', 'null'],
                                                'description': 'The postal code of the address',
                                            },
                                            'state': {
                                                'type': ['string', 'null'],
                                                'description': 'The state or region of the address',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The shipping address of the customer',
                            },
                            'billing_address': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Address object',
                                        'properties': {
                                            'city': {
                                                'type': ['string', 'null'],
                                                'description': 'The city of the address',
                                            },
                                            'country': {
                                                'type': ['string', 'null'],
                                                'description': 'The country of the address',
                                            },
                                            'line1': {
                                                'type': ['string', 'null'],
                                                'description': 'The first line of the address',
                                            },
                                            'line2': {
                                                'type': ['string', 'null'],
                                                'description': 'The second line of the address',
                                            },
                                            'postal_code': {
                                                'type': ['string', 'null'],
                                                'description': 'The postal code of the address',
                                            },
                                            'state': {
                                                'type': ['string', 'null'],
                                                'description': 'The state or region of the address',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The billing address of the customer',
                            },
                            'balance': {
                                'type': ['string', 'null'],
                                'description': 'The current balance of the customer',
                            },
                            'currency': {
                                'type': ['string', 'null'],
                                'description': 'The currency of the customer',
                            },
                            'tax_id': {
                                'type': ['object', 'null'],
                                'description': 'Tax identification information',
                                'properties': {
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'The type of tax ID',
                                    },
                                    'value': {
                                        'type': ['string', 'null'],
                                        'description': 'The value of the tax ID',
                                    },
                                    'country': {
                                        'type': ['string', 'null'],
                                        'description': 'The country of the tax ID',
                                    },
                                },
                            },
                            'auto_collection': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether auto collection is enabled',
                            },
                            'metadata': {
                                'type': ['object', 'null'],
                                'description': 'Additional metadata for the customer',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'customers',
                        'x-airbyte-stream-name': 'customers',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Customer object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The unique identifier of the customer'},
                    'external_customer_id': {
                        'type': ['string', 'null'],
                        'description': 'The ID of the customer in an external system',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the customer',
                    },
                    'email': {
                        'type': ['string', 'null'],
                        'description': 'The email address of the customer',
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when the customer was created',
                    },
                    'payment_provider': {
                        'type': ['string', 'null'],
                        'description': 'The payment provider used by the customer',
                    },
                    'payment_provider_id': {
                        'type': ['string', 'null'],
                        'description': "The ID of the customer in the payment provider's system",
                    },
                    'timezone': {
                        'type': ['string', 'null'],
                        'description': 'The timezone setting of the customer',
                    },
                    'shipping_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Address'},
                            {'type': 'null'},
                        ],
                        'description': 'The shipping address of the customer',
                    },
                    'billing_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Address'},
                            {'type': 'null'},
                        ],
                        'description': 'The billing address of the customer',
                    },
                    'balance': {
                        'type': ['string', 'null'],
                        'description': 'The current balance of the customer',
                    },
                    'currency': {
                        'type': ['string', 'null'],
                        'description': 'The currency of the customer',
                    },
                    'tax_id': {
                        'type': ['object', 'null'],
                        'description': 'Tax identification information',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'The type of tax ID',
                            },
                            'value': {
                                'type': ['string', 'null'],
                                'description': 'The value of the tax ID',
                            },
                            'country': {
                                'type': ['string', 'null'],
                                'description': 'The country of the tax ID',
                            },
                        },
                    },
                    'auto_collection': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether auto collection is enabled',
                    },
                    'metadata': {
                        'type': ['object', 'null'],
                        'description': 'Additional metadata for the customer',
                        'additionalProperties': True,
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'customers',
                'x-airbyte-stream-name': 'customers',
            },
        ),
        EntityDefinition(
            name='subscriptions',
            stream_name='subscriptions',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/subscriptions',
                    action=Action.LIST,
                    description='Returns a paginated list of subscriptions',
                    query_params=[
                        'limit',
                        'cursor',
                        'customer_id',
                        'external_customer_id',
                        'status',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'cursor': {'type': 'string', 'required': False},
                        'customer_id': {'type': 'string', 'required': False},
                        'external_customer_id': {'type': 'string', 'required': False},
                        'status': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of subscriptions',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Subscription object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The unique identifier of the subscription'},
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the subscription was created',
                                        },
                                        'start_date': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the subscription starts',
                                        },
                                        'end_date': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the subscription ends',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'The current status of the subscription',
                                        },
                                        'customer': {
                                            'type': ['object', 'null'],
                                            'description': 'The customer associated with the subscription',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The customer ID',
                                                },
                                                'external_customer_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The external customer ID',
                                                },
                                            },
                                        },
                                        'plan': {
                                            'type': ['object', 'null'],
                                            'description': 'The plan associated with the subscription',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The plan ID',
                                                },
                                                'name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The plan name',
                                                },
                                            },
                                        },
                                        'current_billing_period_start_date': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The start date of the current billing period',
                                        },
                                        'current_billing_period_end_date': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The end date of the current billing period',
                                        },
                                        'active_plan_phase_order': {
                                            'type': ['integer', 'null'],
                                            'description': 'The order of the active plan phase',
                                        },
                                        'fixed_fee_quantity_schedule': {
                                            'type': ['array', 'null'],
                                            'description': 'The fixed fee quantity schedule',
                                            'items': {'type': 'object'},
                                        },
                                        'price_intervals': {
                                            'type': ['array', 'null'],
                                            'description': 'The price intervals for the subscription',
                                            'items': {'type': 'object'},
                                        },
                                        'redeemed_coupon': {
                                            'type': ['object', 'null'],
                                            'description': 'The redeemed coupon for the subscription',
                                        },
                                        'default_invoice_memo': {
                                            'type': ['string', 'null'],
                                            'description': 'The default invoice memo',
                                        },
                                        'auto_collection': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether auto collection is enabled',
                                        },
                                        'net_terms': {
                                            'type': ['integer', 'null'],
                                            'description': 'The net terms for the subscription',
                                        },
                                        'invoicing_threshold': {
                                            'type': ['string', 'null'],
                                            'description': 'The invoicing threshold',
                                        },
                                        'metadata': {
                                            'type': ['object', 'null'],
                                            'description': 'Additional metadata for the subscription',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'subscriptions',
                                    'x-airbyte-stream-name': 'subscriptions',
                                },
                            },
                            'pagination_metadata': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'has_more': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether there are more results',
                                    },
                                    'next_cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'Cursor for the next page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination_metadata.next_cursor'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/subscriptions/{subscription_id}',
                    action=Action.GET,
                    description='Get a single subscription by ID',
                    path_params=['subscription_id'],
                    path_params_schema={
                        'subscription_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Subscription object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The unique identifier of the subscription'},
                            'created_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when the subscription was created',
                            },
                            'start_date': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when the subscription starts',
                            },
                            'end_date': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when the subscription ends',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'The current status of the subscription',
                            },
                            'customer': {
                                'type': ['object', 'null'],
                                'description': 'The customer associated with the subscription',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                        'description': 'The customer ID',
                                    },
                                    'external_customer_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The external customer ID',
                                    },
                                },
                            },
                            'plan': {
                                'type': ['object', 'null'],
                                'description': 'The plan associated with the subscription',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                        'description': 'The plan ID',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The plan name',
                                    },
                                },
                            },
                            'current_billing_period_start_date': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The start date of the current billing period',
                            },
                            'current_billing_period_end_date': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The end date of the current billing period',
                            },
                            'active_plan_phase_order': {
                                'type': ['integer', 'null'],
                                'description': 'The order of the active plan phase',
                            },
                            'fixed_fee_quantity_schedule': {
                                'type': ['array', 'null'],
                                'description': 'The fixed fee quantity schedule',
                                'items': {'type': 'object'},
                            },
                            'price_intervals': {
                                'type': ['array', 'null'],
                                'description': 'The price intervals for the subscription',
                                'items': {'type': 'object'},
                            },
                            'redeemed_coupon': {
                                'type': ['object', 'null'],
                                'description': 'The redeemed coupon for the subscription',
                            },
                            'default_invoice_memo': {
                                'type': ['string', 'null'],
                                'description': 'The default invoice memo',
                            },
                            'auto_collection': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether auto collection is enabled',
                            },
                            'net_terms': {
                                'type': ['integer', 'null'],
                                'description': 'The net terms for the subscription',
                            },
                            'invoicing_threshold': {
                                'type': ['string', 'null'],
                                'description': 'The invoicing threshold',
                            },
                            'metadata': {
                                'type': ['object', 'null'],
                                'description': 'Additional metadata for the subscription',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'subscriptions',
                        'x-airbyte-stream-name': 'subscriptions',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Subscription object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The unique identifier of the subscription'},
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when the subscription was created',
                    },
                    'start_date': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when the subscription starts',
                    },
                    'end_date': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when the subscription ends',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'The current status of the subscription',
                    },
                    'customer': {
                        'type': ['object', 'null'],
                        'description': 'The customer associated with the subscription',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                                'description': 'The customer ID',
                            },
                            'external_customer_id': {
                                'type': ['string', 'null'],
                                'description': 'The external customer ID',
                            },
                        },
                    },
                    'plan': {
                        'type': ['object', 'null'],
                        'description': 'The plan associated with the subscription',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                                'description': 'The plan ID',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The plan name',
                            },
                        },
                    },
                    'current_billing_period_start_date': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The start date of the current billing period',
                    },
                    'current_billing_period_end_date': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The end date of the current billing period',
                    },
                    'active_plan_phase_order': {
                        'type': ['integer', 'null'],
                        'description': 'The order of the active plan phase',
                    },
                    'fixed_fee_quantity_schedule': {
                        'type': ['array', 'null'],
                        'description': 'The fixed fee quantity schedule',
                        'items': {'type': 'object'},
                    },
                    'price_intervals': {
                        'type': ['array', 'null'],
                        'description': 'The price intervals for the subscription',
                        'items': {'type': 'object'},
                    },
                    'redeemed_coupon': {
                        'type': ['object', 'null'],
                        'description': 'The redeemed coupon for the subscription',
                    },
                    'default_invoice_memo': {
                        'type': ['string', 'null'],
                        'description': 'The default invoice memo',
                    },
                    'auto_collection': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether auto collection is enabled',
                    },
                    'net_terms': {
                        'type': ['integer', 'null'],
                        'description': 'The net terms for the subscription',
                    },
                    'invoicing_threshold': {
                        'type': ['string', 'null'],
                        'description': 'The invoicing threshold',
                    },
                    'metadata': {
                        'type': ['object', 'null'],
                        'description': 'Additional metadata for the subscription',
                        'additionalProperties': True,
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'subscriptions',
                'x-airbyte-stream-name': 'subscriptions',
            },
        ),
        EntityDefinition(
            name='plans',
            stream_name='plans',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/plans',
                    action=Action.LIST,
                    description='Returns a paginated list of plans',
                    query_params=['limit', 'cursor'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of plans',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Plan object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The unique identifier of the plan'},
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the plan was created',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the plan',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'A description of the plan',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'The status of the plan',
                                        },
                                        'default_invoice_memo': {
                                            'type': ['string', 'null'],
                                            'description': 'The default invoice memo for the plan',
                                        },
                                        'net_terms': {
                                            'type': ['integer', 'null'],
                                            'description': 'The net terms for the plan',
                                        },
                                        'currency': {
                                            'type': ['string', 'null'],
                                            'description': 'The currency of the plan',
                                        },
                                        'prices': {
                                            'type': ['array', 'null'],
                                            'description': 'The pricing options for the plan',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The unique identifier of the price',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The name of the price',
                                                    },
                                                    'price_type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The type of price',
                                                    },
                                                    'model_type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The model type of the price',
                                                    },
                                                    'currency': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The currency of the price',
                                                    },
                                                },
                                            },
                                        },
                                        'product': {
                                            'type': ['object', 'null'],
                                            'description': 'The product associated with the plan',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The product ID',
                                                },
                                                'name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The product name',
                                                },
                                            },
                                        },
                                        'minimum': {
                                            'type': ['object', 'null'],
                                            'description': 'The minimum configuration for the plan',
                                        },
                                        'maximum': {
                                            'type': ['object', 'null'],
                                            'description': 'The maximum configuration for the plan',
                                        },
                                        'discount': {
                                            'type': ['object', 'null'],
                                            'description': 'The discount configuration for the plan',
                                        },
                                        'trial_config': {
                                            'type': ['object', 'null'],
                                            'description': 'The trial configuration for the plan',
                                        },
                                        'plan_phases': {
                                            'type': ['array', 'null'],
                                            'description': 'The phases of the plan',
                                            'items': {'type': 'object'},
                                        },
                                        'external_plan_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The external plan ID',
                                        },
                                        'invoicing_currency': {
                                            'type': ['string', 'null'],
                                            'description': 'The invoicing currency',
                                        },
                                        'metadata': {
                                            'type': ['object', 'null'],
                                            'description': 'Additional metadata for the plan',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'plans',
                                    'x-airbyte-stream-name': 'plans',
                                },
                            },
                            'pagination_metadata': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'has_more': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether there are more results',
                                    },
                                    'next_cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'Cursor for the next page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination_metadata.next_cursor'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/plans/{plan_id}',
                    action=Action.GET,
                    description='Get a single plan by ID',
                    path_params=['plan_id'],
                    path_params_schema={
                        'plan_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Plan object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The unique identifier of the plan'},
                            'created_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when the plan was created',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the plan',
                            },
                            'description': {
                                'type': ['string', 'null'],
                                'description': 'A description of the plan',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'The status of the plan',
                            },
                            'default_invoice_memo': {
                                'type': ['string', 'null'],
                                'description': 'The default invoice memo for the plan',
                            },
                            'net_terms': {
                                'type': ['integer', 'null'],
                                'description': 'The net terms for the plan',
                            },
                            'currency': {
                                'type': ['string', 'null'],
                                'description': 'The currency of the plan',
                            },
                            'prices': {
                                'type': ['array', 'null'],
                                'description': 'The pricing options for the plan',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                            'description': 'The unique identifier of the price',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the price',
                                        },
                                        'price_type': {
                                            'type': ['string', 'null'],
                                            'description': 'The type of price',
                                        },
                                        'model_type': {
                                            'type': ['string', 'null'],
                                            'description': 'The model type of the price',
                                        },
                                        'currency': {
                                            'type': ['string', 'null'],
                                            'description': 'The currency of the price',
                                        },
                                    },
                                },
                            },
                            'product': {
                                'type': ['object', 'null'],
                                'description': 'The product associated with the plan',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                        'description': 'The product ID',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The product name',
                                    },
                                },
                            },
                            'minimum': {
                                'type': ['object', 'null'],
                                'description': 'The minimum configuration for the plan',
                            },
                            'maximum': {
                                'type': ['object', 'null'],
                                'description': 'The maximum configuration for the plan',
                            },
                            'discount': {
                                'type': ['object', 'null'],
                                'description': 'The discount configuration for the plan',
                            },
                            'trial_config': {
                                'type': ['object', 'null'],
                                'description': 'The trial configuration for the plan',
                            },
                            'plan_phases': {
                                'type': ['array', 'null'],
                                'description': 'The phases of the plan',
                                'items': {'type': 'object'},
                            },
                            'external_plan_id': {
                                'type': ['string', 'null'],
                                'description': 'The external plan ID',
                            },
                            'invoicing_currency': {
                                'type': ['string', 'null'],
                                'description': 'The invoicing currency',
                            },
                            'metadata': {
                                'type': ['object', 'null'],
                                'description': 'Additional metadata for the plan',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'plans',
                        'x-airbyte-stream-name': 'plans',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Plan object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The unique identifier of the plan'},
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when the plan was created',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the plan',
                    },
                    'description': {
                        'type': ['string', 'null'],
                        'description': 'A description of the plan',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'The status of the plan',
                    },
                    'default_invoice_memo': {
                        'type': ['string', 'null'],
                        'description': 'The default invoice memo for the plan',
                    },
                    'net_terms': {
                        'type': ['integer', 'null'],
                        'description': 'The net terms for the plan',
                    },
                    'currency': {
                        'type': ['string', 'null'],
                        'description': 'The currency of the plan',
                    },
                    'prices': {
                        'type': ['array', 'null'],
                        'description': 'The pricing options for the plan',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['string', 'null'],
                                    'description': 'The unique identifier of the price',
                                },
                                'name': {
                                    'type': ['string', 'null'],
                                    'description': 'The name of the price',
                                },
                                'price_type': {
                                    'type': ['string', 'null'],
                                    'description': 'The type of price',
                                },
                                'model_type': {
                                    'type': ['string', 'null'],
                                    'description': 'The model type of the price',
                                },
                                'currency': {
                                    'type': ['string', 'null'],
                                    'description': 'The currency of the price',
                                },
                            },
                        },
                    },
                    'product': {
                        'type': ['object', 'null'],
                        'description': 'The product associated with the plan',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                                'description': 'The product ID',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The product name',
                            },
                        },
                    },
                    'minimum': {
                        'type': ['object', 'null'],
                        'description': 'The minimum configuration for the plan',
                    },
                    'maximum': {
                        'type': ['object', 'null'],
                        'description': 'The maximum configuration for the plan',
                    },
                    'discount': {
                        'type': ['object', 'null'],
                        'description': 'The discount configuration for the plan',
                    },
                    'trial_config': {
                        'type': ['object', 'null'],
                        'description': 'The trial configuration for the plan',
                    },
                    'plan_phases': {
                        'type': ['array', 'null'],
                        'description': 'The phases of the plan',
                        'items': {'type': 'object'},
                    },
                    'external_plan_id': {
                        'type': ['string', 'null'],
                        'description': 'The external plan ID',
                    },
                    'invoicing_currency': {
                        'type': ['string', 'null'],
                        'description': 'The invoicing currency',
                    },
                    'metadata': {
                        'type': ['object', 'null'],
                        'description': 'Additional metadata for the plan',
                        'additionalProperties': True,
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'plans',
                'x-airbyte-stream-name': 'plans',
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
                    query_params=[
                        'limit',
                        'cursor',
                        'customer_id',
                        'external_customer_id',
                        'subscription_id',
                        'invoice_date_gt',
                        'invoice_date_gte',
                        'invoice_date_lt',
                        'invoice_date_lte',
                        'status',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'cursor': {'type': 'string', 'required': False},
                        'customer_id': {'type': 'string', 'required': False},
                        'external_customer_id': {'type': 'string', 'required': False},
                        'subscription_id': {'type': 'string', 'required': False},
                        'invoice_date_gt': {'type': 'string', 'required': False},
                        'invoice_date_gte': {'type': 'string', 'required': False},
                        'invoice_date_lt': {'type': 'string', 'required': False},
                        'invoice_date_lte': {'type': 'string', 'required': False},
                        'status': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of invoices',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Invoice object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The unique identifier of the invoice'},
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the invoice was created',
                                        },
                                        'invoice_date': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date of the invoice',
                                        },
                                        'due_date': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The due date for the invoice',
                                        },
                                        'invoice_pdf': {
                                            'type': ['string', 'null'],
                                            'description': 'The URL to download the PDF version of the invoice',
                                        },
                                        'subtotal': {
                                            'type': ['string', 'null'],
                                            'description': 'The subtotal amount of the invoice',
                                        },
                                        'total': {
                                            'type': ['string', 'null'],
                                            'description': 'The total amount of the invoice',
                                        },
                                        'amount_due': {
                                            'type': ['string', 'null'],
                                            'description': 'The amount due on the invoice',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'The current status of the invoice',
                                        },
                                        'memo': {
                                            'type': ['string', 'null'],
                                            'description': 'Any additional notes or comments on the invoice',
                                        },
                                        'issue_failed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when issuing the invoice failed',
                                        },
                                        'sync_failed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when syncing the invoice failed',
                                        },
                                        'payment_failed_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when payment failed',
                                        },
                                        'payment_started_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when payment started',
                                        },
                                        'voided_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the invoice was voided',
                                        },
                                        'paid_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the invoice was paid',
                                        },
                                        'issued_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the invoice was issued',
                                        },
                                        'hosted_invoice_url': {
                                            'type': ['string', 'null'],
                                            'description': 'The URL to view the hosted invoice',
                                        },
                                        'line_items': {
                                            'type': ['array', 'null'],
                                            'description': 'The line items on the invoice',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The unique identifier of the line item',
                                                    },
                                                    'quantity': {
                                                        'type': ['number', 'null'],
                                                        'description': 'The quantity of the line item',
                                                    },
                                                    'amount': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The amount of the line item',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The name of the line item',
                                                    },
                                                    'start_date': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'The start date of the line item',
                                                    },
                                                    'end_date': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'The end date of the line item',
                                                    },
                                                },
                                            },
                                        },
                                        'subscription': {
                                            'type': ['object', 'null'],
                                            'description': 'The subscription associated with the invoice',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The subscription ID',
                                                },
                                            },
                                        },
                                        'customer': {
                                            'type': ['object', 'null'],
                                            'description': 'The customer associated with the invoice',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The customer ID',
                                                },
                                                'external_customer_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The external customer ID',
                                                },
                                            },
                                        },
                                        'currency': {
                                            'type': ['string', 'null'],
                                            'description': 'The currency of the invoice',
                                        },
                                        'discount': {
                                            'type': ['object', 'null'],
                                            'description': 'The discount applied to the invoice',
                                        },
                                        'minimum': {
                                            'type': ['object', 'null'],
                                            'description': 'The minimum configuration for the invoice',
                                        },
                                        'maximum': {
                                            'type': ['object', 'null'],
                                            'description': 'The maximum configuration for the invoice',
                                        },
                                        'credit_notes': {
                                            'type': ['array', 'null'],
                                            'description': 'Credit notes associated with the invoice',
                                            'items': {'type': 'object'},
                                        },
                                        'will_auto_issue': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the invoice will auto issue',
                                        },
                                        'eligible_to_issue_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date when the invoice is eligible to issue',
                                        },
                                        'customer_balance_transactions': {
                                            'type': ['array', 'null'],
                                            'description': 'Customer balance transactions',
                                            'items': {'type': 'object'},
                                        },
                                        'auto_collection': {
                                            'type': ['object', 'null'],
                                            'description': 'Auto collection settings',
                                        },
                                        'invoice_number': {
                                            'type': ['string', 'null'],
                                            'description': 'The invoice number',
                                        },
                                        'billing_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Address object',
                                                    'properties': {
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The city of the address',
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The country of the address',
                                                        },
                                                        'line1': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The first line of the address',
                                                        },
                                                        'line2': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The second line of the address',
                                                        },
                                                        'postal_code': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The postal code of the address',
                                                        },
                                                        'state': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The state or region of the address',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The billing address on the invoice',
                                        },
                                        'shipping_address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Address object',
                                                    'properties': {
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The city of the address',
                                                        },
                                                        'country': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The country of the address',
                                                        },
                                                        'line1': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The first line of the address',
                                                        },
                                                        'line2': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The second line of the address',
                                                        },
                                                        'postal_code': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The postal code of the address',
                                                        },
                                                        'state': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The state or region of the address',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The shipping address on the invoice',
                                        },
                                        'metadata': {
                                            'type': ['object', 'null'],
                                            'description': 'Additional metadata for the invoice',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'invoices',
                                    'x-airbyte-stream-name': 'invoices',
                                },
                            },
                            'pagination_metadata': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'has_more': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether there are more results',
                                    },
                                    'next_cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'Cursor for the next page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination_metadata.next_cursor'},
                    untested=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/invoices/{invoice_id}',
                    action=Action.GET,
                    description='Get a single invoice by ID',
                    path_params=['invoice_id'],
                    path_params_schema={
                        'invoice_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Invoice object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The unique identifier of the invoice'},
                            'created_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when the invoice was created',
                            },
                            'invoice_date': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date of the invoice',
                            },
                            'due_date': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The due date for the invoice',
                            },
                            'invoice_pdf': {
                                'type': ['string', 'null'],
                                'description': 'The URL to download the PDF version of the invoice',
                            },
                            'subtotal': {
                                'type': ['string', 'null'],
                                'description': 'The subtotal amount of the invoice',
                            },
                            'total': {
                                'type': ['string', 'null'],
                                'description': 'The total amount of the invoice',
                            },
                            'amount_due': {
                                'type': ['string', 'null'],
                                'description': 'The amount due on the invoice',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'The current status of the invoice',
                            },
                            'memo': {
                                'type': ['string', 'null'],
                                'description': 'Any additional notes or comments on the invoice',
                            },
                            'issue_failed_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when issuing the invoice failed',
                            },
                            'sync_failed_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when syncing the invoice failed',
                            },
                            'payment_failed_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when payment failed',
                            },
                            'payment_started_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when payment started',
                            },
                            'voided_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when the invoice was voided',
                            },
                            'paid_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when the invoice was paid',
                            },
                            'issued_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time when the invoice was issued',
                            },
                            'hosted_invoice_url': {
                                'type': ['string', 'null'],
                                'description': 'The URL to view the hosted invoice',
                            },
                            'line_items': {
                                'type': ['array', 'null'],
                                'description': 'The line items on the invoice',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                            'description': 'The unique identifier of the line item',
                                        },
                                        'quantity': {
                                            'type': ['number', 'null'],
                                            'description': 'The quantity of the line item',
                                        },
                                        'amount': {
                                            'type': ['string', 'null'],
                                            'description': 'The amount of the line item',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the line item',
                                        },
                                        'start_date': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The start date of the line item',
                                        },
                                        'end_date': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The end date of the line item',
                                        },
                                    },
                                },
                            },
                            'subscription': {
                                'type': ['object', 'null'],
                                'description': 'The subscription associated with the invoice',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                        'description': 'The subscription ID',
                                    },
                                },
                            },
                            'customer': {
                                'type': ['object', 'null'],
                                'description': 'The customer associated with the invoice',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                        'description': 'The customer ID',
                                    },
                                    'external_customer_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The external customer ID',
                                    },
                                },
                            },
                            'currency': {
                                'type': ['string', 'null'],
                                'description': 'The currency of the invoice',
                            },
                            'discount': {
                                'type': ['object', 'null'],
                                'description': 'The discount applied to the invoice',
                            },
                            'minimum': {
                                'type': ['object', 'null'],
                                'description': 'The minimum configuration for the invoice',
                            },
                            'maximum': {
                                'type': ['object', 'null'],
                                'description': 'The maximum configuration for the invoice',
                            },
                            'credit_notes': {
                                'type': ['array', 'null'],
                                'description': 'Credit notes associated with the invoice',
                                'items': {'type': 'object'},
                            },
                            'will_auto_issue': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the invoice will auto issue',
                            },
                            'eligible_to_issue_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date when the invoice is eligible to issue',
                            },
                            'customer_balance_transactions': {
                                'type': ['array', 'null'],
                                'description': 'Customer balance transactions',
                                'items': {'type': 'object'},
                            },
                            'auto_collection': {
                                'type': ['object', 'null'],
                                'description': 'Auto collection settings',
                            },
                            'invoice_number': {
                                'type': ['string', 'null'],
                                'description': 'The invoice number',
                            },
                            'billing_address': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Address object',
                                        'properties': {
                                            'city': {
                                                'type': ['string', 'null'],
                                                'description': 'The city of the address',
                                            },
                                            'country': {
                                                'type': ['string', 'null'],
                                                'description': 'The country of the address',
                                            },
                                            'line1': {
                                                'type': ['string', 'null'],
                                                'description': 'The first line of the address',
                                            },
                                            'line2': {
                                                'type': ['string', 'null'],
                                                'description': 'The second line of the address',
                                            },
                                            'postal_code': {
                                                'type': ['string', 'null'],
                                                'description': 'The postal code of the address',
                                            },
                                            'state': {
                                                'type': ['string', 'null'],
                                                'description': 'The state or region of the address',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The billing address on the invoice',
                            },
                            'shipping_address': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Address object',
                                        'properties': {
                                            'city': {
                                                'type': ['string', 'null'],
                                                'description': 'The city of the address',
                                            },
                                            'country': {
                                                'type': ['string', 'null'],
                                                'description': 'The country of the address',
                                            },
                                            'line1': {
                                                'type': ['string', 'null'],
                                                'description': 'The first line of the address',
                                            },
                                            'line2': {
                                                'type': ['string', 'null'],
                                                'description': 'The second line of the address',
                                            },
                                            'postal_code': {
                                                'type': ['string', 'null'],
                                                'description': 'The postal code of the address',
                                            },
                                            'state': {
                                                'type': ['string', 'null'],
                                                'description': 'The state or region of the address',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The shipping address on the invoice',
                            },
                            'metadata': {
                                'type': ['object', 'null'],
                                'description': 'Additional metadata for the invoice',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'invoices',
                        'x-airbyte-stream-name': 'invoices',
                    },
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Invoice object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The unique identifier of the invoice'},
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when the invoice was created',
                    },
                    'invoice_date': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date of the invoice',
                    },
                    'due_date': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The due date for the invoice',
                    },
                    'invoice_pdf': {
                        'type': ['string', 'null'],
                        'description': 'The URL to download the PDF version of the invoice',
                    },
                    'subtotal': {
                        'type': ['string', 'null'],
                        'description': 'The subtotal amount of the invoice',
                    },
                    'total': {
                        'type': ['string', 'null'],
                        'description': 'The total amount of the invoice',
                    },
                    'amount_due': {
                        'type': ['string', 'null'],
                        'description': 'The amount due on the invoice',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'The current status of the invoice',
                    },
                    'memo': {
                        'type': ['string', 'null'],
                        'description': 'Any additional notes or comments on the invoice',
                    },
                    'issue_failed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when issuing the invoice failed',
                    },
                    'sync_failed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when syncing the invoice failed',
                    },
                    'payment_failed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when payment failed',
                    },
                    'payment_started_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when payment started',
                    },
                    'voided_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when the invoice was voided',
                    },
                    'paid_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when the invoice was paid',
                    },
                    'issued_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time when the invoice was issued',
                    },
                    'hosted_invoice_url': {
                        'type': ['string', 'null'],
                        'description': 'The URL to view the hosted invoice',
                    },
                    'line_items': {
                        'type': ['array', 'null'],
                        'description': 'The line items on the invoice',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['string', 'null'],
                                    'description': 'The unique identifier of the line item',
                                },
                                'quantity': {
                                    'type': ['number', 'null'],
                                    'description': 'The quantity of the line item',
                                },
                                'amount': {
                                    'type': ['string', 'null'],
                                    'description': 'The amount of the line item',
                                },
                                'name': {
                                    'type': ['string', 'null'],
                                    'description': 'The name of the line item',
                                },
                                'start_date': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'The start date of the line item',
                                },
                                'end_date': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'The end date of the line item',
                                },
                            },
                        },
                    },
                    'subscription': {
                        'type': ['object', 'null'],
                        'description': 'The subscription associated with the invoice',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                                'description': 'The subscription ID',
                            },
                        },
                    },
                    'customer': {
                        'type': ['object', 'null'],
                        'description': 'The customer associated with the invoice',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                                'description': 'The customer ID',
                            },
                            'external_customer_id': {
                                'type': ['string', 'null'],
                                'description': 'The external customer ID',
                            },
                        },
                    },
                    'currency': {
                        'type': ['string', 'null'],
                        'description': 'The currency of the invoice',
                    },
                    'discount': {
                        'type': ['object', 'null'],
                        'description': 'The discount applied to the invoice',
                    },
                    'minimum': {
                        'type': ['object', 'null'],
                        'description': 'The minimum configuration for the invoice',
                    },
                    'maximum': {
                        'type': ['object', 'null'],
                        'description': 'The maximum configuration for the invoice',
                    },
                    'credit_notes': {
                        'type': ['array', 'null'],
                        'description': 'Credit notes associated with the invoice',
                        'items': {'type': 'object'},
                    },
                    'will_auto_issue': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the invoice will auto issue',
                    },
                    'eligible_to_issue_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date when the invoice is eligible to issue',
                    },
                    'customer_balance_transactions': {
                        'type': ['array', 'null'],
                        'description': 'Customer balance transactions',
                        'items': {'type': 'object'},
                    },
                    'auto_collection': {
                        'type': ['object', 'null'],
                        'description': 'Auto collection settings',
                    },
                    'invoice_number': {
                        'type': ['string', 'null'],
                        'description': 'The invoice number',
                    },
                    'billing_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Address'},
                            {'type': 'null'},
                        ],
                        'description': 'The billing address on the invoice',
                    },
                    'shipping_address': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Address'},
                            {'type': 'null'},
                        ],
                        'description': 'The shipping address on the invoice',
                    },
                    'metadata': {
                        'type': ['object', 'null'],
                        'description': 'Additional metadata for the invoice',
                        'additionalProperties': True,
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'invoices',
                'x-airbyte-stream-name': 'invoices',
            },
        ),
    ],
    search_field_paths={
        'customers': [
            'id',
            'external_customer_id',
            'name',
            'email',
            'created_at',
            'payment_provider',
            'payment_provider_id',
            'timezone',
            'shipping_address',
            'billing_address',
            'balance',
            'currency',
            'auto_collection',
            'metadata',
        ],
        'subscriptions': [
            'id',
            'created_at',
            'start_date',
            'end_date',
            'status',
            'customer',
            'plan',
            'current_billing_period_start_date',
            'current_billing_period_end_date',
            'auto_collection',
            'net_terms',
            'metadata',
        ],
        'plans': [
            'id',
            'created_at',
            'name',
            'description',
            'status',
            'currency',
            'prices',
            'prices[]',
            'product',
            'external_plan_id',
            'metadata',
        ],
        'invoices': [
            'id',
            'created_at',
            'invoice_date',
            'due_date',
            'invoice_pdf',
            'subtotal',
            'total',
            'amount_due',
            'status',
            'memo',
            'paid_at',
            'issued_at',
            'hosted_invoice_url',
            'line_items',
            'line_items[]',
            'subscription',
            'customer',
            'currency',
            'invoice_number',
            'metadata',
        ],
    },
)