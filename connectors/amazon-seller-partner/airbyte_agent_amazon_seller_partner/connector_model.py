"""
Connector model for amazon-seller-partner.

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

AmazonSellerPartnerConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('e55879a8-0ef8-4557-abcf-ab34c53ec460'),
    name='amazon-seller-partner',
    version='1.0.2',
    base_url='https://sellingpartnerapi-{region}.amazon.com',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://api.amazon.com/auth/o2/token',
            'auth_style': 'body',
            'body_format': 'form',
            'additional_headers': {'x-amz-access-token': '{{ access_token }}'},
        },
        user_config_spec=AirbyteAuthConfig(
            title='Login with Amazon OAuth 2.0',
            type='object',
            required=['lwa_app_id', 'lwa_client_secret', 'refresh_token'],
            properties={
                'lwa_app_id': AuthConfigFieldSpec(
                    title='LWA Client ID',
                    description='Your Login with Amazon Client ID.',
                ),
                'lwa_client_secret': AuthConfigFieldSpec(
                    title='LWA Client Secret',
                    description='Your Login with Amazon Client Secret.',
                ),
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='The Refresh Token obtained via the OAuth authorization flow.',
                ),
                'access_token': AuthConfigFieldSpec(
                    title='Access Token',
                    description='Access token (optional if refresh_token is provided).',
                ),
            },
            auth_mapping={
                'client_id': '${lwa_app_id}',
                'client_secret': '${lwa_client_secret}',
                'refresh_token': '${refresh_token}',
                'access_token': '${access_token}',
            },
            replication_auth_key_mapping={
                'lwa_app_id': 'lwa_app_id',
                'lwa_client_secret': 'lwa_client_secret',
                'refresh_token': 'refresh_token',
            },
            additional_headers={'x-amz-access-token': '{{ access_token }}'},
            replication_auth_key_constants={'auth_type': 'oauth2.0'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='orders',
            stream_name='Orders',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/orders/v0/orders',
                    action=Action.LIST,
                    description='Returns a list of orders based on the specified parameters.',
                    query_params=[
                        'MarketplaceIds',
                        'CreatedAfter',
                        'CreatedBefore',
                        'LastUpdatedAfter',
                        'LastUpdatedBefore',
                        'OrderStatuses',
                        'MaxResultsPerPage',
                        'NextToken',
                    ],
                    query_params_schema={
                        'MarketplaceIds': {
                            'type': 'string',
                            'required': True,
                            'default': 'ATVPDKIKX0DER',
                        },
                        'CreatedAfter': {'type': 'string', 'required': False},
                        'CreatedBefore': {'type': 'string', 'required': False},
                        'LastUpdatedAfter': {'type': 'string', 'required': False},
                        'LastUpdatedBefore': {'type': 'string', 'required': False},
                        'OrderStatuses': {'type': 'string', 'required': False},
                        'MaxResultsPerPage': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'NextToken': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of orders',
                        'properties': {
                            'payload': {
                                'type': 'object',
                                'properties': {
                                    'Orders': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Amazon order object',
                                            'properties': {
                                                'AmazonOrderId': {'type': 'string', 'description': "Amazon's unique identifier for the order"},
                                                'SellerOrderId': {'type': 'string', 'description': 'Seller-defined order identifier'},
                                                'PurchaseDate': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Date and time when the order was created',
                                                },
                                                'LastUpdateDate': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Date and time when the order was last updated',
                                                },
                                                'OrderStatus': {
                                                    'type': 'string',
                                                    'description': 'Current status of the order',
                                                    'enum': [
                                                        'Pending',
                                                        'Unshipped',
                                                        'PartiallyShipped',
                                                        'Shipped',
                                                        'Canceled',
                                                        'Unfulfillable',
                                                        'InvoiceUnconfirmed',
                                                        'PendingAvailability',
                                                    ],
                                                },
                                                'FulfillmentChannel': {'type': 'string', 'description': 'Fulfillment channel (AFN for FBA, MFN for seller-fulfilled)'},
                                                'SalesChannel': {'type': 'string', 'description': 'Sales channel (e.g. Amazon.com)'},
                                                'ShipServiceLevel': {'type': 'string', 'description': 'Shipping service level of the order'},
                                                'OrderTotal': {
                                                    'type': 'object',
                                                    'description': 'Total amount of the order',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'NumberOfItemsShipped': {'type': 'integer', 'description': 'Number of items shipped'},
                                                'NumberOfItemsUnshipped': {'type': 'integer', 'description': 'Number of items not yet shipped'},
                                                'PaymentMethod': {'type': 'string', 'description': 'Payment method for the order'},
                                                'PaymentMethodDetails': {
                                                    'type': 'array',
                                                    'description': 'Payment method details',
                                                    'items': {'type': 'string'},
                                                },
                                                'MarketplaceId': {'type': 'string', 'description': 'Identifier for the marketplace'},
                                                'ShipmentServiceLevelCategory': {'type': 'string', 'description': 'Shipment service level category'},
                                                'OrderType': {'type': 'string', 'description': 'Type of order'},
                                                'EarliestShipDate': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Earliest ship date',
                                                },
                                                'LatestShipDate': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Latest ship date',
                                                },
                                                'EarliestDeliveryDate': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Earliest delivery date',
                                                },
                                                'LatestDeliveryDate': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Latest delivery date',
                                                },
                                                'IsBusinessOrder': {'type': 'boolean', 'description': 'Whether this is a business order'},
                                                'IsPrime': {'type': 'boolean', 'description': 'Whether this is a Prime order'},
                                                'IsGlobalExpressEnabled': {'type': 'boolean', 'description': 'Whether global express is enabled'},
                                                'IsPremiumOrder': {'type': 'boolean', 'description': 'Whether this is a premium order'},
                                                'IsSoldByAB': {'type': 'boolean', 'description': 'Whether sold by Amazon Business'},
                                                'IsReplacementOrder': {'type': 'string', 'description': 'Whether this is a replacement order'},
                                                'IsISPU': {'type': 'boolean', 'description': 'Whether this is an In-Store Pickup order'},
                                                'IsAccessPointOrder': {'type': 'boolean', 'description': 'Whether this is an access point order'},
                                                'HasRegulatedItems': {'type': 'boolean', 'description': 'Whether the order contains regulated items'},
                                                'ShippingAddress': {
                                                    'type': 'object',
                                                    'description': 'Shipping address for the order',
                                                    'properties': {
                                                        'City': {'type': 'string'},
                                                        'StateOrRegion': {'type': 'string'},
                                                        'PostalCode': {'type': 'string'},
                                                        'CountryCode': {'type': 'string'},
                                                    },
                                                },
                                                'DefaultShipFromLocationAddress': {
                                                    'type': 'object',
                                                    'description': 'Default ship-from address',
                                                    'properties': {
                                                        'Name': {'type': 'string'},
                                                        'AddressLine1': {'type': 'string'},
                                                        'City': {'type': 'string'},
                                                        'StateOrRegion': {'type': 'string'},
                                                        'PostalCode': {'type': 'string'},
                                                        'CountryCode': {'type': 'string'},
                                                    },
                                                },
                                                'AutomatedShippingSettings': {
                                                    'type': 'object',
                                                    'description': 'Automated shipping settings',
                                                    'properties': {
                                                        'HasAutomatedShippingSettings': {'type': 'boolean'},
                                                    },
                                                },
                                                'BuyerInfo': {'type': 'object', 'description': 'Buyer information'},
                                            },
                                            'required': ['AmazonOrderId'],
                                            'x-airbyte-entity-name': 'orders',
                                            'x-airbyte-stream-name': 'Orders',
                                        },
                                    },
                                    'NextToken': {'type': 'string', 'description': 'Pagination token for next page'},
                                },
                            },
                        },
                    },
                    record_extractor='$.payload.Orders',
                    meta_extractor={'next_token': '$.payload.NextToken'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/orders/v0/orders/{orderId}',
                    action=Action.GET,
                    description='Returns the order indicated by the specified order ID.',
                    path_params=['orderId'],
                    path_params_schema={
                        'orderId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Amazon order object',
                        'properties': {
                            'AmazonOrderId': {'type': 'string', 'description': "Amazon's unique identifier for the order"},
                            'SellerOrderId': {'type': 'string', 'description': 'Seller-defined order identifier'},
                            'PurchaseDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Date and time when the order was created',
                            },
                            'LastUpdateDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Date and time when the order was last updated',
                            },
                            'OrderStatus': {
                                'type': 'string',
                                'description': 'Current status of the order',
                                'enum': [
                                    'Pending',
                                    'Unshipped',
                                    'PartiallyShipped',
                                    'Shipped',
                                    'Canceled',
                                    'Unfulfillable',
                                    'InvoiceUnconfirmed',
                                    'PendingAvailability',
                                ],
                            },
                            'FulfillmentChannel': {'type': 'string', 'description': 'Fulfillment channel (AFN for FBA, MFN for seller-fulfilled)'},
                            'SalesChannel': {'type': 'string', 'description': 'Sales channel (e.g. Amazon.com)'},
                            'ShipServiceLevel': {'type': 'string', 'description': 'Shipping service level of the order'},
                            'OrderTotal': {
                                'type': 'object',
                                'description': 'Total amount of the order',
                                'properties': {
                                    'CurrencyCode': {'type': 'string'},
                                    'Amount': {'type': 'string'},
                                },
                            },
                            'NumberOfItemsShipped': {'type': 'integer', 'description': 'Number of items shipped'},
                            'NumberOfItemsUnshipped': {'type': 'integer', 'description': 'Number of items not yet shipped'},
                            'PaymentMethod': {'type': 'string', 'description': 'Payment method for the order'},
                            'PaymentMethodDetails': {
                                'type': 'array',
                                'description': 'Payment method details',
                                'items': {'type': 'string'},
                            },
                            'MarketplaceId': {'type': 'string', 'description': 'Identifier for the marketplace'},
                            'ShipmentServiceLevelCategory': {'type': 'string', 'description': 'Shipment service level category'},
                            'OrderType': {'type': 'string', 'description': 'Type of order'},
                            'EarliestShipDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Earliest ship date',
                            },
                            'LatestShipDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Latest ship date',
                            },
                            'EarliestDeliveryDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Earliest delivery date',
                            },
                            'LatestDeliveryDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Latest delivery date',
                            },
                            'IsBusinessOrder': {'type': 'boolean', 'description': 'Whether this is a business order'},
                            'IsPrime': {'type': 'boolean', 'description': 'Whether this is a Prime order'},
                            'IsGlobalExpressEnabled': {'type': 'boolean', 'description': 'Whether global express is enabled'},
                            'IsPremiumOrder': {'type': 'boolean', 'description': 'Whether this is a premium order'},
                            'IsSoldByAB': {'type': 'boolean', 'description': 'Whether sold by Amazon Business'},
                            'IsReplacementOrder': {'type': 'string', 'description': 'Whether this is a replacement order'},
                            'IsISPU': {'type': 'boolean', 'description': 'Whether this is an In-Store Pickup order'},
                            'IsAccessPointOrder': {'type': 'boolean', 'description': 'Whether this is an access point order'},
                            'HasRegulatedItems': {'type': 'boolean', 'description': 'Whether the order contains regulated items'},
                            'ShippingAddress': {
                                'type': 'object',
                                'description': 'Shipping address for the order',
                                'properties': {
                                    'City': {'type': 'string'},
                                    'StateOrRegion': {'type': 'string'},
                                    'PostalCode': {'type': 'string'},
                                    'CountryCode': {'type': 'string'},
                                },
                            },
                            'DefaultShipFromLocationAddress': {
                                'type': 'object',
                                'description': 'Default ship-from address',
                                'properties': {
                                    'Name': {'type': 'string'},
                                    'AddressLine1': {'type': 'string'},
                                    'City': {'type': 'string'},
                                    'StateOrRegion': {'type': 'string'},
                                    'PostalCode': {'type': 'string'},
                                    'CountryCode': {'type': 'string'},
                                },
                            },
                            'AutomatedShippingSettings': {
                                'type': 'object',
                                'description': 'Automated shipping settings',
                                'properties': {
                                    'HasAutomatedShippingSettings': {'type': 'boolean'},
                                },
                            },
                            'BuyerInfo': {'type': 'object', 'description': 'Buyer information'},
                        },
                        'required': ['AmazonOrderId'],
                        'x-airbyte-entity-name': 'orders',
                        'x-airbyte-stream-name': 'Orders',
                    },
                    record_extractor='$.payload',
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Amazon order object',
                'properties': {
                    'AmazonOrderId': {'type': 'string', 'description': "Amazon's unique identifier for the order"},
                    'SellerOrderId': {'type': 'string', 'description': 'Seller-defined order identifier'},
                    'PurchaseDate': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Date and time when the order was created',
                    },
                    'LastUpdateDate': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Date and time when the order was last updated',
                    },
                    'OrderStatus': {
                        'type': 'string',
                        'description': 'Current status of the order',
                        'enum': [
                            'Pending',
                            'Unshipped',
                            'PartiallyShipped',
                            'Shipped',
                            'Canceled',
                            'Unfulfillable',
                            'InvoiceUnconfirmed',
                            'PendingAvailability',
                        ],
                    },
                    'FulfillmentChannel': {'type': 'string', 'description': 'Fulfillment channel (AFN for FBA, MFN for seller-fulfilled)'},
                    'SalesChannel': {'type': 'string', 'description': 'Sales channel (e.g. Amazon.com)'},
                    'ShipServiceLevel': {'type': 'string', 'description': 'Shipping service level of the order'},
                    'OrderTotal': {
                        'type': 'object',
                        'description': 'Total amount of the order',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'NumberOfItemsShipped': {'type': 'integer', 'description': 'Number of items shipped'},
                    'NumberOfItemsUnshipped': {'type': 'integer', 'description': 'Number of items not yet shipped'},
                    'PaymentMethod': {'type': 'string', 'description': 'Payment method for the order'},
                    'PaymentMethodDetails': {
                        'type': 'array',
                        'description': 'Payment method details',
                        'items': {'type': 'string'},
                    },
                    'MarketplaceId': {'type': 'string', 'description': 'Identifier for the marketplace'},
                    'ShipmentServiceLevelCategory': {'type': 'string', 'description': 'Shipment service level category'},
                    'OrderType': {'type': 'string', 'description': 'Type of order'},
                    'EarliestShipDate': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Earliest ship date',
                    },
                    'LatestShipDate': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Latest ship date',
                    },
                    'EarliestDeliveryDate': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Earliest delivery date',
                    },
                    'LatestDeliveryDate': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Latest delivery date',
                    },
                    'IsBusinessOrder': {'type': 'boolean', 'description': 'Whether this is a business order'},
                    'IsPrime': {'type': 'boolean', 'description': 'Whether this is a Prime order'},
                    'IsGlobalExpressEnabled': {'type': 'boolean', 'description': 'Whether global express is enabled'},
                    'IsPremiumOrder': {'type': 'boolean', 'description': 'Whether this is a premium order'},
                    'IsSoldByAB': {'type': 'boolean', 'description': 'Whether sold by Amazon Business'},
                    'IsReplacementOrder': {'type': 'string', 'description': 'Whether this is a replacement order'},
                    'IsISPU': {'type': 'boolean', 'description': 'Whether this is an In-Store Pickup order'},
                    'IsAccessPointOrder': {'type': 'boolean', 'description': 'Whether this is an access point order'},
                    'HasRegulatedItems': {'type': 'boolean', 'description': 'Whether the order contains regulated items'},
                    'ShippingAddress': {
                        'type': 'object',
                        'description': 'Shipping address for the order',
                        'properties': {
                            'City': {'type': 'string'},
                            'StateOrRegion': {'type': 'string'},
                            'PostalCode': {'type': 'string'},
                            'CountryCode': {'type': 'string'},
                        },
                    },
                    'DefaultShipFromLocationAddress': {
                        'type': 'object',
                        'description': 'Default ship-from address',
                        'properties': {
                            'Name': {'type': 'string'},
                            'AddressLine1': {'type': 'string'},
                            'City': {'type': 'string'},
                            'StateOrRegion': {'type': 'string'},
                            'PostalCode': {'type': 'string'},
                            'CountryCode': {'type': 'string'},
                        },
                    },
                    'AutomatedShippingSettings': {
                        'type': 'object',
                        'description': 'Automated shipping settings',
                        'properties': {
                            'HasAutomatedShippingSettings': {'type': 'boolean'},
                        },
                    },
                    'BuyerInfo': {'type': 'object', 'description': 'Buyer information'},
                },
                'required': ['AmazonOrderId'],
                'x-airbyte-entity-name': 'orders',
                'x-airbyte-stream-name': 'Orders',
            },
        ),
        EntityDefinition(
            name='order_items',
            stream_name='OrderItems',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/orders/v0/orders/{orderId}/orderItems',
                    action=Action.LIST,
                    description='Returns detailed order item information for the order indicated by the specified order ID.',
                    query_params=['NextToken'],
                    query_params_schema={
                        'NextToken': {'type': 'string', 'required': False},
                    },
                    path_params=['orderId'],
                    path_params_schema={
                        'orderId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of order items',
                        'properties': {
                            'payload': {
                                'type': 'object',
                                'properties': {
                                    'AmazonOrderId': {'type': 'string'},
                                    'OrderItems': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Amazon order item object',
                                            'properties': {
                                                'OrderItemId': {'type': 'string', 'description': 'Unique identifier for the order item'},
                                                'AmazonOrderId': {'type': 'string', 'description': 'Amazon order identifier this item belongs to'},
                                                'ASIN': {'type': 'string', 'description': 'Amazon Standard Identification Number'},
                                                'SellerSKU': {'type': 'string', 'description': "Seller's SKU for the item"},
                                                'Title': {'type': 'string', 'description': 'Title of the item'},
                                                'QuantityOrdered': {'type': 'integer', 'description': 'Quantity ordered'},
                                                'QuantityShipped': {'type': 'integer', 'description': 'Quantity shipped'},
                                                'ItemPrice': {
                                                    'type': 'object',
                                                    'description': 'Item price',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'ItemTax': {
                                                    'type': 'object',
                                                    'description': 'Item tax',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'ShippingPrice': {
                                                    'type': 'object',
                                                    'description': 'Shipping price',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'ShippingTax': {
                                                    'type': 'object',
                                                    'description': 'Shipping tax',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'ShippingDiscount': {
                                                    'type': 'object',
                                                    'description': 'Shipping discount',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'ShippingDiscountTax': {
                                                    'type': 'object',
                                                    'description': 'Shipping discount tax',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'PromotionDiscount': {
                                                    'type': 'object',
                                                    'description': 'Promotion discount',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'PromotionDiscountTax': {
                                                    'type': 'object',
                                                    'description': 'Promotion discount tax',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'PromotionIds': {
                                                    'type': 'array',
                                                    'description': 'Promotion identifiers',
                                                    'items': {'type': 'string'},
                                                },
                                                'CODFee': {
                                                    'type': 'object',
                                                    'description': 'Cash on delivery fee',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'CODFeeDiscount': {
                                                    'type': 'object',
                                                    'description': 'Cash on delivery fee discount',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'Amount': {'type': 'string'},
                                                    },
                                                },
                                                'IsGift': {'type': 'string', 'description': 'Whether the item is a gift'},
                                                'ConditionId': {'type': 'string', 'description': 'Condition of the item'},
                                                'ConditionSubtypeId': {'type': 'string', 'description': 'Condition subtype'},
                                                'ConditionNote': {'type': 'string', 'description': 'Note about the condition'},
                                                'IsTransparency': {'type': 'boolean', 'description': 'Whether Transparency codes are required'},
                                                'SerialNumberRequired': {'type': 'boolean', 'description': 'Whether serial number is required'},
                                                'IossNumber': {'type': 'string', 'description': 'Import One Stop Shop number'},
                                                'DeemedResellerCategory': {'type': 'string', 'description': 'Deemed reseller category (IOSS or UOSS)'},
                                                'StoreChainStoreId': {'type': 'string', 'description': 'Store chain store identifier'},
                                                'ProductInfo': {
                                                    'type': 'object',
                                                    'description': 'Product information',
                                                    'properties': {
                                                        'NumberOfItems': {'type': 'string'},
                                                    },
                                                },
                                                'BuyerInfo': {
                                                    'type': 'object',
                                                    'description': 'Buyer information for the item',
                                                    'properties': {
                                                        'BuyerCustomizedInfo': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'CustomizedURL': {'type': 'string'},
                                                            },
                                                        },
                                                        'GiftMessageText': {'type': 'string'},
                                                        'GiftWrapPrice': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'CurrencyCode': {'type': 'string'},
                                                                'Amount': {'type': 'string'},
                                                            },
                                                        },
                                                        'GiftWrapLevel': {'type': 'string'},
                                                    },
                                                },
                                                'BuyerRequestedCancel': {
                                                    'type': 'object',
                                                    'description': 'Buyer cancellation request information',
                                                    'properties': {
                                                        'IsBuyerRequestedCancel': {'type': 'string'},
                                                        'BuyerCancelReason': {'type': 'string'},
                                                    },
                                                },
                                                'PointsGranted': {
                                                    'type': 'object',
                                                    'description': 'Points granted for the purchase',
                                                    'properties': {
                                                        'PointsNumber': {'type': 'integer'},
                                                        'PointsMonetaryValue': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'CurrencyCode': {'type': 'string'},
                                                                'Amount': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'TaxCollection': {
                                                    'type': 'object',
                                                    'description': 'Tax collection information',
                                                    'properties': {
                                                        'Model': {'type': 'string'},
                                                        'ResponsibleParty': {'type': 'string'},
                                                    },
                                                },
                                                'PriceDesignation': {'type': 'string', 'description': 'Price designation'},
                                            },
                                            'required': ['OrderItemId'],
                                            'x-airbyte-entity-name': 'order_items',
                                            'x-airbyte-stream-name': 'OrderItems',
                                        },
                                    },
                                    'NextToken': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.payload.OrderItems',
                    meta_extractor={'next_token': '$.payload.NextToken'},
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Amazon order item object',
                'properties': {
                    'OrderItemId': {'type': 'string', 'description': 'Unique identifier for the order item'},
                    'AmazonOrderId': {'type': 'string', 'description': 'Amazon order identifier this item belongs to'},
                    'ASIN': {'type': 'string', 'description': 'Amazon Standard Identification Number'},
                    'SellerSKU': {'type': 'string', 'description': "Seller's SKU for the item"},
                    'Title': {'type': 'string', 'description': 'Title of the item'},
                    'QuantityOrdered': {'type': 'integer', 'description': 'Quantity ordered'},
                    'QuantityShipped': {'type': 'integer', 'description': 'Quantity shipped'},
                    'ItemPrice': {
                        'type': 'object',
                        'description': 'Item price',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'ItemTax': {
                        'type': 'object',
                        'description': 'Item tax',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'ShippingPrice': {
                        'type': 'object',
                        'description': 'Shipping price',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'ShippingTax': {
                        'type': 'object',
                        'description': 'Shipping tax',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'ShippingDiscount': {
                        'type': 'object',
                        'description': 'Shipping discount',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'ShippingDiscountTax': {
                        'type': 'object',
                        'description': 'Shipping discount tax',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'PromotionDiscount': {
                        'type': 'object',
                        'description': 'Promotion discount',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'PromotionDiscountTax': {
                        'type': 'object',
                        'description': 'Promotion discount tax',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'PromotionIds': {
                        'type': 'array',
                        'description': 'Promotion identifiers',
                        'items': {'type': 'string'},
                    },
                    'CODFee': {
                        'type': 'object',
                        'description': 'Cash on delivery fee',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'CODFeeDiscount': {
                        'type': 'object',
                        'description': 'Cash on delivery fee discount',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'Amount': {'type': 'string'},
                        },
                    },
                    'IsGift': {'type': 'string', 'description': 'Whether the item is a gift'},
                    'ConditionId': {'type': 'string', 'description': 'Condition of the item'},
                    'ConditionSubtypeId': {'type': 'string', 'description': 'Condition subtype'},
                    'ConditionNote': {'type': 'string', 'description': 'Note about the condition'},
                    'IsTransparency': {'type': 'boolean', 'description': 'Whether Transparency codes are required'},
                    'SerialNumberRequired': {'type': 'boolean', 'description': 'Whether serial number is required'},
                    'IossNumber': {'type': 'string', 'description': 'Import One Stop Shop number'},
                    'DeemedResellerCategory': {'type': 'string', 'description': 'Deemed reseller category (IOSS or UOSS)'},
                    'StoreChainStoreId': {'type': 'string', 'description': 'Store chain store identifier'},
                    'ProductInfo': {
                        'type': 'object',
                        'description': 'Product information',
                        'properties': {
                            'NumberOfItems': {'type': 'string'},
                        },
                    },
                    'BuyerInfo': {
                        'type': 'object',
                        'description': 'Buyer information for the item',
                        'properties': {
                            'BuyerCustomizedInfo': {
                                'type': 'object',
                                'properties': {
                                    'CustomizedURL': {'type': 'string'},
                                },
                            },
                            'GiftMessageText': {'type': 'string'},
                            'GiftWrapPrice': {
                                'type': 'object',
                                'properties': {
                                    'CurrencyCode': {'type': 'string'},
                                    'Amount': {'type': 'string'},
                                },
                            },
                            'GiftWrapLevel': {'type': 'string'},
                        },
                    },
                    'BuyerRequestedCancel': {
                        'type': 'object',
                        'description': 'Buyer cancellation request information',
                        'properties': {
                            'IsBuyerRequestedCancel': {'type': 'string'},
                            'BuyerCancelReason': {'type': 'string'},
                        },
                    },
                    'PointsGranted': {
                        'type': 'object',
                        'description': 'Points granted for the purchase',
                        'properties': {
                            'PointsNumber': {'type': 'integer'},
                            'PointsMonetaryValue': {
                                'type': 'object',
                                'properties': {
                                    'CurrencyCode': {'type': 'string'},
                                    'Amount': {'type': 'string'},
                                },
                            },
                        },
                    },
                    'TaxCollection': {
                        'type': 'object',
                        'description': 'Tax collection information',
                        'properties': {
                            'Model': {'type': 'string'},
                            'ResponsibleParty': {'type': 'string'},
                        },
                    },
                    'PriceDesignation': {'type': 'string', 'description': 'Price designation'},
                },
                'required': ['OrderItemId'],
                'x-airbyte-entity-name': 'order_items',
                'x-airbyte-stream-name': 'OrderItems',
            },
        ),
        EntityDefinition(
            name='list_financial_event_groups',
            stream_name='ListFinancialEventGroups',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/finances/v0/financialEventGroups',
                    action=Action.LIST,
                    description='Returns financial event groups for a given date range.',
                    query_params=[
                        'FinancialEventGroupStartedAfter',
                        'FinancialEventGroupStartedBefore',
                        'MaxResultsPerPage',
                        'NextToken',
                    ],
                    query_params_schema={
                        'FinancialEventGroupStartedAfter': {'type': 'string', 'required': False},
                        'FinancialEventGroupStartedBefore': {'type': 'string', 'required': False},
                        'MaxResultsPerPage': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'NextToken': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of financial event groups',
                        'properties': {
                            'payload': {
                                'type': 'object',
                                'properties': {
                                    'FinancialEventGroupList': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'A financial event group',
                                            'properties': {
                                                'FinancialEventGroupId': {'type': 'string', 'description': 'Unique identifier for the financial event group'},
                                                'ProcessingStatus': {'type': 'string', 'description': 'Processing status (Open or Closed)'},
                                                'FundTransferStatus': {'type': 'string', 'description': 'Status of the fund transfer'},
                                                'OriginalTotal': {
                                                    'type': 'object',
                                                    'description': "Original total in seller's currency",
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'CurrencyAmount': {'type': 'number'},
                                                    },
                                                },
                                                'ConvertedTotal': {
                                                    'type': 'object',
                                                    'description': 'Converted total',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'CurrencyAmount': {'type': 'number'},
                                                    },
                                                },
                                                'FundTransferDate': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Date funds were transferred',
                                                },
                                                'TraceId': {'type': 'string', 'description': 'Bank trace identifier'},
                                                'AccountTail': {'type': 'string', 'description': 'Last digits of the account number'},
                                                'BeginningBalance': {
                                                    'type': 'object',
                                                    'description': 'Beginning balance',
                                                    'properties': {
                                                        'CurrencyCode': {'type': 'string'},
                                                        'CurrencyAmount': {'type': 'number'},
                                                    },
                                                },
                                                'FinancialEventGroupStart': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Start date of the event group',
                                                },
                                                'FinancialEventGroupEnd': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'End date of the event group',
                                                },
                                            },
                                            'required': ['FinancialEventGroupId'],
                                            'x-airbyte-entity-name': 'list_financial_event_groups',
                                            'x-airbyte-stream-name': 'ListFinancialEventGroups',
                                        },
                                    },
                                    'NextToken': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.payload.FinancialEventGroupList',
                    meta_extractor={'next_token': '$.payload.NextToken'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A financial event group',
                'properties': {
                    'FinancialEventGroupId': {'type': 'string', 'description': 'Unique identifier for the financial event group'},
                    'ProcessingStatus': {'type': 'string', 'description': 'Processing status (Open or Closed)'},
                    'FundTransferStatus': {'type': 'string', 'description': 'Status of the fund transfer'},
                    'OriginalTotal': {
                        'type': 'object',
                        'description': "Original total in seller's currency",
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'CurrencyAmount': {'type': 'number'},
                        },
                    },
                    'ConvertedTotal': {
                        'type': 'object',
                        'description': 'Converted total',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'CurrencyAmount': {'type': 'number'},
                        },
                    },
                    'FundTransferDate': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Date funds were transferred',
                    },
                    'TraceId': {'type': 'string', 'description': 'Bank trace identifier'},
                    'AccountTail': {'type': 'string', 'description': 'Last digits of the account number'},
                    'BeginningBalance': {
                        'type': 'object',
                        'description': 'Beginning balance',
                        'properties': {
                            'CurrencyCode': {'type': 'string'},
                            'CurrencyAmount': {'type': 'number'},
                        },
                    },
                    'FinancialEventGroupStart': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Start date of the event group',
                    },
                    'FinancialEventGroupEnd': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'End date of the event group',
                    },
                },
                'required': ['FinancialEventGroupId'],
                'x-airbyte-entity-name': 'list_financial_event_groups',
                'x-airbyte-stream-name': 'ListFinancialEventGroups',
            },
        ),
        EntityDefinition(
            name='list_financial_events',
            stream_name='ListFinancialEvents',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/finances/v0/financialEvents',
                    action=Action.LIST,
                    description='Returns financial events for a given date range.',
                    query_params=[
                        'PostedAfter',
                        'PostedBefore',
                        'MaxResultsPerPage',
                        'NextToken',
                    ],
                    query_params_schema={
                        'PostedAfter': {'type': 'string', 'required': False},
                        'PostedBefore': {'type': 'string', 'required': False},
                        'MaxResultsPerPage': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'NextToken': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response wrapper for financial events',
                        'properties': {
                            'payload': {
                                'type': 'object',
                                'properties': {
                                    'FinancialEvents': {
                                        'type': 'object',
                                        'description': 'A collection of financial events grouped by type',
                                        'properties': {
                                            'ShipmentEventList': {
                                                'type': 'array',
                                                'description': 'Shipment events',
                                                'items': {'type': 'object'},
                                            },
                                            'ShipmentSettleEventList': {
                                                'type': 'array',
                                                'description': 'Shipment settlement events',
                                                'items': {'type': 'object'},
                                            },
                                            'RefundEventList': {
                                                'type': 'array',
                                                'description': 'Refund events',
                                                'items': {'type': 'object'},
                                            },
                                            'GuaranteeClaimEventList': {
                                                'type': 'array',
                                                'description': 'Guarantee claim events',
                                                'items': {'type': 'object'},
                                            },
                                            'ChargebackEventList': {
                                                'type': 'array',
                                                'description': 'Chargeback events',
                                                'items': {'type': 'object'},
                                            },
                                            'ChargeRefundEventList': {
                                                'type': 'array',
                                                'description': 'Charge refund events',
                                                'items': {'type': 'object'},
                                            },
                                            'PayWithAmazonEventList': {
                                                'type': 'array',
                                                'description': 'Pay with Amazon events',
                                                'items': {'type': 'object'},
                                            },
                                            'ServiceProviderCreditEventList': {
                                                'type': 'array',
                                                'description': 'Service provider credit events',
                                                'items': {'type': 'object'},
                                            },
                                            'RetrochargeEventList': {
                                                'type': 'array',
                                                'description': 'Retrocharge events',
                                                'items': {'type': 'object'},
                                            },
                                            'RentalTransactionEventList': {
                                                'type': 'array',
                                                'description': 'Rental transaction events',
                                                'items': {'type': 'object'},
                                            },
                                            'ProductAdsPaymentEventList': {
                                                'type': 'array',
                                                'description': 'Product ads payment events',
                                                'items': {'type': 'object'},
                                            },
                                            'ServiceFeeEventList': {
                                                'type': 'array',
                                                'description': 'Service fee events',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'FeeList': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'FeeType': {'type': 'string'},
                                                                    'FeeAmount': {
                                                                        'type': 'object',
                                                                        'properties': {
                                                                            'CurrencyCode': {'type': 'string'},
                                                                            'CurrencyAmount': {'type': 'number'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'SellerDealPaymentEventList': {
                                                'type': 'array',
                                                'description': 'Seller deal payment events',
                                                'items': {'type': 'object'},
                                            },
                                            'DebtRecoveryEventList': {
                                                'type': 'array',
                                                'description': 'Debt recovery events',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'DebtRecoveryType': {'type': 'string'},
                                                        'RecoveryAmount': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'CurrencyCode': {'type': 'string'},
                                                                'CurrencyAmount': {'type': 'number'},
                                                            },
                                                        },
                                                        'DebtRecoveryItemList': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'RecoveryAmount': {
                                                                        'type': 'object',
                                                                        'properties': {
                                                                            'CurrencyCode': {'type': 'string'},
                                                                            'CurrencyAmount': {'type': 'number'},
                                                                        },
                                                                    },
                                                                    'OriginalAmount': {
                                                                        'type': 'object',
                                                                        'properties': {
                                                                            'CurrencyCode': {'type': 'string'},
                                                                            'CurrencyAmount': {'type': 'number'},
                                                                        },
                                                                    },
                                                                    'GroupBeginDate': {'type': 'string'},
                                                                    'GroupEndDate': {'type': 'string'},
                                                                },
                                                            },
                                                        },
                                                        'ChargeInstrumentList': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'Description': {'type': 'string'},
                                                                    'Tail': {'type': 'string'},
                                                                    'Amount': {
                                                                        'type': 'object',
                                                                        'properties': {
                                                                            'CurrencyCode': {'type': 'string'},
                                                                            'CurrencyAmount': {'type': 'number'},
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'LoanServicingEventList': {
                                                'type': 'array',
                                                'description': 'Loan servicing events',
                                                'items': {'type': 'object'},
                                            },
                                            'AdjustmentEventList': {
                                                'type': 'array',
                                                'description': 'Adjustment events',
                                                'items': {'type': 'object'},
                                            },
                                            'SAFETReimbursementEventList': {
                                                'type': 'array',
                                                'description': 'SAFET reimbursement events',
                                                'items': {'type': 'object'},
                                            },
                                            'SellerReviewEnrollmentPaymentEventList': {
                                                'type': 'array',
                                                'description': 'Seller review enrollment payment events',
                                                'items': {'type': 'object'},
                                            },
                                            'FBALiquidationEventList': {
                                                'type': 'array',
                                                'description': 'FBA liquidation events',
                                                'items': {'type': 'object'},
                                            },
                                            'CouponPaymentEventList': {
                                                'type': 'array',
                                                'description': 'Coupon payment events',
                                                'items': {'type': 'object'},
                                            },
                                            'ImagingServicesFeeEventList': {
                                                'type': 'array',
                                                'description': 'Imaging services fee events',
                                                'items': {'type': 'object'},
                                            },
                                            'NetworkComminglingTransactionEventList': {
                                                'type': 'array',
                                                'description': 'Network commingling transaction events',
                                                'items': {'type': 'object'},
                                            },
                                            'AffordabilityExpenseEventList': {
                                                'type': 'array',
                                                'description': 'Affordability expense events',
                                                'items': {'type': 'object'},
                                            },
                                            'AffordabilityExpenseReversalEventList': {
                                                'type': 'array',
                                                'description': 'Affordability expense reversal events',
                                                'items': {'type': 'object'},
                                            },
                                            'TrialShipmentEventList': {
                                                'type': 'array',
                                                'description': 'Trial shipment events',
                                                'items': {'type': 'object'},
                                            },
                                            'TDSReimbursementEventList': {
                                                'type': 'array',
                                                'description': 'TDS reimbursement events',
                                                'items': {'type': 'object'},
                                            },
                                            'TaxWithholdingEventList': {
                                                'type': 'array',
                                                'description': 'Tax withholding events',
                                                'items': {'type': 'object'},
                                            },
                                            'RemovalShipmentEventList': {
                                                'type': 'array',
                                                'description': 'Removal shipment events',
                                                'items': {'type': 'object'},
                                            },
                                            'RemovalShipmentAdjustmentEventList': {
                                                'type': 'array',
                                                'description': 'Removal shipment adjustment events',
                                                'items': {'type': 'object'},
                                            },
                                            'ValueAddedServiceChargeEventList': {
                                                'type': 'array',
                                                'description': 'Value-added service charge events',
                                                'items': {'type': 'object'},
                                            },
                                            'CapacityReservationBillingEventList': {
                                                'type': 'array',
                                                'description': 'Capacity reservation billing events',
                                                'items': {'type': 'object'},
                                            },
                                            'FailedAdhocDisbursementEventList': {
                                                'type': 'array',
                                                'description': 'Failed adhoc disbursement events',
                                                'items': {'type': 'object'},
                                            },
                                            'AdhocDisbursementEventList': {
                                                'type': 'array',
                                                'description': 'Adhoc disbursement events',
                                                'items': {'type': 'object'},
                                            },
                                            'PerformanceBondRefundEventList': {
                                                'type': 'array',
                                                'description': 'Performance bond refund events',
                                                'items': {'type': 'object'},
                                            },
                                            'EBTRefundReimbursementOnlyEventList': {
                                                'type': 'array',
                                                'description': 'EBT refund reimbursement only events',
                                                'items': {'type': 'object'},
                                            },
                                        },
                                        'x-airbyte-entity-name': 'list_financial_events',
                                        'x-airbyte-stream-name': 'ListFinancialEvents',
                                    },
                                    'NextToken': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.payload.FinancialEvents',
                    meta_extractor={'next_token': '$.payload.NextToken'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A collection of financial events grouped by type',
                'properties': {
                    'ShipmentEventList': {
                        'type': 'array',
                        'description': 'Shipment events',
                        'items': {'type': 'object'},
                    },
                    'ShipmentSettleEventList': {
                        'type': 'array',
                        'description': 'Shipment settlement events',
                        'items': {'type': 'object'},
                    },
                    'RefundEventList': {
                        'type': 'array',
                        'description': 'Refund events',
                        'items': {'type': 'object'},
                    },
                    'GuaranteeClaimEventList': {
                        'type': 'array',
                        'description': 'Guarantee claim events',
                        'items': {'type': 'object'},
                    },
                    'ChargebackEventList': {
                        'type': 'array',
                        'description': 'Chargeback events',
                        'items': {'type': 'object'},
                    },
                    'ChargeRefundEventList': {
                        'type': 'array',
                        'description': 'Charge refund events',
                        'items': {'type': 'object'},
                    },
                    'PayWithAmazonEventList': {
                        'type': 'array',
                        'description': 'Pay with Amazon events',
                        'items': {'type': 'object'},
                    },
                    'ServiceProviderCreditEventList': {
                        'type': 'array',
                        'description': 'Service provider credit events',
                        'items': {'type': 'object'},
                    },
                    'RetrochargeEventList': {
                        'type': 'array',
                        'description': 'Retrocharge events',
                        'items': {'type': 'object'},
                    },
                    'RentalTransactionEventList': {
                        'type': 'array',
                        'description': 'Rental transaction events',
                        'items': {'type': 'object'},
                    },
                    'ProductAdsPaymentEventList': {
                        'type': 'array',
                        'description': 'Product ads payment events',
                        'items': {'type': 'object'},
                    },
                    'ServiceFeeEventList': {
                        'type': 'array',
                        'description': 'Service fee events',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'FeeList': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'FeeType': {'type': 'string'},
                                            'FeeAmount': {
                                                'type': 'object',
                                                'properties': {
                                                    'CurrencyCode': {'type': 'string'},
                                                    'CurrencyAmount': {'type': 'number'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'SellerDealPaymentEventList': {
                        'type': 'array',
                        'description': 'Seller deal payment events',
                        'items': {'type': 'object'},
                    },
                    'DebtRecoveryEventList': {
                        'type': 'array',
                        'description': 'Debt recovery events',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'DebtRecoveryType': {'type': 'string'},
                                'RecoveryAmount': {
                                    'type': 'object',
                                    'properties': {
                                        'CurrencyCode': {'type': 'string'},
                                        'CurrencyAmount': {'type': 'number'},
                                    },
                                },
                                'DebtRecoveryItemList': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'RecoveryAmount': {
                                                'type': 'object',
                                                'properties': {
                                                    'CurrencyCode': {'type': 'string'},
                                                    'CurrencyAmount': {'type': 'number'},
                                                },
                                            },
                                            'OriginalAmount': {
                                                'type': 'object',
                                                'properties': {
                                                    'CurrencyCode': {'type': 'string'},
                                                    'CurrencyAmount': {'type': 'number'},
                                                },
                                            },
                                            'GroupBeginDate': {'type': 'string'},
                                            'GroupEndDate': {'type': 'string'},
                                        },
                                    },
                                },
                                'ChargeInstrumentList': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'Description': {'type': 'string'},
                                            'Tail': {'type': 'string'},
                                            'Amount': {
                                                'type': 'object',
                                                'properties': {
                                                    'CurrencyCode': {'type': 'string'},
                                                    'CurrencyAmount': {'type': 'number'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'LoanServicingEventList': {
                        'type': 'array',
                        'description': 'Loan servicing events',
                        'items': {'type': 'object'},
                    },
                    'AdjustmentEventList': {
                        'type': 'array',
                        'description': 'Adjustment events',
                        'items': {'type': 'object'},
                    },
                    'SAFETReimbursementEventList': {
                        'type': 'array',
                        'description': 'SAFET reimbursement events',
                        'items': {'type': 'object'},
                    },
                    'SellerReviewEnrollmentPaymentEventList': {
                        'type': 'array',
                        'description': 'Seller review enrollment payment events',
                        'items': {'type': 'object'},
                    },
                    'FBALiquidationEventList': {
                        'type': 'array',
                        'description': 'FBA liquidation events',
                        'items': {'type': 'object'},
                    },
                    'CouponPaymentEventList': {
                        'type': 'array',
                        'description': 'Coupon payment events',
                        'items': {'type': 'object'},
                    },
                    'ImagingServicesFeeEventList': {
                        'type': 'array',
                        'description': 'Imaging services fee events',
                        'items': {'type': 'object'},
                    },
                    'NetworkComminglingTransactionEventList': {
                        'type': 'array',
                        'description': 'Network commingling transaction events',
                        'items': {'type': 'object'},
                    },
                    'AffordabilityExpenseEventList': {
                        'type': 'array',
                        'description': 'Affordability expense events',
                        'items': {'type': 'object'},
                    },
                    'AffordabilityExpenseReversalEventList': {
                        'type': 'array',
                        'description': 'Affordability expense reversal events',
                        'items': {'type': 'object'},
                    },
                    'TrialShipmentEventList': {
                        'type': 'array',
                        'description': 'Trial shipment events',
                        'items': {'type': 'object'},
                    },
                    'TDSReimbursementEventList': {
                        'type': 'array',
                        'description': 'TDS reimbursement events',
                        'items': {'type': 'object'},
                    },
                    'TaxWithholdingEventList': {
                        'type': 'array',
                        'description': 'Tax withholding events',
                        'items': {'type': 'object'},
                    },
                    'RemovalShipmentEventList': {
                        'type': 'array',
                        'description': 'Removal shipment events',
                        'items': {'type': 'object'},
                    },
                    'RemovalShipmentAdjustmentEventList': {
                        'type': 'array',
                        'description': 'Removal shipment adjustment events',
                        'items': {'type': 'object'},
                    },
                    'ValueAddedServiceChargeEventList': {
                        'type': 'array',
                        'description': 'Value-added service charge events',
                        'items': {'type': 'object'},
                    },
                    'CapacityReservationBillingEventList': {
                        'type': 'array',
                        'description': 'Capacity reservation billing events',
                        'items': {'type': 'object'},
                    },
                    'FailedAdhocDisbursementEventList': {
                        'type': 'array',
                        'description': 'Failed adhoc disbursement events',
                        'items': {'type': 'object'},
                    },
                    'AdhocDisbursementEventList': {
                        'type': 'array',
                        'description': 'Adhoc disbursement events',
                        'items': {'type': 'object'},
                    },
                    'PerformanceBondRefundEventList': {
                        'type': 'array',
                        'description': 'Performance bond refund events',
                        'items': {'type': 'object'},
                    },
                    'EBTRefundReimbursementOnlyEventList': {
                        'type': 'array',
                        'description': 'EBT refund reimbursement only events',
                        'items': {'type': 'object'},
                    },
                },
                'x-airbyte-entity-name': 'list_financial_events',
                'x-airbyte-stream-name': 'ListFinancialEvents',
            },
        ),
        EntityDefinition(
            name='catalog_items',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/catalog/2022-04-01/items',
                    action=Action.LIST,
                    description='Search for items in the Amazon catalog by keywords or identifiers.',
                    query_params=[
                        'marketplaceIds',
                        'keywords',
                        'identifiers',
                        'identifiersType',
                        'includedData',
                        'pageSize',
                        'pageToken',
                    ],
                    query_params_schema={
                        'marketplaceIds': {
                            'type': 'string',
                            'required': True,
                            'default': 'ATVPDKIKX0DER',
                        },
                        'keywords': {'type': 'string', 'required': False},
                        'identifiers': {'type': 'string', 'required': False},
                        'identifiersType': {'type': 'string', 'required': False},
                        'includedData': {
                            'type': 'string',
                            'required': False,
                            'default': 'summaries',
                        },
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Catalog items search results',
                        'properties': {
                            'numberOfResults': {'type': 'integer', 'description': 'Total number of matching items'},
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'nextToken': {'type': 'string'},
                                    'previousToken': {'type': 'string'},
                                },
                            },
                            'refinements': {
                                'type': 'object',
                                'properties': {
                                    'brands': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'numberOfResults': {'type': 'integer'},
                                                'brandName': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'classifications': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'numberOfResults': {'type': 'integer'},
                                                'displayName': {'type': 'string'},
                                                'classificationId': {'type': 'string'},
                                            },
                                        },
                                    },
                                },
                            },
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Amazon catalog item',
                                    'properties': {
                                        'asin': {'type': 'string', 'description': 'Amazon Standard Identification Number'},
                                        'attributes': {'type': 'object', 'description': 'Item attributes'},
                                        'classifications': {
                                            'type': 'array',
                                            'description': 'Browse node classifications by marketplace',
                                            'items': {'type': 'object'},
                                        },
                                        'dimensions': {
                                            'type': 'array',
                                            'description': 'Item and package dimensions by marketplace',
                                            'items': {'type': 'object'},
                                        },
                                        'identifiers': {
                                            'type': 'array',
                                            'description': 'Product identifiers (EAN, UPC, etc.) by marketplace',
                                            'items': {'type': 'object'},
                                        },
                                        'images': {
                                            'type': 'array',
                                            'description': 'Product images by marketplace',
                                            'items': {'type': 'object'},
                                        },
                                        'productTypes': {
                                            'type': 'array',
                                            'description': 'Product types by marketplace',
                                            'items': {'type': 'object'},
                                        },
                                        'relationships': {
                                            'type': 'array',
                                            'description': 'Variation and package relationships by marketplace',
                                            'items': {'type': 'object'},
                                        },
                                        'salesRanks': {
                                            'type': 'array',
                                            'description': 'Sales rank information by marketplace',
                                            'items': {'type': 'object'},
                                        },
                                        'summaries': {
                                            'type': 'array',
                                            'description': 'Summary information by marketplace',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'marketplaceId': {'type': 'string'},
                                                    'adultProduct': {'type': 'boolean'},
                                                    'autographed': {'type': 'boolean'},
                                                    'brand': {'type': 'string'},
                                                    'browseClassification': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'displayName': {'type': 'string'},
                                                            'classificationId': {'type': 'string'},
                                                        },
                                                    },
                                                    'color': {'type': 'string'},
                                                    'itemClassification': {'type': 'string'},
                                                    'itemName': {'type': 'string'},
                                                    'manufacturer': {'type': 'string'},
                                                    'memorabilia': {'type': 'boolean'},
                                                    'modelNumber': {'type': 'string'},
                                                    'packageQuantity': {'type': 'integer'},
                                                    'partNumber': {'type': 'string'},
                                                    'size': {'type': 'string'},
                                                    'style': {'type': 'string'},
                                                    'tradeInEligible': {'type': 'boolean'},
                                                    'websiteDisplayGroup': {'type': 'string'},
                                                    'websiteDisplayGroupName': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'vendorDetails': {
                                            'type': 'array',
                                            'description': 'Vendor details by marketplace',
                                            'items': {'type': 'object'},
                                        },
                                    },
                                    'required': ['asin'],
                                    'x-airbyte-entity-name': 'catalog_items',
                                },
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'next_token': '$.pagination.nextToken', 'number_of_results': '$.numberOfResults'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/catalog/2022-04-01/items/{asin}',
                    action=Action.GET,
                    description='Retrieves details for an item in the Amazon catalog by ASIN.',
                    query_params=['marketplaceIds', 'includedData'],
                    query_params_schema={
                        'marketplaceIds': {
                            'type': 'string',
                            'required': True,
                            'default': 'ATVPDKIKX0DER',
                        },
                        'includedData': {
                            'type': 'string',
                            'required': False,
                            'default': 'summaries',
                        },
                    },
                    path_params=['asin'],
                    path_params_schema={
                        'asin': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Amazon catalog item',
                        'properties': {
                            'asin': {'type': 'string', 'description': 'Amazon Standard Identification Number'},
                            'attributes': {'type': 'object', 'description': 'Item attributes'},
                            'classifications': {
                                'type': 'array',
                                'description': 'Browse node classifications by marketplace',
                                'items': {'type': 'object'},
                            },
                            'dimensions': {
                                'type': 'array',
                                'description': 'Item and package dimensions by marketplace',
                                'items': {'type': 'object'},
                            },
                            'identifiers': {
                                'type': 'array',
                                'description': 'Product identifiers (EAN, UPC, etc.) by marketplace',
                                'items': {'type': 'object'},
                            },
                            'images': {
                                'type': 'array',
                                'description': 'Product images by marketplace',
                                'items': {'type': 'object'},
                            },
                            'productTypes': {
                                'type': 'array',
                                'description': 'Product types by marketplace',
                                'items': {'type': 'object'},
                            },
                            'relationships': {
                                'type': 'array',
                                'description': 'Variation and package relationships by marketplace',
                                'items': {'type': 'object'},
                            },
                            'salesRanks': {
                                'type': 'array',
                                'description': 'Sales rank information by marketplace',
                                'items': {'type': 'object'},
                            },
                            'summaries': {
                                'type': 'array',
                                'description': 'Summary information by marketplace',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'marketplaceId': {'type': 'string'},
                                        'adultProduct': {'type': 'boolean'},
                                        'autographed': {'type': 'boolean'},
                                        'brand': {'type': 'string'},
                                        'browseClassification': {
                                            'type': 'object',
                                            'properties': {
                                                'displayName': {'type': 'string'},
                                                'classificationId': {'type': 'string'},
                                            },
                                        },
                                        'color': {'type': 'string'},
                                        'itemClassification': {'type': 'string'},
                                        'itemName': {'type': 'string'},
                                        'manufacturer': {'type': 'string'},
                                        'memorabilia': {'type': 'boolean'},
                                        'modelNumber': {'type': 'string'},
                                        'packageQuantity': {'type': 'integer'},
                                        'partNumber': {'type': 'string'},
                                        'size': {'type': 'string'},
                                        'style': {'type': 'string'},
                                        'tradeInEligible': {'type': 'boolean'},
                                        'websiteDisplayGroup': {'type': 'string'},
                                        'websiteDisplayGroupName': {'type': 'string'},
                                    },
                                },
                            },
                            'vendorDetails': {
                                'type': 'array',
                                'description': 'Vendor details by marketplace',
                                'items': {'type': 'object'},
                            },
                        },
                        'required': ['asin'],
                        'x-airbyte-entity-name': 'catalog_items',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Amazon catalog item',
                'properties': {
                    'asin': {'type': 'string', 'description': 'Amazon Standard Identification Number'},
                    'attributes': {'type': 'object', 'description': 'Item attributes'},
                    'classifications': {
                        'type': 'array',
                        'description': 'Browse node classifications by marketplace',
                        'items': {'type': 'object'},
                    },
                    'dimensions': {
                        'type': 'array',
                        'description': 'Item and package dimensions by marketplace',
                        'items': {'type': 'object'},
                    },
                    'identifiers': {
                        'type': 'array',
                        'description': 'Product identifiers (EAN, UPC, etc.) by marketplace',
                        'items': {'type': 'object'},
                    },
                    'images': {
                        'type': 'array',
                        'description': 'Product images by marketplace',
                        'items': {'type': 'object'},
                    },
                    'productTypes': {
                        'type': 'array',
                        'description': 'Product types by marketplace',
                        'items': {'type': 'object'},
                    },
                    'relationships': {
                        'type': 'array',
                        'description': 'Variation and package relationships by marketplace',
                        'items': {'type': 'object'},
                    },
                    'salesRanks': {
                        'type': 'array',
                        'description': 'Sales rank information by marketplace',
                        'items': {'type': 'object'},
                    },
                    'summaries': {
                        'type': 'array',
                        'description': 'Summary information by marketplace',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'marketplaceId': {'type': 'string'},
                                'adultProduct': {'type': 'boolean'},
                                'autographed': {'type': 'boolean'},
                                'brand': {'type': 'string'},
                                'browseClassification': {
                                    'type': 'object',
                                    'properties': {
                                        'displayName': {'type': 'string'},
                                        'classificationId': {'type': 'string'},
                                    },
                                },
                                'color': {'type': 'string'},
                                'itemClassification': {'type': 'string'},
                                'itemName': {'type': 'string'},
                                'manufacturer': {'type': 'string'},
                                'memorabilia': {'type': 'boolean'},
                                'modelNumber': {'type': 'string'},
                                'packageQuantity': {'type': 'integer'},
                                'partNumber': {'type': 'string'},
                                'size': {'type': 'string'},
                                'style': {'type': 'string'},
                                'tradeInEligible': {'type': 'boolean'},
                                'websiteDisplayGroup': {'type': 'string'},
                                'websiteDisplayGroupName': {'type': 'string'},
                            },
                        },
                    },
                    'vendorDetails': {
                        'type': 'array',
                        'description': 'Vendor details by marketplace',
                        'items': {'type': 'object'},
                    },
                },
                'required': ['asin'],
                'x-airbyte-entity-name': 'catalog_items',
            },
        ),
        EntityDefinition(
            name='reports',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/reports/2021-06-30/reports',
                    action=Action.LIST,
                    description='Returns report details for the reports that match the specified filters.',
                    query_params=[
                        'reportTypes',
                        'processingStatuses',
                        'marketplaceIds',
                        'pageSize',
                        'createdSince',
                        'createdUntil',
                        'nextToken',
                    ],
                    query_params_schema={
                        'reportTypes': {'type': 'string', 'required': False},
                        'processingStatuses': {'type': 'string', 'required': False},
                        'marketplaceIds': {'type': 'string', 'required': False},
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'createdSince': {'type': 'string', 'required': False},
                        'createdUntil': {'type': 'string', 'required': False},
                        'nextToken': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of reports',
                        'properties': {
                            'reports': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Amazon SP-API report',
                                    'properties': {
                                        'reportId': {'type': 'string', 'description': 'Unique identifier for the report'},
                                        'reportType': {'type': 'string', 'description': 'The type of report'},
                                        'createdTime': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the report was created',
                                        },
                                        'processingStatus': {
                                            'type': 'string',
                                            'description': 'Processing status of the report',
                                            'enum': [
                                                'IN_QUEUE',
                                                'IN_PROGRESS',
                                                'DONE',
                                                'CANCELLED',
                                                'FATAL',
                                            ],
                                        },
                                        'dataStartTime': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Start of the report data date range',
                                        },
                                        'dataEndTime': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'End of the report data date range',
                                        },
                                        'reportScheduleId': {'type': 'string', 'description': 'Schedule that created this report'},
                                        'processingStartTime': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When processing started',
                                        },
                                        'processingEndTime': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When processing ended',
                                        },
                                        'reportDocumentId': {'type': 'string', 'description': 'Document ID for downloading the report (available when DONE)'},
                                        'marketplaceIds': {
                                            'type': 'array',
                                            'description': 'Marketplaces the report covers',
                                            'items': {'type': 'string'},
                                        },
                                    },
                                    'required': ['reportId'],
                                    'x-airbyte-entity-name': 'reports',
                                },
                            },
                            'nextToken': {'type': 'string', 'description': 'Pagination token for next page'},
                        },
                    },
                    record_extractor='$.reports',
                    meta_extractor={'next_token': '$.nextToken'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/reports/2021-06-30/reports/{reportId}',
                    action=Action.GET,
                    description='Returns report details including status and report document ID for a specified report.',
                    path_params=['reportId'],
                    path_params_schema={
                        'reportId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Amazon SP-API report',
                        'properties': {
                            'reportId': {'type': 'string', 'description': 'Unique identifier for the report'},
                            'reportType': {'type': 'string', 'description': 'The type of report'},
                            'createdTime': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the report was created',
                            },
                            'processingStatus': {
                                'type': 'string',
                                'description': 'Processing status of the report',
                                'enum': [
                                    'IN_QUEUE',
                                    'IN_PROGRESS',
                                    'DONE',
                                    'CANCELLED',
                                    'FATAL',
                                ],
                            },
                            'dataStartTime': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Start of the report data date range',
                            },
                            'dataEndTime': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'End of the report data date range',
                            },
                            'reportScheduleId': {'type': 'string', 'description': 'Schedule that created this report'},
                            'processingStartTime': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When processing started',
                            },
                            'processingEndTime': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When processing ended',
                            },
                            'reportDocumentId': {'type': 'string', 'description': 'Document ID for downloading the report (available when DONE)'},
                            'marketplaceIds': {
                                'type': 'array',
                                'description': 'Marketplaces the report covers',
                                'items': {'type': 'string'},
                            },
                        },
                        'required': ['reportId'],
                        'x-airbyte-entity-name': 'reports',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Amazon SP-API report',
                'properties': {
                    'reportId': {'type': 'string', 'description': 'Unique identifier for the report'},
                    'reportType': {'type': 'string', 'description': 'The type of report'},
                    'createdTime': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the report was created',
                    },
                    'processingStatus': {
                        'type': 'string',
                        'description': 'Processing status of the report',
                        'enum': [
                            'IN_QUEUE',
                            'IN_PROGRESS',
                            'DONE',
                            'CANCELLED',
                            'FATAL',
                        ],
                    },
                    'dataStartTime': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Start of the report data date range',
                    },
                    'dataEndTime': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'End of the report data date range',
                    },
                    'reportScheduleId': {'type': 'string', 'description': 'Schedule that created this report'},
                    'processingStartTime': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When processing started',
                    },
                    'processingEndTime': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When processing ended',
                    },
                    'reportDocumentId': {'type': 'string', 'description': 'Document ID for downloading the report (available when DONE)'},
                    'marketplaceIds': {
                        'type': 'array',
                        'description': 'Marketplaces the report covers',
                        'items': {'type': 'string'},
                    },
                },
                'required': ['reportId'],
                'x-airbyte-entity-name': 'reports',
            },
        ),
    ],
    search_field_paths={
        'orders': [
            'AmazonOrderId',
            'AutomatedShippingSettings',
            'AutomatedShippingSettings.HasAutomatedShippingSettings',
            'BuyerInfo',
            'DefaultShipFromLocationAddress',
            'DefaultShipFromLocationAddress.AddressLine1',
            'DefaultShipFromLocationAddress.City',
            'DefaultShipFromLocationAddress.CountryCode',
            'DefaultShipFromLocationAddress.Name',
            'DefaultShipFromLocationAddress.PostalCode',
            'DefaultShipFromLocationAddress.StateOrRegion',
            'EarliestDeliveryDate',
            'EarliestShipDate',
            'FulfillmentChannel',
            'HasRegulatedItems',
            'IsAccessPointOrder',
            'IsBusinessOrder',
            'IsGlobalExpressEnabled',
            'IsISPU',
            'IsPremiumOrder',
            'IsPrime',
            'IsReplacementOrder',
            'IsSoldByAB',
            'LastUpdateDate',
            'LatestDeliveryDate',
            'LatestShipDate',
            'MarketplaceId',
            'NumberOfItemsShipped',
            'NumberOfItemsUnshipped',
            'OrderStatus',
            'OrderTotal',
            'OrderTotal.CurrencyCode',
            'OrderTotal.Amount',
            'OrderType',
            'PaymentMethod',
            'PaymentMethodDetails',
            'PaymentMethodDetails[]',
            'PurchaseDate',
            'SalesChannel',
            'SellerOrderId',
            'ShipServiceLevel',
            'ShipmentServiceLevelCategory',
            'ShippingAddress',
            'ShippingAddress.City',
            'ShippingAddress.CountryCode',
            'ShippingAddress.PostalCode',
            'ShippingAddress.StateOrRegion',
            'seller_id',
        ],
        'order_items': [
            'ASIN',
            'AmazonOrderId',
            'BuyerInfo',
            'BuyerRequestedCancel',
            'CODFee',
            'CODFeeDiscount',
            'ConditionId',
            'ConditionNote',
            'ConditionSubtypeId',
            'DeemedResellerCategory',
            'IossNumber',
            'IsGift',
            'IsTransparency',
            'ItemPrice',
            'ItemTax',
            'LastUpdateDate',
            'OrderItemId',
            'PointsGranted',
            'PriceDesignation',
            'ProductInfo',
            'PromotionDiscount',
            'PromotionDiscountTax',
            'PromotionIds',
            'PromotionIds[]',
            'QuantityOrdered',
            'QuantityShipped',
            'ScheduledDeliveryEndDate',
            'ScheduledDeliveryStartDate',
            'SellerSKU',
            'SerialNumberRequired',
            'SerialNumbers',
            'SerialNumbers[]',
            'ShippingDiscount',
            'ShippingDiscountTax',
            'ShippingPrice',
            'ShippingTax',
            'StoreChainStoreId',
            'TaxCollection',
            'Title',
        ],
        'list_financial_event_groups': [
            'AccountTail',
            'BeginningBalance',
            'BeginningBalance.CurrencyCode',
            'BeginningBalance.CurrencyAmount',
            'ConvertedTotal',
            'ConvertedTotal.CurrencyCode',
            'ConvertedTotal.CurrencyAmount',
            'FinancialEventGroupEnd',
            'FinancialEventGroupId',
            'FinancialEventGroupStart',
            'FundTransferDate',
            'FundTransferStatus',
            'OriginalTotal',
            'OriginalTotal.CurrencyCode',
            'OriginalTotal.CurrencyAmount',
            'ProcessingStatus',
            'TraceId',
        ],
        'list_financial_events': [
            'AdhocDisbursementEventList',
            'AdhocDisbursementEventList[]',
            'AdjustmentEventList',
            'AdjustmentEventList[]',
            'AffordabilityExpenseEventList',
            'AffordabilityExpenseEventList[]',
            'AffordabilityExpenseReversalEventList',
            'AffordabilityExpenseReversalEventList[]',
            'CapacityReservationBillingEventList',
            'CapacityReservationBillingEventList[]',
            'ChargeRefundEventList',
            'ChargeRefundEventList[]',
            'ChargebackEventList',
            'ChargebackEventList[]',
            'CouponPaymentEventList',
            'CouponPaymentEventList[]',
            'DebtRecoveryEventList',
            'DebtRecoveryEventList[]',
            'FBALiquidationEventList',
            'FBALiquidationEventList[]',
            'FailedAdhocDisbursementEventList',
            'FailedAdhocDisbursementEventList[]',
            'GuaranteeClaimEventList',
            'GuaranteeClaimEventList[]',
            'ImagingServicesFeeEventList',
            'ImagingServicesFeeEventList[]',
            'LoanServicingEventList',
            'LoanServicingEventList[]',
            'NetworkComminglingTransactionEventList',
            'NetworkComminglingTransactionEventList[]',
            'PayWithAmazonEventList',
            'PayWithAmazonEventList[]',
            'PerformanceBondRefundEventList',
            'PerformanceBondRefundEventList[]',
            'PostedBefore',
            'ProductAdsPaymentEventList',
            'ProductAdsPaymentEventList[]',
            'RefundEventList',
            'RefundEventList[]',
            'RemovalShipmentAdjustmentEventList',
            'RemovalShipmentAdjustmentEventList[]',
            'RemovalShipmentEventList',
            'RemovalShipmentEventList[]',
            'RentalTransactionEventList',
            'RentalTransactionEventList[]',
            'RetrochargeEventList',
            'RetrochargeEventList[]',
            'SAFETReimbursementEventList',
            'SAFETReimbursementEventList[]',
            'SellerDealPaymentEventList',
            'SellerDealPaymentEventList[]',
            'SellerReviewEnrollmentPaymentEventList',
            'SellerReviewEnrollmentPaymentEventList[]',
            'ServiceFeeEventList',
            'ServiceFeeEventList[]',
            'ServiceProviderCreditEventList',
            'ServiceProviderCreditEventList[]',
            'ShipmentEventList',
            'ShipmentEventList[]',
            'ShipmentSettleEventList',
            'ShipmentSettleEventList[]',
            'TDSReimbursementEventList',
            'TDSReimbursementEventList[]',
            'TaxWithholdingEventList',
            'TaxWithholdingEventList[]',
            'TrialShipmentEventList',
            'TrialShipmentEventList[]',
            'ValueAddedServiceChargeEventList',
            'ValueAddedServiceChargeEventList[]',
        ],
    },
    server_variable_defaults={'region': 'na'},
)