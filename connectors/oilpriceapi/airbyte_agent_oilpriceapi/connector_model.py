"""
Connector model for oilpriceapi.

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

OilPriceApiConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('d19db54a-fac7-44ee-b57c-f2e712b3230b'),
    name='oilpriceapi',
    version='0.1.0',
    base_url='https://api.oilpriceapi.com/v1',
    auth=AuthConfig(
        type=AuthType.API_KEY,
        config={'header': 'Authorization', 'prefix': 'Token'},
        user_config_spec=AirbyteAuthConfig(
            title='API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='API key from oilpriceapi.com. Used as Token {api_key} in Authorization header.',
                ),
            },
            auth_mapping={'api_token': 'Token ${api_key}'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='latest_prices',
            actions=[
                Action.GET,
            ],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/prices/latest',
                    action=Action.GET,
                    description='Returns the latest spot price for a commodity (WTI or Brent crude oil)',
                    query_params=[
                        'by_code',
                    ],
                    query_params_schema={
                        'by_code': {'type': 'string', 'required': True, 'enum': ['WTI_USD', 'BRENT_USD']},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'status': {'type': ['string', 'null']},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'price': {'type': ['number', 'null'], 'description': 'Current commodity price'},
                                    'formatted': {'type': ['string', 'null'], 'description': 'Formatted price string'},
                                    'currency': {'type': ['string', 'null'], 'description': 'Currency code'},
                                    'code': {'type': 'string', 'description': 'Commodity code'},
                                    'created_at': {'type': ['string', 'null'], 'description': 'Record creation timestamp'},
                                    'updated_at': {'type': ['string', 'null'], 'description': 'Record update timestamp'},
                                    'type': {'type': ['string', 'null'], 'description': 'Price type'},
                                    'unit': {'type': ['string', 'null'], 'description': 'Price unit'},
                                    'source': {'type': ['string', 'null'], 'description': 'Data source'},
                                    'changes': {'type': ['object', 'null']},
                                    'metadata': {'type': ['object', 'null']},
                                },
                                'required': ['code'],
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'price': {'type': ['number', 'null'], 'description': 'Current commodity price'},
                    'formatted': {'type': ['string', 'null'], 'description': 'Formatted price string'},
                    'currency': {'type': ['string', 'null'], 'description': 'Currency code'},
                    'code': {'type': 'string', 'description': 'Commodity code (e.g. WTI_USD, BRENT_USD)'},
                    'created_at': {'type': ['string', 'null'], 'description': 'Record creation timestamp'},
                    'updated_at': {'type': ['string', 'null'], 'description': 'Record update timestamp'},
                    'type': {'type': ['string', 'null'], 'description': 'Price type'},
                    'unit': {'type': ['string', 'null'], 'description': 'Price unit'},
                    'source': {'type': ['string', 'null'], 'description': 'Data source'},
                    'changes': {'type': ['object', 'null'], 'description': '24h price changes'},
                    'metadata': {'type': ['object', 'null'], 'description': 'Price metadata'},
                },
                'required': ['code'],
            },
        ),
        EntityDefinition(
            name='historical_prices',
            actions=[
                Action.LIST,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/prices',
                    action=Action.LIST,
                    description='Returns historical price data for a commodity (WTI or Brent crude oil)',
                    query_params=[
                        'by_code',
                    ],
                    query_params_schema={
                        'by_code': {'type': 'string', 'required': True, 'enum': ['WTI_USD', 'BRENT_USD']},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'status': {'type': ['string', 'null']},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'prices': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': ['string', 'null'], 'description': 'Price record ID'},
                                                'price': {'type': ['number', 'null'], 'description': 'Historical commodity price'},
                                                'currency': {'type': ['string', 'null'], 'description': 'Currency code'},
                                                'code': {'type': 'string', 'description': 'Commodity code'},
                                                'created_at': {'type': 'string', 'description': 'Price record timestamp'},
                                                'source': {'type': ['string', 'null'], 'description': 'Data source'},
                                                'type': {'type': ['string', 'null'], 'description': 'Price type'},
                                            },
                                            'required': ['code', 'created_at'],
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.prices',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': ['string', 'null'], 'description': 'Price record ID'},
                    'price': {'type': ['number', 'null'], 'description': 'Historical commodity price'},
                    'currency': {'type': ['string', 'null'], 'description': 'Currency code'},
                    'code': {'type': 'string', 'description': 'Commodity code (e.g. WTI_USD, BRENT_USD)'},
                    'created_at': {'type': 'string', 'description': 'Price record timestamp'},
                    'source': {'type': ['string', 'null'], 'description': 'Data source'},
                    'type': {'type': ['string', 'null'], 'description': 'Price type'},
                },
                'required': ['code', 'created_at'],
            },
        ),
    ],
)
