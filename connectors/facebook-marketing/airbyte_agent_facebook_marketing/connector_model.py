"""
Connector model for facebook-marketing.

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

FacebookMarketingConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('e7778cfc-e97c-4458-9ecb-b4f2bba8946c'),
    name='facebook-marketing',
    version='1.0.3',
    base_url='https://graph.facebook.com/v24.0',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
            title='OAuth 2.0 Authentication',
            type='object',
            required=['client_id', 'client_secret', 'account_id'],
            properties={
                'access_token': AuthConfigFieldSpec(
                    title='Access Token',
                    description='Facebook OAuth2 Access Token',
                ),
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='Facebook App Client ID',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='Facebook App Client Secret',
                ),
                'account_id': AuthConfigFieldSpec(
                    title='Ad Account ID',
                    description='Facebook Ad Account ID (without act_ prefix)',
                ),
            },
            auth_mapping={
                'access_token': '${access_token}',
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
            },
            replication_auth_key_mapping={'credentials.client_id': 'client_id', 'credentials.client_secret': 'client_secret'},
            replication_auth_key_constants={'credentials.auth_type': 'oauth2.0'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='campaigns',
            stream_name='campaigns',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/act_{account_id}/campaigns',
                    action=Action.LIST,
                    description='Returns a list of campaigns for the specified ad account',
                    query_params=['fields', 'limit', 'after'],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'id,name,account_id,adlabels,bid_strategy,boosted_object_id,budget_rebalance_flag,budget_remaining,buying_type,daily_budget,created_time,configured_status,effective_status,issues_info,lifetime_budget,objective,smart_promotion_type,source_campaign_id,special_ad_category,special_ad_category_country,spend_cap,start_time,status,stop_time,updated_time',
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Facebook Ad Campaign',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Campaign ID'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Campaign name',
                                        },
                                        'account_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad account ID',
                                        },
                                        'adlabels': {
                                            'type': ['array', 'null'],
                                            'description': 'Ad labels associated with the campaign',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Ad label ID',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Ad label name',
                                                    },
                                                    'created_time': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'Creation time',
                                                    },
                                                    'updated_time': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'Last update time',
                                                    },
                                                },
                                            },
                                        },
                                        'bid_strategy': {
                                            'type': ['string', 'null'],
                                            'description': 'Bid strategy for the campaign',
                                        },
                                        'boosted_object_id': {
                                            'type': ['string', 'null'],
                                            'description': 'ID of the boosted object',
                                        },
                                        'budget_rebalance_flag': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether budget rebalancing is enabled',
                                        },
                                        'budget_remaining': {
                                            'type': ['number', 'null'],
                                            'description': 'Remaining budget',
                                        },
                                        'buying_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Buying type (AUCTION, RESERVED)',
                                        },
                                        'daily_budget': {
                                            'type': ['number', 'null'],
                                            'description': 'Daily budget in account currency',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Campaign creation time',
                                        },
                                        'configured_status': {
                                            'type': ['string', 'null'],
                                            'description': 'Configured status',
                                        },
                                        'effective_status': {
                                            'type': ['string', 'null'],
                                            'description': 'Effective status',
                                        },
                                        'issues_info': {
                                            'type': ['array', 'null'],
                                            'description': 'Issues information',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'error_code': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Error code',
                                                    },
                                                    'error_message': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Error message',
                                                    },
                                                    'error_summary': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Error summary',
                                                    },
                                                    'error_type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Error type',
                                                    },
                                                    'level': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Issue level',
                                                    },
                                                },
                                            },
                                        },
                                        'lifetime_budget': {
                                            'type': ['number', 'null'],
                                            'description': 'Lifetime budget',
                                        },
                                        'objective': {
                                            'type': ['string', 'null'],
                                            'description': 'Campaign objective',
                                        },
                                        'smart_promotion_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Smart promotion type',
                                        },
                                        'source_campaign_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Source campaign ID',
                                        },
                                        'special_ad_category': {
                                            'type': ['string', 'null'],
                                            'description': 'Special ad category',
                                        },
                                        'special_ad_category_country': {
                                            'type': ['array', 'null'],
                                            'description': 'Countries for special ad category',
                                            'items': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                        'spend_cap': {
                                            'type': ['number', 'null'],
                                            'description': 'Spend cap',
                                        },
                                        'start_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Campaign start time',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'Campaign status',
                                        },
                                        'stop_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Campaign stop time',
                                        },
                                        'updated_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Last update time',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'campaigns',
                                    'x-airbyte-stream-name': 'campaigns',
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'cursors': {
                                        'type': 'object',
                                        'properties': {
                                            'before': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for previous page',
                                            },
                                            'after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for next page',
                                    },
                                    'previous': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for previous page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'after': '$.paging.cursors.after'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/{campaign_id}',
                    action=Action.GET,
                    description='Returns a single campaign by ID',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'id,name,account_id,adlabels,bid_strategy,boosted_object_id,budget_rebalance_flag,budget_remaining,buying_type,daily_budget,created_time,configured_status,effective_status,issues_info,lifetime_budget,objective,smart_promotion_type,source_campaign_id,special_ad_category,special_ad_category_country,spend_cap,start_time,status,stop_time,updated_time',
                        },
                    },
                    path_params=['campaign_id'],
                    path_params_schema={
                        'campaign_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Facebook Ad Campaign',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Campaign ID'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Campaign name',
                            },
                            'account_id': {
                                'type': ['string', 'null'],
                                'description': 'Ad account ID',
                            },
                            'adlabels': {
                                'type': ['array', 'null'],
                                'description': 'Ad labels associated with the campaign',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad label ID',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad label name',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Creation time',
                                        },
                                        'updated_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Last update time',
                                        },
                                    },
                                },
                            },
                            'bid_strategy': {
                                'type': ['string', 'null'],
                                'description': 'Bid strategy for the campaign',
                            },
                            'boosted_object_id': {
                                'type': ['string', 'null'],
                                'description': 'ID of the boosted object',
                            },
                            'budget_rebalance_flag': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether budget rebalancing is enabled',
                            },
                            'budget_remaining': {
                                'type': ['number', 'null'],
                                'description': 'Remaining budget',
                            },
                            'buying_type': {
                                'type': ['string', 'null'],
                                'description': 'Buying type (AUCTION, RESERVED)',
                            },
                            'daily_budget': {
                                'type': ['number', 'null'],
                                'description': 'Daily budget in account currency',
                            },
                            'created_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Campaign creation time',
                            },
                            'configured_status': {
                                'type': ['string', 'null'],
                                'description': 'Configured status',
                            },
                            'effective_status': {
                                'type': ['string', 'null'],
                                'description': 'Effective status',
                            },
                            'issues_info': {
                                'type': ['array', 'null'],
                                'description': 'Issues information',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'error_code': {
                                            'type': ['string', 'null'],
                                            'description': 'Error code',
                                        },
                                        'error_message': {
                                            'type': ['string', 'null'],
                                            'description': 'Error message',
                                        },
                                        'error_summary': {
                                            'type': ['string', 'null'],
                                            'description': 'Error summary',
                                        },
                                        'error_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Error type',
                                        },
                                        'level': {
                                            'type': ['string', 'null'],
                                            'description': 'Issue level',
                                        },
                                    },
                                },
                            },
                            'lifetime_budget': {
                                'type': ['number', 'null'],
                                'description': 'Lifetime budget',
                            },
                            'objective': {
                                'type': ['string', 'null'],
                                'description': 'Campaign objective',
                            },
                            'smart_promotion_type': {
                                'type': ['string', 'null'],
                                'description': 'Smart promotion type',
                            },
                            'source_campaign_id': {
                                'type': ['string', 'null'],
                                'description': 'Source campaign ID',
                            },
                            'special_ad_category': {
                                'type': ['string', 'null'],
                                'description': 'Special ad category',
                            },
                            'special_ad_category_country': {
                                'type': ['array', 'null'],
                                'description': 'Countries for special ad category',
                                'items': {
                                    'type': ['string', 'null'],
                                },
                            },
                            'spend_cap': {
                                'type': ['number', 'null'],
                                'description': 'Spend cap',
                            },
                            'start_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Campaign start time',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'Campaign status',
                            },
                            'stop_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Campaign stop time',
                            },
                            'updated_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last update time',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'campaigns',
                        'x-airbyte-stream-name': 'campaigns',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Facebook Ad Campaign',
                'properties': {
                    'id': {'type': 'string', 'description': 'Campaign ID'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Campaign name',
                    },
                    'account_id': {
                        'type': ['string', 'null'],
                        'description': 'Ad account ID',
                    },
                    'adlabels': {
                        'type': ['array', 'null'],
                        'description': 'Ad labels associated with the campaign',
                        'items': {'$ref': '#/components/schemas/AdLabel'},
                    },
                    'bid_strategy': {
                        'type': ['string', 'null'],
                        'description': 'Bid strategy for the campaign',
                    },
                    'boosted_object_id': {
                        'type': ['string', 'null'],
                        'description': 'ID of the boosted object',
                    },
                    'budget_rebalance_flag': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether budget rebalancing is enabled',
                    },
                    'budget_remaining': {
                        'type': ['number', 'null'],
                        'description': 'Remaining budget',
                    },
                    'buying_type': {
                        'type': ['string', 'null'],
                        'description': 'Buying type (AUCTION, RESERVED)',
                    },
                    'daily_budget': {
                        'type': ['number', 'null'],
                        'description': 'Daily budget in account currency',
                    },
                    'created_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Campaign creation time',
                    },
                    'configured_status': {
                        'type': ['string', 'null'],
                        'description': 'Configured status',
                    },
                    'effective_status': {
                        'type': ['string', 'null'],
                        'description': 'Effective status',
                    },
                    'issues_info': {
                        'type': ['array', 'null'],
                        'description': 'Issues information',
                        'items': {'$ref': '#/components/schemas/IssueInfo'},
                    },
                    'lifetime_budget': {
                        'type': ['number', 'null'],
                        'description': 'Lifetime budget',
                    },
                    'objective': {
                        'type': ['string', 'null'],
                        'description': 'Campaign objective',
                    },
                    'smart_promotion_type': {
                        'type': ['string', 'null'],
                        'description': 'Smart promotion type',
                    },
                    'source_campaign_id': {
                        'type': ['string', 'null'],
                        'description': 'Source campaign ID',
                    },
                    'special_ad_category': {
                        'type': ['string', 'null'],
                        'description': 'Special ad category',
                    },
                    'special_ad_category_country': {
                        'type': ['array', 'null'],
                        'description': 'Countries for special ad category',
                        'items': {
                            'type': ['string', 'null'],
                        },
                    },
                    'spend_cap': {
                        'type': ['number', 'null'],
                        'description': 'Spend cap',
                    },
                    'start_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Campaign start time',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Campaign status',
                    },
                    'stop_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Campaign stop time',
                    },
                    'updated_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Last update time',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'campaigns',
                'x-airbyte-stream-name': 'campaigns',
            },
        ),
        EntityDefinition(
            name='ad_sets',
            stream_name='ad_sets',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/act_{account_id}/adsets',
                    action=Action.LIST,
                    description='Returns a list of ad sets for the specified ad account',
                    query_params=['fields', 'limit', 'after'],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'id,name,account_id,adlabels,bid_amount,bid_info,bid_strategy,bid_constraints,budget_remaining,campaign_id,created_time,daily_budget,effective_status,end_time,learning_stage_info,lifetime_budget,promoted_object,start_time,targeting,updated_time',
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Facebook Ad Set',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Ad Set ID'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad Set name',
                                        },
                                        'account_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad account ID',
                                        },
                                        'adlabels': {
                                            'type': ['array', 'null'],
                                            'description': 'Ad labels',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Ad label ID',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Ad label name',
                                                    },
                                                    'created_time': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'Creation time',
                                                    },
                                                    'updated_time': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'Last update time',
                                                    },
                                                },
                                            },
                                        },
                                        'bid_amount': {
                                            'type': ['number', 'null'],
                                            'description': 'Bid amount',
                                        },
                                        'bid_info': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'CLICKS': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Bid for clicks',
                                                        },
                                                        'ACTIONS': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Bid for actions',
                                                        },
                                                        'REACH': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Bid for reach',
                                                        },
                                                        'IMPRESSIONS': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Bid for impressions',
                                                        },
                                                        'SOCIAL': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Bid for social',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'bid_strategy': {
                                            'type': ['string', 'null'],
                                            'description': 'Bid strategy',
                                        },
                                        'bid_constraints': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'roas_average_floor': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'ROAS average floor',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'budget_remaining': {
                                            'type': ['number', 'null'],
                                            'description': 'Remaining budget',
                                        },
                                        'campaign_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Parent campaign ID',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Creation time',
                                        },
                                        'daily_budget': {
                                            'type': ['number', 'null'],
                                            'description': 'Daily budget',
                                        },
                                        'effective_status': {
                                            'type': ['string', 'null'],
                                            'description': 'Effective status',
                                        },
                                        'end_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'End time',
                                        },
                                        'learning_stage_info': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'status': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Learning stage status',
                                                        },
                                                        'conversions': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Number of conversions',
                                                        },
                                                        'last_sig_edit_ts': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Last significant edit timestamp',
                                                        },
                                                        'attribution_windows': {
                                                            'type': ['array', 'null'],
                                                            'description': 'Attribution windows',
                                                            'items': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'lifetime_budget': {
                                            'type': ['number', 'null'],
                                            'description': 'Lifetime budget',
                                        },
                                        'promoted_object': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'custom_event_type': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Custom event type',
                                                        },
                                                        'pixel_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Pixel ID',
                                                        },
                                                        'pixel_rule': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Pixel rule',
                                                        },
                                                        'page_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Page ID',
                                                        },
                                                        'object_store_url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Object store URL',
                                                        },
                                                        'application_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Application ID',
                                                        },
                                                        'product_set_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Product set ID',
                                                        },
                                                        'offer_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Offer ID',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'start_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Start time',
                                        },
                                        'targeting': {
                                            'type': ['object', 'null'],
                                            'description': 'Targeting specification',
                                            'additionalProperties': True,
                                        },
                                        'updated_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Last update time',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'ad_sets',
                                    'x-airbyte-stream-name': 'ad_sets',
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'cursors': {
                                        'type': 'object',
                                        'properties': {
                                            'before': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for previous page',
                                            },
                                            'after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for next page',
                                    },
                                    'previous': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for previous page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'after': '$.paging.cursors.after'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/{adset_id}',
                    action=Action.GET,
                    description='Returns a single ad set by ID',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'id,name,account_id,adlabels,bid_amount,bid_info,bid_strategy,bid_constraints,budget_remaining,campaign_id,created_time,daily_budget,effective_status,end_time,learning_stage_info,lifetime_budget,promoted_object,start_time,targeting,updated_time',
                        },
                    },
                    path_params=['adset_id'],
                    path_params_schema={
                        'adset_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Facebook Ad Set',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Ad Set ID'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Ad Set name',
                            },
                            'account_id': {
                                'type': ['string', 'null'],
                                'description': 'Ad account ID',
                            },
                            'adlabels': {
                                'type': ['array', 'null'],
                                'description': 'Ad labels',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad label ID',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad label name',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Creation time',
                                        },
                                        'updated_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Last update time',
                                        },
                                    },
                                },
                            },
                            'bid_amount': {
                                'type': ['number', 'null'],
                                'description': 'Bid amount',
                            },
                            'bid_info': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'CLICKS': {
                                                'type': ['integer', 'null'],
                                                'description': 'Bid for clicks',
                                            },
                                            'ACTIONS': {
                                                'type': ['integer', 'null'],
                                                'description': 'Bid for actions',
                                            },
                                            'REACH': {
                                                'type': ['integer', 'null'],
                                                'description': 'Bid for reach',
                                            },
                                            'IMPRESSIONS': {
                                                'type': ['integer', 'null'],
                                                'description': 'Bid for impressions',
                                            },
                                            'SOCIAL': {
                                                'type': ['integer', 'null'],
                                                'description': 'Bid for social',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'bid_strategy': {
                                'type': ['string', 'null'],
                                'description': 'Bid strategy',
                            },
                            'bid_constraints': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'roas_average_floor': {
                                                'type': ['integer', 'null'],
                                                'description': 'ROAS average floor',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'budget_remaining': {
                                'type': ['number', 'null'],
                                'description': 'Remaining budget',
                            },
                            'campaign_id': {
                                'type': ['string', 'null'],
                                'description': 'Parent campaign ID',
                            },
                            'created_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Creation time',
                            },
                            'daily_budget': {
                                'type': ['number', 'null'],
                                'description': 'Daily budget',
                            },
                            'effective_status': {
                                'type': ['string', 'null'],
                                'description': 'Effective status',
                            },
                            'end_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'End time',
                            },
                            'learning_stage_info': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'status': {
                                                'type': ['string', 'null'],
                                                'description': 'Learning stage status',
                                            },
                                            'conversions': {
                                                'type': ['integer', 'null'],
                                                'description': 'Number of conversions',
                                            },
                                            'last_sig_edit_ts': {
                                                'type': ['integer', 'null'],
                                                'description': 'Last significant edit timestamp',
                                            },
                                            'attribution_windows': {
                                                'type': ['array', 'null'],
                                                'description': 'Attribution windows',
                                                'items': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'lifetime_budget': {
                                'type': ['number', 'null'],
                                'description': 'Lifetime budget',
                            },
                            'promoted_object': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'custom_event_type': {
                                                'type': ['string', 'null'],
                                                'description': 'Custom event type',
                                            },
                                            'pixel_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Pixel ID',
                                            },
                                            'pixel_rule': {
                                                'type': ['string', 'null'],
                                                'description': 'Pixel rule',
                                            },
                                            'page_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Page ID',
                                            },
                                            'object_store_url': {
                                                'type': ['string', 'null'],
                                                'description': 'Object store URL',
                                            },
                                            'application_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Application ID',
                                            },
                                            'product_set_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Product set ID',
                                            },
                                            'offer_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Offer ID',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'start_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Start time',
                            },
                            'targeting': {
                                'type': ['object', 'null'],
                                'description': 'Targeting specification',
                                'additionalProperties': True,
                            },
                            'updated_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last update time',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'ad_sets',
                        'x-airbyte-stream-name': 'ad_sets',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Facebook Ad Set',
                'properties': {
                    'id': {'type': 'string', 'description': 'Ad Set ID'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Ad Set name',
                    },
                    'account_id': {
                        'type': ['string', 'null'],
                        'description': 'Ad account ID',
                    },
                    'adlabels': {
                        'type': ['array', 'null'],
                        'description': 'Ad labels',
                        'items': {'$ref': '#/components/schemas/AdLabel'},
                    },
                    'bid_amount': {
                        'type': ['number', 'null'],
                        'description': 'Bid amount',
                    },
                    'bid_info': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/BidInfo'},
                            {'type': 'null'},
                        ],
                    },
                    'bid_strategy': {
                        'type': ['string', 'null'],
                        'description': 'Bid strategy',
                    },
                    'bid_constraints': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/BidConstraints'},
                            {'type': 'null'},
                        ],
                    },
                    'budget_remaining': {
                        'type': ['number', 'null'],
                        'description': 'Remaining budget',
                    },
                    'campaign_id': {
                        'type': ['string', 'null'],
                        'description': 'Parent campaign ID',
                    },
                    'created_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Creation time',
                    },
                    'daily_budget': {
                        'type': ['number', 'null'],
                        'description': 'Daily budget',
                    },
                    'effective_status': {
                        'type': ['string', 'null'],
                        'description': 'Effective status',
                    },
                    'end_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'End time',
                    },
                    'learning_stage_info': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LearningStageInfo'},
                            {'type': 'null'},
                        ],
                    },
                    'lifetime_budget': {
                        'type': ['number', 'null'],
                        'description': 'Lifetime budget',
                    },
                    'promoted_object': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/PromotedObject'},
                            {'type': 'null'},
                        ],
                    },
                    'start_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Start time',
                    },
                    'targeting': {
                        'type': ['object', 'null'],
                        'description': 'Targeting specification',
                        'additionalProperties': True,
                    },
                    'updated_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Last update time',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'ad_sets',
                'x-airbyte-stream-name': 'ad_sets',
            },
        ),
        EntityDefinition(
            name='ads',
            stream_name='ads',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/act_{account_id}/ads',
                    action=Action.LIST,
                    description='Returns a list of ads for the specified ad account',
                    query_params=['fields', 'limit', 'after'],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'id,name,account_id,adset_id,campaign_id,adlabels,bid_amount,bid_info,bid_type,configured_status,conversion_specs,created_time,creative,effective_status,last_updated_by_app_id,recommendations,source_ad_id,status,tracking_specs,updated_time',
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Facebook Ad',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Ad ID'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad name',
                                        },
                                        'account_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad account ID',
                                        },
                                        'adset_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Parent ad set ID',
                                        },
                                        'campaign_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Parent campaign ID',
                                        },
                                        'adlabels': {
                                            'type': ['array', 'null'],
                                            'description': 'Ad labels',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Ad label ID',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Ad label name',
                                                    },
                                                    'created_time': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'Creation time',
                                                    },
                                                    'updated_time': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'Last update time',
                                                    },
                                                },
                                            },
                                        },
                                        'bid_amount': {
                                            'type': ['integer', 'null'],
                                            'description': 'Bid amount',
                                        },
                                        'bid_info': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'CLICKS': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Bid for clicks',
                                                        },
                                                        'ACTIONS': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Bid for actions',
                                                        },
                                                        'REACH': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Bid for reach',
                                                        },
                                                        'IMPRESSIONS': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Bid for impressions',
                                                        },
                                                        'SOCIAL': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Bid for social',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'bid_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Bid type',
                                        },
                                        'configured_status': {
                                            'type': ['string', 'null'],
                                            'description': 'Configured status',
                                        },
                                        'conversion_specs': {
                                            'type': ['array', 'null'],
                                            'description': 'Conversion specifications',
                                            'items': {'type': 'object', 'additionalProperties': True},
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Creation time',
                                        },
                                        'creative': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Creative ID',
                                                        },
                                                        'creative_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Creative ID (alternate)',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'effective_status': {
                                            'type': ['string', 'null'],
                                            'description': 'Effective status',
                                        },
                                        'last_updated_by_app_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Last updated by app ID',
                                        },
                                        'recommendations': {
                                            'type': ['array', 'null'],
                                            'description': 'Recommendations',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'blame_field': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Field causing the recommendation',
                                                    },
                                                    'code': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Recommendation code',
                                                    },
                                                    'confidence': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Confidence level',
                                                    },
                                                    'importance': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Importance level',
                                                    },
                                                    'message': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Recommendation message',
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Recommendation title',
                                                    },
                                                },
                                            },
                                        },
                                        'source_ad_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Source ad ID',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad status',
                                        },
                                        'tracking_specs': {
                                            'type': ['array', 'null'],
                                            'description': 'Tracking specifications',
                                            'items': {'type': 'object', 'additionalProperties': True},
                                        },
                                        'updated_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Last update time',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'ads',
                                    'x-airbyte-stream-name': 'ads',
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'cursors': {
                                        'type': 'object',
                                        'properties': {
                                            'before': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for previous page',
                                            },
                                            'after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for next page',
                                    },
                                    'previous': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for previous page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'after': '$.paging.cursors.after'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/{ad_id}',
                    action=Action.GET,
                    description='Returns a single ad by ID',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'id,name,account_id,adset_id,campaign_id,adlabels,bid_amount,bid_info,bid_type,configured_status,conversion_specs,created_time,creative,effective_status,last_updated_by_app_id,recommendations,source_ad_id,status,tracking_specs,updated_time',
                        },
                    },
                    path_params=['ad_id'],
                    path_params_schema={
                        'ad_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Facebook Ad',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Ad ID'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Ad name',
                            },
                            'account_id': {
                                'type': ['string', 'null'],
                                'description': 'Ad account ID',
                            },
                            'adset_id': {
                                'type': ['string', 'null'],
                                'description': 'Parent ad set ID',
                            },
                            'campaign_id': {
                                'type': ['string', 'null'],
                                'description': 'Parent campaign ID',
                            },
                            'adlabels': {
                                'type': ['array', 'null'],
                                'description': 'Ad labels',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad label ID',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad label name',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Creation time',
                                        },
                                        'updated_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Last update time',
                                        },
                                    },
                                },
                            },
                            'bid_amount': {
                                'type': ['integer', 'null'],
                                'description': 'Bid amount',
                            },
                            'bid_info': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'CLICKS': {
                                                'type': ['integer', 'null'],
                                                'description': 'Bid for clicks',
                                            },
                                            'ACTIONS': {
                                                'type': ['integer', 'null'],
                                                'description': 'Bid for actions',
                                            },
                                            'REACH': {
                                                'type': ['integer', 'null'],
                                                'description': 'Bid for reach',
                                            },
                                            'IMPRESSIONS': {
                                                'type': ['integer', 'null'],
                                                'description': 'Bid for impressions',
                                            },
                                            'SOCIAL': {
                                                'type': ['integer', 'null'],
                                                'description': 'Bid for social',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'bid_type': {
                                'type': ['string', 'null'],
                                'description': 'Bid type',
                            },
                            'configured_status': {
                                'type': ['string', 'null'],
                                'description': 'Configured status',
                            },
                            'conversion_specs': {
                                'type': ['array', 'null'],
                                'description': 'Conversion specifications',
                                'items': {'type': 'object', 'additionalProperties': True},
                            },
                            'created_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Creation time',
                            },
                            'creative': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['string', 'null'],
                                                'description': 'Creative ID',
                                            },
                                            'creative_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Creative ID (alternate)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'effective_status': {
                                'type': ['string', 'null'],
                                'description': 'Effective status',
                            },
                            'last_updated_by_app_id': {
                                'type': ['string', 'null'],
                                'description': 'Last updated by app ID',
                            },
                            'recommendations': {
                                'type': ['array', 'null'],
                                'description': 'Recommendations',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'blame_field': {
                                            'type': ['string', 'null'],
                                            'description': 'Field causing the recommendation',
                                        },
                                        'code': {
                                            'type': ['integer', 'null'],
                                            'description': 'Recommendation code',
                                        },
                                        'confidence': {
                                            'type': ['string', 'null'],
                                            'description': 'Confidence level',
                                        },
                                        'importance': {
                                            'type': ['string', 'null'],
                                            'description': 'Importance level',
                                        },
                                        'message': {
                                            'type': ['string', 'null'],
                                            'description': 'Recommendation message',
                                        },
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Recommendation title',
                                        },
                                    },
                                },
                            },
                            'source_ad_id': {
                                'type': ['string', 'null'],
                                'description': 'Source ad ID',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'Ad status',
                            },
                            'tracking_specs': {
                                'type': ['array', 'null'],
                                'description': 'Tracking specifications',
                                'items': {'type': 'object', 'additionalProperties': True},
                            },
                            'updated_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last update time',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'ads',
                        'x-airbyte-stream-name': 'ads',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Facebook Ad',
                'properties': {
                    'id': {'type': 'string', 'description': 'Ad ID'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Ad name',
                    },
                    'account_id': {
                        'type': ['string', 'null'],
                        'description': 'Ad account ID',
                    },
                    'adset_id': {
                        'type': ['string', 'null'],
                        'description': 'Parent ad set ID',
                    },
                    'campaign_id': {
                        'type': ['string', 'null'],
                        'description': 'Parent campaign ID',
                    },
                    'adlabels': {
                        'type': ['array', 'null'],
                        'description': 'Ad labels',
                        'items': {'$ref': '#/components/schemas/AdLabel'},
                    },
                    'bid_amount': {
                        'type': ['integer', 'null'],
                        'description': 'Bid amount',
                    },
                    'bid_info': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/BidInfo'},
                            {'type': 'null'},
                        ],
                    },
                    'bid_type': {
                        'type': ['string', 'null'],
                        'description': 'Bid type',
                    },
                    'configured_status': {
                        'type': ['string', 'null'],
                        'description': 'Configured status',
                    },
                    'conversion_specs': {
                        'type': ['array', 'null'],
                        'description': 'Conversion specifications',
                        'items': {'type': 'object', 'additionalProperties': True},
                    },
                    'created_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Creation time',
                    },
                    'creative': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/AdCreativeRef'},
                            {'type': 'null'},
                        ],
                    },
                    'effective_status': {
                        'type': ['string', 'null'],
                        'description': 'Effective status',
                    },
                    'last_updated_by_app_id': {
                        'type': ['string', 'null'],
                        'description': 'Last updated by app ID',
                    },
                    'recommendations': {
                        'type': ['array', 'null'],
                        'description': 'Recommendations',
                        'items': {'$ref': '#/components/schemas/Recommendation'},
                    },
                    'source_ad_id': {
                        'type': ['string', 'null'],
                        'description': 'Source ad ID',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Ad status',
                    },
                    'tracking_specs': {
                        'type': ['array', 'null'],
                        'description': 'Tracking specifications',
                        'items': {'type': 'object', 'additionalProperties': True},
                    },
                    'updated_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Last update time',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'ads',
                'x-airbyte-stream-name': 'ads',
            },
        ),
        EntityDefinition(
            name='ad_creatives',
            stream_name='ad_creatives',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/act_{account_id}/adcreatives',
                    action=Action.LIST,
                    description='Returns a list of ad creatives for the specified ad account',
                    query_params=['fields', 'limit', 'after'],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'id,name,account_id,actor_id,body,call_to_action_type,effective_object_story_id,image_hash,image_url,link_url,object_story_id,object_story_spec,object_type,status,thumbnail_url,title,url_tags',
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Facebook Ad Creative',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Ad Creative ID'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad Creative name',
                                        },
                                        'account_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad account ID',
                                        },
                                        'actor_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Actor ID (Page ID)',
                                        },
                                        'body': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad body text',
                                        },
                                        'call_to_action_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Call to action type',
                                        },
                                        'effective_object_story_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Effective object story ID',
                                        },
                                        'image_hash': {
                                            'type': ['string', 'null'],
                                            'description': 'Image hash',
                                        },
                                        'image_url': {
                                            'type': ['string', 'null'],
                                            'description': 'Image URL',
                                        },
                                        'link_url': {
                                            'type': ['string', 'null'],
                                            'description': 'Link URL',
                                        },
                                        'object_story_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Object story ID',
                                        },
                                        'object_story_spec': {
                                            'type': ['object', 'null'],
                                            'description': 'Object story specification',
                                            'additionalProperties': True,
                                        },
                                        'object_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'Creative status',
                                        },
                                        'thumbnail_url': {
                                            'type': ['string', 'null'],
                                            'description': 'Thumbnail URL',
                                        },
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad title',
                                        },
                                        'url_tags': {
                                            'type': ['string', 'null'],
                                            'description': 'URL tags',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'ad_creatives',
                                    'x-airbyte-stream-name': 'ad_creatives',
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'cursors': {
                                        'type': 'object',
                                        'properties': {
                                            'before': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for previous page',
                                            },
                                            'after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for next page',
                                    },
                                    'previous': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for previous page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'after': '$.paging.cursors.after'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Facebook Ad Creative',
                'properties': {
                    'id': {'type': 'string', 'description': 'Ad Creative ID'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Ad Creative name',
                    },
                    'account_id': {
                        'type': ['string', 'null'],
                        'description': 'Ad account ID',
                    },
                    'actor_id': {
                        'type': ['string', 'null'],
                        'description': 'Actor ID (Page ID)',
                    },
                    'body': {
                        'type': ['string', 'null'],
                        'description': 'Ad body text',
                    },
                    'call_to_action_type': {
                        'type': ['string', 'null'],
                        'description': 'Call to action type',
                    },
                    'effective_object_story_id': {
                        'type': ['string', 'null'],
                        'description': 'Effective object story ID',
                    },
                    'image_hash': {
                        'type': ['string', 'null'],
                        'description': 'Image hash',
                    },
                    'image_url': {
                        'type': ['string', 'null'],
                        'description': 'Image URL',
                    },
                    'link_url': {
                        'type': ['string', 'null'],
                        'description': 'Link URL',
                    },
                    'object_story_id': {
                        'type': ['string', 'null'],
                        'description': 'Object story ID',
                    },
                    'object_story_spec': {
                        'type': ['object', 'null'],
                        'description': 'Object story specification',
                        'additionalProperties': True,
                    },
                    'object_type': {
                        'type': ['string', 'null'],
                        'description': 'Object type',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Creative status',
                    },
                    'thumbnail_url': {
                        'type': ['string', 'null'],
                        'description': 'Thumbnail URL',
                    },
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Ad title',
                    },
                    'url_tags': {
                        'type': ['string', 'null'],
                        'description': 'URL tags',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'ad_creatives',
                'x-airbyte-stream-name': 'ad_creatives',
            },
        ),
        EntityDefinition(
            name='ads_insights',
            stream_name='ads_insights',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/act_{account_id}/insights',
                    action=Action.LIST,
                    description='Returns performance insights for the specified ad account',
                    query_params=[
                        'fields',
                        'date_preset',
                        'time_range',
                        'level',
                        'limit',
                        'after',
                    ],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'account_id,account_name,campaign_id,campaign_name,adset_id,adset_name,ad_id,ad_name,clicks,impressions,reach,spend,cpc,cpm,ctr,date_start,date_stop',
                        },
                        'date_preset': {'type': 'string', 'required': False},
                        'time_range': {'type': 'string', 'required': False},
                        'level': {
                            'type': 'string',
                            'required': False,
                            'default': 'account',
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Facebook Ads Insight',
                                    'properties': {
                                        'account_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad account ID',
                                        },
                                        'account_name': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad account name',
                                        },
                                        'campaign_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Campaign ID',
                                        },
                                        'campaign_name': {
                                            'type': ['string', 'null'],
                                            'description': 'Campaign name',
                                        },
                                        'adset_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad set ID',
                                        },
                                        'adset_name': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad set name',
                                        },
                                        'ad_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad ID',
                                        },
                                        'ad_name': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad name',
                                        },
                                        'clicks': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of clicks',
                                        },
                                        'impressions': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of impressions',
                                        },
                                        'reach': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of people reached',
                                        },
                                        'spend': {
                                            'type': ['number', 'null'],
                                            'description': 'Amount spent',
                                        },
                                        'cpc': {
                                            'type': ['number', 'null'],
                                            'description': 'Cost per click',
                                        },
                                        'cpm': {
                                            'type': ['number', 'null'],
                                            'description': 'Cost per 1000 impressions',
                                        },
                                        'ctr': {
                                            'type': ['number', 'null'],
                                            'description': 'Click-through rate',
                                        },
                                        'date_start': {
                                            'type': ['string', 'null'],
                                            'format': 'date',
                                            'description': 'Start date of the data',
                                        },
                                        'date_stop': {
                                            'type': ['string', 'null'],
                                            'format': 'date',
                                            'description': 'End date of the data',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'ads_insights',
                                    'x-airbyte-stream-name': 'ads_insights',
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'cursors': {
                                        'type': 'object',
                                        'properties': {
                                            'before': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for previous page',
                                            },
                                            'after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for next page',
                                    },
                                    'previous': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for previous page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'after': '$.paging.cursors.after'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Facebook Ads Insight',
                'properties': {
                    'account_id': {
                        'type': ['string', 'null'],
                        'description': 'Ad account ID',
                    },
                    'account_name': {
                        'type': ['string', 'null'],
                        'description': 'Ad account name',
                    },
                    'campaign_id': {
                        'type': ['string', 'null'],
                        'description': 'Campaign ID',
                    },
                    'campaign_name': {
                        'type': ['string', 'null'],
                        'description': 'Campaign name',
                    },
                    'adset_id': {
                        'type': ['string', 'null'],
                        'description': 'Ad set ID',
                    },
                    'adset_name': {
                        'type': ['string', 'null'],
                        'description': 'Ad set name',
                    },
                    'ad_id': {
                        'type': ['string', 'null'],
                        'description': 'Ad ID',
                    },
                    'ad_name': {
                        'type': ['string', 'null'],
                        'description': 'Ad name',
                    },
                    'clicks': {
                        'type': ['integer', 'null'],
                        'description': 'Number of clicks',
                    },
                    'impressions': {
                        'type': ['integer', 'null'],
                        'description': 'Number of impressions',
                    },
                    'reach': {
                        'type': ['integer', 'null'],
                        'description': 'Number of people reached',
                    },
                    'spend': {
                        'type': ['number', 'null'],
                        'description': 'Amount spent',
                    },
                    'cpc': {
                        'type': ['number', 'null'],
                        'description': 'Cost per click',
                    },
                    'cpm': {
                        'type': ['number', 'null'],
                        'description': 'Cost per 1000 impressions',
                    },
                    'ctr': {
                        'type': ['number', 'null'],
                        'description': 'Click-through rate',
                    },
                    'date_start': {
                        'type': ['string', 'null'],
                        'format': 'date',
                        'description': 'Start date of the data',
                    },
                    'date_stop': {
                        'type': ['string', 'null'],
                        'format': 'date',
                        'description': 'End date of the data',
                    },
                },
                'x-airbyte-entity-name': 'ads_insights',
                'x-airbyte-stream-name': 'ads_insights',
            },
        ),
        EntityDefinition(
            name='custom_conversions',
            stream_name='custom_conversions',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/act_{account_id}/customconversions',
                    action=Action.LIST,
                    description='Returns a list of custom conversions for the specified ad account',
                    query_params=['fields', 'limit', 'after'],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'id,name,account_id,business,creation_time,custom_event_type,data_sources,default_conversion_value,description,event_source_type,first_fired_time,is_archived,is_unavailable,last_fired_time,offline_conversion_data_set,retention_days,rule',
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Facebook Custom Conversion',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Custom Conversion ID'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Custom Conversion name',
                                        },
                                        'account_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad account ID',
                                        },
                                        'business': {
                                            'type': ['string', 'null'],
                                            'description': 'Business ID',
                                        },
                                        'creation_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Creation time',
                                        },
                                        'custom_event_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Custom event type',
                                        },
                                        'data_sources': {
                                            'type': ['array', 'null'],
                                            'description': 'Data sources',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Data source ID',
                                                    },
                                                    'source_type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Source type',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Data source name',
                                                    },
                                                },
                                            },
                                        },
                                        'default_conversion_value': {
                                            'type': ['number', 'null'],
                                            'description': 'Default conversion value',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'Description',
                                        },
                                        'event_source_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Event source type',
                                        },
                                        'first_fired_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'First fired time',
                                        },
                                        'is_archived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether archived',
                                        },
                                        'is_unavailable': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether unavailable',
                                        },
                                        'last_fired_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Last fired time',
                                        },
                                        'offline_conversion_data_set': {
                                            'type': ['string', 'null'],
                                            'description': 'Offline conversion data set ID',
                                        },
                                        'retention_days': {
                                            'type': ['number', 'null'],
                                            'description': 'Retention days',
                                        },
                                        'rule': {
                                            'type': ['string', 'null'],
                                            'description': 'Rule definition',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'custom_conversions',
                                    'x-airbyte-stream-name': 'custom_conversions',
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'cursors': {
                                        'type': 'object',
                                        'properties': {
                                            'before': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for previous page',
                                            },
                                            'after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for next page',
                                    },
                                    'previous': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for previous page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'after': '$.paging.cursors.after'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Facebook Custom Conversion',
                'properties': {
                    'id': {'type': 'string', 'description': 'Custom Conversion ID'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Custom Conversion name',
                    },
                    'account_id': {
                        'type': ['string', 'null'],
                        'description': 'Ad account ID',
                    },
                    'business': {
                        'type': ['string', 'null'],
                        'description': 'Business ID',
                    },
                    'creation_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Creation time',
                    },
                    'custom_event_type': {
                        'type': ['string', 'null'],
                        'description': 'Custom event type',
                    },
                    'data_sources': {
                        'type': ['array', 'null'],
                        'description': 'Data sources',
                        'items': {'$ref': '#/components/schemas/DataSource'},
                    },
                    'default_conversion_value': {
                        'type': ['number', 'null'],
                        'description': 'Default conversion value',
                    },
                    'description': {
                        'type': ['string', 'null'],
                        'description': 'Description',
                    },
                    'event_source_type': {
                        'type': ['string', 'null'],
                        'description': 'Event source type',
                    },
                    'first_fired_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'First fired time',
                    },
                    'is_archived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether archived',
                    },
                    'is_unavailable': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether unavailable',
                    },
                    'last_fired_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Last fired time',
                    },
                    'offline_conversion_data_set': {
                        'type': ['string', 'null'],
                        'description': 'Offline conversion data set ID',
                    },
                    'retention_days': {
                        'type': ['number', 'null'],
                        'description': 'Retention days',
                    },
                    'rule': {
                        'type': ['string', 'null'],
                        'description': 'Rule definition',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'custom_conversions',
                'x-airbyte-stream-name': 'custom_conversions',
            },
        ),
        EntityDefinition(
            name='images',
            stream_name='images',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/act_{account_id}/adimages',
                    action=Action.LIST,
                    description='Returns a list of ad images for the specified ad account',
                    query_params=['fields', 'limit', 'after'],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'id,name,account_id,created_time,creatives,filename,hash,height,is_associated_creatives_in_adgroups,original_height,original_width,permalink_url,status,updated_time,url,url_128,width',
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                            'description': 'Image ID',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Image name',
                                        },
                                        'account_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad account ID',
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Creation time',
                                        },
                                        'creatives': {
                                            'type': ['array', 'null'],
                                            'description': 'Associated creatives',
                                            'items': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                        'filename': {
                                            'type': ['string', 'null'],
                                            'description': 'Filename',
                                        },
                                        'hash': {
                                            'type': ['string', 'null'],
                                            'description': 'Image hash',
                                        },
                                        'height': {
                                            'type': ['integer', 'null'],
                                            'description': 'Image height',
                                        },
                                        'is_associated_creatives_in_adgroups': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether associated with creatives in ad groups',
                                        },
                                        'original_height': {
                                            'type': ['integer', 'null'],
                                            'description': 'Original height',
                                        },
                                        'original_width': {
                                            'type': ['integer', 'null'],
                                            'description': 'Original width',
                                        },
                                        'permalink_url': {
                                            'type': ['string', 'null'],
                                            'description': 'Permalink URL',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'Image status',
                                        },
                                        'updated_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Last update time',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'Image URL',
                                        },
                                        'url_128': {
                                            'type': ['string', 'null'],
                                            'description': '128px thumbnail URL',
                                        },
                                        'width': {
                                            'type': ['integer', 'null'],
                                            'description': 'Image width',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'images',
                                    'x-airbyte-stream-name': 'images',
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'cursors': {
                                        'type': 'object',
                                        'properties': {
                                            'before': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for previous page',
                                            },
                                            'after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for next page',
                                    },
                                    'previous': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for previous page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'after': '$.paging.cursors.after'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['string', 'null'],
                        'description': 'Image ID',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Image name',
                    },
                    'account_id': {
                        'type': ['string', 'null'],
                        'description': 'Ad account ID',
                    },
                    'created_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Creation time',
                    },
                    'creatives': {
                        'type': ['array', 'null'],
                        'description': 'Associated creatives',
                        'items': {
                            'type': ['string', 'null'],
                        },
                    },
                    'filename': {
                        'type': ['string', 'null'],
                        'description': 'Filename',
                    },
                    'hash': {
                        'type': ['string', 'null'],
                        'description': 'Image hash',
                    },
                    'height': {
                        'type': ['integer', 'null'],
                        'description': 'Image height',
                    },
                    'is_associated_creatives_in_adgroups': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether associated with creatives in ad groups',
                    },
                    'original_height': {
                        'type': ['integer', 'null'],
                        'description': 'Original height',
                    },
                    'original_width': {
                        'type': ['integer', 'null'],
                        'description': 'Original width',
                    },
                    'permalink_url': {
                        'type': ['string', 'null'],
                        'description': 'Permalink URL',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Image status',
                    },
                    'updated_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Last update time',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'Image URL',
                    },
                    'url_128': {
                        'type': ['string', 'null'],
                        'description': '128px thumbnail URL',
                    },
                    'width': {
                        'type': ['integer', 'null'],
                        'description': 'Image width',
                    },
                },
                'x-airbyte-entity-name': 'images',
                'x-airbyte-stream-name': 'images',
            },
        ),
        EntityDefinition(
            name='videos',
            stream_name='videos',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/act_{account_id}/advideos',
                    action=Action.LIST,
                    description='Returns a list of ad videos for the specified ad account',
                    query_params=['fields', 'limit', 'after'],
                    query_params_schema={
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'id,title,account_id,ad_breaks,backdated_time,backdated_time_granularity,content_category,content_tags,created_time,custom_labels,description,embed_html,embeddable,format,icon,is_crosspost_video,is_crossposting_eligible,is_episode,is_instagram_eligible,length,live_status,permalink_url,post_views,premiere_living_room_status,published,scheduled_publish_time,source,universal_video_id,updated_time,views',
                        },
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Video ID'},
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Video title',
                                        },
                                        'account_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Ad account ID',
                                        },
                                        'ad_breaks': {
                                            'type': ['array', 'null'],
                                            'description': 'Ad breaks',
                                            'items': {'type': 'integer'},
                                        },
                                        'backdated_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Backdated time',
                                        },
                                        'backdated_time_granularity': {
                                            'type': ['string', 'null'],
                                            'description': 'Backdated time granularity',
                                        },
                                        'content_category': {
                                            'type': ['string', 'null'],
                                            'description': 'Content category',
                                        },
                                        'content_tags': {
                                            'type': ['array', 'null'],
                                            'description': 'Content tags',
                                            'items': {'type': 'string'},
                                        },
                                        'created_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Creation time',
                                        },
                                        'custom_labels': {
                                            'type': ['array', 'null'],
                                            'description': 'Custom labels',
                                            'items': {'type': 'string'},
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'Video description',
                                        },
                                        'embed_html': {
                                            'type': ['string', 'null'],
                                            'description': 'Embed HTML',
                                        },
                                        'embeddable': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether embeddable',
                                        },
                                        'format': {
                                            'type': ['array', 'null'],
                                            'description': 'Video formats',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'filter': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Format filter',
                                                    },
                                                    'embed_html': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Embed HTML',
                                                    },
                                                    'width': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Width',
                                                    },
                                                    'height': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Height',
                                                    },
                                                    'picture': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Picture URL',
                                                    },
                                                },
                                            },
                                        },
                                        'icon': {
                                            'type': ['string', 'null'],
                                            'description': 'Icon URL',
                                        },
                                        'is_crosspost_video': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether crosspost video',
                                        },
                                        'is_crossposting_eligible': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether eligible for crossposting',
                                        },
                                        'is_episode': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether episode',
                                        },
                                        'is_instagram_eligible': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether Instagram eligible',
                                        },
                                        'length': {
                                            'type': ['number', 'null'],
                                            'description': 'Video length in seconds',
                                        },
                                        'live_status': {
                                            'type': ['string', 'null'],
                                            'description': 'Live status',
                                        },
                                        'permalink_url': {
                                            'type': ['string', 'null'],
                                            'description': 'Permalink URL',
                                        },
                                        'post_views': {
                                            'type': ['integer', 'null'],
                                            'description': 'Post views',
                                        },
                                        'premiere_living_room_status': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Premiere living room status',
                                        },
                                        'published': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether published',
                                        },
                                        'scheduled_publish_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Scheduled publish time',
                                        },
                                        'source': {
                                            'type': ['string', 'null'],
                                            'description': 'Video source URL',
                                        },
                                        'universal_video_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Universal video ID',
                                        },
                                        'updated_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Last update time',
                                        },
                                        'views': {
                                            'type': ['integer', 'null'],
                                            'description': 'View count',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'videos',
                                    'x-airbyte-stream-name': 'videos',
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'cursors': {
                                        'type': 'object',
                                        'properties': {
                                            'before': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for previous page',
                                            },
                                            'after': {
                                                'type': ['string', 'null'],
                                                'description': 'Cursor for next page',
                                            },
                                        },
                                    },
                                    'next': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for next page',
                                    },
                                    'previous': {
                                        'type': ['string', 'null'],
                                        'description': 'URL for previous page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'after': '$.paging.cursors.after'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Video ID'},
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Video title',
                    },
                    'account_id': {
                        'type': ['string', 'null'],
                        'description': 'Ad account ID',
                    },
                    'ad_breaks': {
                        'type': ['array', 'null'],
                        'description': 'Ad breaks',
                        'items': {'type': 'integer'},
                    },
                    'backdated_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Backdated time',
                    },
                    'backdated_time_granularity': {
                        'type': ['string', 'null'],
                        'description': 'Backdated time granularity',
                    },
                    'content_category': {
                        'type': ['string', 'null'],
                        'description': 'Content category',
                    },
                    'content_tags': {
                        'type': ['array', 'null'],
                        'description': 'Content tags',
                        'items': {'type': 'string'},
                    },
                    'created_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Creation time',
                    },
                    'custom_labels': {
                        'type': ['array', 'null'],
                        'description': 'Custom labels',
                        'items': {'type': 'string'},
                    },
                    'description': {
                        'type': ['string', 'null'],
                        'description': 'Video description',
                    },
                    'embed_html': {
                        'type': ['string', 'null'],
                        'description': 'Embed HTML',
                    },
                    'embeddable': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether embeddable',
                    },
                    'format': {
                        'type': ['array', 'null'],
                        'description': 'Video formats',
                        'items': {'$ref': '#/components/schemas/VideoFormat'},
                    },
                    'icon': {
                        'type': ['string', 'null'],
                        'description': 'Icon URL',
                    },
                    'is_crosspost_video': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether crosspost video',
                    },
                    'is_crossposting_eligible': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether eligible for crossposting',
                    },
                    'is_episode': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether episode',
                    },
                    'is_instagram_eligible': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether Instagram eligible',
                    },
                    'length': {
                        'type': ['number', 'null'],
                        'description': 'Video length in seconds',
                    },
                    'live_status': {
                        'type': ['string', 'null'],
                        'description': 'Live status',
                    },
                    'permalink_url': {
                        'type': ['string', 'null'],
                        'description': 'Permalink URL',
                    },
                    'post_views': {
                        'type': ['integer', 'null'],
                        'description': 'Post views',
                    },
                    'premiere_living_room_status': {
                        'type': ['boolean', 'null'],
                        'description': 'Premiere living room status',
                    },
                    'published': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether published',
                    },
                    'scheduled_publish_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Scheduled publish time',
                    },
                    'source': {
                        'type': ['string', 'null'],
                        'description': 'Video source URL',
                    },
                    'universal_video_id': {
                        'type': ['string', 'null'],
                        'description': 'Universal video ID',
                    },
                    'updated_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Last update time',
                    },
                    'views': {
                        'type': ['integer', 'null'],
                        'description': 'View count',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'videos',
                'x-airbyte-stream-name': 'videos',
            },
        ),
    ],
    search_field_paths={
        'campaigns': [
            'id',
            'name',
            'account_id',
            'status',
            'effective_status',
            'objective',
            'daily_budget',
            'lifetime_budget',
            'budget_remaining',
            'created_time',
            'start_time',
            'stop_time',
            'updated_time',
        ],
        'ad_sets': [
            'id',
            'name',
            'account_id',
            'campaign_id',
            'effective_status',
            'daily_budget',
            'lifetime_budget',
            'budget_remaining',
            'bid_amount',
            'bid_strategy',
            'created_time',
            'start_time',
            'end_time',
            'updated_time',
        ],
        'ads': [
            'id',
            'name',
            'account_id',
            'adset_id',
            'campaign_id',
            'status',
            'effective_status',
            'created_time',
            'updated_time',
        ],
        'ad_creatives': [
            'id',
            'name',
            'account_id',
            'body',
            'title',
            'status',
            'image_url',
            'thumbnail_url',
            'link_url',
            'call_to_action_type',
        ],
        'ads_insights': [
            'account_id',
            'account_name',
            'campaign_id',
            'campaign_name',
            'adset_id',
            'adset_name',
            'ad_id',
            'ad_name',
            'clicks',
            'impressions',
            'reach',
            'spend',
            'cpc',
            'cpm',
            'ctr',
            'date_start',
            'date_stop',
        ],
        'custom_conversions': [
            'id',
            'name',
            'account_id',
            'description',
            'custom_event_type',
            'creation_time',
            'first_fired_time',
            'last_fired_time',
            'is_archived',
        ],
        'images': [
            'id',
            'name',
            'account_id',
            'hash',
            'url',
            'permalink_url',
            'width',
            'height',
            'status',
            'created_time',
            'updated_time',
        ],
        'videos': [
            'id',
            'title',
            'account_id',
            'description',
            'length',
            'source',
            'permalink_url',
            'views',
            'created_time',
            'updated_time',
        ],
    },
)