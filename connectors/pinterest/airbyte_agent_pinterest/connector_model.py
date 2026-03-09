"""
Connector model for pinterest.

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

PinterestConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('5cb7e5fe-38c2-11ec-8d3d-0242ac130003'),
    name='pinterest',
    version='0.1.1',
    base_url='https://api.pinterest.com/v5',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://api.pinterest.com/v5/oauth/token',
            'auth_style': 'basic',
            'body_format': 'form',
        },
        user_config_spec=AirbyteAuthConfig(
            title='OAuth 2.0 Authentication',
            type='object',
            required=['refresh_token', 'client_id', 'client_secret'],
            properties={
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='Pinterest OAuth2 refresh token.',
                ),
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='Pinterest OAuth2 client ID.',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='Pinterest OAuth2 client secret.',
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
            },
            replication_auth_key_constants={'credentials.auth_method': 'oauth2.0'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='ad_accounts',
            stream_name='ad_accounts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts',
                    action=Action.LIST,
                    description='Get a list of the ad accounts that the authenticated user has access to.',
                    query_params=['page_size', 'bookmark', 'include_shared_accounts'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                        'include_shared_accounts': {
                            'type': 'boolean',
                            'required': False,
                            'default': True,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of ad accounts',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest ad account object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier for the ad account',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the ad account',
                                        },
                                        'owner': {
                                            'type': ['null', 'object'],
                                            'description': 'Owner details of the ad account',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique identifier of the owner',
                                                },
                                                'username': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Username of the owner',
                                                },
                                            },
                                        },
                                        'country': {
                                            'type': ['null', 'string'],
                                            'description': 'Country associated with the ad account',
                                        },
                                        'currency': {
                                            'type': ['null', 'string'],
                                            'description': 'Currency used for billing',
                                        },
                                        'created_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Timestamp when the ad account was created (Unix seconds)',
                                        },
                                        'updated_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Timestamp when the ad account was last updated (Unix seconds)',
                                        },
                                        'permissions': {
                                            'type': ['null', 'array'],
                                            'description': 'Permissions assigned to the ad account',
                                            'items': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'ad_accounts',
                                    'x-airbyte-stream-name': 'ad_accounts',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts/{ad_account_id}',
                    action=Action.GET,
                    description='Get an ad account by ID.',
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Pinterest ad account object',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                                'description': 'Unique identifier for the ad account',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the ad account',
                            },
                            'owner': {
                                'type': ['null', 'object'],
                                'description': 'Owner details of the ad account',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'string'],
                                        'description': 'Unique identifier of the owner',
                                    },
                                    'username': {
                                        'type': ['null', 'string'],
                                        'description': 'Username of the owner',
                                    },
                                },
                            },
                            'country': {
                                'type': ['null', 'string'],
                                'description': 'Country associated with the ad account',
                            },
                            'currency': {
                                'type': ['null', 'string'],
                                'description': 'Currency used for billing',
                            },
                            'created_time': {
                                'type': ['null', 'integer'],
                                'description': 'Timestamp when the ad account was created (Unix seconds)',
                            },
                            'updated_time': {
                                'type': ['null', 'integer'],
                                'description': 'Timestamp when the ad account was last updated (Unix seconds)',
                            },
                            'permissions': {
                                'type': ['null', 'array'],
                                'description': 'Permissions assigned to the ad account',
                                'items': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'ad_accounts',
                        'x-airbyte-stream-name': 'ad_accounts',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest ad account object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier for the ad account',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the ad account',
                    },
                    'owner': {
                        'type': ['null', 'object'],
                        'description': 'Owner details of the ad account',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                                'description': 'Unique identifier of the owner',
                            },
                            'username': {
                                'type': ['null', 'string'],
                                'description': 'Username of the owner',
                            },
                        },
                    },
                    'country': {
                        'type': ['null', 'string'],
                        'description': 'Country associated with the ad account',
                    },
                    'currency': {
                        'type': ['null', 'string'],
                        'description': 'Currency used for billing',
                    },
                    'created_time': {
                        'type': ['null', 'integer'],
                        'description': 'Timestamp when the ad account was created (Unix seconds)',
                    },
                    'updated_time': {
                        'type': ['null', 'integer'],
                        'description': 'Timestamp when the ad account was last updated (Unix seconds)',
                    },
                    'permissions': {
                        'type': ['null', 'array'],
                        'description': 'Permissions assigned to the ad account',
                        'items': {
                            'type': ['null', 'string'],
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'ad_accounts',
                'x-airbyte-stream-name': 'ad_accounts',
            },
        ),
        EntityDefinition(
            name='boards',
            stream_name='boards',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/boards',
                    action=Action.LIST,
                    description='Get a list of the boards owned by the authenticated user.',
                    query_params=['page_size', 'bookmark', 'privacy'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                        'privacy': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of boards',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest board object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier for the board',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Board name',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Board description',
                                        },
                                        'owner': {
                                            'type': ['null', 'object'],
                                            'description': 'Board owner details',
                                            'properties': {
                                                'username': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Username of the board owner',
                                                },
                                            },
                                        },
                                        'is_ads_only': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the board is exclusively for ads',
                                        },
                                        'privacy': {
                                            'type': ['null', 'string'],
                                            'description': 'Board privacy setting (PUBLIC, SECRET)',
                                        },
                                        'follower_count': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of followers',
                                        },
                                        'collaborator_count': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of collaborators',
                                        },
                                        'pin_count': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of pins on the board',
                                        },
                                        'media': {
                                            'type': ['null', 'object'],
                                            'description': 'Media content for the board',
                                            'properties': {
                                                'image_cover_url': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Cover image URL',
                                                },
                                                'pin_thumbnail_urls': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Thumbnail URLs of pins',
                                                    'items': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the board was created',
                                        },
                                        'board_pins_modified_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when pins on the board were last modified',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'boards',
                                    'x-airbyte-stream-name': 'boards',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/boards/{board_id}',
                    action=Action.GET,
                    description='Get a board by ID.',
                    path_params=['board_id'],
                    path_params_schema={
                        'board_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Pinterest board object',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                                'description': 'Unique identifier for the board',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Board name',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Board description',
                            },
                            'owner': {
                                'type': ['null', 'object'],
                                'description': 'Board owner details',
                                'properties': {
                                    'username': {
                                        'type': ['null', 'string'],
                                        'description': 'Username of the board owner',
                                    },
                                },
                            },
                            'is_ads_only': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the board is exclusively for ads',
                            },
                            'privacy': {
                                'type': ['null', 'string'],
                                'description': 'Board privacy setting (PUBLIC, SECRET)',
                            },
                            'follower_count': {
                                'type': ['null', 'integer'],
                                'description': 'Number of followers',
                            },
                            'collaborator_count': {
                                'type': ['null', 'integer'],
                                'description': 'Number of collaborators',
                            },
                            'pin_count': {
                                'type': ['null', 'integer'],
                                'description': 'Number of pins on the board',
                            },
                            'media': {
                                'type': ['null', 'object'],
                                'description': 'Media content for the board',
                                'properties': {
                                    'image_cover_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Cover image URL',
                                    },
                                    'pin_thumbnail_urls': {
                                        'type': ['null', 'array'],
                                        'description': 'Thumbnail URLs of pins',
                                        'items': {'type': 'string'},
                                    },
                                },
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when the board was created',
                            },
                            'board_pins_modified_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp when pins on the board were last modified',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'boards',
                        'x-airbyte-stream-name': 'boards',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest board object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier for the board',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Board name',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Board description',
                    },
                    'owner': {
                        'type': ['null', 'object'],
                        'description': 'Board owner details',
                        'properties': {
                            'username': {
                                'type': ['null', 'string'],
                                'description': 'Username of the board owner',
                            },
                        },
                    },
                    'is_ads_only': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the board is exclusively for ads',
                    },
                    'privacy': {
                        'type': ['null', 'string'],
                        'description': 'Board privacy setting (PUBLIC, SECRET)',
                    },
                    'follower_count': {
                        'type': ['null', 'integer'],
                        'description': 'Number of followers',
                    },
                    'collaborator_count': {
                        'type': ['null', 'integer'],
                        'description': 'Number of collaborators',
                    },
                    'pin_count': {
                        'type': ['null', 'integer'],
                        'description': 'Number of pins on the board',
                    },
                    'media': {
                        'type': ['null', 'object'],
                        'description': 'Media content for the board',
                        'properties': {
                            'image_cover_url': {
                                'type': ['null', 'string'],
                                'description': 'Cover image URL',
                            },
                            'pin_thumbnail_urls': {
                                'type': ['null', 'array'],
                                'description': 'Thumbnail URLs of pins',
                                'items': {'type': 'string'},
                            },
                        },
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the board was created',
                    },
                    'board_pins_modified_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when pins on the board were last modified',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'boards',
                'x-airbyte-stream-name': 'boards',
            },
        ),
        EntityDefinition(
            name='campaigns',
            stream_name='campaigns',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts/{ad_account_id}/campaigns',
                    action=Action.LIST,
                    description='Get a list of campaigns in the specified ad account.',
                    query_params=[
                        'page_size',
                        'bookmark',
                        'entity_statuses',
                        'order',
                    ],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                        'entity_statuses': {'type': 'array', 'required': False},
                        'order': {'type': 'string', 'required': False},
                    },
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of campaigns',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest campaign object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign ID',
                                        },
                                        'ad_account_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad account ID',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign name',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Entity status (ACTIVE, PAUSED, ARCHIVED, DRAFT, DELETED_DRAFT)',
                                        },
                                        'lifetime_spend_cap': {
                                            'type': ['null', 'integer'],
                                            'description': 'Maximum lifetime spend in microcurrency',
                                        },
                                        'daily_spend_cap': {
                                            'type': ['null', 'integer'],
                                            'description': 'Maximum daily spend in microcurrency',
                                        },
                                        'order_line_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Order line ID on invoice',
                                        },
                                        'tracking_urls': {
                                            'type': ['null', 'object'],
                                            'description': 'Third-party tracking URLs',
                                            'properties': {
                                                'impression': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Impression tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'click': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Click tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'engagement': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Engagement tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'buyable_button': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Buyable button tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'audience_verification': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Audience verification tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'objective_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign objective type',
                                        },
                                        'created_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix seconds)',
                                        },
                                        'updated_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix seconds)',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': "Always 'campaign'",
                                        },
                                        'start_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Start timestamp (Unix seconds)',
                                        },
                                        'end_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'End timestamp (Unix seconds)',
                                        },
                                        'summary_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Summary status (RUNNING, PAUSED, NOT_STARTED, COMPLETED, ADVERTISER_DISABLED, ARCHIVED, DRAFT, DELETED_DRAFT)',
                                        },
                                        'is_campaign_budget_optimization': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether campaign budget optimization is enabled',
                                        },
                                        'is_flexible_daily_budgets': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether flexible daily budgets are enabled',
                                        },
                                        'is_performance_plus': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is a Performance+ campaign',
                                        },
                                        'is_top_of_search': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether top of search placement is enabled',
                                        },
                                        'is_automated_campaign': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is an automated campaign',
                                        },
                                        'bid_options': {
                                            'type': ['null', 'object'],
                                            'description': 'Campaign bid options',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'campaigns',
                                    'x-airbyte-stream-name': 'campaigns',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest campaign object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Campaign ID',
                    },
                    'ad_account_id': {
                        'type': ['null', 'string'],
                        'description': 'Ad account ID',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Campaign name',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Entity status (ACTIVE, PAUSED, ARCHIVED, DRAFT, DELETED_DRAFT)',
                    },
                    'lifetime_spend_cap': {
                        'type': ['null', 'integer'],
                        'description': 'Maximum lifetime spend in microcurrency',
                    },
                    'daily_spend_cap': {
                        'type': ['null', 'integer'],
                        'description': 'Maximum daily spend in microcurrency',
                    },
                    'order_line_id': {
                        'type': ['null', 'string'],
                        'description': 'Order line ID on invoice',
                    },
                    'tracking_urls': {
                        'type': ['null', 'object'],
                        'description': 'Third-party tracking URLs',
                        'properties': {
                            'impression': {
                                'type': ['null', 'array'],
                                'description': 'Impression tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'click': {
                                'type': ['null', 'array'],
                                'description': 'Click tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'engagement': {
                                'type': ['null', 'array'],
                                'description': 'Engagement tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'buyable_button': {
                                'type': ['null', 'array'],
                                'description': 'Buyable button tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'audience_verification': {
                                'type': ['null', 'array'],
                                'description': 'Audience verification tracking URLs',
                                'items': {'type': 'string'},
                            },
                        },
                    },
                    'objective_type': {
                        'type': ['null', 'string'],
                        'description': 'Campaign objective type',
                    },
                    'created_time': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix seconds)',
                    },
                    'updated_time': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix seconds)',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': "Always 'campaign'",
                    },
                    'start_time': {
                        'type': ['null', 'integer'],
                        'description': 'Start timestamp (Unix seconds)',
                    },
                    'end_time': {
                        'type': ['null', 'integer'],
                        'description': 'End timestamp (Unix seconds)',
                    },
                    'summary_status': {
                        'type': ['null', 'string'],
                        'description': 'Summary status (RUNNING, PAUSED, NOT_STARTED, COMPLETED, ADVERTISER_DISABLED, ARCHIVED, DRAFT, DELETED_DRAFT)',
                    },
                    'is_campaign_budget_optimization': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether campaign budget optimization is enabled',
                    },
                    'is_flexible_daily_budgets': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether flexible daily budgets are enabled',
                    },
                    'is_performance_plus': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is a Performance+ campaign',
                    },
                    'is_top_of_search': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether top of search placement is enabled',
                    },
                    'is_automated_campaign': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is an automated campaign',
                    },
                    'bid_options': {
                        'type': ['null', 'object'],
                        'description': 'Campaign bid options',
                    },
                },
                'required': ['id'],
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
                    path='/ad_accounts/{ad_account_id}/ad_groups',
                    action=Action.LIST,
                    description='Get a list of ad groups in the specified ad account.',
                    query_params=[
                        'page_size',
                        'bookmark',
                        'entity_statuses',
                        'order',
                    ],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                        'entity_statuses': {'type': 'array', 'required': False},
                        'order': {'type': 'string', 'required': False},
                    },
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of ad groups',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest ad group object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad group ID',
                                        },
                                        'ad_account_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad account ID',
                                        },
                                        'campaign_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Parent campaign ID',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad group name',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Entity status',
                                        },
                                        'budget_in_micro_currency': {
                                            'type': ['null', 'number'],
                                            'description': 'Budget in microcurrency',
                                        },
                                        'bid_in_micro_currency': {
                                            'type': ['null', 'number'],
                                            'description': 'Bid in microcurrency',
                                        },
                                        'budget_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Budget type (DAILY, LIFETIME, CBO_ADGROUP)',
                                        },
                                        'start_time': {
                                            'type': ['null', 'number'],
                                            'description': 'Start time (Unix seconds)',
                                        },
                                        'end_time': {
                                            'type': ['null', 'number'],
                                            'description': 'End time (Unix seconds)',
                                        },
                                        'targeting_spec': {
                                            'type': ['null', 'object'],
                                            'description': 'Targeting specifications',
                                        },
                                        'lifetime_frequency_cap': {
                                            'type': ['null', 'number'],
                                            'description': 'Maximum impressions per user in 30 days',
                                        },
                                        'tracking_urls': {
                                            'type': ['null', 'object'],
                                            'description': 'Third-party tracking URLs',
                                            'properties': {
                                                'impression': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Impression tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'click': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Click tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'engagement': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Engagement tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'buyable_button': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Buyable button tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'audience_verification': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Audience verification tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'auto_targeting_enabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether auto targeting is enabled',
                                        },
                                        'placement_group': {
                                            'type': ['null', 'string'],
                                            'description': 'Placement group (ALL, SEARCH, BROWSE, OTHER)',
                                        },
                                        'pacing_delivery_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Pacing delivery type (STANDARD, ACCELERATED)',
                                        },
                                        'conversion_learning_mode_type': {
                                            'type': ['null', 'string'],
                                            'description': 'oCPM learn mode type (NOT_ACTIVE, ACTIVE)',
                                        },
                                        'summary_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Summary status',
                                        },
                                        'feed_profile_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Feed profile ID',
                                        },
                                        'billable_event': {
                                            'type': ['null', 'string'],
                                            'description': 'Billable event type',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': "Always 'adgroup'",
                                        },
                                        'created_time': {
                                            'type': ['null', 'number'],
                                            'description': 'Creation timestamp (Unix seconds)',
                                        },
                                        'updated_time': {
                                            'type': ['null', 'number'],
                                            'description': 'Last update timestamp (Unix seconds)',
                                        },
                                        'bid_strategy_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Bid strategy type (AUTOMATIC_BID, MAX_BID, TARGET_AVG)',
                                        },
                                        'optimization_goal_metadata': {
                                            'type': ['null', 'object'],
                                            'description': 'Optimization goal metadata',
                                        },
                                        'placement_traffic_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Traffic type for placement',
                                        },
                                        'targeting_template_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'Targeting template IDs',
                                            'items': {'type': 'string'},
                                        },
                                        'is_creative_optimization': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether creative optimization is enabled',
                                        },
                                        'promotion_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Promotion ID',
                                        },
                                        'promotion_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'List of promotion IDs',
                                            'items': {'type': 'string'},
                                        },
                                        'promotion_application_level': {
                                            'type': ['null', 'string'],
                                            'description': 'Promotion application level (NONE, ITEM, AD_GROUP)',
                                        },
                                        'bid_multiplier': {
                                            'type': ['null', 'number'],
                                            'description': 'Bid multiplier (0.1 to 10.0)',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'ad_groups',
                                    'x-airbyte-stream-name': 'ad_groups',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest ad group object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Ad group ID',
                    },
                    'ad_account_id': {
                        'type': ['null', 'string'],
                        'description': 'Ad account ID',
                    },
                    'campaign_id': {
                        'type': ['null', 'string'],
                        'description': 'Parent campaign ID',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Ad group name',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Entity status',
                    },
                    'budget_in_micro_currency': {
                        'type': ['null', 'number'],
                        'description': 'Budget in microcurrency',
                    },
                    'bid_in_micro_currency': {
                        'type': ['null', 'number'],
                        'description': 'Bid in microcurrency',
                    },
                    'budget_type': {
                        'type': ['null', 'string'],
                        'description': 'Budget type (DAILY, LIFETIME, CBO_ADGROUP)',
                    },
                    'start_time': {
                        'type': ['null', 'number'],
                        'description': 'Start time (Unix seconds)',
                    },
                    'end_time': {
                        'type': ['null', 'number'],
                        'description': 'End time (Unix seconds)',
                    },
                    'targeting_spec': {
                        'type': ['null', 'object'],
                        'description': 'Targeting specifications',
                    },
                    'lifetime_frequency_cap': {
                        'type': ['null', 'number'],
                        'description': 'Maximum impressions per user in 30 days',
                    },
                    'tracking_urls': {
                        'type': ['null', 'object'],
                        'description': 'Third-party tracking URLs',
                        'properties': {
                            'impression': {
                                'type': ['null', 'array'],
                                'description': 'Impression tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'click': {
                                'type': ['null', 'array'],
                                'description': 'Click tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'engagement': {
                                'type': ['null', 'array'],
                                'description': 'Engagement tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'buyable_button': {
                                'type': ['null', 'array'],
                                'description': 'Buyable button tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'audience_verification': {
                                'type': ['null', 'array'],
                                'description': 'Audience verification tracking URLs',
                                'items': {'type': 'string'},
                            },
                        },
                    },
                    'auto_targeting_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether auto targeting is enabled',
                    },
                    'placement_group': {
                        'type': ['null', 'string'],
                        'description': 'Placement group (ALL, SEARCH, BROWSE, OTHER)',
                    },
                    'pacing_delivery_type': {
                        'type': ['null', 'string'],
                        'description': 'Pacing delivery type (STANDARD, ACCELERATED)',
                    },
                    'conversion_learning_mode_type': {
                        'type': ['null', 'string'],
                        'description': 'oCPM learn mode type (NOT_ACTIVE, ACTIVE)',
                    },
                    'summary_status': {
                        'type': ['null', 'string'],
                        'description': 'Summary status',
                    },
                    'feed_profile_id': {
                        'type': ['null', 'string'],
                        'description': 'Feed profile ID',
                    },
                    'billable_event': {
                        'type': ['null', 'string'],
                        'description': 'Billable event type',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': "Always 'adgroup'",
                    },
                    'created_time': {
                        'type': ['null', 'number'],
                        'description': 'Creation timestamp (Unix seconds)',
                    },
                    'updated_time': {
                        'type': ['null', 'number'],
                        'description': 'Last update timestamp (Unix seconds)',
                    },
                    'bid_strategy_type': {
                        'type': ['null', 'string'],
                        'description': 'Bid strategy type (AUTOMATIC_BID, MAX_BID, TARGET_AVG)',
                    },
                    'optimization_goal_metadata': {
                        'type': ['null', 'object'],
                        'description': 'Optimization goal metadata',
                    },
                    'placement_traffic_type': {
                        'type': ['null', 'string'],
                        'description': 'Traffic type for placement',
                    },
                    'targeting_template_ids': {
                        'type': ['null', 'array'],
                        'description': 'Targeting template IDs',
                        'items': {'type': 'string'},
                    },
                    'is_creative_optimization': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether creative optimization is enabled',
                    },
                    'promotion_id': {
                        'type': ['null', 'string'],
                        'description': 'Promotion ID',
                    },
                    'promotion_ids': {
                        'type': ['null', 'array'],
                        'description': 'List of promotion IDs',
                        'items': {'type': 'string'},
                    },
                    'promotion_application_level': {
                        'type': ['null', 'string'],
                        'description': 'Promotion application level (NONE, ITEM, AD_GROUP)',
                    },
                    'bid_multiplier': {
                        'type': ['null', 'number'],
                        'description': 'Bid multiplier (0.1 to 10.0)',
                    },
                },
                'required': ['id'],
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
                    path='/ad_accounts/{ad_account_id}/ads',
                    action=Action.LIST,
                    description='Get a list of ads in the specified ad account.',
                    query_params=[
                        'page_size',
                        'bookmark',
                        'entity_statuses',
                        'order',
                    ],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                        'entity_statuses': {'type': 'array', 'required': False},
                        'order': {'type': 'string', 'required': False},
                    },
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of ads',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest ad object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique ad ID',
                                        },
                                        'ad_group_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad group ID',
                                        },
                                        'ad_account_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad account ID',
                                        },
                                        'campaign_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign ID',
                                        },
                                        'pin_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Associated pin ID',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad name',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Entity status',
                                        },
                                        'creative_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Creative type (REGULAR, VIDEO, SHOPPING, CAROUSEL, etc.)',
                                        },
                                        'destination_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Main destination URL',
                                        },
                                        'click_tracking_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Click tracking URL',
                                        },
                                        'view_tracking_url': {
                                            'type': ['null', 'string'],
                                            'description': 'View tracking URL',
                                        },
                                        'android_deep_link': {
                                            'type': ['null', 'string'],
                                            'description': 'Android deep link',
                                        },
                                        'ios_deep_link': {
                                            'type': ['null', 'string'],
                                            'description': 'iOS deep link',
                                        },
                                        'carousel_android_deep_links': {
                                            'type': ['null', 'array'],
                                            'description': 'Carousel Android deep links',
                                            'items': {'type': 'string'},
                                        },
                                        'carousel_destination_urls': {
                                            'type': ['null', 'array'],
                                            'description': 'Carousel destination URLs',
                                            'items': {'type': 'string'},
                                        },
                                        'carousel_ios_deep_links': {
                                            'type': ['null', 'array'],
                                            'description': 'Carousel iOS deep links',
                                            'items': {'type': 'string'},
                                        },
                                        'tracking_urls': {
                                            'type': ['null', 'object'],
                                            'description': 'Third-party tracking URLs',
                                            'properties': {
                                                'impression': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Impression tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'click': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Click tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'engagement': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Engagement tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'buyable_button': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Buyable button tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                                'audience_verification': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Audience verification tracking URLs',
                                                    'items': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'is_pin_deleted': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the original pin is deleted',
                                        },
                                        'is_removable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the ad is removable',
                                        },
                                        'lead_form_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead form ID',
                                        },
                                        'collection_items_destination_url_template': {
                                            'type': ['null', 'string'],
                                            'description': 'Template URL for collection items',
                                        },
                                        'created_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix seconds)',
                                        },
                                        'updated_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix seconds)',
                                        },
                                        'rejected_reasons': {
                                            'type': ['null', 'array'],
                                            'description': 'Rejection reasons',
                                            'items': {'type': 'string'},
                                        },
                                        'rejection_labels': {
                                            'type': ['null', 'array'],
                                            'description': 'Rejection text labels',
                                            'items': {'type': 'string'},
                                        },
                                        'review_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Review status (OTHER, PENDING, REJECTED, APPROVED)',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': "Always 'pinpromotion'",
                                        },
                                        'summary_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Summary status',
                                        },
                                        'quiz_pin_data': {
                                            'type': ['null', 'object'],
                                            'description': 'Quiz pin data',
                                        },
                                        'grid_click_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Grid click type',
                                        },
                                        'customizable_cta_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Customizable CTA type (GET_OFFER, LEARN_MORE, SHOP_NOW, etc.)',
                                        },
                                        'disclosure_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Disclosure type',
                                        },
                                        'disclosure_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Pharmaceutical disclosure URL',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'ads',
                                    'x-airbyte-stream-name': 'ads',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest ad object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique ad ID',
                    },
                    'ad_group_id': {
                        'type': ['null', 'string'],
                        'description': 'Ad group ID',
                    },
                    'ad_account_id': {
                        'type': ['null', 'string'],
                        'description': 'Ad account ID',
                    },
                    'campaign_id': {
                        'type': ['null', 'string'],
                        'description': 'Campaign ID',
                    },
                    'pin_id': {
                        'type': ['null', 'string'],
                        'description': 'Associated pin ID',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Ad name',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Entity status',
                    },
                    'creative_type': {
                        'type': ['null', 'string'],
                        'description': 'Creative type (REGULAR, VIDEO, SHOPPING, CAROUSEL, etc.)',
                    },
                    'destination_url': {
                        'type': ['null', 'string'],
                        'description': 'Main destination URL',
                    },
                    'click_tracking_url': {
                        'type': ['null', 'string'],
                        'description': 'Click tracking URL',
                    },
                    'view_tracking_url': {
                        'type': ['null', 'string'],
                        'description': 'View tracking URL',
                    },
                    'android_deep_link': {
                        'type': ['null', 'string'],
                        'description': 'Android deep link',
                    },
                    'ios_deep_link': {
                        'type': ['null', 'string'],
                        'description': 'iOS deep link',
                    },
                    'carousel_android_deep_links': {
                        'type': ['null', 'array'],
                        'description': 'Carousel Android deep links',
                        'items': {'type': 'string'},
                    },
                    'carousel_destination_urls': {
                        'type': ['null', 'array'],
                        'description': 'Carousel destination URLs',
                        'items': {'type': 'string'},
                    },
                    'carousel_ios_deep_links': {
                        'type': ['null', 'array'],
                        'description': 'Carousel iOS deep links',
                        'items': {'type': 'string'},
                    },
                    'tracking_urls': {
                        'type': ['null', 'object'],
                        'description': 'Third-party tracking URLs',
                        'properties': {
                            'impression': {
                                'type': ['null', 'array'],
                                'description': 'Impression tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'click': {
                                'type': ['null', 'array'],
                                'description': 'Click tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'engagement': {
                                'type': ['null', 'array'],
                                'description': 'Engagement tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'buyable_button': {
                                'type': ['null', 'array'],
                                'description': 'Buyable button tracking URLs',
                                'items': {'type': 'string'},
                            },
                            'audience_verification': {
                                'type': ['null', 'array'],
                                'description': 'Audience verification tracking URLs',
                                'items': {'type': 'string'},
                            },
                        },
                    },
                    'is_pin_deleted': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the original pin is deleted',
                    },
                    'is_removable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the ad is removable',
                    },
                    'lead_form_id': {
                        'type': ['null', 'string'],
                        'description': 'Lead form ID',
                    },
                    'collection_items_destination_url_template': {
                        'type': ['null', 'string'],
                        'description': 'Template URL for collection items',
                    },
                    'created_time': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix seconds)',
                    },
                    'updated_time': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix seconds)',
                    },
                    'rejected_reasons': {
                        'type': ['null', 'array'],
                        'description': 'Rejection reasons',
                        'items': {'type': 'string'},
                    },
                    'rejection_labels': {
                        'type': ['null', 'array'],
                        'description': 'Rejection text labels',
                        'items': {'type': 'string'},
                    },
                    'review_status': {
                        'type': ['null', 'string'],
                        'description': 'Review status (OTHER, PENDING, REJECTED, APPROVED)',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': "Always 'pinpromotion'",
                    },
                    'summary_status': {
                        'type': ['null', 'string'],
                        'description': 'Summary status',
                    },
                    'quiz_pin_data': {
                        'type': ['null', 'object'],
                        'description': 'Quiz pin data',
                    },
                    'grid_click_type': {
                        'type': ['null', 'string'],
                        'description': 'Grid click type',
                    },
                    'customizable_cta_type': {
                        'type': ['null', 'string'],
                        'description': 'Customizable CTA type (GET_OFFER, LEARN_MORE, SHOP_NOW, etc.)',
                    },
                    'disclosure_type': {
                        'type': ['null', 'string'],
                        'description': 'Disclosure type',
                    },
                    'disclosure_url': {
                        'type': ['null', 'string'],
                        'description': 'Pharmaceutical disclosure URL',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'ads',
                'x-airbyte-stream-name': 'ads',
            },
        ),
        EntityDefinition(
            name='board_sections',
            stream_name='board_sections',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/boards/{board_id}/sections',
                    action=Action.LIST,
                    description='Get a list of sections for a specific board.',
                    query_params=['page_size', 'bookmark'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                    },
                    path_params=['board_id'],
                    path_params_schema={
                        'board_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of board sections',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest board section object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier for the board section',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the board section',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'board_sections',
                                    'x-airbyte-stream-name': 'board_sections',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest board section object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier for the board section',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the board section',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'board_sections',
                'x-airbyte-stream-name': 'board_sections',
            },
        ),
        EntityDefinition(
            name='board_pins',
            stream_name='board_pins',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/boards/{board_id}/pins',
                    action=Action.LIST,
                    description='Get a list of pins on a specific board.',
                    query_params=['page_size', 'bookmark'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                    },
                    path_params=['board_id'],
                    path_params_schema={
                        'board_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of board pins',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest pin on a board',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique pin identifier',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the pin was created',
                                        },
                                        'creative_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Creative type (REGULAR, VIDEO, SHOPPING, CAROUSEL, etc.)',
                                        },
                                        'is_standard': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the pin is a standard pin',
                                        },
                                        'is_owner': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the current user is the owner',
                                        },
                                        'dominant_color': {
                                            'type': ['null', 'string'],
                                            'description': 'Dominant color from the pin image (hex)',
                                        },
                                        'parent_pin_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Parent pin ID if this is a repin',
                                        },
                                        'link': {
                                            'type': ['null', 'string'],
                                            'description': 'URL link associated with the pin',
                                        },
                                        'title': {
                                            'type': ['null', 'string'],
                                            'description': 'Pin title',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Pin description',
                                        },
                                        'alt_text': {
                                            'type': ['null', 'string'],
                                            'description': 'Alternate text for accessibility',
                                        },
                                        'board_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Board the pin belongs to',
                                        },
                                        'board_section_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Section within the board',
                                        },
                                        'board_owner': {
                                            'type': ['null', 'object'],
                                            'description': 'Board owner info',
                                            'properties': {
                                                'username': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Username of the board owner',
                                                },
                                            },
                                        },
                                        'media': {
                                            'type': ['null', 'object'],
                                            'description': 'Media content',
                                            'properties': {
                                                'media_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Type of media',
                                                },
                                            },
                                        },
                                        'pin_metrics': {
                                            'type': ['null', 'object'],
                                            'description': 'Pin metrics data',
                                        },
                                        'has_been_promoted': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the pin has been promoted',
                                        },
                                        'is_removable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the pin can be removed',
                                        },
                                        'product_tags': {
                                            'type': ['null', 'array'],
                                            'description': 'Product tags associated with the pin',
                                            'items': {'type': 'object'},
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'board_pins',
                                    'x-airbyte-stream-name': 'board_pins',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest pin on a board',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique pin identifier',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the pin was created',
                    },
                    'creative_type': {
                        'type': ['null', 'string'],
                        'description': 'Creative type (REGULAR, VIDEO, SHOPPING, CAROUSEL, etc.)',
                    },
                    'is_standard': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the pin is a standard pin',
                    },
                    'is_owner': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the current user is the owner',
                    },
                    'dominant_color': {
                        'type': ['null', 'string'],
                        'description': 'Dominant color from the pin image (hex)',
                    },
                    'parent_pin_id': {
                        'type': ['null', 'string'],
                        'description': 'Parent pin ID if this is a repin',
                    },
                    'link': {
                        'type': ['null', 'string'],
                        'description': 'URL link associated with the pin',
                    },
                    'title': {
                        'type': ['null', 'string'],
                        'description': 'Pin title',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Pin description',
                    },
                    'alt_text': {
                        'type': ['null', 'string'],
                        'description': 'Alternate text for accessibility',
                    },
                    'board_id': {
                        'type': ['null', 'string'],
                        'description': 'Board the pin belongs to',
                    },
                    'board_section_id': {
                        'type': ['null', 'string'],
                        'description': 'Section within the board',
                    },
                    'board_owner': {
                        'type': ['null', 'object'],
                        'description': 'Board owner info',
                        'properties': {
                            'username': {
                                'type': ['null', 'string'],
                                'description': 'Username of the board owner',
                            },
                        },
                    },
                    'media': {
                        'type': ['null', 'object'],
                        'description': 'Media content',
                        'properties': {
                            'media_type': {
                                'type': ['null', 'string'],
                                'description': 'Type of media',
                            },
                        },
                    },
                    'pin_metrics': {
                        'type': ['null', 'object'],
                        'description': 'Pin metrics data',
                    },
                    'has_been_promoted': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the pin has been promoted',
                    },
                    'is_removable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the pin can be removed',
                    },
                    'product_tags': {
                        'type': ['null', 'array'],
                        'description': 'Product tags associated with the pin',
                        'items': {'type': 'object'},
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'board_pins',
                'x-airbyte-stream-name': 'board_pins',
            },
        ),
        EntityDefinition(
            name='catalogs',
            stream_name='catalogs',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/catalogs',
                    action=Action.LIST,
                    description='Get a list of catalogs for the authenticated user.',
                    query_params=['page_size', 'bookmark'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of catalogs',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest catalog object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique catalog identifier',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the catalog was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the catalog was last updated',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Catalog name',
                                        },
                                        'catalog_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Type of catalog (RETAIL, HOTEL, CREATIVE_ASSETS)',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'catalogs',
                                    'x-airbyte-stream-name': 'catalogs',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest catalog object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique catalog identifier',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the catalog was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the catalog was last updated',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Catalog name',
                    },
                    'catalog_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of catalog (RETAIL, HOTEL, CREATIVE_ASSETS)',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'catalogs',
                'x-airbyte-stream-name': 'catalogs',
            },
        ),
        EntityDefinition(
            name='catalogs_feeds',
            stream_name='catalogs_feeds',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/catalogs/feeds',
                    action=Action.LIST,
                    description='Get a list of catalog feeds for the authenticated user.',
                    query_params=['page_size', 'bookmark'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of catalog feeds',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest catalog feed object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique feed identifier',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the feed was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the feed was last updated',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Feed name',
                                        },
                                        'format': {
                                            'type': ['null', 'string'],
                                            'description': 'Feed format (TSV, CSV, XML)',
                                        },
                                        'catalog_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Type of catalog',
                                        },
                                        'location': {
                                            'type': ['null', 'string'],
                                            'description': 'URL where the feed is available',
                                        },
                                        'preferred_processing_schedule': {
                                            'type': ['null', 'object'],
                                            'description': 'Preferred processing schedule',
                                            'properties': {
                                                'time': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Preferred processing time',
                                                },
                                                'timezone': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Timezone for processing',
                                                },
                                            },
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Feed status (ACTIVE, INACTIVE)',
                                        },
                                        'default_currency': {
                                            'type': ['null', 'string'],
                                            'description': 'Default currency for pricing',
                                        },
                                        'default_locale': {
                                            'type': ['null', 'string'],
                                            'description': 'Default locale',
                                        },
                                        'default_country': {
                                            'type': ['null', 'string'],
                                            'description': 'Default country',
                                        },
                                        'default_availability': {
                                            'type': ['null', 'string'],
                                            'description': 'Default availability status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'catalogs_feeds',
                                    'x-airbyte-stream-name': 'catalogs_feeds',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest catalog feed object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique feed identifier',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the feed was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the feed was last updated',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Feed name',
                    },
                    'format': {
                        'type': ['null', 'string'],
                        'description': 'Feed format (TSV, CSV, XML)',
                    },
                    'catalog_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of catalog',
                    },
                    'location': {
                        'type': ['null', 'string'],
                        'description': 'URL where the feed is available',
                    },
                    'preferred_processing_schedule': {
                        'type': ['null', 'object'],
                        'description': 'Preferred processing schedule',
                        'properties': {
                            'time': {
                                'type': ['null', 'string'],
                                'description': 'Preferred processing time',
                            },
                            'timezone': {
                                'type': ['null', 'string'],
                                'description': 'Timezone for processing',
                            },
                        },
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Feed status (ACTIVE, INACTIVE)',
                    },
                    'default_currency': {
                        'type': ['null', 'string'],
                        'description': 'Default currency for pricing',
                    },
                    'default_locale': {
                        'type': ['null', 'string'],
                        'description': 'Default locale',
                    },
                    'default_country': {
                        'type': ['null', 'string'],
                        'description': 'Default country',
                    },
                    'default_availability': {
                        'type': ['null', 'string'],
                        'description': 'Default availability status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'catalogs_feeds',
                'x-airbyte-stream-name': 'catalogs_feeds',
            },
        ),
        EntityDefinition(
            name='catalogs_product_groups',
            stream_name='catalogs_product_groups',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/catalogs/product_groups',
                    action=Action.LIST,
                    description='Get a list of catalog product groups for the authenticated user.',
                    query_params=['page_size', 'bookmark'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of catalog product groups',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest catalog product group object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique product group identifier',
                                        },
                                        'created_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix seconds)',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix seconds)',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Product group name',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Product group description',
                                        },
                                        'feed_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Associated feed ID',
                                        },
                                        'is_featured': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the product group is featured',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Product group status',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Product group type',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'catalogs_product_groups',
                                    'x-airbyte-stream-name': 'catalogs_product_groups',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest catalog product group object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique product group identifier',
                    },
                    'created_at': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix seconds)',
                    },
                    'updated_at': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix seconds)',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Product group name',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Product group description',
                    },
                    'feed_id': {
                        'type': ['null', 'string'],
                        'description': 'Associated feed ID',
                    },
                    'is_featured': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the product group is featured',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Product group status',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Product group type',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'catalogs_product_groups',
                'x-airbyte-stream-name': 'catalogs_product_groups',
            },
        ),
        EntityDefinition(
            name='audiences',
            stream_name='audiences',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts/{ad_account_id}/audiences',
                    action=Action.LIST,
                    description='Get a list of audiences for the specified ad account.',
                    query_params=['page_size', 'bookmark'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                    },
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of audiences',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest audience object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique audience identifier',
                                        },
                                        'ad_account_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad account ID',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Audience name',
                                        },
                                        'audience_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Audience type (ACTALIKE, ENGAGEMENT, CUSTOMER_LIST, VISITOR)',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Audience description',
                                        },
                                        'rule': {
                                            'type': ['null', 'object'],
                                            'description': 'Audience targeting rules',
                                            'properties': {
                                                'country': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Country criteria',
                                                },
                                                'customer_list_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Customer list ID',
                                                },
                                                'engagement_domain': {
                                                    'type': ['null', 'array'],
                                                    'description': 'Domains for engagement tracking',
                                                    'items': {'type': 'string'},
                                                },
                                                'engagement_type': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Engagement type',
                                                },
                                                'event': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Pinterest tag event',
                                                },
                                                'retention_days': {
                                                    'type': ['null', 'integer'],
                                                    'description': 'Days to retain audience data',
                                                },
                                                'visitor_source_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Visitor source ID',
                                                },
                                            },
                                        },
                                        'size': {
                                            'type': ['null', 'integer'],
                                            'description': 'Estimated audience size',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Audience status (READY, INITIALIZING, TOO_SMALL)',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': "Always 'audience'",
                                        },
                                        'created_timestamp': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation time (Unix seconds)',
                                        },
                                        'updated_timestamp': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update time (Unix seconds)',
                                        },
                                        'created_by_company_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the company that created the audience',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'audiences',
                                    'x-airbyte-stream-name': 'audiences',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest audience object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique audience identifier',
                    },
                    'ad_account_id': {
                        'type': ['null', 'string'],
                        'description': 'Ad account ID',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Audience name',
                    },
                    'audience_type': {
                        'type': ['null', 'string'],
                        'description': 'Audience type (ACTALIKE, ENGAGEMENT, CUSTOMER_LIST, VISITOR)',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Audience description',
                    },
                    'rule': {
                        'type': ['null', 'object'],
                        'description': 'Audience targeting rules',
                        'properties': {
                            'country': {
                                'type': ['null', 'string'],
                                'description': 'Country criteria',
                            },
                            'customer_list_id': {
                                'type': ['null', 'string'],
                                'description': 'Customer list ID',
                            },
                            'engagement_domain': {
                                'type': ['null', 'array'],
                                'description': 'Domains for engagement tracking',
                                'items': {'type': 'string'},
                            },
                            'engagement_type': {
                                'type': ['null', 'string'],
                                'description': 'Engagement type',
                            },
                            'event': {
                                'type': ['null', 'string'],
                                'description': 'Pinterest tag event',
                            },
                            'retention_days': {
                                'type': ['null', 'integer'],
                                'description': 'Days to retain audience data',
                            },
                            'visitor_source_id': {
                                'type': ['null', 'string'],
                                'description': 'Visitor source ID',
                            },
                        },
                    },
                    'size': {
                        'type': ['null', 'integer'],
                        'description': 'Estimated audience size',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Audience status (READY, INITIALIZING, TOO_SMALL)',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': "Always 'audience'",
                    },
                    'created_timestamp': {
                        'type': ['null', 'integer'],
                        'description': 'Creation time (Unix seconds)',
                    },
                    'updated_timestamp': {
                        'type': ['null', 'integer'],
                        'description': 'Last update time (Unix seconds)',
                    },
                    'created_by_company_name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the company that created the audience',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'audiences',
                'x-airbyte-stream-name': 'audiences',
            },
        ),
        EntityDefinition(
            name='conversion_tags',
            stream_name='conversion_tags',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts/{ad_account_id}/conversion_tags',
                    action=Action.LIST,
                    description='Get a list of conversion tags for the specified ad account.',
                    query_params=['page_size', 'bookmark'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                    },
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of conversion tags',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest conversion tag object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique conversion tag identifier',
                                        },
                                        'ad_account_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad account ID',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Conversion tag name',
                                        },
                                        'code_snippet': {
                                            'type': ['null', 'string'],
                                            'description': 'JavaScript code snippet for tracking',
                                        },
                                        'enhanced_match_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Enhanced match status',
                                        },
                                        'last_fired_time_ms': {
                                            'type': ['null', 'integer'],
                                            'description': 'Timestamp of last event fired (milliseconds)',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Status (ACTIVE, PAUSED, ARCHIVED)',
                                        },
                                        'version': {
                                            'type': ['null', 'string'],
                                            'description': 'Version number',
                                        },
                                        'configs': {
                                            'type': ['null', 'object'],
                                            'description': 'Tag configurations',
                                            'properties': {
                                                'aem_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'AEM email integration enabled',
                                                },
                                                'md_frequency': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Metadata ingestion frequency',
                                                },
                                                'aem_fnln_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'AEM name integration enabled',
                                                },
                                                'aem_ph_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'AEM phone integration enabled',
                                                },
                                                'aem_ge_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'AEM gender integration enabled',
                                                },
                                                'aem_db_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'AEM birthdate integration enabled',
                                                },
                                                'aem_loc_enabled': {
                                                    'type': ['null', 'boolean'],
                                                    'description': 'AEM location integration enabled',
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'conversion_tags',
                                    'x-airbyte-stream-name': 'conversion_tags',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest conversion tag object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique conversion tag identifier',
                    },
                    'ad_account_id': {
                        'type': ['null', 'string'],
                        'description': 'Ad account ID',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Conversion tag name',
                    },
                    'code_snippet': {
                        'type': ['null', 'string'],
                        'description': 'JavaScript code snippet for tracking',
                    },
                    'enhanced_match_status': {
                        'type': ['null', 'string'],
                        'description': 'Enhanced match status',
                    },
                    'last_fired_time_ms': {
                        'type': ['null', 'integer'],
                        'description': 'Timestamp of last event fired (milliseconds)',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Status (ACTIVE, PAUSED, ARCHIVED)',
                    },
                    'version': {
                        'type': ['null', 'string'],
                        'description': 'Version number',
                    },
                    'configs': {
                        'type': ['null', 'object'],
                        'description': 'Tag configurations',
                        'properties': {
                            'aem_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'AEM email integration enabled',
                            },
                            'md_frequency': {
                                'type': ['null', 'number'],
                                'description': 'Metadata ingestion frequency',
                            },
                            'aem_fnln_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'AEM name integration enabled',
                            },
                            'aem_ph_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'AEM phone integration enabled',
                            },
                            'aem_ge_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'AEM gender integration enabled',
                            },
                            'aem_db_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'AEM birthdate integration enabled',
                            },
                            'aem_loc_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'AEM location integration enabled',
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'conversion_tags',
                'x-airbyte-stream-name': 'conversion_tags',
            },
        ),
        EntityDefinition(
            name='customer_lists',
            stream_name='customer_lists',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts/{ad_account_id}/customer_lists',
                    action=Action.LIST,
                    description='Get a list of customer lists for the specified ad account.',
                    query_params=['page_size', 'bookmark'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                    },
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of customer lists',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest customer list object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique customer list identifier',
                                        },
                                        'ad_account_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Associated ad account ID',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Customer list name',
                                        },
                                        'created_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation time (Unix seconds)',
                                        },
                                        'updated_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update time (Unix seconds)',
                                        },
                                        'num_batches': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total number of list updates',
                                        },
                                        'num_removed_user_records': {
                                            'type': ['null', 'integer'],
                                            'description': 'Count of removed user records',
                                        },
                                        'num_uploaded_user_records': {
                                            'type': ['null', 'integer'],
                                            'description': 'Count of uploaded user records',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Status (PROCESSING, READY, TOO_SMALL, UPLOADING)',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': "Always 'customerlist'",
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'customer_lists',
                                    'x-airbyte-stream-name': 'customer_lists',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest customer list object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique customer list identifier',
                    },
                    'ad_account_id': {
                        'type': ['null', 'string'],
                        'description': 'Associated ad account ID',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Customer list name',
                    },
                    'created_time': {
                        'type': ['null', 'integer'],
                        'description': 'Creation time (Unix seconds)',
                    },
                    'updated_time': {
                        'type': ['null', 'integer'],
                        'description': 'Last update time (Unix seconds)',
                    },
                    'num_batches': {
                        'type': ['null', 'integer'],
                        'description': 'Total number of list updates',
                    },
                    'num_removed_user_records': {
                        'type': ['null', 'integer'],
                        'description': 'Count of removed user records',
                    },
                    'num_uploaded_user_records': {
                        'type': ['null', 'integer'],
                        'description': 'Count of uploaded user records',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Status (PROCESSING, READY, TOO_SMALL, UPLOADING)',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': "Always 'customerlist'",
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'customer_lists',
                'x-airbyte-stream-name': 'customer_lists',
            },
        ),
        EntityDefinition(
            name='keywords',
            stream_name='keywords',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts/{ad_account_id}/keywords',
                    action=Action.LIST,
                    description='Get a list of keywords for the specified ad account. Requires an ad_group_id filter.',
                    query_params=['ad_group_id', 'page_size', 'bookmark'],
                    query_params_schema={
                        'ad_group_id': {'type': 'string', 'required': True},
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'bookmark': {'type': 'string', 'required': False},
                    },
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of keywords',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Pinterest keyword object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique keyword identifier',
                                        },
                                        'archived': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the keyword is archived',
                                        },
                                        'parent_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Parent entity ID',
                                        },
                                        'parent_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Parent entity type',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': "Always 'keyword'",
                                        },
                                        'bid': {
                                            'type': ['null', 'integer'],
                                            'description': 'Bid value in microcurrency',
                                        },
                                        'match_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Match type (BROAD, PHRASE, EXACT, EXACT_NEGATIVE, PHRASE_NEGATIVE, BROAD_NEGATIVE)',
                                        },
                                        'value': {
                                            'type': ['null', 'string'],
                                            'description': 'Keyword text value',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'keywords',
                                    'x-airbyte-stream-name': 'keywords',
                                },
                            },
                            'bookmark': {
                                'type': ['null', 'string'],
                                'description': 'Cursor for next page of results',
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'bookmark': '$.bookmark'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Pinterest keyword object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique keyword identifier',
                    },
                    'archived': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the keyword is archived',
                    },
                    'parent_id': {
                        'type': ['null', 'string'],
                        'description': 'Parent entity ID',
                    },
                    'parent_type': {
                        'type': ['null', 'string'],
                        'description': 'Parent entity type',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': "Always 'keyword'",
                    },
                    'bid': {
                        'type': ['null', 'integer'],
                        'description': 'Bid value in microcurrency',
                    },
                    'match_type': {
                        'type': ['null', 'string'],
                        'description': 'Match type (BROAD, PHRASE, EXACT, EXACT_NEGATIVE, PHRASE_NEGATIVE, BROAD_NEGATIVE)',
                    },
                    'value': {
                        'type': ['null', 'string'],
                        'description': 'Keyword text value',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'keywords',
                'x-airbyte-stream-name': 'keywords',
            },
        ),
    ],
    search_field_paths={
        'ad_accounts': [
            'country',
            'created_time',
            'currency',
            'id',
            'name',
            'owner',
            'owner.id',
            'owner.username',
            'permissions',
            'permissions[]',
            'updated_time',
        ],
        'boards': [
            'board_pins_modified_at',
            'collaborator_count',
            'created_at',
            'description',
            'follower_count',
            'id',
            'media',
            'name',
            'owner',
            'owner.username',
            'pin_count',
            'privacy',
        ],
        'campaigns': [
            'ad_account_id',
            'created_time',
            'daily_spend_cap',
            'end_time',
            'id',
            'is_campaign_budget_optimization',
            'is_flexible_daily_budgets',
            'lifetime_spend_cap',
            'name',
            'objective_type',
            'order_line_id',
            'start_time',
            'status',
            'summary_status',
            'tracking_urls',
            'type',
            'updated_time',
        ],
        'ad_groups': [
            'ad_account_id',
            'auto_targeting_enabled',
            'bid_in_micro_currency',
            'bid_strategy_type',
            'billable_event',
            'budget_in_micro_currency',
            'budget_type',
            'campaign_id',
            'conversion_learning_mode_type',
            'created_time',
            'end_time',
            'feed_profile_id',
            'id',
            'lifetime_frequency_cap',
            'name',
            'optimization_goal_metadata',
            'pacing_delivery_type',
            'placement_group',
            'start_time',
            'status',
            'summary_status',
            'targeting_spec',
            'tracking_urls',
            'type',
            'updated_time',
        ],
        'ads': [
            'ad_account_id',
            'ad_group_id',
            'android_deep_link',
            'campaign_id',
            'carousel_android_deep_links',
            'carousel_android_deep_links[]',
            'carousel_destination_urls',
            'carousel_destination_urls[]',
            'carousel_ios_deep_links',
            'carousel_ios_deep_links[]',
            'click_tracking_url',
            'collection_items_destination_url_template',
            'created_time',
            'creative_type',
            'destination_url',
            'id',
            'ios_deep_link',
            'is_pin_deleted',
            'is_removable',
            'lead_form_id',
            'name',
            'pin_id',
            'rejected_reasons',
            'rejected_reasons[]',
            'rejection_labels',
            'rejection_labels[]',
            'review_status',
            'status',
            'summary_status',
            'tracking_urls',
            'type',
            'updated_time',
            'view_tracking_url',
        ],
        'board_sections': ['id', 'name'],
        'board_pins': [
            'alt_text',
            'board_id',
            'board_owner',
            'board_owner.username',
            'board_section_id',
            'created_at',
            'creative_type',
            'description',
            'dominant_color',
            'has_been_promoted',
            'id',
            'is_owner',
            'is_standard',
            'link',
            'media',
            'parent_pin_id',
            'pin_metrics',
            'title',
        ],
        'catalogs': [
            'catalog_type',
            'created_at',
            'id',
            'name',
            'updated_at',
        ],
        'catalogs_feeds': [
            'catalog_type',
            'created_at',
            'default_availability',
            'default_country',
            'default_currency',
            'default_locale',
            'format',
            'id',
            'location',
            'name',
            'preferred_processing_schedule',
            'status',
            'updated_at',
        ],
        'catalogs_product_groups': [
            'created_at',
            'description',
            'feed_id',
            'id',
            'is_featured',
            'name',
            'status',
            'type',
            'updated_at',
        ],
        'audiences': [
            'ad_account_id',
            'audience_type',
            'created_timestamp',
            'description',
            'id',
            'name',
            'rule',
            'size',
            'status',
            'type',
            'updated_timestamp',
        ],
        'conversion_tags': [
            'ad_account_id',
            'code_snippet',
            'configs',
            'enhanced_match_status',
            'id',
            'last_fired_time_ms',
            'name',
            'status',
            'version',
        ],
        'customer_lists': [
            'ad_account_id',
            'created_time',
            'id',
            'name',
            'num_batches',
            'num_removed_user_records',
            'num_uploaded_user_records',
            'status',
            'type',
            'updated_time',
        ],
        'keywords': [
            'archived',
            'bid',
            'id',
            'match_type',
            'parent_id',
            'parent_type',
            'type',
            'value',
        ],
    },
)