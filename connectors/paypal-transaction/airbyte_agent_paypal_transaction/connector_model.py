"""
Connector model for paypal-transaction.

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

PaypalTransactionConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('d913b0f2-cc51-4e55-a44c-8ba1697b9239'),
    name='paypal-transaction',
    version='1.0.1',
    base_url='https://api-m.sandbox.paypal.com',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://api-m.sandbox.paypal.com/v1/oauth2/token',
            'auth_style': 'basic',
            'body_format': 'form',
        },
        user_config_spec=AirbyteAuthConfig(
            title='PayPal OAuth2 Authentication',
            type='object',
            required=['client_id', 'client_secret'],
            properties={
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='The Client ID of your PayPal developer application.',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='The Client Secret of your PayPal developer application.',
                ),
                'access_token': AuthConfigFieldSpec(
                    title='Access Token',
                    description='OAuth2 access token obtained via client credentials grant. Use the PayPal token endpoint with your client_id and client_secret to obtain this.\n',
                ),
            },
            auth_mapping={
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
                'access_token': '${access_token}',
            },
            replication_auth_key_mapping={'client_id': 'client_id', 'client_secret': 'client_secret'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='balances',
            stream_name='balances',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/reporting/balances',
                    action=Action.LIST,
                    description='List all balances for a PayPal account. Specify date time to list balances for that time. It takes a maximum of three hours for balances to appear. Lists balances up to the previous three years.\n',
                    query_params=['as_of_time', 'currency_code'],
                    query_params_schema={
                        'as_of_time': {'type': 'string', 'required': False},
                        'currency_code': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Balances response with account balance details.',
                        'properties': {
                            'balances': {
                                'type': 'array',
                                'description': 'Array of balance detail objects.',
                                'items': {
                                    'type': 'object',
                                    'description': 'Balance information for a single currency.',
                                    'properties': {
                                        'primary': {'type': 'boolean', 'description': 'Whether this is the primary currency balance.'},
                                        'currency': {'type': 'string', 'description': 'Currency code for this balance.'},
                                        'total_balance': {
                                            'type': 'object',
                                            'description': 'Currency amount with code and value.',
                                            'properties': {
                                                'currency_code': {
                                                    'type': 'string',
                                                    'description': 'Three-character ISO-4217 currency code.',
                                                    'minLength': 3,
                                                    'maxLength': 3,
                                                },
                                                'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                            },
                                        },
                                        'available_balance': {
                                            'type': 'object',
                                            'description': 'Currency amount with code and value.',
                                            'properties': {
                                                'currency_code': {
                                                    'type': 'string',
                                                    'description': 'Three-character ISO-4217 currency code.',
                                                    'minLength': 3,
                                                    'maxLength': 3,
                                                },
                                                'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                            },
                                        },
                                        'withheld_balance': {
                                            'type': 'object',
                                            'description': 'Currency amount with code and value.',
                                            'properties': {
                                                'currency_code': {
                                                    'type': 'string',
                                                    'description': 'Three-character ISO-4217 currency code.',
                                                    'minLength': 3,
                                                    'maxLength': 3,
                                                },
                                                'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                            },
                                        },
                                    },
                                },
                            },
                            'account_id': {'type': 'string', 'description': 'PayPal payer ID for the account.'},
                            'as_of_time': {'type': 'string', 'description': 'Timestamp when balances were reported.'},
                            'last_refresh_time': {'type': 'string', 'description': 'Timestamp when balances were last refreshed.'},
                        },
                        'x-airbyte-entity-name': 'balances',
                        'x-airbyte-stream-name': 'balances',
                    },
                    preferred_for_check=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Balances response with account balance details.',
                'properties': {
                    'balances': {
                        'type': 'array',
                        'description': 'Array of balance detail objects.',
                        'items': {'$ref': '#/components/schemas/BalanceDetail'},
                    },
                    'account_id': {'type': 'string', 'description': 'PayPal payer ID for the account.'},
                    'as_of_time': {'type': 'string', 'description': 'Timestamp when balances were reported.'},
                    'last_refresh_time': {'type': 'string', 'description': 'Timestamp when balances were last refreshed.'},
                },
                'x-airbyte-entity-name': 'balances',
                'x-airbyte-stream-name': 'balances',
            },
        ),
        EntityDefinition(
            name='transactions',
            stream_name='transactions',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/reporting/transactions',
                    action=Action.LIST,
                    description='Lists transactions for a PayPal account. Specify one or more query parameters to filter the transactions. Requires start_date and end_date parameters. The maximum supported date range is 31 days. It takes a maximum of three hours for executed transactions to appear.\n',
                    query_params=[
                        'start_date',
                        'end_date',
                        'transaction_id',
                        'transaction_type',
                        'transaction_status',
                        'transaction_currency',
                        'fields',
                        'page_size',
                        'page',
                        'balance_affecting_records_only',
                    ],
                    query_params_schema={
                        'start_date': {'type': 'string', 'required': True},
                        'end_date': {'type': 'string', 'required': True},
                        'transaction_id': {'type': 'string', 'required': False},
                        'transaction_type': {'type': 'string', 'required': False},
                        'transaction_status': {'type': 'string', 'required': False},
                        'transaction_currency': {'type': 'string', 'required': False},
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'all',
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'balance_affecting_records_only': {
                            'type': 'string',
                            'required': False,
                            'default': 'Y',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of transactions.',
                        'properties': {
                            'transaction_details': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A single PayPal transaction with full details.',
                                    'properties': {
                                        'transaction_info': {
                                            'type': 'object',
                                            'description': 'Detailed transaction information.',
                                            'properties': {
                                                'paypal_account_id': {'type': 'string', 'description': 'PayPal account ID for the transaction.'},
                                                'transaction_id': {'type': 'string', 'description': 'Unique transaction ID.'},
                                                'paypal_reference_id': {'type': 'string', 'description': 'PayPal reference ID.'},
                                                'paypal_reference_id_type': {'type': 'string', 'description': 'Type of PayPal reference ID.'},
                                                'transaction_event_code': {'type': 'string', 'description': 'Transaction event code.'},
                                                'transaction_initiation_date': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Date and time the transaction was initiated.',
                                                },
                                                'transaction_updated_date': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Date and time the transaction was last updated.',
                                                },
                                                'transaction_amount': {
                                                    'type': 'object',
                                                    'description': 'Currency amount with code and value.',
                                                    'properties': {
                                                        'currency_code': {
                                                            'type': 'string',
                                                            'description': 'Three-character ISO-4217 currency code.',
                                                            'minLength': 3,
                                                            'maxLength': 3,
                                                        },
                                                        'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                    },
                                                },
                                                'fee_amount': {
                                                    'type': 'object',
                                                    'description': 'Currency amount with code and value.',
                                                    'properties': {
                                                        'currency_code': {
                                                            'type': 'string',
                                                            'description': 'Three-character ISO-4217 currency code.',
                                                            'minLength': 3,
                                                            'maxLength': 3,
                                                        },
                                                        'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                    },
                                                },
                                                'insurance_amount': {
                                                    'type': 'object',
                                                    'description': 'Currency amount with code and value.',
                                                    'properties': {
                                                        'currency_code': {
                                                            'type': 'string',
                                                            'description': 'Three-character ISO-4217 currency code.',
                                                            'minLength': 3,
                                                            'maxLength': 3,
                                                        },
                                                        'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                    },
                                                },
                                                'shipping_amount': {
                                                    'type': 'object',
                                                    'description': 'Currency amount with code and value.',
                                                    'properties': {
                                                        'currency_code': {
                                                            'type': 'string',
                                                            'description': 'Three-character ISO-4217 currency code.',
                                                            'minLength': 3,
                                                            'maxLength': 3,
                                                        },
                                                        'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                    },
                                                },
                                                'shipping_discount_amount': {
                                                    'type': 'object',
                                                    'description': 'Currency amount with code and value.',
                                                    'properties': {
                                                        'currency_code': {
                                                            'type': 'string',
                                                            'description': 'Three-character ISO-4217 currency code.',
                                                            'minLength': 3,
                                                            'maxLength': 3,
                                                        },
                                                        'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                    },
                                                },
                                                'transaction_status': {'type': 'string', 'description': 'Transaction status: D=Denied, P=Pending, S=Success, V=Reversed.'},
                                                'transaction_subject': {'type': 'string', 'description': 'Subject or purpose of the transaction.'},
                                                'transaction_note': {'type': 'string', 'description': 'Note or comment on the transaction.'},
                                                'invoice_id': {'type': 'string', 'description': 'Invoice ID associated with the transaction.'},
                                                'custom_field': {'type': 'string', 'description': 'Custom field associated with the transaction.'},
                                                'protection_eligibility': {'type': 'string', 'description': 'Protection eligibility status.'},
                                            },
                                        },
                                        'payer_info': {
                                            'type': 'object',
                                            'description': 'Information about the payer.',
                                            'properties': {
                                                'account_id': {'type': 'string', 'description': 'Payer account ID.'},
                                                'email_address': {'type': 'string', 'description': 'Payer email address.'},
                                                'address_status': {'type': 'string', 'description': 'Status of the payer address.'},
                                                'payer_status': {'type': 'string', 'description': 'Status of the payer.'},
                                                'payer_name': {
                                                    'type': 'object',
                                                    'description': 'Payer name details.',
                                                    'properties': {
                                                        'given_name': {'type': 'string', 'description': 'Given name of the payer.'},
                                                        'surname': {'type': 'string', 'description': 'Surname of the payer.'},
                                                        'alternate_full_name': {'type': 'string', 'description': 'Alternate full name.'},
                                                    },
                                                },
                                                'country_code': {'type': 'string', 'description': 'Country code of the payer.'},
                                            },
                                        },
                                        'shipping_info': {
                                            'type': 'object',
                                            'description': 'Shipping information for the transaction.',
                                            'properties': {
                                                'name': {'type': 'string', 'description': 'Recipient name.'},
                                                'address': {
                                                    'type': 'object',
                                                    'description': 'Shipping address details.',
                                                    'properties': {
                                                        'line1': {'type': 'string', 'description': 'First line of the address.'},
                                                        'line2': {'type': 'string', 'description': 'Second line of the address.'},
                                                        'city': {'type': 'string', 'description': 'City.'},
                                                        'country_code': {'type': 'string', 'description': 'Country code.'},
                                                        'postal_code': {'type': 'string', 'description': 'Postal code.'},
                                                    },
                                                },
                                            },
                                        },
                                        'cart_info': {
                                            'type': 'object',
                                            'description': 'Cart information for the transaction.',
                                            'properties': {
                                                'item_details': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'Details for a single cart item.',
                                                        'properties': {
                                                            'item_code': {'type': 'string', 'description': 'Item code.'},
                                                            'item_name': {'type': 'string', 'description': 'Item name.'},
                                                            'item_description': {'type': 'string', 'description': 'Item description.'},
                                                            'item_quantity': {'type': 'string', 'description': 'Item quantity.'},
                                                            'item_unit_price': {
                                                                'type': 'object',
                                                                'description': 'Currency amount with code and value.',
                                                                'properties': {
                                                                    'currency_code': {
                                                                        'type': 'string',
                                                                        'description': 'Three-character ISO-4217 currency code.',
                                                                        'minLength': 3,
                                                                        'maxLength': 3,
                                                                    },
                                                                    'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                                },
                                                            },
                                                            'item_amount': {
                                                                'type': 'object',
                                                                'description': 'Currency amount with code and value.',
                                                                'properties': {
                                                                    'currency_code': {
                                                                        'type': 'string',
                                                                        'description': 'Three-character ISO-4217 currency code.',
                                                                        'minLength': 3,
                                                                        'maxLength': 3,
                                                                    },
                                                                    'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                                },
                                                            },
                                                            'total_item_amount': {
                                                                'type': 'object',
                                                                'description': 'Currency amount with code and value.',
                                                                'properties': {
                                                                    'currency_code': {
                                                                        'type': 'string',
                                                                        'description': 'Three-character ISO-4217 currency code.',
                                                                        'minLength': 3,
                                                                        'maxLength': 3,
                                                                    },
                                                                    'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                                },
                                                            },
                                                            'tax_amounts': {
                                                                'type': 'array',
                                                                'items': {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'tax_amount': {
                                                                            'type': 'object',
                                                                            'description': 'Currency amount with code and value.',
                                                                            'properties': {
                                                                                'currency_code': {
                                                                                    'type': 'string',
                                                                                    'description': 'Three-character ISO-4217 currency code.',
                                                                                    'minLength': 3,
                                                                                    'maxLength': 3,
                                                                                },
                                                                                'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'invoice_number': {'type': 'string', 'description': 'Invoice number for the item.'},
                                                        },
                                                    },
                                                },
                                                'tax_inclusive': {'type': 'boolean', 'description': 'Whether item amounts include tax.'},
                                                'paypal_invoice_id': {'type': 'string', 'description': 'PayPal-generated invoice ID.'},
                                            },
                                        },
                                        'auction_info': {
                                            'type': 'object',
                                            'description': 'Auction information.',
                                            'properties': {
                                                'auction_site': {'type': 'string', 'description': 'Name of the auction site.'},
                                                'auction_item_site': {'type': 'string', 'description': 'Auction item URL.'},
                                                'auction_buyer_id': {'type': 'string', 'description': 'Buyer ID in the auction.'},
                                                'auction_closing_date': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Auction closing date.',
                                                },
                                            },
                                        },
                                        'incentive_info': {
                                            'type': 'object',
                                            'description': 'Incentive information.',
                                            'properties': {
                                                'incentive_details': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'description': 'Incentive detail.',
                                                        'properties': {
                                                            'incentive_type': {'type': 'string', 'description': 'Type of incentive.'},
                                                            'incentive_code': {'type': 'string', 'description': 'Incentive code.'},
                                                            'incentive_amount': {
                                                                'type': 'object',
                                                                'description': 'Currency amount with code and value.',
                                                                'properties': {
                                                                    'currency_code': {
                                                                        'type': 'string',
                                                                        'description': 'Three-character ISO-4217 currency code.',
                                                                        'minLength': 3,
                                                                        'maxLength': 3,
                                                                    },
                                                                    'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                                },
                                                            },
                                                            'incentive_program_code': {'type': 'string', 'description': 'Incentive program code.'},
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'store_info': {
                                            'type': 'object',
                                            'description': 'Store information.',
                                            'properties': {
                                                'store_id': {'type': 'string', 'description': 'Store ID.'},
                                                'terminal_id': {'type': 'string', 'description': 'Terminal ID.'},
                                            },
                                        },
                                        'transaction_id': {'type': 'string', 'description': 'Top-level transaction ID.'},
                                        'transaction_updated_date': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Top-level transaction updated date.',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'transactions',
                                    'x-airbyte-stream-name': 'transactions',
                                },
                            },
                            'account_number': {'type': 'string', 'description': 'Encrypted account number for the PayPal account.'},
                            'start_date': {'type': 'string', 'description': 'Start date of the query range.'},
                            'end_date': {'type': 'string', 'description': 'End date of the query range.'},
                            'last_refreshed_datetime': {'type': 'string', 'description': 'Last data refresh timestamp.'},
                            'page': {'type': 'integer', 'description': 'Current page number.'},
                            'total_items': {'type': 'integer', 'description': 'Total number of items.'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages.'},
                            'links': {
                                'type': 'array',
                                'description': 'HATEOAS links for pagination.',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'href': {'type': 'string'},
                                        'rel': {'type': 'string'},
                                        'method': {'type': 'string'},
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.transaction_details',
                    meta_extractor={
                        'total_items': '$.total_items',
                        'total_pages': '$.total_pages',
                        'page': '$.page',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A single PayPal transaction with full details.',
                'properties': {
                    'transaction_info': {'$ref': '#/components/schemas/TransactionInfo'},
                    'payer_info': {'$ref': '#/components/schemas/PayerInfo'},
                    'shipping_info': {'$ref': '#/components/schemas/ShippingInfo'},
                    'cart_info': {'$ref': '#/components/schemas/CartInfo'},
                    'auction_info': {'$ref': '#/components/schemas/AuctionInfo'},
                    'incentive_info': {'$ref': '#/components/schemas/IncentiveInfo'},
                    'store_info': {'$ref': '#/components/schemas/StoreInfo'},
                    'transaction_id': {'type': 'string', 'description': 'Top-level transaction ID.'},
                    'transaction_updated_date': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Top-level transaction updated date.',
                    },
                },
                'x-airbyte-entity-name': 'transactions',
                'x-airbyte-stream-name': 'transactions',
            },
        ),
        EntityDefinition(
            name='list_payments',
            stream_name='list_payments',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/payments/payment',
                    action=Action.LIST,
                    description='Lists payments for the PayPal account. Supports filtering by start and end times.\n',
                    query_params=[
                        'start_time',
                        'end_time',
                        'count',
                        'start_id',
                    ],
                    query_params_schema={
                        'start_time': {'type': 'string', 'required': False},
                        'end_time': {'type': 'string', 'required': False},
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'start_id': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'List of payments.',
                        'properties': {
                            'payments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A PayPal payment object.',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Payment ID.'},
                                        'intent': {'type': 'string', 'description': 'Payment intent (sale, authorize, order).'},
                                        'state': {'type': 'string', 'description': 'Payment state.'},
                                        'cart': {'type': 'string', 'description': 'Cart ID.'},
                                        'payer': {
                                            'type': 'object',
                                            'description': 'Payer information.',
                                            'properties': {
                                                'payment_method': {'type': 'string', 'description': 'Payment method.'},
                                                'status': {'type': 'string', 'description': 'Payer status.'},
                                                'payer_info': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'email': {'type': 'string', 'description': 'Payer email.'},
                                                        'first_name': {'type': 'string', 'description': 'Payer first name.'},
                                                        'last_name': {'type': 'string', 'description': 'Payer last name.'},
                                                        'payer_id': {'type': 'string', 'description': 'Payer ID.'},
                                                        'country_code': {'type': 'string', 'description': 'Payer country code.'},
                                                    },
                                                },
                                            },
                                        },
                                        'transactions': {
                                            'type': 'array',
                                            'description': 'Array of transaction objects within the payment.',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'amount': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'total': {'type': 'string', 'description': 'Total amount.'},
                                                            'currency': {'type': 'string', 'description': 'Currency code.'},
                                                            'details': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'subtotal': {'type': 'string'},
                                                                    'shipping': {'type': 'string'},
                                                                    'insurance': {'type': 'string'},
                                                                    'handling_fee': {'type': 'string'},
                                                                    'shipping_discount': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                    'description': {'type': 'string', 'description': 'Transaction description.'},
                                                    'related_resources': {
                                                        'type': 'array',
                                                        'items': {'type': 'object', 'additionalProperties': True},
                                                    },
                                                },
                                            },
                                        },
                                        'create_time': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Payment creation time.',
                                        },
                                        'update_time': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Payment last update time.',
                                        },
                                        'links': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'href': {'type': 'string'},
                                                    'rel': {'type': 'string'},
                                                    'method': {'type': 'string'},
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'list_payments',
                                    'x-airbyte-stream-name': 'list_payments',
                                },
                            },
                            'count': {'type': 'integer', 'description': 'Number of payments returned.'},
                            'next_id': {'type': 'string', 'description': 'Next payment ID for pagination.'},
                        },
                    },
                    record_extractor='$.payments',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A PayPal payment object.',
                'properties': {
                    'id': {'type': 'string', 'description': 'Payment ID.'},
                    'intent': {'type': 'string', 'description': 'Payment intent (sale, authorize, order).'},
                    'state': {'type': 'string', 'description': 'Payment state.'},
                    'cart': {'type': 'string', 'description': 'Cart ID.'},
                    'payer': {
                        'type': 'object',
                        'description': 'Payer information.',
                        'properties': {
                            'payment_method': {'type': 'string', 'description': 'Payment method.'},
                            'status': {'type': 'string', 'description': 'Payer status.'},
                            'payer_info': {
                                'type': 'object',
                                'properties': {
                                    'email': {'type': 'string', 'description': 'Payer email.'},
                                    'first_name': {'type': 'string', 'description': 'Payer first name.'},
                                    'last_name': {'type': 'string', 'description': 'Payer last name.'},
                                    'payer_id': {'type': 'string', 'description': 'Payer ID.'},
                                    'country_code': {'type': 'string', 'description': 'Payer country code.'},
                                },
                            },
                        },
                    },
                    'transactions': {
                        'type': 'array',
                        'description': 'Array of transaction objects within the payment.',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'amount': {
                                    'type': 'object',
                                    'properties': {
                                        'total': {'type': 'string', 'description': 'Total amount.'},
                                        'currency': {'type': 'string', 'description': 'Currency code.'},
                                        'details': {
                                            'type': 'object',
                                            'properties': {
                                                'subtotal': {'type': 'string'},
                                                'shipping': {'type': 'string'},
                                                'insurance': {'type': 'string'},
                                                'handling_fee': {'type': 'string'},
                                                'shipping_discount': {'type': 'string'},
                                            },
                                        },
                                    },
                                },
                                'description': {'type': 'string', 'description': 'Transaction description.'},
                                'related_resources': {
                                    'type': 'array',
                                    'items': {'type': 'object', 'additionalProperties': True},
                                },
                            },
                        },
                    },
                    'create_time': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Payment creation time.',
                    },
                    'update_time': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Payment last update time.',
                    },
                    'links': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'href': {'type': 'string'},
                                'rel': {'type': 'string'},
                                'method': {'type': 'string'},
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'list_payments',
                'x-airbyte-stream-name': 'list_payments',
            },
        ),
        EntityDefinition(
            name='list_disputes',
            stream_name='list_disputes',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/customer/disputes',
                    action=Action.LIST,
                    description='Lists disputes for the PayPal account. Supports filtering by update time range.\n',
                    query_params=[
                        'update_time_after',
                        'update_time_before',
                        'page_size',
                        'next_page_token',
                    ],
                    query_params_schema={
                        'update_time_after': {'type': 'string', 'required': False},
                        'update_time_before': {'type': 'string', 'required': False},
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'next_page_token': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'List of disputes.',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A PayPal dispute object.',
                                    'properties': {
                                        'dispute_id': {'type': 'string', 'description': 'Unique dispute identifier.'},
                                        'create_time': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Dispute creation time.',
                                        },
                                        'update_time': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Dispute last update time.',
                                        },
                                        'status': {'type': 'string', 'description': 'Current dispute status.'},
                                        'reason': {'type': 'string', 'description': 'Reason for the dispute.'},
                                        'dispute_state': {'type': 'string', 'description': 'Current state of the dispute.'},
                                        'dispute_life_cycle_stage': {'type': 'string', 'description': 'Life cycle stage of the dispute.'},
                                        'dispute_channel': {'type': 'string', 'description': 'Channel through which the dispute was initiated.'},
                                        'dispute_amount': {
                                            'type': 'object',
                                            'description': 'Currency amount with code and value.',
                                            'properties': {
                                                'currency_code': {
                                                    'type': 'string',
                                                    'description': 'Three-character ISO-4217 currency code.',
                                                    'minLength': 3,
                                                    'maxLength': 3,
                                                },
                                                'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                            },
                                        },
                                        'outcome': {'type': 'string', 'description': 'Outcome of the dispute resolution.'},
                                        'disputed_transactions': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'buyer_transaction_id': {'type': 'string', 'description': "Buyer's transaction ID."},
                                                    'seller': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'merchant_id': {'type': 'string', 'description': "Seller's merchant ID."},
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'links': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'href': {'type': 'string'},
                                                    'rel': {'type': 'string'},
                                                    'method': {'type': 'string'},
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'list_disputes',
                                    'x-airbyte-stream-name': 'list_disputes',
                                },
                            },
                            'links': {
                                'type': 'array',
                                'description': 'HATEOAS links for pagination.',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'href': {'type': 'string'},
                                        'rel': {'type': 'string'},
                                        'method': {'type': 'string'},
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.items',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A PayPal dispute object.',
                'properties': {
                    'dispute_id': {'type': 'string', 'description': 'Unique dispute identifier.'},
                    'create_time': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Dispute creation time.',
                    },
                    'update_time': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Dispute last update time.',
                    },
                    'status': {'type': 'string', 'description': 'Current dispute status.'},
                    'reason': {'type': 'string', 'description': 'Reason for the dispute.'},
                    'dispute_state': {'type': 'string', 'description': 'Current state of the dispute.'},
                    'dispute_life_cycle_stage': {'type': 'string', 'description': 'Life cycle stage of the dispute.'},
                    'dispute_channel': {'type': 'string', 'description': 'Channel through which the dispute was initiated.'},
                    'dispute_amount': {'$ref': '#/components/schemas/Money'},
                    'outcome': {'type': 'string', 'description': 'Outcome of the dispute resolution.'},
                    'disputed_transactions': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'buyer_transaction_id': {'type': 'string', 'description': "Buyer's transaction ID."},
                                'seller': {
                                    'type': 'object',
                                    'properties': {
                                        'merchant_id': {'type': 'string', 'description': "Seller's merchant ID."},
                                    },
                                },
                            },
                        },
                    },
                    'links': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'href': {'type': 'string'},
                                'rel': {'type': 'string'},
                                'method': {'type': 'string'},
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'list_disputes',
                'x-airbyte-stream-name': 'list_disputes',
            },
        ),
        EntityDefinition(
            name='list_products',
            stream_name='list_products',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/catalogs/products',
                    action=Action.LIST,
                    description='Lists all catalog products for the PayPal account.',
                    query_params=['page_size', 'page'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'List of catalog products.',
                        'properties': {
                            'products': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A PayPal catalog product (summary).',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Product ID.'},
                                        'name': {'type': 'string', 'description': 'Product name.'},
                                        'description': {'type': 'string', 'description': 'Product description.'},
                                        'create_time': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Product creation time.',
                                        },
                                        'links': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'href': {'type': 'string'},
                                                    'rel': {'type': 'string'},
                                                    'method': {'type': 'string'},
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'list_products',
                                    'x-airbyte-stream-name': 'list_products',
                                },
                            },
                            'links': {
                                'type': 'array',
                                'description': 'HATEOAS links for pagination.',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'href': {'type': 'string'},
                                        'rel': {'type': 'string'},
                                        'method': {'type': 'string'},
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.products',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A PayPal catalog product (summary).',
                'properties': {
                    'id': {'type': 'string', 'description': 'Product ID.'},
                    'name': {'type': 'string', 'description': 'Product name.'},
                    'description': {'type': 'string', 'description': 'Product description.'},
                    'create_time': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Product creation time.',
                    },
                    'links': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'href': {'type': 'string'},
                                'rel': {'type': 'string'},
                                'method': {'type': 'string'},
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'list_products',
                'x-airbyte-stream-name': 'list_products',
            },
        ),
        EntityDefinition(
            name='show_product_details',
            stream_name='show_product_details',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/catalogs/products/{id}',
                    action=Action.GET,
                    description='Shows details for a catalog product by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Detailed catalog product information.',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Product ID.'},
                            'name': {'type': 'string', 'description': 'Product name.'},
                            'description': {'type': 'string', 'description': 'Product description.'},
                            'type': {'type': 'string', 'description': 'Product type.'},
                            'category': {'type': 'string', 'description': 'Product category.'},
                            'image_url': {'type': 'string', 'description': 'Product image URL.'},
                            'home_url': {'type': 'string', 'description': 'Product home URL.'},
                            'create_time': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Product creation time.',
                            },
                            'update_time': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Product last update time.',
                            },
                            'links': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'href': {'type': 'string'},
                                        'rel': {'type': 'string'},
                                        'method': {'type': 'string'},
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'show_product_details',
                        'x-airbyte-stream-name': 'show_product_details',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Detailed catalog product information.',
                'properties': {
                    'id': {'type': 'string', 'description': 'Product ID.'},
                    'name': {'type': 'string', 'description': 'Product name.'},
                    'description': {'type': 'string', 'description': 'Product description.'},
                    'type': {'type': 'string', 'description': 'Product type.'},
                    'category': {'type': 'string', 'description': 'Product category.'},
                    'image_url': {'type': 'string', 'description': 'Product image URL.'},
                    'home_url': {'type': 'string', 'description': 'Product home URL.'},
                    'create_time': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Product creation time.',
                    },
                    'update_time': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Product last update time.',
                    },
                    'links': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'href': {'type': 'string'},
                                'rel': {'type': 'string'},
                                'method': {'type': 'string'},
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'show_product_details',
                'x-airbyte-stream-name': 'show_product_details',
            },
        ),
        EntityDefinition(
            name='search_invoices',
            stream_name='search_invoices',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v2/invoicing/search-invoices',
                    action=Action.LIST,
                    description='Searches for invoices matching the specified criteria. Uses POST with a JSON body for filtering.\n',
                    body_fields=['creation_date_range'],
                    query_params=['page_size', 'page'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for searching invoices.',
                        'properties': {
                            'creation_date_range': {
                                'type': 'object',
                                'description': 'Filter by invoice creation date range.',
                                'properties': {
                                    'start': {'type': 'string', 'description': 'Start date in ISO 8601 format.'},
                                    'end': {'type': 'string', 'description': 'End date in ISO 8601 format.'},
                                },
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of invoices from search.',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A PayPal invoice object.',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Invoice ID.'},
                                        'status': {'type': 'string', 'description': 'Invoice status.'},
                                        'detail': {
                                            'type': 'object',
                                            'description': 'Invoice detail information.',
                                            'properties': {
                                                'reference': {'type': 'string', 'description': 'Reference for the invoice.'},
                                                'currency_code': {'type': 'string', 'description': 'Currency code.'},
                                                'note': {'type': 'string', 'description': 'Note to the recipient.'},
                                                'terms_and_conditions': {'type': 'string', 'description': 'Terms and conditions.'},
                                                'memo': {'type': 'string', 'description': 'Memo for the invoice.'},
                                                'invoice_number': {'type': 'string', 'description': 'Invoice number.'},
                                                'invoice_date': {'type': 'string', 'description': 'Invoice date.'},
                                                'payment_term': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'term_type': {'type': 'string', 'description': 'Payment term type.'},
                                                        'due_date': {'type': 'string', 'description': 'Due date.'},
                                                    },
                                                },
                                                'metadata': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'create_time': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'Invoice creation time.',
                                                        },
                                                        'created_by': {'type': 'string', 'description': 'Creator of the invoice.'},
                                                        'last_update_time': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'Last update time.',
                                                        },
                                                        'last_updated_by': {'type': 'string', 'description': 'Last updater.'},
                                                        'first_sent_time': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'First sent time.',
                                                        },
                                                        'last_sent_time': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'Last sent time.',
                                                        },
                                                        'created_by_flow': {'type': 'string', 'description': 'Flow that created the invoice.'},
                                                        'invoicer_view_url': {'type': 'string', 'description': 'Invoicer view URL.'},
                                                        'recipient_view_url': {'type': 'string', 'description': 'Recipient view URL.'},
                                                        'cancel_time': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'Cancellation time.',
                                                        },
                                                        'cancelled_by': {'type': 'string', 'description': 'Canceller.'},
                                                    },
                                                },
                                            },
                                        },
                                        'invoicer': {
                                            'type': 'object',
                                            'description': 'Invoicer details.',
                                            'properties': {
                                                'name': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'given_name': {'type': 'string'},
                                                        'surname': {'type': 'string'},
                                                        'full_name': {'type': 'string'},
                                                    },
                                                },
                                                'address': {'type': 'object', 'additionalProperties': True},
                                                'email_address': {'type': 'string', 'description': 'Invoicer email.'},
                                            },
                                        },
                                        'primary_recipients': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'billing_info': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'given_name': {'type': 'string'},
                                                                    'surname': {'type': 'string'},
                                                                    'full_name': {'type': 'string'},
                                                                },
                                                            },
                                                            'email_address': {'type': 'string'},
                                                            'additional_info_value': {'type': 'string'},
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'additional_recipients': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                        },
                                        'items': {
                                            'type': 'array',
                                            'description': 'Line items on the invoice.',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {'type': 'string'},
                                                    'description': {'type': 'string'},
                                                    'quantity': {'type': 'string'},
                                                    'unit_amount': {
                                                        'type': 'object',
                                                        'description': 'Currency amount with code and value.',
                                                        'properties': {
                                                            'currency_code': {
                                                                'type': 'string',
                                                                'description': 'Three-character ISO-4217 currency code.',
                                                                'minLength': 3,
                                                                'maxLength': 3,
                                                            },
                                                            'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                        },
                                                    },
                                                    'tax': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string'},
                                                            'percent': {'type': 'string'},
                                                            'amount': {
                                                                'type': 'object',
                                                                'description': 'Currency amount with code and value.',
                                                                'properties': {
                                                                    'currency_code': {
                                                                        'type': 'string',
                                                                        'description': 'Three-character ISO-4217 currency code.',
                                                                        'minLength': 3,
                                                                        'maxLength': 3,
                                                                    },
                                                                    'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                                },
                                                            },
                                                        },
                                                    },
                                                    'unit_of_measure': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'amount': {
                                            'type': 'object',
                                            'description': 'Total invoice amount.',
                                            'properties': {
                                                'currency_code': {'type': 'string'},
                                                'value': {'type': 'string'},
                                                'breakdown': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'item_total': {
                                                            'type': 'object',
                                                            'description': 'Currency amount with code and value.',
                                                            'properties': {
                                                                'currency_code': {
                                                                    'type': 'string',
                                                                    'description': 'Three-character ISO-4217 currency code.',
                                                                    'minLength': 3,
                                                                    'maxLength': 3,
                                                                },
                                                                'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                            },
                                                        },
                                                        'discount': {'type': 'object', 'additionalProperties': True},
                                                        'tax_total': {
                                                            'type': 'object',
                                                            'description': 'Currency amount with code and value.',
                                                            'properties': {
                                                                'currency_code': {
                                                                    'type': 'string',
                                                                    'description': 'Three-character ISO-4217 currency code.',
                                                                    'minLength': 3,
                                                                    'maxLength': 3,
                                                                },
                                                                'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                            },
                                                        },
                                                        'shipping': {
                                                            'type': 'object',
                                                            'description': 'Currency amount with code and value.',
                                                            'properties': {
                                                                'currency_code': {
                                                                    'type': 'string',
                                                                    'description': 'Three-character ISO-4217 currency code.',
                                                                    'minLength': 3,
                                                                    'maxLength': 3,
                                                                },
                                                                'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                            },
                                                        },
                                                        'custom': {'type': 'object', 'additionalProperties': True},
                                                    },
                                                },
                                            },
                                        },
                                        'configuration': {
                                            'type': 'object',
                                            'description': 'Invoice configuration.',
                                            'properties': {
                                                'tax_calculated_after_discount': {'type': 'string'},
                                                'tax_inclusive': {'type': 'string'},
                                                'allow_tip': {'type': 'string'},
                                                'template_id': {'type': 'string'},
                                                'partial_payment': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'allow_partial_payment': {'type': 'string'},
                                                        'minimum_amount_due': {
                                                            'type': 'object',
                                                            'description': 'Currency amount with code and value.',
                                                            'properties': {
                                                                'currency_code': {
                                                                    'type': 'string',
                                                                    'description': 'Three-character ISO-4217 currency code.',
                                                                    'minLength': 3,
                                                                    'maxLength': 3,
                                                                },
                                                                'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'due_amount': {
                                            'type': 'object',
                                            'description': 'Currency amount with code and value.',
                                            'properties': {
                                                'currency_code': {
                                                    'type': 'string',
                                                    'description': 'Three-character ISO-4217 currency code.',
                                                    'minLength': 3,
                                                    'maxLength': 3,
                                                },
                                                'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                            },
                                        },
                                        'payments': {
                                            'type': 'object',
                                            'description': 'Payment records for this invoice.',
                                            'properties': {
                                                'paid_amount': {
                                                    'type': 'object',
                                                    'description': 'Currency amount with code and value.',
                                                    'properties': {
                                                        'currency_code': {
                                                            'type': 'string',
                                                            'description': 'Three-character ISO-4217 currency code.',
                                                            'minLength': 3,
                                                            'maxLength': 3,
                                                        },
                                                        'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                    },
                                                },
                                                'transactions': {
                                                    'type': 'array',
                                                    'items': {'type': 'object', 'additionalProperties': True},
                                                },
                                            },
                                        },
                                        'refunds': {
                                            'type': 'object',
                                            'description': 'Refund records for this invoice.',
                                            'properties': {
                                                'refund_amount': {
                                                    'type': 'object',
                                                    'description': 'Currency amount with code and value.',
                                                    'properties': {
                                                        'currency_code': {
                                                            'type': 'string',
                                                            'description': 'Three-character ISO-4217 currency code.',
                                                            'minLength': 3,
                                                            'maxLength': 3,
                                                        },
                                                        'value': {'type': 'string', 'description': 'Monetary value as a string.'},
                                                    },
                                                },
                                                'transactions': {
                                                    'type': 'array',
                                                    'items': {'type': 'object', 'additionalProperties': True},
                                                },
                                            },
                                        },
                                        'links': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'href': {'type': 'string'},
                                                    'rel': {'type': 'string'},
                                                    'method': {'type': 'string'},
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'search_invoices',
                                    'x-airbyte-stream-name': 'search_invoices',
                                },
                            },
                            'total_items': {'type': 'integer', 'description': 'Total number of matching invoices.'},
                            'total_pages': {'type': 'integer', 'description': 'Total number of pages.'},
                        },
                    },
                    record_extractor='$.items',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A PayPal invoice object.',
                'properties': {
                    'id': {'type': 'string', 'description': 'Invoice ID.'},
                    'status': {'type': 'string', 'description': 'Invoice status.'},
                    'detail': {
                        'type': 'object',
                        'description': 'Invoice detail information.',
                        'properties': {
                            'reference': {'type': 'string', 'description': 'Reference for the invoice.'},
                            'currency_code': {'type': 'string', 'description': 'Currency code.'},
                            'note': {'type': 'string', 'description': 'Note to the recipient.'},
                            'terms_and_conditions': {'type': 'string', 'description': 'Terms and conditions.'},
                            'memo': {'type': 'string', 'description': 'Memo for the invoice.'},
                            'invoice_number': {'type': 'string', 'description': 'Invoice number.'},
                            'invoice_date': {'type': 'string', 'description': 'Invoice date.'},
                            'payment_term': {
                                'type': 'object',
                                'properties': {
                                    'term_type': {'type': 'string', 'description': 'Payment term type.'},
                                    'due_date': {'type': 'string', 'description': 'Due date.'},
                                },
                            },
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'create_time': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Invoice creation time.',
                                    },
                                    'created_by': {'type': 'string', 'description': 'Creator of the invoice.'},
                                    'last_update_time': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Last update time.',
                                    },
                                    'last_updated_by': {'type': 'string', 'description': 'Last updater.'},
                                    'first_sent_time': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'First sent time.',
                                    },
                                    'last_sent_time': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Last sent time.',
                                    },
                                    'created_by_flow': {'type': 'string', 'description': 'Flow that created the invoice.'},
                                    'invoicer_view_url': {'type': 'string', 'description': 'Invoicer view URL.'},
                                    'recipient_view_url': {'type': 'string', 'description': 'Recipient view URL.'},
                                    'cancel_time': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Cancellation time.',
                                    },
                                    'cancelled_by': {'type': 'string', 'description': 'Canceller.'},
                                },
                            },
                        },
                    },
                    'invoicer': {
                        'type': 'object',
                        'description': 'Invoicer details.',
                        'properties': {
                            'name': {
                                'type': 'object',
                                'properties': {
                                    'given_name': {'type': 'string'},
                                    'surname': {'type': 'string'},
                                    'full_name': {'type': 'string'},
                                },
                            },
                            'address': {'type': 'object', 'additionalProperties': True},
                            'email_address': {'type': 'string', 'description': 'Invoicer email.'},
                        },
                    },
                    'primary_recipients': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'billing_info': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {
                                            'type': 'object',
                                            'properties': {
                                                'given_name': {'type': 'string'},
                                                'surname': {'type': 'string'},
                                                'full_name': {'type': 'string'},
                                            },
                                        },
                                        'email_address': {'type': 'string'},
                                        'additional_info_value': {'type': 'string'},
                                    },
                                },
                            },
                        },
                    },
                    'additional_recipients': {
                        'type': 'array',
                        'items': {'type': 'string'},
                    },
                    'items': {
                        'type': 'array',
                        'description': 'Line items on the invoice.',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'name': {'type': 'string'},
                                'description': {'type': 'string'},
                                'quantity': {'type': 'string'},
                                'unit_amount': {'$ref': '#/components/schemas/Money'},
                                'tax': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                        'percent': {'type': 'string'},
                                        'amount': {'$ref': '#/components/schemas/Money'},
                                    },
                                },
                                'unit_of_measure': {'type': 'string'},
                            },
                        },
                    },
                    'amount': {
                        'type': 'object',
                        'description': 'Total invoice amount.',
                        'properties': {
                            'currency_code': {'type': 'string'},
                            'value': {'type': 'string'},
                            'breakdown': {
                                'type': 'object',
                                'properties': {
                                    'item_total': {'$ref': '#/components/schemas/Money'},
                                    'discount': {'type': 'object', 'additionalProperties': True},
                                    'tax_total': {'$ref': '#/components/schemas/Money'},
                                    'shipping': {'$ref': '#/components/schemas/Money'},
                                    'custom': {'type': 'object', 'additionalProperties': True},
                                },
                            },
                        },
                    },
                    'configuration': {
                        'type': 'object',
                        'description': 'Invoice configuration.',
                        'properties': {
                            'tax_calculated_after_discount': {'type': 'string'},
                            'tax_inclusive': {'type': 'string'},
                            'allow_tip': {'type': 'string'},
                            'template_id': {'type': 'string'},
                            'partial_payment': {
                                'type': 'object',
                                'properties': {
                                    'allow_partial_payment': {'type': 'string'},
                                    'minimum_amount_due': {'$ref': '#/components/schemas/Money'},
                                },
                            },
                        },
                    },
                    'due_amount': {'$ref': '#/components/schemas/Money'},
                    'payments': {
                        'type': 'object',
                        'description': 'Payment records for this invoice.',
                        'properties': {
                            'paid_amount': {'$ref': '#/components/schemas/Money'},
                            'transactions': {
                                'type': 'array',
                                'items': {'type': 'object', 'additionalProperties': True},
                            },
                        },
                    },
                    'refunds': {
                        'type': 'object',
                        'description': 'Refund records for this invoice.',
                        'properties': {
                            'refund_amount': {'$ref': '#/components/schemas/Money'},
                            'transactions': {
                                'type': 'array',
                                'items': {'type': 'object', 'additionalProperties': True},
                            },
                        },
                    },
                    'links': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'href': {'type': 'string'},
                                'rel': {'type': 'string'},
                                'method': {'type': 'string'},
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'search_invoices',
                'x-airbyte-stream-name': 'search_invoices',
            },
        ),
    ],
    search_field_paths={
        'transactions': [
            'auction_info',
            'auction_info.auction_buyer_id',
            'auction_info.auction_closing_date',
            'auction_info.auction_item_site',
            'auction_info.auction_site',
            'cart_info',
            'cart_info.item_details',
            'cart_info.item_details[]',
            'incentive_info',
            'incentive_info.incentive_details',
            'incentive_info.incentive_details[]',
            'payer_info',
            'payer_info.account_id',
            'payer_info.address_status',
            'payer_info.country_code',
            'payer_info.email_address',
            'payer_info.payer_name',
            'payer_info.payer_name.alternate_full_name',
            'payer_info.payer_name.given_name',
            'payer_info.payer_name.surname',
            'payer_info.payer_status',
            'shipping_info',
            'shipping_info.address',
            'shipping_info.address.city',
            'shipping_info.address.country_code',
            'shipping_info.address.line1',
            'shipping_info.address.line2',
            'shipping_info.address.postal_code',
            'shipping_info.name',
            'store_info',
            'store_info.store_id',
            'store_info.terminal_id',
            'transaction_id',
            'transaction_info',
            'transaction_info.custom_field',
            'transaction_info.fee_amount',
            'transaction_info.fee_amount.currency_code',
            'transaction_info.fee_amount.value',
            'transaction_info.insurance_amount',
            'transaction_info.insurance_amount.currency_code',
            'transaction_info.insurance_amount.value',
            'transaction_info.invoice_id',
            'transaction_info.paypal_account_id',
            'transaction_info.paypal_reference_id',
            'transaction_info.paypal_reference_id_type',
            'transaction_info.protection_eligibility',
            'transaction_info.shipping_amount',
            'transaction_info.shipping_amount.currency_code',
            'transaction_info.shipping_amount.value',
            'transaction_info.shipping_discount_amount',
            'transaction_info.shipping_discount_amount.currency_code',
            'transaction_info.shipping_discount_amount.value',
            'transaction_info.transaction_amount',
            'transaction_info.transaction_amount.currency_code',
            'transaction_info.transaction_amount.value',
            'transaction_info.transaction_event_code',
            'transaction_info.transaction_id',
            'transaction_info.transaction_initiation_date',
            'transaction_info.transaction_note',
            'transaction_info.transaction_status',
            'transaction_info.transaction_subject',
            'transaction_info.transaction_updated_date',
            'transaction_initiation_date',
            'transaction_updated_date',
        ],
        'balances': [
            'account_id',
            'as_of_time',
            'balances',
            'balances[]',
            'last_refresh_time',
        ],
        'list_products': [
            'create_time',
            'description',
            'id',
            'links',
            'links[]',
            'name',
        ],
        'show_product_details': [
            'category',
            'create_time',
            'description',
            'home_url',
            'id',
            'image_url',
            'links',
            'links[]',
            'name',
            'type',
            'update_time',
        ],
        'list_disputes': [
            'create_time',
            'dispute_amount',
            'dispute_amount.currency_code',
            'dispute_amount.value',
            'dispute_channel',
            'dispute_id',
            'dispute_life_cycle_stage',
            'dispute_state',
            'disputed_transactions',
            'disputed_transactions[]',
            'links',
            'links[]',
            'outcome',
            'reason',
            'status',
            'update_time',
            'updated_time_cut',
        ],
        'search_invoices': [
            'additional_recipients',
            'additional_recipients[]',
            'amount',
            'amount.breakdown',
            'amount.currency_code',
            'amount.value',
            'configuration',
            'detail',
            'due_amount',
            'due_amount.currency_code',
            'due_amount.value',
            'gratuity',
            'gratuity.currency_code',
            'gratuity.value',
            'id',
            'invoicer',
            'last_update_time',
            'links',
            'links[]',
            'payments',
            'primary_recipients',
            'primary_recipients[]',
            'refunds',
            'status',
        ],
        'list_payments': [
            'cart',
            'create_time',
            'id',
            'intent',
            'links',
            'links[]',
            'payer',
            'payer.payer_info',
            'payer.payer_info.country_code',
            'payer.payer_info.email',
            'payer.payer_info.first_name',
            'payer.payer_info.last_name',
            'payer.payer_info.payer_id',
            'payer.payment_method',
            'payer.status',
            'state',
            'transactions',
            'transactions[]',
            'update_time',
        ],
    },
)