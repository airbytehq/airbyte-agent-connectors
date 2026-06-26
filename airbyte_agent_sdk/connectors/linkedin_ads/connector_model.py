"""
Connector model for linkedin-ads.

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
    EntityRelationshipConfig,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from airbyte_agent_sdk.schema.components import (
    PathOverrideConfig,
)
from uuid import (
    UUID,
)

LinkedinAdsConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('137ece28-5434-455c-8f34-69dc3782f451'),
    name='linkedin-ads',
    version='1.0.6',
    base_url='https://api.linkedin.com/rest',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://www.linkedin.com/oauth/v2/accessToken',
            'auth_style': 'body',
            'body_format': 'form',
        },
        user_config_spec=AuthConfigSpec(
            title='OAuth 2.0 Authentication',
            type='object',
            required=['refresh_token', 'client_id', 'client_secret'],
            properties={
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='OAuth 2.0 refresh token for automatic renewal',
                ),
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='OAuth 2.0 application client ID',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='OAuth 2.0 application client secret',
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
            replication_auth_key_constants={'credentials.auth_method': 'oAuth2.0'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='accounts',
            stream_name='accounts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/adAccounts',
                    action=Action.LIST,
                    description='Returns a list of ad accounts the authenticated user has access to',
                    query_params=['q', 'pageSize', 'pageToken'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'search',
                        },
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                    },
                    header_params=['LinkedIn-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of ad accounts',
                        'properties': {
                            'elements': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'LinkedIn ad account object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique account identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Account name',
                                        },
                                        'currency': {
                                            'type': ['null', 'string'],
                                            'description': 'Currency code used by the account',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Account status (ACTIVE, PAUSED, etc.)',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Account type',
                                        },
                                        'reference': {
                                            'type': ['null', 'string'],
                                            'description': 'Reference organization URN',
                                        },
                                        'test': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is a test account',
                                        },
                                        'changeAuditStamps': {
                                            'type': ['null', 'object'],
                                            'description': 'Creation and last modification audit stamps',
                                            'properties': {
                                                'created': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'actor': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'time': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                    },
                                                },
                                                'lastModified': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'actor': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'time': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'notifiedOnCampaignOptimization': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Notification flag for campaign optimization',
                                        },
                                        'notifiedOnCreativeApproval': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Notification flag for creative approval',
                                        },
                                        'notifiedOnCreativeRejection': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Notification flag for creative rejection',
                                        },
                                        'notifiedOnEndOfCampaign': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Notification flag for end of campaign',
                                        },
                                        'notifiedOnNewFeaturesEnabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Notification flag for new features',
                                        },
                                        'servingStatuses': {
                                            'type': ['null', 'array'],
                                            'description': 'List of serving statuses',
                                            'items': {'type': 'string'},
                                        },
                                        'version': {
                                            'type': ['null', 'object'],
                                            'description': 'Version information',
                                            'properties': {
                                                'versionTag': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'accounts',
                                    'x-airbyte-stream-name': 'accounts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'LinkedIn Ads accounts with status and billing information',
                                        'when_to_use': 'Questions about ad account details or account-level settings',
                                        'trigger_phrases': ['linkedin ads account', 'ad account'],
                                        'freshness': 'live',
                                        'example_questions': ['What LinkedIn Ads accounts do I have?'],
                                        'search_strategy': 'List all accessible accounts',
                                    },
                                },
                            },
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'nextPageToken': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.elements',
                    record_transform={'account_urn': 'urn:li:sponsoredAccount:{{ record.id }}'},
                    meta_extractor={'nextPageToken': '$.metadata.nextPageToken'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/adAccounts/{id}',
                    action=Action.GET,
                    description='Get a single ad account by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    header_params=['LinkedIn-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'LinkedIn ad account object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique account identifier',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Account name',
                            },
                            'currency': {
                                'type': ['null', 'string'],
                                'description': 'Currency code used by the account',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'Account status (ACTIVE, PAUSED, etc.)',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'Account type',
                            },
                            'reference': {
                                'type': ['null', 'string'],
                                'description': 'Reference organization URN',
                            },
                            'test': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether this is a test account',
                            },
                            'changeAuditStamps': {
                                'type': ['null', 'object'],
                                'description': 'Creation and last modification audit stamps',
                                'properties': {
                                    'created': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'actor': {
                                                'type': ['null', 'string'],
                                            },
                                            'time': {
                                                'type': ['null', 'integer'],
                                            },
                                        },
                                    },
                                    'lastModified': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'actor': {
                                                'type': ['null', 'string'],
                                            },
                                            'time': {
                                                'type': ['null', 'integer'],
                                            },
                                        },
                                    },
                                },
                            },
                            'notifiedOnCampaignOptimization': {
                                'type': ['null', 'boolean'],
                                'description': 'Notification flag for campaign optimization',
                            },
                            'notifiedOnCreativeApproval': {
                                'type': ['null', 'boolean'],
                                'description': 'Notification flag for creative approval',
                            },
                            'notifiedOnCreativeRejection': {
                                'type': ['null', 'boolean'],
                                'description': 'Notification flag for creative rejection',
                            },
                            'notifiedOnEndOfCampaign': {
                                'type': ['null', 'boolean'],
                                'description': 'Notification flag for end of campaign',
                            },
                            'notifiedOnNewFeaturesEnabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Notification flag for new features',
                            },
                            'servingStatuses': {
                                'type': ['null', 'array'],
                                'description': 'List of serving statuses',
                                'items': {'type': 'string'},
                            },
                            'version': {
                                'type': ['null', 'object'],
                                'description': 'Version information',
                                'properties': {
                                    'versionTag': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'accounts',
                        'x-airbyte-stream-name': 'accounts',
                        'x-airbyte-ai-hints': {
                            'summary': 'LinkedIn Ads accounts with status and billing information',
                            'when_to_use': 'Questions about ad account details or account-level settings',
                            'trigger_phrases': ['linkedin ads account', 'ad account'],
                            'freshness': 'live',
                            'example_questions': ['What LinkedIn Ads accounts do I have?'],
                            'search_strategy': 'List all accessible accounts',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'LinkedIn ad account object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique account identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Account name',
                    },
                    'currency': {
                        'type': ['null', 'string'],
                        'description': 'Currency code used by the account',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Account status (ACTIVE, PAUSED, etc.)',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Account type',
                    },
                    'reference': {
                        'type': ['null', 'string'],
                        'description': 'Reference organization URN',
                    },
                    'test': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is a test account',
                    },
                    'changeAuditStamps': {
                        'type': ['null', 'object'],
                        'description': 'Creation and last modification audit stamps',
                        'properties': {
                            'created': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'actor': {
                                        'type': ['null', 'string'],
                                    },
                                    'time': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                            },
                            'lastModified': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'actor': {
                                        'type': ['null', 'string'],
                                    },
                                    'time': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                            },
                        },
                    },
                    'notifiedOnCampaignOptimization': {
                        'type': ['null', 'boolean'],
                        'description': 'Notification flag for campaign optimization',
                    },
                    'notifiedOnCreativeApproval': {
                        'type': ['null', 'boolean'],
                        'description': 'Notification flag for creative approval',
                    },
                    'notifiedOnCreativeRejection': {
                        'type': ['null', 'boolean'],
                        'description': 'Notification flag for creative rejection',
                    },
                    'notifiedOnEndOfCampaign': {
                        'type': ['null', 'boolean'],
                        'description': 'Notification flag for end of campaign',
                    },
                    'notifiedOnNewFeaturesEnabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Notification flag for new features',
                    },
                    'servingStatuses': {
                        'type': ['null', 'array'],
                        'description': 'List of serving statuses',
                        'items': {'type': 'string'},
                    },
                    'version': {
                        'type': ['null', 'object'],
                        'description': 'Version information',
                        'properties': {
                            'versionTag': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'accounts',
                'x-airbyte-stream-name': 'accounts',
                'x-airbyte-ai-hints': {
                    'summary': 'LinkedIn Ads accounts with status and billing information',
                    'when_to_use': 'Questions about ad account details or account-level settings',
                    'trigger_phrases': ['linkedin ads account', 'ad account'],
                    'freshness': 'live',
                    'example_questions': ['What LinkedIn Ads accounts do I have?'],
                    'search_strategy': 'List all accessible accounts',
                },
            },
            ai_hints={
                'summary': 'LinkedIn Ads accounts with status and billing information',
                'when_to_use': 'Questions about ad account details or account-level settings',
                'trigger_phrases': ['linkedin ads account', 'ad account'],
                'freshness': 'live',
                'example_questions': ['What LinkedIn Ads accounts do I have?'],
                'search_strategy': 'List all accessible accounts',
            },
        ),
        EntityDefinition(
            name='account_users',
            stream_name='account_users',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/adAccountUsers',
                    action=Action.LIST,
                    description='Returns a list of users associated with ad accounts',
                    query_params=[
                        'q',
                        'accounts',
                        'count',
                        'start',
                    ],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'accounts',
                        },
                        'accounts': {'type': 'string', 'required': True},
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'start': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                            'minimum': 0,
                        },
                    },
                    header_params=['LinkedIn-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of account users',
                        'properties': {
                            'elements': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'LinkedIn ad account user object',
                                    'properties': {
                                        'account': {
                                            'type': ['null', 'string'],
                                            'description': 'Associated account URN',
                                        },
                                        'user': {
                                            'type': ['null', 'string'],
                                            'description': 'User URN',
                                        },
                                        'role': {
                                            'type': ['null', 'string'],
                                            'description': 'User role in the account',
                                        },
                                        'changeAuditStamps': {
                                            'type': ['null', 'object'],
                                            'description': 'Creation and last modification audit stamps',
                                            'properties': {
                                                'created': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'actor': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'time': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                    },
                                                },
                                                'lastModified': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'actor': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'time': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'account_users',
                                    'x-airbyte-stream-name': 'account_users',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Users with access to LinkedIn Ads accounts and their roles',
                                        'when_to_use': 'Questions about who has access to ad accounts',
                                        'trigger_phrases': ['account user', 'ad account access', 'who has access'],
                                        'freshness': 'live',
                                        'example_questions': ['Who has access to this LinkedIn Ads account?'],
                                        'search_strategy': 'Filter by account',
                                    },
                                },
                            },
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'nextPageToken': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.elements',
                    meta_extractor={'nextPageToken': '$.metadata.nextPageToken'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'LinkedIn ad account user object',
                'properties': {
                    'account': {
                        'type': ['null', 'string'],
                        'description': 'Associated account URN',
                    },
                    'user': {
                        'type': ['null', 'string'],
                        'description': 'User URN',
                    },
                    'role': {
                        'type': ['null', 'string'],
                        'description': 'User role in the account',
                    },
                    'changeAuditStamps': {
                        'type': ['null', 'object'],
                        'description': 'Creation and last modification audit stamps',
                        'properties': {
                            'created': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'actor': {
                                        'type': ['null', 'string'],
                                    },
                                    'time': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                            },
                            'lastModified': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'actor': {
                                        'type': ['null', 'string'],
                                    },
                                    'time': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                            },
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'account_users',
                'x-airbyte-stream-name': 'account_users',
                'x-airbyte-ai-hints': {
                    'summary': 'Users with access to LinkedIn Ads accounts and their roles',
                    'when_to_use': 'Questions about who has access to ad accounts',
                    'trigger_phrases': ['account user', 'ad account access', 'who has access'],
                    'freshness': 'live',
                    'example_questions': ['Who has access to this LinkedIn Ads account?'],
                    'search_strategy': 'Filter by account',
                },
            },
            ai_hints={
                'summary': 'Users with access to LinkedIn Ads accounts and their roles',
                'when_to_use': 'Questions about who has access to ad accounts',
                'trigger_phrases': ['account user', 'ad account access', 'who has access'],
                'freshness': 'live',
                'example_questions': ['Who has access to this LinkedIn Ads account?'],
                'search_strategy': 'Filter by account',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='account_users',
                    target_entity='accounts',
                    foreign_key='accounts',
                    target_key='account_urn',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='campaigns',
            stream_name='campaigns',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/adAccounts/{account_id}/adCampaigns',
                    action=Action.LIST,
                    description='Returns a list of campaigns for an ad account',
                    query_params=['q', 'pageSize', 'pageToken'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'search',
                        },
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'integer', 'required': True},
                    },
                    header_params=['LinkedIn-Version', 'X-Restli-Protocol-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                        'X-Restli-Protocol-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2.0.0',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of campaigns',
                        'properties': {
                            'elements': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'LinkedIn ad campaign object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique campaign identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign name',
                                        },
                                        'account': {
                                            'type': ['null', 'string'],
                                            'description': 'Associated account URN',
                                        },
                                        'campaignGroup': {
                                            'type': ['null', 'string'],
                                            'description': 'Parent campaign group URN',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign status',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign type',
                                        },
                                        'costType': {
                                            'type': ['null', 'string'],
                                            'description': 'Cost type (CPC, CPM, etc.)',
                                        },
                                        'format': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign ad format',
                                        },
                                        'objectiveType': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign objective type',
                                        },
                                        'optimizationTargetType': {
                                            'type': ['null', 'string'],
                                            'description': 'Optimization target type',
                                        },
                                        'creativeSelection': {
                                            'type': ['null', 'string'],
                                            'description': 'Creative selection mode',
                                        },
                                        'pacingStrategy': {
                                            'type': ['null', 'string'],
                                            'description': 'Budget pacing strategy',
                                        },
                                        'audienceExpansionEnabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether audience expansion is enabled',
                                        },
                                        'offsiteDeliveryEnabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether offsite delivery is enabled',
                                        },
                                        'storyDeliveryEnabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether story delivery is enabled',
                                        },
                                        'test': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is a test campaign',
                                        },
                                        'associatedEntity': {
                                            'type': ['null', 'string'],
                                            'description': 'Associated entity URN',
                                        },
                                        'connectedTelevisionOnly': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the campaign targets connected television only',
                                        },
                                        'politicalIntent': {
                                            'type': ['null', 'string'],
                                            'description': 'Political intent status of the campaign (e.g., NOT_POLITICAL)',
                                        },
                                        'changeAuditStamps': {
                                            'type': ['null', 'object'],
                                            'description': 'Creation and last modification audit stamps',
                                            'properties': {
                                                'created': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'actor': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'time': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                    },
                                                },
                                                'lastModified': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'actor': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'time': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'dailyBudget': {
                                            'type': ['null', 'object'],
                                            'description': 'Daily budget configuration',
                                            'properties': {
                                                'amount': {
                                                    'type': ['null', 'string'],
                                                },
                                                'currencyCode': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'totalBudget': {
                                            'type': ['null', 'object'],
                                            'description': 'Total budget configuration',
                                            'properties': {
                                                'amount': {
                                                    'type': ['null', 'string'],
                                                },
                                                'currencyCode': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'unitCost': {
                                            'type': ['null', 'object'],
                                            'description': 'Cost per unit (bid amount)',
                                            'properties': {
                                                'amount': {
                                                    'type': ['null', 'string'],
                                                },
                                                'currencyCode': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'runSchedule': {
                                            'type': ['null', 'object'],
                                            'description': 'Campaign run schedule',
                                            'properties': {
                                                'start': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'end': {
                                                    'type': ['null', 'integer'],
                                                },
                                            },
                                        },
                                        'locale': {
                                            'type': ['null', 'object'],
                                            'description': 'Campaign locale settings',
                                            'properties': {
                                                'country': {
                                                    'type': ['null', 'string'],
                                                },
                                                'language': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'targetingCriteria': {
                                            'type': ['null', 'object'],
                                            'description': 'Targeting criteria for the campaign',
                                        },
                                        'offsitePreferences': {
                                            'type': ['null', 'object'],
                                            'description': 'Offsite delivery preferences',
                                        },
                                        'servingStatuses': {
                                            'type': ['null', 'array'],
                                            'description': 'List of serving statuses',
                                            'items': {'type': 'string'},
                                        },
                                        'version': {
                                            'type': ['null', 'object'],
                                            'description': 'Version information',
                                            'properties': {
                                                'versionTag': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'campaigns',
                                    'x-airbyte-stream-name': 'campaigns',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'LinkedIn ad campaigns with targeting, budget, and status',
                                        'when_to_use': 'Questions about campaign configuration, status, or performance',
                                        'trigger_phrases': ['linkedin campaign', 'ad campaign', 'campaign status'],
                                        'freshness': 'live',
                                        'example_questions': ['Show active LinkedIn campaigns'],
                                        'search_strategy': 'Search by name or filter by status',
                                    },
                                },
                            },
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'nextPageToken': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.elements',
                    record_transform={'campaign_analytics_param': 'List(urn:li:sponsoredCampaign:{{ record.id }})'},
                    meta_extractor={'nextPageToken': '$.metadata.nextPageToken'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/adAccounts/{account_id}/adCampaigns/{id}',
                    action=Action.GET,
                    description='Get a single campaign by ID',
                    path_params=['account_id', 'id'],
                    path_params_schema={
                        'account_id': {'type': 'integer', 'required': True},
                        'id': {'type': 'integer', 'required': True},
                    },
                    header_params=['LinkedIn-Version', 'X-Restli-Protocol-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                        'X-Restli-Protocol-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2.0.0',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'LinkedIn ad campaign object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique campaign identifier',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Campaign name',
                            },
                            'account': {
                                'type': ['null', 'string'],
                                'description': 'Associated account URN',
                            },
                            'campaignGroup': {
                                'type': ['null', 'string'],
                                'description': 'Parent campaign group URN',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'Campaign status',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'Campaign type',
                            },
                            'costType': {
                                'type': ['null', 'string'],
                                'description': 'Cost type (CPC, CPM, etc.)',
                            },
                            'format': {
                                'type': ['null', 'string'],
                                'description': 'Campaign ad format',
                            },
                            'objectiveType': {
                                'type': ['null', 'string'],
                                'description': 'Campaign objective type',
                            },
                            'optimizationTargetType': {
                                'type': ['null', 'string'],
                                'description': 'Optimization target type',
                            },
                            'creativeSelection': {
                                'type': ['null', 'string'],
                                'description': 'Creative selection mode',
                            },
                            'pacingStrategy': {
                                'type': ['null', 'string'],
                                'description': 'Budget pacing strategy',
                            },
                            'audienceExpansionEnabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether audience expansion is enabled',
                            },
                            'offsiteDeliveryEnabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether offsite delivery is enabled',
                            },
                            'storyDeliveryEnabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether story delivery is enabled',
                            },
                            'test': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether this is a test campaign',
                            },
                            'associatedEntity': {
                                'type': ['null', 'string'],
                                'description': 'Associated entity URN',
                            },
                            'connectedTelevisionOnly': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the campaign targets connected television only',
                            },
                            'politicalIntent': {
                                'type': ['null', 'string'],
                                'description': 'Political intent status of the campaign (e.g., NOT_POLITICAL)',
                            },
                            'changeAuditStamps': {
                                'type': ['null', 'object'],
                                'description': 'Creation and last modification audit stamps',
                                'properties': {
                                    'created': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'actor': {
                                                'type': ['null', 'string'],
                                            },
                                            'time': {
                                                'type': ['null', 'integer'],
                                            },
                                        },
                                    },
                                    'lastModified': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'actor': {
                                                'type': ['null', 'string'],
                                            },
                                            'time': {
                                                'type': ['null', 'integer'],
                                            },
                                        },
                                    },
                                },
                            },
                            'dailyBudget': {
                                'type': ['null', 'object'],
                                'description': 'Daily budget configuration',
                                'properties': {
                                    'amount': {
                                        'type': ['null', 'string'],
                                    },
                                    'currencyCode': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'totalBudget': {
                                'type': ['null', 'object'],
                                'description': 'Total budget configuration',
                                'properties': {
                                    'amount': {
                                        'type': ['null', 'string'],
                                    },
                                    'currencyCode': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'unitCost': {
                                'type': ['null', 'object'],
                                'description': 'Cost per unit (bid amount)',
                                'properties': {
                                    'amount': {
                                        'type': ['null', 'string'],
                                    },
                                    'currencyCode': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'runSchedule': {
                                'type': ['null', 'object'],
                                'description': 'Campaign run schedule',
                                'properties': {
                                    'start': {
                                        'type': ['null', 'integer'],
                                    },
                                    'end': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                            },
                            'locale': {
                                'type': ['null', 'object'],
                                'description': 'Campaign locale settings',
                                'properties': {
                                    'country': {
                                        'type': ['null', 'string'],
                                    },
                                    'language': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'targetingCriteria': {
                                'type': ['null', 'object'],
                                'description': 'Targeting criteria for the campaign',
                            },
                            'offsitePreferences': {
                                'type': ['null', 'object'],
                                'description': 'Offsite delivery preferences',
                            },
                            'servingStatuses': {
                                'type': ['null', 'array'],
                                'description': 'List of serving statuses',
                                'items': {'type': 'string'},
                            },
                            'version': {
                                'type': ['null', 'object'],
                                'description': 'Version information',
                                'properties': {
                                    'versionTag': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'campaigns',
                        'x-airbyte-stream-name': 'campaigns',
                        'x-airbyte-ai-hints': {
                            'summary': 'LinkedIn ad campaigns with targeting, budget, and status',
                            'when_to_use': 'Questions about campaign configuration, status, or performance',
                            'trigger_phrases': ['linkedin campaign', 'ad campaign', 'campaign status'],
                            'freshness': 'live',
                            'example_questions': ['Show active LinkedIn campaigns'],
                            'search_strategy': 'Search by name or filter by status',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'LinkedIn ad campaign object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique campaign identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Campaign name',
                    },
                    'account': {
                        'type': ['null', 'string'],
                        'description': 'Associated account URN',
                    },
                    'campaignGroup': {
                        'type': ['null', 'string'],
                        'description': 'Parent campaign group URN',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Campaign status',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Campaign type',
                    },
                    'costType': {
                        'type': ['null', 'string'],
                        'description': 'Cost type (CPC, CPM, etc.)',
                    },
                    'format': {
                        'type': ['null', 'string'],
                        'description': 'Campaign ad format',
                    },
                    'objectiveType': {
                        'type': ['null', 'string'],
                        'description': 'Campaign objective type',
                    },
                    'optimizationTargetType': {
                        'type': ['null', 'string'],
                        'description': 'Optimization target type',
                    },
                    'creativeSelection': {
                        'type': ['null', 'string'],
                        'description': 'Creative selection mode',
                    },
                    'pacingStrategy': {
                        'type': ['null', 'string'],
                        'description': 'Budget pacing strategy',
                    },
                    'audienceExpansionEnabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether audience expansion is enabled',
                    },
                    'offsiteDeliveryEnabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether offsite delivery is enabled',
                    },
                    'storyDeliveryEnabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether story delivery is enabled',
                    },
                    'test': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is a test campaign',
                    },
                    'associatedEntity': {
                        'type': ['null', 'string'],
                        'description': 'Associated entity URN',
                    },
                    'connectedTelevisionOnly': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the campaign targets connected television only',
                    },
                    'politicalIntent': {
                        'type': ['null', 'string'],
                        'description': 'Political intent status of the campaign (e.g., NOT_POLITICAL)',
                    },
                    'changeAuditStamps': {
                        'type': ['null', 'object'],
                        'description': 'Creation and last modification audit stamps',
                        'properties': {
                            'created': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'actor': {
                                        'type': ['null', 'string'],
                                    },
                                    'time': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                            },
                            'lastModified': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'actor': {
                                        'type': ['null', 'string'],
                                    },
                                    'time': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                            },
                        },
                    },
                    'dailyBudget': {
                        'type': ['null', 'object'],
                        'description': 'Daily budget configuration',
                        'properties': {
                            'amount': {
                                'type': ['null', 'string'],
                            },
                            'currencyCode': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'totalBudget': {
                        'type': ['null', 'object'],
                        'description': 'Total budget configuration',
                        'properties': {
                            'amount': {
                                'type': ['null', 'string'],
                            },
                            'currencyCode': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'unitCost': {
                        'type': ['null', 'object'],
                        'description': 'Cost per unit (bid amount)',
                        'properties': {
                            'amount': {
                                'type': ['null', 'string'],
                            },
                            'currencyCode': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'runSchedule': {
                        'type': ['null', 'object'],
                        'description': 'Campaign run schedule',
                        'properties': {
                            'start': {
                                'type': ['null', 'integer'],
                            },
                            'end': {
                                'type': ['null', 'integer'],
                            },
                        },
                    },
                    'locale': {
                        'type': ['null', 'object'],
                        'description': 'Campaign locale settings',
                        'properties': {
                            'country': {
                                'type': ['null', 'string'],
                            },
                            'language': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'targetingCriteria': {
                        'type': ['null', 'object'],
                        'description': 'Targeting criteria for the campaign',
                    },
                    'offsitePreferences': {
                        'type': ['null', 'object'],
                        'description': 'Offsite delivery preferences',
                    },
                    'servingStatuses': {
                        'type': ['null', 'array'],
                        'description': 'List of serving statuses',
                        'items': {'type': 'string'},
                    },
                    'version': {
                        'type': ['null', 'object'],
                        'description': 'Version information',
                        'properties': {
                            'versionTag': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'campaigns',
                'x-airbyte-stream-name': 'campaigns',
                'x-airbyte-ai-hints': {
                    'summary': 'LinkedIn ad campaigns with targeting, budget, and status',
                    'when_to_use': 'Questions about campaign configuration, status, or performance',
                    'trigger_phrases': ['linkedin campaign', 'ad campaign', 'campaign status'],
                    'freshness': 'live',
                    'example_questions': ['Show active LinkedIn campaigns'],
                    'search_strategy': 'Search by name or filter by status',
                },
            },
            ai_hints={
                'summary': 'LinkedIn ad campaigns with targeting, budget, and status',
                'when_to_use': 'Questions about campaign configuration, status, or performance',
                'trigger_phrases': ['linkedin campaign', 'ad campaign', 'campaign status'],
                'freshness': 'live',
                'example_questions': ['Show active LinkedIn campaigns'],
                'search_strategy': 'Search by name or filter by status',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='campaigns',
                    target_entity='accounts',
                    foreign_key='account_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='campaign_groups',
            stream_name='campaign_groups',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/adAccounts/{account_id}/adCampaignGroups',
                    action=Action.LIST,
                    description='Returns a list of campaign groups for an ad account',
                    query_params=['q', 'pageSize', 'pageToken'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'search',
                        },
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'integer', 'required': True},
                    },
                    header_params=['LinkedIn-Version', 'X-Restli-Protocol-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                        'X-Restli-Protocol-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2.0.0',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of campaign groups',
                        'properties': {
                            'elements': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'LinkedIn ad campaign group object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique campaign group identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign group name',
                                        },
                                        'account': {
                                            'type': ['null', 'string'],
                                            'description': 'Associated account URN',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign group status',
                                        },
                                        'test': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is a test campaign group',
                                        },
                                        'backfilled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the campaign group is backfilled',
                                        },
                                        'changeAuditStamps': {
                                            'type': ['null', 'object'],
                                            'description': 'Creation and last modification audit stamps',
                                            'properties': {
                                                'created': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'actor': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'time': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                    },
                                                },
                                                'lastModified': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'actor': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'time': {
                                                            'type': ['null', 'integer'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'totalBudget': {
                                            'type': ['null', 'object'],
                                            'description': 'Total budget for the campaign group',
                                            'properties': {
                                                'amount': {
                                                    'type': ['null', 'string'],
                                                },
                                                'currencyCode': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'runSchedule': {
                                            'type': ['null', 'object'],
                                            'description': 'Campaign group run schedule',
                                            'properties': {
                                                'start': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'end': {
                                                    'type': ['null', 'integer'],
                                                },
                                            },
                                        },
                                        'servingStatuses': {
                                            'type': ['null', 'array'],
                                            'description': 'List of serving statuses',
                                            'items': {'type': 'string'},
                                        },
                                        'allowedCampaignTypes': {
                                            'type': ['null', 'array'],
                                            'description': 'Types of campaigns allowed in this group',
                                            'items': {'type': 'string'},
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'campaign_groups',
                                    'x-airbyte-stream-name': 'campaign_groups',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Campaign groups organizing LinkedIn ad campaigns',
                                        'when_to_use': 'Questions about campaign organization or grouping',
                                        'trigger_phrases': ['campaign group', 'campaign folder'],
                                        'freshness': 'live',
                                        'example_questions': ['What campaign groups exist?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'nextPageToken': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.elements',
                    meta_extractor={'nextPageToken': '$.metadata.nextPageToken'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/adAccounts/{account_id}/adCampaignGroups/{id}',
                    action=Action.GET,
                    description='Get a single campaign group by ID',
                    path_params=['account_id', 'id'],
                    path_params_schema={
                        'account_id': {'type': 'integer', 'required': True},
                        'id': {'type': 'integer', 'required': True},
                    },
                    header_params=['LinkedIn-Version', 'X-Restli-Protocol-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                        'X-Restli-Protocol-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2.0.0',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'LinkedIn ad campaign group object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique campaign group identifier',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Campaign group name',
                            },
                            'account': {
                                'type': ['null', 'string'],
                                'description': 'Associated account URN',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'Campaign group status',
                            },
                            'test': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether this is a test campaign group',
                            },
                            'backfilled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the campaign group is backfilled',
                            },
                            'changeAuditStamps': {
                                'type': ['null', 'object'],
                                'description': 'Creation and last modification audit stamps',
                                'properties': {
                                    'created': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'actor': {
                                                'type': ['null', 'string'],
                                            },
                                            'time': {
                                                'type': ['null', 'integer'],
                                            },
                                        },
                                    },
                                    'lastModified': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'actor': {
                                                'type': ['null', 'string'],
                                            },
                                            'time': {
                                                'type': ['null', 'integer'],
                                            },
                                        },
                                    },
                                },
                            },
                            'totalBudget': {
                                'type': ['null', 'object'],
                                'description': 'Total budget for the campaign group',
                                'properties': {
                                    'amount': {
                                        'type': ['null', 'string'],
                                    },
                                    'currencyCode': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'runSchedule': {
                                'type': ['null', 'object'],
                                'description': 'Campaign group run schedule',
                                'properties': {
                                    'start': {
                                        'type': ['null', 'integer'],
                                    },
                                    'end': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                            },
                            'servingStatuses': {
                                'type': ['null', 'array'],
                                'description': 'List of serving statuses',
                                'items': {'type': 'string'},
                            },
                            'allowedCampaignTypes': {
                                'type': ['null', 'array'],
                                'description': 'Types of campaigns allowed in this group',
                                'items': {'type': 'string'},
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'campaign_groups',
                        'x-airbyte-stream-name': 'campaign_groups',
                        'x-airbyte-ai-hints': {
                            'summary': 'Campaign groups organizing LinkedIn ad campaigns',
                            'when_to_use': 'Questions about campaign organization or grouping',
                            'trigger_phrases': ['campaign group', 'campaign folder'],
                            'freshness': 'live',
                            'example_questions': ['What campaign groups exist?'],
                            'search_strategy': 'Search by name',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'LinkedIn ad campaign group object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique campaign group identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Campaign group name',
                    },
                    'account': {
                        'type': ['null', 'string'],
                        'description': 'Associated account URN',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Campaign group status',
                    },
                    'test': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is a test campaign group',
                    },
                    'backfilled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the campaign group is backfilled',
                    },
                    'changeAuditStamps': {
                        'type': ['null', 'object'],
                        'description': 'Creation and last modification audit stamps',
                        'properties': {
                            'created': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'actor': {
                                        'type': ['null', 'string'],
                                    },
                                    'time': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                            },
                            'lastModified': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'actor': {
                                        'type': ['null', 'string'],
                                    },
                                    'time': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                            },
                        },
                    },
                    'totalBudget': {
                        'type': ['null', 'object'],
                        'description': 'Total budget for the campaign group',
                        'properties': {
                            'amount': {
                                'type': ['null', 'string'],
                            },
                            'currencyCode': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'runSchedule': {
                        'type': ['null', 'object'],
                        'description': 'Campaign group run schedule',
                        'properties': {
                            'start': {
                                'type': ['null', 'integer'],
                            },
                            'end': {
                                'type': ['null', 'integer'],
                            },
                        },
                    },
                    'servingStatuses': {
                        'type': ['null', 'array'],
                        'description': 'List of serving statuses',
                        'items': {'type': 'string'},
                    },
                    'allowedCampaignTypes': {
                        'type': ['null', 'array'],
                        'description': 'Types of campaigns allowed in this group',
                        'items': {'type': 'string'},
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'campaign_groups',
                'x-airbyte-stream-name': 'campaign_groups',
                'x-airbyte-ai-hints': {
                    'summary': 'Campaign groups organizing LinkedIn ad campaigns',
                    'when_to_use': 'Questions about campaign organization or grouping',
                    'trigger_phrases': ['campaign group', 'campaign folder'],
                    'freshness': 'live',
                    'example_questions': ['What campaign groups exist?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Campaign groups organizing LinkedIn ad campaigns',
                'when_to_use': 'Questions about campaign organization or grouping',
                'trigger_phrases': ['campaign group', 'campaign folder'],
                'freshness': 'live',
                'example_questions': ['What campaign groups exist?'],
                'search_strategy': 'Search by name',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='campaign_groups',
                    target_entity='accounts',
                    foreign_key='account_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='creatives',
            stream_name='creatives',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/adAccounts/{account_id}/creatives',
                    action=Action.LIST,
                    description='Returns a list of creatives for an ad account',
                    query_params=['q', 'pageSize', 'pageToken'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'criteria',
                        },
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                    },
                    path_params=['account_id'],
                    path_params_schema={
                        'account_id': {'type': 'integer', 'required': True},
                    },
                    header_params=['LinkedIn-Version', 'X-RestLi-Method'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                        'X-RestLi-Method': {
                            'type': 'string',
                            'required': True,
                            'default': 'FINDER',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of creatives',
                        'properties': {
                            'elements': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'LinkedIn ad creative object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique creative identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Creative name',
                                        },
                                        'account': {
                                            'type': ['null', 'string'],
                                            'description': 'Associated account URN',
                                        },
                                        'campaign': {
                                            'type': ['null', 'string'],
                                            'description': 'Parent campaign URN',
                                        },
                                        'intendedStatus': {
                                            'type': ['null', 'string'],
                                            'description': 'Intended creative status',
                                        },
                                        'isServing': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the creative is currently serving',
                                        },
                                        'isTest': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is a test creative',
                                        },
                                        'createdAt': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (epoch milliseconds)',
                                        },
                                        'createdBy': {
                                            'type': ['null', 'string'],
                                            'description': 'URN of the user who created the creative',
                                        },
                                        'lastModifiedAt': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last modification timestamp (epoch milliseconds)',
                                        },
                                        'lastModifiedBy': {
                                            'type': ['null', 'string'],
                                            'description': 'URN of the user who last modified the creative',
                                        },
                                        'content': {
                                            'type': ['null', 'object'],
                                            'description': 'Creative content configuration',
                                        },
                                        'review': {
                                            'type': ['null', 'object'],
                                            'description': 'Review status and rejection reasons',
                                            'properties': {
                                                'status': {
                                                    'type': ['null', 'string'],
                                                },
                                                'rejectionReasons': {
                                                    'type': ['null', 'array'],
                                                },
                                            },
                                        },
                                        'servingHoldReasons': {
                                            'type': ['null', 'array'],
                                            'description': 'Reasons for holding creative from serving',
                                            'items': {'type': 'string'},
                                        },
                                        'leadgenCallToAction': {
                                            'type': ['null', 'object'],
                                            'description': 'Lead generation call to action',
                                            'properties': {
                                                'destination': {
                                                    'type': ['null', 'string'],
                                                },
                                                'label': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'creatives',
                                    'x-airbyte-stream-name': 'creatives',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'LinkedIn ad creatives with copy, images, and format details',
                                        'when_to_use': 'Questions about ad creative content or creative assets',
                                        'trigger_phrases': ['linkedin creative', 'ad creative', 'ad copy'],
                                        'freshness': 'live',
                                        'example_questions': ['Show creatives for a campaign'],
                                        'search_strategy': 'Filter by campaign',
                                    },
                                },
                            },
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'nextPageToken': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.elements',
                    record_transform={'creative_analytics_param': 'List({{ record.id }})'},
                    meta_extractor={'nextPageToken': '$.metadata.nextPageToken'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/adAccounts/{account_id}/creatives/{id}',
                    action=Action.GET,
                    description='Get a single creative by ID',
                    path_params=['account_id', 'id'],
                    path_params_schema={
                        'account_id': {'type': 'integer', 'required': True},
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['LinkedIn-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'LinkedIn ad creative object',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                                'description': 'Unique creative identifier',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Creative name',
                            },
                            'account': {
                                'type': ['null', 'string'],
                                'description': 'Associated account URN',
                            },
                            'campaign': {
                                'type': ['null', 'string'],
                                'description': 'Parent campaign URN',
                            },
                            'intendedStatus': {
                                'type': ['null', 'string'],
                                'description': 'Intended creative status',
                            },
                            'isServing': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the creative is currently serving',
                            },
                            'isTest': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether this is a test creative',
                            },
                            'createdAt': {
                                'type': ['null', 'integer'],
                                'description': 'Creation timestamp (epoch milliseconds)',
                            },
                            'createdBy': {
                                'type': ['null', 'string'],
                                'description': 'URN of the user who created the creative',
                            },
                            'lastModifiedAt': {
                                'type': ['null', 'integer'],
                                'description': 'Last modification timestamp (epoch milliseconds)',
                            },
                            'lastModifiedBy': {
                                'type': ['null', 'string'],
                                'description': 'URN of the user who last modified the creative',
                            },
                            'content': {
                                'type': ['null', 'object'],
                                'description': 'Creative content configuration',
                            },
                            'review': {
                                'type': ['null', 'object'],
                                'description': 'Review status and rejection reasons',
                                'properties': {
                                    'status': {
                                        'type': ['null', 'string'],
                                    },
                                    'rejectionReasons': {
                                        'type': ['null', 'array'],
                                    },
                                },
                            },
                            'servingHoldReasons': {
                                'type': ['null', 'array'],
                                'description': 'Reasons for holding creative from serving',
                                'items': {'type': 'string'},
                            },
                            'leadgenCallToAction': {
                                'type': ['null', 'object'],
                                'description': 'Lead generation call to action',
                                'properties': {
                                    'destination': {
                                        'type': ['null', 'string'],
                                    },
                                    'label': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'creatives',
                        'x-airbyte-stream-name': 'creatives',
                        'x-airbyte-ai-hints': {
                            'summary': 'LinkedIn ad creatives with copy, images, and format details',
                            'when_to_use': 'Questions about ad creative content or creative assets',
                            'trigger_phrases': ['linkedin creative', 'ad creative', 'ad copy'],
                            'freshness': 'live',
                            'example_questions': ['Show creatives for a campaign'],
                            'search_strategy': 'Filter by campaign',
                        },
                    },
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'LinkedIn ad creative object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique creative identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Creative name',
                    },
                    'account': {
                        'type': ['null', 'string'],
                        'description': 'Associated account URN',
                    },
                    'campaign': {
                        'type': ['null', 'string'],
                        'description': 'Parent campaign URN',
                    },
                    'intendedStatus': {
                        'type': ['null', 'string'],
                        'description': 'Intended creative status',
                    },
                    'isServing': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the creative is currently serving',
                    },
                    'isTest': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is a test creative',
                    },
                    'createdAt': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (epoch milliseconds)',
                    },
                    'createdBy': {
                        'type': ['null', 'string'],
                        'description': 'URN of the user who created the creative',
                    },
                    'lastModifiedAt': {
                        'type': ['null', 'integer'],
                        'description': 'Last modification timestamp (epoch milliseconds)',
                    },
                    'lastModifiedBy': {
                        'type': ['null', 'string'],
                        'description': 'URN of the user who last modified the creative',
                    },
                    'content': {
                        'type': ['null', 'object'],
                        'description': 'Creative content configuration',
                    },
                    'review': {
                        'type': ['null', 'object'],
                        'description': 'Review status and rejection reasons',
                        'properties': {
                            'status': {
                                'type': ['null', 'string'],
                            },
                            'rejectionReasons': {
                                'type': ['null', 'array'],
                            },
                        },
                    },
                    'servingHoldReasons': {
                        'type': ['null', 'array'],
                        'description': 'Reasons for holding creative from serving',
                        'items': {'type': 'string'},
                    },
                    'leadgenCallToAction': {
                        'type': ['null', 'object'],
                        'description': 'Lead generation call to action',
                        'properties': {
                            'destination': {
                                'type': ['null', 'string'],
                            },
                            'label': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'creatives',
                'x-airbyte-stream-name': 'creatives',
                'x-airbyte-ai-hints': {
                    'summary': 'LinkedIn ad creatives with copy, images, and format details',
                    'when_to_use': 'Questions about ad creative content or creative assets',
                    'trigger_phrases': ['linkedin creative', 'ad creative', 'ad copy'],
                    'freshness': 'live',
                    'example_questions': ['Show creatives for a campaign'],
                    'search_strategy': 'Filter by campaign',
                },
            },
            ai_hints={
                'summary': 'LinkedIn ad creatives with copy, images, and format details',
                'when_to_use': 'Questions about ad creative content or creative assets',
                'trigger_phrases': ['linkedin creative', 'ad creative', 'ad copy'],
                'freshness': 'live',
                'example_questions': ['Show creatives for a campaign'],
                'search_strategy': 'Filter by campaign',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='creatives',
                    target_entity='accounts',
                    foreign_key='account_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='conversions',
            stream_name='conversions',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/conversions',
                    action=Action.LIST,
                    description='Returns a list of conversion rules for an ad account',
                    query_params=[
                        'q',
                        'account',
                        'count',
                        'start',
                    ],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'account',
                        },
                        'account': {'type': 'string', 'required': True},
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'start': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                            'minimum': 0,
                        },
                    },
                    header_params=['LinkedIn-Version', 'X-Restli-Protocol-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                        'X-Restli-Protocol-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2.0.0',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of conversions',
                        'properties': {
                            'elements': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'LinkedIn ad conversion tracking rule',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique conversion identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Conversion name',
                                        },
                                        'account': {
                                            'type': ['null', 'string'],
                                            'description': 'Associated account URN',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Conversion type',
                                        },
                                        'attributionType': {
                                            'type': ['null', 'string'],
                                            'description': 'Attribution type for the conversion',
                                        },
                                        'conversionMethod': {
                                            'type': ['null', 'string'],
                                            'description': 'Method used for tracking conversions (e.g., INSIGHT_TAG_URL_MATCH_RULES)',
                                        },
                                        'valueType': {
                                            'type': ['null', 'string'],
                                            'description': 'Type of conversion value (DYNAMIC or FIXED)',
                                        },
                                        'enabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the conversion tracking is enabled',
                                        },
                                        'created': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (epoch milliseconds)',
                                        },
                                        'lastModified': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last modification timestamp (epoch milliseconds)',
                                        },
                                        'postClickAttributionWindowSize': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-click attribution window size in days',
                                        },
                                        'viewThroughAttributionWindowSize': {
                                            'type': ['null', 'integer'],
                                            'description': 'View-through attribution window size in days',
                                        },
                                        'campaigns': {
                                            'type': ['null', 'array'],
                                            'description': 'Related campaign URNs',
                                            'items': {'type': 'string'},
                                        },
                                        'associatedCampaigns': {
                                            'type': ['null', 'array'],
                                            'description': 'Associated campaigns',
                                        },
                                        'imagePixelTag': {
                                            'type': ['null', 'string'],
                                            'description': 'Image pixel tracking tag',
                                        },
                                        'lastCallbackAt': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last callback timestamp',
                                        },
                                        'latestFirstPartyCallbackAt': {
                                            'type': ['null', 'integer'],
                                            'description': 'Latest first-party callback timestamp',
                                        },
                                        'urlMatchRuleExpression': {
                                            'type': ['null', 'array'],
                                            'description': 'URL match rule expressions',
                                        },
                                        'urlRules': {
                                            'type': ['null', 'array'],
                                            'description': 'URL rules for conversion matching',
                                        },
                                        'value': {
                                            'type': ['null', 'object'],
                                            'description': 'Conversion value',
                                            'properties': {
                                                'amount': {
                                                    'type': ['null', 'string'],
                                                },
                                                'currencyCode': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'conversions',
                                    'x-airbyte-stream-name': 'conversions',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Conversion tracking rules for LinkedIn ad attribution',
                                        'when_to_use': 'Questions about conversion tracking or attribution setup',
                                        'trigger_phrases': ['linkedin conversion', 'conversion tracking', 'attribution'],
                                        'freshness': 'live',
                                        'example_questions': ['What conversion rules are set up?'],
                                        'search_strategy': 'List all conversion rules',
                                    },
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'total': {'type': 'integer'},
                                    'count': {'type': 'integer'},
                                    'start': {'type': 'integer'},
                                },
                            },
                        },
                    },
                    record_extractor='$.elements',
                    meta_extractor={'total': '$.paging.total'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/conversions/{id}',
                    action=Action.GET,
                    description='Get a single conversion rule by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    header_params=['LinkedIn-Version', 'X-Restli-Protocol-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                        'X-Restli-Protocol-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2.0.0',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'LinkedIn ad conversion tracking rule',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique conversion identifier',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Conversion name',
                            },
                            'account': {
                                'type': ['null', 'string'],
                                'description': 'Associated account URN',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'Conversion type',
                            },
                            'attributionType': {
                                'type': ['null', 'string'],
                                'description': 'Attribution type for the conversion',
                            },
                            'conversionMethod': {
                                'type': ['null', 'string'],
                                'description': 'Method used for tracking conversions (e.g., INSIGHT_TAG_URL_MATCH_RULES)',
                            },
                            'valueType': {
                                'type': ['null', 'string'],
                                'description': 'Type of conversion value (DYNAMIC or FIXED)',
                            },
                            'enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the conversion tracking is enabled',
                            },
                            'created': {
                                'type': ['null', 'integer'],
                                'description': 'Creation timestamp (epoch milliseconds)',
                            },
                            'lastModified': {
                                'type': ['null', 'integer'],
                                'description': 'Last modification timestamp (epoch milliseconds)',
                            },
                            'postClickAttributionWindowSize': {
                                'type': ['null', 'integer'],
                                'description': 'Post-click attribution window size in days',
                            },
                            'viewThroughAttributionWindowSize': {
                                'type': ['null', 'integer'],
                                'description': 'View-through attribution window size in days',
                            },
                            'campaigns': {
                                'type': ['null', 'array'],
                                'description': 'Related campaign URNs',
                                'items': {'type': 'string'},
                            },
                            'associatedCampaigns': {
                                'type': ['null', 'array'],
                                'description': 'Associated campaigns',
                            },
                            'imagePixelTag': {
                                'type': ['null', 'string'],
                                'description': 'Image pixel tracking tag',
                            },
                            'lastCallbackAt': {
                                'type': ['null', 'integer'],
                                'description': 'Last callback timestamp',
                            },
                            'latestFirstPartyCallbackAt': {
                                'type': ['null', 'integer'],
                                'description': 'Latest first-party callback timestamp',
                            },
                            'urlMatchRuleExpression': {
                                'type': ['null', 'array'],
                                'description': 'URL match rule expressions',
                            },
                            'urlRules': {
                                'type': ['null', 'array'],
                                'description': 'URL rules for conversion matching',
                            },
                            'value': {
                                'type': ['null', 'object'],
                                'description': 'Conversion value',
                                'properties': {
                                    'amount': {
                                        'type': ['null', 'string'],
                                    },
                                    'currencyCode': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'conversions',
                        'x-airbyte-stream-name': 'conversions',
                        'x-airbyte-ai-hints': {
                            'summary': 'Conversion tracking rules for LinkedIn ad attribution',
                            'when_to_use': 'Questions about conversion tracking or attribution setup',
                            'trigger_phrases': ['linkedin conversion', 'conversion tracking', 'attribution'],
                            'freshness': 'live',
                            'example_questions': ['What conversion rules are set up?'],
                            'search_strategy': 'List all conversion rules',
                        },
                    },
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'LinkedIn ad conversion tracking rule',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique conversion identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Conversion name',
                    },
                    'account': {
                        'type': ['null', 'string'],
                        'description': 'Associated account URN',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Conversion type',
                    },
                    'attributionType': {
                        'type': ['null', 'string'],
                        'description': 'Attribution type for the conversion',
                    },
                    'conversionMethod': {
                        'type': ['null', 'string'],
                        'description': 'Method used for tracking conversions (e.g., INSIGHT_TAG_URL_MATCH_RULES)',
                    },
                    'valueType': {
                        'type': ['null', 'string'],
                        'description': 'Type of conversion value (DYNAMIC or FIXED)',
                    },
                    'enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the conversion tracking is enabled',
                    },
                    'created': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (epoch milliseconds)',
                    },
                    'lastModified': {
                        'type': ['null', 'integer'],
                        'description': 'Last modification timestamp (epoch milliseconds)',
                    },
                    'postClickAttributionWindowSize': {
                        'type': ['null', 'integer'],
                        'description': 'Post-click attribution window size in days',
                    },
                    'viewThroughAttributionWindowSize': {
                        'type': ['null', 'integer'],
                        'description': 'View-through attribution window size in days',
                    },
                    'campaigns': {
                        'type': ['null', 'array'],
                        'description': 'Related campaign URNs',
                        'items': {'type': 'string'},
                    },
                    'associatedCampaigns': {
                        'type': ['null', 'array'],
                        'description': 'Associated campaigns',
                    },
                    'imagePixelTag': {
                        'type': ['null', 'string'],
                        'description': 'Image pixel tracking tag',
                    },
                    'lastCallbackAt': {
                        'type': ['null', 'integer'],
                        'description': 'Last callback timestamp',
                    },
                    'latestFirstPartyCallbackAt': {
                        'type': ['null', 'integer'],
                        'description': 'Latest first-party callback timestamp',
                    },
                    'urlMatchRuleExpression': {
                        'type': ['null', 'array'],
                        'description': 'URL match rule expressions',
                    },
                    'urlRules': {
                        'type': ['null', 'array'],
                        'description': 'URL rules for conversion matching',
                    },
                    'value': {
                        'type': ['null', 'object'],
                        'description': 'Conversion value',
                        'properties': {
                            'amount': {
                                'type': ['null', 'string'],
                            },
                            'currencyCode': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'conversions',
                'x-airbyte-stream-name': 'conversions',
                'x-airbyte-ai-hints': {
                    'summary': 'Conversion tracking rules for LinkedIn ad attribution',
                    'when_to_use': 'Questions about conversion tracking or attribution setup',
                    'trigger_phrases': ['linkedin conversion', 'conversion tracking', 'attribution'],
                    'freshness': 'live',
                    'example_questions': ['What conversion rules are set up?'],
                    'search_strategy': 'List all conversion rules',
                },
            },
            ai_hints={
                'summary': 'Conversion tracking rules for LinkedIn ad attribution',
                'when_to_use': 'Questions about conversion tracking or attribution setup',
                'trigger_phrases': ['linkedin conversion', 'conversion tracking', 'attribution'],
                'freshness': 'live',
                'example_questions': ['What conversion rules are set up?'],
                'search_strategy': 'List all conversion rules',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='conversions',
                    target_entity='accounts',
                    foreign_key='account',
                    target_key='account_urn',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='ad_campaign_analytics',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/adAnalytics:campaign',
                    path_override=PathOverrideConfig(
                        path='/adAnalytics',
                    ),
                    action=Action.LIST,
                    description='Returns ad analytics data pivoted by campaign. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by campaign.\n',
                    query_params=[
                        'q',
                        'pivot',
                        'timeGranularity',
                        'dateRange',
                        'campaigns',
                        'fields',
                    ],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'analytics',
                        },
                        'pivot': {
                            'type': 'string',
                            'required': True,
                            'default': 'CAMPAIGN',
                        },
                        'timeGranularity': {
                            'type': 'string',
                            'required': True,
                            'default': 'DAILY',
                            'enum': ['DAILY', 'MONTHLY', 'ALL'],
                        },
                        'dateRange': {
                            'type': 'string',
                            'required': True,
                            'default': '(start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))',
                        },
                        'campaigns': {'type': 'string', 'required': True},
                        'fields': {'type': 'string', 'required': False},
                    },
                    header_params=['LinkedIn-Version', 'X-Restli-Protocol-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                        'X-Restli-Protocol-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2.0.0',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Ad analytics API response',
                        'properties': {
                            'elements': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Ad analytics data record with performance metrics',
                                    'properties': {
                                        'dateRange': {
                                            'type': ['null', 'object'],
                                            'description': 'Date range for this analytics record',
                                            'properties': {
                                                'start': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'year': {'type': 'integer'},
                                                        'month': {'type': 'integer'},
                                                        'day': {'type': 'integer'},
                                                    },
                                                },
                                                'end': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'year': {'type': 'integer'},
                                                        'month': {'type': 'integer'},
                                                        'day': {'type': 'integer'},
                                                    },
                                                },
                                            },
                                        },
                                        'pivotValues': {
                                            'type': ['null', 'array'],
                                            'description': 'Pivot values (URNs) for this analytics record',
                                            'items': {'type': 'string'},
                                        },
                                        'impressions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times the ad was shown',
                                        },
                                        'clicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of clicks on the ad',
                                        },
                                        'costInLocalCurrency': {
                                            'type': ['null', 'string'],
                                            'description': "Total cost in the account's local currency",
                                        },
                                        'costInUsd': {
                                            'type': ['null', 'string'],
                                            'description': 'Total cost in USD',
                                        },
                                        'likes': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of likes',
                                        },
                                        'shares': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of shares',
                                        },
                                        'comments': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of comments',
                                        },
                                        'reactions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of reactions',
                                        },
                                        'follows': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of follows',
                                        },
                                        'totalEngagements': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total number of engagements',
                                        },
                                        'landingPageClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of landing page clicks',
                                        },
                                        'companyPageClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of company page clicks',
                                        },
                                        'externalWebsiteConversions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of conversions on external websites',
                                        },
                                        'externalWebsitePostClickConversions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-click conversions on external websites',
                                        },
                                        'externalWebsitePostViewConversions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-view conversions on external websites',
                                        },
                                        'conversionValueInLocalCurrency': {
                                            'type': ['null', 'string'],
                                            'description': 'Conversion value in local currency',
                                        },
                                        'approximateMemberReach': {
                                            'type': ['null', 'integer'],
                                            'description': 'Approximate unique member reach',
                                        },
                                        'cardClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of carousel card clicks',
                                        },
                                        'cardImpressions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of carousel card impressions',
                                        },
                                        'videoStarts': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of video starts',
                                        },
                                        'videoViews': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of video views',
                                        },
                                        'videoFirstQuartileCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times video played to 25%',
                                        },
                                        'videoMidpointCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times video played to 50%',
                                        },
                                        'videoThirdQuartileCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times video played to 75%',
                                        },
                                        'videoCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times video played to 100%',
                                        },
                                        'fullScreenPlays': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of full screen video plays',
                                        },
                                        'oneClickLeads': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of one-click leads',
                                        },
                                        'oneClickLeadFormOpens': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of one-click lead form opens',
                                        },
                                        'otherEngagements': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of other engagements',
                                        },
                                        'adUnitClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of ad unit clicks',
                                        },
                                        'actionClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of action clicks',
                                        },
                                        'textUrlClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of text URL clicks',
                                        },
                                        'commentLikes': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of comment likes',
                                        },
                                        'sends': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of sends (InMail)',
                                        },
                                        'opens': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of opens (InMail)',
                                        },
                                        'downloadClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of download clicks',
                                        },
                                        'jobApplications': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of job applications',
                                        },
                                        'jobApplyClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of job apply clicks',
                                        },
                                        'registrations': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of registrations',
                                        },
                                        'talentLeads': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of talent leads',
                                        },
                                        'validWorkEmailLeads': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of valid work email leads',
                                        },
                                        'postClickJobApplications': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-click job applications',
                                        },
                                        'postClickJobApplyClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-click job apply clicks',
                                        },
                                        'postClickRegistrations': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-click registrations',
                                        },
                                        'postViewJobApplications': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-view job applications',
                                        },
                                        'postViewJobApplyClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-view job apply clicks',
                                        },
                                        'postViewRegistrations': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-view registrations',
                                        },
                                        'leadGenerationMailContactInfoShares': {
                                            'type': ['null', 'integer'],
                                            'description': 'Lead gen mail contact info shares',
                                        },
                                        'leadGenerationMailInterestedClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Lead gen mail interested clicks',
                                        },
                                        'documentCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of document completions',
                                        },
                                        'documentFirstQuartileCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times document viewed to 25%',
                                        },
                                        'documentMidpointCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times document viewed to 50%',
                                        },
                                        'documentThirdQuartileCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times document viewed to 75%',
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'count': {'type': 'integer'},
                                    'start': {'type': 'integer'},
                                },
                            },
                        },
                    },
                    record_extractor='$.elements',
                    no_pagination='Analytics endpoint returns a bounded aggregation scoped to the requested dateRange and campaigns URNs; LinkedIn does not return a next-page cursor for /adAnalytics.',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='ad_campaign_analytics',
                    target_entity='campaigns',
                    foreign_key='campaigns',
                    target_key='campaign_analytics_param',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='ad_creative_analytics',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/adAnalytics:creative',
                    path_override=PathOverrideConfig(
                        path='/adAnalytics',
                    ),
                    action=Action.LIST,
                    description='Returns ad analytics data pivoted by creative. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by creative.\n',
                    query_params=[
                        'q',
                        'pivot',
                        'timeGranularity',
                        'dateRange',
                        'creatives',
                        'fields',
                    ],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'analytics',
                        },
                        'pivot': {
                            'type': 'string',
                            'required': True,
                            'default': 'CREATIVE',
                        },
                        'timeGranularity': {
                            'type': 'string',
                            'required': True,
                            'default': 'DAILY',
                            'enum': ['DAILY', 'MONTHLY', 'ALL'],
                        },
                        'dateRange': {
                            'type': 'string',
                            'required': True,
                            'default': '(start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))',
                        },
                        'creatives': {'type': 'string', 'required': True},
                        'fields': {'type': 'string', 'required': False},
                    },
                    header_params=['LinkedIn-Version', 'X-Restli-Protocol-Version'],
                    header_params_schema={
                        'LinkedIn-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '202601',
                        },
                        'X-Restli-Protocol-Version': {
                            'type': 'string',
                            'required': True,
                            'default': '2.0.0',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Ad analytics API response',
                        'properties': {
                            'elements': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Ad analytics data record with performance metrics',
                                    'properties': {
                                        'dateRange': {
                                            'type': ['null', 'object'],
                                            'description': 'Date range for this analytics record',
                                            'properties': {
                                                'start': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'year': {'type': 'integer'},
                                                        'month': {'type': 'integer'},
                                                        'day': {'type': 'integer'},
                                                    },
                                                },
                                                'end': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'year': {'type': 'integer'},
                                                        'month': {'type': 'integer'},
                                                        'day': {'type': 'integer'},
                                                    },
                                                },
                                            },
                                        },
                                        'pivotValues': {
                                            'type': ['null', 'array'],
                                            'description': 'Pivot values (URNs) for this analytics record',
                                            'items': {'type': 'string'},
                                        },
                                        'impressions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times the ad was shown',
                                        },
                                        'clicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of clicks on the ad',
                                        },
                                        'costInLocalCurrency': {
                                            'type': ['null', 'string'],
                                            'description': "Total cost in the account's local currency",
                                        },
                                        'costInUsd': {
                                            'type': ['null', 'string'],
                                            'description': 'Total cost in USD',
                                        },
                                        'likes': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of likes',
                                        },
                                        'shares': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of shares',
                                        },
                                        'comments': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of comments',
                                        },
                                        'reactions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of reactions',
                                        },
                                        'follows': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of follows',
                                        },
                                        'totalEngagements': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total number of engagements',
                                        },
                                        'landingPageClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of landing page clicks',
                                        },
                                        'companyPageClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of company page clicks',
                                        },
                                        'externalWebsiteConversions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of conversions on external websites',
                                        },
                                        'externalWebsitePostClickConversions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-click conversions on external websites',
                                        },
                                        'externalWebsitePostViewConversions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-view conversions on external websites',
                                        },
                                        'conversionValueInLocalCurrency': {
                                            'type': ['null', 'string'],
                                            'description': 'Conversion value in local currency',
                                        },
                                        'approximateMemberReach': {
                                            'type': ['null', 'integer'],
                                            'description': 'Approximate unique member reach',
                                        },
                                        'cardClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of carousel card clicks',
                                        },
                                        'cardImpressions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of carousel card impressions',
                                        },
                                        'videoStarts': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of video starts',
                                        },
                                        'videoViews': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of video views',
                                        },
                                        'videoFirstQuartileCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times video played to 25%',
                                        },
                                        'videoMidpointCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times video played to 50%',
                                        },
                                        'videoThirdQuartileCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times video played to 75%',
                                        },
                                        'videoCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times video played to 100%',
                                        },
                                        'fullScreenPlays': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of full screen video plays',
                                        },
                                        'oneClickLeads': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of one-click leads',
                                        },
                                        'oneClickLeadFormOpens': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of one-click lead form opens',
                                        },
                                        'otherEngagements': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of other engagements',
                                        },
                                        'adUnitClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of ad unit clicks',
                                        },
                                        'actionClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of action clicks',
                                        },
                                        'textUrlClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of text URL clicks',
                                        },
                                        'commentLikes': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of comment likes',
                                        },
                                        'sends': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of sends (InMail)',
                                        },
                                        'opens': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of opens (InMail)',
                                        },
                                        'downloadClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of download clicks',
                                        },
                                        'jobApplications': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of job applications',
                                        },
                                        'jobApplyClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of job apply clicks',
                                        },
                                        'registrations': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of registrations',
                                        },
                                        'talentLeads': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of talent leads',
                                        },
                                        'validWorkEmailLeads': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of valid work email leads',
                                        },
                                        'postClickJobApplications': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-click job applications',
                                        },
                                        'postClickJobApplyClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-click job apply clicks',
                                        },
                                        'postClickRegistrations': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-click registrations',
                                        },
                                        'postViewJobApplications': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-view job applications',
                                        },
                                        'postViewJobApplyClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-view job apply clicks',
                                        },
                                        'postViewRegistrations': {
                                            'type': ['null', 'integer'],
                                            'description': 'Post-view registrations',
                                        },
                                        'leadGenerationMailContactInfoShares': {
                                            'type': ['null', 'integer'],
                                            'description': 'Lead gen mail contact info shares',
                                        },
                                        'leadGenerationMailInterestedClicks': {
                                            'type': ['null', 'integer'],
                                            'description': 'Lead gen mail interested clicks',
                                        },
                                        'documentCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of document completions',
                                        },
                                        'documentFirstQuartileCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times document viewed to 25%',
                                        },
                                        'documentMidpointCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times document viewed to 50%',
                                        },
                                        'documentThirdQuartileCompletions': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of times document viewed to 75%',
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                            'paging': {
                                'type': 'object',
                                'properties': {
                                    'count': {'type': 'integer'},
                                    'start': {'type': 'integer'},
                                },
                            },
                        },
                    },
                    record_extractor='$.elements',
                    no_pagination='Analytics endpoint returns a bounded aggregation scoped to the requested dateRange and creatives URNs; LinkedIn does not return a next-page cursor for /adAnalytics.',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='ad_creative_analytics',
                    target_entity='creatives',
                    foreign_key='creatives',
                    target_key='creative_analytics_param',
                    cardinality='many_to_one',
                ),
            ],
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='accounts',
                suggested=True,
                x_airbyte_name='accounts',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique account identifier',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Account name',
                    ),
                    CacheFieldConfig(
                        name='currency',
                        type=['null', 'string'],
                        description='Currency code used by the account',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Account status',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Account type',
                    ),
                    CacheFieldConfig(
                        name='reference',
                        type=['null', 'string'],
                        description='Reference organization URN',
                    ),
                    CacheFieldConfig(
                        name='test',
                        type=['null', 'boolean'],
                        description='Whether this is a test account',
                    ),
                    CacheFieldConfig(
                        name='notifiedOnCampaignOptimization',
                        type=['null', 'boolean'],
                        description='Flag for notifications on campaign optimization',
                    ),
                    CacheFieldConfig(
                        name='notifiedOnCreativeApproval',
                        type=['null', 'boolean'],
                        description='Flag for notifications on creative approval',
                    ),
                    CacheFieldConfig(
                        name='notifiedOnCreativeRejection',
                        type=['null', 'boolean'],
                        description='Flag for notifications on creative rejection',
                    ),
                    CacheFieldConfig(
                        name='notifiedOnEndOfCampaign',
                        type=['null', 'boolean'],
                        description='Flag for notifications on end of campaign',
                    ),
                    CacheFieldConfig(
                        name='notifiedOnNewFeaturesEnabled',
                        type=['null', 'boolean'],
                        description='Flag for notifications on new features',
                    ),
                    CacheFieldConfig(
                        name='servingStatuses',
                        type=['null', 'array'],
                        description='List of serving statuses',
                    ),
                    CacheFieldConfig(
                        name='version',
                        type=['null', 'object'],
                        description='Version information',
                        properties={
                            'versionTag': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='account_users',
                suggested=True,
                x_airbyte_name='account_users',
                fields=[
                    CacheFieldConfig(
                        name='account',
                        type=['null', 'string'],
                        description='Associated account URN',
                    ),
                    CacheFieldConfig(
                        name='user',
                        type=['null', 'string'],
                        description='User URN',
                    ),
                    CacheFieldConfig(
                        name='role',
                        type=['null', 'string'],
                        description='User role in the account',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='campaigns',
                suggested=True,
                x_airbyte_name='campaigns',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique campaign identifier',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Campaign name',
                    ),
                    CacheFieldConfig(
                        name='account',
                        type=['null', 'string'],
                        description='Associated account URN',
                    ),
                    CacheFieldConfig(
                        name='campaignGroup',
                        type=['null', 'string'],
                        description='Parent campaign group URN',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Campaign status',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Campaign type',
                    ),
                    CacheFieldConfig(
                        name='costType',
                        type=['null', 'string'],
                        description='Cost type (CPC CPM etc)',
                    ),
                    CacheFieldConfig(
                        name='format',
                        type=['null', 'string'],
                        description='Campaign ad format',
                    ),
                    CacheFieldConfig(
                        name='objectiveType',
                        type=['null', 'string'],
                        description='Campaign objective type',
                    ),
                    CacheFieldConfig(
                        name='optimizationTargetType',
                        type=['null', 'string'],
                        description='Optimization target type',
                    ),
                    CacheFieldConfig(
                        name='creativeSelection',
                        type=['null', 'string'],
                        description='Creative selection mode',
                    ),
                    CacheFieldConfig(
                        name='pacingStrategy',
                        type=['null', 'string'],
                        description='Budget pacing strategy',
                    ),
                    CacheFieldConfig(
                        name='audienceExpansionEnabled',
                        type=['null', 'boolean'],
                        description='Whether audience expansion is enabled',
                    ),
                    CacheFieldConfig(
                        name='offsiteDeliveryEnabled',
                        type=['null', 'boolean'],
                        description='Whether offsite delivery is enabled',
                    ),
                    CacheFieldConfig(
                        name='storyDeliveryEnabled',
                        type=['null', 'boolean'],
                        description='Whether story delivery is enabled',
                    ),
                    CacheFieldConfig(
                        name='test',
                        type=['null', 'boolean'],
                        description='Whether this is a test campaign',
                    ),
                    CacheFieldConfig(
                        name='associatedEntity',
                        type=['null', 'string'],
                        description='Associated entity URN',
                    ),
                    CacheFieldConfig(
                        name='dailyBudget',
                        type=['null', 'object'],
                        description='Daily budget configuration',
                        properties={
                            'amount': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'currencyCode': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='totalBudget',
                        type=['null', 'object'],
                        description='Total budget configuration',
                        properties={
                            'amount': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'currencyCode': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='unitCost',
                        type=['null', 'object'],
                        description='Cost per unit (bid amount)',
                        properties={
                            'amount': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'currencyCode': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='runSchedule',
                        type=['null', 'object'],
                        description='Campaign run schedule',
                        properties={
                            'start': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'end': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='locale',
                        type=['null', 'object'],
                        description='Campaign locale settings',
                        properties={
                            'country': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'language': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='servingStatuses',
                        type=['null', 'array'],
                        description='List of serving statuses',
                    ),
                    CacheFieldConfig(
                        name='version',
                        type=['null', 'object'],
                        description='Version information',
                        properties={
                            'versionTag': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='campaign_groups',
                suggested=True,
                x_airbyte_name='campaign_groups',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique campaign group identifier',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Campaign group name',
                    ),
                    CacheFieldConfig(
                        name='account',
                        type=['null', 'string'],
                        description='Associated account URN',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Campaign group status',
                    ),
                    CacheFieldConfig(
                        name='test',
                        type=['null', 'boolean'],
                        description='Whether this is a test campaign group',
                    ),
                    CacheFieldConfig(
                        name='backfilled',
                        type=['null', 'boolean'],
                        description='Whether the campaign group is backfilled',
                    ),
                    CacheFieldConfig(
                        name='totalBudget',
                        type=['null', 'object'],
                        description='Total budget for the campaign group',
                        properties={
                            'amount': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'currencyCode': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='runSchedule',
                        type=['null', 'object'],
                        description='Campaign group run schedule',
                        properties={
                            'start': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'end': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='servingStatuses',
                        type=['null', 'array'],
                        description='List of serving statuses',
                    ),
                    CacheFieldConfig(
                        name='allowedCampaignTypes',
                        type=['null', 'array'],
                        description='Types of campaigns allowed in this group',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='creatives',
                suggested=True,
                x_airbyte_name='creatives',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique creative identifier',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Creative name',
                    ),
                    CacheFieldConfig(
                        name='account',
                        type=['null', 'string'],
                        description='Associated account URN',
                    ),
                    CacheFieldConfig(
                        name='campaign',
                        type=['null', 'string'],
                        description='Parent campaign URN',
                    ),
                    CacheFieldConfig(
                        name='intendedStatus',
                        type=['null', 'string'],
                        description='Intended creative status',
                    ),
                    CacheFieldConfig(
                        name='isServing',
                        type=['null', 'boolean'],
                        description='Whether the creative is currently serving',
                    ),
                    CacheFieldConfig(
                        name='isTest',
                        type=['null', 'boolean'],
                        description='Whether this is a test creative',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'integer'],
                        description='Creation timestamp (epoch milliseconds)',
                    ),
                    CacheFieldConfig(
                        name='createdBy',
                        type=['null', 'string'],
                        description='URN of the user who created the creative',
                    ),
                    CacheFieldConfig(
                        name='lastModifiedAt',
                        type=['null', 'integer'],
                        description='Last modification timestamp (epoch milliseconds)',
                    ),
                    CacheFieldConfig(
                        name='lastModifiedBy',
                        type=['null', 'string'],
                        description='URN of the user who last modified the creative',
                    ),
                    CacheFieldConfig(
                        name='content',
                        type=['null', 'object'],
                        description='Creative content configuration',
                    ),
                    CacheFieldConfig(
                        name='servingHoldReasons',
                        type=['null', 'array'],
                        description='Reasons for holding creative from serving',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='conversions',
                x_airbyte_name='conversions',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique conversion identifier',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Conversion name',
                    ),
                    CacheFieldConfig(
                        name='account',
                        type=['null', 'string'],
                        description='Associated account URN',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Conversion type',
                    ),
                    CacheFieldConfig(
                        name='attributionType',
                        type=['null', 'string'],
                        description='Attribution type for the conversion',
                    ),
                    CacheFieldConfig(
                        name='enabled',
                        type=['null', 'boolean'],
                        description='Whether the conversion tracking is enabled',
                    ),
                    CacheFieldConfig(
                        name='created',
                        type=['null', 'integer'],
                        description='Creation timestamp (epoch milliseconds)',
                    ),
                    CacheFieldConfig(
                        name='lastModified',
                        type=['null', 'integer'],
                        description='Last modification timestamp (epoch milliseconds)',
                    ),
                    CacheFieldConfig(
                        name='postClickAttributionWindowSize',
                        type=['null', 'integer'],
                        description='Post-click attribution window size in days',
                    ),
                    CacheFieldConfig(
                        name='viewThroughAttributionWindowSize',
                        type=['null', 'integer'],
                        description='View-through attribution window size in days',
                    ),
                    CacheFieldConfig(
                        name='campaigns',
                        type=['null', 'array'],
                        description='Related campaign URNs',
                    ),
                    CacheFieldConfig(
                        name='associatedCampaigns',
                        type=['null', 'array'],
                        description='Associated campaigns',
                    ),
                    CacheFieldConfig(
                        name='imagePixelTag',
                        type=['null', 'string'],
                        description='Image pixel tracking tag',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'object'],
                        description='Conversion value',
                        properties={
                            'amount': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'currencyCode': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='ad_campaign_analytics',
                suggested=True,
                x_airbyte_name='ad_campaign_analytics',
                fields=[
                    CacheFieldConfig(
                        name='impressions',
                        type=['null', 'number'],
                        description='Number of times the ad was shown',
                    ),
                    CacheFieldConfig(
                        name='clicks',
                        type=['null', 'number'],
                        description='Number of clicks on the ad',
                    ),
                    CacheFieldConfig(
                        name='costInLocalCurrency',
                        type=['null', 'number'],
                        description='Total cost in the accounts local currency',
                    ),
                    CacheFieldConfig(
                        name='costInUsd',
                        type=['null', 'number'],
                        description='Total cost in USD',
                    ),
                    CacheFieldConfig(
                        name='likes',
                        type=['null', 'number'],
                        description='Number of likes',
                    ),
                    CacheFieldConfig(
                        name='shares',
                        type=['null', 'number'],
                        description='Number of shares',
                    ),
                    CacheFieldConfig(
                        name='comments',
                        type=['null', 'number'],
                        description='Number of comments',
                    ),
                    CacheFieldConfig(
                        name='reactions',
                        type=['null', 'number'],
                        description='Number of reactions',
                    ),
                    CacheFieldConfig(
                        name='follows',
                        type=['null', 'number'],
                        description='Number of follows',
                    ),
                    CacheFieldConfig(
                        name='totalEngagements',
                        type=['null', 'number'],
                        description='Total number of engagements',
                    ),
                    CacheFieldConfig(
                        name='landingPageClicks',
                        type=['null', 'number'],
                        description='Number of landing page clicks',
                    ),
                    CacheFieldConfig(
                        name='companyPageClicks',
                        type=['null', 'number'],
                        description='Number of company page clicks',
                    ),
                    CacheFieldConfig(
                        name='externalWebsiteConversions',
                        type=['null', 'number'],
                        description='Number of conversions on external websites',
                    ),
                    CacheFieldConfig(
                        name='externalWebsitePostClickConversions',
                        type=['null', 'number'],
                        description='Post-click conversions on external websites',
                    ),
                    CacheFieldConfig(
                        name='externalWebsitePostViewConversions',
                        type=['null', 'number'],
                        description='Post-view conversions on external websites',
                    ),
                    CacheFieldConfig(
                        name='conversionValueInLocalCurrency',
                        type=['null', 'number'],
                        description='Conversion value in local currency',
                    ),
                    CacheFieldConfig(
                        name='approximateMemberReach',
                        type=['null', 'number'],
                        description='Approximate unique member reach',
                    ),
                    CacheFieldConfig(
                        name='cardClicks',
                        type=['null', 'number'],
                        description='Number of carousel card clicks',
                    ),
                    CacheFieldConfig(
                        name='cardImpressions',
                        type=['null', 'number'],
                        description='Number of carousel card impressions',
                    ),
                    CacheFieldConfig(
                        name='videoStarts',
                        type=['null', 'number'],
                        description='Number of video starts',
                    ),
                    CacheFieldConfig(
                        name='videoViews',
                        type=['null', 'number'],
                        description='Number of video views',
                    ),
                    CacheFieldConfig(
                        name='videoFirstQuartileCompletions',
                        type=['null', 'number'],
                        description='Number of times video played to 25%',
                    ),
                    CacheFieldConfig(
                        name='videoMidpointCompletions',
                        type=['null', 'number'],
                        description='Number of times video played to 50%',
                    ),
                    CacheFieldConfig(
                        name='videoThirdQuartileCompletions',
                        type=['null', 'number'],
                        description='Number of times video played to 75%',
                    ),
                    CacheFieldConfig(
                        name='videoCompletions',
                        type=['null', 'number'],
                        description='Number of times video played to 100%',
                    ),
                    CacheFieldConfig(
                        name='fullScreenPlays',
                        type=['null', 'number'],
                        description='Number of full screen video plays',
                    ),
                    CacheFieldConfig(
                        name='oneClickLeads',
                        type=['null', 'number'],
                        description='Number of one-click leads',
                    ),
                    CacheFieldConfig(
                        name='oneClickLeadFormOpens',
                        type=['null', 'number'],
                        description='Number of one-click lead form opens',
                    ),
                    CacheFieldConfig(
                        name='otherEngagements',
                        type=['null', 'number'],
                        description='Number of other engagements',
                    ),
                    CacheFieldConfig(
                        name='adUnitClicks',
                        type=['null', 'number'],
                        description='Number of ad unit clicks',
                    ),
                    CacheFieldConfig(
                        name='actionClicks',
                        type=['null', 'number'],
                        description='Number of action clicks',
                    ),
                    CacheFieldConfig(
                        name='textUrlClicks',
                        type=['null', 'number'],
                        description='Number of text URL clicks',
                    ),
                    CacheFieldConfig(
                        name='commentLikes',
                        type=['null', 'number'],
                        description='Number of comment likes',
                    ),
                    CacheFieldConfig(
                        name='sends',
                        type=['null', 'number'],
                        description='Number of sends (InMail)',
                    ),
                    CacheFieldConfig(
                        name='opens',
                        type=['null', 'number'],
                        description='Number of opens (InMail)',
                    ),
                    CacheFieldConfig(
                        name='downloadClicks',
                        type=['null', 'number'],
                        description='Number of download clicks',
                    ),
                    CacheFieldConfig(
                        name='pivotValues',
                        type=['null', 'array'],
                        description='Pivot values (URNs) for this analytics record',
                    ),
                    CacheFieldConfig(
                        name='start_date',
                        type=['null', 'string'],
                        description='Start date of the ad analytics data',
                    ),
                    CacheFieldConfig(
                        name='end_date',
                        type=['null', 'string'],
                        description='End date of the ad analytics data',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='ad_creative_analytics',
                suggested=True,
                x_airbyte_name='ad_creative_analytics',
                fields=[
                    CacheFieldConfig(
                        name='impressions',
                        type=['null', 'number'],
                        description='Number of times the ad was shown',
                    ),
                    CacheFieldConfig(
                        name='clicks',
                        type=['null', 'number'],
                        description='Number of clicks on the ad',
                    ),
                    CacheFieldConfig(
                        name='costInLocalCurrency',
                        type=['null', 'number'],
                        description='Total cost in the accounts local currency',
                    ),
                    CacheFieldConfig(
                        name='costInUsd',
                        type=['null', 'number'],
                        description='Total cost in USD',
                    ),
                    CacheFieldConfig(
                        name='likes',
                        type=['null', 'number'],
                        description='Number of likes',
                    ),
                    CacheFieldConfig(
                        name='shares',
                        type=['null', 'number'],
                        description='Number of shares',
                    ),
                    CacheFieldConfig(
                        name='comments',
                        type=['null', 'number'],
                        description='Number of comments',
                    ),
                    CacheFieldConfig(
                        name='reactions',
                        type=['null', 'number'],
                        description='Number of reactions',
                    ),
                    CacheFieldConfig(
                        name='follows',
                        type=['null', 'number'],
                        description='Number of follows',
                    ),
                    CacheFieldConfig(
                        name='totalEngagements',
                        type=['null', 'number'],
                        description='Total number of engagements',
                    ),
                    CacheFieldConfig(
                        name='landingPageClicks',
                        type=['null', 'number'],
                        description='Number of landing page clicks',
                    ),
                    CacheFieldConfig(
                        name='companyPageClicks',
                        type=['null', 'number'],
                        description='Number of company page clicks',
                    ),
                    CacheFieldConfig(
                        name='externalWebsiteConversions',
                        type=['null', 'number'],
                        description='Number of conversions on external websites',
                    ),
                    CacheFieldConfig(
                        name='externalWebsitePostClickConversions',
                        type=['null', 'number'],
                        description='Post-click conversions on external websites',
                    ),
                    CacheFieldConfig(
                        name='externalWebsitePostViewConversions',
                        type=['null', 'number'],
                        description='Post-view conversions on external websites',
                    ),
                    CacheFieldConfig(
                        name='conversionValueInLocalCurrency',
                        type=['null', 'number'],
                        description='Conversion value in local currency',
                    ),
                    CacheFieldConfig(
                        name='approximateMemberReach',
                        type=['null', 'number'],
                        description='Approximate unique member reach',
                    ),
                    CacheFieldConfig(
                        name='cardClicks',
                        type=['null', 'number'],
                        description='Number of carousel card clicks',
                    ),
                    CacheFieldConfig(
                        name='cardImpressions',
                        type=['null', 'number'],
                        description='Number of carousel card impressions',
                    ),
                    CacheFieldConfig(
                        name='videoStarts',
                        type=['null', 'number'],
                        description='Number of video starts',
                    ),
                    CacheFieldConfig(
                        name='videoViews',
                        type=['null', 'number'],
                        description='Number of video views',
                    ),
                    CacheFieldConfig(
                        name='videoFirstQuartileCompletions',
                        type=['null', 'number'],
                        description='Number of times video played to 25%',
                    ),
                    CacheFieldConfig(
                        name='videoMidpointCompletions',
                        type=['null', 'number'],
                        description='Number of times video played to 50%',
                    ),
                    CacheFieldConfig(
                        name='videoThirdQuartileCompletions',
                        type=['null', 'number'],
                        description='Number of times video played to 75%',
                    ),
                    CacheFieldConfig(
                        name='videoCompletions',
                        type=['null', 'number'],
                        description='Number of times video played to 100%',
                    ),
                    CacheFieldConfig(
                        name='fullScreenPlays',
                        type=['null', 'number'],
                        description='Number of full screen video plays',
                    ),
                    CacheFieldConfig(
                        name='oneClickLeads',
                        type=['null', 'number'],
                        description='Number of one-click leads',
                    ),
                    CacheFieldConfig(
                        name='oneClickLeadFormOpens',
                        type=['null', 'number'],
                        description='Number of one-click lead form opens',
                    ),
                    CacheFieldConfig(
                        name='otherEngagements',
                        type=['null', 'number'],
                        description='Number of other engagements',
                    ),
                    CacheFieldConfig(
                        name='adUnitClicks',
                        type=['null', 'number'],
                        description='Number of ad unit clicks',
                    ),
                    CacheFieldConfig(
                        name='actionClicks',
                        type=['null', 'number'],
                        description='Number of action clicks',
                    ),
                    CacheFieldConfig(
                        name='textUrlClicks',
                        type=['null', 'number'],
                        description='Number of text URL clicks',
                    ),
                    CacheFieldConfig(
                        name='commentLikes',
                        type=['null', 'number'],
                        description='Number of comment likes',
                    ),
                    CacheFieldConfig(
                        name='sends',
                        type=['null', 'number'],
                        description='Number of sends (InMail)',
                    ),
                    CacheFieldConfig(
                        name='opens',
                        type=['null', 'number'],
                        description='Number of opens (InMail)',
                    ),
                    CacheFieldConfig(
                        name='downloadClicks',
                        type=['null', 'number'],
                        description='Number of download clicks',
                    ),
                    CacheFieldConfig(
                        name='pivotValues',
                        type=['null', 'array'],
                        description='Pivot values (URNs) for this analytics record',
                    ),
                    CacheFieldConfig(
                        name='start_date',
                        type=['null', 'string'],
                        description='Start date of the ad analytics data',
                    ),
                    CacheFieldConfig(
                        name='end_date',
                        type=['null', 'string'],
                        description='End date of the ad analytics data',
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'accounts': [
            'id',
            'name',
            'currency',
            'status',
            'type',
            'reference',
            'test',
            'notifiedOnCampaignOptimization',
            'notifiedOnCreativeApproval',
            'notifiedOnCreativeRejection',
            'notifiedOnEndOfCampaign',
            'notifiedOnNewFeaturesEnabled',
            'servingStatuses',
            'servingStatuses[]',
            'version',
            'version.versionTag',
        ],
        'account_users': ['account', 'user', 'role'],
        'campaigns': [
            'id',
            'name',
            'account',
            'campaignGroup',
            'status',
            'type',
            'costType',
            'format',
            'objectiveType',
            'optimizationTargetType',
            'creativeSelection',
            'pacingStrategy',
            'audienceExpansionEnabled',
            'offsiteDeliveryEnabled',
            'storyDeliveryEnabled',
            'test',
            'associatedEntity',
            'dailyBudget',
            'dailyBudget.amount',
            'dailyBudget.currencyCode',
            'totalBudget',
            'totalBudget.amount',
            'totalBudget.currencyCode',
            'unitCost',
            'unitCost.amount',
            'unitCost.currencyCode',
            'runSchedule',
            'runSchedule.start',
            'runSchedule.end',
            'locale',
            'locale.country',
            'locale.language',
            'servingStatuses',
            'servingStatuses[]',
            'version',
            'version.versionTag',
        ],
        'campaign_groups': [
            'id',
            'name',
            'account',
            'status',
            'test',
            'backfilled',
            'totalBudget',
            'totalBudget.amount',
            'totalBudget.currencyCode',
            'runSchedule',
            'runSchedule.start',
            'runSchedule.end',
            'servingStatuses',
            'servingStatuses[]',
            'allowedCampaignTypes',
            'allowedCampaignTypes[]',
        ],
        'creatives': [
            'id',
            'name',
            'account',
            'campaign',
            'intendedStatus',
            'isServing',
            'isTest',
            'createdAt',
            'createdBy',
            'lastModifiedAt',
            'lastModifiedBy',
            'content',
            'servingHoldReasons',
            'servingHoldReasons[]',
        ],
        'conversions': [
            'id',
            'name',
            'account',
            'type',
            'attributionType',
            'enabled',
            'created',
            'lastModified',
            'postClickAttributionWindowSize',
            'viewThroughAttributionWindowSize',
            'campaigns',
            'campaigns[]',
            'associatedCampaigns',
            'associatedCampaigns[]',
            'imagePixelTag',
            'value',
            'value.amount',
            'value.currencyCode',
        ],
        'ad_campaign_analytics': [
            'impressions',
            'clicks',
            'costInLocalCurrency',
            'costInUsd',
            'likes',
            'shares',
            'comments',
            'reactions',
            'follows',
            'totalEngagements',
            'landingPageClicks',
            'companyPageClicks',
            'externalWebsiteConversions',
            'externalWebsitePostClickConversions',
            'externalWebsitePostViewConversions',
            'conversionValueInLocalCurrency',
            'approximateMemberReach',
            'cardClicks',
            'cardImpressions',
            'videoStarts',
            'videoViews',
            'videoFirstQuartileCompletions',
            'videoMidpointCompletions',
            'videoThirdQuartileCompletions',
            'videoCompletions',
            'fullScreenPlays',
            'oneClickLeads',
            'oneClickLeadFormOpens',
            'otherEngagements',
            'adUnitClicks',
            'actionClicks',
            'textUrlClicks',
            'commentLikes',
            'sends',
            'opens',
            'downloadClicks',
            'pivotValues',
            'pivotValues[]',
            'start_date',
            'end_date',
        ],
        'ad_creative_analytics': [
            'impressions',
            'clicks',
            'costInLocalCurrency',
            'costInUsd',
            'likes',
            'shares',
            'comments',
            'reactions',
            'follows',
            'totalEngagements',
            'landingPageClicks',
            'companyPageClicks',
            'externalWebsiteConversions',
            'externalWebsitePostClickConversions',
            'externalWebsitePostViewConversions',
            'conversionValueInLocalCurrency',
            'approximateMemberReach',
            'cardClicks',
            'cardImpressions',
            'videoStarts',
            'videoViews',
            'videoFirstQuartileCompletions',
            'videoMidpointCompletions',
            'videoThirdQuartileCompletions',
            'videoCompletions',
            'fullScreenPlays',
            'oneClickLeads',
            'oneClickLeadFormOpens',
            'otherEngagements',
            'adUnitClicks',
            'actionClicks',
            'textUrlClicks',
            'commentLikes',
            'sends',
            'opens',
            'downloadClicks',
            'pivotValues',
            'pivotValues[]',
            'start_date',
            'end_date',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all my LinkedIn ad accounts',
            'Show me all campaigns in my ad account',
            'List all campaign groups',
            'Show me the creatives for my campaigns',
            'List all conversions configured for my ad accounts',
            'Show me account users for my LinkedIn ads accounts',
            'Show me campaign analytics for my LinkedIn ad campaigns',
            'Show me creative analytics for my ad creatives',
        ],
        context_store_search=[
            'Which campaigns have the highest click-through rate?',
            'What is the total ad spend across all campaigns this month?',
            'Show me campaigns with status ACTIVE',
            'Which creatives have the most impressions?',
            'Compare campaign performance by cost type',
        ],
        search=[
            'Which campaigns have the highest click-through rate?',
            'What is the total ad spend across all campaigns this month?',
            'Show me campaigns with status ACTIVE',
            'Which creatives have the most impressions?',
            'Compare campaign performance by cost type',
        ],
        unsupported=[
            'Create a new campaign',
            'Update campaign budgets',
            'Delete an ad creative',
            'Pause a campaign',
        ],
    ),
)