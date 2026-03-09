"""
Connector model for tiktok-marketing.

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
from ._vendored.connector_sdk.schema.components import (
    PathOverrideConfig,
)
from uuid import (
    UUID,
)

TiktokMarketingConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('4bfac00d-ce15-44ff-95b9-9e3c3e8fbd35'),
    name='tiktok-marketing',
    version='1.1.4',
    base_url='https://business-api.tiktok.com/open_api/v1.3',
    auth=AuthConfig(
        type=AuthType.API_KEY,
        config={'header': 'Access-Token', 'in': 'header'},
        user_config_spec=AirbyteAuthConfig(
            title='OAuth Access Token',
            type='object',
            required=['access_token'],
            properties={
                'access_token': AuthConfigFieldSpec(
                    title='Access Token',
                    description='Your TikTok Marketing API access token',
                ),
            },
            auth_mapping={'api_key': '${access_token}'},
            replication_auth_key_mapping={'credentials.access_token': 'access_token'},
            replication_auth_key_constants={
                'credentials.auth_type': 'oauth2.0',
                'credentials.app_id': '**',
                'credentials.secret': '**',
            },
        ),
    ),
    entities=[
        EntityDefinition(
            name='advertisers',
            stream_name='advertisers',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/advertiser/info/',
                    action=Action.LIST,
                    description='Get advertiser account information',
                    query_params=['advertiser_ids', 'page', 'page_size'],
                    query_params_schema={
                        'advertiser_ids': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'TikTok advertiser account',
                                            'properties': {
                                                'advertiser_id': {'type': 'string', 'description': 'Unique identifier for the advertiser'},
                                                'name': {'type': 'string', 'description': 'The name of the advertiser or company'},
                                                'address': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The physical address of the advertiser',
                                                },
                                                'company': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The name of the company associated with the advertiser',
                                                },
                                                'contacter': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The contact person for the advertiser',
                                                },
                                                'country': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The country where the advertiser is located',
                                                },
                                                'currency': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The currency used for transactions in the account',
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                    'description': 'A brief description of the advertiser or company',
                                                },
                                                'email': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The email address associated with the advertiser',
                                                },
                                                'industry': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The industry or sector the advertiser operates in',
                                                },
                                                'language': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The preferred language of communication for the advertiser',
                                                },
                                                'license_no': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The license number of the advertiser',
                                                },
                                                'license_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The URL link to the license documentation',
                                                },
                                                'cellphone_number': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The cellphone number of the advertiser',
                                                },
                                                'promotion_area': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The specific area where the advertiser focuses promotion',
                                                },
                                                'rejection_reason': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Reason for any advertisement rejection',
                                                },
                                                'role': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The role or position of the advertiser within the company',
                                                },
                                                'status': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The current status of the advertiser account',
                                                },
                                                'timezone': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The timezone setting for the advertiser',
                                                },
                                                'balance': {'type': 'number', 'description': 'The current balance in the advertiser account'},
                                                'create_time': {'type': 'integer', 'description': 'The timestamp when the advertiser account was created'},
                                                'telephone_number': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The telephone number of the advertiser',
                                                },
                                                'display_timezone': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The timezone for display purposes',
                                                },
                                                'promotion_center_province': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The province at the center of the promotion activities',
                                                },
                                                'advertiser_account_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of advertiser account',
                                                },
                                                'license_city': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The city where the license is registered',
                                                },
                                                'brand': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The brand name associated with the advertiser',
                                                },
                                                'license_province': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The province where the license is registered',
                                                },
                                                'promotion_center_city': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The city at the center of the promotion activities',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'advertisers',
                                            'x-airbyte-stream-name': 'advertisers',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    preferred_for_check=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'TikTok advertiser account',
                'properties': {
                    'advertiser_id': {'type': 'string', 'description': 'Unique identifier for the advertiser'},
                    'name': {'type': 'string', 'description': 'The name of the advertiser or company'},
                    'address': {
                        'type': ['null', 'string'],
                        'description': 'The physical address of the advertiser',
                    },
                    'company': {
                        'type': ['null', 'string'],
                        'description': 'The name of the company associated with the advertiser',
                    },
                    'contacter': {
                        'type': ['null', 'string'],
                        'description': 'The contact person for the advertiser',
                    },
                    'country': {
                        'type': ['null', 'string'],
                        'description': 'The country where the advertiser is located',
                    },
                    'currency': {
                        'type': ['null', 'string'],
                        'description': 'The currency used for transactions in the account',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'A brief description of the advertiser or company',
                    },
                    'email': {
                        'type': ['null', 'string'],
                        'description': 'The email address associated with the advertiser',
                    },
                    'industry': {
                        'type': ['null', 'string'],
                        'description': 'The industry or sector the advertiser operates in',
                    },
                    'language': {
                        'type': ['null', 'string'],
                        'description': 'The preferred language of communication for the advertiser',
                    },
                    'license_no': {
                        'type': ['null', 'string'],
                        'description': 'The license number of the advertiser',
                    },
                    'license_url': {
                        'type': ['null', 'string'],
                        'description': 'The URL link to the license documentation',
                    },
                    'cellphone_number': {
                        'type': ['null', 'string'],
                        'description': 'The cellphone number of the advertiser',
                    },
                    'promotion_area': {
                        'type': ['null', 'string'],
                        'description': 'The specific area where the advertiser focuses promotion',
                    },
                    'rejection_reason': {
                        'type': ['null', 'string'],
                        'description': 'Reason for any advertisement rejection',
                    },
                    'role': {
                        'type': ['null', 'string'],
                        'description': 'The role or position of the advertiser within the company',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'The current status of the advertiser account',
                    },
                    'timezone': {
                        'type': ['null', 'string'],
                        'description': 'The timezone setting for the advertiser',
                    },
                    'balance': {'type': 'number', 'description': 'The current balance in the advertiser account'},
                    'create_time': {'type': 'integer', 'description': 'The timestamp when the advertiser account was created'},
                    'telephone_number': {
                        'type': ['null', 'string'],
                        'description': 'The telephone number of the advertiser',
                    },
                    'display_timezone': {
                        'type': ['null', 'string'],
                        'description': 'The timezone for display purposes',
                    },
                    'promotion_center_province': {
                        'type': ['null', 'string'],
                        'description': 'The province at the center of the promotion activities',
                    },
                    'advertiser_account_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of advertiser account',
                    },
                    'license_city': {
                        'type': ['null', 'string'],
                        'description': 'The city where the license is registered',
                    },
                    'brand': {
                        'type': ['null', 'string'],
                        'description': 'The brand name associated with the advertiser',
                    },
                    'license_province': {
                        'type': ['null', 'string'],
                        'description': 'The province where the license is registered',
                    },
                    'promotion_center_city': {
                        'type': ['null', 'string'],
                        'description': 'The city at the center of the promotion activities',
                    },
                },
                'x-airbyte-entity-name': 'advertisers',
                'x-airbyte-stream-name': 'advertisers',
            },
        ),
        EntityDefinition(
            name='campaigns',
            stream_name='campaigns',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/campaign/get/',
                    action=Action.LIST,
                    description='Get campaigns for an advertiser',
                    query_params=['advertiser_id', 'page', 'page_size'],
                    query_params_schema={
                        'advertiser_id': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 1000,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'TikTok marketing campaign',
                                            'properties': {
                                                'campaign_id': {'type': 'string', 'description': 'The unique identifier of the campaign'},
                                                'campaign_name': {'type': 'string', 'description': 'Name of the campaign'},
                                                'campaign_type': {'type': 'string', 'description': 'Type of campaign'},
                                                'advertiser_id': {'type': 'string', 'description': 'The unique identifier of the advertiser'},
                                                'budget': {'type': 'number', 'description': 'Total budget allocated for the campaign'},
                                                'budget_mode': {'type': 'string', 'description': 'Mode in which the budget is managed'},
                                                'secondary_status': {'type': 'string', 'description': 'Additional status information of the campaign'},
                                                'operation_status': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Current operational status of the campaign',
                                                },
                                                'objective': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The objective or goal of the campaign',
                                                },
                                                'objective_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Type of objective selected for the campaign',
                                                },
                                                'budget_optimize_on': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'The metric that the budget optimization is based on',
                                                },
                                                'bid_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Type of bid strategy being used',
                                                },
                                                'deep_bid_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Advanced bid type used for optimization',
                                                },
                                                'optimization_goal': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Specific goal to be optimized for',
                                                },
                                                'split_test_variable': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Variable being tested in a split test campaign',
                                                },
                                                'is_new_structure': {'type': 'boolean', 'description': 'Flag indicating if the campaign uses a new structure'},
                                                'create_time': {'type': 'string', 'description': 'Timestamp when the campaign was created'},
                                                'modify_time': {'type': 'string', 'description': 'Timestamp when the campaign was last modified'},
                                                'roas_bid': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Return on ad spend goal set for the campaign',
                                                },
                                                'is_smart_performance_campaign': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if the campaign uses smart performance',
                                                },
                                                'is_search_campaign': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if the campaign is a search campaign',
                                                },
                                                'app_promotion_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Type of app promotion being used',
                                                },
                                                'rf_campaign_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Type of reach and frequency campaign',
                                                },
                                                'disable_skan_campaign': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if SKAN campaign is disabled',
                                                },
                                                'is_advanced_dedicated_campaign': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if campaign is advanced dedicated',
                                                },
                                                'rta_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time API ID',
                                                },
                                                'campaign_automation_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Campaign automation type',
                                                },
                                                'rta_bid_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if RTA bid is enabled',
                                                },
                                                'rta_product_selection_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if RTA product selection is enabled',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'campaigns',
                                            'x-airbyte-stream-name': 'campaigns',
                                        },
                                    },
                                    'page_info': {
                                        'type': 'object',
                                        'properties': {
                                            'total_number': {'type': 'integer'},
                                            'page': {'type': 'integer'},
                                            'page_size': {'type': 'integer'},
                                            'total_page': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    meta_extractor={'page_info': '$.data.page_info'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'TikTok marketing campaign',
                'properties': {
                    'campaign_id': {'type': 'string', 'description': 'The unique identifier of the campaign'},
                    'campaign_name': {'type': 'string', 'description': 'Name of the campaign'},
                    'campaign_type': {'type': 'string', 'description': 'Type of campaign'},
                    'advertiser_id': {'type': 'string', 'description': 'The unique identifier of the advertiser'},
                    'budget': {'type': 'number', 'description': 'Total budget allocated for the campaign'},
                    'budget_mode': {'type': 'string', 'description': 'Mode in which the budget is managed'},
                    'secondary_status': {'type': 'string', 'description': 'Additional status information of the campaign'},
                    'operation_status': {
                        'type': ['null', 'string'],
                        'description': 'Current operational status of the campaign',
                    },
                    'objective': {
                        'type': ['null', 'string'],
                        'description': 'The objective or goal of the campaign',
                    },
                    'objective_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of objective selected for the campaign',
                    },
                    'budget_optimize_on': {
                        'type': ['null', 'boolean'],
                        'description': 'The metric that the budget optimization is based on',
                    },
                    'bid_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of bid strategy being used',
                    },
                    'deep_bid_type': {
                        'type': ['null', 'string'],
                        'description': 'Advanced bid type used for optimization',
                    },
                    'optimization_goal': {
                        'type': ['null', 'string'],
                        'description': 'Specific goal to be optimized for',
                    },
                    'split_test_variable': {
                        'type': ['null', 'string'],
                        'description': 'Variable being tested in a split test campaign',
                    },
                    'is_new_structure': {'type': 'boolean', 'description': 'Flag indicating if the campaign uses a new structure'},
                    'create_time': {'type': 'string', 'description': 'Timestamp when the campaign was created'},
                    'modify_time': {'type': 'string', 'description': 'Timestamp when the campaign was last modified'},
                    'roas_bid': {
                        'type': ['null', 'number'],
                        'description': 'Return on ad spend goal set for the campaign',
                    },
                    'is_smart_performance_campaign': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if the campaign uses smart performance',
                    },
                    'is_search_campaign': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if the campaign is a search campaign',
                    },
                    'app_promotion_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of app promotion being used',
                    },
                    'rf_campaign_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of reach and frequency campaign',
                    },
                    'disable_skan_campaign': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if SKAN campaign is disabled',
                    },
                    'is_advanced_dedicated_campaign': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if campaign is advanced dedicated',
                    },
                    'rta_id': {
                        'type': ['null', 'string'],
                        'description': 'Real-time API ID',
                    },
                    'campaign_automation_type': {
                        'type': ['null', 'string'],
                        'description': 'Campaign automation type',
                    },
                    'rta_bid_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if RTA bid is enabled',
                    },
                    'rta_product_selection_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if RTA product selection is enabled',
                    },
                },
                'x-airbyte-entity-name': 'campaigns',
                'x-airbyte-stream-name': 'campaigns',
            },
        ),
        EntityDefinition(
            name='ad_groups',
            stream_name='ad_groups',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/adgroup/get/',
                    action=Action.LIST,
                    description='Get ad groups for an advertiser',
                    query_params=['advertiser_id', 'page', 'page_size'],
                    query_params_schema={
                        'advertiser_id': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 1000,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'TikTok ad group',
                                            'properties': {
                                                'adgroup_id': {'type': 'string', 'description': 'The unique identifier of the ad group'},
                                                'campaign_id': {'type': 'string', 'description': 'The unique identifier of the campaign'},
                                                'advertiser_id': {'type': 'string', 'description': 'The unique identifier of the advertiser'},
                                                'adgroup_name': {'type': 'string', 'description': 'The name of the ad group'},
                                                'placement_type': {'type': 'string', 'description': 'The type of ad placement'},
                                                'placements': {
                                                    'type': ['null', 'array'],
                                                    'items': {'type': 'string'},
                                                    'description': 'Information about the ad placements targeted',
                                                },
                                                'budget': {'type': 'number', 'description': 'The allocated budget for the ad group'},
                                                'budget_mode': {'type': 'string', 'description': 'The mode for managing the budget'},
                                                'secondary_status': {'type': 'string', 'description': 'The secondary status of the ad group'},
                                                'operation_status': {'type': 'string', 'description': 'The status of the operation'},
                                                'optimization_goal': {'type': 'string', 'description': 'The goal set for optimization'},
                                                'bid_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of bidding',
                                                },
                                                'bid_price': {'type': 'number', 'description': 'The price set for bidding'},
                                                'promotion_type': {'type': 'string', 'description': 'The type of promotion'},
                                                'creative_material_mode': {'type': 'string', 'description': 'The mode for creative materials'},
                                                'schedule_type': {'type': 'string', 'description': 'The type of scheduling'},
                                                'schedule_start_time': {'type': 'string', 'description': 'The start time of the scheduling'},
                                                'schedule_end_time': {'type': 'string', 'description': 'The end time of the scheduling'},
                                                'create_time': {'type': 'string', 'description': 'Timestamp when the ad group was created'},
                                                'modify_time': {'type': 'string', 'description': 'Timestamp when the ad group was last modified'},
                                                'gender': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The targeted gender for the ad group',
                                                },
                                                'age_groups': {
                                                    'type': ['null', 'array'],
                                                    'items': {'type': 'string'},
                                                    'description': 'The targeted age groups',
                                                },
                                                'languages': {
                                                    'type': ['null', 'array'],
                                                    'items': {'type': 'string'},
                                                    'description': 'The targeted languages',
                                                },
                                                'location_ids': {
                                                    'type': ['null', 'array'],
                                                    'items': {'type': 'string'},
                                                    'description': 'The IDs of targeted locations',
                                                },
                                                'audience_ids': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The IDs of the targeted audience',
                                                },
                                                'excluded_audience_ids': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The IDs of excluded audiences',
                                                },
                                                'interest_category_ids': {
                                                    'type': ['null', 'array'],
                                                    'items': {'type': 'string'},
                                                    'description': 'The IDs of interest categories for targeting',
                                                },
                                                'interest_keyword_ids': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The IDs of interest keywords for targeting',
                                                },
                                                'pixel_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The ID of the pixel used for tracking',
                                                },
                                                'deep_bid_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of deep bid strategy',
                                                },
                                                'deep_cpa_bid': {'type': 'number', 'description': 'The bid amount for deep cost-per-action'},
                                                'conversion_bid_price': {'type': 'number', 'description': 'The bid price for conversions'},
                                                'billing_event': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The event used for billing',
                                                },
                                                'pacing': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Information about the pacing settings',
                                                },
                                                'dayparting': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Information about dayparting settings',
                                                },
                                                'frequency': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The frequency of ad display',
                                                },
                                                'frequency_schedule': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The schedule for frequency capping',
                                                },
                                                'is_new_structure': {'type': 'boolean', 'description': 'Flag indicating if the ad group follows a new structure'},
                                                'is_smart_performance_campaign': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if smart performance campaign',
                                                },
                                                'app_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The unique identifier of the app',
                                                },
                                                'app_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of the associated app',
                                                },
                                                'app_download_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The URL for downloading the associated app',
                                                },
                                                'optimization_event': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The event used for optimization',
                                                },
                                                'secondary_optimization_event': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Additional event used for optimization',
                                                },
                                                'conversion_window': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The window for tracking conversions',
                                                },
                                                'comment_disabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if comments are disabled',
                                                },
                                                'video_download_disabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if video downloads are disabled',
                                                },
                                                'share_disabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if sharing is disabled',
                                                },
                                                'auto_targeting_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if auto-targeting is enabled',
                                                },
                                                'is_hfss': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if high-frequency short sequences are included',
                                                },
                                                'search_result_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if search results are enabled',
                                                },
                                                'inventory_filter_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if inventory filter is enabled',
                                                },
                                                'skip_learning_phase': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if the learning phase is skipped',
                                                },
                                                'brand_safety_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of brand safety measures',
                                                },
                                                'brand_safety_partner': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Information about the brand safety partners',
                                                },
                                                'campaign_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The name of the campaign',
                                                },
                                                'campaign_automation_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Campaign automation type',
                                                },
                                                'bid_display_mode': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The display mode for bidding',
                                                },
                                                'scheduled_budget': {
                                                    'type': ['null', 'number'],
                                                    'description': 'The budget allocated for scheduling',
                                                },
                                                'category_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The ID of the category',
                                                },
                                                'feed_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of feed used',
                                                },
                                                'delivery_mode': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The mode for delivery',
                                                },
                                                'ios14_quota_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of iOS 14 quota',
                                                },
                                                'spending_power': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Spending power targeted',
                                                },
                                                'next_day_retention': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Next day retention information',
                                                },
                                                'rf_purchased_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Type of purchased results',
                                                },
                                                'rf_estimated_cpr': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Estimated cost per result',
                                                },
                                                'rf_estimated_frequency': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Estimated frequency of results',
                                                },
                                                'purchased_impression': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Purchased impressions',
                                                },
                                                'purchased_reach': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Purchased reach',
                                                },
                                                'actions': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Information about the actions',
                                                },
                                                'network_types': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The types of networks targeted',
                                                },
                                                'operating_systems': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The targeted operating systems',
                                                },
                                                'device_model_ids': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The IDs of targeted device models',
                                                },
                                                'device_price_ranges': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The price ranges for devices',
                                                },
                                                'included_custom_actions': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Custom actions that are included',
                                                },
                                                'excluded_custom_actions': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Custom actions that are excluded',
                                                },
                                                'category_exclusion_ids': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The IDs of excluded categories',
                                                },
                                                'contextual_tag_ids': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The IDs of contextual tags',
                                                },
                                                'zipcode_ids': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The IDs of targeted ZIP codes',
                                                },
                                                'household_income': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The targeted household income groups',
                                                },
                                                'isp_ids': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The IDs of targeted ISPs',
                                                },
                                                'schedule_infos': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Information about scheduling',
                                                },
                                                'statistic_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of statistics being tracked',
                                                },
                                                'keywords': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Keywords associated with the ad group',
                                                },
                                                'adgroup_app_profile_page_state': {
                                                    'type': ['null', 'string'],
                                                    'description': 'State of the app profile page',
                                                },
                                                'automated_keywords_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if automated keywords are enabled',
                                                },
                                                'smart_audience_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if smart audience is enabled',
                                                },
                                                'smart_interest_behavior_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if smart interest behavior is enabled',
                                                },
                                                'vbo_window': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Value-based optimization window',
                                                },
                                                'deep_funnel_optimization_status': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Deep funnel optimization status',
                                                },
                                                'deep_funnel_event_source': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Deep funnel event source',
                                                },
                                                'deep_funnel_event_source_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Deep funnel event source ID',
                                                },
                                                'deep_funnel_optimization_event': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Deep funnel optimization event',
                                                },
                                                'custom_conversion_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Custom conversion ID',
                                                },
                                                'app_config': {
                                                    'type': ['null', 'object'],
                                                    'description': 'App configuration',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'ad_groups',
                                            'x-airbyte-stream-name': 'ad_groups',
                                        },
                                    },
                                    'page_info': {
                                        'type': 'object',
                                        'properties': {
                                            'total_number': {'type': 'integer'},
                                            'page': {'type': 'integer'},
                                            'page_size': {'type': 'integer'},
                                            'total_page': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    meta_extractor={'page_info': '$.data.page_info'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'TikTok ad group',
                'properties': {
                    'adgroup_id': {'type': 'string', 'description': 'The unique identifier of the ad group'},
                    'campaign_id': {'type': 'string', 'description': 'The unique identifier of the campaign'},
                    'advertiser_id': {'type': 'string', 'description': 'The unique identifier of the advertiser'},
                    'adgroup_name': {'type': 'string', 'description': 'The name of the ad group'},
                    'placement_type': {'type': 'string', 'description': 'The type of ad placement'},
                    'placements': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'Information about the ad placements targeted',
                    },
                    'budget': {'type': 'number', 'description': 'The allocated budget for the ad group'},
                    'budget_mode': {'type': 'string', 'description': 'The mode for managing the budget'},
                    'secondary_status': {'type': 'string', 'description': 'The secondary status of the ad group'},
                    'operation_status': {'type': 'string', 'description': 'The status of the operation'},
                    'optimization_goal': {'type': 'string', 'description': 'The goal set for optimization'},
                    'bid_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of bidding',
                    },
                    'bid_price': {'type': 'number', 'description': 'The price set for bidding'},
                    'promotion_type': {'type': 'string', 'description': 'The type of promotion'},
                    'creative_material_mode': {'type': 'string', 'description': 'The mode for creative materials'},
                    'schedule_type': {'type': 'string', 'description': 'The type of scheduling'},
                    'schedule_start_time': {'type': 'string', 'description': 'The start time of the scheduling'},
                    'schedule_end_time': {'type': 'string', 'description': 'The end time of the scheduling'},
                    'create_time': {'type': 'string', 'description': 'Timestamp when the ad group was created'},
                    'modify_time': {'type': 'string', 'description': 'Timestamp when the ad group was last modified'},
                    'gender': {
                        'type': ['null', 'string'],
                        'description': 'The targeted gender for the ad group',
                    },
                    'age_groups': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'The targeted age groups',
                    },
                    'languages': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'The targeted languages',
                    },
                    'location_ids': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'The IDs of targeted locations',
                    },
                    'audience_ids': {
                        'type': ['null', 'array'],
                        'description': 'The IDs of the targeted audience',
                    },
                    'excluded_audience_ids': {
                        'type': ['null', 'array'],
                        'description': 'The IDs of excluded audiences',
                    },
                    'interest_category_ids': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'The IDs of interest categories for targeting',
                    },
                    'interest_keyword_ids': {
                        'type': ['null', 'array'],
                        'description': 'The IDs of interest keywords for targeting',
                    },
                    'pixel_id': {
                        'type': ['null', 'string'],
                        'description': 'The ID of the pixel used for tracking',
                    },
                    'deep_bid_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of deep bid strategy',
                    },
                    'deep_cpa_bid': {'type': 'number', 'description': 'The bid amount for deep cost-per-action'},
                    'conversion_bid_price': {'type': 'number', 'description': 'The bid price for conversions'},
                    'billing_event': {
                        'type': ['null', 'string'],
                        'description': 'The event used for billing',
                    },
                    'pacing': {
                        'type': ['null', 'string'],
                        'description': 'Information about the pacing settings',
                    },
                    'dayparting': {
                        'type': ['null', 'string'],
                        'description': 'Information about dayparting settings',
                    },
                    'frequency': {
                        'type': ['null', 'integer'],
                        'description': 'The frequency of ad display',
                    },
                    'frequency_schedule': {
                        'type': ['null', 'integer'],
                        'description': 'The schedule for frequency capping',
                    },
                    'is_new_structure': {'type': 'boolean', 'description': 'Flag indicating if the ad group follows a new structure'},
                    'is_smart_performance_campaign': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if smart performance campaign',
                    },
                    'app_id': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier of the app',
                    },
                    'app_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of the associated app',
                    },
                    'app_download_url': {
                        'type': ['null', 'string'],
                        'description': 'The URL for downloading the associated app',
                    },
                    'optimization_event': {
                        'type': ['null', 'string'],
                        'description': 'The event used for optimization',
                    },
                    'secondary_optimization_event': {
                        'type': ['null', 'string'],
                        'description': 'Additional event used for optimization',
                    },
                    'conversion_window': {
                        'type': ['null', 'string'],
                        'description': 'The window for tracking conversions',
                    },
                    'comment_disabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if comments are disabled',
                    },
                    'video_download_disabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if video downloads are disabled',
                    },
                    'share_disabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if sharing is disabled',
                    },
                    'auto_targeting_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if auto-targeting is enabled',
                    },
                    'is_hfss': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if high-frequency short sequences are included',
                    },
                    'search_result_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if search results are enabled',
                    },
                    'inventory_filter_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if inventory filter is enabled',
                    },
                    'skip_learning_phase': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if the learning phase is skipped',
                    },
                    'brand_safety_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of brand safety measures',
                    },
                    'brand_safety_partner': {
                        'type': ['null', 'string'],
                        'description': 'Information about the brand safety partners',
                    },
                    'campaign_name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the campaign',
                    },
                    'campaign_automation_type': {
                        'type': ['null', 'string'],
                        'description': 'Campaign automation type',
                    },
                    'bid_display_mode': {
                        'type': ['null', 'string'],
                        'description': 'The display mode for bidding',
                    },
                    'scheduled_budget': {
                        'type': ['null', 'number'],
                        'description': 'The budget allocated for scheduling',
                    },
                    'category_id': {
                        'type': ['null', 'string'],
                        'description': 'The ID of the category',
                    },
                    'feed_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of feed used',
                    },
                    'delivery_mode': {
                        'type': ['null', 'string'],
                        'description': 'The mode for delivery',
                    },
                    'ios14_quota_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of iOS 14 quota',
                    },
                    'spending_power': {
                        'type': ['null', 'string'],
                        'description': 'Spending power targeted',
                    },
                    'next_day_retention': {
                        'type': ['null', 'number'],
                        'description': 'Next day retention information',
                    },
                    'rf_purchased_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of purchased results',
                    },
                    'rf_estimated_cpr': {
                        'type': ['null', 'number'],
                        'description': 'Estimated cost per result',
                    },
                    'rf_estimated_frequency': {
                        'type': ['null', 'number'],
                        'description': 'Estimated frequency of results',
                    },
                    'purchased_impression': {
                        'type': ['null', 'number'],
                        'description': 'Purchased impressions',
                    },
                    'purchased_reach': {
                        'type': ['null', 'number'],
                        'description': 'Purchased reach',
                    },
                    'actions': {
                        'type': ['null', 'array'],
                        'description': 'Information about the actions',
                    },
                    'network_types': {
                        'type': ['null', 'array'],
                        'description': 'The types of networks targeted',
                    },
                    'operating_systems': {
                        'type': ['null', 'array'],
                        'description': 'The targeted operating systems',
                    },
                    'device_model_ids': {
                        'type': ['null', 'array'],
                        'description': 'The IDs of targeted device models',
                    },
                    'device_price_ranges': {
                        'type': ['null', 'array'],
                        'description': 'The price ranges for devices',
                    },
                    'included_custom_actions': {
                        'type': ['null', 'array'],
                        'description': 'Custom actions that are included',
                    },
                    'excluded_custom_actions': {
                        'type': ['null', 'array'],
                        'description': 'Custom actions that are excluded',
                    },
                    'category_exclusion_ids': {
                        'type': ['null', 'array'],
                        'description': 'The IDs of excluded categories',
                    },
                    'contextual_tag_ids': {
                        'type': ['null', 'array'],
                        'description': 'The IDs of contextual tags',
                    },
                    'zipcode_ids': {
                        'type': ['null', 'array'],
                        'description': 'The IDs of targeted ZIP codes',
                    },
                    'household_income': {
                        'type': ['null', 'array'],
                        'description': 'The targeted household income groups',
                    },
                    'isp_ids': {
                        'type': ['null', 'array'],
                        'description': 'The IDs of targeted ISPs',
                    },
                    'schedule_infos': {
                        'type': ['null', 'array'],
                        'description': 'Information about scheduling',
                    },
                    'statistic_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of statistics being tracked',
                    },
                    'keywords': {
                        'type': ['null', 'string'],
                        'description': 'Keywords associated with the ad group',
                    },
                    'adgroup_app_profile_page_state': {
                        'type': ['null', 'string'],
                        'description': 'State of the app profile page',
                    },
                    'automated_keywords_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if automated keywords are enabled',
                    },
                    'smart_audience_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if smart audience is enabled',
                    },
                    'smart_interest_behavior_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if smart interest behavior is enabled',
                    },
                    'vbo_window': {
                        'type': ['null', 'string'],
                        'description': 'Value-based optimization window',
                    },
                    'deep_funnel_optimization_status': {
                        'type': ['null', 'string'],
                        'description': 'Deep funnel optimization status',
                    },
                    'deep_funnel_event_source': {
                        'type': ['null', 'string'],
                        'description': 'Deep funnel event source',
                    },
                    'deep_funnel_event_source_id': {
                        'type': ['null', 'string'],
                        'description': 'Deep funnel event source ID',
                    },
                    'deep_funnel_optimization_event': {
                        'type': ['null', 'string'],
                        'description': 'Deep funnel optimization event',
                    },
                    'custom_conversion_id': {
                        'type': ['null', 'string'],
                        'description': 'Custom conversion ID',
                    },
                    'app_config': {
                        'type': ['null', 'object'],
                        'description': 'App configuration',
                    },
                },
                'x-airbyte-entity-name': 'ad_groups',
                'x-airbyte-stream-name': 'ad_groups',
            },
        ),
        EntityDefinition(
            name='ads',
            stream_name='ads',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ad/get/',
                    action=Action.LIST,
                    description='Get ads for an advertiser',
                    query_params=['advertiser_id', 'page', 'page_size'],
                    query_params_schema={
                        'advertiser_id': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 1000,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'TikTok ad',
                                            'properties': {
                                                'ad_id': {'type': 'string', 'description': 'The unique identifier of the ad'},
                                                'advertiser_id': {'type': 'string', 'description': 'The unique identifier of the advertiser'},
                                                'campaign_id': {'type': 'string', 'description': 'The unique identifier of the campaign'},
                                                'campaign_name': {'type': 'string', 'description': 'The name of the campaign'},
                                                'adgroup_id': {'type': 'string', 'description': 'The unique identifier of the ad group'},
                                                'adgroup_name': {'type': 'string', 'description': 'The name of the ad group'},
                                                'ad_name': {'type': 'string', 'description': 'The name of the ad'},
                                                'ad_text': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The text content of the ad',
                                                },
                                                'ad_texts': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The text content of the ad in various languages',
                                                },
                                                'ad_format': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The format of the ad',
                                                },
                                                'secondary_status': {'type': 'string', 'description': 'The secondary status of the ad'},
                                                'operation_status': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The operational status of the ad',
                                                },
                                                'call_to_action': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The call-to-action text for the ad',
                                                },
                                                'call_to_action_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The identifier of the call-to-action',
                                                },
                                                'landing_page_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The URL of the landing page for the ad',
                                                },
                                                'landing_page_urls': {
                                                    'type': ['null', 'array'],
                                                    'description': 'The URLs of landing pages for the ad',
                                                },
                                                'display_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The display name of the ad',
                                                },
                                                'profile_image_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The URL of the profile image',
                                                },
                                                'video_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The unique identifier of the video',
                                                },
                                                'image_ids': {
                                                    'type': ['null', 'array'],
                                                    'items': {'type': 'string'},
                                                    'description': 'The unique identifiers of images used in the ad',
                                                },
                                                'image_mode': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The mode of displaying images',
                                                },
                                                'is_aco': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Indicates if the ad is under Automated Creative Optimization',
                                                },
                                                'is_new_structure': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Indicates if the ad is part of a new structure',
                                                },
                                                'creative_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of creative used in the ad',
                                                },
                                                'creative_authorized': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Indicates if the creative is authorized',
                                                },
                                                'identity_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The identifier of the identity',
                                                },
                                                'identity_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of identity',
                                                },
                                                'deeplink': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The deeplink URL for the ad',
                                                },
                                                'deeplink_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of deeplink used',
                                                },
                                                'fallback_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The type of fallback used',
                                                },
                                                'tracking_pixel_id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The unique identifier of the tracking pixel',
                                                },
                                                'impression_tracking_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The URL for tracking ad impressions',
                                                },
                                                'click_tracking_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The URL for tracking ad clicks',
                                                },
                                                'music_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The unique identifier of the music used in the ad',
                                                },
                                                'optimization_event': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The event used for optimization',
                                                },
                                                'vast_moat_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Indicates if VAST MOAT is enabled',
                                                },
                                                'page_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The unique identifier of the page',
                                                },
                                                'viewability_postbid_partner': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Post-bidding partner for viewability',
                                                },
                                                'viewability_vast_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'VAST URL for viewability tracking',
                                                },
                                                'brand_safety_postbid_partner': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Post-bidding partner for brand safety',
                                                },
                                                'brand_safety_vast_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'VAST URL for brand safety tracking',
                                                },
                                                'app_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The name of the mobile app',
                                                },
                                                'playable_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The URL for a playable ad',
                                                },
                                                'card_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The identifier of the card',
                                                },
                                                'carousel_image_labels': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Labels for carousel images',
                                                },
                                                'avatar_icon_web_uri': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The URL of the avatar icon',
                                                },
                                                'campaign_automation_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Campaign automation type',
                                                },
                                                'create_time': {'type': 'string', 'description': 'Timestamp when the ad was created'},
                                                'modify_time': {'type': 'string', 'description': 'Timestamp when the ad was last modified'},
                                            },
                                            'x-airbyte-entity-name': 'ads',
                                            'x-airbyte-stream-name': 'ads',
                                        },
                                    },
                                    'page_info': {
                                        'type': 'object',
                                        'properties': {
                                            'total_number': {'type': 'integer'},
                                            'page': {'type': 'integer'},
                                            'page_size': {'type': 'integer'},
                                            'total_page': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    meta_extractor={'page_info': '$.data.page_info'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'TikTok ad',
                'properties': {
                    'ad_id': {'type': 'string', 'description': 'The unique identifier of the ad'},
                    'advertiser_id': {'type': 'string', 'description': 'The unique identifier of the advertiser'},
                    'campaign_id': {'type': 'string', 'description': 'The unique identifier of the campaign'},
                    'campaign_name': {'type': 'string', 'description': 'The name of the campaign'},
                    'adgroup_id': {'type': 'string', 'description': 'The unique identifier of the ad group'},
                    'adgroup_name': {'type': 'string', 'description': 'The name of the ad group'},
                    'ad_name': {'type': 'string', 'description': 'The name of the ad'},
                    'ad_text': {
                        'type': ['null', 'string'],
                        'description': 'The text content of the ad',
                    },
                    'ad_texts': {
                        'type': ['null', 'array'],
                        'description': 'The text content of the ad in various languages',
                    },
                    'ad_format': {
                        'type': ['null', 'string'],
                        'description': 'The format of the ad',
                    },
                    'secondary_status': {'type': 'string', 'description': 'The secondary status of the ad'},
                    'operation_status': {
                        'type': ['null', 'string'],
                        'description': 'The operational status of the ad',
                    },
                    'call_to_action': {
                        'type': ['null', 'string'],
                        'description': 'The call-to-action text for the ad',
                    },
                    'call_to_action_id': {
                        'type': ['null', 'string'],
                        'description': 'The identifier of the call-to-action',
                    },
                    'landing_page_url': {
                        'type': ['null', 'string'],
                        'description': 'The URL of the landing page for the ad',
                    },
                    'landing_page_urls': {
                        'type': ['null', 'array'],
                        'description': 'The URLs of landing pages for the ad',
                    },
                    'display_name': {
                        'type': ['null', 'string'],
                        'description': 'The display name of the ad',
                    },
                    'profile_image_url': {
                        'type': ['null', 'string'],
                        'description': 'The URL of the profile image',
                    },
                    'video_id': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier of the video',
                    },
                    'image_ids': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'The unique identifiers of images used in the ad',
                    },
                    'image_mode': {
                        'type': ['null', 'string'],
                        'description': 'The mode of displaying images',
                    },
                    'is_aco': {
                        'type': ['null', 'boolean'],
                        'description': 'Indicates if the ad is under Automated Creative Optimization',
                    },
                    'is_new_structure': {
                        'type': ['null', 'boolean'],
                        'description': 'Indicates if the ad is part of a new structure',
                    },
                    'creative_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of creative used in the ad',
                    },
                    'creative_authorized': {
                        'type': ['null', 'boolean'],
                        'description': 'Indicates if the creative is authorized',
                    },
                    'identity_id': {
                        'type': ['null', 'string'],
                        'description': 'The identifier of the identity',
                    },
                    'identity_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of identity',
                    },
                    'deeplink': {
                        'type': ['null', 'string'],
                        'description': 'The deeplink URL for the ad',
                    },
                    'deeplink_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of deeplink used',
                    },
                    'fallback_type': {
                        'type': ['null', 'string'],
                        'description': 'The type of fallback used',
                    },
                    'tracking_pixel_id': {
                        'type': ['null', 'integer'],
                        'description': 'The unique identifier of the tracking pixel',
                    },
                    'impression_tracking_url': {
                        'type': ['null', 'string'],
                        'description': 'The URL for tracking ad impressions',
                    },
                    'click_tracking_url': {
                        'type': ['null', 'string'],
                        'description': 'The URL for tracking ad clicks',
                    },
                    'music_id': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier of the music used in the ad',
                    },
                    'optimization_event': {
                        'type': ['null', 'string'],
                        'description': 'The event used for optimization',
                    },
                    'vast_moat_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Indicates if VAST MOAT is enabled',
                    },
                    'page_id': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier of the page',
                    },
                    'viewability_postbid_partner': {
                        'type': ['null', 'string'],
                        'description': 'Post-bidding partner for viewability',
                    },
                    'viewability_vast_url': {
                        'type': ['null', 'string'],
                        'description': 'VAST URL for viewability tracking',
                    },
                    'brand_safety_postbid_partner': {
                        'type': ['null', 'string'],
                        'description': 'Post-bidding partner for brand safety',
                    },
                    'brand_safety_vast_url': {
                        'type': ['null', 'string'],
                        'description': 'VAST URL for brand safety tracking',
                    },
                    'app_name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the mobile app',
                    },
                    'playable_url': {
                        'type': ['null', 'string'],
                        'description': 'The URL for a playable ad',
                    },
                    'card_id': {
                        'type': ['null', 'string'],
                        'description': 'The identifier of the card',
                    },
                    'carousel_image_labels': {
                        'type': ['null', 'array'],
                        'description': 'Labels for carousel images',
                    },
                    'avatar_icon_web_uri': {
                        'type': ['null', 'string'],
                        'description': 'The URL of the avatar icon',
                    },
                    'campaign_automation_type': {
                        'type': ['null', 'string'],
                        'description': 'Campaign automation type',
                    },
                    'create_time': {'type': 'string', 'description': 'Timestamp when the ad was created'},
                    'modify_time': {'type': 'string', 'description': 'Timestamp when the ad was last modified'},
                },
                'x-airbyte-entity-name': 'ads',
                'x-airbyte-stream-name': 'ads',
            },
        ),
        EntityDefinition(
            name='audiences',
            stream_name='audiences',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/dmp/custom_audience/list/',
                    action=Action.LIST,
                    description='Get custom audiences for an advertiser',
                    query_params=['advertiser_id', 'page', 'page_size'],
                    query_params_schema={
                        'advertiser_id': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'TikTok custom audience',
                                            'properties': {
                                                'audience_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique identifier for the audience',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Name of the audience',
                                                },
                                                'audience_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Type of audience',
                                                },
                                                'cover_num': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Number of audience members covered',
                                                },
                                                'is_valid': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if the audience data is valid',
                                                },
                                                'is_expiring': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if the audience data is expiring soon',
                                                },
                                                'is_creator': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if the audience creator is the user',
                                                },
                                                'shared': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if the audience is shared',
                                                },
                                                'calculate_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Method used to calculate audience data',
                                                },
                                                'create_time': {
                                                    'type': ['null', 'string'],
                                                    'format': 'date-time',
                                                    'description': 'Timestamp when the audience was created',
                                                },
                                                'expired_time': {
                                                    'type': ['null', 'string'],
                                                    'format': 'date-time',
                                                    'description': 'Timestamp when the audience data expires',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'audiences',
                                            'x-airbyte-stream-name': 'audiences',
                                        },
                                    },
                                    'page_info': {
                                        'type': 'object',
                                        'properties': {
                                            'total_number': {'type': 'integer'},
                                            'page': {'type': 'integer'},
                                            'page_size': {'type': 'integer'},
                                            'total_page': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    meta_extractor={'page_info': '$.data.page_info'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'TikTok custom audience',
                'properties': {
                    'audience_id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier for the audience',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the audience',
                    },
                    'audience_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of audience',
                    },
                    'cover_num': {
                        'type': ['null', 'integer'],
                        'description': 'Number of audience members covered',
                    },
                    'is_valid': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if the audience data is valid',
                    },
                    'is_expiring': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if the audience data is expiring soon',
                    },
                    'is_creator': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if the audience creator is the user',
                    },
                    'shared': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if the audience is shared',
                    },
                    'calculate_type': {
                        'type': ['null', 'string'],
                        'description': 'Method used to calculate audience data',
                    },
                    'create_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the audience was created',
                    },
                    'expired_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the audience data expires',
                    },
                },
                'x-airbyte-entity-name': 'audiences',
                'x-airbyte-stream-name': 'audiences',
            },
        ),
        EntityDefinition(
            name='creative_assets_images',
            stream_name='creative_assets_images',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/file/image/ad/search/',
                    action=Action.LIST,
                    description='Search creative asset images for an advertiser',
                    query_params=['advertiser_id', 'page', 'page_size'],
                    query_params_schema={
                        'advertiser_id': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'TikTok creative asset image',
                                            'properties': {
                                                'image_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The unique identifier for the image',
                                                },
                                                'format': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The format type of the image file',
                                                },
                                                'image_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The URL to access the image',
                                                },
                                                'height': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The height dimension of the image',
                                                },
                                                'width': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The width dimension of the image',
                                                },
                                                'signature': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The signature of the image for security',
                                                },
                                                'size': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The size of the image file',
                                                },
                                                'material_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The ID associated with the material',
                                                },
                                                'is_carousel_usable': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if the image can be used in a carousel',
                                                },
                                                'file_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The name of the image file',
                                                },
                                                'create_time': {
                                                    'type': ['null', 'string'],
                                                    'format': 'date-time',
                                                    'description': 'Timestamp when the image was created',
                                                },
                                                'modify_time': {
                                                    'type': ['null', 'string'],
                                                    'format': 'date-time',
                                                    'description': 'Timestamp when the image was last modified',
                                                },
                                                'displayable': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Flag indicating if the image is displayable',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'creative_assets_images',
                                            'x-airbyte-stream-name': 'creative_assets_images',
                                        },
                                    },
                                    'page_info': {
                                        'type': 'object',
                                        'properties': {
                                            'total_number': {'type': 'integer'},
                                            'page': {'type': 'integer'},
                                            'page_size': {'type': 'integer'},
                                            'total_page': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    meta_extractor={'page_info': '$.data.page_info'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'TikTok creative asset image',
                'properties': {
                    'image_id': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier for the image',
                    },
                    'format': {
                        'type': ['null', 'string'],
                        'description': 'The format type of the image file',
                    },
                    'image_url': {
                        'type': ['null', 'string'],
                        'description': 'The URL to access the image',
                    },
                    'height': {
                        'type': ['null', 'integer'],
                        'description': 'The height dimension of the image',
                    },
                    'width': {
                        'type': ['null', 'integer'],
                        'description': 'The width dimension of the image',
                    },
                    'signature': {
                        'type': ['null', 'string'],
                        'description': 'The signature of the image for security',
                    },
                    'size': {
                        'type': ['null', 'integer'],
                        'description': 'The size of the image file',
                    },
                    'material_id': {
                        'type': ['null', 'string'],
                        'description': 'The ID associated with the material',
                    },
                    'is_carousel_usable': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if the image can be used in a carousel',
                    },
                    'file_name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the image file',
                    },
                    'create_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the image was created',
                    },
                    'modify_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the image was last modified',
                    },
                    'displayable': {
                        'type': ['null', 'boolean'],
                        'description': 'Flag indicating if the image is displayable',
                    },
                },
                'x-airbyte-entity-name': 'creative_assets_images',
                'x-airbyte-stream-name': 'creative_assets_images',
            },
        ),
        EntityDefinition(
            name='creative_assets_videos',
            stream_name='creative_assets_videos',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/file/video/ad/search/',
                    action=Action.LIST,
                    description='Search creative asset videos for an advertiser',
                    query_params=['advertiser_id', 'page', 'page_size'],
                    query_params_schema={
                        'advertiser_id': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'TikTok creative asset video',
                                            'properties': {
                                                'video_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'ID of the video',
                                                },
                                                'video_cover_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL for the cover image of the video',
                                                },
                                                'format': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Format of the video file',
                                                },
                                                'preview_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL for previewing the video',
                                                },
                                                'preview_url_expire_time': {
                                                    'type': ['null', 'string'],
                                                    'format': 'date-time',
                                                    'description': 'Timestamp when the preview URL expires',
                                                },
                                                'duration': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Duration of the video in seconds',
                                                },
                                                'height': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Height of the video in pixels',
                                                },
                                                'width': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Width of the video in pixels',
                                                },
                                                'bit_rate': {
                                                    'type': ['null', 'number'],
                                                    'description': 'The bitrate of the video',
                                                },
                                                'signature': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Signature for authenticating the video request',
                                                },
                                                'size': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Size of the video file in bytes',
                                                },
                                                'material_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'ID of the video material',
                                                },
                                                'allowed_placements': {
                                                    'type': ['null', 'array'],
                                                    'items': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'description': 'List of placements where the video can be used',
                                                },
                                                'allow_download': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Indicates if the video can be downloaded',
                                                },
                                                'file_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Name of the video file',
                                                },
                                                'create_time': {
                                                    'type': ['null', 'string'],
                                                    'format': 'date-time',
                                                    'description': 'Timestamp when the video was created',
                                                },
                                                'modify_time': {
                                                    'type': ['null', 'string'],
                                                    'format': 'date-time',
                                                    'description': 'Timestamp when the video was last modified',
                                                },
                                                'displayable': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'Indicates if the video is displayable',
                                                },
                                                'fix_task_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'ID of the fix task for the video',
                                                },
                                                'flaw_types': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Types of flaws detected in the video',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'creative_assets_videos',
                                            'x-airbyte-stream-name': 'creative_assets_videos',
                                        },
                                    },
                                    'page_info': {
                                        'type': 'object',
                                        'properties': {
                                            'total_number': {'type': 'integer'},
                                            'page': {'type': 'integer'},
                                            'page_size': {'type': 'integer'},
                                            'total_page': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    meta_extractor={'page_info': '$.data.page_info'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'TikTok creative asset video',
                'properties': {
                    'video_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the video',
                    },
                    'video_cover_url': {
                        'type': ['null', 'string'],
                        'description': 'URL for the cover image of the video',
                    },
                    'format': {
                        'type': ['null', 'string'],
                        'description': 'Format of the video file',
                    },
                    'preview_url': {
                        'type': ['null', 'string'],
                        'description': 'URL for previewing the video',
                    },
                    'preview_url_expire_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the preview URL expires',
                    },
                    'duration': {
                        'type': ['null', 'number'],
                        'description': 'Duration of the video in seconds',
                    },
                    'height': {
                        'type': ['null', 'integer'],
                        'description': 'Height of the video in pixels',
                    },
                    'width': {
                        'type': ['null', 'integer'],
                        'description': 'Width of the video in pixels',
                    },
                    'bit_rate': {
                        'type': ['null', 'number'],
                        'description': 'The bitrate of the video',
                    },
                    'signature': {
                        'type': ['null', 'string'],
                        'description': 'Signature for authenticating the video request',
                    },
                    'size': {
                        'type': ['null', 'integer'],
                        'description': 'Size of the video file in bytes',
                    },
                    'material_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the video material',
                    },
                    'allowed_placements': {
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'string'],
                        },
                        'description': 'List of placements where the video can be used',
                    },
                    'allow_download': {
                        'type': ['null', 'boolean'],
                        'description': 'Indicates if the video can be downloaded',
                    },
                    'file_name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the video file',
                    },
                    'create_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the video was created',
                    },
                    'modify_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the video was last modified',
                    },
                    'displayable': {
                        'type': ['null', 'boolean'],
                        'description': 'Indicates if the video is displayable',
                    },
                    'fix_task_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the fix task for the video',
                    },
                    'flaw_types': {
                        'type': ['null', 'array'],
                        'description': 'Types of flaws detected in the video',
                    },
                },
                'x-airbyte-entity-name': 'creative_assets_videos',
                'x-airbyte-stream-name': 'creative_assets_videos',
            },
        ),
        EntityDefinition(
            name='advertisers_reports_daily',
            stream_name='advertisers_reports_daily',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/report/integrated/get/:advertisers_reports_daily',
                    path_override=PathOverrideConfig(
                        path='/report/integrated/get/',
                    ),
                    action=Action.LIST,
                    description='Get daily performance reports at the advertiser level',
                    query_params=[
                        'advertiser_id',
                        'service_type',
                        'report_type',
                        'data_level',
                        'dimensions',
                        'metrics',
                        'start_date',
                        'end_date',
                        'page',
                        'page_size',
                    ],
                    query_params_schema={
                        'advertiser_id': {'type': 'string', 'required': True},
                        'service_type': {
                            'type': 'string',
                            'required': True,
                            'default': 'AUCTION',
                        },
                        'report_type': {
                            'type': 'string',
                            'required': True,
                            'default': 'BASIC',
                        },
                        'data_level': {
                            'type': 'string',
                            'required': True,
                            'default': 'AUCTION_ADVERTISER',
                        },
                        'dimensions': {
                            'type': 'string',
                            'required': True,
                            'default': '["advertiser_id", "stat_time_day"]',
                        },
                        'metrics': {
                            'type': 'string',
                            'required': True,
                            'default': '["cash_spend", "voucher_spend", "spend", "cpc", "cpm", "impressions", "clicks", "ctr", "reach", "cost_per_1000_reached", "frequency", "video_play_actions", "video_watched_2s", "video_watched_6s", "average_video_play", "average_video_play_per_user", "video_views_p25", "video_views_p50", "video_views_p75", "video_views_p100", "profile_visits", "likes", "comments", "shares", "follows", "clicks_on_music_disc", "real_time_app_install", "real_time_app_install_cost", "app_install"]',
                        },
                        'start_date': {'type': 'string', 'required': True},
                        'end_date': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 1000,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Daily performance report at the advertiser level',
                                            'properties': {
                                                'advertiser_id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The unique identifier for the advertiser',
                                                },
                                                'stat_time_day': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The date for which the statistical data is recorded',
                                                },
                                                'spend': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Total amount of money spent',
                                                },
                                                'cash_spend': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The amount of money spent in cash',
                                                },
                                                'voucher_spend': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Amount spent using vouchers',
                                                },
                                                'cpc': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per click',
                                                },
                                                'cpm': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per thousand impressions',
                                                },
                                                'impressions': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of times the ad was displayed',
                                                },
                                                'clicks': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of clicks on the ad',
                                                },
                                                'ctr': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Click-through rate',
                                                },
                                                'reach': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Total number of unique users reached',
                                                },
                                                'cost_per_1000_reached': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per 1000 unique users reached',
                                                },
                                                'frequency': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Average number of times each person saw the ad',
                                                },
                                                'video_play_actions': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of video play actions',
                                                },
                                                'video_watched_2s': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched for at least 2 seconds',
                                                },
                                                'video_watched_6s': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched for at least 6 seconds',
                                                },
                                                'average_video_play': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Average video play duration',
                                                },
                                                'average_video_play_per_user': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Average video play duration per user',
                                                },
                                                'video_views_p25': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 25%',
                                                },
                                                'video_views_p50': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 50%',
                                                },
                                                'video_views_p75': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 75%',
                                                },
                                                'video_views_p100': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 100%',
                                                },
                                                'profile_visits': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of profile visits',
                                                },
                                                'likes': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of likes',
                                                },
                                                'comments': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of comments',
                                                },
                                                'shares': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of shares',
                                                },
                                                'follows': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of follows',
                                                },
                                                'clicks_on_music_disc': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of clicks on the music disc',
                                                },
                                                'real_time_app_install': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Real-time app installations',
                                                },
                                                'real_time_app_install_cost': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Cost of real-time app installations',
                                                },
                                                'app_install': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of app installations',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'advertisers_reports_daily',
                                            'x-airbyte-stream-name': 'advertisers_reports_daily',
                                        },
                                    },
                                    'page_info': {
                                        'type': 'object',
                                        'properties': {
                                            'total_number': {'type': 'integer'},
                                            'page': {'type': 'integer'},
                                            'page_size': {'type': 'integer'},
                                            'total_page': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    meta_extractor={'page_info': '$.data.page_info'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Daily performance report at the advertiser level',
                'properties': {
                    'advertiser_id': {
                        'type': ['null', 'integer'],
                        'description': 'The unique identifier for the advertiser',
                    },
                    'stat_time_day': {
                        'type': ['null', 'string'],
                        'description': 'The date for which the statistical data is recorded',
                    },
                    'spend': {
                        'type': ['null', 'string'],
                        'description': 'Total amount of money spent',
                    },
                    'cash_spend': {
                        'type': ['null', 'string'],
                        'description': 'The amount of money spent in cash',
                    },
                    'voucher_spend': {
                        'type': ['null', 'string'],
                        'description': 'Amount spent using vouchers',
                    },
                    'cpc': {
                        'type': ['null', 'string'],
                        'description': 'Cost per click',
                    },
                    'cpm': {
                        'type': ['null', 'string'],
                        'description': 'Cost per thousand impressions',
                    },
                    'impressions': {
                        'type': ['null', 'string'],
                        'description': 'Number of times the ad was displayed',
                    },
                    'clicks': {
                        'type': ['null', 'string'],
                        'description': 'Number of clicks on the ad',
                    },
                    'ctr': {
                        'type': ['null', 'string'],
                        'description': 'Click-through rate',
                    },
                    'reach': {
                        'type': ['null', 'string'],
                        'description': 'Total number of unique users reached',
                    },
                    'cost_per_1000_reached': {
                        'type': ['null', 'string'],
                        'description': 'Cost per 1000 unique users reached',
                    },
                    'frequency': {
                        'type': ['null', 'string'],
                        'description': 'Average number of times each person saw the ad',
                    },
                    'video_play_actions': {
                        'type': ['null', 'number'],
                        'description': 'Number of video play actions',
                    },
                    'video_watched_2s': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched for at least 2 seconds',
                    },
                    'video_watched_6s': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched for at least 6 seconds',
                    },
                    'average_video_play': {
                        'type': ['null', 'number'],
                        'description': 'Average video play duration',
                    },
                    'average_video_play_per_user': {
                        'type': ['null', 'number'],
                        'description': 'Average video play duration per user',
                    },
                    'video_views_p25': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 25%',
                    },
                    'video_views_p50': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 50%',
                    },
                    'video_views_p75': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 75%',
                    },
                    'video_views_p100': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 100%',
                    },
                    'profile_visits': {
                        'type': ['null', 'number'],
                        'description': 'Number of profile visits',
                    },
                    'likes': {
                        'type': ['null', 'number'],
                        'description': 'Number of likes',
                    },
                    'comments': {
                        'type': ['null', 'number'],
                        'description': 'Number of comments',
                    },
                    'shares': {
                        'type': ['null', 'number'],
                        'description': 'Number of shares',
                    },
                    'follows': {
                        'type': ['null', 'number'],
                        'description': 'Number of follows',
                    },
                    'clicks_on_music_disc': {
                        'type': ['null', 'number'],
                        'description': 'Number of clicks on the music disc',
                    },
                    'real_time_app_install': {
                        'type': ['null', 'number'],
                        'description': 'Real-time app installations',
                    },
                    'real_time_app_install_cost': {
                        'type': ['null', 'number'],
                        'description': 'Cost of real-time app installations',
                    },
                    'app_install': {
                        'type': ['null', 'number'],
                        'description': 'Number of app installations',
                    },
                },
                'x-airbyte-entity-name': 'advertisers_reports_daily',
                'x-airbyte-stream-name': 'advertisers_reports_daily',
            },
        ),
        EntityDefinition(
            name='campaigns_reports_daily',
            stream_name='campaigns_reports_daily',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/report/integrated/get/:campaigns_reports_daily',
                    path_override=PathOverrideConfig(
                        path='/report/integrated/get/',
                    ),
                    action=Action.LIST,
                    description='Get daily performance reports at the campaign level',
                    query_params=[
                        'advertiser_id',
                        'service_type',
                        'report_type',
                        'data_level',
                        'dimensions',
                        'metrics',
                        'start_date',
                        'end_date',
                        'page',
                        'page_size',
                    ],
                    query_params_schema={
                        'advertiser_id': {'type': 'string', 'required': True},
                        'service_type': {
                            'type': 'string',
                            'required': True,
                            'default': 'AUCTION',
                        },
                        'report_type': {
                            'type': 'string',
                            'required': True,
                            'default': 'BASIC',
                        },
                        'data_level': {
                            'type': 'string',
                            'required': True,
                            'default': 'AUCTION_CAMPAIGN',
                        },
                        'dimensions': {
                            'type': 'string',
                            'required': True,
                            'default': '["campaign_id", "stat_time_day"]',
                        },
                        'metrics': {
                            'type': 'string',
                            'required': True,
                            'default': '["campaign_name", "spend", "cpc", "cpm", "impressions", "clicks", "ctr", "reach", "cost_per_1000_reached", "frequency", "video_play_actions", "video_watched_2s", "video_watched_6s", "average_video_play", "average_video_play_per_user", "video_views_p25", "video_views_p50", "video_views_p75", "video_views_p100", "profile_visits", "likes", "comments", "shares", "follows", "clicks_on_music_disc", "real_time_app_install", "real_time_app_install_cost", "app_install"]',
                        },
                        'start_date': {'type': 'string', 'required': True},
                        'end_date': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 1000,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Daily performance report at the campaign level',
                                            'properties': {
                                                'campaign_id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The unique identifier for the campaign',
                                                },
                                                'stat_time_day': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The date for which the statistical data is recorded',
                                                },
                                                'campaign_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The name of the marketing campaign',
                                                },
                                                'spend': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Total amount of money spent',
                                                },
                                                'cpc': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per click',
                                                },
                                                'cpm': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per thousand impressions',
                                                },
                                                'impressions': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of times the ad was displayed',
                                                },
                                                'clicks': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of clicks on the ad',
                                                },
                                                'ctr': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Click-through rate',
                                                },
                                                'reach': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Total number of unique users reached',
                                                },
                                                'cost_per_1000_reached': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per 1000 unique users reached',
                                                },
                                                'frequency': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Average number of times each person saw the ad',
                                                },
                                                'video_play_actions': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of video play actions',
                                                },
                                                'video_watched_2s': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched for at least 2 seconds',
                                                },
                                                'video_watched_6s': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched for at least 6 seconds',
                                                },
                                                'average_video_play': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Average video play duration',
                                                },
                                                'average_video_play_per_user': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Average video play duration per user',
                                                },
                                                'video_views_p25': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 25%',
                                                },
                                                'video_views_p50': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 50%',
                                                },
                                                'video_views_p75': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 75%',
                                                },
                                                'video_views_p100': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 100%',
                                                },
                                                'profile_visits': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of profile visits',
                                                },
                                                'likes': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of likes',
                                                },
                                                'comments': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of comments',
                                                },
                                                'shares': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of shares',
                                                },
                                                'follows': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of follows',
                                                },
                                                'clicks_on_music_disc': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of clicks on the music disc',
                                                },
                                                'real_time_app_install': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Real-time app installations',
                                                },
                                                'real_time_app_install_cost': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Cost of real-time app installations',
                                                },
                                                'app_install': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of app installations',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'campaigns_reports_daily',
                                            'x-airbyte-stream-name': 'campaigns_reports_daily',
                                        },
                                    },
                                    'page_info': {
                                        'type': 'object',
                                        'properties': {
                                            'total_number': {'type': 'integer'},
                                            'page': {'type': 'integer'},
                                            'page_size': {'type': 'integer'},
                                            'total_page': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    meta_extractor={'page_info': '$.data.page_info'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Daily performance report at the campaign level',
                'properties': {
                    'campaign_id': {
                        'type': ['null', 'integer'],
                        'description': 'The unique identifier for the campaign',
                    },
                    'stat_time_day': {
                        'type': ['null', 'string'],
                        'description': 'The date for which the statistical data is recorded',
                    },
                    'campaign_name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the marketing campaign',
                    },
                    'spend': {
                        'type': ['null', 'string'],
                        'description': 'Total amount of money spent',
                    },
                    'cpc': {
                        'type': ['null', 'string'],
                        'description': 'Cost per click',
                    },
                    'cpm': {
                        'type': ['null', 'string'],
                        'description': 'Cost per thousand impressions',
                    },
                    'impressions': {
                        'type': ['null', 'string'],
                        'description': 'Number of times the ad was displayed',
                    },
                    'clicks': {
                        'type': ['null', 'string'],
                        'description': 'Number of clicks on the ad',
                    },
                    'ctr': {
                        'type': ['null', 'string'],
                        'description': 'Click-through rate',
                    },
                    'reach': {
                        'type': ['null', 'string'],
                        'description': 'Total number of unique users reached',
                    },
                    'cost_per_1000_reached': {
                        'type': ['null', 'string'],
                        'description': 'Cost per 1000 unique users reached',
                    },
                    'frequency': {
                        'type': ['null', 'string'],
                        'description': 'Average number of times each person saw the ad',
                    },
                    'video_play_actions': {
                        'type': ['null', 'number'],
                        'description': 'Number of video play actions',
                    },
                    'video_watched_2s': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched for at least 2 seconds',
                    },
                    'video_watched_6s': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched for at least 6 seconds',
                    },
                    'average_video_play': {
                        'type': ['null', 'number'],
                        'description': 'Average video play duration',
                    },
                    'average_video_play_per_user': {
                        'type': ['null', 'number'],
                        'description': 'Average video play duration per user',
                    },
                    'video_views_p25': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 25%',
                    },
                    'video_views_p50': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 50%',
                    },
                    'video_views_p75': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 75%',
                    },
                    'video_views_p100': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 100%',
                    },
                    'profile_visits': {
                        'type': ['null', 'number'],
                        'description': 'Number of profile visits',
                    },
                    'likes': {
                        'type': ['null', 'number'],
                        'description': 'Number of likes',
                    },
                    'comments': {
                        'type': ['null', 'number'],
                        'description': 'Number of comments',
                    },
                    'shares': {
                        'type': ['null', 'number'],
                        'description': 'Number of shares',
                    },
                    'follows': {
                        'type': ['null', 'number'],
                        'description': 'Number of follows',
                    },
                    'clicks_on_music_disc': {
                        'type': ['null', 'number'],
                        'description': 'Number of clicks on the music disc',
                    },
                    'real_time_app_install': {
                        'type': ['null', 'number'],
                        'description': 'Real-time app installations',
                    },
                    'real_time_app_install_cost': {
                        'type': ['null', 'number'],
                        'description': 'Cost of real-time app installations',
                    },
                    'app_install': {
                        'type': ['null', 'number'],
                        'description': 'Number of app installations',
                    },
                },
                'x-airbyte-entity-name': 'campaigns_reports_daily',
                'x-airbyte-stream-name': 'campaigns_reports_daily',
            },
        ),
        EntityDefinition(
            name='ad_groups_reports_daily',
            stream_name='ad_groups_reports_daily',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/report/integrated/get/:ad_groups_reports_daily',
                    path_override=PathOverrideConfig(
                        path='/report/integrated/get/',
                    ),
                    action=Action.LIST,
                    description='Get daily performance reports at the ad group level',
                    query_params=[
                        'advertiser_id',
                        'service_type',
                        'report_type',
                        'data_level',
                        'dimensions',
                        'metrics',
                        'start_date',
                        'end_date',
                        'page',
                        'page_size',
                    ],
                    query_params_schema={
                        'advertiser_id': {'type': 'string', 'required': True},
                        'service_type': {
                            'type': 'string',
                            'required': True,
                            'default': 'AUCTION',
                        },
                        'report_type': {
                            'type': 'string',
                            'required': True,
                            'default': 'BASIC',
                        },
                        'data_level': {
                            'type': 'string',
                            'required': True,
                            'default': 'AUCTION_ADGROUP',
                        },
                        'dimensions': {
                            'type': 'string',
                            'required': True,
                            'default': '["adgroup_id", "stat_time_day"]',
                        },
                        'metrics': {
                            'type': 'string',
                            'required': True,
                            'default': '["campaign_name", "campaign_id", "adgroup_name", "placement_type", "spend", "cpc", "cpm", "impressions", "clicks", "ctr", "reach", "cost_per_1000_reached", "conversion", "cost_per_conversion", "conversion_rate", "real_time_conversion", "real_time_cost_per_conversion", "real_time_conversion_rate", "result", "cost_per_result", "result_rate", "real_time_result", "real_time_cost_per_result", "real_time_result_rate", "secondary_goal_result", "cost_per_secondary_goal_result", "secondary_goal_result_rate", "frequency", "video_play_actions", "video_watched_2s", "video_watched_6s", "average_video_play", "average_video_play_per_user", "video_views_p25", "video_views_p50", "video_views_p75", "video_views_p100", "profile_visits", "likes", "comments", "shares", "follows", "clicks_on_music_disc", "real_time_app_install", "real_time_app_install_cost", "app_install"]',
                        },
                        'start_date': {'type': 'string', 'required': True},
                        'end_date': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 1000,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Daily performance report at the ad group level',
                                            'properties': {
                                                'adgroup_id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The unique identifier for the ad group',
                                                },
                                                'stat_time_day': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The date for which the statistical data is recorded',
                                                },
                                                'campaign_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The name of the marketing campaign',
                                                },
                                                'campaign_id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The unique identifier for the campaign',
                                                },
                                                'adgroup_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The name of the ad group',
                                                },
                                                'placement_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Type of ad placement',
                                                },
                                                'spend': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Total amount of money spent',
                                                },
                                                'cpc': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per click',
                                                },
                                                'cpm': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per thousand impressions',
                                                },
                                                'impressions': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of times the ad was displayed',
                                                },
                                                'clicks': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of clicks on the ad',
                                                },
                                                'ctr': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Click-through rate',
                                                },
                                                'reach': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Total number of unique users reached',
                                                },
                                                'cost_per_1000_reached': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per 1000 unique users reached',
                                                },
                                                'conversion': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of conversions',
                                                },
                                                'cost_per_conversion': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per conversion',
                                                },
                                                'conversion_rate': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Rate of conversions',
                                                },
                                                'real_time_conversion': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time conversions',
                                                },
                                                'real_time_cost_per_conversion': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time cost per conversion',
                                                },
                                                'real_time_conversion_rate': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time conversion rate',
                                                },
                                                'result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of results',
                                                },
                                                'cost_per_result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per result',
                                                },
                                                'result_rate': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Rate of results',
                                                },
                                                'real_time_result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time results',
                                                },
                                                'real_time_cost_per_result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time cost per result',
                                                },
                                                'real_time_result_rate': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time result rate',
                                                },
                                                'secondary_goal_result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Results for secondary goals',
                                                },
                                                'cost_per_secondary_goal_result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per secondary goal result',
                                                },
                                                'secondary_goal_result_rate': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Rate of secondary goal results',
                                                },
                                                'frequency': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Average number of times each person saw the ad',
                                                },
                                                'video_play_actions': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of video play actions',
                                                },
                                                'video_watched_2s': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched for at least 2 seconds',
                                                },
                                                'video_watched_6s': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched for at least 6 seconds',
                                                },
                                                'average_video_play': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Average video play duration',
                                                },
                                                'average_video_play_per_user': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Average video play duration per user',
                                                },
                                                'video_views_p25': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 25%',
                                                },
                                                'video_views_p50': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 50%',
                                                },
                                                'video_views_p75': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 75%',
                                                },
                                                'video_views_p100': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 100%',
                                                },
                                                'profile_visits': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of profile visits',
                                                },
                                                'likes': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of likes',
                                                },
                                                'comments': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of comments',
                                                },
                                                'shares': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of shares',
                                                },
                                                'follows': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of follows',
                                                },
                                                'clicks_on_music_disc': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of clicks on the music disc',
                                                },
                                                'real_time_app_install': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Real-time app installations',
                                                },
                                                'real_time_app_install_cost': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Cost of real-time app installations',
                                                },
                                                'app_install': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of app installations',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'ad_groups_reports_daily',
                                            'x-airbyte-stream-name': 'ad_groups_reports_daily',
                                        },
                                    },
                                    'page_info': {
                                        'type': 'object',
                                        'properties': {
                                            'total_number': {'type': 'integer'},
                                            'page': {'type': 'integer'},
                                            'page_size': {'type': 'integer'},
                                            'total_page': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    meta_extractor={'page_info': '$.data.page_info'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Daily performance report at the ad group level',
                'properties': {
                    'adgroup_id': {
                        'type': ['null', 'integer'],
                        'description': 'The unique identifier for the ad group',
                    },
                    'stat_time_day': {
                        'type': ['null', 'string'],
                        'description': 'The date for which the statistical data is recorded',
                    },
                    'campaign_name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the marketing campaign',
                    },
                    'campaign_id': {
                        'type': ['null', 'integer'],
                        'description': 'The unique identifier for the campaign',
                    },
                    'adgroup_name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the ad group',
                    },
                    'placement_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of ad placement',
                    },
                    'spend': {
                        'type': ['null', 'string'],
                        'description': 'Total amount of money spent',
                    },
                    'cpc': {
                        'type': ['null', 'string'],
                        'description': 'Cost per click',
                    },
                    'cpm': {
                        'type': ['null', 'string'],
                        'description': 'Cost per thousand impressions',
                    },
                    'impressions': {
                        'type': ['null', 'string'],
                        'description': 'Number of times the ad was displayed',
                    },
                    'clicks': {
                        'type': ['null', 'string'],
                        'description': 'Number of clicks on the ad',
                    },
                    'ctr': {
                        'type': ['null', 'string'],
                        'description': 'Click-through rate',
                    },
                    'reach': {
                        'type': ['null', 'string'],
                        'description': 'Total number of unique users reached',
                    },
                    'cost_per_1000_reached': {
                        'type': ['null', 'string'],
                        'description': 'Cost per 1000 unique users reached',
                    },
                    'conversion': {
                        'type': ['null', 'string'],
                        'description': 'Number of conversions',
                    },
                    'cost_per_conversion': {
                        'type': ['null', 'string'],
                        'description': 'Cost per conversion',
                    },
                    'conversion_rate': {
                        'type': ['null', 'string'],
                        'description': 'Rate of conversions',
                    },
                    'real_time_conversion': {
                        'type': ['null', 'string'],
                        'description': 'Real-time conversions',
                    },
                    'real_time_cost_per_conversion': {
                        'type': ['null', 'string'],
                        'description': 'Real-time cost per conversion',
                    },
                    'real_time_conversion_rate': {
                        'type': ['null', 'string'],
                        'description': 'Real-time conversion rate',
                    },
                    'result': {
                        'type': ['null', 'string'],
                        'description': 'Number of results',
                    },
                    'cost_per_result': {
                        'type': ['null', 'string'],
                        'description': 'Cost per result',
                    },
                    'result_rate': {
                        'type': ['null', 'string'],
                        'description': 'Rate of results',
                    },
                    'real_time_result': {
                        'type': ['null', 'string'],
                        'description': 'Real-time results',
                    },
                    'real_time_cost_per_result': {
                        'type': ['null', 'string'],
                        'description': 'Real-time cost per result',
                    },
                    'real_time_result_rate': {
                        'type': ['null', 'string'],
                        'description': 'Real-time result rate',
                    },
                    'secondary_goal_result': {
                        'type': ['null', 'string'],
                        'description': 'Results for secondary goals',
                    },
                    'cost_per_secondary_goal_result': {
                        'type': ['null', 'string'],
                        'description': 'Cost per secondary goal result',
                    },
                    'secondary_goal_result_rate': {
                        'type': ['null', 'string'],
                        'description': 'Rate of secondary goal results',
                    },
                    'frequency': {
                        'type': ['null', 'string'],
                        'description': 'Average number of times each person saw the ad',
                    },
                    'video_play_actions': {
                        'type': ['null', 'number'],
                        'description': 'Number of video play actions',
                    },
                    'video_watched_2s': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched for at least 2 seconds',
                    },
                    'video_watched_6s': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched for at least 6 seconds',
                    },
                    'average_video_play': {
                        'type': ['null', 'number'],
                        'description': 'Average video play duration',
                    },
                    'average_video_play_per_user': {
                        'type': ['null', 'number'],
                        'description': 'Average video play duration per user',
                    },
                    'video_views_p25': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 25%',
                    },
                    'video_views_p50': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 50%',
                    },
                    'video_views_p75': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 75%',
                    },
                    'video_views_p100': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 100%',
                    },
                    'profile_visits': {
                        'type': ['null', 'number'],
                        'description': 'Number of profile visits',
                    },
                    'likes': {
                        'type': ['null', 'number'],
                        'description': 'Number of likes',
                    },
                    'comments': {
                        'type': ['null', 'number'],
                        'description': 'Number of comments',
                    },
                    'shares': {
                        'type': ['null', 'number'],
                        'description': 'Number of shares',
                    },
                    'follows': {
                        'type': ['null', 'number'],
                        'description': 'Number of follows',
                    },
                    'clicks_on_music_disc': {
                        'type': ['null', 'number'],
                        'description': 'Number of clicks on the music disc',
                    },
                    'real_time_app_install': {
                        'type': ['null', 'number'],
                        'description': 'Real-time app installations',
                    },
                    'real_time_app_install_cost': {
                        'type': ['null', 'number'],
                        'description': 'Cost of real-time app installations',
                    },
                    'app_install': {
                        'type': ['null', 'number'],
                        'description': 'Number of app installations',
                    },
                },
                'x-airbyte-entity-name': 'ad_groups_reports_daily',
                'x-airbyte-stream-name': 'ad_groups_reports_daily',
            },
        ),
        EntityDefinition(
            name='ads_reports_daily',
            stream_name='ads_reports_daily',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/report/integrated/get/:ads_reports_daily',
                    path_override=PathOverrideConfig(
                        path='/report/integrated/get/',
                    ),
                    action=Action.LIST,
                    description='Get daily performance reports at the ad level',
                    query_params=[
                        'advertiser_id',
                        'service_type',
                        'report_type',
                        'data_level',
                        'dimensions',
                        'metrics',
                        'start_date',
                        'end_date',
                        'page',
                        'page_size',
                    ],
                    query_params_schema={
                        'advertiser_id': {'type': 'string', 'required': True},
                        'service_type': {
                            'type': 'string',
                            'required': True,
                            'default': 'AUCTION',
                        },
                        'report_type': {
                            'type': 'string',
                            'required': True,
                            'default': 'BASIC',
                        },
                        'data_level': {
                            'type': 'string',
                            'required': True,
                            'default': 'AUCTION_AD',
                        },
                        'dimensions': {
                            'type': 'string',
                            'required': True,
                            'default': '["ad_id", "stat_time_day"]',
                        },
                        'metrics': {
                            'type': 'string',
                            'required': True,
                            'default': '["campaign_name", "campaign_id", "adgroup_name", "adgroup_id", "ad_name", "ad_text", "placement_type", "spend", "cpc", "cpm", "impressions", "clicks", "ctr", "reach", "cost_per_1000_reached", "conversion", "cost_per_conversion", "conversion_rate", "real_time_conversion", "real_time_cost_per_conversion", "real_time_conversion_rate", "result", "cost_per_result", "result_rate", "real_time_result", "real_time_cost_per_result", "real_time_result_rate", "secondary_goal_result", "cost_per_secondary_goal_result", "secondary_goal_result_rate", "frequency", "video_play_actions", "video_watched_2s", "video_watched_6s", "average_video_play", "average_video_play_per_user", "video_views_p25", "video_views_p50", "video_views_p75", "video_views_p100", "profile_visits", "likes", "comments", "shares", "follows", "clicks_on_music_disc", "real_time_app_install", "real_time_app_install_cost", "app_install"]',
                        },
                        'start_date': {'type': 'string', 'required': True},
                        'end_date': {'type': 'string', 'required': True},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 1000,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'code': {'type': 'integer'},
                            'message': {'type': 'string'},
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'list': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Daily performance report at the ad level',
                                            'properties': {
                                                'ad_id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The unique identifier for the ad',
                                                },
                                                'stat_time_day': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The date for which the statistical data is recorded',
                                                },
                                                'campaign_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The name of the marketing campaign',
                                                },
                                                'campaign_id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The unique identifier for the campaign',
                                                },
                                                'adgroup_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The name of the ad group',
                                                },
                                                'adgroup_id': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'The unique identifier for the ad group',
                                                },
                                                'ad_name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The name of the ad',
                                                },
                                                'ad_text': {
                                                    'type': ['null', 'string'],
                                                    'description': 'The text content of the ad',
                                                },
                                                'placement_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Type of ad placement',
                                                },
                                                'spend': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Total amount of money spent',
                                                },
                                                'cpc': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per click',
                                                },
                                                'cpm': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per thousand impressions',
                                                },
                                                'impressions': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of times the ad was displayed',
                                                },
                                                'clicks': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of clicks on the ad',
                                                },
                                                'ctr': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Click-through rate',
                                                },
                                                'reach': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Total number of unique users reached',
                                                },
                                                'cost_per_1000_reached': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per 1000 unique users reached',
                                                },
                                                'conversion': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of conversions',
                                                },
                                                'cost_per_conversion': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per conversion',
                                                },
                                                'conversion_rate': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Rate of conversions',
                                                },
                                                'real_time_conversion': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time conversions',
                                                },
                                                'real_time_cost_per_conversion': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time cost per conversion',
                                                },
                                                'real_time_conversion_rate': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time conversion rate',
                                                },
                                                'result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Number of results',
                                                },
                                                'cost_per_result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per result',
                                                },
                                                'result_rate': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Rate of results',
                                                },
                                                'real_time_result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time results',
                                                },
                                                'real_time_cost_per_result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time cost per result',
                                                },
                                                'real_time_result_rate': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Real-time result rate',
                                                },
                                                'secondary_goal_result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Results for secondary goals',
                                                },
                                                'cost_per_secondary_goal_result': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cost per secondary goal result',
                                                },
                                                'secondary_goal_result_rate': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Rate of secondary goal results',
                                                },
                                                'frequency': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Average number of times each person saw the ad',
                                                },
                                                'video_play_actions': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of video play actions',
                                                },
                                                'video_watched_2s': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched for at least 2 seconds',
                                                },
                                                'video_watched_6s': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched for at least 6 seconds',
                                                },
                                                'average_video_play': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Average video play duration',
                                                },
                                                'average_video_play_per_user': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Average video play duration per user',
                                                },
                                                'video_views_p25': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 25%',
                                                },
                                                'video_views_p50': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 50%',
                                                },
                                                'video_views_p75': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 75%',
                                                },
                                                'video_views_p100': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of times video was watched to 100%',
                                                },
                                                'profile_visits': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of profile visits',
                                                },
                                                'likes': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of likes',
                                                },
                                                'comments': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of comments',
                                                },
                                                'shares': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of shares',
                                                },
                                                'follows': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of follows',
                                                },
                                                'clicks_on_music_disc': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of clicks on the music disc',
                                                },
                                                'real_time_app_install': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Real-time app installations',
                                                },
                                                'real_time_app_install_cost': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Cost of real-time app installations',
                                                },
                                                'app_install': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Number of app installations',
                                                },
                                            },
                                            'x-airbyte-entity-name': 'ads_reports_daily',
                                            'x-airbyte-stream-name': 'ads_reports_daily',
                                        },
                                    },
                                    'page_info': {
                                        'type': 'object',
                                        'properties': {
                                            'total_number': {'type': 'integer'},
                                            'page': {'type': 'integer'},
                                            'page_size': {'type': 'integer'},
                                            'total_page': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.list',
                    meta_extractor={'page_info': '$.data.page_info'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Daily performance report at the ad level',
                'properties': {
                    'ad_id': {
                        'type': ['null', 'integer'],
                        'description': 'The unique identifier for the ad',
                    },
                    'stat_time_day': {
                        'type': ['null', 'string'],
                        'description': 'The date for which the statistical data is recorded',
                    },
                    'campaign_name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the marketing campaign',
                    },
                    'campaign_id': {
                        'type': ['null', 'integer'],
                        'description': 'The unique identifier for the campaign',
                    },
                    'adgroup_name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the ad group',
                    },
                    'adgroup_id': {
                        'type': ['null', 'integer'],
                        'description': 'The unique identifier for the ad group',
                    },
                    'ad_name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the ad',
                    },
                    'ad_text': {
                        'type': ['null', 'string'],
                        'description': 'The text content of the ad',
                    },
                    'placement_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of ad placement',
                    },
                    'spend': {
                        'type': ['null', 'string'],
                        'description': 'Total amount of money spent',
                    },
                    'cpc': {
                        'type': ['null', 'string'],
                        'description': 'Cost per click',
                    },
                    'cpm': {
                        'type': ['null', 'string'],
                        'description': 'Cost per thousand impressions',
                    },
                    'impressions': {
                        'type': ['null', 'string'],
                        'description': 'Number of times the ad was displayed',
                    },
                    'clicks': {
                        'type': ['null', 'string'],
                        'description': 'Number of clicks on the ad',
                    },
                    'ctr': {
                        'type': ['null', 'string'],
                        'description': 'Click-through rate',
                    },
                    'reach': {
                        'type': ['null', 'string'],
                        'description': 'Total number of unique users reached',
                    },
                    'cost_per_1000_reached': {
                        'type': ['null', 'string'],
                        'description': 'Cost per 1000 unique users reached',
                    },
                    'conversion': {
                        'type': ['null', 'string'],
                        'description': 'Number of conversions',
                    },
                    'cost_per_conversion': {
                        'type': ['null', 'string'],
                        'description': 'Cost per conversion',
                    },
                    'conversion_rate': {
                        'type': ['null', 'string'],
                        'description': 'Rate of conversions',
                    },
                    'real_time_conversion': {
                        'type': ['null', 'string'],
                        'description': 'Real-time conversions',
                    },
                    'real_time_cost_per_conversion': {
                        'type': ['null', 'string'],
                        'description': 'Real-time cost per conversion',
                    },
                    'real_time_conversion_rate': {
                        'type': ['null', 'string'],
                        'description': 'Real-time conversion rate',
                    },
                    'result': {
                        'type': ['null', 'string'],
                        'description': 'Number of results',
                    },
                    'cost_per_result': {
                        'type': ['null', 'string'],
                        'description': 'Cost per result',
                    },
                    'result_rate': {
                        'type': ['null', 'string'],
                        'description': 'Rate of results',
                    },
                    'real_time_result': {
                        'type': ['null', 'string'],
                        'description': 'Real-time results',
                    },
                    'real_time_cost_per_result': {
                        'type': ['null', 'string'],
                        'description': 'Real-time cost per result',
                    },
                    'real_time_result_rate': {
                        'type': ['null', 'string'],
                        'description': 'Real-time result rate',
                    },
                    'secondary_goal_result': {
                        'type': ['null', 'string'],
                        'description': 'Results for secondary goals',
                    },
                    'cost_per_secondary_goal_result': {
                        'type': ['null', 'string'],
                        'description': 'Cost per secondary goal result',
                    },
                    'secondary_goal_result_rate': {
                        'type': ['null', 'string'],
                        'description': 'Rate of secondary goal results',
                    },
                    'frequency': {
                        'type': ['null', 'string'],
                        'description': 'Average number of times each person saw the ad',
                    },
                    'video_play_actions': {
                        'type': ['null', 'number'],
                        'description': 'Number of video play actions',
                    },
                    'video_watched_2s': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched for at least 2 seconds',
                    },
                    'video_watched_6s': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched for at least 6 seconds',
                    },
                    'average_video_play': {
                        'type': ['null', 'number'],
                        'description': 'Average video play duration',
                    },
                    'average_video_play_per_user': {
                        'type': ['null', 'number'],
                        'description': 'Average video play duration per user',
                    },
                    'video_views_p25': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 25%',
                    },
                    'video_views_p50': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 50%',
                    },
                    'video_views_p75': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 75%',
                    },
                    'video_views_p100': {
                        'type': ['null', 'number'],
                        'description': 'Number of times video was watched to 100%',
                    },
                    'profile_visits': {
                        'type': ['null', 'number'],
                        'description': 'Number of profile visits',
                    },
                    'likes': {
                        'type': ['null', 'number'],
                        'description': 'Number of likes',
                    },
                    'comments': {
                        'type': ['null', 'number'],
                        'description': 'Number of comments',
                    },
                    'shares': {
                        'type': ['null', 'number'],
                        'description': 'Number of shares',
                    },
                    'follows': {
                        'type': ['null', 'number'],
                        'description': 'Number of follows',
                    },
                    'clicks_on_music_disc': {
                        'type': ['null', 'number'],
                        'description': 'Number of clicks on the music disc',
                    },
                    'real_time_app_install': {
                        'type': ['null', 'number'],
                        'description': 'Real-time app installations',
                    },
                    'real_time_app_install_cost': {
                        'type': ['null', 'number'],
                        'description': 'Cost of real-time app installations',
                    },
                    'app_install': {
                        'type': ['null', 'number'],
                        'description': 'Number of app installations',
                    },
                },
                'x-airbyte-entity-name': 'ads_reports_daily',
                'x-airbyte-stream-name': 'ads_reports_daily',
            },
        ),
    ],
    search_field_paths={
        'advertisers': [
            'address',
            'advertiser_account_type',
            'advertiser_id',
            'balance',
            'brand',
            'cellphone_number',
            'company',
            'contacter',
            'country',
            'create_time',
            'currency',
            'description',
            'display_timezone',
            'email',
            'industry',
            'language',
            'license_city',
            'license_no',
            'license_province',
            'license_url',
            'name',
            'promotion_area',
            'promotion_center_city',
            'promotion_center_province',
            'rejection_reason',
            'role',
            'status',
            'telephone_number',
            'timezone',
        ],
        'campaigns': [
            'advertiser_id',
            'app_promotion_type',
            'bid_type',
            'budget',
            'budget_mode',
            'budget_optimize_on',
            'campaign_id',
            'campaign_name',
            'campaign_type',
            'create_time',
            'deep_bid_type',
            'is_new_structure',
            'is_search_campaign',
            'is_smart_performance_campaign',
            'modify_time',
            'objective',
            'objective_type',
            'operation_status',
            'optimization_goal',
            'rf_campaign_type',
            'roas_bid',
            'secondary_status',
            'split_test_variable',
        ],
        'ad_groups': [
            'adgroup_id',
            'adgroup_name',
            'advertiser_id',
            'budget',
            'budget_mode',
            'campaign_id',
            'create_time',
            'modify_time',
            'operation_status',
            'optimization_goal',
            'placement_type',
            'promotion_type',
            'secondary_status',
        ],
        'ads': [
            'ad_format',
            'ad_id',
            'ad_name',
            'ad_text',
            'adgroup_id',
            'adgroup_name',
            'advertiser_id',
            'campaign_id',
            'campaign_name',
            'create_time',
            'landing_page_url',
            'modify_time',
            'operation_status',
            'secondary_status',
            'video_id',
        ],
        'audiences': [
            'audience_id',
            'audience_type',
            'cover_num',
            'create_time',
            'is_valid',
            'name',
            'shared',
        ],
        'creative_assets_images': [
            'create_time',
            'file_name',
            'format',
            'height',
            'image_id',
            'image_url',
            'modify_time',
            'size',
            'width',
        ],
        'creative_assets_videos': [
            'create_time',
            'duration',
            'file_name',
            'format',
            'height',
            'modify_time',
            'size',
            'video_cover_url',
            'video_id',
            'width',
        ],
        'advertisers_reports_daily': [
            'advertiser_id',
            'stat_time_day',
            'spend',
            'cash_spend',
            'voucher_spend',
            'cpc',
            'cpm',
            'impressions',
            'clicks',
            'ctr',
            'reach',
            'cost_per_1000_reached',
            'frequency',
            'video_play_actions',
            'video_watched_2s',
            'video_watched_6s',
            'average_video_play',
            'average_video_play_per_user',
            'video_views_p25',
            'video_views_p50',
            'video_views_p75',
            'video_views_p100',
            'profile_visits',
            'likes',
            'comments',
            'shares',
            'follows',
            'clicks_on_music_disc',
            'real_time_app_install',
            'real_time_app_install_cost',
            'app_install',
        ],
        'campaigns_reports_daily': [
            'campaign_id',
            'stat_time_day',
            'campaign_name',
            'spend',
            'cpc',
            'cpm',
            'impressions',
            'clicks',
            'ctr',
            'reach',
            'cost_per_1000_reached',
            'frequency',
            'video_play_actions',
            'video_watched_2s',
            'video_watched_6s',
            'average_video_play',
            'average_video_play_per_user',
            'video_views_p25',
            'video_views_p50',
            'video_views_p75',
            'video_views_p100',
            'profile_visits',
            'likes',
            'comments',
            'shares',
            'follows',
            'clicks_on_music_disc',
            'real_time_app_install',
            'real_time_app_install_cost',
            'app_install',
        ],
        'ad_groups_reports_daily': [
            'adgroup_id',
            'stat_time_day',
            'campaign_name',
            'campaign_id',
            'adgroup_name',
            'placement_type',
            'spend',
            'cpc',
            'cpm',
            'impressions',
            'clicks',
            'ctr',
            'reach',
            'cost_per_1000_reached',
            'conversion',
            'cost_per_conversion',
            'conversion_rate',
            'real_time_conversion',
            'real_time_cost_per_conversion',
            'real_time_conversion_rate',
            'result',
            'cost_per_result',
            'result_rate',
            'real_time_result',
            'real_time_cost_per_result',
            'real_time_result_rate',
            'secondary_goal_result',
            'cost_per_secondary_goal_result',
            'secondary_goal_result_rate',
            'frequency',
            'video_play_actions',
            'video_watched_2s',
            'video_watched_6s',
            'average_video_play',
            'average_video_play_per_user',
            'video_views_p25',
            'video_views_p50',
            'video_views_p75',
            'video_views_p100',
            'profile_visits',
            'likes',
            'comments',
            'shares',
            'follows',
            'clicks_on_music_disc',
            'real_time_app_install',
            'real_time_app_install_cost',
            'app_install',
        ],
        'ads_reports_daily': [
            'ad_id',
            'stat_time_day',
            'campaign_name',
            'campaign_id',
            'adgroup_name',
            'adgroup_id',
            'ad_name',
            'ad_text',
            'placement_type',
            'spend',
            'cpc',
            'cpm',
            'impressions',
            'clicks',
            'ctr',
            'reach',
            'cost_per_1000_reached',
            'conversion',
            'cost_per_conversion',
            'conversion_rate',
            'real_time_conversion',
            'real_time_cost_per_conversion',
            'real_time_conversion_rate',
            'result',
            'cost_per_result',
            'result_rate',
            'real_time_result',
            'real_time_cost_per_result',
            'real_time_result_rate',
            'secondary_goal_result',
            'cost_per_secondary_goal_result',
            'secondary_goal_result_rate',
            'frequency',
            'video_play_actions',
            'video_watched_2s',
            'video_watched_6s',
            'average_video_play',
            'average_video_play_per_user',
            'video_views_p25',
            'video_views_p50',
            'video_views_p75',
            'video_views_p100',
            'profile_visits',
            'likes',
            'comments',
            'shares',
            'follows',
            'clicks_on_music_disc',
            'real_time_app_install',
            'real_time_app_install_cost',
            'app_install',
        ],
    },
)