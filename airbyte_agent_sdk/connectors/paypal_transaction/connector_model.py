"""
Connector model for paypal-transaction.

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

PaypalTransactionConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('d913b0f2-cc51-4e55-a44c-8ba1697b9239'),
    name='paypal-transaction',
    version='1.0.3',
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
        user_config_spec=AuthConfigSpec(
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
                        'x-airbyte-ai-hints': {
                            'summary': 'PayPal account balances across currencies',
                            'when_to_use': 'Questions about account balance or available funds',
                            'trigger_phrases': ['paypal balance', 'account balance', 'available funds'],
                            'freshness': 'live',
                            'example_questions': ['What is my PayPal balance?'],
                            'search_strategy': 'Retrieve current balances',
                        },
                    },
                    no_pagination='The PayPal /v1/reporting/balances endpoint returns the full list of account balances across currencies in a single response; no pagination parameters are exposed.',
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
                'x-airbyte-ai-hints': {
                    'summary': 'PayPal account balances across currencies',
                    'when_to_use': 'Questions about account balance or available funds',
                    'trigger_phrases': ['paypal balance', 'account balance', 'available funds'],
                    'freshness': 'live',
                    'example_questions': ['What is my PayPal balance?'],
                    'search_strategy': 'Retrieve current balances',
                },
            },
            ai_hints={
                'summary': 'PayPal account balances across currencies',
                'when_to_use': 'Questions about account balance or available funds',
                'trigger_phrases': ['paypal balance', 'account balance', 'available funds'],
                'freshness': 'live',
                'example_questions': ['What is my PayPal balance?'],
                'search_strategy': 'Retrieve current balances',
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
                        'start_date': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-01-01T00:00:00Z',
                        },
                        'end_date': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-01-31T00:00:00Z',
                        },
                        'transaction_id': {'type': 'string', 'required': False},
                        'transaction_type': {'type': 'string', 'required': False},
                        'transaction_status': {
                            'type': 'string',
                            'required': False,
                            'enum': [
                                'D',
                                'P',
                                'S',
                                'V',
                            ],
                        },
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
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                            'minimum': 1,
                        },
                        'balance_affecting_records_only': {
                            'type': 'string',
                            'required': False,
                            'default': 'Y',
                            'enum': ['Y', 'N'],
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'PayPal transaction records with amount, type, and status',
                                        'when_to_use': 'Questions about payment transactions or transaction history',
                                        'trigger_phrases': ['paypal transaction', 'payment history', 'transaction'],
                                        'freshness': 'live',
                                        'example_questions': ['Show recent PayPal transactions'],
                                        'search_strategy': 'Filter by date range, type, or status',
                                    },
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
                'x-airbyte-ai-hints': {
                    'summary': 'PayPal transaction records with amount, type, and status',
                    'when_to_use': 'Questions about payment transactions or transaction history',
                    'trigger_phrases': ['paypal transaction', 'payment history', 'transaction'],
                    'freshness': 'live',
                    'example_questions': ['Show recent PayPal transactions'],
                    'search_strategy': 'Filter by date range, type, or status',
                },
            },
            ai_hints={
                'summary': 'PayPal transaction records with amount, type, and status',
                'when_to_use': 'Questions about payment transactions or transaction history',
                'trigger_phrases': ['paypal transaction', 'payment history', 'transaction'],
                'freshness': 'live',
                'example_questions': ['Show recent PayPal transactions'],
                'search_strategy': 'Filter by date range, type, or status',
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
                            'minimum': 1,
                            'maximum': 20,
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'PayPal payment records for orders and purchases',
                                        'when_to_use': 'Questions about payments received or payment details',
                                        'trigger_phrases': ['paypal payment', 'payment received', 'payment details'],
                                        'freshness': 'live',
                                        'example_questions': ['Show recent payments'],
                                        'search_strategy': 'Filter by date range',
                                    },
                                },
                            },
                            'count': {'type': 'integer', 'description': 'Number of payments returned.'},
                            'next_id': {'type': 'string', 'description': 'Next payment ID for pagination.'},
                        },
                    },
                    record_extractor='$.payments',
                    meta_extractor={'next_id': '$.next_id'},
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
                'x-airbyte-ai-hints': {
                    'summary': 'PayPal payment records for orders and purchases',
                    'when_to_use': 'Questions about payments received or payment details',
                    'trigger_phrases': ['paypal payment', 'payment received', 'payment details'],
                    'freshness': 'live',
                    'example_questions': ['Show recent payments'],
                    'search_strategy': 'Filter by date range',
                },
            },
            ai_hints={
                'summary': 'PayPal payment records for orders and purchases',
                'when_to_use': 'Questions about payments received or payment details',
                'trigger_phrases': ['paypal payment', 'payment received', 'payment details'],
                'freshness': 'live',
                'example_questions': ['Show recent payments'],
                'search_strategy': 'Filter by date range',
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
                            'minimum': 1,
                            'maximum': 50,
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'PayPal disputes and chargebacks from buyers',
                                        'when_to_use': 'Questions about payment disputes, chargebacks, or claims',
                                        'trigger_phrases': ['paypal dispute', 'chargeback', 'buyer claim'],
                                        'freshness': 'live',
                                        'example_questions': ['Are there any open disputes?'],
                                        'search_strategy': 'Filter by status or date',
                                    },
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
                    meta_extractor={'next': '$.links'},
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
                'x-airbyte-ai-hints': {
                    'summary': 'PayPal disputes and chargebacks from buyers',
                    'when_to_use': 'Questions about payment disputes, chargebacks, or claims',
                    'trigger_phrases': ['paypal dispute', 'chargeback', 'buyer claim'],
                    'freshness': 'live',
                    'example_questions': ['Are there any open disputes?'],
                    'search_strategy': 'Filter by status or date',
                },
            },
            ai_hints={
                'summary': 'PayPal disputes and chargebacks from buyers',
                'when_to_use': 'Questions about payment disputes, chargebacks, or claims',
                'trigger_phrases': ['paypal dispute', 'chargeback', 'buyer claim'],
                'freshness': 'live',
                'example_questions': ['Are there any open disputes?'],
                'search_strategy': 'Filter by status or date',
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
                            'minimum': 1,
                            'maximum': 20,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                            'minimum': 1,
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Products cataloged in PayPal for billing',
                                        'when_to_use': 'Questions about product catalog or available products',
                                        'trigger_phrases': ['paypal product', 'product catalog'],
                                        'freshness': 'live',
                                        'example_questions': ['What products are in PayPal?'],
                                        'search_strategy': 'List all products',
                                    },
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
                    meta_extractor={'next': '$.links'},
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
                'x-airbyte-ai-hints': {
                    'summary': 'Products cataloged in PayPal for billing',
                    'when_to_use': 'Questions about product catalog or available products',
                    'trigger_phrases': ['paypal product', 'product catalog'],
                    'freshness': 'live',
                    'example_questions': ['What products are in PayPal?'],
                    'search_strategy': 'List all products',
                },
            },
            ai_hints={
                'summary': 'Products cataloged in PayPal for billing',
                'when_to_use': 'Questions about product catalog or available products',
                'trigger_phrases': ['paypal product', 'product catalog'],
                'freshness': 'live',
                'example_questions': ['What products are in PayPal?'],
                'search_strategy': 'List all products',
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Detailed information about a specific PayPal product',
                            'when_to_use': 'Looking up details for a specific product',
                            'trigger_phrases': ['product details', 'product info'],
                            'freshness': 'live',
                            'example_questions': ['Show details for a PayPal product'],
                            'search_strategy': 'Retrieve by product ID',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Detailed information about a specific PayPal product',
                    'when_to_use': 'Looking up details for a specific product',
                    'trigger_phrases': ['product details', 'product info'],
                    'freshness': 'live',
                    'example_questions': ['Show details for a PayPal product'],
                    'search_strategy': 'Retrieve by product ID',
                },
            },
            ai_hints={
                'summary': 'Detailed information about a specific PayPal product',
                'when_to_use': 'Looking up details for a specific product',
                'trigger_phrases': ['product details', 'product info'],
                'freshness': 'live',
                'example_questions': ['Show details for a PayPal product'],
                'search_strategy': 'Retrieve by product ID',
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
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                            'minimum': 1,
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
                                    'x-airbyte-ai-hints': {
                                        'summary': 'PayPal invoices with line items and payment status',
                                        'when_to_use': 'Questions about PayPal invoices or billing',
                                        'trigger_phrases': ['paypal invoice', 'invoice search', 'billing'],
                                        'freshness': 'live',
                                        'example_questions': ['Show PayPal invoices'],
                                        'search_strategy': 'Search by recipient, date, or status',
                                    },
                                },
                            },
                            'total_items': {'type': 'integer', 'description': 'Total number of matching invoices.'},
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
                    record_extractor='$.items',
                    meta_extractor={'next': '$.links'},
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
                'x-airbyte-ai-hints': {
                    'summary': 'PayPal invoices with line items and payment status',
                    'when_to_use': 'Questions about PayPal invoices or billing',
                    'trigger_phrases': ['paypal invoice', 'invoice search', 'billing'],
                    'freshness': 'live',
                    'example_questions': ['Show PayPal invoices'],
                    'search_strategy': 'Search by recipient, date, or status',
                },
            },
            ai_hints={
                'summary': 'PayPal invoices with line items and payment status',
                'when_to_use': 'Questions about PayPal invoices or billing',
                'trigger_phrases': ['paypal invoice', 'invoice search', 'billing'],
                'freshness': 'live',
                'example_questions': ['Show PayPal invoices'],
                'search_strategy': 'Search by recipient, date, or status',
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='transactions',
                suggested=True,
                x_airbyte_name='transactions',
                fields=[
                    CacheFieldConfig(
                        name='auction_info',
                        type=['null', 'object'],
                        description='Information related to an auction',
                        properties={
                            'auction_buyer_id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'auction_closing_date': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'auction_item_site': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'auction_site': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='cart_info',
                        type=['null', 'object'],
                        description='Details of items in the cart',
                        properties={
                            'item_details': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='incentive_info',
                        type=['null', 'object'],
                        description='Details of any incentives applied',
                        properties={
                            'incentive_details': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='payer_info',
                        type=['null', 'object'],
                        description='Information about the payer',
                        properties={
                            'account_id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'address_status': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'country_code': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'email_address': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'payer_name': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'alternate_full_name': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'given_name': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'surname': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'payer_status': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='shipping_info',
                        type=['null', 'object'],
                        description='Shipping information',
                        properties={
                            'address': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'city': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'country_code': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'line1': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'line2': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'postal_code': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='store_info',
                        type=['null', 'object'],
                        description='Information about the store',
                        properties={
                            'store_id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'terminal_id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='transaction_id',
                        type=['null', 'string'],
                        description='Unique ID of the transaction',
                    ),
                    CacheFieldConfig(
                        name='transaction_info',
                        type=['null', 'object'],
                        description='Detailed information about the transaction',
                        properties={
                            'custom_field': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'fee_amount': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'currency_code': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'value': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'insurance_amount': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'currency_code': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'value': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'invoice_id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'paypal_account_id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'paypal_reference_id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'paypal_reference_id_type': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'protection_eligibility': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'shipping_amount': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'currency_code': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'value': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'shipping_discount_amount': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'currency_code': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'value': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'transaction_amount': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'currency_code': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'value': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'transaction_event_code': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'transaction_id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'transaction_initiation_date': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'transaction_note': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'transaction_status': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'transaction_subject': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'transaction_updated_date': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='transaction_initiation_date',
                        type=['null', 'string'],
                        description='Date and time when the transaction was initiated',
                    ),
                    CacheFieldConfig(
                        name='transaction_updated_date',
                        type=['null', 'string'],
                        description='Date and time when the transaction was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='balances',
                suggested=True,
                x_airbyte_name='balances',
                fields=[
                    CacheFieldConfig(
                        name='account_id',
                        type=['null', 'string'],
                        description='The unique identifier of the account.',
                    ),
                    CacheFieldConfig(
                        name='as_of_time',
                        type=['null', 'string'],
                        description='The timestamp when the balances data was reported.',
                    ),
                    CacheFieldConfig(
                        name='balances',
                        type=['null', 'array'],
                        description='Object containing information about the account balances.',
                    ),
                    CacheFieldConfig(
                        name='last_refresh_time',
                        type=['null', 'string'],
                        description='The timestamp when the balances data was last refreshed.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='list_products',
                suggested=True,
                x_airbyte_name='list_products',
                fields=[
                    CacheFieldConfig(
                        name='create_time',
                        type=['null', 'string'],
                        description='The time when the product was created',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Detailed information or features of the product',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the product',
                    ),
                    CacheFieldConfig(
                        name='links',
                        type=['null', 'array'],
                        description='List of links related to the fetched products.',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='The name or title of the product',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='show_product_details',
                x_airbyte_name='show_product_details',
                fields=[
                    CacheFieldConfig(
                        name='category',
                        type=['null', 'string'],
                        description='The category to which the product belongs',
                    ),
                    CacheFieldConfig(
                        name='create_time',
                        type=['null', 'string'],
                        description='The date and time when the product was created',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='The detailed description of the product',
                    ),
                    CacheFieldConfig(
                        name='home_url',
                        type=['null', 'string'],
                        description='The URL for the home page of the product',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='The unique identifier for the product',
                    ),
                    CacheFieldConfig(
                        name='image_url',
                        type=['null', 'string'],
                        description='The URL to the image representing the product',
                    ),
                    CacheFieldConfig(
                        name='links',
                        type=['null', 'array'],
                        description='Contains links related to the product details.',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='The name of the product',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='The type or category of the product',
                    ),
                    CacheFieldConfig(
                        name='update_time',
                        type=['null', 'string'],
                        description='The date and time when the product was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='list_disputes',
                suggested=True,
                x_airbyte_name='list_disputes',
                fields=[
                    CacheFieldConfig(
                        name='create_time',
                        type=['null', 'string'],
                        description='The timestamp when the dispute was created.',
                    ),
                    CacheFieldConfig(
                        name='dispute_amount',
                        type=['null', 'object'],
                        description='Details about the disputed amount.',
                        properties={
                            'currency_code': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'value': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='dispute_channel',
                        type=['null', 'string'],
                        description='The channel through which the dispute was initiated.',
                    ),
                    CacheFieldConfig(
                        name='dispute_id',
                        type=['null', 'string'],
                        description='The unique identifier for the dispute.',
                    ),
                    CacheFieldConfig(
                        name='dispute_life_cycle_stage',
                        type=['null', 'string'],
                        description='The stage in the life cycle of the dispute.',
                    ),
                    CacheFieldConfig(
                        name='dispute_state',
                        type=['null', 'string'],
                        description='The current state of the dispute.',
                    ),
                    CacheFieldConfig(
                        name='disputed_transactions',
                        type=['null', 'array'],
                        description='Details of transactions involved in the dispute.',
                    ),
                    CacheFieldConfig(
                        name='links',
                        type=['null', 'array'],
                        description='Links related to the dispute.',
                    ),
                    CacheFieldConfig(
                        name='outcome',
                        type=['null', 'string'],
                        description='The outcome of the dispute resolution.',
                    ),
                    CacheFieldConfig(
                        name='reason',
                        type=['null', 'string'],
                        description='The reason for the dispute.',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='The current status of the dispute.',
                    ),
                    CacheFieldConfig(
                        name='update_time',
                        type=['null', 'string'],
                        description='The timestamp when the dispute was last updated.',
                    ),
                    CacheFieldConfig(
                        name='updated_time_cut',
                        type=['null', 'string'],
                        description='The cut-off timestamp for the last update.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='search_invoices',
                suggested=True,
                x_airbyte_name='search_invoices',
                fields=[
                    CacheFieldConfig(
                        name='additional_recipients',
                        type=['null', 'array'],
                        description='List of additional recipients associated with the invoice',
                    ),
                    CacheFieldConfig(
                        name='amount',
                        type=['null', 'object'],
                        description='Detailed breakdown of the invoice amount',
                        properties={
                            'breakdown': CacheFieldProperty(
                                type=['null', 'object'],
                            ),
                            'currency_code': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'value': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='configuration',
                        type=['null', 'object'],
                        description='Configuration settings related to the invoice',
                    ),
                    CacheFieldConfig(
                        name='detail',
                        type=['null', 'object'],
                        description='Detailed information about the invoice',
                    ),
                    CacheFieldConfig(
                        name='due_amount',
                        type=['null', 'object'],
                        description='Due amount remaining to be paid for the invoice',
                        properties={
                            'currency_code': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'value': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='gratuity',
                        type=['null', 'object'],
                        description='Gratuity amount included in the invoice',
                        properties={
                            'currency_code': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'value': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier of the invoice',
                    ),
                    CacheFieldConfig(
                        name='invoicer',
                        type=['null', 'object'],
                        description='Information about the invoicer associated with the invoice',
                    ),
                    CacheFieldConfig(
                        name='last_update_time',
                        type=['null', 'string'],
                        description='Date and time of the last update made to the invoice',
                    ),
                    CacheFieldConfig(
                        name='links',
                        type=['null', 'array'],
                        description='Links associated with the invoice',
                    ),
                    CacheFieldConfig(
                        name='payments',
                        type=['null', 'object'],
                        description='Payment transactions associated with the invoice',
                    ),
                    CacheFieldConfig(
                        name='primary_recipients',
                        type=['null', 'array'],
                        description='Primary recipients associated with the invoice',
                    ),
                    CacheFieldConfig(
                        name='refunds',
                        type=['null', 'object'],
                        description='Refund transactions associated with the invoice',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Current status of the invoice',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='list_payments',
                suggested=True,
                x_airbyte_name='list_payments',
                fields=[
                    CacheFieldConfig(
                        name='cart',
                        type=['null', 'string'],
                        description='Details of the cart associated with the payment.',
                    ),
                    CacheFieldConfig(
                        name='create_time',
                        type=['null', 'string'],
                        description='The date and time when the payment was created.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the payment.',
                    ),
                    CacheFieldConfig(
                        name='intent',
                        type=['null', 'string'],
                        description='The intention or purpose behind the payment.',
                    ),
                    CacheFieldConfig(
                        name='links',
                        type=['null', 'array'],
                        description='Collection of links related to the payment',
                    ),
                    CacheFieldConfig(
                        name='payer',
                        type=['null', 'object'],
                        description='Details of the payer who made the payment',
                        properties={
                            'payer_info': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'country_code': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'email': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'first_name': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'last_name': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'payer_id': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'payment_method': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'status': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='state',
                        type=['null', 'string'],
                        description='The state of the payment.',
                    ),
                    CacheFieldConfig(
                        name='transactions',
                        type=['null', 'array'],
                        description='List of transactions associated with the payment',
                    ),
                    CacheFieldConfig(
                        name='update_time',
                        type=['null', 'string'],
                        description='The date and time when the payment was last updated.',
                    ),
                ],
            ),
        ],
        disable_compaction=True,
    ),
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
    example_questions=ExampleQuestions(
        direct=[
            'List all balances for my PayPal account',
            'Show recent transactions from the last 7 days',
            'List all catalog products',
            'Show details for a specific product',
            'List all disputes',
            'Show recent payments',
        ],
        context_store_search=[
            'What transactions had the highest amounts last month?',
            'Find all declined transactions',
            'Show disputes grouped by status',
            'What is the total balance across all currencies?',
        ],
        search=[
            'What transactions had the highest amounts last month?',
            'Find all declined transactions',
            'Show disputes grouped by status',
            'What is the total balance across all currencies?',
        ],
        unsupported=[
            'Create a new payment',
            'Refund a transaction',
            'Delete a dispute',
            'Update product details',
        ],
    ),
)