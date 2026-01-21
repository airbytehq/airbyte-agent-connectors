"""
Connector model for amazon-ads.

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

AmazonAdsConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('c6b0a29e-1da9-4512-9002-7bfd0cba2246'),
    name='amazon-ads',
    version='1.0.1',
    base_url='{region_url}',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://api.amazon.com/auth/o2/token',
            'additional_headers': {'Amazon-Advertising-API-ClientId': '{{ client_id }}'},
        },
        user_config_spec=AirbyteAuthConfig(
            title='OAuth2 Authentication',
            type='object',
            required=['client_id', 'client_secret', 'refresh_token'],
            properties={
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='The client ID of your Amazon Ads API application',
                    airbyte_secret=True,
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='The client secret of your Amazon Ads API application',
                    airbyte_secret=True,
                ),
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='The refresh token obtained from the OAuth authorization flow',
                    airbyte_secret=True,
                ),
            },
            auth_mapping={
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
                'refresh_token': '${refresh_token}',
            },
            replication_auth_key_mapping={
                'client_id': 'client_id',
                'client_secret': 'client_secret',
                'refresh_token': 'refresh_token',
            },
            additional_headers={'Amazon-Advertising-API-ClientId': '{{ client_id }}'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='profiles',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/profiles',
                    action=Action.LIST,
                    description="Returns a list of advertising profiles associated with the authenticated user.\nProfiles represent an advertiser's account in a specific marketplace. Advertisers\nmay have a single profile if they advertise in only one marketplace, or a separate\nprofile for each marketplace if they advertise regionally or globally.\n",
                    query_params=['profileTypeFilter'],
                    query_params_schema={
                        'profileTypeFilter': {
                            'type': 'string',
                            'required': False,
                            'default': 'seller,vendor',
                        },
                    },
                    header_params=['Amazon-Advertising-API-ClientId'],
                    header_params_schema={
                        'Amazon-Advertising-API-ClientId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': "An advertising profile represents an advertiser's account in a specific marketplace.\nProfiles are used to scope API calls and manage advertising campaigns.\n",
                            'properties': {
                                'profileId': {
                                    'type': 'integer',
                                    'format': 'int64',
                                    'description': 'The unique identifier of the profile',
                                },
                                'countryCode': {
                                    'type': ['string', 'null'],
                                    'description': 'The country code of the marketplace (e.g., US, UK, DE, JP)',
                                },
                                'currencyCode': {
                                    'type': ['string', 'null'],
                                    'description': 'The currency code used for the profile (e.g., USD, GBP, EUR, JPY)',
                                },
                                'dailyBudget': {
                                    'type': ['number', 'null'],
                                    'description': 'The daily budget limit for the profile',
                                },
                                'timezone': {
                                    'type': ['string', 'null'],
                                    'description': 'The timezone of the profile (e.g., America/Los_Angeles, Europe/London)',
                                },
                                'accountInfo': {
                                    'oneOf': [
                                        {
                                            'type': 'object',
                                            'description': "Information about the advertiser's account associated with a profile",
                                            'properties': {
                                                'marketplaceStringId': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The unique identifier of the marketplace',
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The unique identifier of the account',
                                                },
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The type of account (e.g., seller, vendor, agency)',
                                                    'enum': ['seller', 'vendor', 'agency'],
                                                },
                                                'name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The name of the account',
                                                },
                                                'subType': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The subtype of the account',
                                                },
                                                'validPaymentMethod': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether the account has a valid payment method configured',
                                                },
                                            },
                                        },
                                        {'type': 'null'},
                                    ],
                                    'description': "Information about the advertiser's account",
                                },
                            },
                            'x-airbyte-entity-name': 'profiles',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/profiles/{profileId}',
                    action=Action.GET,
                    description="Retrieves a single advertising profile by its ID. The profile contains\ninformation about the advertiser's account in a specific marketplace.\n",
                    path_params=['profileId'],
                    path_params_schema={
                        'profileId': {'type': 'integer', 'required': True},
                    },
                    header_params=['Amazon-Advertising-API-ClientId'],
                    header_params_schema={
                        'Amazon-Advertising-API-ClientId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': "An advertising profile represents an advertiser's account in a specific marketplace.\nProfiles are used to scope API calls and manage advertising campaigns.\n",
                        'properties': {
                            'profileId': {
                                'type': 'integer',
                                'format': 'int64',
                                'description': 'The unique identifier of the profile',
                            },
                            'countryCode': {
                                'type': ['string', 'null'],
                                'description': 'The country code of the marketplace (e.g., US, UK, DE, JP)',
                            },
                            'currencyCode': {
                                'type': ['string', 'null'],
                                'description': 'The currency code used for the profile (e.g., USD, GBP, EUR, JPY)',
                            },
                            'dailyBudget': {
                                'type': ['number', 'null'],
                                'description': 'The daily budget limit for the profile',
                            },
                            'timezone': {
                                'type': ['string', 'null'],
                                'description': 'The timezone of the profile (e.g., America/Los_Angeles, Europe/London)',
                            },
                            'accountInfo': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': "Information about the advertiser's account associated with a profile",
                                        'properties': {
                                            'marketplaceStringId': {
                                                'type': ['string', 'null'],
                                                'description': 'The unique identifier of the marketplace',
                                            },
                                            'id': {
                                                'type': ['string', 'null'],
                                                'description': 'The unique identifier of the account',
                                            },
                                            'type': {
                                                'type': ['string', 'null'],
                                                'description': 'The type of account (e.g., seller, vendor, agency)',
                                                'enum': ['seller', 'vendor', 'agency'],
                                            },
                                            'name': {
                                                'type': ['string', 'null'],
                                                'description': 'The name of the account',
                                            },
                                            'subType': {
                                                'type': ['string', 'null'],
                                                'description': 'The subtype of the account',
                                            },
                                            'validPaymentMethod': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether the account has a valid payment method configured',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': "Information about the advertiser's account",
                            },
                        },
                        'x-airbyte-entity-name': 'profiles',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': "An advertising profile represents an advertiser's account in a specific marketplace.\nProfiles are used to scope API calls and manage advertising campaigns.\n",
                'properties': {
                    'profileId': {
                        'type': 'integer',
                        'format': 'int64',
                        'description': 'The unique identifier of the profile',
                    },
                    'countryCode': {
                        'type': ['string', 'null'],
                        'description': 'The country code of the marketplace (e.g., US, UK, DE, JP)',
                    },
                    'currencyCode': {
                        'type': ['string', 'null'],
                        'description': 'The currency code used for the profile (e.g., USD, GBP, EUR, JPY)',
                    },
                    'dailyBudget': {
                        'type': ['number', 'null'],
                        'description': 'The daily budget limit for the profile',
                    },
                    'timezone': {
                        'type': ['string', 'null'],
                        'description': 'The timezone of the profile (e.g., America/Los_Angeles, Europe/London)',
                    },
                    'accountInfo': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/AccountInfo'},
                            {'type': 'null'},
                        ],
                        'description': "Information about the advertiser's account",
                    },
                },
                'x-airbyte-entity-name': 'profiles',
            },
        ),
        EntityDefinition(
            name='portfolios',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/portfolios/list',
                    action=Action.LIST,
                    description='Returns a list of portfolios for the specified profile. Portfolios are used to\ngroup campaigns together for organizational and budget management purposes.\n',
                    body_fields=['includeExtendedDataFields'],
                    header_params=['Amazon-Advertising-API-ClientId', 'Amazon-Advertising-API-Scope'],
                    header_params_schema={
                        'Amazon-Advertising-API-ClientId': {'type': 'string', 'required': True},
                        'Amazon-Advertising-API-Scope': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={'includeExtendedDataFields': 'true'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'includeExtendedDataFields': {
                                'type': 'string',
                                'default': 'true',
                                'description': 'Whether to include extended data fields in the response',
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'portfolios': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A portfolio is a container for grouping campaigns together for organizational\nand budget management purposes.\n',
                                    'properties': {
                                        'portfolioId': {
                                            'oneOf': [
                                                {'type': 'string'},
                                                {'type': 'integer', 'format': 'int64'},
                                            ],
                                            'description': 'The unique identifier of the portfolio',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the portfolio',
                                        },
                                        'budget': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Budget configuration for a portfolio',
                                                    'properties': {
                                                        'amount': {
                                                            'type': ['number', 'null'],
                                                            'description': 'The budget amount',
                                                        },
                                                        'currencyCode': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The currency code for the budget',
                                                        },
                                                        'policy': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The budget policy (dateRange, monthlyRecurring)',
                                                        },
                                                        'startDate': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The start date of the budget period',
                                                        },
                                                        'endDate': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The end date of the budget period',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Budget configuration for the portfolio',
                                        },
                                        'inBudget': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the portfolio is within its budget',
                                        },
                                        'state': {
                                            'type': ['string', 'null'],
                                            'description': 'The state of the portfolio (enabled, paused, archived)',
                                            'enum': [
                                                'enabled',
                                                'paused',
                                                'archived',
                                                'ENABLED',
                                                'PAUSED',
                                                'ARCHIVED',
                                            ],
                                        },
                                        'creationDate': {
                                            'type': ['integer', 'null'],
                                            'format': 'int64',
                                            'description': 'The creation date of the portfolio (epoch milliseconds)',
                                        },
                                        'lastUpdatedDate': {
                                            'type': ['integer', 'null'],
                                            'format': 'int64',
                                            'description': 'The last updated date of the portfolio (epoch milliseconds)',
                                        },
                                        'servingStatus': {
                                            'type': ['string', 'null'],
                                            'description': 'The serving status of the portfolio',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'portfolios',
                                },
                            },
                            'nextToken': {
                                'type': ['string', 'null'],
                                'description': 'Token for pagination',
                            },
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/portfolios/{portfolioId}',
                    action=Action.GET,
                    description='Retrieves a single portfolio by its ID using the v2 API.\n',
                    path_params=['portfolioId'],
                    path_params_schema={
                        'portfolioId': {'type': 'integer', 'required': True},
                    },
                    header_params=['Amazon-Advertising-API-ClientId', 'Amazon-Advertising-API-Scope'],
                    header_params_schema={
                        'Amazon-Advertising-API-ClientId': {'type': 'string', 'required': True},
                        'Amazon-Advertising-API-Scope': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A portfolio is a container for grouping campaigns together for organizational\nand budget management purposes.\n',
                        'properties': {
                            'portfolioId': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'integer', 'format': 'int64'},
                                ],
                                'description': 'The unique identifier of the portfolio',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the portfolio',
                            },
                            'budget': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Budget configuration for a portfolio',
                                        'properties': {
                                            'amount': {
                                                'type': ['number', 'null'],
                                                'description': 'The budget amount',
                                            },
                                            'currencyCode': {
                                                'type': ['string', 'null'],
                                                'description': 'The currency code for the budget',
                                            },
                                            'policy': {
                                                'type': ['string', 'null'],
                                                'description': 'The budget policy (dateRange, monthlyRecurring)',
                                            },
                                            'startDate': {
                                                'type': ['string', 'null'],
                                                'description': 'The start date of the budget period',
                                            },
                                            'endDate': {
                                                'type': ['string', 'null'],
                                                'description': 'The end date of the budget period',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Budget configuration for the portfolio',
                            },
                            'inBudget': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the portfolio is within its budget',
                            },
                            'state': {
                                'type': ['string', 'null'],
                                'description': 'The state of the portfolio (enabled, paused, archived)',
                                'enum': [
                                    'enabled',
                                    'paused',
                                    'archived',
                                    'ENABLED',
                                    'PAUSED',
                                    'ARCHIVED',
                                ],
                            },
                            'creationDate': {
                                'type': ['integer', 'null'],
                                'format': 'int64',
                                'description': 'The creation date of the portfolio (epoch milliseconds)',
                            },
                            'lastUpdatedDate': {
                                'type': ['integer', 'null'],
                                'format': 'int64',
                                'description': 'The last updated date of the portfolio (epoch milliseconds)',
                            },
                            'servingStatus': {
                                'type': ['string', 'null'],
                                'description': 'The serving status of the portfolio',
                            },
                        },
                        'x-airbyte-entity-name': 'portfolios',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A portfolio is a container for grouping campaigns together for organizational\nand budget management purposes.\n',
                'properties': {
                    'portfolioId': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'integer', 'format': 'int64'},
                        ],
                        'description': 'The unique identifier of the portfolio',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the portfolio',
                    },
                    'budget': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/PortfolioBudget'},
                            {'type': 'null'},
                        ],
                        'description': 'Budget configuration for the portfolio',
                    },
                    'inBudget': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the portfolio is within its budget',
                    },
                    'state': {
                        'type': ['string', 'null'],
                        'description': 'The state of the portfolio (enabled, paused, archived)',
                        'enum': [
                            'enabled',
                            'paused',
                            'archived',
                            'ENABLED',
                            'PAUSED',
                            'ARCHIVED',
                        ],
                    },
                    'creationDate': {
                        'type': ['integer', 'null'],
                        'format': 'int64',
                        'description': 'The creation date of the portfolio (epoch milliseconds)',
                    },
                    'lastUpdatedDate': {
                        'type': ['integer', 'null'],
                        'format': 'int64',
                        'description': 'The last updated date of the portfolio (epoch milliseconds)',
                    },
                    'servingStatus': {
                        'type': ['string', 'null'],
                        'description': 'The serving status of the portfolio',
                    },
                },
                'x-airbyte-entity-name': 'portfolios',
            },
        ),
        EntityDefinition(
            name='sponsored_product_campaigns',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/sp/campaigns/list',
                    action=Action.LIST,
                    description='Returns a list of sponsored product campaigns for the specified profile.\nSponsored Products campaigns promote individual product listings on Amazon.\n',
                    body_fields=['stateFilter', 'maxResults', 'nextToken'],
                    header_params=[
                        'Amazon-Advertising-API-ClientId',
                        'Amazon-Advertising-API-Scope',
                        'Accept',
                        'Content-Type',
                    ],
                    header_params_schema={
                        'Amazon-Advertising-API-ClientId': {'type': 'string', 'required': True},
                        'Amazon-Advertising-API-Scope': {'type': 'string', 'required': True},
                        'Accept': {
                            'type': 'string',
                            'required': True,
                            'default': 'application/vnd.spCampaign.v3+json',
                        },
                        'Content-Type': {
                            'type': 'string',
                            'required': True,
                            'default': 'application/vnd.spCampaign.v3+json',
                        },
                    },
                    request_body_defaults={'maxResults': 100},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'stateFilter': {
                                'type': 'object',
                                'properties': {
                                    'include': {'type': 'string', 'description': 'Comma-separated list of states to include (enabled, paused, archived)'},
                                },
                            },
                            'maxResults': {
                                'type': 'integer',
                                'description': 'Maximum number of results to return',
                                'default': 100,
                            },
                            'nextToken': {'type': 'string', 'description': 'Token for pagination'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'campaigns': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Sponsored Products campaign promotes individual product listings on Amazon.\nCampaigns contain ad groups, which contain ads and targeting settings.\nNote: The list endpoint (v3) and get endpoint (v2) return slightly different field formats.\n',
                                    'properties': {
                                        'campaignId': {
                                            'oneOf': [
                                                {'type': 'string'},
                                                {'type': 'integer', 'format': 'int64'},
                                            ],
                                            'description': 'The unique identifier of the campaign',
                                        },
                                        'portfolioId': {
                                            'oneOf': [
                                                {'type': 'string'},
                                                {'type': 'integer', 'format': 'int64'},
                                                {'type': 'null'},
                                            ],
                                            'description': 'The portfolio ID this campaign belongs to',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the campaign',
                                        },
                                        'campaignType': {
                                            'type': ['string', 'null'],
                                            'description': 'The type of campaign (sponsoredProducts) - returned by v2 API',
                                        },
                                        'tags': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': True,
                                            'description': 'Tags associated with the campaign',
                                        },
                                        'targetingType': {
                                            'type': ['string', 'null'],
                                            'description': 'The targeting type (manual, auto)',
                                            'enum': [
                                                'manual',
                                                'auto',
                                                'MANUAL',
                                                'AUTO',
                                            ],
                                        },
                                        'premiumBidAdjustment': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether premium bid adjustment is enabled - returned by v2 API',
                                        },
                                        'state': {
                                            'type': ['string', 'null'],
                                            'description': 'The state of the campaign (enabled, paused, archived)',
                                            'enum': [
                                                'enabled',
                                                'paused',
                                                'archived',
                                                'ENABLED',
                                                'PAUSED',
                                                'ARCHIVED',
                                            ],
                                        },
                                        'dynamicBidding': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Dynamic bidding settings for a campaign',
                                                    'properties': {
                                                        'placementBidding': {
                                                            'type': ['array', 'null'],
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'placement': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'The placement type',
                                                                    },
                                                                    'percentage': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'The bid adjustment percentage',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        'strategy': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The bidding strategy (legacyForSales, autoForSales, manual)',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Dynamic bidding settings for the campaign (v3 API format)',
                                        },
                                        'bidding': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Dynamic bidding settings for a campaign',
                                                    'properties': {
                                                        'placementBidding': {
                                                            'type': ['array', 'null'],
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'placement': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'The placement type',
                                                                    },
                                                                    'percentage': {
                                                                        'type': ['integer', 'null'],
                                                                        'description': 'The bid adjustment percentage',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        'strategy': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The bidding strategy (legacyForSales, autoForSales, manual)',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Bidding settings for the campaign (v2 API format)',
                                        },
                                        'startDate': {
                                            'type': ['string', 'null'],
                                            'description': 'The start date of the campaign (YYYYMMDD format)',
                                        },
                                        'endDate': {
                                            'type': ['string', 'null'],
                                            'description': 'The end date of the campaign (YYYYMMDD format)',
                                        },
                                        'dailyBudget': {
                                            'type': ['number', 'null'],
                                            'description': 'The daily budget amount - returned by v2 API',
                                        },
                                        'budget': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Budget configuration for a campaign',
                                                    'properties': {
                                                        'budgetType': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The budget type (daily)',
                                                        },
                                                        'budget': {
                                                            'type': ['number', 'null'],
                                                            'description': 'The budget amount',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Budget configuration for the campaign (v3 API format)',
                                        },
                                        'extendedData': {
                                            'type': ['object', 'null'],
                                            'description': 'Extended data fields for the campaign',
                                        },
                                        'marketplaceBudgetAllocation': {
                                            'type': ['string', 'null'],
                                            'description': 'Marketplace budget allocation setting (MANUAL, AUTO)',
                                        },
                                        'offAmazonSettings': {
                                            'type': ['object', 'null'],
                                            'description': 'Off-Amazon settings for the campaign',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'sponsored_product_campaigns',
                                },
                            },
                            'nextToken': {
                                'type': ['string', 'null'],
                                'description': 'Token for pagination',
                            },
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/sp/campaigns/{campaignId}',
                    action=Action.GET,
                    description='Retrieves a single sponsored product campaign by its ID using the v2 API.\n',
                    path_params=['campaignId'],
                    path_params_schema={
                        'campaignId': {'type': 'integer', 'required': True},
                    },
                    header_params=['Amazon-Advertising-API-ClientId', 'Amazon-Advertising-API-Scope'],
                    header_params_schema={
                        'Amazon-Advertising-API-ClientId': {'type': 'string', 'required': True},
                        'Amazon-Advertising-API-Scope': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Sponsored Products campaign promotes individual product listings on Amazon.\nCampaigns contain ad groups, which contain ads and targeting settings.\nNote: The list endpoint (v3) and get endpoint (v2) return slightly different field formats.\n',
                        'properties': {
                            'campaignId': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'integer', 'format': 'int64'},
                                ],
                                'description': 'The unique identifier of the campaign',
                            },
                            'portfolioId': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'integer', 'format': 'int64'},
                                    {'type': 'null'},
                                ],
                                'description': 'The portfolio ID this campaign belongs to',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the campaign',
                            },
                            'campaignType': {
                                'type': ['string', 'null'],
                                'description': 'The type of campaign (sponsoredProducts) - returned by v2 API',
                            },
                            'tags': {
                                'type': ['object', 'null'],
                                'additionalProperties': True,
                                'description': 'Tags associated with the campaign',
                            },
                            'targetingType': {
                                'type': ['string', 'null'],
                                'description': 'The targeting type (manual, auto)',
                                'enum': [
                                    'manual',
                                    'auto',
                                    'MANUAL',
                                    'AUTO',
                                ],
                            },
                            'premiumBidAdjustment': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether premium bid adjustment is enabled - returned by v2 API',
                            },
                            'state': {
                                'type': ['string', 'null'],
                                'description': 'The state of the campaign (enabled, paused, archived)',
                                'enum': [
                                    'enabled',
                                    'paused',
                                    'archived',
                                    'ENABLED',
                                    'PAUSED',
                                    'ARCHIVED',
                                ],
                            },
                            'dynamicBidding': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Dynamic bidding settings for a campaign',
                                        'properties': {
                                            'placementBidding': {
                                                'type': ['array', 'null'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'placement': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The placement type',
                                                        },
                                                        'percentage': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'The bid adjustment percentage',
                                                        },
                                                    },
                                                },
                                            },
                                            'strategy': {
                                                'type': ['string', 'null'],
                                                'description': 'The bidding strategy (legacyForSales, autoForSales, manual)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Dynamic bidding settings for the campaign (v3 API format)',
                            },
                            'bidding': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Dynamic bidding settings for a campaign',
                                        'properties': {
                                            'placementBidding': {
                                                'type': ['array', 'null'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'placement': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The placement type',
                                                        },
                                                        'percentage': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'The bid adjustment percentage',
                                                        },
                                                    },
                                                },
                                            },
                                            'strategy': {
                                                'type': ['string', 'null'],
                                                'description': 'The bidding strategy (legacyForSales, autoForSales, manual)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Bidding settings for the campaign (v2 API format)',
                            },
                            'startDate': {
                                'type': ['string', 'null'],
                                'description': 'The start date of the campaign (YYYYMMDD format)',
                            },
                            'endDate': {
                                'type': ['string', 'null'],
                                'description': 'The end date of the campaign (YYYYMMDD format)',
                            },
                            'dailyBudget': {
                                'type': ['number', 'null'],
                                'description': 'The daily budget amount - returned by v2 API',
                            },
                            'budget': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Budget configuration for a campaign',
                                        'properties': {
                                            'budgetType': {
                                                'type': ['string', 'null'],
                                                'description': 'The budget type (daily)',
                                            },
                                            'budget': {
                                                'type': ['number', 'null'],
                                                'description': 'The budget amount',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Budget configuration for the campaign (v3 API format)',
                            },
                            'extendedData': {
                                'type': ['object', 'null'],
                                'description': 'Extended data fields for the campaign',
                            },
                            'marketplaceBudgetAllocation': {
                                'type': ['string', 'null'],
                                'description': 'Marketplace budget allocation setting (MANUAL, AUTO)',
                            },
                            'offAmazonSettings': {
                                'type': ['object', 'null'],
                                'description': 'Off-Amazon settings for the campaign',
                            },
                        },
                        'x-airbyte-entity-name': 'sponsored_product_campaigns',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Sponsored Products campaign promotes individual product listings on Amazon.\nCampaigns contain ad groups, which contain ads and targeting settings.\nNote: The list endpoint (v3) and get endpoint (v2) return slightly different field formats.\n',
                'properties': {
                    'campaignId': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'integer', 'format': 'int64'},
                        ],
                        'description': 'The unique identifier of the campaign',
                    },
                    'portfolioId': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'integer', 'format': 'int64'},
                            {'type': 'null'},
                        ],
                        'description': 'The portfolio ID this campaign belongs to',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the campaign',
                    },
                    'campaignType': {
                        'type': ['string', 'null'],
                        'description': 'The type of campaign (sponsoredProducts) - returned by v2 API',
                    },
                    'tags': {
                        'type': ['object', 'null'],
                        'additionalProperties': True,
                        'description': 'Tags associated with the campaign',
                    },
                    'targetingType': {
                        'type': ['string', 'null'],
                        'description': 'The targeting type (manual, auto)',
                        'enum': [
                            'manual',
                            'auto',
                            'MANUAL',
                            'AUTO',
                        ],
                    },
                    'premiumBidAdjustment': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether premium bid adjustment is enabled - returned by v2 API',
                    },
                    'state': {
                        'type': ['string', 'null'],
                        'description': 'The state of the campaign (enabled, paused, archived)',
                        'enum': [
                            'enabled',
                            'paused',
                            'archived',
                            'ENABLED',
                            'PAUSED',
                            'ARCHIVED',
                        ],
                    },
                    'dynamicBidding': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/DynamicBidding'},
                            {'type': 'null'},
                        ],
                        'description': 'Dynamic bidding settings for the campaign (v3 API format)',
                    },
                    'bidding': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/DynamicBidding'},
                            {'type': 'null'},
                        ],
                        'description': 'Bidding settings for the campaign (v2 API format)',
                    },
                    'startDate': {
                        'type': ['string', 'null'],
                        'description': 'The start date of the campaign (YYYYMMDD format)',
                    },
                    'endDate': {
                        'type': ['string', 'null'],
                        'description': 'The end date of the campaign (YYYYMMDD format)',
                    },
                    'dailyBudget': {
                        'type': ['number', 'null'],
                        'description': 'The daily budget amount - returned by v2 API',
                    },
                    'budget': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CampaignBudget'},
                            {'type': 'null'},
                        ],
                        'description': 'Budget configuration for the campaign (v3 API format)',
                    },
                    'extendedData': {
                        'type': ['object', 'null'],
                        'description': 'Extended data fields for the campaign',
                    },
                    'marketplaceBudgetAllocation': {
                        'type': ['string', 'null'],
                        'description': 'Marketplace budget allocation setting (MANUAL, AUTO)',
                    },
                    'offAmazonSettings': {
                        'type': ['object', 'null'],
                        'description': 'Off-Amazon settings for the campaign',
                    },
                },
                'x-airbyte-entity-name': 'sponsored_product_campaigns',
            },
        ),
    ],
)