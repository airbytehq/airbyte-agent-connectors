"""
Connector model for woocommerce.

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
from ._vendored.connector_sdk.schema.extensions import (
    EntityRelationshipConfig,
)
from uuid import (
    UUID,
)

WoocommerceConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('2a2552ca-9f78-4c1c-9eb7-4d0dc66d72df'),
    name='woocommerce',
    version='1.0.3',
    base_url='https://{shop}/wp-json/wc/v3',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AirbyteAuthConfig(
            title='WooCommerce API Key Authentication',
            type='object',
            required=['api_key', 'api_secret'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='Consumer Key',
                    description='WooCommerce REST API consumer key (starts with ck_)',
                ),
                'api_secret': AuthConfigFieldSpec(
                    title='Consumer Secret',
                    description='WooCommerce REST API consumer secret (starts with cs_)',
                ),
            },
            auth_mapping={'username': '${api_key}', 'password': '${api_secret}'},
            replication_auth_key_mapping={'api_key': 'api_key', 'api_secret': 'api_secret'},
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
                    description='List customers',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'orderby',
                        'order',
                        'email',
                        'role',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'search': {'type': 'string', 'required': False},
                        'orderby': {
                            'type': 'string',
                            'required': False,
                            'default': 'name',
                        },
                        'order': {
                            'type': 'string',
                            'required': False,
                            'default': 'asc',
                        },
                        'email': {'type': 'string', 'required': False},
                        'role': {
                            'type': 'string',
                            'required': False,
                            'default': 'customer',
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'date_created': {
                                    'type': ['null', 'string'],
                                    'description': "The date the customer was created, in the site's timezone",
                                },
                                'date_created_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the customer was created, as GMT',
                                },
                                'date_modified': {
                                    'type': ['null', 'string'],
                                    'description': "The date the customer was last modified, in the site's timezone",
                                },
                                'date_modified_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the customer was last modified, as GMT',
                                },
                                'email': {
                                    'type': ['null', 'string'],
                                    'description': 'The email address for the customer',
                                },
                                'first_name': {
                                    'type': ['null', 'string'],
                                    'description': 'Customer first name',
                                },
                                'last_name': {
                                    'type': ['null', 'string'],
                                    'description': 'Customer last name',
                                },
                                'role': {
                                    'type': ['null', 'string'],
                                    'description': 'Customer role',
                                },
                                'username': {
                                    'type': ['null', 'string'],
                                    'description': 'Customer login name',
                                },
                                'billing': {
                                    'type': ['null', 'object'],
                                    'description': 'List of billing address data',
                                    'properties': {
                                        'first_name': {
                                            'type': ['null', 'string'],
                                        },
                                        'last_name': {
                                            'type': ['null', 'string'],
                                        },
                                        'company': {
                                            'type': ['null', 'string'],
                                        },
                                        'address_1': {
                                            'type': ['null', 'string'],
                                        },
                                        'address_2': {
                                            'type': ['null', 'string'],
                                        },
                                        'city': {
                                            'type': ['null', 'string'],
                                        },
                                        'state': {
                                            'type': ['null', 'string'],
                                        },
                                        'postcode': {
                                            'type': ['null', 'string'],
                                        },
                                        'country': {
                                            'type': ['null', 'string'],
                                        },
                                        'email': {
                                            'type': ['null', 'string'],
                                        },
                                        'phone': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'shipping': {
                                    'type': ['null', 'object'],
                                    'description': 'List of shipping address data',
                                    'properties': {
                                        'first_name': {
                                            'type': ['null', 'string'],
                                        },
                                        'last_name': {
                                            'type': ['null', 'string'],
                                        },
                                        'company': {
                                            'type': ['null', 'string'],
                                        },
                                        'address_1': {
                                            'type': ['null', 'string'],
                                        },
                                        'address_2': {
                                            'type': ['null', 'string'],
                                        },
                                        'city': {
                                            'type': ['null', 'string'],
                                        },
                                        'state': {
                                            'type': ['null', 'string'],
                                        },
                                        'postcode': {
                                            'type': ['null', 'string'],
                                        },
                                        'country': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'is_paying_customer': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Is the customer a paying customer',
                                },
                                'avatar_url': {
                                    'type': ['null', 'string'],
                                    'description': 'Avatar URL',
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'description': 'Meta data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                            'value': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                            'x-airbyte-entity-name': 'customers',
                            'x-airbyte-stream-name': 'customers',
                        },
                    },
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/customers/{id}',
                    action=Action.GET,
                    description='Retrieve a customer',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'description': "The date the customer was created, in the site's timezone",
                            },
                            'date_created_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the customer was created, as GMT',
                            },
                            'date_modified': {
                                'type': ['null', 'string'],
                                'description': "The date the customer was last modified, in the site's timezone",
                            },
                            'date_modified_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the customer was last modified, as GMT',
                            },
                            'email': {
                                'type': ['null', 'string'],
                                'description': 'The email address for the customer',
                            },
                            'first_name': {
                                'type': ['null', 'string'],
                                'description': 'Customer first name',
                            },
                            'last_name': {
                                'type': ['null', 'string'],
                                'description': 'Customer last name',
                            },
                            'role': {
                                'type': ['null', 'string'],
                                'description': 'Customer role',
                            },
                            'username': {
                                'type': ['null', 'string'],
                                'description': 'Customer login name',
                            },
                            'billing': {
                                'type': ['null', 'object'],
                                'description': 'List of billing address data',
                                'properties': {
                                    'first_name': {
                                        'type': ['null', 'string'],
                                    },
                                    'last_name': {
                                        'type': ['null', 'string'],
                                    },
                                    'company': {
                                        'type': ['null', 'string'],
                                    },
                                    'address_1': {
                                        'type': ['null', 'string'],
                                    },
                                    'address_2': {
                                        'type': ['null', 'string'],
                                    },
                                    'city': {
                                        'type': ['null', 'string'],
                                    },
                                    'state': {
                                        'type': ['null', 'string'],
                                    },
                                    'postcode': {
                                        'type': ['null', 'string'],
                                    },
                                    'country': {
                                        'type': ['null', 'string'],
                                    },
                                    'email': {
                                        'type': ['null', 'string'],
                                    },
                                    'phone': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'shipping': {
                                'type': ['null', 'object'],
                                'description': 'List of shipping address data',
                                'properties': {
                                    'first_name': {
                                        'type': ['null', 'string'],
                                    },
                                    'last_name': {
                                        'type': ['null', 'string'],
                                    },
                                    'company': {
                                        'type': ['null', 'string'],
                                    },
                                    'address_1': {
                                        'type': ['null', 'string'],
                                    },
                                    'address_2': {
                                        'type': ['null', 'string'],
                                    },
                                    'city': {
                                        'type': ['null', 'string'],
                                    },
                                    'state': {
                                        'type': ['null', 'string'],
                                    },
                                    'postcode': {
                                        'type': ['null', 'string'],
                                    },
                                    'country': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'is_paying_customer': {
                                'type': ['null', 'boolean'],
                                'description': 'Is the customer a paying customer',
                            },
                            'avatar_url': {
                                'type': ['null', 'string'],
                                'description': 'Avatar URL',
                            },
                            'meta_data': {
                                'type': ['null', 'array'],
                                'description': 'Meta data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'key': {
                                            'type': ['null', 'string'],
                                        },
                                        'value': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'customers',
                        'x-airbyte-stream-name': 'customers',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'description': "The date the customer was created, in the site's timezone",
                    },
                    'date_created_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the customer was created, as GMT',
                    },
                    'date_modified': {
                        'type': ['null', 'string'],
                        'description': "The date the customer was last modified, in the site's timezone",
                    },
                    'date_modified_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the customer was last modified, as GMT',
                    },
                    'email': {
                        'type': ['null', 'string'],
                        'description': 'The email address for the customer',
                    },
                    'first_name': {
                        'type': ['null', 'string'],
                        'description': 'Customer first name',
                    },
                    'last_name': {
                        'type': ['null', 'string'],
                        'description': 'Customer last name',
                    },
                    'role': {
                        'type': ['null', 'string'],
                        'description': 'Customer role',
                    },
                    'username': {
                        'type': ['null', 'string'],
                        'description': 'Customer login name',
                    },
                    'billing': {
                        'type': ['null', 'object'],
                        'description': 'List of billing address data',
                        'properties': {
                            'first_name': {
                                'type': ['null', 'string'],
                            },
                            'last_name': {
                                'type': ['null', 'string'],
                            },
                            'company': {
                                'type': ['null', 'string'],
                            },
                            'address_1': {
                                'type': ['null', 'string'],
                            },
                            'address_2': {
                                'type': ['null', 'string'],
                            },
                            'city': {
                                'type': ['null', 'string'],
                            },
                            'state': {
                                'type': ['null', 'string'],
                            },
                            'postcode': {
                                'type': ['null', 'string'],
                            },
                            'country': {
                                'type': ['null', 'string'],
                            },
                            'email': {
                                'type': ['null', 'string'],
                            },
                            'phone': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'shipping': {
                        'type': ['null', 'object'],
                        'description': 'List of shipping address data',
                        'properties': {
                            'first_name': {
                                'type': ['null', 'string'],
                            },
                            'last_name': {
                                'type': ['null', 'string'],
                            },
                            'company': {
                                'type': ['null', 'string'],
                            },
                            'address_1': {
                                'type': ['null', 'string'],
                            },
                            'address_2': {
                                'type': ['null', 'string'],
                            },
                            'city': {
                                'type': ['null', 'string'],
                            },
                            'state': {
                                'type': ['null', 'string'],
                            },
                            'postcode': {
                                'type': ['null', 'string'],
                            },
                            'country': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'is_paying_customer': {
                        'type': ['null', 'boolean'],
                        'description': 'Is the customer a paying customer',
                    },
                    'avatar_url': {
                        'type': ['null', 'string'],
                        'description': 'Avatar URL',
                    },
                    'meta_data': {
                        'type': ['null', 'array'],
                        'description': 'Meta data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'key': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                },
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
                    path='/orders',
                    action=Action.LIST,
                    description='List orders',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'after',
                        'before',
                        'modified_after',
                        'modified_before',
                        'status',
                        'customer',
                        'product',
                        'orderby',
                        'order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'search': {'type': 'string', 'required': False},
                        'after': {'type': 'string', 'required': False},
                        'before': {'type': 'string', 'required': False},
                        'modified_after': {'type': 'string', 'required': False},
                        'modified_before': {'type': 'string', 'required': False},
                        'status': {
                            'type': 'string',
                            'required': False,
                            'default': 'any',
                        },
                        'customer': {'type': 'integer', 'required': False},
                        'product': {'type': 'integer', 'required': False},
                        'orderby': {
                            'type': 'string',
                            'required': False,
                            'default': 'date',
                        },
                        'order': {
                            'type': 'string',
                            'required': False,
                            'default': 'desc',
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'parent_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Parent order ID',
                                },
                                'number': {
                                    'type': ['null', 'string'],
                                    'description': 'Order number',
                                },
                                'order_key': {
                                    'type': ['null', 'string'],
                                    'description': 'Order key',
                                },
                                'created_via': {
                                    'type': ['null', 'string'],
                                    'description': 'Shows where the order was created',
                                },
                                'version': {
                                    'type': ['null', 'string'],
                                    'description': 'Version of WooCommerce which last updated the order',
                                },
                                'status': {
                                    'type': ['null', 'string'],
                                    'description': 'Order status',
                                },
                                'currency': {
                                    'type': ['null', 'string'],
                                    'description': 'Currency the order was created with, in ISO format',
                                },
                                'currency_symbol': {
                                    'type': ['null', 'string'],
                                    'description': 'Currency symbol',
                                },
                                'date_created': {
                                    'type': ['null', 'string'],
                                    'description': "The date the order was created, in the site's timezone",
                                },
                                'date_created_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the order was created, as GMT',
                                },
                                'date_modified': {
                                    'type': ['null', 'string'],
                                    'description': "The date the order was last modified, in the site's timezone",
                                },
                                'date_modified_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the order was last modified, as GMT',
                                },
                                'discount_total': {
                                    'type': ['null', 'string'],
                                    'description': 'Total discount amount for the order',
                                },
                                'discount_tax': {
                                    'type': ['null', 'string'],
                                    'description': 'Total discount tax amount for the order',
                                },
                                'shipping_total': {
                                    'type': ['null', 'string'],
                                    'description': 'Total shipping amount for the order',
                                },
                                'shipping_tax': {
                                    'type': ['null', 'string'],
                                    'description': 'Total shipping tax amount for the order',
                                },
                                'cart_tax': {
                                    'type': ['null', 'string'],
                                    'description': 'Sum of line item taxes only',
                                },
                                'total': {
                                    'type': ['null', 'string'],
                                    'description': 'Grand total',
                                },
                                'total_tax': {
                                    'type': ['null', 'string'],
                                    'description': 'Sum of all taxes',
                                },
                                'prices_include_tax': {
                                    'type': ['null', 'boolean'],
                                    'description': 'True if the prices included tax during checkout',
                                },
                                'customer_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'User ID who owns the order (0 for guests)',
                                },
                                'customer_ip_address': {
                                    'type': ['null', 'string'],
                                    'description': "Customer's IP address",
                                },
                                'customer_user_agent': {
                                    'type': ['null', 'string'],
                                    'description': 'User agent of the customer',
                                },
                                'customer_note': {
                                    'type': ['null', 'string'],
                                    'description': 'Note left by the customer during checkout',
                                },
                                'billing': {
                                    'type': ['null', 'object'],
                                    'description': 'Billing address',
                                    'properties': {
                                        'first_name': {
                                            'type': ['null', 'string'],
                                        },
                                        'last_name': {
                                            'type': ['null', 'string'],
                                        },
                                        'company': {
                                            'type': ['null', 'string'],
                                        },
                                        'address_1': {
                                            'type': ['null', 'string'],
                                        },
                                        'address_2': {
                                            'type': ['null', 'string'],
                                        },
                                        'city': {
                                            'type': ['null', 'string'],
                                        },
                                        'state': {
                                            'type': ['null', 'string'],
                                        },
                                        'postcode': {
                                            'type': ['null', 'string'],
                                        },
                                        'country': {
                                            'type': ['null', 'string'],
                                        },
                                        'email': {
                                            'type': ['null', 'string'],
                                        },
                                        'phone': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'shipping': {
                                    'type': ['null', 'object'],
                                    'description': 'Shipping address',
                                    'properties': {
                                        'first_name': {
                                            'type': ['null', 'string'],
                                        },
                                        'last_name': {
                                            'type': ['null', 'string'],
                                        },
                                        'company': {
                                            'type': ['null', 'string'],
                                        },
                                        'address_1': {
                                            'type': ['null', 'string'],
                                        },
                                        'address_2': {
                                            'type': ['null', 'string'],
                                        },
                                        'city': {
                                            'type': ['null', 'string'],
                                        },
                                        'state': {
                                            'type': ['null', 'string'],
                                        },
                                        'postcode': {
                                            'type': ['null', 'string'],
                                        },
                                        'country': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'payment_method': {
                                    'type': ['null', 'string'],
                                    'description': 'Payment method ID',
                                },
                                'payment_method_title': {
                                    'type': ['null', 'string'],
                                    'description': 'Payment method title',
                                },
                                'transaction_id': {
                                    'type': ['null', 'string'],
                                    'description': 'Unique transaction ID',
                                },
                                'date_paid': {
                                    'type': ['null', 'string'],
                                    'description': "The date the order was paid, in the site's timezone",
                                },
                                'date_paid_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the order was paid, as GMT',
                                },
                                'date_completed': {
                                    'type': ['null', 'string'],
                                    'description': "The date the order was completed, in the site's timezone",
                                },
                                'date_completed_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the order was completed, as GMT',
                                },
                                'cart_hash': {
                                    'type': ['null', 'string'],
                                    'description': 'MD5 hash of cart items to ensure orders are not modified',
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'description': 'Meta data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'line_items': {
                                    'type': ['null', 'array'],
                                    'description': 'Line items data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'product_id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'variation_id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'quantity': {
                                                'type': ['null', 'integer'],
                                            },
                                            'tax_class': {
                                                'type': ['null', 'string'],
                                            },
                                            'subtotal': {
                                                'type': ['null', 'string'],
                                            },
                                            'subtotal_tax': {
                                                'type': ['null', 'string'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                            'total_tax': {
                                                'type': ['null', 'string'],
                                            },
                                            'taxes': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'total': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'subtotal': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                            'meta_data': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'key': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'display_key': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'display_value': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                            'sku': {
                                                'type': ['null', 'string'],
                                            },
                                            'price': {
                                                'type': ['null', 'number'],
                                            },
                                            'image': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer', 'string'],
                                                    },
                                                    'src': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                            'parent_name': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'tax_lines': {
                                    'type': ['null', 'array'],
                                    'description': 'Tax lines data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'rate_code': {
                                                'type': ['null', 'string'],
                                            },
                                            'rate_id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'label': {
                                                'type': ['null', 'string'],
                                            },
                                            'compound': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'tax_total': {
                                                'type': ['null', 'string'],
                                            },
                                            'shipping_tax_total': {
                                                'type': ['null', 'string'],
                                            },
                                            'meta_data': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'key': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'shipping_lines': {
                                    'type': ['null', 'array'],
                                    'description': 'Shipping lines data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'method_title': {
                                                'type': ['null', 'string'],
                                            },
                                            'method_id': {
                                                'type': ['null', 'string'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                            'total_tax': {
                                                'type': ['null', 'string'],
                                            },
                                            'taxes': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'total': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'subtotal': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                            'meta_data': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'key': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'fee_lines': {
                                    'type': ['null', 'array'],
                                    'description': 'Fee lines data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'tax_class': {
                                                'type': ['null', 'string'],
                                            },
                                            'tax_status': {
                                                'type': ['null', 'string'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                            'total_tax': {
                                                'type': ['null', 'string'],
                                            },
                                            'taxes': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'total': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'subtotal': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                            'meta_data': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'key': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'coupon_lines': {
                                    'type': ['null', 'array'],
                                    'description': 'Coupons line data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'code': {
                                                'type': ['null', 'string'],
                                            },
                                            'discount': {
                                                'type': ['null', 'string'],
                                            },
                                            'discount_tax': {
                                                'type': ['null', 'string'],
                                            },
                                            'meta_data': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'key': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'refunds': {
                                    'type': ['null', 'array'],
                                    'description': 'List of refunds',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'reason': {
                                                'type': ['null', 'string'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'payment_url': {
                                    'type': ['null', 'string'],
                                    'description': 'URL to the payment page for the order',
                                },
                                'is_editable': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the order is editable',
                                },
                                'needs_payment': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the order needs payment',
                                },
                                'needs_processing': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the order needs processing',
                                },
                            },
                            'x-airbyte-entity-name': 'orders',
                            'x-airbyte-stream-name': 'orders',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/orders/{id}',
                    action=Action.GET,
                    description='Retrieve an order',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'parent_id': {
                                'type': ['null', 'integer'],
                                'description': 'Parent order ID',
                            },
                            'number': {
                                'type': ['null', 'string'],
                                'description': 'Order number',
                            },
                            'order_key': {
                                'type': ['null', 'string'],
                                'description': 'Order key',
                            },
                            'created_via': {
                                'type': ['null', 'string'],
                                'description': 'Shows where the order was created',
                            },
                            'version': {
                                'type': ['null', 'string'],
                                'description': 'Version of WooCommerce which last updated the order',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'Order status',
                            },
                            'currency': {
                                'type': ['null', 'string'],
                                'description': 'Currency the order was created with, in ISO format',
                            },
                            'currency_symbol': {
                                'type': ['null', 'string'],
                                'description': 'Currency symbol',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'description': "The date the order was created, in the site's timezone",
                            },
                            'date_created_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the order was created, as GMT',
                            },
                            'date_modified': {
                                'type': ['null', 'string'],
                                'description': "The date the order was last modified, in the site's timezone",
                            },
                            'date_modified_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the order was last modified, as GMT',
                            },
                            'discount_total': {
                                'type': ['null', 'string'],
                                'description': 'Total discount amount for the order',
                            },
                            'discount_tax': {
                                'type': ['null', 'string'],
                                'description': 'Total discount tax amount for the order',
                            },
                            'shipping_total': {
                                'type': ['null', 'string'],
                                'description': 'Total shipping amount for the order',
                            },
                            'shipping_tax': {
                                'type': ['null', 'string'],
                                'description': 'Total shipping tax amount for the order',
                            },
                            'cart_tax': {
                                'type': ['null', 'string'],
                                'description': 'Sum of line item taxes only',
                            },
                            'total': {
                                'type': ['null', 'string'],
                                'description': 'Grand total',
                            },
                            'total_tax': {
                                'type': ['null', 'string'],
                                'description': 'Sum of all taxes',
                            },
                            'prices_include_tax': {
                                'type': ['null', 'boolean'],
                                'description': 'True if the prices included tax during checkout',
                            },
                            'customer_id': {
                                'type': ['null', 'integer'],
                                'description': 'User ID who owns the order (0 for guests)',
                            },
                            'customer_ip_address': {
                                'type': ['null', 'string'],
                                'description': "Customer's IP address",
                            },
                            'customer_user_agent': {
                                'type': ['null', 'string'],
                                'description': 'User agent of the customer',
                            },
                            'customer_note': {
                                'type': ['null', 'string'],
                                'description': 'Note left by the customer during checkout',
                            },
                            'billing': {
                                'type': ['null', 'object'],
                                'description': 'Billing address',
                                'properties': {
                                    'first_name': {
                                        'type': ['null', 'string'],
                                    },
                                    'last_name': {
                                        'type': ['null', 'string'],
                                    },
                                    'company': {
                                        'type': ['null', 'string'],
                                    },
                                    'address_1': {
                                        'type': ['null', 'string'],
                                    },
                                    'address_2': {
                                        'type': ['null', 'string'],
                                    },
                                    'city': {
                                        'type': ['null', 'string'],
                                    },
                                    'state': {
                                        'type': ['null', 'string'],
                                    },
                                    'postcode': {
                                        'type': ['null', 'string'],
                                    },
                                    'country': {
                                        'type': ['null', 'string'],
                                    },
                                    'email': {
                                        'type': ['null', 'string'],
                                    },
                                    'phone': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'shipping': {
                                'type': ['null', 'object'],
                                'description': 'Shipping address',
                                'properties': {
                                    'first_name': {
                                        'type': ['null', 'string'],
                                    },
                                    'last_name': {
                                        'type': ['null', 'string'],
                                    },
                                    'company': {
                                        'type': ['null', 'string'],
                                    },
                                    'address_1': {
                                        'type': ['null', 'string'],
                                    },
                                    'address_2': {
                                        'type': ['null', 'string'],
                                    },
                                    'city': {
                                        'type': ['null', 'string'],
                                    },
                                    'state': {
                                        'type': ['null', 'string'],
                                    },
                                    'postcode': {
                                        'type': ['null', 'string'],
                                    },
                                    'country': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'payment_method': {
                                'type': ['null', 'string'],
                                'description': 'Payment method ID',
                            },
                            'payment_method_title': {
                                'type': ['null', 'string'],
                                'description': 'Payment method title',
                            },
                            'transaction_id': {
                                'type': ['null', 'string'],
                                'description': 'Unique transaction ID',
                            },
                            'date_paid': {
                                'type': ['null', 'string'],
                                'description': "The date the order was paid, in the site's timezone",
                            },
                            'date_paid_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the order was paid, as GMT',
                            },
                            'date_completed': {
                                'type': ['null', 'string'],
                                'description': "The date the order was completed, in the site's timezone",
                            },
                            'date_completed_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the order was completed, as GMT',
                            },
                            'cart_hash': {
                                'type': ['null', 'string'],
                                'description': 'MD5 hash of cart items to ensure orders are not modified',
                            },
                            'meta_data': {
                                'type': ['null', 'array'],
                                'description': 'Meta data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'key': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'line_items': {
                                'type': ['null', 'array'],
                                'description': 'Line items data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'product_id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'variation_id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'quantity': {
                                            'type': ['null', 'integer'],
                                        },
                                        'tax_class': {
                                            'type': ['null', 'string'],
                                        },
                                        'subtotal': {
                                            'type': ['null', 'string'],
                                        },
                                        'subtotal_tax': {
                                            'type': ['null', 'string'],
                                        },
                                        'total': {
                                            'type': ['null', 'string'],
                                        },
                                        'total_tax': {
                                            'type': ['null', 'string'],
                                        },
                                        'taxes': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'total': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'subtotal': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                        'meta_data': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'key': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'display_key': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'display_value': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                        'sku': {
                                            'type': ['null', 'string'],
                                        },
                                        'price': {
                                            'type': ['null', 'number'],
                                        },
                                        'image': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'integer', 'string'],
                                                },
                                                'src': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'parent_name': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'tax_lines': {
                                'type': ['null', 'array'],
                                'description': 'Tax lines data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'rate_code': {
                                            'type': ['null', 'string'],
                                        },
                                        'rate_id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'label': {
                                            'type': ['null', 'string'],
                                        },
                                        'compound': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'tax_total': {
                                            'type': ['null', 'string'],
                                        },
                                        'shipping_tax_total': {
                                            'type': ['null', 'string'],
                                        },
                                        'meta_data': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'key': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'shipping_lines': {
                                'type': ['null', 'array'],
                                'description': 'Shipping lines data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'method_title': {
                                            'type': ['null', 'string'],
                                        },
                                        'method_id': {
                                            'type': ['null', 'string'],
                                        },
                                        'total': {
                                            'type': ['null', 'string'],
                                        },
                                        'total_tax': {
                                            'type': ['null', 'string'],
                                        },
                                        'taxes': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'total': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'subtotal': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                        'meta_data': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'key': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'fee_lines': {
                                'type': ['null', 'array'],
                                'description': 'Fee lines data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'tax_class': {
                                            'type': ['null', 'string'],
                                        },
                                        'tax_status': {
                                            'type': ['null', 'string'],
                                        },
                                        'total': {
                                            'type': ['null', 'string'],
                                        },
                                        'total_tax': {
                                            'type': ['null', 'string'],
                                        },
                                        'taxes': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'total': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'subtotal': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                        'meta_data': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'key': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'coupon_lines': {
                                'type': ['null', 'array'],
                                'description': 'Coupons line data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'code': {
                                            'type': ['null', 'string'],
                                        },
                                        'discount': {
                                            'type': ['null', 'string'],
                                        },
                                        'discount_tax': {
                                            'type': ['null', 'string'],
                                        },
                                        'meta_data': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'key': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'refunds': {
                                'type': ['null', 'array'],
                                'description': 'List of refunds',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'reason': {
                                            'type': ['null', 'string'],
                                        },
                                        'total': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'payment_url': {
                                'type': ['null', 'string'],
                                'description': 'URL to the payment page for the order',
                            },
                            'is_editable': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the order is editable',
                            },
                            'needs_payment': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the order needs payment',
                            },
                            'needs_processing': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the order needs processing',
                            },
                        },
                        'x-airbyte-entity-name': 'orders',
                        'x-airbyte-stream-name': 'orders',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'parent_id': {
                        'type': ['null', 'integer'],
                        'description': 'Parent order ID',
                    },
                    'number': {
                        'type': ['null', 'string'],
                        'description': 'Order number',
                    },
                    'order_key': {
                        'type': ['null', 'string'],
                        'description': 'Order key',
                    },
                    'created_via': {
                        'type': ['null', 'string'],
                        'description': 'Shows where the order was created',
                    },
                    'version': {
                        'type': ['null', 'string'],
                        'description': 'Version of WooCommerce which last updated the order',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Order status',
                    },
                    'currency': {
                        'type': ['null', 'string'],
                        'description': 'Currency the order was created with, in ISO format',
                    },
                    'currency_symbol': {
                        'type': ['null', 'string'],
                        'description': 'Currency symbol',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'description': "The date the order was created, in the site's timezone",
                    },
                    'date_created_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the order was created, as GMT',
                    },
                    'date_modified': {
                        'type': ['null', 'string'],
                        'description': "The date the order was last modified, in the site's timezone",
                    },
                    'date_modified_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the order was last modified, as GMT',
                    },
                    'discount_total': {
                        'type': ['null', 'string'],
                        'description': 'Total discount amount for the order',
                    },
                    'discount_tax': {
                        'type': ['null', 'string'],
                        'description': 'Total discount tax amount for the order',
                    },
                    'shipping_total': {
                        'type': ['null', 'string'],
                        'description': 'Total shipping amount for the order',
                    },
                    'shipping_tax': {
                        'type': ['null', 'string'],
                        'description': 'Total shipping tax amount for the order',
                    },
                    'cart_tax': {
                        'type': ['null', 'string'],
                        'description': 'Sum of line item taxes only',
                    },
                    'total': {
                        'type': ['null', 'string'],
                        'description': 'Grand total',
                    },
                    'total_tax': {
                        'type': ['null', 'string'],
                        'description': 'Sum of all taxes',
                    },
                    'prices_include_tax': {
                        'type': ['null', 'boolean'],
                        'description': 'True if the prices included tax during checkout',
                    },
                    'customer_id': {
                        'type': ['null', 'integer'],
                        'description': 'User ID who owns the order (0 for guests)',
                    },
                    'customer_ip_address': {
                        'type': ['null', 'string'],
                        'description': "Customer's IP address",
                    },
                    'customer_user_agent': {
                        'type': ['null', 'string'],
                        'description': 'User agent of the customer',
                    },
                    'customer_note': {
                        'type': ['null', 'string'],
                        'description': 'Note left by the customer during checkout',
                    },
                    'billing': {
                        'type': ['null', 'object'],
                        'description': 'Billing address',
                        'properties': {
                            'first_name': {
                                'type': ['null', 'string'],
                            },
                            'last_name': {
                                'type': ['null', 'string'],
                            },
                            'company': {
                                'type': ['null', 'string'],
                            },
                            'address_1': {
                                'type': ['null', 'string'],
                            },
                            'address_2': {
                                'type': ['null', 'string'],
                            },
                            'city': {
                                'type': ['null', 'string'],
                            },
                            'state': {
                                'type': ['null', 'string'],
                            },
                            'postcode': {
                                'type': ['null', 'string'],
                            },
                            'country': {
                                'type': ['null', 'string'],
                            },
                            'email': {
                                'type': ['null', 'string'],
                            },
                            'phone': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'shipping': {
                        'type': ['null', 'object'],
                        'description': 'Shipping address',
                        'properties': {
                            'first_name': {
                                'type': ['null', 'string'],
                            },
                            'last_name': {
                                'type': ['null', 'string'],
                            },
                            'company': {
                                'type': ['null', 'string'],
                            },
                            'address_1': {
                                'type': ['null', 'string'],
                            },
                            'address_2': {
                                'type': ['null', 'string'],
                            },
                            'city': {
                                'type': ['null', 'string'],
                            },
                            'state': {
                                'type': ['null', 'string'],
                            },
                            'postcode': {
                                'type': ['null', 'string'],
                            },
                            'country': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'payment_method': {
                        'type': ['null', 'string'],
                        'description': 'Payment method ID',
                    },
                    'payment_method_title': {
                        'type': ['null', 'string'],
                        'description': 'Payment method title',
                    },
                    'transaction_id': {
                        'type': ['null', 'string'],
                        'description': 'Unique transaction ID',
                    },
                    'date_paid': {
                        'type': ['null', 'string'],
                        'description': "The date the order was paid, in the site's timezone",
                    },
                    'date_paid_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the order was paid, as GMT',
                    },
                    'date_completed': {
                        'type': ['null', 'string'],
                        'description': "The date the order was completed, in the site's timezone",
                    },
                    'date_completed_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the order was completed, as GMT',
                    },
                    'cart_hash': {
                        'type': ['null', 'string'],
                        'description': 'MD5 hash of cart items to ensure orders are not modified',
                    },
                    'meta_data': {
                        'type': ['null', 'array'],
                        'description': 'Meta data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'key': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'line_items': {
                        'type': ['null', 'array'],
                        'description': 'Line items data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'product_id': {
                                    'type': ['null', 'integer'],
                                },
                                'variation_id': {
                                    'type': ['null', 'integer'],
                                },
                                'quantity': {
                                    'type': ['null', 'integer'],
                                },
                                'tax_class': {
                                    'type': ['null', 'string'],
                                },
                                'subtotal': {
                                    'type': ['null', 'string'],
                                },
                                'subtotal_tax': {
                                    'type': ['null', 'string'],
                                },
                                'total': {
                                    'type': ['null', 'string'],
                                },
                                'total_tax': {
                                    'type': ['null', 'string'],
                                },
                                'taxes': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                            'subtotal': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                            'display_key': {
                                                'type': ['null', 'string'],
                                            },
                                            'display_value': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'sku': {
                                    'type': ['null', 'string'],
                                },
                                'price': {
                                    'type': ['null', 'number'],
                                },
                                'image': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer', 'string'],
                                        },
                                        'src': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'parent_name': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'tax_lines': {
                        'type': ['null', 'array'],
                        'description': 'Tax lines data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'rate_code': {
                                    'type': ['null', 'string'],
                                },
                                'rate_id': {
                                    'type': ['null', 'integer'],
                                },
                                'label': {
                                    'type': ['null', 'string'],
                                },
                                'compound': {
                                    'type': ['null', 'boolean'],
                                },
                                'tax_total': {
                                    'type': ['null', 'string'],
                                },
                                'shipping_tax_total': {
                                    'type': ['null', 'string'],
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'shipping_lines': {
                        'type': ['null', 'array'],
                        'description': 'Shipping lines data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'method_title': {
                                    'type': ['null', 'string'],
                                },
                                'method_id': {
                                    'type': ['null', 'string'],
                                },
                                'total': {
                                    'type': ['null', 'string'],
                                },
                                'total_tax': {
                                    'type': ['null', 'string'],
                                },
                                'taxes': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                            'subtotal': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'fee_lines': {
                        'type': ['null', 'array'],
                        'description': 'Fee lines data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'tax_class': {
                                    'type': ['null', 'string'],
                                },
                                'tax_status': {
                                    'type': ['null', 'string'],
                                },
                                'total': {
                                    'type': ['null', 'string'],
                                },
                                'total_tax': {
                                    'type': ['null', 'string'],
                                },
                                'taxes': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                            'subtotal': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'coupon_lines': {
                        'type': ['null', 'array'],
                        'description': 'Coupons line data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'code': {
                                    'type': ['null', 'string'],
                                },
                                'discount': {
                                    'type': ['null', 'string'],
                                },
                                'discount_tax': {
                                    'type': ['null', 'string'],
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'refunds': {
                        'type': ['null', 'array'],
                        'description': 'List of refunds',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'reason': {
                                    'type': ['null', 'string'],
                                },
                                'total': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'payment_url': {
                        'type': ['null', 'string'],
                        'description': 'URL to the payment page for the order',
                    },
                    'is_editable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the order is editable',
                    },
                    'needs_payment': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the order needs payment',
                    },
                    'needs_processing': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the order needs processing',
                    },
                },
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
                    path='/products',
                    action=Action.LIST,
                    description='List products',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'after',
                        'before',
                        'modified_after',
                        'modified_before',
                        'status',
                        'type',
                        'sku',
                        'featured',
                        'category',
                        'tag',
                        'on_sale',
                        'min_price',
                        'max_price',
                        'stock_status',
                        'orderby',
                        'order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'search': {'type': 'string', 'required': False},
                        'after': {'type': 'string', 'required': False},
                        'before': {'type': 'string', 'required': False},
                        'modified_after': {'type': 'string', 'required': False},
                        'modified_before': {'type': 'string', 'required': False},
                        'status': {
                            'type': 'string',
                            'required': False,
                            'default': 'any',
                        },
                        'type': {'type': 'string', 'required': False},
                        'sku': {'type': 'string', 'required': False},
                        'featured': {'type': 'boolean', 'required': False},
                        'category': {'type': 'string', 'required': False},
                        'tag': {'type': 'string', 'required': False},
                        'on_sale': {'type': 'boolean', 'required': False},
                        'min_price': {'type': 'string', 'required': False},
                        'max_price': {'type': 'string', 'required': False},
                        'stock_status': {'type': 'string', 'required': False},
                        'orderby': {
                            'type': 'string',
                            'required': False,
                            'default': 'date',
                        },
                        'order': {
                            'type': 'string',
                            'required': False,
                            'default': 'desc',
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Product name',
                                },
                                'slug': {
                                    'type': ['null', 'string'],
                                    'description': 'Product slug',
                                },
                                'permalink': {
                                    'type': ['null', 'string'],
                                    'description': 'Product URL',
                                },
                                'date_created': {
                                    'type': ['null', 'string'],
                                    'description': "The date the product was created, in the site's timezone",
                                },
                                'date_created_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the product was created, as GMT',
                                },
                                'date_modified': {
                                    'type': ['null', 'string'],
                                    'description': "The date the product was last modified, in the site's timezone",
                                },
                                'date_modified_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the product was last modified, as GMT',
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                    'description': 'Product type (simple, grouped, external, variable)',
                                },
                                'status': {
                                    'type': ['null', 'string'],
                                    'description': 'Product status (draft, pending, private, publish)',
                                },
                                'featured': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Featured product',
                                },
                                'catalog_visibility': {
                                    'type': ['null', 'string'],
                                    'description': 'Catalog visibility (visible, catalog, search, hidden)',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Product description',
                                },
                                'short_description': {
                                    'type': ['null', 'string'],
                                    'description': 'Product short description',
                                },
                                'sku': {
                                    'type': ['null', 'string'],
                                    'description': 'Unique identifier (SKU)',
                                },
                                'price': {
                                    'type': ['null', 'string'],
                                    'description': 'Current product price',
                                },
                                'regular_price': {
                                    'type': ['null', 'string'],
                                    'description': 'Product regular price',
                                },
                                'sale_price': {
                                    'type': ['null', 'string'],
                                    'description': 'Product sale price',
                                },
                                'date_on_sale_from': {
                                    'type': ['null', 'string'],
                                    'description': "Start date of sale price, in the site's timezone",
                                },
                                'date_on_sale_from_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'Start date of sale price, as GMT',
                                },
                                'date_on_sale_to': {
                                    'type': ['null', 'string'],
                                    'description': "End date of sale price, in the site's timezone",
                                },
                                'date_on_sale_to_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'End date of sale price, as GMT',
                                },
                                'price_html': {
                                    'type': ['null', 'string'],
                                    'description': 'Price formatted in HTML',
                                },
                                'on_sale': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows if the product is on sale',
                                },
                                'purchasable': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows if the product can be bought',
                                },
                                'total_sales': {
                                    'type': ['null', 'integer'],
                                    'description': 'Amount of sales',
                                },
                                'virtual': {
                                    'type': ['null', 'boolean'],
                                    'description': 'If the product is virtual',
                                },
                                'downloadable': {
                                    'type': ['null', 'boolean'],
                                    'description': 'If the product is downloadable',
                                },
                                'downloads': {
                                    'type': ['null', 'array'],
                                    'description': 'List of downloadable files',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'string'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'file': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'download_limit': {
                                    'type': ['null', 'integer'],
                                    'description': 'Number of times downloadable files can be downloaded after purchase',
                                },
                                'download_expiry': {
                                    'type': ['null', 'integer'],
                                    'description': 'Number of days until access to downloadable files expires',
                                },
                                'external_url': {
                                    'type': ['null', 'string'],
                                    'description': 'Product external URL (only for external products)',
                                },
                                'button_text': {
                                    'type': ['null', 'string'],
                                    'description': 'Product external button text (only for external products)',
                                },
                                'tax_status': {
                                    'type': ['null', 'string'],
                                    'description': 'Tax status (taxable, shipping, none)',
                                },
                                'tax_class': {
                                    'type': ['null', 'string'],
                                    'description': 'Tax class',
                                },
                                'manage_stock': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Stock management at product level',
                                },
                                'stock_quantity': {
                                    'type': ['null', 'integer'],
                                    'description': 'Stock quantity',
                                },
                                'stock_status': {
                                    'type': ['null', 'string'],
                                    'description': 'Controls the stock status of the product',
                                },
                                'backorders': {
                                    'type': ['null', 'string'],
                                    'description': 'If managing stock, this controls if backorders are allowed',
                                },
                                'backorders_allowed': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows if backorders are allowed',
                                },
                                'backordered': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows if the product is on backordered',
                                },
                                'sold_individually': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Allow one item to be bought in a single order',
                                },
                                'weight': {
                                    'type': ['null', 'string'],
                                    'description': 'Product weight',
                                },
                                'dimensions': {
                                    'type': ['null', 'object'],
                                    'description': 'Product dimensions',
                                    'properties': {
                                        'length': {
                                            'type': ['null', 'string'],
                                        },
                                        'width': {
                                            'type': ['null', 'string'],
                                        },
                                        'height': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'shipping_required': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows if the product needs to be shipped',
                                },
                                'shipping_taxable': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows whether or not the product shipping is taxable',
                                },
                                'shipping_class': {
                                    'type': ['null', 'string'],
                                    'description': 'Shipping class slug',
                                },
                                'shipping_class_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Shipping class ID',
                                },
                                'reviews_allowed': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Allow reviews',
                                },
                                'average_rating': {
                                    'type': ['null', 'string'],
                                    'description': 'Reviews average rating',
                                },
                                'rating_count': {
                                    'type': ['null', 'integer'],
                                    'description': 'Amount of reviews that the product has',
                                },
                                'related_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'List of related products IDs',
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'upsell_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'List of up-sell products IDs',
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'cross_sell_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'List of cross-sell products IDs',
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'parent_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Product parent ID',
                                },
                                'purchase_note': {
                                    'type': ['null', 'string'],
                                    'description': 'Optional note to send the customer after purchase',
                                },
                                'categories': {
                                    'type': ['null', 'array'],
                                    'description': 'List of categories',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'slug': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'tags': {
                                    'type': ['null', 'array'],
                                    'description': 'List of tags',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'slug': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'images': {
                                    'type': ['null', 'array'],
                                    'description': 'List of images',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'date_created': {
                                                'type': ['null', 'string'],
                                            },
                                            'date_created_gmt': {
                                                'type': ['null', 'string'],
                                            },
                                            'date_modified': {
                                                'type': ['null', 'string'],
                                            },
                                            'date_modified_gmt': {
                                                'type': ['null', 'string'],
                                            },
                                            'src': {
                                                'type': ['null', 'string'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'alt': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'attributes': {
                                    'type': ['null', 'array'],
                                    'description': 'List of attributes',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'position': {
                                                'type': ['null', 'integer'],
                                            },
                                            'visible': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'variation': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'options': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                    },
                                },
                                'default_attributes': {
                                    'type': ['null', 'array'],
                                    'description': 'Defaults variation attributes',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'option': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'variations': {
                                    'type': ['null', 'array'],
                                    'description': 'List of variations IDs',
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'grouped_products': {
                                    'type': ['null', 'array'],
                                    'description': 'List of grouped products ID',
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'menu_order': {
                                    'type': ['null', 'integer'],
                                    'description': 'Menu order, used to custom sort products',
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'description': 'Meta data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'low_stock_amount': {
                                    'type': ['null', 'integer'],
                                    'description': 'Low stock amount threshold',
                                },
                                'brands': {
                                    'type': ['null', 'array'],
                                    'description': 'List of product brands',
                                    'items': {'type': 'object'},
                                },
                                'has_options': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the product has options',
                                },
                                'post_password': {
                                    'type': ['null', 'string'],
                                    'description': 'Post password',
                                },
                                'global_unique_id': {
                                    'type': ['null', 'string'],
                                    'description': 'GTIN, UPC, EAN or ISBN',
                                },
                            },
                            'x-airbyte-entity-name': 'products',
                            'x-airbyte-stream-name': 'products',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/products/{id}',
                    action=Action.GET,
                    description='Retrieve a product',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Product name',
                            },
                            'slug': {
                                'type': ['null', 'string'],
                                'description': 'Product slug',
                            },
                            'permalink': {
                                'type': ['null', 'string'],
                                'description': 'Product URL',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'description': "The date the product was created, in the site's timezone",
                            },
                            'date_created_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the product was created, as GMT',
                            },
                            'date_modified': {
                                'type': ['null', 'string'],
                                'description': "The date the product was last modified, in the site's timezone",
                            },
                            'date_modified_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the product was last modified, as GMT',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'Product type (simple, grouped, external, variable)',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'Product status (draft, pending, private, publish)',
                            },
                            'featured': {
                                'type': ['null', 'boolean'],
                                'description': 'Featured product',
                            },
                            'catalog_visibility': {
                                'type': ['null', 'string'],
                                'description': 'Catalog visibility (visible, catalog, search, hidden)',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Product description',
                            },
                            'short_description': {
                                'type': ['null', 'string'],
                                'description': 'Product short description',
                            },
                            'sku': {
                                'type': ['null', 'string'],
                                'description': 'Unique identifier (SKU)',
                            },
                            'price': {
                                'type': ['null', 'string'],
                                'description': 'Current product price',
                            },
                            'regular_price': {
                                'type': ['null', 'string'],
                                'description': 'Product regular price',
                            },
                            'sale_price': {
                                'type': ['null', 'string'],
                                'description': 'Product sale price',
                            },
                            'date_on_sale_from': {
                                'type': ['null', 'string'],
                                'description': "Start date of sale price, in the site's timezone",
                            },
                            'date_on_sale_from_gmt': {
                                'type': ['null', 'string'],
                                'description': 'Start date of sale price, as GMT',
                            },
                            'date_on_sale_to': {
                                'type': ['null', 'string'],
                                'description': "End date of sale price, in the site's timezone",
                            },
                            'date_on_sale_to_gmt': {
                                'type': ['null', 'string'],
                                'description': 'End date of sale price, as GMT',
                            },
                            'price_html': {
                                'type': ['null', 'string'],
                                'description': 'Price formatted in HTML',
                            },
                            'on_sale': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows if the product is on sale',
                            },
                            'purchasable': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows if the product can be bought',
                            },
                            'total_sales': {
                                'type': ['null', 'integer'],
                                'description': 'Amount of sales',
                            },
                            'virtual': {
                                'type': ['null', 'boolean'],
                                'description': 'If the product is virtual',
                            },
                            'downloadable': {
                                'type': ['null', 'boolean'],
                                'description': 'If the product is downloadable',
                            },
                            'downloads': {
                                'type': ['null', 'array'],
                                'description': 'List of downloadable files',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'file': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'download_limit': {
                                'type': ['null', 'integer'],
                                'description': 'Number of times downloadable files can be downloaded after purchase',
                            },
                            'download_expiry': {
                                'type': ['null', 'integer'],
                                'description': 'Number of days until access to downloadable files expires',
                            },
                            'external_url': {
                                'type': ['null', 'string'],
                                'description': 'Product external URL (only for external products)',
                            },
                            'button_text': {
                                'type': ['null', 'string'],
                                'description': 'Product external button text (only for external products)',
                            },
                            'tax_status': {
                                'type': ['null', 'string'],
                                'description': 'Tax status (taxable, shipping, none)',
                            },
                            'tax_class': {
                                'type': ['null', 'string'],
                                'description': 'Tax class',
                            },
                            'manage_stock': {
                                'type': ['null', 'boolean'],
                                'description': 'Stock management at product level',
                            },
                            'stock_quantity': {
                                'type': ['null', 'integer'],
                                'description': 'Stock quantity',
                            },
                            'stock_status': {
                                'type': ['null', 'string'],
                                'description': 'Controls the stock status of the product',
                            },
                            'backorders': {
                                'type': ['null', 'string'],
                                'description': 'If managing stock, this controls if backorders are allowed',
                            },
                            'backorders_allowed': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows if backorders are allowed',
                            },
                            'backordered': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows if the product is on backordered',
                            },
                            'sold_individually': {
                                'type': ['null', 'boolean'],
                                'description': 'Allow one item to be bought in a single order',
                            },
                            'weight': {
                                'type': ['null', 'string'],
                                'description': 'Product weight',
                            },
                            'dimensions': {
                                'type': ['null', 'object'],
                                'description': 'Product dimensions',
                                'properties': {
                                    'length': {
                                        'type': ['null', 'string'],
                                    },
                                    'width': {
                                        'type': ['null', 'string'],
                                    },
                                    'height': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'shipping_required': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows if the product needs to be shipped',
                            },
                            'shipping_taxable': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows whether or not the product shipping is taxable',
                            },
                            'shipping_class': {
                                'type': ['null', 'string'],
                                'description': 'Shipping class slug',
                            },
                            'shipping_class_id': {
                                'type': ['null', 'integer'],
                                'description': 'Shipping class ID',
                            },
                            'reviews_allowed': {
                                'type': ['null', 'boolean'],
                                'description': 'Allow reviews',
                            },
                            'average_rating': {
                                'type': ['null', 'string'],
                                'description': 'Reviews average rating',
                            },
                            'rating_count': {
                                'type': ['null', 'integer'],
                                'description': 'Amount of reviews that the product has',
                            },
                            'related_ids': {
                                'type': ['null', 'array'],
                                'description': 'List of related products IDs',
                                'items': {
                                    'type': ['null', 'integer'],
                                },
                            },
                            'upsell_ids': {
                                'type': ['null', 'array'],
                                'description': 'List of up-sell products IDs',
                                'items': {
                                    'type': ['null', 'integer'],
                                },
                            },
                            'cross_sell_ids': {
                                'type': ['null', 'array'],
                                'description': 'List of cross-sell products IDs',
                                'items': {
                                    'type': ['null', 'integer'],
                                },
                            },
                            'parent_id': {
                                'type': ['null', 'integer'],
                                'description': 'Product parent ID',
                            },
                            'purchase_note': {
                                'type': ['null', 'string'],
                                'description': 'Optional note to send the customer after purchase',
                            },
                            'categories': {
                                'type': ['null', 'array'],
                                'description': 'List of categories',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'slug': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'tags': {
                                'type': ['null', 'array'],
                                'description': 'List of tags',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'slug': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'images': {
                                'type': ['null', 'array'],
                                'description': 'List of images',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                        },
                                        'date_created_gmt': {
                                            'type': ['null', 'string'],
                                        },
                                        'date_modified': {
                                            'type': ['null', 'string'],
                                        },
                                        'date_modified_gmt': {
                                            'type': ['null', 'string'],
                                        },
                                        'src': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'alt': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'attributes': {
                                'type': ['null', 'array'],
                                'description': 'List of attributes',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'position': {
                                            'type': ['null', 'integer'],
                                        },
                                        'visible': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'variation': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'options': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                            'default_attributes': {
                                'type': ['null', 'array'],
                                'description': 'Defaults variation attributes',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'option': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'variations': {
                                'type': ['null', 'array'],
                                'description': 'List of variations IDs',
                                'items': {
                                    'type': ['null', 'integer'],
                                },
                            },
                            'grouped_products': {
                                'type': ['null', 'array'],
                                'description': 'List of grouped products ID',
                                'items': {
                                    'type': ['null', 'integer'],
                                },
                            },
                            'menu_order': {
                                'type': ['null', 'integer'],
                                'description': 'Menu order, used to custom sort products',
                            },
                            'meta_data': {
                                'type': ['null', 'array'],
                                'description': 'Meta data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'key': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'low_stock_amount': {
                                'type': ['null', 'integer'],
                                'description': 'Low stock amount threshold',
                            },
                            'brands': {
                                'type': ['null', 'array'],
                                'description': 'List of product brands',
                                'items': {'type': 'object'},
                            },
                            'has_options': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the product has options',
                            },
                            'post_password': {
                                'type': ['null', 'string'],
                                'description': 'Post password',
                            },
                            'global_unique_id': {
                                'type': ['null', 'string'],
                                'description': 'GTIN, UPC, EAN or ISBN',
                            },
                        },
                        'x-airbyte-entity-name': 'products',
                        'x-airbyte-stream-name': 'products',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Product name',
                    },
                    'slug': {
                        'type': ['null', 'string'],
                        'description': 'Product slug',
                    },
                    'permalink': {
                        'type': ['null', 'string'],
                        'description': 'Product URL',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'description': "The date the product was created, in the site's timezone",
                    },
                    'date_created_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the product was created, as GMT',
                    },
                    'date_modified': {
                        'type': ['null', 'string'],
                        'description': "The date the product was last modified, in the site's timezone",
                    },
                    'date_modified_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the product was last modified, as GMT',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Product type (simple, grouped, external, variable)',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Product status (draft, pending, private, publish)',
                    },
                    'featured': {
                        'type': ['null', 'boolean'],
                        'description': 'Featured product',
                    },
                    'catalog_visibility': {
                        'type': ['null', 'string'],
                        'description': 'Catalog visibility (visible, catalog, search, hidden)',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Product description',
                    },
                    'short_description': {
                        'type': ['null', 'string'],
                        'description': 'Product short description',
                    },
                    'sku': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier (SKU)',
                    },
                    'price': {
                        'type': ['null', 'string'],
                        'description': 'Current product price',
                    },
                    'regular_price': {
                        'type': ['null', 'string'],
                        'description': 'Product regular price',
                    },
                    'sale_price': {
                        'type': ['null', 'string'],
                        'description': 'Product sale price',
                    },
                    'date_on_sale_from': {
                        'type': ['null', 'string'],
                        'description': "Start date of sale price, in the site's timezone",
                    },
                    'date_on_sale_from_gmt': {
                        'type': ['null', 'string'],
                        'description': 'Start date of sale price, as GMT',
                    },
                    'date_on_sale_to': {
                        'type': ['null', 'string'],
                        'description': "End date of sale price, in the site's timezone",
                    },
                    'date_on_sale_to_gmt': {
                        'type': ['null', 'string'],
                        'description': 'End date of sale price, as GMT',
                    },
                    'price_html': {
                        'type': ['null', 'string'],
                        'description': 'Price formatted in HTML',
                    },
                    'on_sale': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows if the product is on sale',
                    },
                    'purchasable': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows if the product can be bought',
                    },
                    'total_sales': {
                        'type': ['null', 'integer'],
                        'description': 'Amount of sales',
                    },
                    'virtual': {
                        'type': ['null', 'boolean'],
                        'description': 'If the product is virtual',
                    },
                    'downloadable': {
                        'type': ['null', 'boolean'],
                        'description': 'If the product is downloadable',
                    },
                    'downloads': {
                        'type': ['null', 'array'],
                        'description': 'List of downloadable files',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'file': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'download_limit': {
                        'type': ['null', 'integer'],
                        'description': 'Number of times downloadable files can be downloaded after purchase',
                    },
                    'download_expiry': {
                        'type': ['null', 'integer'],
                        'description': 'Number of days until access to downloadable files expires',
                    },
                    'external_url': {
                        'type': ['null', 'string'],
                        'description': 'Product external URL (only for external products)',
                    },
                    'button_text': {
                        'type': ['null', 'string'],
                        'description': 'Product external button text (only for external products)',
                    },
                    'tax_status': {
                        'type': ['null', 'string'],
                        'description': 'Tax status (taxable, shipping, none)',
                    },
                    'tax_class': {
                        'type': ['null', 'string'],
                        'description': 'Tax class',
                    },
                    'manage_stock': {
                        'type': ['null', 'boolean'],
                        'description': 'Stock management at product level',
                    },
                    'stock_quantity': {
                        'type': ['null', 'integer'],
                        'description': 'Stock quantity',
                    },
                    'stock_status': {
                        'type': ['null', 'string'],
                        'description': 'Controls the stock status of the product',
                    },
                    'backorders': {
                        'type': ['null', 'string'],
                        'description': 'If managing stock, this controls if backorders are allowed',
                    },
                    'backorders_allowed': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows if backorders are allowed',
                    },
                    'backordered': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows if the product is on backordered',
                    },
                    'sold_individually': {
                        'type': ['null', 'boolean'],
                        'description': 'Allow one item to be bought in a single order',
                    },
                    'weight': {
                        'type': ['null', 'string'],
                        'description': 'Product weight',
                    },
                    'dimensions': {
                        'type': ['null', 'object'],
                        'description': 'Product dimensions',
                        'properties': {
                            'length': {
                                'type': ['null', 'string'],
                            },
                            'width': {
                                'type': ['null', 'string'],
                            },
                            'height': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'shipping_required': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows if the product needs to be shipped',
                    },
                    'shipping_taxable': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows whether or not the product shipping is taxable',
                    },
                    'shipping_class': {
                        'type': ['null', 'string'],
                        'description': 'Shipping class slug',
                    },
                    'shipping_class_id': {
                        'type': ['null', 'integer'],
                        'description': 'Shipping class ID',
                    },
                    'reviews_allowed': {
                        'type': ['null', 'boolean'],
                        'description': 'Allow reviews',
                    },
                    'average_rating': {
                        'type': ['null', 'string'],
                        'description': 'Reviews average rating',
                    },
                    'rating_count': {
                        'type': ['null', 'integer'],
                        'description': 'Amount of reviews that the product has',
                    },
                    'related_ids': {
                        'type': ['null', 'array'],
                        'description': 'List of related products IDs',
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'upsell_ids': {
                        'type': ['null', 'array'],
                        'description': 'List of up-sell products IDs',
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'cross_sell_ids': {
                        'type': ['null', 'array'],
                        'description': 'List of cross-sell products IDs',
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'parent_id': {
                        'type': ['null', 'integer'],
                        'description': 'Product parent ID',
                    },
                    'purchase_note': {
                        'type': ['null', 'string'],
                        'description': 'Optional note to send the customer after purchase',
                    },
                    'categories': {
                        'type': ['null', 'array'],
                        'description': 'List of categories',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'slug': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'tags': {
                        'type': ['null', 'array'],
                        'description': 'List of tags',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'slug': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'images': {
                        'type': ['null', 'array'],
                        'description': 'List of images',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'date_created': {
                                    'type': ['null', 'string'],
                                },
                                'date_created_gmt': {
                                    'type': ['null', 'string'],
                                },
                                'date_modified': {
                                    'type': ['null', 'string'],
                                },
                                'date_modified_gmt': {
                                    'type': ['null', 'string'],
                                },
                                'src': {
                                    'type': ['null', 'string'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'alt': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'attributes': {
                        'type': ['null', 'array'],
                        'description': 'List of attributes',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'position': {
                                    'type': ['null', 'integer'],
                                },
                                'visible': {
                                    'type': ['null', 'boolean'],
                                },
                                'variation': {
                                    'type': ['null', 'boolean'],
                                },
                                'options': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                    },
                    'default_attributes': {
                        'type': ['null', 'array'],
                        'description': 'Defaults variation attributes',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'option': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'variations': {
                        'type': ['null', 'array'],
                        'description': 'List of variations IDs',
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'grouped_products': {
                        'type': ['null', 'array'],
                        'description': 'List of grouped products ID',
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'menu_order': {
                        'type': ['null', 'integer'],
                        'description': 'Menu order, used to custom sort products',
                    },
                    'meta_data': {
                        'type': ['null', 'array'],
                        'description': 'Meta data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'key': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'low_stock_amount': {
                        'type': ['null', 'integer'],
                        'description': 'Low stock amount threshold',
                    },
                    'brands': {
                        'type': ['null', 'array'],
                        'description': 'List of product brands',
                        'items': {'type': 'object'},
                    },
                    'has_options': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the product has options',
                    },
                    'post_password': {
                        'type': ['null', 'string'],
                        'description': 'Post password',
                    },
                    'global_unique_id': {
                        'type': ['null', 'string'],
                        'description': 'GTIN, UPC, EAN or ISBN',
                    },
                },
                'x-airbyte-entity-name': 'products',
                'x-airbyte-stream-name': 'products',
            },
        ),
        EntityDefinition(
            name='coupons',
            stream_name='coupons',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/coupons',
                    action=Action.LIST,
                    description='List coupons',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'after',
                        'before',
                        'modified_after',
                        'modified_before',
                        'code',
                        'orderby',
                        'order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'search': {'type': 'string', 'required': False},
                        'after': {'type': 'string', 'required': False},
                        'before': {'type': 'string', 'required': False},
                        'modified_after': {'type': 'string', 'required': False},
                        'modified_before': {'type': 'string', 'required': False},
                        'code': {'type': 'string', 'required': False},
                        'orderby': {
                            'type': 'string',
                            'required': False,
                            'default': 'date',
                        },
                        'order': {
                            'type': 'string',
                            'required': False,
                            'default': 'desc',
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the object',
                                },
                                'code': {
                                    'type': ['null', 'string'],
                                    'description': 'Coupon code',
                                },
                                'amount': {
                                    'type': ['null', 'string'],
                                    'description': 'The amount of discount',
                                },
                                'date_created': {
                                    'type': ['null', 'string'],
                                    'description': "The date the coupon was created, in the site's timezone",
                                },
                                'date_created_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the coupon was created, as GMT',
                                },
                                'date_modified': {
                                    'type': ['null', 'string'],
                                    'description': "The date the coupon was last modified, in the site's timezone",
                                },
                                'date_modified_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the coupon was last modified, as GMT',
                                },
                                'discount_type': {
                                    'type': ['null', 'string'],
                                    'description': 'Determines the type of discount that will be applied',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Coupon description',
                                },
                                'date_expires': {
                                    'type': ['null', 'string'],
                                    'description': "The date the coupon expires, in the site's timezone",
                                },
                                'date_expires_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the coupon expires, as GMT',
                                },
                                'usage_count': {
                                    'type': ['null', 'integer'],
                                    'description': 'Number of times the coupon has been used already',
                                },
                                'individual_use': {
                                    'type': ['null', 'boolean'],
                                    'description': 'If true, the coupon can only be used individually',
                                },
                                'product_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'List of product IDs the coupon can be used on',
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'excluded_product_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'List of product IDs the coupon cannot be used on',
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'usage_limit': {
                                    'type': ['null', 'integer'],
                                    'description': 'How many times the coupon can be used in total',
                                },
                                'usage_limit_per_user': {
                                    'type': ['null', 'integer'],
                                    'description': 'How many times the coupon can be used per customer',
                                },
                                'limit_usage_to_x_items': {
                                    'type': ['null', 'integer'],
                                    'description': 'Max number of items in the cart the coupon can be applied to',
                                },
                                'free_shipping': {
                                    'type': ['null', 'boolean'],
                                    'description': 'If true and if the free shipping method requires a coupon, this coupon will enable free shipping',
                                },
                                'product_categories': {
                                    'type': ['null', 'array'],
                                    'description': 'List of category IDs the coupon applies to',
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'excluded_product_categories': {
                                    'type': ['null', 'array'],
                                    'description': 'List of category IDs the coupon does not apply to',
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'exclude_sale_items': {
                                    'type': ['null', 'boolean'],
                                    'description': 'If true, this coupon will not be applied to items that have sale prices',
                                },
                                'minimum_amount': {
                                    'type': ['null', 'string'],
                                    'description': 'Minimum order amount that needs to be in the cart before coupon applies',
                                },
                                'maximum_amount': {
                                    'type': ['null', 'string'],
                                    'description': 'Maximum order amount allowed when using the coupon',
                                },
                                'email_restrictions': {
                                    'type': ['null', 'array'],
                                    'description': 'List of email addresses that can use this coupon',
                                    'items': {
                                        'type': ['null', 'string'],
                                    },
                                },
                                'used_by': {
                                    'type': ['null', 'array'],
                                    'description': 'List of user IDs (or guest emails) that have used the coupon',
                                    'items': {
                                        'type': ['null', 'string'],
                                    },
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'description': 'Meta data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'status': {
                                    'type': ['null', 'string'],
                                    'description': 'Coupon status (publish, draft, pending, trash)',
                                },
                            },
                            'x-airbyte-entity-name': 'coupons',
                            'x-airbyte-stream-name': 'coupons',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/coupons/{id}',
                    action=Action.GET,
                    description='Retrieve a coupon',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the object',
                            },
                            'code': {
                                'type': ['null', 'string'],
                                'description': 'Coupon code',
                            },
                            'amount': {
                                'type': ['null', 'string'],
                                'description': 'The amount of discount',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'description': "The date the coupon was created, in the site's timezone",
                            },
                            'date_created_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the coupon was created, as GMT',
                            },
                            'date_modified': {
                                'type': ['null', 'string'],
                                'description': "The date the coupon was last modified, in the site's timezone",
                            },
                            'date_modified_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the coupon was last modified, as GMT',
                            },
                            'discount_type': {
                                'type': ['null', 'string'],
                                'description': 'Determines the type of discount that will be applied',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Coupon description',
                            },
                            'date_expires': {
                                'type': ['null', 'string'],
                                'description': "The date the coupon expires, in the site's timezone",
                            },
                            'date_expires_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the coupon expires, as GMT',
                            },
                            'usage_count': {
                                'type': ['null', 'integer'],
                                'description': 'Number of times the coupon has been used already',
                            },
                            'individual_use': {
                                'type': ['null', 'boolean'],
                                'description': 'If true, the coupon can only be used individually',
                            },
                            'product_ids': {
                                'type': ['null', 'array'],
                                'description': 'List of product IDs the coupon can be used on',
                                'items': {
                                    'type': ['null', 'integer'],
                                },
                            },
                            'excluded_product_ids': {
                                'type': ['null', 'array'],
                                'description': 'List of product IDs the coupon cannot be used on',
                                'items': {
                                    'type': ['null', 'integer'],
                                },
                            },
                            'usage_limit': {
                                'type': ['null', 'integer'],
                                'description': 'How many times the coupon can be used in total',
                            },
                            'usage_limit_per_user': {
                                'type': ['null', 'integer'],
                                'description': 'How many times the coupon can be used per customer',
                            },
                            'limit_usage_to_x_items': {
                                'type': ['null', 'integer'],
                                'description': 'Max number of items in the cart the coupon can be applied to',
                            },
                            'free_shipping': {
                                'type': ['null', 'boolean'],
                                'description': 'If true and if the free shipping method requires a coupon, this coupon will enable free shipping',
                            },
                            'product_categories': {
                                'type': ['null', 'array'],
                                'description': 'List of category IDs the coupon applies to',
                                'items': {
                                    'type': ['null', 'integer'],
                                },
                            },
                            'excluded_product_categories': {
                                'type': ['null', 'array'],
                                'description': 'List of category IDs the coupon does not apply to',
                                'items': {
                                    'type': ['null', 'integer'],
                                },
                            },
                            'exclude_sale_items': {
                                'type': ['null', 'boolean'],
                                'description': 'If true, this coupon will not be applied to items that have sale prices',
                            },
                            'minimum_amount': {
                                'type': ['null', 'string'],
                                'description': 'Minimum order amount that needs to be in the cart before coupon applies',
                            },
                            'maximum_amount': {
                                'type': ['null', 'string'],
                                'description': 'Maximum order amount allowed when using the coupon',
                            },
                            'email_restrictions': {
                                'type': ['null', 'array'],
                                'description': 'List of email addresses that can use this coupon',
                                'items': {
                                    'type': ['null', 'string'],
                                },
                            },
                            'used_by': {
                                'type': ['null', 'array'],
                                'description': 'List of user IDs (or guest emails) that have used the coupon',
                                'items': {
                                    'type': ['null', 'string'],
                                },
                            },
                            'meta_data': {
                                'type': ['null', 'array'],
                                'description': 'Meta data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'key': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'Coupon status (publish, draft, pending, trash)',
                            },
                        },
                        'x-airbyte-entity-name': 'coupons',
                        'x-airbyte-stream-name': 'coupons',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the object',
                    },
                    'code': {
                        'type': ['null', 'string'],
                        'description': 'Coupon code',
                    },
                    'amount': {
                        'type': ['null', 'string'],
                        'description': 'The amount of discount',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'description': "The date the coupon was created, in the site's timezone",
                    },
                    'date_created_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the coupon was created, as GMT',
                    },
                    'date_modified': {
                        'type': ['null', 'string'],
                        'description': "The date the coupon was last modified, in the site's timezone",
                    },
                    'date_modified_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the coupon was last modified, as GMT',
                    },
                    'discount_type': {
                        'type': ['null', 'string'],
                        'description': 'Determines the type of discount that will be applied',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Coupon description',
                    },
                    'date_expires': {
                        'type': ['null', 'string'],
                        'description': "The date the coupon expires, in the site's timezone",
                    },
                    'date_expires_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the coupon expires, as GMT',
                    },
                    'usage_count': {
                        'type': ['null', 'integer'],
                        'description': 'Number of times the coupon has been used already',
                    },
                    'individual_use': {
                        'type': ['null', 'boolean'],
                        'description': 'If true, the coupon can only be used individually',
                    },
                    'product_ids': {
                        'type': ['null', 'array'],
                        'description': 'List of product IDs the coupon can be used on',
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'excluded_product_ids': {
                        'type': ['null', 'array'],
                        'description': 'List of product IDs the coupon cannot be used on',
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'usage_limit': {
                        'type': ['null', 'integer'],
                        'description': 'How many times the coupon can be used in total',
                    },
                    'usage_limit_per_user': {
                        'type': ['null', 'integer'],
                        'description': 'How many times the coupon can be used per customer',
                    },
                    'limit_usage_to_x_items': {
                        'type': ['null', 'integer'],
                        'description': 'Max number of items in the cart the coupon can be applied to',
                    },
                    'free_shipping': {
                        'type': ['null', 'boolean'],
                        'description': 'If true and if the free shipping method requires a coupon, this coupon will enable free shipping',
                    },
                    'product_categories': {
                        'type': ['null', 'array'],
                        'description': 'List of category IDs the coupon applies to',
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'excluded_product_categories': {
                        'type': ['null', 'array'],
                        'description': 'List of category IDs the coupon does not apply to',
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'exclude_sale_items': {
                        'type': ['null', 'boolean'],
                        'description': 'If true, this coupon will not be applied to items that have sale prices',
                    },
                    'minimum_amount': {
                        'type': ['null', 'string'],
                        'description': 'Minimum order amount that needs to be in the cart before coupon applies',
                    },
                    'maximum_amount': {
                        'type': ['null', 'string'],
                        'description': 'Maximum order amount allowed when using the coupon',
                    },
                    'email_restrictions': {
                        'type': ['null', 'array'],
                        'description': 'List of email addresses that can use this coupon',
                        'items': {
                            'type': ['null', 'string'],
                        },
                    },
                    'used_by': {
                        'type': ['null', 'array'],
                        'description': 'List of user IDs (or guest emails) that have used the coupon',
                        'items': {
                            'type': ['null', 'string'],
                        },
                    },
                    'meta_data': {
                        'type': ['null', 'array'],
                        'description': 'Meta data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'key': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Coupon status (publish, draft, pending, trash)',
                    },
                },
                'x-airbyte-entity-name': 'coupons',
                'x-airbyte-stream-name': 'coupons',
            },
        ),
        EntityDefinition(
            name='product_categories',
            stream_name='product_categories',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/products/categories',
                    action=Action.LIST,
                    description='List product categories',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'orderby',
                        'order',
                        'hide_empty',
                        'parent',
                        'product',
                        'slug',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'search': {'type': 'string', 'required': False},
                        'orderby': {
                            'type': 'string',
                            'required': False,
                            'default': 'name',
                        },
                        'order': {
                            'type': 'string',
                            'required': False,
                            'default': 'asc',
                        },
                        'hide_empty': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                        'parent': {'type': 'integer', 'required': False},
                        'product': {'type': 'integer', 'required': False},
                        'slug': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Category name',
                                },
                                'slug': {
                                    'type': ['null', 'string'],
                                    'description': 'An alphanumeric identifier for the resource unique to its type',
                                },
                                'parent': {
                                    'type': ['null', 'integer'],
                                    'description': 'The ID for the parent of the resource',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'HTML description of the resource',
                                },
                                'display': {
                                    'type': ['null', 'string'],
                                    'description': 'Category archive display type',
                                },
                                'image': {
                                    'type': ['null', 'object'],
                                    'description': 'Image data',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                        },
                                        'date_created_gmt': {
                                            'type': ['null', 'string'],
                                        },
                                        'date_modified': {
                                            'type': ['null', 'string'],
                                        },
                                        'date_modified_gmt': {
                                            'type': ['null', 'string'],
                                        },
                                        'src': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'alt': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'menu_order': {
                                    'type': ['null', 'integer'],
                                    'description': 'Menu order, used to custom sort the resource',
                                },
                                'count': {
                                    'type': ['null', 'integer'],
                                    'description': 'Number of published products for the resource',
                                },
                            },
                            'x-airbyte-entity-name': 'product_categories',
                            'x-airbyte-stream-name': 'product_categories',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/products/categories/{id}',
                    action=Action.GET,
                    description='Retrieve a product category',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Category name',
                            },
                            'slug': {
                                'type': ['null', 'string'],
                                'description': 'An alphanumeric identifier for the resource unique to its type',
                            },
                            'parent': {
                                'type': ['null', 'integer'],
                                'description': 'The ID for the parent of the resource',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'HTML description of the resource',
                            },
                            'display': {
                                'type': ['null', 'string'],
                                'description': 'Category archive display type',
                            },
                            'image': {
                                'type': ['null', 'object'],
                                'description': 'Image data',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                    },
                                    'date_created': {
                                        'type': ['null', 'string'],
                                    },
                                    'date_created_gmt': {
                                        'type': ['null', 'string'],
                                    },
                                    'date_modified': {
                                        'type': ['null', 'string'],
                                    },
                                    'date_modified_gmt': {
                                        'type': ['null', 'string'],
                                    },
                                    'src': {
                                        'type': ['null', 'string'],
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                    },
                                    'alt': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'menu_order': {
                                'type': ['null', 'integer'],
                                'description': 'Menu order, used to custom sort the resource',
                            },
                            'count': {
                                'type': ['null', 'integer'],
                                'description': 'Number of published products for the resource',
                            },
                        },
                        'x-airbyte-entity-name': 'product_categories',
                        'x-airbyte-stream-name': 'product_categories',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Category name',
                    },
                    'slug': {
                        'type': ['null', 'string'],
                        'description': 'An alphanumeric identifier for the resource unique to its type',
                    },
                    'parent': {
                        'type': ['null', 'integer'],
                        'description': 'The ID for the parent of the resource',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'HTML description of the resource',
                    },
                    'display': {
                        'type': ['null', 'string'],
                        'description': 'Category archive display type',
                    },
                    'image': {
                        'type': ['null', 'object'],
                        'description': 'Image data',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                            },
                            'date_created_gmt': {
                                'type': ['null', 'string'],
                            },
                            'date_modified': {
                                'type': ['null', 'string'],
                            },
                            'date_modified_gmt': {
                                'type': ['null', 'string'],
                            },
                            'src': {
                                'type': ['null', 'string'],
                            },
                            'name': {
                                'type': ['null', 'string'],
                            },
                            'alt': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'menu_order': {
                        'type': ['null', 'integer'],
                        'description': 'Menu order, used to custom sort the resource',
                    },
                    'count': {
                        'type': ['null', 'integer'],
                        'description': 'Number of published products for the resource',
                    },
                },
                'x-airbyte-entity-name': 'product_categories',
                'x-airbyte-stream-name': 'product_categories',
            },
        ),
        EntityDefinition(
            name='product_tags',
            stream_name='product_tags',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/products/tags',
                    action=Action.LIST,
                    description='List product tags',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'orderby',
                        'order',
                        'hide_empty',
                        'product',
                        'slug',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'search': {'type': 'string', 'required': False},
                        'orderby': {
                            'type': 'string',
                            'required': False,
                            'default': 'name',
                        },
                        'order': {
                            'type': 'string',
                            'required': False,
                            'default': 'asc',
                        },
                        'hide_empty': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                        'product': {'type': 'integer', 'required': False},
                        'slug': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Tag name',
                                },
                                'slug': {
                                    'type': ['null', 'string'],
                                    'description': 'An alphanumeric identifier for the resource unique to its type',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'HTML description of the resource',
                                },
                                'count': {
                                    'type': ['null', 'integer'],
                                    'description': 'Number of published products for the resource',
                                },
                            },
                            'x-airbyte-entity-name': 'product_tags',
                            'x-airbyte-stream-name': 'product_tags',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/products/tags/{id}',
                    action=Action.GET,
                    description='Retrieve a product tag',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Tag name',
                            },
                            'slug': {
                                'type': ['null', 'string'],
                                'description': 'An alphanumeric identifier for the resource unique to its type',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'HTML description of the resource',
                            },
                            'count': {
                                'type': ['null', 'integer'],
                                'description': 'Number of published products for the resource',
                            },
                        },
                        'x-airbyte-entity-name': 'product_tags',
                        'x-airbyte-stream-name': 'product_tags',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Tag name',
                    },
                    'slug': {
                        'type': ['null', 'string'],
                        'description': 'An alphanumeric identifier for the resource unique to its type',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'HTML description of the resource',
                    },
                    'count': {
                        'type': ['null', 'integer'],
                        'description': 'Number of published products for the resource',
                    },
                },
                'x-airbyte-entity-name': 'product_tags',
                'x-airbyte-stream-name': 'product_tags',
            },
        ),
        EntityDefinition(
            name='product_reviews',
            stream_name='product_reviews',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/products/reviews',
                    action=Action.LIST,
                    description='List product reviews',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'after',
                        'before',
                        'product',
                        'status',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'search': {'type': 'string', 'required': False},
                        'after': {'type': 'string', 'required': False},
                        'before': {'type': 'string', 'required': False},
                        'product': {'type': 'array', 'required': False},
                        'status': {
                            'type': 'string',
                            'required': False,
                            'default': 'approved',
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'date_created': {
                                    'type': ['null', 'string'],
                                    'description': "The date the review was created, in the site's timezone",
                                },
                                'date_created_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the review was created, as GMT',
                                },
                                'product_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the product that the review belongs to',
                                },
                                'product_name': {
                                    'type': ['null', 'string'],
                                    'description': 'Product name',
                                },
                                'product_permalink': {
                                    'type': ['null', 'string'],
                                    'description': 'Product permalink',
                                },
                                'status': {
                                    'type': ['null', 'string'],
                                    'description': 'Status of the review (approved, hold, spam, unspam, trash, untrash)',
                                },
                                'reviewer': {
                                    'type': ['null', 'string'],
                                    'description': 'Reviewer name',
                                },
                                'reviewer_email': {
                                    'type': ['null', 'string'],
                                    'description': 'Reviewer email',
                                },
                                'review': {
                                    'type': ['null', 'string'],
                                    'description': 'The content of the review',
                                },
                                'rating': {
                                    'type': ['null', 'integer'],
                                    'description': 'Review rating (0 to 5)',
                                },
                                'verified': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows if the reviewer bought the product or not',
                                },
                                'reviewer_avatar_urls': {
                                    'type': ['null', 'object'],
                                    'description': 'Avatar URLs for the reviewer',
                                    'additionalProperties': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'x-airbyte-entity-name': 'product_reviews',
                            'x-airbyte-stream-name': 'product_reviews',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/products/reviews/{id}',
                    action=Action.GET,
                    description='Retrieve a product review',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'description': "The date the review was created, in the site's timezone",
                            },
                            'date_created_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the review was created, as GMT',
                            },
                            'product_id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the product that the review belongs to',
                            },
                            'product_name': {
                                'type': ['null', 'string'],
                                'description': 'Product name',
                            },
                            'product_permalink': {
                                'type': ['null', 'string'],
                                'description': 'Product permalink',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'Status of the review (approved, hold, spam, unspam, trash, untrash)',
                            },
                            'reviewer': {
                                'type': ['null', 'string'],
                                'description': 'Reviewer name',
                            },
                            'reviewer_email': {
                                'type': ['null', 'string'],
                                'description': 'Reviewer email',
                            },
                            'review': {
                                'type': ['null', 'string'],
                                'description': 'The content of the review',
                            },
                            'rating': {
                                'type': ['null', 'integer'],
                                'description': 'Review rating (0 to 5)',
                            },
                            'verified': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows if the reviewer bought the product or not',
                            },
                            'reviewer_avatar_urls': {
                                'type': ['null', 'object'],
                                'description': 'Avatar URLs for the reviewer',
                                'additionalProperties': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'product_reviews',
                        'x-airbyte-stream-name': 'product_reviews',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'description': "The date the review was created, in the site's timezone",
                    },
                    'date_created_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the review was created, as GMT',
                    },
                    'product_id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the product that the review belongs to',
                    },
                    'product_name': {
                        'type': ['null', 'string'],
                        'description': 'Product name',
                    },
                    'product_permalink': {
                        'type': ['null', 'string'],
                        'description': 'Product permalink',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Status of the review (approved, hold, spam, unspam, trash, untrash)',
                    },
                    'reviewer': {
                        'type': ['null', 'string'],
                        'description': 'Reviewer name',
                    },
                    'reviewer_email': {
                        'type': ['null', 'string'],
                        'description': 'Reviewer email',
                    },
                    'review': {
                        'type': ['null', 'string'],
                        'description': 'The content of the review',
                    },
                    'rating': {
                        'type': ['null', 'integer'],
                        'description': 'Review rating (0 to 5)',
                    },
                    'verified': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows if the reviewer bought the product or not',
                    },
                    'reviewer_avatar_urls': {
                        'type': ['null', 'object'],
                        'description': 'Avatar URLs for the reviewer',
                        'additionalProperties': {
                            'type': ['null', 'string'],
                        },
                    },
                },
                'x-airbyte-entity-name': 'product_reviews',
                'x-airbyte-stream-name': 'product_reviews',
            },
        ),
        EntityDefinition(
            name='product_attributes',
            stream_name='product_attributes',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/products/attributes',
                    action=Action.LIST,
                    description='List product attributes',
                    query_params=['page', 'per_page'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Attribute name',
                                },
                                'slug': {
                                    'type': ['null', 'string'],
                                    'description': 'An alphanumeric identifier for the resource unique to its type',
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                    'description': 'Type of attribute (select)',
                                },
                                'order_by': {
                                    'type': ['null', 'string'],
                                    'description': 'Default sort order (menu_order, name, name_num, id)',
                                },
                                'has_archives': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Enable/Disable attribute archives',
                                },
                            },
                            'x-airbyte-entity-name': 'product_attributes',
                            'x-airbyte-stream-name': 'product_attributes',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/products/attributes/{id}',
                    action=Action.GET,
                    description='Retrieve a product attribute',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Attribute name',
                            },
                            'slug': {
                                'type': ['null', 'string'],
                                'description': 'An alphanumeric identifier for the resource unique to its type',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'Type of attribute (select)',
                            },
                            'order_by': {
                                'type': ['null', 'string'],
                                'description': 'Default sort order (menu_order, name, name_num, id)',
                            },
                            'has_archives': {
                                'type': ['null', 'boolean'],
                                'description': 'Enable/Disable attribute archives',
                            },
                        },
                        'x-airbyte-entity-name': 'product_attributes',
                        'x-airbyte-stream-name': 'product_attributes',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Attribute name',
                    },
                    'slug': {
                        'type': ['null', 'string'],
                        'description': 'An alphanumeric identifier for the resource unique to its type',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Type of attribute (select)',
                    },
                    'order_by': {
                        'type': ['null', 'string'],
                        'description': 'Default sort order (menu_order, name, name_num, id)',
                    },
                    'has_archives': {
                        'type': ['null', 'boolean'],
                        'description': 'Enable/Disable attribute archives',
                    },
                },
                'x-airbyte-entity-name': 'product_attributes',
                'x-airbyte-stream-name': 'product_attributes',
            },
        ),
        EntityDefinition(
            name='product_variations',
            stream_name='product_variations',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/products/{product_id}/variations',
                    action=Action.LIST,
                    description='List product variations',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'sku',
                        'status',
                        'stock_status',
                        'on_sale',
                        'min_price',
                        'max_price',
                        'orderby',
                        'order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'search': {'type': 'string', 'required': False},
                        'sku': {'type': 'string', 'required': False},
                        'status': {
                            'type': 'string',
                            'required': False,
                            'default': 'any',
                        },
                        'stock_status': {'type': 'string', 'required': False},
                        'on_sale': {'type': 'boolean', 'required': False},
                        'min_price': {'type': 'string', 'required': False},
                        'max_price': {'type': 'string', 'required': False},
                        'orderby': {
                            'type': 'string',
                            'required': False,
                            'default': 'date',
                        },
                        'order': {
                            'type': 'string',
                            'required': False,
                            'default': 'desc',
                        },
                    },
                    path_params=['product_id'],
                    path_params_schema={
                        'product_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'date_created': {
                                    'type': ['null', 'string'],
                                    'description': "The date the variation was created, in the site's timezone",
                                },
                                'date_created_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the variation was created, as GMT',
                                },
                                'date_modified': {
                                    'type': ['null', 'string'],
                                    'description': "The date the variation was last modified, in the site's timezone",
                                },
                                'date_modified_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the variation was last modified, as GMT',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Variation description',
                                },
                                'permalink': {
                                    'type': ['null', 'string'],
                                    'description': 'Variation URL',
                                },
                                'sku': {
                                    'type': ['null', 'string'],
                                    'description': 'Unique identifier (SKU)',
                                },
                                'price': {
                                    'type': ['null', 'string'],
                                    'description': 'Current variation price',
                                },
                                'regular_price': {
                                    'type': ['null', 'string'],
                                    'description': 'Variation regular price',
                                },
                                'sale_price': {
                                    'type': ['null', 'string'],
                                    'description': 'Variation sale price',
                                },
                                'date_on_sale_from': {
                                    'type': ['null', 'string'],
                                    'description': 'Start date of sale price',
                                },
                                'date_on_sale_from_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'Start date of sale price, as GMT',
                                },
                                'date_on_sale_to': {
                                    'type': ['null', 'string'],
                                    'description': 'End date of sale price',
                                },
                                'date_on_sale_to_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'End date of sale price, as GMT',
                                },
                                'on_sale': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows if the variation is on sale',
                                },
                                'status': {
                                    'type': ['null', 'string'],
                                    'description': 'Variation status',
                                },
                                'purchasable': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows if the variation can be bought',
                                },
                                'virtual': {
                                    'type': ['null', 'boolean'],
                                    'description': 'If the variation is virtual',
                                },
                                'downloadable': {
                                    'type': ['null', 'boolean'],
                                    'description': 'If the variation is downloadable',
                                },
                                'downloads': {
                                    'type': ['null', 'array'],
                                    'description': 'List of downloadable files',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'string'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'file': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'download_limit': {
                                    'type': ['null', 'integer'],
                                    'description': 'Number of times downloadable files can be downloaded after purchase',
                                },
                                'download_expiry': {
                                    'type': ['null', 'integer'],
                                    'description': 'Number of days until access to downloadable files expires',
                                },
                                'tax_status': {
                                    'type': ['null', 'string'],
                                    'description': 'Tax status (taxable, shipping, none)',
                                },
                                'tax_class': {
                                    'type': ['null', 'string'],
                                    'description': 'Tax class',
                                },
                                'manage_stock': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Stock management at variation level',
                                },
                                'stock_quantity': {
                                    'type': ['null', 'integer'],
                                    'description': 'Stock quantity',
                                },
                                'stock_status': {
                                    'type': ['null', 'string'],
                                    'description': 'Controls the stock status of the variation',
                                },
                                'backorders': {
                                    'type': ['null', 'string'],
                                    'description': 'If managing stock, this controls if backorders are allowed',
                                },
                                'backorders_allowed': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows if backorders are allowed',
                                },
                                'backordered': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Shows if the variation is on backordered',
                                },
                                'weight': {
                                    'type': ['null', 'string'],
                                    'description': 'Variation weight',
                                },
                                'dimensions': {
                                    'type': ['null', 'object'],
                                    'description': 'Variation dimensions',
                                    'properties': {
                                        'length': {
                                            'type': ['null', 'string'],
                                        },
                                        'width': {
                                            'type': ['null', 'string'],
                                        },
                                        'height': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'shipping_class': {
                                    'type': ['null', 'string'],
                                    'description': 'Shipping class slug',
                                },
                                'shipping_class_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Shipping class ID',
                                },
                                'image': {
                                    'type': ['null', 'object'],
                                    'description': 'Variation image data',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                        },
                                        'date_created_gmt': {
                                            'type': ['null', 'string'],
                                        },
                                        'date_modified': {
                                            'type': ['null', 'string'],
                                        },
                                        'date_modified_gmt': {
                                            'type': ['null', 'string'],
                                        },
                                        'src': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'alt': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'attributes': {
                                    'type': ['null', 'array'],
                                    'description': 'List of attributes',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'option': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'menu_order': {
                                    'type': ['null', 'integer'],
                                    'description': 'Menu order, used to custom sort the resource',
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'description': 'Meta data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                    'description': 'Variation type',
                                },
                                'global_unique_id': {
                                    'type': ['null', 'string'],
                                    'description': 'GTIN, UPC, EAN or ISBN',
                                },
                                'low_stock_amount': {
                                    'type': ['null', 'integer'],
                                    'description': 'Low stock amount threshold',
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Variation name',
                                },
                                'parent_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Parent product ID',
                                },
                            },
                            'x-airbyte-entity-name': 'product_variations',
                            'x-airbyte-stream-name': 'product_variations',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/products/{product_id}/variations/{id}',
                    action=Action.GET,
                    description='Retrieve a product variation',
                    path_params=['product_id', 'id'],
                    path_params_schema={
                        'product_id': {'type': 'integer', 'required': True},
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'description': "The date the variation was created, in the site's timezone",
                            },
                            'date_created_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the variation was created, as GMT',
                            },
                            'date_modified': {
                                'type': ['null', 'string'],
                                'description': "The date the variation was last modified, in the site's timezone",
                            },
                            'date_modified_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the variation was last modified, as GMT',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Variation description',
                            },
                            'permalink': {
                                'type': ['null', 'string'],
                                'description': 'Variation URL',
                            },
                            'sku': {
                                'type': ['null', 'string'],
                                'description': 'Unique identifier (SKU)',
                            },
                            'price': {
                                'type': ['null', 'string'],
                                'description': 'Current variation price',
                            },
                            'regular_price': {
                                'type': ['null', 'string'],
                                'description': 'Variation regular price',
                            },
                            'sale_price': {
                                'type': ['null', 'string'],
                                'description': 'Variation sale price',
                            },
                            'date_on_sale_from': {
                                'type': ['null', 'string'],
                                'description': 'Start date of sale price',
                            },
                            'date_on_sale_from_gmt': {
                                'type': ['null', 'string'],
                                'description': 'Start date of sale price, as GMT',
                            },
                            'date_on_sale_to': {
                                'type': ['null', 'string'],
                                'description': 'End date of sale price',
                            },
                            'date_on_sale_to_gmt': {
                                'type': ['null', 'string'],
                                'description': 'End date of sale price, as GMT',
                            },
                            'on_sale': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows if the variation is on sale',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'Variation status',
                            },
                            'purchasable': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows if the variation can be bought',
                            },
                            'virtual': {
                                'type': ['null', 'boolean'],
                                'description': 'If the variation is virtual',
                            },
                            'downloadable': {
                                'type': ['null', 'boolean'],
                                'description': 'If the variation is downloadable',
                            },
                            'downloads': {
                                'type': ['null', 'array'],
                                'description': 'List of downloadable files',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'file': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'download_limit': {
                                'type': ['null', 'integer'],
                                'description': 'Number of times downloadable files can be downloaded after purchase',
                            },
                            'download_expiry': {
                                'type': ['null', 'integer'],
                                'description': 'Number of days until access to downloadable files expires',
                            },
                            'tax_status': {
                                'type': ['null', 'string'],
                                'description': 'Tax status (taxable, shipping, none)',
                            },
                            'tax_class': {
                                'type': ['null', 'string'],
                                'description': 'Tax class',
                            },
                            'manage_stock': {
                                'type': ['null', 'boolean'],
                                'description': 'Stock management at variation level',
                            },
                            'stock_quantity': {
                                'type': ['null', 'integer'],
                                'description': 'Stock quantity',
                            },
                            'stock_status': {
                                'type': ['null', 'string'],
                                'description': 'Controls the stock status of the variation',
                            },
                            'backorders': {
                                'type': ['null', 'string'],
                                'description': 'If managing stock, this controls if backorders are allowed',
                            },
                            'backorders_allowed': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows if backorders are allowed',
                            },
                            'backordered': {
                                'type': ['null', 'boolean'],
                                'description': 'Shows if the variation is on backordered',
                            },
                            'weight': {
                                'type': ['null', 'string'],
                                'description': 'Variation weight',
                            },
                            'dimensions': {
                                'type': ['null', 'object'],
                                'description': 'Variation dimensions',
                                'properties': {
                                    'length': {
                                        'type': ['null', 'string'],
                                    },
                                    'width': {
                                        'type': ['null', 'string'],
                                    },
                                    'height': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'shipping_class': {
                                'type': ['null', 'string'],
                                'description': 'Shipping class slug',
                            },
                            'shipping_class_id': {
                                'type': ['null', 'integer'],
                                'description': 'Shipping class ID',
                            },
                            'image': {
                                'type': ['null', 'object'],
                                'description': 'Variation image data',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                    },
                                    'date_created': {
                                        'type': ['null', 'string'],
                                    },
                                    'date_created_gmt': {
                                        'type': ['null', 'string'],
                                    },
                                    'date_modified': {
                                        'type': ['null', 'string'],
                                    },
                                    'date_modified_gmt': {
                                        'type': ['null', 'string'],
                                    },
                                    'src': {
                                        'type': ['null', 'string'],
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                    },
                                    'alt': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'attributes': {
                                'type': ['null', 'array'],
                                'description': 'List of attributes',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'option': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'menu_order': {
                                'type': ['null', 'integer'],
                                'description': 'Menu order, used to custom sort the resource',
                            },
                            'meta_data': {
                                'type': ['null', 'array'],
                                'description': 'Meta data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'key': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'Variation type',
                            },
                            'global_unique_id': {
                                'type': ['null', 'string'],
                                'description': 'GTIN, UPC, EAN or ISBN',
                            },
                            'low_stock_amount': {
                                'type': ['null', 'integer'],
                                'description': 'Low stock amount threshold',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Variation name',
                            },
                            'parent_id': {
                                'type': ['null', 'integer'],
                                'description': 'Parent product ID',
                            },
                        },
                        'x-airbyte-entity-name': 'product_variations',
                        'x-airbyte-stream-name': 'product_variations',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'description': "The date the variation was created, in the site's timezone",
                    },
                    'date_created_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the variation was created, as GMT',
                    },
                    'date_modified': {
                        'type': ['null', 'string'],
                        'description': "The date the variation was last modified, in the site's timezone",
                    },
                    'date_modified_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the variation was last modified, as GMT',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Variation description',
                    },
                    'permalink': {
                        'type': ['null', 'string'],
                        'description': 'Variation URL',
                    },
                    'sku': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier (SKU)',
                    },
                    'price': {
                        'type': ['null', 'string'],
                        'description': 'Current variation price',
                    },
                    'regular_price': {
                        'type': ['null', 'string'],
                        'description': 'Variation regular price',
                    },
                    'sale_price': {
                        'type': ['null', 'string'],
                        'description': 'Variation sale price',
                    },
                    'date_on_sale_from': {
                        'type': ['null', 'string'],
                        'description': 'Start date of sale price',
                    },
                    'date_on_sale_from_gmt': {
                        'type': ['null', 'string'],
                        'description': 'Start date of sale price, as GMT',
                    },
                    'date_on_sale_to': {
                        'type': ['null', 'string'],
                        'description': 'End date of sale price',
                    },
                    'date_on_sale_to_gmt': {
                        'type': ['null', 'string'],
                        'description': 'End date of sale price, as GMT',
                    },
                    'on_sale': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows if the variation is on sale',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Variation status',
                    },
                    'purchasable': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows if the variation can be bought',
                    },
                    'virtual': {
                        'type': ['null', 'boolean'],
                        'description': 'If the variation is virtual',
                    },
                    'downloadable': {
                        'type': ['null', 'boolean'],
                        'description': 'If the variation is downloadable',
                    },
                    'downloads': {
                        'type': ['null', 'array'],
                        'description': 'List of downloadable files',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'file': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'download_limit': {
                        'type': ['null', 'integer'],
                        'description': 'Number of times downloadable files can be downloaded after purchase',
                    },
                    'download_expiry': {
                        'type': ['null', 'integer'],
                        'description': 'Number of days until access to downloadable files expires',
                    },
                    'tax_status': {
                        'type': ['null', 'string'],
                        'description': 'Tax status (taxable, shipping, none)',
                    },
                    'tax_class': {
                        'type': ['null', 'string'],
                        'description': 'Tax class',
                    },
                    'manage_stock': {
                        'type': ['null', 'boolean'],
                        'description': 'Stock management at variation level',
                    },
                    'stock_quantity': {
                        'type': ['null', 'integer'],
                        'description': 'Stock quantity',
                    },
                    'stock_status': {
                        'type': ['null', 'string'],
                        'description': 'Controls the stock status of the variation',
                    },
                    'backorders': {
                        'type': ['null', 'string'],
                        'description': 'If managing stock, this controls if backorders are allowed',
                    },
                    'backorders_allowed': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows if backorders are allowed',
                    },
                    'backordered': {
                        'type': ['null', 'boolean'],
                        'description': 'Shows if the variation is on backordered',
                    },
                    'weight': {
                        'type': ['null', 'string'],
                        'description': 'Variation weight',
                    },
                    'dimensions': {
                        'type': ['null', 'object'],
                        'description': 'Variation dimensions',
                        'properties': {
                            'length': {
                                'type': ['null', 'string'],
                            },
                            'width': {
                                'type': ['null', 'string'],
                            },
                            'height': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'shipping_class': {
                        'type': ['null', 'string'],
                        'description': 'Shipping class slug',
                    },
                    'shipping_class_id': {
                        'type': ['null', 'integer'],
                        'description': 'Shipping class ID',
                    },
                    'image': {
                        'type': ['null', 'object'],
                        'description': 'Variation image data',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                            },
                            'date_created_gmt': {
                                'type': ['null', 'string'],
                            },
                            'date_modified': {
                                'type': ['null', 'string'],
                            },
                            'date_modified_gmt': {
                                'type': ['null', 'string'],
                            },
                            'src': {
                                'type': ['null', 'string'],
                            },
                            'name': {
                                'type': ['null', 'string'],
                            },
                            'alt': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'attributes': {
                        'type': ['null', 'array'],
                        'description': 'List of attributes',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'option': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'menu_order': {
                        'type': ['null', 'integer'],
                        'description': 'Menu order, used to custom sort the resource',
                    },
                    'meta_data': {
                        'type': ['null', 'array'],
                        'description': 'Meta data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'key': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Variation type',
                    },
                    'global_unique_id': {
                        'type': ['null', 'string'],
                        'description': 'GTIN, UPC, EAN or ISBN',
                    },
                    'low_stock_amount': {
                        'type': ['null', 'integer'],
                        'description': 'Low stock amount threshold',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Variation name',
                    },
                    'parent_id': {
                        'type': ['null', 'integer'],
                        'description': 'Parent product ID',
                    },
                },
                'x-airbyte-entity-name': 'product_variations',
                'x-airbyte-stream-name': 'product_variations',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='product_variations',
                    target_entity='products',
                    foreign_key='product_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='order_notes',
            stream_name='order_notes',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/notes',
                    action=Action.LIST,
                    description='List order notes',
                    query_params=['type'],
                    query_params_schema={
                        'type': {
                            'type': 'string',
                            'required': False,
                            'default': 'any',
                        },
                    },
                    path_params=['order_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'author': {
                                    'type': ['null', 'string'],
                                    'description': 'Order note author',
                                },
                                'date_created': {
                                    'type': ['null', 'string'],
                                    'description': "The date the order note was created, in the site's timezone",
                                },
                                'date_created_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the order note was created, as GMT',
                                },
                                'note': {
                                    'type': ['null', 'string'],
                                    'description': 'Order note content',
                                },
                                'customer_note': {
                                    'type': ['null', 'boolean'],
                                    'description': 'If true, the note will be shown to customers',
                                },
                            },
                            'x-airbyte-entity-name': 'order_notes',
                            'x-airbyte-stream-name': 'order_notes',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/notes/{id}',
                    action=Action.GET,
                    description='Retrieve an order note',
                    path_params=['order_id', 'id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'author': {
                                'type': ['null', 'string'],
                                'description': 'Order note author',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'description': "The date the order note was created, in the site's timezone",
                            },
                            'date_created_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the order note was created, as GMT',
                            },
                            'note': {
                                'type': ['null', 'string'],
                                'description': 'Order note content',
                            },
                            'customer_note': {
                                'type': ['null', 'boolean'],
                                'description': 'If true, the note will be shown to customers',
                            },
                        },
                        'x-airbyte-entity-name': 'order_notes',
                        'x-airbyte-stream-name': 'order_notes',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'author': {
                        'type': ['null', 'string'],
                        'description': 'Order note author',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'description': "The date the order note was created, in the site's timezone",
                    },
                    'date_created_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the order note was created, as GMT',
                    },
                    'note': {
                        'type': ['null', 'string'],
                        'description': 'Order note content',
                    },
                    'customer_note': {
                        'type': ['null', 'boolean'],
                        'description': 'If true, the note will be shown to customers',
                    },
                },
                'x-airbyte-entity-name': 'order_notes',
                'x-airbyte-stream-name': 'order_notes',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='order_notes',
                    target_entity='orders',
                    foreign_key='order_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='refunds',
            stream_name='refunds',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/refunds',
                    action=Action.LIST,
                    description='List order refunds',
                    query_params=['page', 'per_page'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                    },
                    path_params=['order_id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'date_created': {
                                    'type': ['null', 'string'],
                                    'description': "The date the refund was created, in the site's timezone",
                                },
                                'date_created_gmt': {
                                    'type': ['null', 'string'],
                                    'description': 'The date the refund was created, as GMT',
                                },
                                'amount': {
                                    'type': ['null', 'string'],
                                    'description': 'Refund amount',
                                },
                                'reason': {
                                    'type': ['null', 'string'],
                                    'description': 'Reason for refund',
                                },
                                'refunded_by': {
                                    'type': ['null', 'integer'],
                                    'description': 'User ID of user who created the refund',
                                },
                                'refunded_payment': {
                                    'type': ['null', 'boolean'],
                                    'description': 'If the payment was refunded via the API',
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'description': 'Meta data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'line_items': {
                                    'type': ['null', 'array'],
                                    'description': 'Line items data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'product_id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'variation_id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'quantity': {
                                                'type': ['null', 'integer'],
                                            },
                                            'tax_class': {
                                                'type': ['null', 'string'],
                                            },
                                            'subtotal': {
                                                'type': ['null', 'string'],
                                            },
                                            'subtotal_tax': {
                                                'type': ['null', 'string'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                            'total_tax': {
                                                'type': ['null', 'string'],
                                            },
                                            'taxes': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'total': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'subtotal': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                            'meta_data': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'key': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                            'sku': {
                                                'type': ['null', 'string'],
                                            },
                                            'price': {
                                                'type': ['null', 'number'],
                                            },
                                        },
                                    },
                                },
                                'shipping_lines': {
                                    'type': ['null', 'array'],
                                    'description': 'Shipping lines data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'method_title': {
                                                'type': ['null', 'string'],
                                            },
                                            'method_id': {
                                                'type': ['null', 'string'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                            'total_tax': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'tax_lines': {
                                    'type': ['null', 'array'],
                                    'description': 'Tax lines data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'rate_code': {
                                                'type': ['null', 'string'],
                                            },
                                            'rate_id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'label': {
                                                'type': ['null', 'string'],
                                            },
                                            'compound': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'tax_total': {
                                                'type': ['null', 'string'],
                                            },
                                            'shipping_tax_total': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'fee_lines': {
                                    'type': ['null', 'array'],
                                    'description': 'Fee lines data',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'tax_class': {
                                                'type': ['null', 'string'],
                                            },
                                            'tax_status': {
                                                'type': ['null', 'string'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                            'total_tax': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                            'x-airbyte-entity-name': 'refunds',
                            'x-airbyte-stream-name': 'refunds',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/orders/{order_id}/refunds/{id}',
                    action=Action.GET,
                    description='Retrieve a refund',
                    path_params=['order_id', 'id'],
                    path_params_schema={
                        'order_id': {'type': 'integer', 'required': True},
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'description': "The date the refund was created, in the site's timezone",
                            },
                            'date_created_gmt': {
                                'type': ['null', 'string'],
                                'description': 'The date the refund was created, as GMT',
                            },
                            'amount': {
                                'type': ['null', 'string'],
                                'description': 'Refund amount',
                            },
                            'reason': {
                                'type': ['null', 'string'],
                                'description': 'Reason for refund',
                            },
                            'refunded_by': {
                                'type': ['null', 'integer'],
                                'description': 'User ID of user who created the refund',
                            },
                            'refunded_payment': {
                                'type': ['null', 'boolean'],
                                'description': 'If the payment was refunded via the API',
                            },
                            'meta_data': {
                                'type': ['null', 'array'],
                                'description': 'Meta data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'key': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'line_items': {
                                'type': ['null', 'array'],
                                'description': 'Line items data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'product_id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'variation_id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'quantity': {
                                            'type': ['null', 'integer'],
                                        },
                                        'tax_class': {
                                            'type': ['null', 'string'],
                                        },
                                        'subtotal': {
                                            'type': ['null', 'string'],
                                        },
                                        'subtotal_tax': {
                                            'type': ['null', 'string'],
                                        },
                                        'total': {
                                            'type': ['null', 'string'],
                                        },
                                        'total_tax': {
                                            'type': ['null', 'string'],
                                        },
                                        'taxes': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'total': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'subtotal': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                        'meta_data': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'key': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                        'sku': {
                                            'type': ['null', 'string'],
                                        },
                                        'price': {
                                            'type': ['null', 'number'],
                                        },
                                    },
                                },
                            },
                            'shipping_lines': {
                                'type': ['null', 'array'],
                                'description': 'Shipping lines data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'method_title': {
                                            'type': ['null', 'string'],
                                        },
                                        'method_id': {
                                            'type': ['null', 'string'],
                                        },
                                        'total': {
                                            'type': ['null', 'string'],
                                        },
                                        'total_tax': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'tax_lines': {
                                'type': ['null', 'array'],
                                'description': 'Tax lines data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'rate_code': {
                                            'type': ['null', 'string'],
                                        },
                                        'rate_id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'label': {
                                            'type': ['null', 'string'],
                                        },
                                        'compound': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'tax_total': {
                                            'type': ['null', 'string'],
                                        },
                                        'shipping_tax_total': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                            'fee_lines': {
                                'type': ['null', 'array'],
                                'description': 'Fee lines data',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'tax_class': {
                                            'type': ['null', 'string'],
                                        },
                                        'tax_status': {
                                            'type': ['null', 'string'],
                                        },
                                        'total': {
                                            'type': ['null', 'string'],
                                        },
                                        'total_tax': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'refunds',
                        'x-airbyte-stream-name': 'refunds',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'description': "The date the refund was created, in the site's timezone",
                    },
                    'date_created_gmt': {
                        'type': ['null', 'string'],
                        'description': 'The date the refund was created, as GMT',
                    },
                    'amount': {
                        'type': ['null', 'string'],
                        'description': 'Refund amount',
                    },
                    'reason': {
                        'type': ['null', 'string'],
                        'description': 'Reason for refund',
                    },
                    'refunded_by': {
                        'type': ['null', 'integer'],
                        'description': 'User ID of user who created the refund',
                    },
                    'refunded_payment': {
                        'type': ['null', 'boolean'],
                        'description': 'If the payment was refunded via the API',
                    },
                    'meta_data': {
                        'type': ['null', 'array'],
                        'description': 'Meta data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'key': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'line_items': {
                        'type': ['null', 'array'],
                        'description': 'Line items data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'product_id': {
                                    'type': ['null', 'integer'],
                                },
                                'variation_id': {
                                    'type': ['null', 'integer'],
                                },
                                'quantity': {
                                    'type': ['null', 'integer'],
                                },
                                'tax_class': {
                                    'type': ['null', 'string'],
                                },
                                'subtotal': {
                                    'type': ['null', 'string'],
                                },
                                'subtotal_tax': {
                                    'type': ['null', 'string'],
                                },
                                'total': {
                                    'type': ['null', 'string'],
                                },
                                'total_tax': {
                                    'type': ['null', 'string'],
                                },
                                'taxes': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'total': {
                                                'type': ['null', 'string'],
                                            },
                                            'subtotal': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'meta_data': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'key': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'sku': {
                                    'type': ['null', 'string'],
                                },
                                'price': {
                                    'type': ['null', 'number'],
                                },
                            },
                        },
                    },
                    'shipping_lines': {
                        'type': ['null', 'array'],
                        'description': 'Shipping lines data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'method_title': {
                                    'type': ['null', 'string'],
                                },
                                'method_id': {
                                    'type': ['null', 'string'],
                                },
                                'total': {
                                    'type': ['null', 'string'],
                                },
                                'total_tax': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'tax_lines': {
                        'type': ['null', 'array'],
                        'description': 'Tax lines data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'rate_code': {
                                    'type': ['null', 'string'],
                                },
                                'rate_id': {
                                    'type': ['null', 'integer'],
                                },
                                'label': {
                                    'type': ['null', 'string'],
                                },
                                'compound': {
                                    'type': ['null', 'boolean'],
                                },
                                'tax_total': {
                                    'type': ['null', 'string'],
                                },
                                'shipping_tax_total': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'fee_lines': {
                        'type': ['null', 'array'],
                        'description': 'Fee lines data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'tax_class': {
                                    'type': ['null', 'string'],
                                },
                                'tax_status': {
                                    'type': ['null', 'string'],
                                },
                                'total': {
                                    'type': ['null', 'string'],
                                },
                                'total_tax': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'refunds',
                'x-airbyte-stream-name': 'refunds',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='refunds',
                    target_entity='orders',
                    foreign_key='order_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='payment_gateways',
            stream_name='payment_gateways',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/payment_gateways',
                    action=Action.LIST,
                    description='List payment gateways',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                    'description': 'Payment gateway ID',
                                },
                                'title': {
                                    'type': ['null', 'string'],
                                    'description': 'Payment gateway title on checkout',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Payment gateway description on checkout',
                                },
                                'order': {
                                    'type': ['null', 'integer'],
                                    'description': 'Payment gateway sort order',
                                },
                                'enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Payment gateway enabled status',
                                },
                                'method_title': {
                                    'type': ['null', 'string'],
                                    'description': 'Payment gateway method title',
                                },
                                'method_description': {
                                    'type': ['null', 'string'],
                                    'description': 'Payment gateway method description',
                                },
                                'method_supports': {
                                    'type': ['null', 'array'],
                                    'description': 'Supported features for this payment gateway',
                                    'items': {
                                        'type': ['null', 'string'],
                                    },
                                },
                                'settings': {
                                    'type': ['null', 'object'],
                                    'description': 'Payment gateway settings',
                                    'additionalProperties': True,
                                },
                                'needs_setup': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the payment gateway needs setup',
                                },
                                'post_install_scripts': {
                                    'type': ['null', 'array'],
                                    'description': 'Post install scripts',
                                    'items': {
                                        'type': ['null', 'string'],
                                    },
                                },
                                'settings_url': {
                                    'type': ['null', 'string'],
                                    'description': 'URL to the gateway settings page',
                                },
                                'connection_url': {
                                    'type': ['null', 'string'],
                                    'description': 'URL for the gateway connection',
                                },
                                'setup_help_text': {
                                    'type': ['null', 'string'],
                                    'description': 'Help text for setting up the gateway',
                                },
                                'required_settings_keys': {
                                    'type': ['null', 'array'],
                                    'description': 'Required settings keys',
                                    'items': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'x-airbyte-entity-name': 'payment_gateways',
                            'x-airbyte-stream-name': 'payment_gateways',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/payment_gateways/{id}',
                    action=Action.GET,
                    description='Retrieve a payment gateway',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                                'description': 'Payment gateway ID',
                            },
                            'title': {
                                'type': ['null', 'string'],
                                'description': 'Payment gateway title on checkout',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Payment gateway description on checkout',
                            },
                            'order': {
                                'type': ['null', 'integer'],
                                'description': 'Payment gateway sort order',
                            },
                            'enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Payment gateway enabled status',
                            },
                            'method_title': {
                                'type': ['null', 'string'],
                                'description': 'Payment gateway method title',
                            },
                            'method_description': {
                                'type': ['null', 'string'],
                                'description': 'Payment gateway method description',
                            },
                            'method_supports': {
                                'type': ['null', 'array'],
                                'description': 'Supported features for this payment gateway',
                                'items': {
                                    'type': ['null', 'string'],
                                },
                            },
                            'settings': {
                                'type': ['null', 'object'],
                                'description': 'Payment gateway settings',
                                'additionalProperties': True,
                            },
                            'needs_setup': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the payment gateway needs setup',
                            },
                            'post_install_scripts': {
                                'type': ['null', 'array'],
                                'description': 'Post install scripts',
                                'items': {
                                    'type': ['null', 'string'],
                                },
                            },
                            'settings_url': {
                                'type': ['null', 'string'],
                                'description': 'URL to the gateway settings page',
                            },
                            'connection_url': {
                                'type': ['null', 'string'],
                                'description': 'URL for the gateway connection',
                            },
                            'setup_help_text': {
                                'type': ['null', 'string'],
                                'description': 'Help text for setting up the gateway',
                            },
                            'required_settings_keys': {
                                'type': ['null', 'array'],
                                'description': 'Required settings keys',
                                'items': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'payment_gateways',
                        'x-airbyte-stream-name': 'payment_gateways',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Payment gateway ID',
                    },
                    'title': {
                        'type': ['null', 'string'],
                        'description': 'Payment gateway title on checkout',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Payment gateway description on checkout',
                    },
                    'order': {
                        'type': ['null', 'integer'],
                        'description': 'Payment gateway sort order',
                    },
                    'enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Payment gateway enabled status',
                    },
                    'method_title': {
                        'type': ['null', 'string'],
                        'description': 'Payment gateway method title',
                    },
                    'method_description': {
                        'type': ['null', 'string'],
                        'description': 'Payment gateway method description',
                    },
                    'method_supports': {
                        'type': ['null', 'array'],
                        'description': 'Supported features for this payment gateway',
                        'items': {
                            'type': ['null', 'string'],
                        },
                    },
                    'settings': {
                        'type': ['null', 'object'],
                        'description': 'Payment gateway settings',
                        'additionalProperties': True,
                    },
                    'needs_setup': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the payment gateway needs setup',
                    },
                    'post_install_scripts': {
                        'type': ['null', 'array'],
                        'description': 'Post install scripts',
                        'items': {
                            'type': ['null', 'string'],
                        },
                    },
                    'settings_url': {
                        'type': ['null', 'string'],
                        'description': 'URL to the gateway settings page',
                    },
                    'connection_url': {
                        'type': ['null', 'string'],
                        'description': 'URL for the gateway connection',
                    },
                    'setup_help_text': {
                        'type': ['null', 'string'],
                        'description': 'Help text for setting up the gateway',
                    },
                    'required_settings_keys': {
                        'type': ['null', 'array'],
                        'description': 'Required settings keys',
                        'items': {
                            'type': ['null', 'string'],
                        },
                    },
                },
                'x-airbyte-entity-name': 'payment_gateways',
                'x-airbyte-stream-name': 'payment_gateways',
            },
        ),
        EntityDefinition(
            name='shipping_methods',
            stream_name='shipping_methods',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/shipping_methods',
                    action=Action.LIST,
                    description='List shipping methods',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                    'description': 'Method ID',
                                },
                                'title': {
                                    'type': ['null', 'string'],
                                    'description': 'Shipping method title',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Shipping method description',
                                },
                            },
                            'x-airbyte-entity-name': 'shipping_methods',
                            'x-airbyte-stream-name': 'shipping_methods',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/shipping_methods/{id}',
                    action=Action.GET,
                    description='Retrieve a shipping method',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                                'description': 'Method ID',
                            },
                            'title': {
                                'type': ['null', 'string'],
                                'description': 'Shipping method title',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Shipping method description',
                            },
                        },
                        'x-airbyte-entity-name': 'shipping_methods',
                        'x-airbyte-stream-name': 'shipping_methods',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Method ID',
                    },
                    'title': {
                        'type': ['null', 'string'],
                        'description': 'Shipping method title',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Shipping method description',
                    },
                },
                'x-airbyte-entity-name': 'shipping_methods',
                'x-airbyte-stream-name': 'shipping_methods',
            },
        ),
        EntityDefinition(
            name='shipping_zones',
            stream_name='shipping_zones',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/shipping/zones',
                    action=Action.LIST,
                    description='List shipping zones',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Shipping zone name',
                                },
                                'order': {
                                    'type': ['null', 'integer'],
                                    'description': 'Shipping zone order',
                                },
                            },
                            'x-airbyte-entity-name': 'shipping_zones',
                            'x-airbyte-stream-name': 'shipping_zones',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/shipping/zones/{id}',
                    action=Action.GET,
                    description='Retrieve a shipping zone',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Shipping zone name',
                            },
                            'order': {
                                'type': ['null', 'integer'],
                                'description': 'Shipping zone order',
                            },
                        },
                        'x-airbyte-entity-name': 'shipping_zones',
                        'x-airbyte-stream-name': 'shipping_zones',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Shipping zone name',
                    },
                    'order': {
                        'type': ['null', 'integer'],
                        'description': 'Shipping zone order',
                    },
                },
                'x-airbyte-entity-name': 'shipping_zones',
                'x-airbyte-stream-name': 'shipping_zones',
            },
        ),
        EntityDefinition(
            name='tax_rates',
            stream_name='tax_rates',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/taxes',
                    action=Action.LIST,
                    description='List tax rates',
                    query_params=[
                        'page',
                        'per_page',
                        'class',
                        'orderby',
                        'order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'class': {'type': 'string', 'required': False},
                        'orderby': {
                            'type': 'string',
                            'required': False,
                            'default': 'order',
                        },
                        'order': {
                            'type': 'string',
                            'required': False,
                            'default': 'asc',
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'country': {
                                    'type': ['null', 'string'],
                                    'description': 'Country ISO 3166 code',
                                },
                                'state': {
                                    'type': ['null', 'string'],
                                    'description': 'State code',
                                },
                                'postcode': {
                                    'type': ['null', 'string'],
                                    'description': 'Postcode/ZIP',
                                },
                                'city': {
                                    'type': ['null', 'string'],
                                    'description': 'City name',
                                },
                                'postcodes': {
                                    'type': ['null', 'array'],
                                    'description': 'Postcodes/ZIPs',
                                    'items': {
                                        'type': ['null', 'string'],
                                    },
                                },
                                'cities': {
                                    'type': ['null', 'array'],
                                    'description': 'City names',
                                    'items': {
                                        'type': ['null', 'string'],
                                    },
                                },
                                'rate': {
                                    'type': ['null', 'string'],
                                    'description': 'Tax rate',
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Tax rate name',
                                },
                                'priority': {
                                    'type': ['null', 'integer'],
                                    'description': 'Tax priority',
                                },
                                'compound': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether or not this is a compound rate',
                                },
                                'shipping': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether or not this tax rate also gets applied to shipping',
                                },
                                'order': {
                                    'type': ['null', 'integer'],
                                    'description': 'Indicates the order that will appear in queries',
                                },
                                'class': {
                                    'type': ['null', 'string'],
                                    'description': 'Tax class',
                                },
                            },
                            'x-airbyte-entity-name': 'tax_rates',
                            'x-airbyte-stream-name': 'tax_rates',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/taxes/{id}',
                    action=Action.GET,
                    description='Retrieve a tax rate',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique identifier for the resource',
                            },
                            'country': {
                                'type': ['null', 'string'],
                                'description': 'Country ISO 3166 code',
                            },
                            'state': {
                                'type': ['null', 'string'],
                                'description': 'State code',
                            },
                            'postcode': {
                                'type': ['null', 'string'],
                                'description': 'Postcode/ZIP',
                            },
                            'city': {
                                'type': ['null', 'string'],
                                'description': 'City name',
                            },
                            'postcodes': {
                                'type': ['null', 'array'],
                                'description': 'Postcodes/ZIPs',
                                'items': {
                                    'type': ['null', 'string'],
                                },
                            },
                            'cities': {
                                'type': ['null', 'array'],
                                'description': 'City names',
                                'items': {
                                    'type': ['null', 'string'],
                                },
                            },
                            'rate': {
                                'type': ['null', 'string'],
                                'description': 'Tax rate',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Tax rate name',
                            },
                            'priority': {
                                'type': ['null', 'integer'],
                                'description': 'Tax priority',
                            },
                            'compound': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether or not this is a compound rate',
                            },
                            'shipping': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether or not this tax rate also gets applied to shipping',
                            },
                            'order': {
                                'type': ['null', 'integer'],
                                'description': 'Indicates the order that will appear in queries',
                            },
                            'class': {
                                'type': ['null', 'string'],
                                'description': 'Tax class',
                            },
                        },
                        'x-airbyte-entity-name': 'tax_rates',
                        'x-airbyte-stream-name': 'tax_rates',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique identifier for the resource',
                    },
                    'country': {
                        'type': ['null', 'string'],
                        'description': 'Country ISO 3166 code',
                    },
                    'state': {
                        'type': ['null', 'string'],
                        'description': 'State code',
                    },
                    'postcode': {
                        'type': ['null', 'string'],
                        'description': 'Postcode/ZIP',
                    },
                    'city': {
                        'type': ['null', 'string'],
                        'description': 'City name',
                    },
                    'postcodes': {
                        'type': ['null', 'array'],
                        'description': 'Postcodes/ZIPs',
                        'items': {
                            'type': ['null', 'string'],
                        },
                    },
                    'cities': {
                        'type': ['null', 'array'],
                        'description': 'City names',
                        'items': {
                            'type': ['null', 'string'],
                        },
                    },
                    'rate': {
                        'type': ['null', 'string'],
                        'description': 'Tax rate',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Tax rate name',
                    },
                    'priority': {
                        'type': ['null', 'integer'],
                        'description': 'Tax priority',
                    },
                    'compound': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether or not this is a compound rate',
                    },
                    'shipping': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether or not this tax rate also gets applied to shipping',
                    },
                    'order': {
                        'type': ['null', 'integer'],
                        'description': 'Indicates the order that will appear in queries',
                    },
                    'class': {
                        'type': ['null', 'string'],
                        'description': 'Tax class',
                    },
                },
                'x-airbyte-entity-name': 'tax_rates',
                'x-airbyte-stream-name': 'tax_rates',
            },
        ),
        EntityDefinition(
            name='tax_classes',
            stream_name='tax_classes',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/taxes/classes',
                    action=Action.LIST,
                    description='List tax classes',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'slug': {
                                    'type': ['null', 'string'],
                                    'description': 'Unique identifier for the resource',
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Tax class name',
                                },
                            },
                            'x-airbyte-entity-name': 'tax_classes',
                            'x-airbyte-stream-name': 'tax_classes',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'slug': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier for the resource',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Tax class name',
                    },
                },
                'x-airbyte-entity-name': 'tax_classes',
                'x-airbyte-stream-name': 'tax_classes',
            },
        ),
    ],
    search_field_paths={
        'customers': [
            'avatar_url',
            'billing',
            'billing.address_1',
            'billing.address_2',
            'billing.city',
            'billing.company',
            'billing.country',
            'billing.email',
            'billing.first_name',
            'billing.last_name',
            'billing.phone',
            'billing.postcode',
            'billing.state',
            'date_created',
            'date_created_gmt',
            'date_modified',
            'date_modified_gmt',
            'email',
            'first_name',
            'id',
            'is_paying_customer',
            'last_name',
            'meta_data',
            'meta_data[]',
            'role',
            'shipping',
            'shipping.address_1',
            'shipping.address_2',
            'shipping.city',
            'shipping.company',
            'shipping.country',
            'shipping.first_name',
            'shipping.last_name',
            'shipping.postcode',
            'shipping.state',
            'username',
        ],
        'orders': [
            'billing',
            'cart_hash',
            'cart_tax',
            'coupon_lines',
            'coupon_lines[]',
            'created_via',
            'currency',
            'customer_id',
            'customer_ip_address',
            'customer_note',
            'customer_user_agent',
            'date_completed',
            'date_completed_gmt',
            'date_created',
            'date_created_gmt',
            'date_modified',
            'date_modified_gmt',
            'date_paid',
            'date_paid_gmt',
            'discount_tax',
            'discount_total',
            'fee_lines',
            'fee_lines[]',
            'id',
            'line_items',
            'line_items[]',
            'meta_data',
            'meta_data[]',
            'number',
            'order_key',
            'parent_id',
            'payment_method',
            'payment_method_title',
            'prices_include_tax',
            'refunds',
            'refunds[]',
            'shipping',
            'shipping_lines',
            'shipping_lines[]',
            'shipping_tax',
            'shipping_total',
            'status',
            'tax_lines',
            'tax_lines[]',
            'total',
            'total_tax',
            'transaction_id',
            'version',
        ],
        'products': [
            'attributes',
            'attributes[]',
            'average_rating',
            'backordered',
            'backorders',
            'backorders_allowed',
            'button_text',
            'catalog_visibility',
            'categories',
            'categories[]',
            'cross_sell_ids',
            'cross_sell_ids[]',
            'date_created',
            'date_created_gmt',
            'date_modified',
            'date_modified_gmt',
            'date_on_sale_from',
            'date_on_sale_from_gmt',
            'date_on_sale_to',
            'date_on_sale_to_gmt',
            'default_attributes',
            'default_attributes[]',
            'description',
            'dimensions',
            'download_expiry',
            'download_limit',
            'downloadable',
            'downloads',
            'downloads[]',
            'external_url',
            'grouped_products',
            'grouped_products[]',
            'id',
            'images',
            'images[]',
            'manage_stock',
            'menu_order',
            'meta_data',
            'meta_data[]',
            'name',
            'on_sale',
            'parent_id',
            'permalink',
            'price',
            'price_html',
            'purchasable',
            'purchase_note',
            'rating_count',
            'regular_price',
            'related_ids',
            'related_ids[]',
            'reviews_allowed',
            'sale_price',
            'shipping_class',
            'shipping_class_id',
            'shipping_required',
            'shipping_taxable',
            'short_description',
            'sku',
            'slug',
            'sold_individually',
            'status',
            'stock_quantity',
            'stock_status',
            'tags',
            'tags[]',
            'tax_class',
            'tax_status',
            'total_sales',
            'type',
            'upsell_ids',
            'upsell_ids[]',
            'variations',
            'variations[]',
            'virtual',
            'weight',
        ],
        'coupons': [
            'amount',
            'code',
            'date_created',
            'date_created_gmt',
            'date_expires',
            'date_expires_gmt',
            'date_modified',
            'date_modified_gmt',
            'description',
            'discount_type',
            'email_restrictions',
            'email_restrictions[]',
            'exclude_sale_items',
            'excluded_product_categories',
            'excluded_product_categories[]',
            'excluded_product_ids',
            'excluded_product_ids[]',
            'free_shipping',
            'id',
            'individual_use',
            'limit_usage_to_x_items',
            'maximum_amount',
            'meta_data',
            'meta_data[]',
            'minimum_amount',
            'product_categories',
            'product_categories[]',
            'product_ids',
            'product_ids[]',
            'usage_count',
            'usage_limit',
            'usage_limit_per_user',
            'used_by',
            'used_by[]',
        ],
        'product_categories': [
            'count',
            'description',
            'display',
            'id',
            'image',
            'image[]',
            'menu_order',
            'name',
            'parent',
            'slug',
        ],
        'product_tags': [
            'count',
            'description',
            'id',
            'name',
            'slug',
        ],
        'product_reviews': [
            'date_created',
            'date_created_gmt',
            'id',
            'product_id',
            'rating',
            'review',
            'reviewer',
            'reviewer_email',
            'status',
            'verified',
        ],
        'product_attributes': [
            'has_archives',
            'id',
            'name',
            'order_by',
            'slug',
            'type',
        ],
        'product_variations': [
            'attributes',
            'attributes[]',
            'backordered',
            'backorders',
            'backorders_allowed',
            'date_created',
            'date_created_gmt',
            'date_modified',
            'date_modified_gmt',
            'date_on_sale_from',
            'date_on_sale_from_gmt',
            'date_on_sale_to',
            'date_on_sale_to_gmt',
            'description',
            'dimensions',
            'download_expiry',
            'download_limit',
            'downloadable',
            'downloads',
            'downloads[]',
            'id',
            'image',
            'image[]',
            'manage_stock',
            'menu_order',
            'meta_data',
            'meta_data[]',
            'on_sale',
            'permalink',
            'price',
            'purchasable',
            'regular_price',
            'sale_price',
            'shipping_class',
            'shipping_class_id',
            'sku',
            'status',
            'stock_quantity',
            'stock_status',
            'tax_class',
            'tax_status',
            'virtual',
            'weight',
        ],
        'order_notes': [
            'author',
            'date_created',
            'date_created_gmt',
            'id',
            'note',
        ],
        'refunds': [
            'amount',
            'date_created',
            'date_created_gmt',
            'id',
            'line_items',
            'line_items[]',
            'meta_data',
            'meta_data[]',
            'reason',
            'refunded_by',
            'refunded_payment',
        ],
        'payment_gateways': [
            'description',
            'enabled',
            'id',
            'method_description',
            'method_supports',
            'method_supports[]',
            'method_title',
            'order',
            'settings',
            'title',
        ],
        'shipping_methods': ['description', 'id', 'title'],
        'shipping_zones': ['id', 'name', 'order'],
        'tax_rates': [
            'cities',
            'cities[]',
            'city',
            'class',
            'compound',
            'country',
            'id',
            'name',
            'order',
            'postcode',
            'postcodes',
            'postcodes[]',
            'priority',
            'rate',
            'shipping',
            'state',
        ],
        'tax_classes': ['name', 'slug'],
    },
    server_variable_defaults={'shop': 'example.com'},
)