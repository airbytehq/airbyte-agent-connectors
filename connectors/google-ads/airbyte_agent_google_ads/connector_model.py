"""
Connector model for google-ads.

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

GoogleAdsConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('253487c0-2246-43ba-a21f-5116b20a2c50'),
    name='google-ads',
    version='1.0.4',
    base_url='https://googleads.googleapis.com',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://www.googleapis.com/oauth2/v3/token',
            'auth_style': 'body',
            'body_format': 'form',
            'additional_headers': {'developer-token': '{{ developer_token }}'},
        },
        user_config_spec=AirbyteAuthConfig(
            title='OAuth2 Authentication',
            type='object',
            required=[
                'client_id',
                'client_secret',
                'refresh_token',
                'developer_token',
            ],
            properties={
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='OAuth2 client ID from Google Cloud Console',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='OAuth2 client secret from Google Cloud Console',
                ),
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='OAuth2 refresh token',
                ),
                'developer_token': AuthConfigFieldSpec(
                    title='Developer Token',
                    description='Google Ads API developer token',
                ),
            },
            auth_mapping={
                'refresh_token': '${refresh_token}',
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
            },
            replication_auth_key_mapping={
                'credentials.client_id': 'client_id',
                'credentials.client_secret': 'client_secret',
                'credentials.refresh_token': 'refresh_token',
                'credentials.developer_token': 'developer_token',
            },
            additional_headers={'developer-token': '{{ developer_token }}'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='accessible_customers',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v20/customers:listAccessibleCustomers',
                    action=Action.LIST,
                    description='Returns resource names of customers directly accessible by the user authenticating the call. No customer_id is required for this endpoint.',
                    response_schema={
                        'type': 'object',
                        'description': 'List of accessible customer resource names',
                        'properties': {
                            'resourceNames': {
                                'type': 'array',
                                'items': {'type': 'string', 'description': 'Resource name of an accessible customer (e.g., customers/1234567890)'},
                                'description': 'Resource names of accessible customers',
                            },
                        },
                    },
                    preferred_for_check=True,
                ),
            },
        ),
        EntityDefinition(
            name='accounts',
            stream_name='accounts',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/googleAds:search',
                    action=Action.LIST,
                    description='Retrieves customer account details using GAQL query.',
                    body_fields=['query', 'pageToken', 'pageSize'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={'query': 'SELECT\n  customer.auto_tagging_enabled,\n  customer.call_reporting_setting.call_conversion_action,\n  customer.call_reporting_setting.call_conversion_reporting_enabled,\n  customer.call_reporting_setting.call_reporting_enabled,\n  customer.conversion_tracking_setting.conversion_tracking_id,\n  customer.conversion_tracking_setting.cross_account_conversion_tracking_id,\n  customer.currency_code,\n  customer.descriptive_name,\n  customer.final_url_suffix,\n  customer.has_partners_badge,\n  customer.id,\n  customer.manager,\n  customer.optimization_score,\n  customer.optimization_score_weight,\n  customer.pay_per_conversion_eligibility_failure_reasons,\n  customer.remarketing_setting.google_global_site_tag,\n  customer.resource_name,\n  customer.test_account,\n  customer.time_zone,\n  customer.tracking_url_template\nFROM customer'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'query': {
                                'type': 'string',
                                'description': 'Google Ads Query Language (GAQL) query',
                                'default': 'SELECT\n  customer.auto_tagging_enabled,\n  customer.call_reporting_setting.call_conversion_action,\n  customer.call_reporting_setting.call_conversion_reporting_enabled,\n  customer.call_reporting_setting.call_reporting_enabled,\n  customer.conversion_tracking_setting.conversion_tracking_id,\n  customer.conversion_tracking_setting.cross_account_conversion_tracking_id,\n  customer.currency_code,\n  customer.descriptive_name,\n  customer.final_url_suffix,\n  customer.has_partners_badge,\n  customer.id,\n  customer.manager,\n  customer.optimization_score,\n  customer.optimization_score_weight,\n  customer.pay_per_conversion_eligibility_failure_reasons,\n  customer.remarketing_setting.google_global_site_tag,\n  customer.resource_name,\n  customer.test_account,\n  customer.time_zone,\n  customer.tracking_url_template\nFROM customer',
                            },
                            'pageToken': {'type': 'string', 'description': 'Token for pagination'},
                            'pageSize': {'type': 'integer', 'description': 'Number of results per page (max 10000)'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Search response containing account data',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Google Ads customer account',
                                    'properties': {
                                        'customer': {
                                            'type': 'object',
                                            'properties': {
                                                'autoTaggingEnabled': {'type': 'boolean', 'description': 'Whether auto-tagging is enabled'},
                                                'callReportingSetting': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'callConversionAction': {'type': 'string'},
                                                        'callConversionReportingEnabled': {'type': 'boolean'},
                                                        'callReportingEnabled': {'type': 'boolean'},
                                                    },
                                                },
                                                'conversionTrackingSetting': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'conversionTrackingId': {'type': 'string'},
                                                        'crossAccountConversionTrackingId': {'type': 'string'},
                                                    },
                                                },
                                                'currencyCode': {'type': 'string', 'description': 'Currency code (e.g., USD)'},
                                                'descriptiveName': {'type': 'string', 'description': 'Account descriptive name'},
                                                'finalUrlSuffix': {'type': 'string'},
                                                'hasPartnersBadge': {'type': 'boolean'},
                                                'id': {'type': 'string', 'description': 'Customer ID'},
                                                'manager': {'type': 'boolean', 'description': 'Whether this is a manager account'},
                                                'optimizationScore': {'type': 'number'},
                                                'optimizationScoreWeight': {'type': 'number'},
                                                'payPerConversionEligibilityFailureReasons': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                },
                                                'remarketingSetting': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'googleGlobalSiteTag': {'type': 'string'},
                                                    },
                                                },
                                                'resourceName': {'type': 'string', 'description': 'Resource name of the customer'},
                                                'testAccount': {'type': 'boolean'},
                                                'timeZone': {'type': 'string'},
                                                'trackingUrlTemplate': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'accounts',
                                    'x-airbyte-stream-name': 'accounts',
                                },
                            },
                            'nextPageToken': {'type': 'string', 'description': 'Token for retrieving the next page'},
                            'fieldMask': {'type': 'string', 'description': 'Field mask of requested fields'},
                            'queryResourceConsumption': {'type': 'string', 'description': 'Resource consumption of the query'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_page_token': '$.nextPageToken'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Google Ads customer account',
                'properties': {
                    'customer': {
                        'type': 'object',
                        'properties': {
                            'autoTaggingEnabled': {'type': 'boolean', 'description': 'Whether auto-tagging is enabled'},
                            'callReportingSetting': {
                                'type': 'object',
                                'properties': {
                                    'callConversionAction': {'type': 'string'},
                                    'callConversionReportingEnabled': {'type': 'boolean'},
                                    'callReportingEnabled': {'type': 'boolean'},
                                },
                            },
                            'conversionTrackingSetting': {
                                'type': 'object',
                                'properties': {
                                    'conversionTrackingId': {'type': 'string'},
                                    'crossAccountConversionTrackingId': {'type': 'string'},
                                },
                            },
                            'currencyCode': {'type': 'string', 'description': 'Currency code (e.g., USD)'},
                            'descriptiveName': {'type': 'string', 'description': 'Account descriptive name'},
                            'finalUrlSuffix': {'type': 'string'},
                            'hasPartnersBadge': {'type': 'boolean'},
                            'id': {'type': 'string', 'description': 'Customer ID'},
                            'manager': {'type': 'boolean', 'description': 'Whether this is a manager account'},
                            'optimizationScore': {'type': 'number'},
                            'optimizationScoreWeight': {'type': 'number'},
                            'payPerConversionEligibilityFailureReasons': {
                                'type': 'array',
                                'items': {'type': 'string'},
                            },
                            'remarketingSetting': {
                                'type': 'object',
                                'properties': {
                                    'googleGlobalSiteTag': {'type': 'string'},
                                },
                            },
                            'resourceName': {'type': 'string', 'description': 'Resource name of the customer'},
                            'testAccount': {'type': 'boolean'},
                            'timeZone': {'type': 'string'},
                            'trackingUrlTemplate': {'type': 'string'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'accounts',
                'x-airbyte-stream-name': 'accounts',
            },
        ),
        EntityDefinition(
            name='campaigns',
            stream_name='campaigns',
            actions=[Action.LIST, Action.UPDATE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/googleAds:search?entity=campaigns',
                    path_override=PathOverrideConfig(
                        path='/v20/customers/{customer_id}/googleAds:search',
                    ),
                    action=Action.LIST,
                    description='Retrieves campaign data using GAQL query.',
                    body_fields=['query', 'pageToken', 'pageSize'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={'query': 'SELECT\n  campaign.id,\n  campaign.name,\n  campaign.status,\n  campaign.advertising_channel_type,\n  campaign.advertising_channel_sub_type,\n  campaign.bidding_strategy,\n  campaign.bidding_strategy_type,\n  campaign.campaign_budget,\n  campaign_budget.amount_micros,\n  campaign.start_date,\n  campaign.end_date,\n  campaign.serving_status,\n  campaign.resource_name,\n  campaign.labels,\n  campaign.network_settings.target_google_search,\n  campaign.network_settings.target_search_network,\n  campaign.network_settings.target_content_network,\n  campaign.network_settings.target_partner_search_network\nFROM campaign'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'query': {
                                'type': 'string',
                                'description': 'GAQL query for campaigns',
                                'default': 'SELECT\n  campaign.id,\n  campaign.name,\n  campaign.status,\n  campaign.advertising_channel_type,\n  campaign.advertising_channel_sub_type,\n  campaign.bidding_strategy,\n  campaign.bidding_strategy_type,\n  campaign.campaign_budget,\n  campaign_budget.amount_micros,\n  campaign.start_date,\n  campaign.end_date,\n  campaign.serving_status,\n  campaign.resource_name,\n  campaign.labels,\n  campaign.network_settings.target_google_search,\n  campaign.network_settings.target_search_network,\n  campaign.network_settings.target_content_network,\n  campaign.network_settings.target_partner_search_network\nFROM campaign',
                            },
                            'pageToken': {'type': 'string', 'description': 'Token for pagination'},
                            'pageSize': {'type': 'integer', 'description': 'Number of results per page (max 10000)'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Search response containing campaign data',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Google Ads campaign',
                                    'properties': {
                                        'campaign': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Campaign ID'},
                                                'name': {'type': 'string', 'description': 'Campaign name'},
                                                'status': {
                                                    'type': 'string',
                                                    'enum': [
                                                        'ENABLED',
                                                        'PAUSED',
                                                        'REMOVED',
                                                        'UNKNOWN',
                                                        'UNSPECIFIED',
                                                    ],
                                                    'description': 'Campaign status',
                                                },
                                                'advertisingChannelType': {'type': 'string', 'description': 'Primary channel type'},
                                                'advertisingChannelSubType': {'type': 'string'},
                                                'biddingStrategy': {'type': 'string'},
                                                'biddingStrategyType': {'type': 'string'},
                                                'campaignBudget': {'type': 'string', 'description': 'Campaign budget resource name'},
                                                'startDate': {'type': 'string', 'description': 'Campaign start date'},
                                                'endDate': {'type': 'string', 'description': 'Campaign end date'},
                                                'servingStatus': {'type': 'string'},
                                                'resourceName': {'type': 'string'},
                                                'labels': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                },
                                                'networkSettings': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'targetGoogleSearch': {'type': 'boolean'},
                                                        'targetSearchNetwork': {'type': 'boolean'},
                                                        'targetContentNetwork': {'type': 'boolean'},
                                                        'targetPartnerSearchNetwork': {'type': 'boolean'},
                                                    },
                                                },
                                            },
                                        },
                                        'campaignBudget': {
                                            'type': 'object',
                                            'properties': {
                                                'resourceName': {'type': 'string', 'description': 'Resource name of the campaign budget'},
                                                'amountMicros': {'type': 'string', 'description': 'Budget amount in micros'},
                                            },
                                        },
                                        'metrics': {
                                            'type': 'object',
                                            'properties': {
                                                'clicks': {'type': 'string'},
                                                'ctr': {'type': 'number'},
                                                'conversions': {'type': 'number'},
                                                'conversionsValue': {'type': 'number'},
                                                'costMicros': {'type': 'string'},
                                                'impressions': {'type': 'string'},
                                                'averageCpc': {'type': 'number'},
                                                'averageCpm': {'type': 'number'},
                                                'interactions': {'type': 'string'},
                                            },
                                        },
                                        'segments': {
                                            'type': 'object',
                                            'properties': {
                                                'date': {'type': 'string', 'description': 'Date in YYYY-MM-DD format'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'campaigns',
                                    'x-airbyte-stream-name': 'campaigns',
                                },
                            },
                            'nextPageToken': {'type': 'string'},
                            'fieldMask': {'type': 'string'},
                            'queryResourceConsumption': {'type': 'string', 'description': 'Resource consumption of the query'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_page_token': '$.nextPageToken'},
                ),
                Action.UPDATE: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/campaigns:mutate',
                    action=Action.UPDATE,
                    description='Updates campaign properties such as status (enable/pause), name, or other mutable fields using the Google Ads CampaignService mutate endpoint.',
                    body_fields=['operations'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request to mutate (update) campaigns',
                        'properties': {
                            'operations': {
                                'type': 'array',
                                'description': 'List of campaign operations to perform',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'updateMask': {'type': 'string', 'description': 'Comma-separated list of field paths to update (e.g., name,status)'},
                                        'update': {
                                            'type': 'object',
                                            'description': 'Campaign fields to update',
                                            'properties': {
                                                'resourceName': {'type': 'string', 'description': 'Resource name of the campaign to update (e.g., customers/1234567890/campaigns/111222333)'},
                                                'name': {'type': 'string', 'description': 'New campaign name'},
                                                'status': {
                                                    'type': 'string',
                                                    'enum': ['ENABLED', 'PAUSED'],
                                                    'description': 'Campaign status (ENABLED or PAUSED)',
                                                },
                                            },
                                            'required': ['resourceName'],
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['operations'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from campaign mutate operation',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'resourceName': {'type': 'string', 'description': 'Resource name of the mutated campaign'},
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'campaigns',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Google Ads campaign',
                'properties': {
                    'campaign': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Campaign ID'},
                            'name': {'type': 'string', 'description': 'Campaign name'},
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'ENABLED',
                                    'PAUSED',
                                    'REMOVED',
                                    'UNKNOWN',
                                    'UNSPECIFIED',
                                ],
                                'description': 'Campaign status',
                            },
                            'advertisingChannelType': {'type': 'string', 'description': 'Primary channel type'},
                            'advertisingChannelSubType': {'type': 'string'},
                            'biddingStrategy': {'type': 'string'},
                            'biddingStrategyType': {'type': 'string'},
                            'campaignBudget': {'type': 'string', 'description': 'Campaign budget resource name'},
                            'startDate': {'type': 'string', 'description': 'Campaign start date'},
                            'endDate': {'type': 'string', 'description': 'Campaign end date'},
                            'servingStatus': {'type': 'string'},
                            'resourceName': {'type': 'string'},
                            'labels': {
                                'type': 'array',
                                'items': {'type': 'string'},
                            },
                            'networkSettings': {
                                'type': 'object',
                                'properties': {
                                    'targetGoogleSearch': {'type': 'boolean'},
                                    'targetSearchNetwork': {'type': 'boolean'},
                                    'targetContentNetwork': {'type': 'boolean'},
                                    'targetPartnerSearchNetwork': {'type': 'boolean'},
                                },
                            },
                        },
                    },
                    'campaignBudget': {
                        'type': 'object',
                        'properties': {
                            'resourceName': {'type': 'string', 'description': 'Resource name of the campaign budget'},
                            'amountMicros': {'type': 'string', 'description': 'Budget amount in micros'},
                        },
                    },
                    'metrics': {
                        'type': 'object',
                        'properties': {
                            'clicks': {'type': 'string'},
                            'ctr': {'type': 'number'},
                            'conversions': {'type': 'number'},
                            'conversionsValue': {'type': 'number'},
                            'costMicros': {'type': 'string'},
                            'impressions': {'type': 'string'},
                            'averageCpc': {'type': 'number'},
                            'averageCpm': {'type': 'number'},
                            'interactions': {'type': 'string'},
                        },
                    },
                    'segments': {
                        'type': 'object',
                        'properties': {
                            'date': {'type': 'string', 'description': 'Date in YYYY-MM-DD format'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'campaigns',
                'x-airbyte-stream-name': 'campaigns',
            },
        ),
        EntityDefinition(
            name='ad_groups',
            stream_name='ad_groups',
            actions=[Action.LIST, Action.UPDATE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/googleAds:search?entity=ad_groups',
                    path_override=PathOverrideConfig(
                        path='/v20/customers/{customer_id}/googleAds:search',
                    ),
                    action=Action.LIST,
                    description='Retrieves ad group data using GAQL query.',
                    body_fields=['query', 'pageToken', 'pageSize'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={'query': 'SELECT\n  campaign.id,\n  ad_group.id,\n  ad_group.name,\n  ad_group.status,\n  ad_group.type,\n  ad_group.ad_rotation_mode,\n  ad_group.base_ad_group,\n  ad_group.campaign,\n  ad_group.cpc_bid_micros,\n  ad_group.cpm_bid_micros,\n  ad_group.cpv_bid_micros,\n  ad_group.effective_target_cpa_micros,\n  ad_group.effective_target_cpa_source,\n  ad_group.effective_target_roas,\n  ad_group.effective_target_roas_source,\n  ad_group.labels,\n  ad_group.resource_name,\n  ad_group.target_cpa_micros,\n  ad_group.target_roas,\n  ad_group.tracking_url_template\nFROM ad_group'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'query': {
                                'type': 'string',
                                'description': 'GAQL query for ad groups',
                                'default': 'SELECT\n  campaign.id,\n  ad_group.id,\n  ad_group.name,\n  ad_group.status,\n  ad_group.type,\n  ad_group.ad_rotation_mode,\n  ad_group.base_ad_group,\n  ad_group.campaign,\n  ad_group.cpc_bid_micros,\n  ad_group.cpm_bid_micros,\n  ad_group.cpv_bid_micros,\n  ad_group.effective_target_cpa_micros,\n  ad_group.effective_target_cpa_source,\n  ad_group.effective_target_roas,\n  ad_group.effective_target_roas_source,\n  ad_group.labels,\n  ad_group.resource_name,\n  ad_group.target_cpa_micros,\n  ad_group.target_roas,\n  ad_group.tracking_url_template\nFROM ad_group',
                            },
                            'pageToken': {'type': 'string', 'description': 'Token for pagination'},
                            'pageSize': {'type': 'integer', 'description': 'Number of results per page (max 10000)'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Search response containing ad group data',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Google Ads ad group',
                                    'properties': {
                                        'campaign': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Parent campaign ID'},
                                                'resourceName': {'type': 'string', 'description': 'Parent campaign resource name'},
                                            },
                                        },
                                        'adGroup': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Ad group ID'},
                                                'name': {'type': 'string', 'description': 'Ad group name'},
                                                'status': {
                                                    'type': 'string',
                                                    'enum': [
                                                        'ENABLED',
                                                        'PAUSED',
                                                        'REMOVED',
                                                        'UNKNOWN',
                                                        'UNSPECIFIED',
                                                    ],
                                                },
                                                'type': {'type': 'string'},
                                                'adRotationMode': {'type': 'string'},
                                                'baseAdGroup': {'type': 'string'},
                                                'campaign': {'type': 'string', 'description': 'Parent campaign resource name'},
                                                'cpcBidMicros': {'type': 'string'},
                                                'cpmBidMicros': {'type': 'string'},
                                                'cpvBidMicros': {'type': 'string'},
                                                'effectiveTargetCpaMicros': {'type': 'string'},
                                                'effectiveTargetCpaSource': {'type': 'string'},
                                                'effectiveTargetRoas': {'type': 'number'},
                                                'effectiveTargetRoasSource': {'type': 'string'},
                                                'labels': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                },
                                                'resourceName': {'type': 'string'},
                                                'targetCpaMicros': {'type': 'string'},
                                                'targetRoas': {'type': 'number'},
                                                'trackingUrlTemplate': {'type': 'string'},
                                            },
                                        },
                                        'metrics': {
                                            'type': 'object',
                                            'properties': {
                                                'costMicros': {'type': 'string'},
                                            },
                                        },
                                        'segments': {
                                            'type': 'object',
                                            'properties': {
                                                'date': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'ad_groups',
                                    'x-airbyte-stream-name': 'ad_groups',
                                },
                            },
                            'nextPageToken': {'type': 'string'},
                            'fieldMask': {'type': 'string'},
                            'queryResourceConsumption': {'type': 'string', 'description': 'Resource consumption of the query'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_page_token': '$.nextPageToken'},
                ),
                Action.UPDATE: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/adGroups:mutate',
                    action=Action.UPDATE,
                    description='Updates ad group properties such as status (enable/pause), name, or bid amounts using the Google Ads AdGroupService mutate endpoint.',
                    body_fields=['operations'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request to mutate (update) ad groups',
                        'properties': {
                            'operations': {
                                'type': 'array',
                                'description': 'List of ad group operations to perform',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'updateMask': {'type': 'string', 'description': 'Comma-separated list of field paths to update (e.g., name,status,cpcBidMicros)'},
                                        'update': {
                                            'type': 'object',
                                            'description': 'Ad group fields to update',
                                            'properties': {
                                                'resourceName': {'type': 'string', 'description': 'Resource name of the ad group to update (e.g., customers/1234567890/adGroups/111222333)'},
                                                'name': {'type': 'string', 'description': 'New ad group name'},
                                                'status': {
                                                    'type': 'string',
                                                    'enum': ['ENABLED', 'PAUSED'],
                                                    'description': 'Ad group status (ENABLED or PAUSED)',
                                                },
                                                'cpcBidMicros': {'type': 'string', 'description': 'CPC bid amount in micros (1,000,000 micros = 1 currency unit)'},
                                            },
                                            'required': ['resourceName'],
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['operations'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from ad group mutate operation',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'resourceName': {'type': 'string', 'description': 'Resource name of the mutated ad group'},
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'ad_groups',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Google Ads ad group',
                'properties': {
                    'campaign': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Parent campaign ID'},
                            'resourceName': {'type': 'string', 'description': 'Parent campaign resource name'},
                        },
                    },
                    'adGroup': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Ad group ID'},
                            'name': {'type': 'string', 'description': 'Ad group name'},
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'ENABLED',
                                    'PAUSED',
                                    'REMOVED',
                                    'UNKNOWN',
                                    'UNSPECIFIED',
                                ],
                            },
                            'type': {'type': 'string'},
                            'adRotationMode': {'type': 'string'},
                            'baseAdGroup': {'type': 'string'},
                            'campaign': {'type': 'string', 'description': 'Parent campaign resource name'},
                            'cpcBidMicros': {'type': 'string'},
                            'cpmBidMicros': {'type': 'string'},
                            'cpvBidMicros': {'type': 'string'},
                            'effectiveTargetCpaMicros': {'type': 'string'},
                            'effectiveTargetCpaSource': {'type': 'string'},
                            'effectiveTargetRoas': {'type': 'number'},
                            'effectiveTargetRoasSource': {'type': 'string'},
                            'labels': {
                                'type': 'array',
                                'items': {'type': 'string'},
                            },
                            'resourceName': {'type': 'string'},
                            'targetCpaMicros': {'type': 'string'},
                            'targetRoas': {'type': 'number'},
                            'trackingUrlTemplate': {'type': 'string'},
                        },
                    },
                    'metrics': {
                        'type': 'object',
                        'properties': {
                            'costMicros': {'type': 'string'},
                        },
                    },
                    'segments': {
                        'type': 'object',
                        'properties': {
                            'date': {'type': 'string'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'ad_groups',
                'x-airbyte-stream-name': 'ad_groups',
            },
        ),
        EntityDefinition(
            name='ad_group_ads',
            stream_name='ad_group_ads',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/googleAds:search?entity=ad_group_ads',
                    path_override=PathOverrideConfig(
                        path='/v20/customers/{customer_id}/googleAds:search',
                    ),
                    action=Action.LIST,
                    description='Retrieves ad group ad data using GAQL query.',
                    body_fields=['query', 'pageToken', 'pageSize'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={'query': 'SELECT\n  ad_group.id,\n  ad_group_ad.ad.id,\n  ad_group_ad.ad.name,\n  ad_group_ad.ad.type,\n  ad_group_ad.status,\n  ad_group_ad.ad_strength,\n  ad_group_ad.ad.display_url,\n  ad_group_ad.ad.final_urls,\n  ad_group_ad.ad.final_mobile_urls,\n  ad_group_ad.ad.final_url_suffix,\n  ad_group_ad.ad.tracking_url_template,\n  ad_group_ad.ad.resource_name,\n  ad_group_ad.ad_group,\n  ad_group_ad.resource_name,\n  ad_group_ad.labels,\n  ad_group_ad.policy_summary.approval_status,\n  ad_group_ad.policy_summary.review_status\nFROM ad_group_ad'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'query': {
                                'type': 'string',
                                'description': 'GAQL query for ad group ads',
                                'default': 'SELECT\n  ad_group.id,\n  ad_group_ad.ad.id,\n  ad_group_ad.ad.name,\n  ad_group_ad.ad.type,\n  ad_group_ad.status,\n  ad_group_ad.ad_strength,\n  ad_group_ad.ad.display_url,\n  ad_group_ad.ad.final_urls,\n  ad_group_ad.ad.final_mobile_urls,\n  ad_group_ad.ad.final_url_suffix,\n  ad_group_ad.ad.tracking_url_template,\n  ad_group_ad.ad.resource_name,\n  ad_group_ad.ad_group,\n  ad_group_ad.resource_name,\n  ad_group_ad.labels,\n  ad_group_ad.policy_summary.approval_status,\n  ad_group_ad.policy_summary.review_status\nFROM ad_group_ad',
                            },
                            'pageToken': {'type': 'string', 'description': 'Token for pagination'},
                            'pageSize': {'type': 'integer', 'description': 'Number of results per page (max 10000)'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Search response containing ad group ad data',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Google Ads ad group ad',
                                    'properties': {
                                        'adGroup': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Parent ad group ID'},
                                                'resourceName': {'type': 'string', 'description': 'Parent ad group resource name'},
                                            },
                                        },
                                        'adGroupAd': {
                                            'type': 'object',
                                            'properties': {
                                                'ad': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {'type': 'string', 'description': 'Ad ID'},
                                                        'name': {'type': 'string'},
                                                        'type': {'type': 'string'},
                                                        'displayUrl': {'type': 'string'},
                                                        'finalUrls': {
                                                            'type': 'array',
                                                            'items': {'type': 'string'},
                                                        },
                                                        'finalMobileUrls': {
                                                            'type': 'array',
                                                            'items': {'type': 'string'},
                                                        },
                                                        'finalUrlSuffix': {'type': 'string'},
                                                        'trackingUrlTemplate': {'type': 'string'},
                                                        'resourceName': {'type': 'string'},
                                                    },
                                                },
                                                'status': {
                                                    'type': 'string',
                                                    'enum': [
                                                        'ENABLED',
                                                        'PAUSED',
                                                        'REMOVED',
                                                        'UNKNOWN',
                                                        'UNSPECIFIED',
                                                    ],
                                                },
                                                'adStrength': {'type': 'string'},
                                                'adGroup': {'type': 'string'},
                                                'resourceName': {'type': 'string'},
                                                'labels': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                },
                                                'policySummary': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'approvalStatus': {'type': 'string'},
                                                        'reviewStatus': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                        'segments': {
                                            'type': 'object',
                                            'properties': {
                                                'date': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'ad_group_ads',
                                    'x-airbyte-stream-name': 'ad_group_ads',
                                },
                            },
                            'nextPageToken': {'type': 'string'},
                            'fieldMask': {'type': 'string'},
                            'queryResourceConsumption': {'type': 'string', 'description': 'Resource consumption of the query'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_page_token': '$.nextPageToken'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Google Ads ad group ad',
                'properties': {
                    'adGroup': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Parent ad group ID'},
                            'resourceName': {'type': 'string', 'description': 'Parent ad group resource name'},
                        },
                    },
                    'adGroupAd': {
                        'type': 'object',
                        'properties': {
                            'ad': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Ad ID'},
                                    'name': {'type': 'string'},
                                    'type': {'type': 'string'},
                                    'displayUrl': {'type': 'string'},
                                    'finalUrls': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                    },
                                    'finalMobileUrls': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                    },
                                    'finalUrlSuffix': {'type': 'string'},
                                    'trackingUrlTemplate': {'type': 'string'},
                                    'resourceName': {'type': 'string'},
                                },
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'ENABLED',
                                    'PAUSED',
                                    'REMOVED',
                                    'UNKNOWN',
                                    'UNSPECIFIED',
                                ],
                            },
                            'adStrength': {'type': 'string'},
                            'adGroup': {'type': 'string'},
                            'resourceName': {'type': 'string'},
                            'labels': {
                                'type': 'array',
                                'items': {'type': 'string'},
                            },
                            'policySummary': {
                                'type': 'object',
                                'properties': {
                                    'approvalStatus': {'type': 'string'},
                                    'reviewStatus': {'type': 'string'},
                                },
                            },
                        },
                    },
                    'segments': {
                        'type': 'object',
                        'properties': {
                            'date': {'type': 'string'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'ad_group_ads',
                'x-airbyte-stream-name': 'ad_group_ads',
            },
        ),
        EntityDefinition(
            name='campaign_labels',
            stream_name='campaign_labels',
            actions=[Action.LIST, Action.CREATE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/googleAds:search?entity=campaign_labels',
                    path_override=PathOverrideConfig(
                        path='/v20/customers/{customer_id}/googleAds:search',
                    ),
                    action=Action.LIST,
                    description='Retrieves campaign label associations using GAQL query.',
                    body_fields=['query', 'pageToken', 'pageSize'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={'query': 'SELECT\n  campaign.id,\n  campaign_label.campaign,\n  campaign_label.label,\n  campaign_label.resource_name,\n  label.id,\n  label.name,\n  label.resource_name\nFROM campaign_label'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'query': {
                                'type': 'string',
                                'description': 'GAQL query for campaign labels',
                                'default': 'SELECT\n  campaign.id,\n  campaign_label.campaign,\n  campaign_label.label,\n  campaign_label.resource_name,\n  label.id,\n  label.name,\n  label.resource_name\nFROM campaign_label',
                            },
                            'pageToken': {'type': 'string', 'description': 'Token for pagination'},
                            'pageSize': {'type': 'integer', 'description': 'Number of results per page (max 10000)'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Search response containing campaign label data',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Campaign label association',
                                    'properties': {
                                        'campaign': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string'},
                                            },
                                        },
                                        'campaignLabel': {
                                            'type': 'object',
                                            'properties': {
                                                'campaign': {'type': 'string'},
                                                'label': {'type': 'string'},
                                                'resourceName': {'type': 'string'},
                                            },
                                        },
                                        'label': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resourceName': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'campaign_labels',
                                    'x-airbyte-stream-name': 'campaign_labels',
                                },
                            },
                            'nextPageToken': {'type': 'string'},
                            'fieldMask': {'type': 'string'},
                            'queryResourceConsumption': {'type': 'string', 'description': 'Resource consumption of the query'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_page_token': '$.nextPageToken'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/campaignLabels:mutate',
                    action=Action.CREATE,
                    description='Creates a campaign-label association, applying an existing label to a campaign for organization and filtering.',
                    body_fields=['operations'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request to create campaign-label associations',
                        'properties': {
                            'operations': {
                                'type': 'array',
                                'description': 'List of campaign label operations to perform',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'create': {
                                            'type': 'object',
                                            'description': 'Campaign label association to create',
                                            'properties': {
                                                'campaign': {'type': 'string', 'description': 'Resource name of the campaign (e.g., customers/1234567890/campaigns/111222333)'},
                                                'label': {'type': 'string', 'description': 'Resource name of the label (e.g., customers/1234567890/labels/444555666)'},
                                            },
                                            'required': ['campaign', 'label'],
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['operations'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from campaign label mutate operation',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'resourceName': {'type': 'string', 'description': 'Resource name of the created campaign label association'},
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'campaign_labels',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Campaign label association',
                'properties': {
                    'campaign': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string'},
                        },
                    },
                    'campaignLabel': {
                        'type': 'object',
                        'properties': {
                            'campaign': {'type': 'string'},
                            'label': {'type': 'string'},
                            'resourceName': {'type': 'string'},
                        },
                    },
                    'label': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string'},
                            'name': {'type': 'string'},
                            'resourceName': {'type': 'string'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'campaign_labels',
                'x-airbyte-stream-name': 'campaign_labels',
            },
        ),
        EntityDefinition(
            name='ad_group_labels',
            stream_name='ad_group_labels',
            actions=[Action.LIST, Action.CREATE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/googleAds:search?entity=ad_group_labels',
                    path_override=PathOverrideConfig(
                        path='/v20/customers/{customer_id}/googleAds:search',
                    ),
                    action=Action.LIST,
                    description='Retrieves ad group label associations using GAQL query.',
                    body_fields=['query', 'pageToken', 'pageSize'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={'query': 'SELECT\n  ad_group.id,\n  ad_group_label.ad_group,\n  ad_group_label.label,\n  ad_group_label.resource_name,\n  label.id,\n  label.name,\n  label.resource_name\nFROM ad_group_label'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'query': {
                                'type': 'string',
                                'description': 'GAQL query for ad group labels',
                                'default': 'SELECT\n  ad_group.id,\n  ad_group_label.ad_group,\n  ad_group_label.label,\n  ad_group_label.resource_name,\n  label.id,\n  label.name,\n  label.resource_name\nFROM ad_group_label',
                            },
                            'pageToken': {'type': 'string', 'description': 'Token for pagination'},
                            'pageSize': {'type': 'integer', 'description': 'Number of results per page (max 10000)'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Search response containing ad group label data',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Ad group label association',
                                    'properties': {
                                        'adGroup': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string'},
                                            },
                                        },
                                        'adGroupLabel': {
                                            'type': 'object',
                                            'properties': {
                                                'adGroup': {'type': 'string'},
                                                'label': {'type': 'string'},
                                                'resourceName': {'type': 'string'},
                                            },
                                        },
                                        'label': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resourceName': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'ad_group_labels',
                                    'x-airbyte-stream-name': 'ad_group_labels',
                                },
                            },
                            'nextPageToken': {'type': 'string'},
                            'fieldMask': {'type': 'string'},
                            'queryResourceConsumption': {'type': 'string', 'description': 'Resource consumption of the query'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_page_token': '$.nextPageToken'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/adGroupLabels:mutate',
                    action=Action.CREATE,
                    description='Creates an ad group-label association, applying an existing label to an ad group for organization and filtering.',
                    body_fields=['operations'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request to create ad group-label associations',
                        'properties': {
                            'operations': {
                                'type': 'array',
                                'description': 'List of ad group label operations to perform',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'create': {
                                            'type': 'object',
                                            'description': 'Ad group label association to create',
                                            'properties': {
                                                'adGroup': {'type': 'string', 'description': 'Resource name of the ad group (e.g., customers/1234567890/adGroups/111222333)'},
                                                'label': {'type': 'string', 'description': 'Resource name of the label (e.g., customers/1234567890/labels/444555666)'},
                                            },
                                            'required': ['adGroup', 'label'],
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['operations'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from ad group label mutate operation',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'resourceName': {'type': 'string', 'description': 'Resource name of the created ad group label association'},
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'ad_group_labels',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Ad group label association',
                'properties': {
                    'adGroup': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string'},
                        },
                    },
                    'adGroupLabel': {
                        'type': 'object',
                        'properties': {
                            'adGroup': {'type': 'string'},
                            'label': {'type': 'string'},
                            'resourceName': {'type': 'string'},
                        },
                    },
                    'label': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string'},
                            'name': {'type': 'string'},
                            'resourceName': {'type': 'string'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'ad_group_labels',
                'x-airbyte-stream-name': 'ad_group_labels',
            },
        ),
        EntityDefinition(
            name='ad_group_ad_labels',
            stream_name='ad_group_ad_labels',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/googleAds:search?entity=ad_group_ad_labels',
                    path_override=PathOverrideConfig(
                        path='/v20/customers/{customer_id}/googleAds:search',
                    ),
                    action=Action.LIST,
                    description='Retrieves ad group ad label associations using GAQL query.',
                    body_fields=['query', 'pageToken', 'pageSize'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={'query': 'SELECT\n  ad_group_ad.ad.id,\n  ad_group_ad_label.ad_group_ad,\n  ad_group_ad_label.label,\n  ad_group_ad_label.resource_name,\n  label.id,\n  label.name,\n  label.resource_name\nFROM ad_group_ad_label'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'query': {
                                'type': 'string',
                                'description': 'GAQL query for ad group ad labels',
                                'default': 'SELECT\n  ad_group_ad.ad.id,\n  ad_group_ad_label.ad_group_ad,\n  ad_group_ad_label.label,\n  ad_group_ad_label.resource_name,\n  label.id,\n  label.name,\n  label.resource_name\nFROM ad_group_ad_label',
                            },
                            'pageToken': {'type': 'string', 'description': 'Token for pagination'},
                            'pageSize': {'type': 'integer', 'description': 'Number of results per page (max 10000)'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Search response containing ad group ad label data',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Ad group ad label association',
                                    'properties': {
                                        'adGroupAd': {
                                            'type': 'object',
                                            'properties': {
                                                'ad': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                        'adGroupAdLabel': {
                                            'type': 'object',
                                            'properties': {
                                                'adGroupAd': {'type': 'string'},
                                                'label': {'type': 'string'},
                                                'resourceName': {'type': 'string'},
                                            },
                                        },
                                        'label': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resourceName': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'ad_group_ad_labels',
                                    'x-airbyte-stream-name': 'ad_group_ad_labels',
                                },
                            },
                            'nextPageToken': {'type': 'string'},
                            'fieldMask': {'type': 'string'},
                            'queryResourceConsumption': {'type': 'string', 'description': 'Resource consumption of the query'},
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'next_page_token': '$.nextPageToken'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Ad group ad label association',
                'properties': {
                    'adGroupAd': {
                        'type': 'object',
                        'properties': {
                            'ad': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string'},
                                },
                            },
                        },
                    },
                    'adGroupAdLabel': {
                        'type': 'object',
                        'properties': {
                            'adGroupAd': {'type': 'string'},
                            'label': {'type': 'string'},
                            'resourceName': {'type': 'string'},
                        },
                    },
                    'label': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string'},
                            'name': {'type': 'string'},
                            'resourceName': {'type': 'string'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'ad_group_ad_labels',
                'x-airbyte-stream-name': 'ad_group_ad_labels',
            },
        ),
        EntityDefinition(
            name='labels',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v20/customers/{customer_id}/labels:mutate',
                    action=Action.CREATE,
                    description='Creates a new label that can be applied to campaigns, ad groups, or ads for organization and reporting purposes.',
                    body_fields=['operations'],
                    path_params=['customer_id'],
                    path_params_schema={
                        'customer_id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request to create labels',
                        'properties': {
                            'operations': {
                                'type': 'array',
                                'description': 'List of label operations to perform',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'create': {
                                            'type': 'object',
                                            'description': 'Label to create',
                                            'properties': {
                                                'name': {'type': 'string', 'description': 'Name for the new label'},
                                                'description': {'type': 'string', 'description': 'Description for the label'},
                                                'textLabel': {
                                                    'type': 'object',
                                                    'description': 'Text label styling',
                                                    'properties': {
                                                        'backgroundColor': {'type': 'string', 'description': 'Background color in hex format (e.g., #FF0000)'},
                                                        'description': {'type': 'string', 'description': 'Description of the text label'},
                                                    },
                                                },
                                            },
                                            'required': ['name'],
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['operations'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from label mutate operation',
                        'properties': {
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'resourceName': {'type': 'string', 'description': 'Resource name of the created label'},
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'labels',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Response from label mutate operation',
                'properties': {
                    'results': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'resourceName': {'type': 'string', 'description': 'Resource name of the created label'},
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'labels',
            },
        ),
    ],
    search_field_paths={
        'accounts': [
            'customer.auto_tagging_enabled',
            'customer.call_reporting_setting.call_conversion_action',
            'customer.call_reporting_setting.call_conversion_reporting_enabled',
            'customer.call_reporting_setting.call_reporting_enabled',
            'customer.conversion_tracking_setting.conversion_tracking_id',
            'customer.conversion_tracking_setting.cross_account_conversion_tracking_id',
            'customer.currency_code',
            'customer.descriptive_name',
            'customer.final_url_suffix',
            'customer.has_partners_badge',
            'customer.id',
            'customer.manager',
            'customer.optimization_score',
            'customer.optimization_score_weight',
            'customer.pay_per_conversion_eligibility_failure_reasons',
            'customer.pay_per_conversion_eligibility_failure_reasons[]',
            'customer.remarketing_setting.google_global_site_tag',
            'customer.resource_name',
            'customer.test_account',
            'customer.time_zone',
            'customer.tracking_url_template',
            'segments.date',
        ],
        'campaigns': [
            'campaign.id',
            'campaign.name',
            'campaign.status',
            'campaign.advertising_channel_type',
            'campaign.advertising_channel_sub_type',
            'campaign.bidding_strategy',
            'campaign.bidding_strategy_type',
            'campaign.campaign_budget',
            'campaign_budget.amount_micros',
            'campaign.start_date',
            'campaign.end_date',
            'campaign.serving_status',
            'campaign.resource_name',
            'campaign.labels',
            'campaign.labels[]',
            'campaign.network_settings.target_google_search',
            'campaign.network_settings.target_search_network',
            'campaign.network_settings.target_content_network',
            'campaign.network_settings.target_partner_search_network',
            'metrics.clicks',
            'metrics.ctr',
            'metrics.conversions',
            'metrics.conversions_value',
            'metrics.cost_micros',
            'metrics.impressions',
            'metrics.average_cpc',
            'metrics.average_cpm',
            'metrics.interactions',
            'segments.date',
            'segments.hour',
            'segments.ad_network_type',
        ],
        'ad_groups': [
            'campaign.id',
            'ad_group.id',
            'ad_group.name',
            'ad_group.status',
            'ad_group.type',
            'ad_group.ad_rotation_mode',
            'ad_group.base_ad_group',
            'ad_group.campaign',
            'ad_group.cpc_bid_micros',
            'ad_group.cpm_bid_micros',
            'ad_group.cpv_bid_micros',
            'ad_group.effective_target_cpa_micros',
            'ad_group.effective_target_cpa_source',
            'ad_group.effective_target_roas',
            'ad_group.effective_target_roas_source',
            'ad_group.labels',
            'ad_group.labels[]',
            'ad_group.resource_name',
            'ad_group.target_cpa_micros',
            'ad_group.target_roas',
            'ad_group.tracking_url_template',
            'metrics.cost_micros',
            'segments.date',
        ],
        'ad_group_ads': [
            'ad_group.id',
            'ad_group_ad.ad.id',
            'ad_group_ad.ad.name',
            'ad_group_ad.ad.type',
            'ad_group_ad.status',
            'ad_group_ad.ad_strength',
            'ad_group_ad.ad.display_url',
            'ad_group_ad.ad.final_urls',
            'ad_group_ad.ad.final_urls[]',
            'ad_group_ad.ad.final_mobile_urls',
            'ad_group_ad.ad.final_mobile_urls[]',
            'ad_group_ad.ad.final_url_suffix',
            'ad_group_ad.ad.tracking_url_template',
            'ad_group_ad.ad.resource_name',
            'ad_group_ad.ad_group',
            'ad_group_ad.resource_name',
            'ad_group_ad.labels',
            'ad_group_ad.labels[]',
            'ad_group_ad.policy_summary.approval_status',
            'ad_group_ad.policy_summary.review_status',
            'segments.date',
        ],
        'campaign_labels': [
            'campaign.id',
            'campaign_label.resource_name',
            'label.id',
            'label.name',
            'label.resource_name',
        ],
        'ad_group_labels': [
            'ad_group.id',
            'ad_group_label.resource_name',
            'label.id',
            'label.name',
            'label.resource_name',
        ],
        'ad_group_ad_labels': [
            'ad_group_ad.ad.id',
            'ad_group_ad_label.resource_name',
            'label.id',
            'label.name',
            'label.resource_name',
        ],
    },
)